# Probability and statistics: Solutions

- Under a valid continuous null, p-values are Uniform(0,1): flat PDF and CDF `F(p)=p`. Roughly 5% fall below 0.05.
- `sqrt(n)(hat(theta)-theta) -> N(0,sigma^2)` implies `hat(theta) ≈ N(theta, sigma^2/n)`.
- For log odds, `g'(p)=1/[p(1-p)]`, so the delta-method variance is `1/[n p(1-p)]`.
- A second-order example is `g(x)=x^2` at `theta=0`; the first derivative vanishes and `n*hat(theta)^2/sigma^2` approaches chi-square(1).
- `n-1` appears because estimating the mean consumes one degree of freedom and `E[sum(X_i-Xbar)^2]=(n-1)sigma^2`.
- Replacing sigma with random `S` produces a t ratio; as degrees of freedom increase, `S` concentrates near sigma.

Bootstrap median:

```python
def bootstrap_statistic(x, statistic, B=10_000, seed=0):
    rng = np.random.default_rng(seed)
    x = np.asarray(x)
    stats = np.empty(B)
    for b in range(B):
        stats[b] = statistic(rng.choice(x, len(x), replace=True))
    return stats

boot = bootstrap_statistic(x, np.median)
theta = np.median(x)
percentile_ci = np.quantile(boot, [0.025, 0.975])
lo, hi = np.quantile(boot, [0.025, 0.975])
basic_ci = np.array([2*theta-hi, 2*theta-lo])
```

Bootstrap regression:

```python
import statsmodels.api as sm

def x1_coef(df):
    return sm.OLS(df["y"], sm.add_constant(df[["x1","x2"]])).fit().params["x1"]

rng = np.random.default_rng(0)
coefs = np.empty(5000)
for b in range(len(coefs)):
    idx = rng.integers(0, len(df_reg), len(df_reg))
    coefs[b] = x1_coef(df_reg.iloc[idx])
ci = np.quantile(coefs, [0.025,0.975])
```

Permutation test:

```python
def permutation_test_mean(treatment, control, B=20_000, seed=0):
    t, c = np.asarray(treatment), np.asarray(control)
    observed = t.mean()-c.mean()
    pooled, n_t = np.concatenate([t,c]), len(t)
    rng = np.random.default_rng(seed)
    extreme = 0
    for _ in range(B):
        p = rng.permutation(pooled)
        diff = p[:n_t].mean()-p[n_t:].mean()
        extreme += abs(diff) >= abs(observed)
    return observed, (extreme+1)/(B+1)
```

For 100 null tests at 5%: expected false positives = 5; probability of at least one = `1-.95**100 ≈ .994`; Bonferroni alpha = `.0005`. FDR controls the expected false fraction among discoveries.
