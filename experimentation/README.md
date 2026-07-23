# Experimentation and causal inference: Practice problems

```python
def make_experiment(seed: int = 21, n: int = 20000):
    rng = np.random.default_rng(seed)
    pre = rng.normal(50, 15, n)
    treatment = rng.integers(0, 2, n)
    effect = 2.0 + 0.03*(pre - 50)
    outcome = 10 + 0.7*pre + treatment*effect + rng.normal(0, 12, n)
    return pd.DataFrame({"user_id": np.arange(n), "treatment": treatment,
                         "pre_metric": pre, "outcome": outcome})

exp = make_experiment()
```

1. Difference-in-means ATE and standard error.
2. CUPED: estimate theta, construct adjusted outcome, and compare standard errors.
3. Simulate 1,000 A/A tests and inspect p-value calibration.
4. Approximate sample size per arm for 10% baseline conversion, 1 percentage-point lift, alpha 5%, and power 80%.
5. Diagnose a treatment effect that is large in week 1 and near zero by week 4.
6. Construct Simpson's paradox with mobile and desktop.
7. Debug a nominal 50/50 test with 52.5% treatment in the analyzed sample.
8. Explain bias from analyzing only post-assignment clickers.
9. Design a cluster-randomized experiment under interference.
10. Generate panel data and estimate a two-way fixed-effects DiD; discuss parallel trends, event studies, and staggered adoption.
11. Explain synthetic-control donor weighting, fit, placebo tests, and inference limitations.
