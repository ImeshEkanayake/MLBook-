# Chapter 37: Uncertainty and decision quality — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_37_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 37.1 · Calibration and probability quality

- [Fit two actual probability models and calibrate on separate buildings](notebooks/196_Chapter_37_01_calibration_reliability_and_typed_probability_outputs.ipynb#fit-models-and-calibrate-separately)
- [Preserve small-bin uncertainty and unchanged ordering](notebooks/196_Chapter_37_01_calibration_reliability_and_typed_probability_outputs.ipynb#reliability-and-discrimination)

Declared mechanisms: actual boosted classifier and original neural typed probability interface, independent positive-temperature calibration with unchanged ranking, fixed-bin reliability Wilson intervals Brier log loss and sharpness, class-conditional score checks separated from calibration definitions.

```bash
python scripts/run_notebook.py notebooks/196_Chapter_37_01_calibration_reliability_and_typed_probability_outputs.ipynb
```

## 37.2 · Predictive intervals and uncertainty models

- [Compare actual interval constructions under explicit assumptions](notebooks/197_Chapter_37_02_quantile_ensemble_bayesian_and_distributional_intervals.ipynb#fit-four-uncertainty-models)
- [Measure coverage and width separately in familiar and new regimes](notebooks/197_Chapter_37_02_quantile_ensemble_bayesian_and_distributional_intervals.ipynb#assess-prediction-versus-parameter-intervals)

Declared mechanisms: actual quantile regression and bootstrap predictive residual mixture, conjugate Normal inverse gamma Bayesian parameter and predictive Student t intervals, actual heteroscedastic Gaussian likelihood optimization, familiar versus shifted-load coverage and width without final recalibration.

```bash
python scripts/run_notebook.py notebooks/197_Chapter_37_02_quantile_ensemble_bayesian_and_distributional_intervals.ipynb
```

## 37.3 · Conformal prediction and assumptions

- [Calibrate whole-building scores and state the coverage event](notebooks/198_Chapter_37_03_grouped_conformal_sets_intervals_and_delayed_temporal_updates.ipynb#grouped-classification-sets)
- [Conformalize actual quantile fits with a building-level score](notebooks/198_Chapter_37_03_grouped_conformal_sets_intervals_and_delayed_temporal_updates.ipynb#grouped-conformal-quantile-intervals)
- [A recent-window update is assumption-dependent](notebooks/198_Chapter_37_03_grouped_conformal_sets_intervals_and_delayed_temporal_updates.ipynb#delayed-temporal-recalibration)

Declared mechanisms: actual held-out classification nonconformity and building-maximum calibration, finite-sample rank with new-building simultaneous versus row-marginal claims, actual conformalized quantile intervals and material-shift assessment, delayed rolling calibration under drift explicitly without exchangeability guarantee.

```bash
python scripts/run_notebook.py notebooks/198_Chapter_37_03_grouped_conformal_sets_intervals_and_delayed_temporal_updates.ipynb
```

## 37.4 · Thresholds, costs and expected utility

- [Separate event probability, action benefit and resource capacity](notebooks/199_Chapter_37_04_cost_thresholds_capacity_and_decision_curves.ipynb#cost-capacity-and-policy-selection)
- [Make the exchange rate and capacity visible](notebooks/199_Chapter_37_04_cost_thresholds_capacity_and_decision_curves.ipynb#decision-curves-and-service-constraint)

Declared mechanisms: source logistic model with separate probability calibration and policy selection, heterogeneous avoided-loss utility and daily capacity ten allocation, actual decision-curve net benefit with declared threshold exchange rates, realized final utility versus simulator expected utility audit.

```bash
python scripts/run_notebook.py notebooks/199_Chapter_37_04_cost_thresholds_capacity_and_decision_curves.ipynb
```

## 37.5 · Deferral, selective prediction and sequential use

- [Treat confidence and support as different admission questions](notebooks/200_Chapter_37_05_selective_risk_support_gates_and_review_queue.ipynb#choose-a-deferral-policy)
- [Execute the review queue instead of treating deferral as free correctness](notebooks/200_Chapter_37_05_selective_risk_support_gates_and_review_queue.ipynb#review-service-and-delayed-outcomes)

Declared mechanisms: actual independent temperature calibration and empirical deferral selection, confidence-only versus explicit unsupported-domain gate, accepted-risk automation-coverage and repeated-day error diagnostics, executed finite-capacity review queue with delayed outcomes and combined service cost.

```bash
python scripts/run_notebook.py notebooks/200_Chapter_37_05_selective_risk_support_gates_and_review_queue.ipynb
```

## Interpretation and boundaries

# Chapter 37 mechanisms, controls and interpretation

Five laboratories preserve all five original scopes and both visual briefs. They execute 21 code cells and produce 11 inline figures. Imports, helpers and generated observations are internal. Ordinary execution needs no files, network, credentials or GPU. The unchanged main CPython 3.14.3 environment supplies NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0; 196 additionally uses installed Torch 2.14.1 CPU, one thread, deterministic float 64. No dependency, dataset or model asset is added. Literature cutoff remains 18 October 2026; access and execution date 22 October 2026 Australia/Melbourne.

## Actual mechanisms and limits

- **196 / reliability:** Independent 1, 000 source/600 calibration/600 final buildings, one record each, nonlinear noisy finding law. Actual 100-iteration HGB and original 4→16→1 Tanh neural classifier with 600 Adam updates. Neural probability records validate a named event/bounded probability/binary decision; no pretrained language model or schema-based calibration claim. Explicitly doubled source-model logits create an overconfidence stress condition. Positive temperatures fitted on separate calibration log loss are2.607717/2.580041. Final booster Brier 0.200623→0.180979, log loss 0.665050→0.536263, unchanged AUC 0.794837. Typed neural Brier 0.198529→0.175454, log loss 0.659096→0.520369, unchanged AUC 0.807343. Assertions verify exact within-model ordering. Ten equal-width positive-event reliability bins retain counts/empty bins and per-bin Wilson frequency intervals. These are not simultaneous bands, fitted-model uncertainty or a binning-independent calibration certificate. True-class probability distributions describe separation, not a requirement that all positives have probability one. Visual A separates model reliability panels for readability and retains the same booster ranking below them.
- **197 / interval meanings:** Independent 800 source loads 0–1, 400 familiar final loads 0–1, 400 new-load final 1–1.7. True mean adds a new 4(load−1)² term beyond source support; noise scale 0.2+0.4 load. Actual native quantiles0.05/0.95,30 source-bootstrap quadratic Ridge fits with 300 pooled-residual predictive draws per final case, conjugate Normal–inverse-gamma quadratic regression, and optimized heteroscedastic Gaussian quadratic-mean/log-linear-scale likelihood. Prior mean 0, coefficient precision 0.01I scaled by variance, inverse-gamma shape2/scale0.1; posterior predictive Student t df 804. Explicit parameter versus predictive scale differs by future-noise term. Independent 20, 000 posterior variance/coefficient/future-noise draws check analytic predictive quantiles within 0.05 mm. Gaussian optimizer succeeds. Familiar/new coverage and width: quantiles0.830/0.770,1.134984/1.773139 mm; bootstrap predictive0.8625/0.530,1.300806/1.386653; Bayesian predictive0.8925/0.5225,1.306145/1.389195; conditional Gaussian0.860/0.895,1.228477/2.708897. New-regime Gaussian coverage is an observed wide-interval result, not a guarantee of extrapolation. Bayesian parameter-only future-outcome coverage0.0875/0.165 and ensemble-mean-only0.0625/0.18 are explicitly category-error diagnostics, not their intended coverage targets. All source fits precede final assessment; first 12 records per regime are fixed illustrations.
- **198 / grouped conformal:** Source1,000/calibration200/familiar300/shifted300 buildings×3 correlated records. Actual source HGB class probabilities; score 1−probability of true class. Maximum across three records makes the independent building the calibration unit. Alpha 0.1 gives rank181/200, threshold 0.837474; pooled-row diagnostic rank541/600, threshold 0.686506. Familiar building-all-three coverage 0.896667 versus pooled-row 0.723333; corresponding row coverage0.957778/0.894444, mean set sizes1.624444/1.338889. At least 90% marginal probability under exchangeable new whole buildings does not force every realized final cohort frequency above 0.9. Shifted mechanism changes material prevalence, severity and label law; class building coverage0.876667/0.693333. Actual native burden quantiles, sorted before calibration, use max(lower−y, y−upper) then building maxima; CQR correction0.268985/rank181. Familiar/shifted all-three interval coverage0.896667/0.193333, row0.962222/0.434444 and width1.826304/1.863033. Grouped CQR is an original declared adaptation; no feature-conditional, arbitrary-building-size or shifted-law guarantee. Visual B1 shows actual intervals and precise coverage boundary. A separate 240-arrival stream transitions to shifted mechanism; rolling window 80 uses only labels delayed 10 arrivals. Fixed block coverage0.95/0.90/0.925 versus rolling0.875/0.875/0.9125. Temporal heuristic does not improve every block and claims no specialized temporal coverage theorem. Assertions audit label availability.
- **199 / utility and capacity:**120 whole days×30, split 60 source/15 calibration/10 policy-selection/35 final. Actual source logistic plus separate calibration logistic. Assumed avoidable event loss 5–20 and action cost 1–5 utility units, equal-resource visits, capacity 10 daily. Source-calibrated p×B−C ranks up to 10 positive values; risk rank takes 10; a fixed-grid development threshold 0.05 with risk-based truncation produces identical final actions to the latter, retained honestly. Utility policy uses 9.942857 visits/day, realized 37.308946 units/day and simulator-expected 39.927453, versus risk/cutoff10 visits,33.147185/35.645671. Assumed perfect avoidance is a decision-model input, not estimated causal treatment efficacy. Conventional homogeneous net-benefit curves compare act-all/none on a predeclared final grid descriptively and do not select the published policy. They are distinct from heterogeneous B/C and daily capacity. Visual B2 displays actual first-final-day expected utilities and admitted candidates before outcomes.
- **200 / selective service:** Independent 1, 000 source/400 calibration/400 selection/1,000 final buildings. Source authorized load range[−2, 2]; unsupported 2.1–4 has reversed outcome law, selection frequency 15%, final observed 34.1%. Actual source HGB/positive temperature 1.107812. Gate rejects all unsupported inputs. Fixed confidence grid 0.5–0.99 seeks empirical accepted error≤0.12 and review≤0.30, maximizing coverage. No candidate is feasible. The recorded fallback is defer all; numerical threshold 1.01 is only its internal sentinel and figure labels the action as defer all. No final threshold revision. Final automation coverage 0 and accepted risknull; zero days with accepted errors is not evidence of reliable automation. Descriptive confidence-only/gated risk curves remain parallel diagnostics. FIFO server processes 3 cases/day under 100 days×10 arrivals, leaving 700 pending at day 100. Continue after arrivals to drain: mean completion delay 116.667 days, max 234, plus 3 additional days for outcome availability. Simulated reviewer error probability 2% gives eventual combined error 0.016, excluding waiting harm and pending-at-horizon service obligations. Cost 8 per review versus 0.05 per automatic case gives 8, 000 units. No oracle engineer, field service fee or immediate-correctness claim. Delayed final labels never update the frozen model/policy.

## Execution and figure review

All five initial fresh kernels pass; 197 subsequently adds an independent posterior-predictive Monte Carlo check and reruns.196 separates overlapping reliability curves into model-specific panels and reruns; 200 replaces an internal-sentinel display with the actual defer-all action and reruns. These are declared interpretation/readability repairs without selecting different scientific outcomes. Current sources contain no errors or stderr, all assertions pass. Every current cell reruns in an isolated vector-export process with exact scientific RESULTS equality, including the new Monte Carlo result. Eleven original SVG/vector-PDF/PNG sets reproduce actual experiments. Reliability intervals, support curves, group coverage statements, changed-law failures, duplicate policies, infeasible selection and review delays remain visible. Source references distinguish successfully inspected PDFs from verified primary indexed abstracts where full-text access failed. Chapters 38–43 and the whole-book audit remain required; this is not whole-book completion.
