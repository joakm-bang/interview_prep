# Data intuition and debugging: Solutions

### Overnight metric jump
Start with measurement validity before product stories: confirm definition, query, timezone, freshness, numerator and denominator, raw counts, platform/version/geography/source segments, deploy history, duplicate or missing events, bots/internal traffic, joins, and backfills. Cross-check with an independent business metric.

### Platform reversal
Estimate subgroup effects with intervals and interactions; verify sample size and multiplicity; audit platform-specific instrumentation; reweight to a common platform distribution to separate heterogeneity from Simpson's paradox.

### Revenue up, orders down
Use `Revenue = Active Users × Orders per Active User × Average Order Value`. With active users flat and orders down, AOV rose enough to offset it. Check price, quantity, product mix, discounts, geography, enterprise buyers, refunds, and FX.

### Dashboard disagreement
Compare source tables, definitions, filters, timezone, attribution windows, distinct keys, late data, bot exclusions, currency, event versus processing time, and refresh schedules. Produce a row-level diff for a small period.

### MNAR survey
Respondent means are selected because treatment changes response. Report the response-rate effect, compare pre-treatment covariates, reweight by estimated response propensity, perform extreme-value bounds, and consider randomized follow-up incentives.

### Offline metric up, purchases down
Possible causes: label misalignment, position bias, reduced diversity, latency, calibration, distribution shift, cannibalization, or satisfaction costs omitted from NDCG. Run an online randomized experiment with purchases, revenue, retention, latency, and guardrails.

### Voluntary adoption
Adopters differ in need, sophistication, and expected gain. Use random availability/defaults, randomized encouragement, phased rollout, eligibility thresholds, or cautious observational adjustment.

### Segment explosion
Audit taxonomy and pipeline changes, null/default coding, case/whitespace, joins, duplicates, app version, geography/source, bots, backfills, and historical restatement.
