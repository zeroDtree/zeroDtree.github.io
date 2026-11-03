```mermaid
graph TD
1["随机过程/扩散模型/index"] --> 0["随机过程/扩散模型/离散状态/离散时间扩散"]
2["随机过程/马尔可夫过程/离散时间马尔可夫链"] --> 0["随机过程/扩散模型/离散状态/离散时间扩散"]
classDef leaf fill:#fde68a,stroke:#b45309
class 0 leaf
classDef externalRoot fill:#fecaca,stroke:#b91c1c
class 2 externalRoot
classDef foundationRoot fill:#bbf7d0,stroke:#15803d
class 1 foundationRoot
click 0 "/随机过程/扩散模型/离散状态/离散时间扩散" "随机过程/扩散模型/离散状态/离散时间扩散"
click 1 "/随机过程/扩散模型/index" "随机过程/扩散模型/index"
click 2 "/随机过程/马尔可夫过程/离散时间马尔可夫链" "随机过程/马尔可夫过程/离散时间马尔可夫链"
```