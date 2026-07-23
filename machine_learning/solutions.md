# Regression and machine learning: Solutions

- **OLS unbiasedness:** linear-in-parameters specification, no perfect multicollinearity, representative design, and `E[epsilon|X]=0`.
- **Conventional SEs:** additionally require homoskedastic, independent errors; otherwise use robust or clustered SEs.
- **Causality:** no omitted confounding, valid treatment definition, overlap, appropriate interference assumptions, and credible design.
- **Logistic regression:** coefficient = change in log odds; `exp(beta)` = odds ratio; marginal effect = probability derivative at a covariate vector; AME averages derivatives over observations.
- **Rare classes:** class weights preserve data; upsampling increases minority representation; downsampling saves compute but discards information. Optimize PR-AUC, recall at precision, calibrated expected cost, or business utility rather than accuracy.
- **Cost-sensitive threshold:** on validation data, choose the threshold minimizing `20*FN + FP`, ideally from calibrated probabilities.
- **Leakage:** future features, target-derived features, preprocessing on full data, duplicate users across splits, post-outcome timestamps, label proxies, random time leakage, and human-review outcomes.
- **Time validation:** train on earlier periods, validate on a later contiguous period, test on the newest period; reproduce production feature cutoffs.
- **Calibration:** reliability diagram compares predicted and empirical rates; Brier score is squared probability error; Platt is logistic calibration; isotonic is monotone nonparametric calibration.
- **Overfitting:** check split integrity, distribution mismatch, capacity, regularization, feature count, label noise, sample size, and hyperparameter search. Consider simpler models, regularization, more data, early stopping, and better validation.
- **Shift:** compare feature/missingness/score distributions, prevalence, calibration, and subgroup metrics. Separate `P(X)` shift, `P(Y)` shift, `P(Y|X)` drift, logging changes, and model-induced feedback loops.
