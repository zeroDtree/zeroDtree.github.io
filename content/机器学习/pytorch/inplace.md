---
title: inplace
---

## to

module.to 是inplace的
tensor.to 不是inplace的

```python
import torch
import torch.nn as nn

# ===== 选择设备（Mac 可能是 MPS）=====
if torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print(f"Using device: {device}")
print("=" * 50)

# ================================
# 1️⃣ 验证 tensor.to()
# ================================
print("Test 1: tensor.to() 是否 in-place")

x = torch.randn(2, 2)
y = x.to(device)

print("x device:", x.device)
print("y device:", y.device)
print("x is y:", x is y)  # ❌ 应该是 False

# 再测试“相同设备”情况
z = x.to(x.device)
print("z is x (same device):", z is x)  # 可能 True（优化）

print("=" * 50)


# ================================
# 2️⃣ 验证 module.to()
# ================================
print("Test 2: module.to() 是否 in-place")

model = nn.Linear(2, 2)

print("Before:")
print("model weight device:", model.weight.device)

returned_model = model.to(device)

print("\nAfter:")
print("model weight device:", model.weight.device)
print("returned_model weight device:", returned_model.weight.device)

print("model is returned_model:", model is returned_model)  # ✅ True

print("=" * 50)


# ================================
# 3️⃣ 验证 tensor.to() 不赋值是否无效
# ================================
print("Test 3: tensor.to() 不赋值")

a = torch.randn(2, 2)

print("Before:", a.device)

a.to(device)  # ❌ 没接返回值

print("After a.to(device) without assignment:", a.device)  # 还是原设备

# 正确写法
a = a.to(device)
print("After correct assignment:", a.device)

print("=" * 50)


# ================================
# 4️⃣ 验证 module.to() 不需要赋值
# ================================
print("Test 4: module.to() 不赋值")

model2 = nn.Linear(2, 2)

print("Before:", model2.weight.device)

model2.to(device)  # ✅ 不接返回值

print("After:", model2.weight.device)

print("=" * 50)


# Using device: mps
# ==================================================
# Test 1: tensor.to() 是否 in-place
# x device: cpu
# y device: mps:0
# x is y: False
# z is x (same device): True
# ==================================================
# Test 2: module.to() 是否 in-place
# Before:
# model weight device: cpu

# After:
# model weight device: mps:0
# returned_model weight device: mps:0
# model is returned_model: True
# ==================================================
# Test 3: tensor.to() 不赋值
# Before: cpu
# After a.to(device) without assignment: cpu
# After correct assignment: mps:0
# ==================================================
# Test 4: module.to() 不赋值
# Before: cpu
# After: mps:0
# ==================================================
```
