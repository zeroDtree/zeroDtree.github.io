```mermaid
%%{init: {'flowchart': {'curve': 'stepAfter'}}}%%
graph TD
1["机器学习/机器学习的分类"] --> 0["机器学习/generative-model-introduction"]
3["机器学习/VAE"] --> 2["机器学习/VQ-VAE"]
4["机器学习/Straight-Through-Estimator"] --> 2["机器学习/VQ-VAE"]
6["机器学习/diffusion-inpainting(1)"] --> 5["机器学习/repaint"]
8["数学/抽象代数/群论(群作用)"] --> 7["机器学习/SE(3)"]
10["机器学习/normalizing-flow"] --> 9["机器学习/neural-ode"]
12["机器学习/广义特征值"] --> 11["机器学习/广义Rayleigh商"]
0["机器学习/generative-model-introduction"] --> 3["机器学习/VAE"]
3["机器学习/VAE"] --> 13["机器学习/ddpm"]
15["机器学习/posterior_mean"] --> 14["机器学习/DPS"]
17["机器学习/SFA"] --> 16["机器学习/TICA"]
19["机器学习/Dirac分布"] --> 18["机器学习/fourier"]
21["机器学习/大模型轻量化"] --> 20["机器学习/知识蒸馏"]
23["机器学习/强化学习"] --> 22["机器学习/PPO"]
1["机器学习/机器学习的分类"] --> 21["机器学习/大模型轻量化"]
9["机器学习/neural-ode"] --> 24["机器学习/flow-matching"]
1["机器学习/机器学习的分类"] --> 23["机器学习/强化学习"]
25["机器学习/拉格朗日乘子法"] --> 12["机器学习/广义特征值"]
26["机器学习/矩阵微分演算"] --> 12["机器学习/广义特征值"]
27["机器学习/矩阵分解/Cholesky分解"] --> 12["机器学习/广义特征值"]
0["机器学习/generative-model-introduction"] --> 10["机器学习/normalizing-flow"]
11["机器学习/广义Rayleigh商"] --> 17["机器学习/SFA"]
28["数学/数学分析/平方可积"] --> 17["机器学习/SFA"]
21["机器学习/大模型轻量化"] --> 29["机器学习/quantization"]
classDef leaf fill:#fde68a,stroke:#b45309
class 2,5,7,13,14,16,18,20,22,24,29 leaf
classDef root fill:#bfdbfe,stroke:#1d4ed8
class 1,4,6,15,19,25,26,27 root
classDef foundationRoot fill:#bbf7d0,stroke:#15803d
class 8,28 foundationRoot
click 0 "/机器学习/generative-model-introduction" "机器学习/generative-model-introduction"
click 1 "/机器学习/机器学习的分类" "机器学习/机器学习的分类"
click 2 "/机器学习/vq-vae" "机器学习/VQ-VAE"
click 3 "/机器学习/vae" "机器学习/VAE"
click 4 "/机器学习/straight-through-estimator" "机器学习/Straight-Through-Estimator"
click 5 "/机器学习/repaint" "机器学习/repaint"
click 6 "/机器学习/diffusion-inpainting(1)" "机器学习/diffusion-inpainting(1)"
click 7 "/机器学习/se(3)" "机器学习/SE(3)"
click 8 "/数学/抽象代数/群论(群作用)" "数学/抽象代数/群论(群作用)"
click 9 "/机器学习/neural-ode" "机器学习/neural-ode"
click 10 "/机器学习/normalizing-flow" "机器学习/normalizing-flow"
click 11 "/机器学习/广义rayleigh商" "机器学习/广义Rayleigh商"
click 12 "/机器学习/广义特征值" "机器学习/广义特征值"
click 13 "/机器学习/ddpm" "机器学习/ddpm"
click 14 "/机器学习/dps" "机器学习/DPS"
click 15 "/机器学习/posterior_mean" "机器学习/posterior_mean"
click 16 "/机器学习/tica" "机器学习/TICA"
click 17 "/机器学习/sfa" "机器学习/SFA"
click 18 "/机器学习/fourier" "机器学习/fourier"
click 19 "/机器学习/dirac分布" "机器学习/Dirac分布"
click 20 "/机器学习/知识蒸馏" "机器学习/知识蒸馏"
click 21 "/机器学习/大模型轻量化" "机器学习/大模型轻量化"
click 22 "/机器学习/ppo" "机器学习/PPO"
click 23 "/机器学习/强化学习" "机器学习/强化学习"
click 24 "/机器学习/flow-matching" "机器学习/flow-matching"
click 25 "/机器学习/拉格朗日乘子法" "机器学习/拉格朗日乘子法"
click 26 "/机器学习/矩阵微分演算" "机器学习/矩阵微分演算"
click 27 "/机器学习/矩阵分解/cholesky分解" "机器学习/矩阵分解/Cholesky分解"
click 28 "/数学/数学分析/平方可积" "数学/数学分析/平方可积"
click 29 "/机器学习/quantization" "机器学习/quantization"
```