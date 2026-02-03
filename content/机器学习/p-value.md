---
title: p-value
---

In statistics, every conjecture concerning the unknown probability distribution of a collection of random variables representing the observed data X in some study is called a statistical hypothesis. If we state one hypothesis only and the aim of the statistical test is to see whether this hypothesis is tenable, but not to investigate other specific hypotheses, then such a test is called a **null hypothesis test**.

The p-value is used in the context of null hypothesis testing in order to quantify the **statistical significance** of a result, the result being the observed value of the chosen statistic $T$, The lower the p-value is, the lower the probability of getting that result if the null hypothesis were true. A result is said to be statistically significant if it allows us to reject the null hypothesis. All other things being equal, smaller p-values are taken as stronger evidence against the null hypothesis.

## Definition of p-value

The **p-value** is the probability under the null hypothesis of obtaining a real-valued test statistic at least as extreme as the one obtained.

Consider an observed test statistic $t$ from an unknown distribution $T$. Then the p-value $p$ is the prior probability of observing a test-statistic value at least as "extreme" as $t$ if the null hypothesis $H_0$ were true.

Formally:

- **One-sided right-tail test**:

  $$
  p = \Pr(T \geq t \mid H_0)
  $$

- **One-sided left-tail test**:

  $$
  p = \Pr(T \leq t \mid H_0)
  $$

- **Two-sided test**:
  $$
  p = 2 \min \{ \Pr(T \geq t \mid H_0), \Pr(T \leq t \mid H_0) \}
  $$

If the distribution of $T$ is symmetric about zero:

$$
p = \Pr(|T| \geq |t| \mid H_0)
$$

In a significance test, the null hypothesis $H_0$ is rejected if the p-value is less than to a predefined threshold value $\alpha$, which is referred to as the alpha level or **significance level**. $\alpha$ is not derived from the data, but rather is set by the researcher before examining the data. $\alpha$ is commonly set to 0.05
