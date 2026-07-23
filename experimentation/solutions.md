# Experimentation and causal inference: Solutions

Difference in means and CUPED:

```python
def diff_and_se(df, outcome):
    t = df.loc[df.treatment.eq(1), outcome]
    c = df.loc[df.treatment.eq(0), outcome]
    return t.mean()-c.mean(), np.sqrt(t.var(ddof=1)/len(t) + c.var(ddof=1)/len(c))

raw = diff_and_se(exp, "outcome")
theta = np.cov(exp["outcome"], exp["pre_metric"], ddof=1)[0,1] / np.var(exp["pre_metric"], ddof=1)
exp["outcome_cuped"] = exp["outcome"] - theta*(exp["pre_metric"]-exp["pre_metric"].mean())
adjusted = diff_and_se(exp, "outcome_cuped")
```

CUPED preserves unbiasedness because randomization makes treatment independent of the centered pre-treatment covariate.

A/A simulation:

```python
from scipy.stats import ttest_ind
rng = np.random.default_rng(1)
pvals = []
for _ in range(1000):
    y = rng.normal(size=4000)
    z = rng.integers(0,2,len(y))
    pvals.append(ttest_ind(y[z==1], y[z==0], equal_var=False).pvalue)
np.mean(np.array(pvals) < .05)
```

Power: for 10% versus 11%, alpha 5%, power 80%, the normal approximation gives roughly 14,700–15,000 users per arm.

Diagnostic summaries:

- **Novelty:** estimate effects by time since exposure, stable cohort, and repeat use; audit logging and traffic composition.
- **Simpson's paradox:** aggregate arm rates use different subgroup weights. Reweight to a common platform mix.
- **SRM:** chi-square observed versus expected counts; inspect assignment, exposure logs, duplicates, eligibility, joins, platform/version, post-assignment filters, and backfills.
- **Triggered analysis:** conditioning on a treatment-affected click selects different latent populations. Prefer ITT or a pre-treatment trigger.
- **Interference:** randomize clusters, estimate cluster-assignment effects, and use cluster-robust SEs. Cross-cluster spillovers remain a threat.

DiD generator and model:

```python
import statsmodels.formula.api as smf
rng = np.random.default_rng(0)
rows, units, periods = [], 200, 12
unit_effect = rng.normal(0,2,units)
for i in range(units):
    treated = int(i < units//2)
    for t in range(periods):
        post = int(t >= 6)
        y = 5 + unit_effect[i] + .3*t + 2*treated*post + rng.normal()
        rows.append((i,t,treated,post,y))
panel = pd.DataFrame(rows, columns=["unit","time","treated","post","y"])
model = smf.ols("y ~ treated:post + C(unit) + C(time)", panel).fit(
    cov_type="cluster", cov_kwds={"groups": panel["unit"]}
)
```

Parallel trends is the identifying assumption; event studies inspect pre-trends. Standard TWFE can use problematic weights under staggered adoption and heterogeneous effects.

Synthetic control chooses nonnegative donor weights summing to one to match pre-treatment outcomes. Assess pre-fit, in-space and in-time placebos, donor sensitivity, and post/pre RMSPE ratios.
