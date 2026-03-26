---
title: 有用的hook
---

- [Hook](#hook)
- [enable\_grad / no\_grad 测试](#enable_grad--no_grad-测试)
	- [register\_post\_accumulate\_grad\_hook \&\& saved\_tensors\_hooks](#register_post_accumulate_grad_hook--saved_tensors_hooks)
	- [register\_forward\_pre\_hook](#register_forward_pre_hook)
	- [register\_full\_backward\_pre\_hook](#register_full_backward_pre_hook)
	- [register\_full\_backward\_hook](#register_full_backward_hook)
	- [register\_forward\_hook](#register_forward_hook)

## Hook

涉及反向传播的hook一般会禁用梯度，否则一般不禁用梯度

注册hook的函数名带`pre`的表示在某个过程前，否则一般表示某个过程后。

- [torch.Tensor.register_post_accumulate_grad_hook](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.register_post_accumulate_grad_hook.html#torch-tensor-register-post-accumulate-grad-hook)
  hook内默认禁用梯度

- [torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook)](https://docs.pytorch.org/docs/stable/autograd.html#torch.autograd.graph.saved_tensors_hooks)
  hook内默认禁用梯度
- 模块
  - [torch.nn.Module.register_forward_pre_hook](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_forward_pre_hook)
    hook内默认不禁用梯度
  - [orch.nn.Module.register_forward_hook](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_forward_hook)
    hook内默认不禁用梯度
- 操作模块反向传播过程中对输入输出的梯度
  - [torch.nn.Module.register_full_backward_pre_hook](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_pre_hook)
    hook内默认禁用梯度
  - [torch.nn.Module.register_full_backward_hook](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module.register_full_backward_hook)
    hook内默认禁用梯度


## enable_grad / no_grad 测试

### register_post_accumulate_grad_hook && saved_tensors_hooks
```python
import torch

# -----------------------------
# 1️⃣ 测试 register_post_accumulate_grad_hook
# -----------------------------
x = torch.tensor([1., 2., 3.], requires_grad=True)
lr = 0.01

def post_acc_hook(param):
    print("Inside post_accumulate_grad_hook, grad enabled:", torch.is_grad_enabled())
    print("param.grad:", param.grad)

# 注册 hook
handle = x.register_post_accumulate_grad_hook(post_acc_hook)

# 模拟 backward
y = x.sum()
y.backward()
# hook 会在这里打印 grad_enabled 和 param.grad

handle.remove()  # 移除 hook

print("\n" + "-"*40 + "\n")

# -----------------------------
# 2️⃣ 测试 saved_tensors_hooks
# -----------------------------
def pack_hook(t):
    print("Inside pack_hook, grad enabled:", torch.is_grad_enabled())
    return t.detach()  # 官方推荐 detach 避免循环引用

def unpack_hook(packed):
    print("Inside unpack_hook, grad enabled:", torch.is_grad_enabled())
    return packed

a = torch.ones(3, requires_grad=True)
b = torch.ones(3, requires_grad=True) * 2

with torch.autograd.graph.saved_tensors_hooks(pack_hook, unpack_hook):
    c = a * b  # 这里会触发 pack_hook

c.sum().backward()  # 这里会触发 unpack_hook
```
输出：
```
Inside post_accumulate_grad_hook, grad enabled: False
param.grad: tensor([1., 1., 1.])

----------------------------------------

Inside pack_hook, grad enabled: False
Inside pack_hook, grad enabled: False
Inside unpack_hook, grad enabled: False
Inside unpack_hook, grad enabled: False
```

### register_forward_pre_hook

```python
import torch
import torch.nn as nn

# Define a simple model
class MyModel(nn.Module):
    def forward(self, x):
        print("Inside forward, grad enabled:", torch.is_grad_enabled())
        return x * 2

model = MyModel()

# Define hook
def pre_hook(module, args):
    print("Inside hook, grad enabled:", torch.is_grad_enabled())
    return args

# Register hook
handle = model.register_forward_pre_hook(pre_hook)

# Test 1: default (grad enabled)
x = torch.tensor([1.0], requires_grad=True)
print("=== With grad ===")
out = model(x)

# Test 2: no_grad context
print("\n=== With torch.no_grad ===")
with torch.no_grad():
    out = model(x)

# Remove hook
handle.remove()
```
输出
```
=== With grad ===
Inside hook, grad enabled: True
Inside forward, grad enabled: True

=== With torch.no_grad ===
Inside hook, grad enabled: False
Inside forward, grad enabled: False
```

### register_full_backward_pre_hook

```
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def forward(self, x):
        return x * 2

model = MyModel()

def backward_pre_hook(module, grad_output):
    print("Inside backward_pre_hook:")
    print("  grad enabled:", torch.is_grad_enabled())
    print("  grad_output:", grad_output)
    return grad_output

handle = model.register_full_backward_pre_hook(backward_pre_hook)

x = torch.tensor([1.0], requires_grad=True)
y = model(x)

loss = y.sum()

print("=== Backward ===")
loss.backward()

handle.remove()
```
输出
```
=== Backward ===
Inside backward_pre_hook:
  grad enabled: False
  grad_output: (tensor([1.]),)
```

### register_full_backward_hook

```
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def forward(self, x):
        return x * 2

model = MyModel()

def backward_hook(module, grad_input, grad_output):
    print("Inside backward_hook:")
    print("  grad enabled:", torch.is_grad_enabled())
    
    # 检查 grad_input / grad_output 是否带 grad
    for i, g in enumerate(grad_input):
        if g is not None:
            print(f"  grad_input[{i}].requires_grad:", g.requires_grad)
    
    for i, g in enumerate(grad_output):
        if g is not None:
            print(f"  grad_output[{i}].requires_grad:", g.requires_grad)

    return grad_input  # 不修改

handle = model.register_full_backward_hook(backward_hook)

x = torch.tensor([1.0], requires_grad=True)
y = model(x)

loss = y.sum()

print("=== Backward ===")
loss.backward()

handle.remove()

# === Backward ===
# Inside backward_hook:
#   grad enabled: False
#   grad_input[0].requires_grad: False
#   grad_output[0].requires_grad: False
```

### register_forward_hook

```python
import torch
import torch.nn as nn

class MyModel(nn.Module):
    def forward(self, x):
        print("Inside forward, grad enabled:", torch.is_grad_enabled())
        return x * 2

model = MyModel()

def forward_hook(module, args, output):
    print("Inside forward_hook:")
    print("  grad enabled:", torch.is_grad_enabled())
    print("  output.requires_grad:", output.requires_grad)
    return output

handle = model.register_forward_hook(forward_hook)

x = torch.tensor([1.0], requires_grad=True)

# ✅ 情况1：默认（开启grad）
print("=== With grad ===")
y = model(x)

# ❌ 情况2：no_grad
print("\n=== With torch.no_grad ===")
with torch.no_grad():
    y = model(x)

handle.remove()

# === With grad ===
# Inside forward, grad enabled: True
# Inside forward_hook:
#   grad enabled: True
#   output.requires_grad: True

# === With torch.no_grad ===
# Inside forward, grad enabled: False
# Inside forward_hook:
#   grad enabled: False
#   output.requires_grad: False
```