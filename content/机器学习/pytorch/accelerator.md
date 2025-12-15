---
title: accelerator
---

## 梯度累计-代码片段分析

只关注梯度累计和分布式部分。

```python
    def train_a_step(self, batch: Dict[str, Any]):
        self.trigger_callbacks(event=CallbackEvent.STEP_START, batch=batch)
        model: torch.nn.Module = self.model
        optimizer = self.optimizer
        scheduler = self.scheduler
        logger = self.logger
        model.train()

        result = {}

        should_sync = (
            self.training_state.current_global_step + 1
        ) % self.training_config.gradient_accumulation_steps == 0
        ctx = self.accelerator.no_sync(model=model) if not should_sync else nullcontext()
        with ctx:
            loss = self.compute_loss(model, batch)
            self.accelerator.backward(loss)
        if should_sync:
            result["grad_norm_pre_clip"] = self.observer.get_gradient_norm()
            self.gradient_clip()
            result["grad_norm_post_clip"] = self.observer.get_gradient_norm()
            # print(f"grad_norm_pre_clip = {result['grad_norm_pre_clip']}, grad_norm_post_clip = {result['grad_norm_post_clip']}")
            optimizer.step()
            optimizer.zero_grad()

        if scheduler is not None:
            scheduler.step()

        result["loss"] = loss.item()
        result["weight_norm"] = self.observer.get_weight_norm()
        result["lr"] = scheduler.get_last_lr()[0]
        result["global_step"] = self.training_state.current_global_step

        # Only log on local main process
        if self._can_log(flag="steps") and self.accelerator.is_local_main_process:
            logger.info(
                f"[Training] Epoch {self.training_state.current_epoch}, Step {self.training_state.current_step_in_epoch}, Loss {loss.item()}"
            )
            wandb.log(result, step=self.training_state.current_global_step)

        self.trigger_callbacks(event=CallbackEvent.STEP_END, batch=batch)
        return result
```

在每个设备（显卡）上，`accelerator`会将反向传播的梯度自动处以`gradient_accumulation_steps`

PyTorch adds hooks to the forward and backward method of your PyTorch model when training in a distributed setup.

In DDP (distributed data parallel), the specific order in which processes are performed and ran are expected at specific points and these must also occur at roughly the same time before moving on.

The most direct example is when update model parameters through optimizer.step(). Without gradient accumulation, all instances of the model need to have updated their gradients computed, collated, and updated before moving on to the next batch of data. When performing gradient accumulation, you accumulate n loss gradients and skip optimizer.step() until n batches have been reached. As all training processes only need to synchronize by the time optimizer.step() is called, without any modification to your training step, this needless inter-process communication can cause a significant slowdown.

使用`accelerator.no_sync(model=model)`上下文包裹住梯度累计时的前向传播和反向传播部分，可以避免不必要的通信。

## 学习率调度-代码片段分析

只关注设置lr_scheduler的总步数。

下面这个代码片段假定`scheduler`之后会被`accelerator.prepare`包裹

```python
def get_learing_rate_scheduler(optimizer, accelerator: Accelerator, train_set, cfg: DictConfig, inplace: bool = True):
    from ls_mlkit.scheduler.lr_scheduler_factory import get_lr_scheduler

    per_device_batch_size = cfg.train.batch_size
    real_batch_size = cfg.train.get(
        "real_batch_size", cfg.train.batch_size * cfg.train.gradient_accumulation_steps * accelerator.num_processes
    )
    effective_batch_size = accelerator.num_processes * cfg.train.batch_size
    assert real_batch_size % effective_batch_size == 0, "real_batch_size must be divisible by effective_batch_size"
    gradient_accumulation_steps = real_batch_size // effective_batch_size

    if cfg.train.train_strategy in ["epochs"]:
        n_training_steps = math.ceil(1.0 * len(train_set) * cfg.train.n_epochs / per_device_batch_size)
    elif cfg.train.train_strategy in ["steps"]:
        n_training_steps = cfg.train.n_steps
    else:
        raise ValueError(f"Train Strategy {cfg.train.train_strategy} is not supported")
    if inplace:
        cfg.train.n_steps = n_training_steps
        cfg.train.real_batch_size = real_batch_size
        cfg.train.gradient_accumulation_steps = gradient_accumulation_steps

    lr_scheduler = get_lr_scheduler(
        optimizer=optimizer,
        n_warmup_steps=cfg.train.n_warmup_steps,
        n_training_steps=(
            n_training_steps * accelerator.num_processes if cfg.train.train_strategy == "steps" else n_training_steps
        ),
        lr_scheduler_type=cfg.train.lr_scheduler_type,
    )
    return lr_scheduler
```

设置`n_training_steps`是的根本原则：`n_training_steps`$=$ 一共会有多少个`per_device_bacth`被处理。

- 对于按`epochs`训练：一共有`math.ceil(1.0 * len(train_set) * cfg.train.n_epochs / per_device_batch_size)`个。可以这样考虑，既然是按`per_device_batch`,那直接考虑没有分布式会有多少个batch即可。
- 对于按`steps`训练：一共有`n_training_steps * accelerator.num_processes`个, 有几张卡就乘几倍。

## 参考资料

```
https://huggingface.co/docs/accelerate/concept_guides/gradient_synchronization
```
