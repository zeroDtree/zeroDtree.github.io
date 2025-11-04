---
title: 正则表达式
---

- [1. 方向定义](#1-方向定义)
- [2. 零宽断言](#2-零宽断言)
- [3. 非捕获组](#3-非捕获组)
- [4. 命名捕获组](#4-命名捕获组)

#### 1. 方向定义

前：$\rightarrow$
后：$\leftarrow$

#### 2. 零宽断言

`(?=pattern)` 零宽正向先行断言(zero-width positive lookahead assertion) 又称正向前瞻
`(?!pattern)` 零宽负向先行断言(zero-width negative lookahead assertion) 又称负向前瞻
`(?<=pattern)` 零宽正向后行断言(zero-width positive lookbehind assertion) 又称正向后瞻
`(?<!pattern)` 零宽负向后行断言(zero-width negative lookbehind assertion) 又称负向后瞻

#### 3. 非捕获组

`(?:...)`

#### 4. 命名捕获组

`(?<name>...)`
