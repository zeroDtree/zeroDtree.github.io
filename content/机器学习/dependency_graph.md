```mermaid
graph TD
1["机器学习/VAE"] --> 0["机器学习/VQ-VAE"]
2["机器学习/Straight-Through-Estimator"] --> 0["机器学习/VQ-VAE"]
4["机器学习/diffusion-inpainting(1)"] --> 3["机器学习/repaint"]
6["数学/抽象代数/群论(群作用)"] --> 5["机器学习/SE(3)"]
8["机器学习/posterior_mean"] --> 7["机器学习/DPS"]
10["机器学习/Dirac分布"] --> 9["机器学习/fourier"]
classDef leaf fill:#fde68a,stroke:#b45309
class 0,3,5,7,9 leaf
classDef root fill:#bfdbfe,stroke:#1d4ed8
class 1,2,4,8,10 root
classDef foundationRoot fill:#bbf7d0,stroke:#15803d
class 6 foundationRoot
click 0 "/机器学习/vq-vae" "机器学习/VQ-VAE"
click 1 "/机器学习/vae" "机器学习/VAE"
click 2 "/机器学习/straight-through-estimator" "机器学习/Straight-Through-Estimator"
click 3 "/机器学习/repaint" "机器学习/repaint"
click 4 "/机器学习/diffusion-inpainting(1)" "机器学习/diffusion-inpainting(1)"
click 5 "/机器学习/se(3)" "机器学习/SE(3)"
click 6 "/数学/抽象代数/群论(群作用)" "数学/抽象代数/群论(群作用)"
click 7 "/机器学习/dps" "机器学习/DPS"
click 8 "/机器学习/posterior_mean" "机器学习/posterior_mean"
click 9 "/机器学习/fourier" "机器学习/fourier"
click 10 "/机器学习/dirac分布" "机器学习/Dirac分布"
```