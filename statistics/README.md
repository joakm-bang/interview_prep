# Probability and statistics: Practice problems

1. **Null p-values:** What should the PDF and CDF look like? Diagnose a pileup near zero in A/A tests.
2. **CLT notation:** Rewrite `sqrt(n)(hat(theta)-theta) -> N(0, sigma^2)` as the approximate distribution of `hat(theta)`.
3. **Delta method:** If `Var(hat(p)) = p(1-p)/n`, derive the variance of `log(hat(p)/(1-hat(p)))`.
4. **Second-order Taylor:** Give an example where the first derivative is zero and first-order delta method fails.
5. **Sample variance:** Explain the `n-1` denominator.
6. **Student's t:** Explain why estimating sigma changes the reference distribution and why t approaches normal.
7. **Bootstrap median:** Generate lognormal data and compute percentile and basic 95% intervals.
8. **Bootstrap regression:** Bootstrap the coefficient on `x1` in a two-predictor OLS model.
9. **Permutation test:** Implement a two-sided Monte Carlo difference-in-means test; discuss exchangeability, exact tests, and Fisher's exact test.
10. **Multiple testing:** For 100 null tests at alpha 0.05, calculate expected false positives, probability of at least one, Bonferroni threshold, and explain FDR.

Bootstrap data:

```python
rng = np.random.default_rng(3)
x = rng.lognormal(mean=1.0, sigma=1.1, size=300)

rng = np.random.default_rng(4)
n = 500
df_reg = pd.DataFrame({"x1": rng.normal(size=n), "x2": rng.normal(size=n)})
df_reg["y"] = 1.5 + 2.0*df_reg["x1"] - 0.8*df_reg["x2"] + rng.normal(size=n)
```
