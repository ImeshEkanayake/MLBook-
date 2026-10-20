# Chapter 15: Linear, additive, and interpretable models — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_15_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 15.1 · Linear regression and robust alternatives

- [Match the response target to the loss](notebooks/072_Chapter_15_01_Losses_Residuals_And_Quantiles.ipynb#losses)
- [Coefficients can be nonunique while predictions agree](notebooks/072_Chapter_15_01_Losses_Residuals_And_Quantiles.ipynb#geometry)

Declared mechanisms: least squares geometry and rank deficiency, contaminated training responses, median and conditional quantile targets, fitting versus inference assumptions.

```bash
python scripts/run_notebook.py notebooks/072_Chapter_15_01_Losses_Residuals_And_Quantiles.ipynb
```

## 15.2 · Generalized linear models

- [The output distribution and exposure define the task](notebooks/073_Chapter_15_02_Bernoulli_Counts_And_Exposure.ipynb#links)
- [A count expectation is not a probability of at least one event](notebooks/073_Chapter_15_02_Bernoulli_Counts_And_Exposure.ipynb#probabilities)

Declared mechanisms: Bernoulli logit versus count log-mean, exposure offset and weighted rates, Poisson mean versus overdispersion, count means are not event probabilities.

```bash
python scripts/run_notebook.py notebooks/073_Chapter_15_02_Bernoulli_Counts_And_Exposure.ipynb
```

## 15.3 · Regularization and high-dimensional fitting

- [Align the penalty convention before comparing paths](notebooks/074_Chapter_15_03_Correlated_Sensors_And_Shrinkage.ipynb#penalties)
- [Refitting measures conditional sensitivity, not newly collected evidence](notebooks/074_Chapter_15_03_Correlated_Sensors_And_Shrinkage.ipynb#stability)

Declared mechanisms: Ridge Lasso ElasticNet common penalty convention, training-only standardization and development selection, correlated sensor coefficient paths, bootstrap coefficient and prediction stability.

```bash
python scripts/run_notebook.py notebooks/074_Chapter_15_03_Correlated_Sensors_And_Shrinkage.ipynb
```

## 15.4 · Additive, spline and shape-constrained models

- [A nonlinear additive predictor with a declared load constraint](notebooks/075_Chapter_15_04_Additive_Risk_And_Monotone_Load.ipynb#additive)
- [Calibrate on a separate role and retain a possibly worse result](notebooks/075_Chapter_15_04_Additive_Risk_And_Monotone_Load.ipynb#calibration)

Declared mechanisms: linear versus additive response on a fixed cohort, training-fitted spline basis and penalty selection, nonnegative monotone load increments, independent isotonic calibration and limits.

```bash
python scripts/run_notebook.py notebooks/075_Chapter_15_04_Additive_Risk_And_Monotone_Load.ipynb
```

## 15.5 · Rules, sparse scores and symbolic models

- [Restrict the expression search and preserve dimensions](notebooks/076_Chapter_15_05_Compact_Rules_And_Dimensional_Search.ipynb#units)
- [Compact rules can lose important interactions](notebooks/076_Chapter_15_05_Compact_Rules_And_Dimensional_Search.ipynb#rules)

Declared mechanisms: finite symbolic dictionary with dimensional guards, development complexity selection and locked assessment, decision list sparse score and rule ensemble, compactness fidelity and expression limits.

```bash
python scripts/run_notebook.py notebooks/076_Chapter_15_05_Compact_Rules_And_Dimensional_Search.ipynb
```

## Interpretation and boundaries

Five generated-data CPU laboratories use seeds 1572–1576 and the unchanged Python 3.14.3 / NumPy 2.4.4 / SciPy 1.17.1 / pandas 3.0.3 / Matplotlib 3.11.0 / scikit-learn 1.9.0 environment. All current notebooks execute in fresh kernels without error outputs or solver warnings. code_076 initially reached its summary with a NumPy int 64 leaf count that JSON could not serialize; converting that count to Python int repaired the reporting boundary and its fresh run passes. code_072 reran after clarifying a reporting-loss field; code_074 reran after adding the separate p>n algebra audit. code_075 reran after clarifying that its clipped ramps form a piecewise-linear load spline; the current result dictionaries agree exactly with the original registered report. Visual review caught colliding titles in notebook panels073,075,076; shorter titles repaired them and fresh kernels retained exactly the registered result dictionaries. Current timings belong to current sources. No dependency was added; ordinary execution is offline and self-contained.

The strain laboratory uses 240 training, 100 unused reserved development and 400 clean final observations. Exactly twelve training responses receive +180 microstrain contamination. Fixed OLS, Huber(epsilon 1.35, alpha 0) and quantile(.1,.5,.9, alpha 0) models use the same load feature. OLS/Huber/median slopes are 1.863631/2.001519/2.032093 microstrain per kN; final MSE is 158.5001/79.1505/80.1145. Final fractions below q 10/q 90 are .0825/.95 and their empirical interval coverage is .8675, not guaranteed nominal .8. Orthogonality of the OLS residual to its fitted design is numerically verified; duplicate load columns have rank 2 with three columns, and a [0,7,-7] coefficient perturbation preserves predictions. Neither audit establishes inference assumptions, a causal law or robustness to predictor leverage.

The GLM laboratory has 600 training, 200 unused development and 400 final records. Bernoulli failure and inspection counts are separate outcomes. Counts have log exposure offset and a Gamma(shape2,scale.5) rate multiplier, giving variance mu+mu²/2. The explicit Poisson working likelihood passes gradient error 1.64e-8 and matches an unpenalized exposure-weighted rate fit within 2e-5 coefficient tolerance. Fitted coefficients [.1223195,.6615078] compare with declared [.1,.7]; training Pearson dispersion is 1.6200 and final mean Pearson residual square is 1.5804. Final observed/predicted mean counts are 1.5225/1.5447. Mean count two gives positive-event chance .864665 under Poisson and .75 under the generated mixture. No negative-binomial fit or significance test is claimed. Failure Brier/log loss is .205868/.602950 on 121 events in 400 rows.

Correlated sensors use training 90/development 120/final 400 with twelve features and A/B correlation .999721. Common objective SSE/(2 n)+lambda*(rho*L 1+(1-rho)*L 2²/2) implies Ridge alpha=n*lambda, Lasso alpha=lambda and ElasticNet alpha=lambda,rho=.5. Each family independently selects lambda .0811131 using development MSE. Final MSEs Ridge/Lasso/ElasticNet are .339376/.329724/.330161. Sixty training-row bootstrap draws refit scalers but condition on each selected penalty; they do not repeat tuning. Lasso A/B coefficient SDs .735086/.738685 contrast with summed SD .056579 and selection frequencies .4/.816667. Mean fixed-final-covariate prediction SDs are .175774/.105886/.128567 for the three families. A separate24-row/40-column algebra fixture interpolates with rank 24 and a null direction preserving every prediction; Ridge at penalty .1 reduces norm with training MSE 2.06e-5. That separate audit makes no held-out generalization claim. Paths use exactly the same data/common lambda and highlight the correlated pair.

The additive logistic laboratory uses train 350/development 150/calibration 300/final 400 plus a locked 200-record temperature-zero slice. Generated risk is sigmoid(-2+3*load²+1.5*temperature²). Four clipped ramps with nonnegative coefficients enforce nondecreasing load logits; a training-fitted cubic temperature B-spline has free coefficients. Development chooses penalty .001. Load increments [0,.217827,1.671465,.902634] and a dense-grid check verify the stated shape. Raw final linear/additive log loss is .586065/.575679 and Brier .199369/.193511. Locked-slice log loss is .566530/.553058. Independent isotonic calibration changes final Brier to .193496 but worsens 1e-6-clipped log loss to .652219, with 22 empirical endpoint predictions. The worse result is retained. Additivity is on the link scale; the load ramps saturate and temperature spline has constant extension outside declared support. No causal interpretation, comprehensive GAM library or out-of-support physical validity is asserted.

Finite expression search uses train 250/development 120/final 300 under the declared simply supported central-load relation delta=P*L³/(48EI) with .1 mm noise. Three predeclared dimensionally valid dictionaries fit dimensionless coefficients; development MSE+1e-9 m² per term selects the beam term alone. Coefficient .0208438668 compares with 1/48; final MSE 1.06857738e-8 m² is .010685774 mm². A unitless coefficient multiplying P/EI is rejected because it cannot produce a length; a differently dimensioned coefficient would describe another contract. Unit conversion is checked. This favorable finite dictionary already contains the true synthetic form and is not unrestricted symbolic discovery. Fixed decision list, sparse integer score, four-leaf tree and a logistic ensemble of four fixed rules achieve observed >3 mm flag accuracy .563333/.716667/.876667/.856667, separately expression-flag agreement .56/.713333/.88/.86. No final-driven rule changes, field safety threshold or RuleFit implementation is claimed.

Ten original SVG/vector-PDF/PNG figure sets implement the linear/additive common-cohort and correlated shrinkage-path briefs plus loss, count, resampling, calibration and dimensional-fidelity mechanisms. Five equations and eight connected exercises retain the fitting/inference distinction. Official quantile, Poisson, spline and isotonic documentation and the primary Friedman/Hastie/Tibshirani 2010 JSS path paper were inspected 20 October 2026. Documentation maintenance version 1.9.1 versus executed 1.9.0 is disclosed. The book is a bounded synthetic teaching draft, not external empirical validation.
