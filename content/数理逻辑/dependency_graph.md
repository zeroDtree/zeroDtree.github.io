```mermaid
graph TD
1["数理逻辑/一阶逻辑"] --> 0["数理逻辑/一阶逻辑演算"]
2["数理逻辑/命题逻辑演算"] --> 1["数理逻辑/一阶逻辑"]
3["数理逻辑/命题逻辑"] --> 2["数理逻辑/命题逻辑演算"]
5["朴素集合论/naive-set-theory-2"] --> 3["数理逻辑/命题逻辑"]
classDef leaf fill:#fde68a,stroke:#b45309
class 0 leaf
classDef root fill:#bfdbfe,stroke:#1d4ed8
class 4 root
classDef externalRoot fill:#fecaca,stroke:#b91c1c
class 5 externalRoot
```