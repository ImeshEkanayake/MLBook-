# Chapter 36: Evaluation and error diagnosis — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_36_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 36.1 · Regression and predictive distributions

- [Fit predictions and choose the reporting contract before final assessment](notebooks/188_Chapter_36_01_point_quantile_and_proper_distribution_scores.ipynb#point-and-quantile-scores)
- [Score uncertainty rather than reward width alone](notebooks/188_Chapter_36_01_point_quantile_and_proper_distribution_scores.ipynb#proper-distribution-scores)

Declared mechanisms: actual ridge and histogram point predictors with unit-aware weighted metrics, actual source-fitted conditional quantiles and pinball loss, Gaussian log score CRPS coverage and interval width, independent final scores with declared asymmetric underprediction cost.

```bash
python scripts/run_notebook.py notebooks/188_Chapter_36_01_point_quantile_and_proper_distribution_scores.ipynb
```

## 36.2 · Classification, ranking and recommendation

- [Hold whole inspection days apart and freeze the decision threshold](notebooks/189_Chapter_36_02_classification_query_ranking_and_physical_diagnosis.ipynb#classification-and-query-denominators)
- [Inspect classification, capacity and structural validity together](notebooks/189_Chapter_36_02_classification_query_ranking_and_physical_diagnosis.ipynb#metric-matched-to-use)

Declared mechanisms: source-fitted classifier and development-only cost threshold, ROC precision recall Brier log loss and query-macro top capacity metrics, observed exposure distinguished from complete generated relevance, one workflow confusion ranking and physical residual Visual A.

```bash
python scripts/run_notebook.py notebooks/189_Chapter_36_02_classification_query_ranking_and_physical_diagnosis.ipynb
```

## 36.3 · Survival, clustering and anomaly detection

- [Keep censored durations out of ordinary regression scores](notebooks/190_Chapter_36_03_censoring_cluster_stability_and_alarm_episodes.ipynb#censor-aware-discrimination)
- [Separate reproducibility of a partition from its scientific meaning](notebooks/190_Chapter_36_03_censoring_cluster_stability_and_alarm_episodes.ipynb#cluster-stability-and-agreement)
- [Count events, lead times and operating burden explicitly](notebooks/190_Chapter_36_03_censoring_cluster_stability_and_alarm_episodes.ipynb#alarm-episodes-and-point-adjustment)

Declared mechanisms: actual source Cox likelihood and censor-aware discrimination and Brier scores, bootstrap-fitted KMeans stability separated from external agreement, pointwise eventwise warning time and false alarm episode denominators, explicit demonstration of point adjustment inflation.

```bash
python scripts/run_notebook.py notebooks/190_Chapter_36_03_censoring_cluster_stability_and_alarm_episodes.ipynb
```

## 36.4 · Graph, temporal and physical prediction

- [Score a field at the sampling resolution and physical boundary](notebooks/191_Chapter_36_04_graph_field_constraints_spectra_and_forecast_horizons.ipynb#node-edge-and-field-validity)
- [Evaluate repeated forecast origins within their parent trajectory](notebooks/191_Chapter_36_04_graph_field_constraints_spectra_and_forecast_horizons.ipynb#horizon-and-graph-aggregation)

Declared mechanisms: actual unconstrained and boundary-conforming field surrogates, node edge graph L2 gradient boundary and equation residual assessment, discrete sine residual spectrum and whole-graph aggregation, actual source-fitted recursive forecasts assessed by horizon and trajectory.

```bash
python scripts/run_notebook.py notebooks/191_Chapter_36_04_graph_field_constraints_spectra_and_forecast_horizons.ipynb
```

## 36.5 · Generative and representation quality

- [Fit generators on source observations and evaluate independent observations](notebooks/192_Chapter_36_05_synthetic_fidelity_coverage_utility_and_memorization.ipynb#generator-evaluation-suite)
- [A low-variance feature can carry the task information](notebooks/192_Chapter_36_05_synthetic_fidelity_coverage_utility_and_memorization.ipynb#representation-reconstruction-and-probes)

Declared mechanisms: actual conditional Gaussian sensor generator versus mode dropping and copying, rare regime coverage conditional means correlations and exact-copy diagnostics, actual train-on-synthetic test-on-independent-real regression, source-fitted PCA reconstruction and predictive probes with rare-slice scores.

```bash
python scripts/run_notebook.py notebooks/192_Chapter_36_05_synthetic_fidelity_coverage_utility_and_memorization.ipynb
```

## 36.6 · Policies, causal estimators and decisions

- [Fit nuisance responses elsewhere and assess a locked policy](notebooks/193_Chapter_36_06_policy_values_causal_effects_and_control_constraints.ipynb#supported-policy-and-causal-assessment)
- [Execute identical-disturbance rollouts and retain violations](notebooks/193_Chapter_36_06_policy_values_causal_effects_and_control_constraints.ipynb#executed-control-and-constraints)

Declared mechanisms: independent logged bandit IPS and doubly robust values with simulator audit, actual source-fitted nuisance outcomes and supported ATE score, unsupported deterministic logging explicitly refuses full policy value, executed sequential controllers report return regret and constraint violations.

```bash
python scripts/run_notebook.py notebooks/193_Chapter_36_06_policy_values_causal_effects_and_control_constraints.ipynb
```

## 36.7 · Statistical uncertainty and fair comparisons

- [Resample independent buildings while preserving paired predictions](notebooks/194_Chapter_36_07_paired_building_bootstrap_seeds_and_error_slices.ipynb#paired-building-resampling)
- [Keep subgroup denominators and uncertainty targets visible](notebooks/194_Chapter_36_07_paired_building_bootstrap_seeds_and_error_slices.ipynb#load-slices-and-seed-variation)

Declared mechanisms: actual fixed ridge and eight seeded random forest fits, paired equal-building loss comparison with building versus row bootstrap, source fixed training seed variation separated from cohort uncertainty, building-level paired differences and counted load slices Visual B.

```bash
python scripts/run_notebook.py notebooks/194_Chapter_36_07_paired_building_bootstrap_seeds_and_error_slices.ipynb
```

## 36.8 · Error analysis and actionable diagnosis

- [Distinguish label defects, timing defects and missing support](notebooks/195_Chapter_36_08_units_shortcuts_support_and_targeted_data_acquisition.ipynb#diagnostic-audit-before-revision)
- [Acquire new source observations for the identified regime](notebooks/195_Chapter_36_08_units_shortcuts_support_and_targeted_data_acquisition.ipynb#targeted-new-source-and-final-assessment)

Declared mechanisms: audited source unit conversion and removal of post-outcome shortcut, diagnostic residual slices with support and sample counts, actual new source acquisition in unsupported material-load regime, fixed-recipe augmentation assessed on independent locked buildings.

```bash
python scripts/run_notebook.py notebooks/195_Chapter_36_08_units_shortcuts_support_and_targeted_data_acquisition.ipynb
```

## Interpretation and boundaries

# Chapter 36 mechanisms, controls and interpretation

Eight self-contained laboratories preserve all eight original scopes and both visual briefs. They execute 33 code cells and produce 17 inline figures. All imports, helpers and generated observations are internal; ordinary runs need no files, network, credentials or GPU. The unchanged main CPython 3.14.3 runtime uses NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0. No dependency installation, environment change, external dataset or model asset is added. Literature cutoff remains 18 October 2026; primary-source access/execution is 22 October 2026 Australia/Melbourne.

## Actual mechanisms and evidence boundaries

- **188 / points and distributions:** Independent 1, 000 source/600 final structures, nonlinear mean, load-dependent noise and occasional positive-tail disturbances. Actual fixed Ridge and native 120-iteration histogram models; separately fitted quantiles 0.1/0.5/0.9. MAE, RMSE, explicit 1 mm relative denominator floor, source-declared high-load weight four and underprediction cost four retain different meanings. Booster MAE 0.689311/RMSE 1.337864 mm; weighted RMSE 1.586742. Raw quantiles cross on one record; sorted interval coverage 0.790, width 1.865545 mm. A source-fitted residual scale around the booster defines two misspecified Gaussian forecasts, scale 1.066240 or twice it. Coverage rises 0.900→0.983333, but CRPS worsens 0.538054→0.687887 mm and NLL 1.770275→1.873024. Numerical CDF integration independently checks one closed-form CRPS to rounding. No final recalibration or model selection.
- **189 / inspection decisions:** 120 whole days×12 sites, split 70 source/20 development/30 final. Actual source logistic; fixed-grid development cost FN5/FP1 chooses threshold 0.21. Final confusion [[159, 88],[23, 90]], ROC AUC 0.789115, average precision 0.624740, Brier 0.169364, log loss 0.512958. AP is step-weighted, distinct from the drawn line's trapezoidal area. Query-macro precision@3 0.588889; positive-query-only recall@3 0.523071; NDCG@3 0.703762 with zero for one empty-positive day. Complete generated relevance enables a separate position-examination diagnostic; unexamined response is not relevance. A separate actual Ridge on these sites' source displacement fields lacks the load-coordinate interaction. Final field RMSE 0.025905 mm, maximum support displacement 0.073456 mm despite exact zero supports. Visual A uses the actual confusion, capacity curve and signed first-final-day residual. It does not infer physical validity from classifier AUC.
- **190 / incomplete supervision:** Actual penalized Cox partial-likelihood optimization and Breslow baseline on 700 source components; optimizer succeeds, beta 0.632506. Same 500 final lifetimes observed separately under independent Uniform(0, 10) and Uniform(0, 6) censoring. Known-law G, explicitly not estimated censor nuisance, weights age-five concordance and age-four Brier. Weighted C 0.673481/0.675049; raw C 0.674885/0.682503; latent audit 0.667458. IPCW Brier 0.225059/0.196468, latent Brier audit 0.215080. Independent KMeans study fits 20 source-bootstrap partitions per k=2/3/5 using 600 source records, predicts 200 common independent anchors and compares all 190 pairs. Mean stability ARI 0.889605/0.851280/0.702182; external latent ARI 0.500282/0.552461/0.381880. No anchor-selected cluster count. Six assets×180 days give 18 declared fault intervals. Score fixtures are a precursor-sensitive monitor and independent random alarms, not fitted detectors. Useful window begins three days before onset. Monitor detects 18, median lead 2 days, false episode rate 0.25 per 30 asset-days; random detects 7, median lead−1 day, rate 1.388889. False episodes count alarm-run starts outside every warning/event window. Actual point F1 monitor/random 0.743421/0.072727; retrospective point-adjusted diagnostics 0.899135/0.452555 are explicitly not deployed predictions.
- **191 / structure and horizons:** 80 source/40 final path graphs, 24 nodes, normalized coordinate, exact u=q x(1−x). Source fits use noisy interior nodes. Actual unconstrained polynomial Ridge versus fitted scalar boundary-conforming basis; nodal RMSE 0.018685/0.001027 mm, edge-gradient RMSE0.132209/0.003315, max boundary0.089077/0 mm, equation RMS0.458208/0.011495. Also graph peak errors, trapezoidal field L2 and normalized type-I sine spectra with Parseval check. Nonzero equation residual remains despite exact conforming endpoints. Independent temporal study: 60 source/40 final trajectories, 100 steps, six fixed origins and horizons1/3/6/12. Actual one-step Ridge rolls out recursively with explicitly known future forcing; origin scores average within each trajectory. Recursive MAE0.124796/0.164008/0.177030/0.183003 versus persistence0.142978/0.280095/0.477684/0.848903. Overlapping horizons are not independent replicates.
- **192 / synthetic data and representations:** 800 source/600 independent assessment sensor records, 65 rare assessment records. Actual source-fitted regime-conditional joint Gaussian, deliberate mode dropping, and exact bootstrap copying each produce 800 synthetic rows. Evaluate correlation error, conditional response means, rare frequency, source-scaled nearest-source distance and exact joint-row copying. Conditional rare frequency 0.09125 versus independent 0.108333; dropped 0. Exact copier fraction 1; Gaussian 0 does not establish privacy. Same actual Ridge trained on synthetic observations yields all/rare assessment RMSE Gaussian3.026827/8.552114, dropped4.944900/14.976423, copier2.922720/8.206833; real-source baseline2.896400/8.128664. Probe regularization/scaling are part of utility, not an intrinsic generator ranking. Actual source-only raw-scale PCA 3 retains 0.999974853 variance with independent reconstruction MSE 0.00026168 but rare probe RMSE 13.480343; invertible PCA 4 reconstruction≈0 and rare probe 8.128664. No FID, distributional PRD or privacy guarantee is falsely claimed as executed.
- **193 / actions and effects:** Actual source-only separate Ridge response nuisances on 3, 000 logged contexts; locked policy assessed using 1, 500 independent supported logs, known clipped propensity 0.05–0.95. IPS value0.521580/DR0.585038 versus simulator audit 0.592504. Six hundred independent-context bootstrap replicates produce conditional CIs IPS[0.446057, 0.601995], DR[0.538186, 0.627244]. DR ATE−0.334248 versus simulator−0.296490, CI[−0.399066,−0.275892]. Weighted context imbalance 0.108661 versus unweighted 0.791946 does not prove observational ignorability. Separate deterministic logging has unsupported target mass 0.854667 and explicitly returns no full value. Original 20-step control simulator executes 200 paired identical-disturbance rollouts for never/state-trigger/always rules. Mean returns−218.292946/−20.304078/−14.194143; any-violation fractions1/0.09/0, actions0/12.485/20 per episode. No field safety or unknown counterfactual claim; regret is explicitly simulator-only.
- **194 / comparison uncertainty:** Independent 160 source/60 final buildings×20 records. Actual Ridge and eight 64-tree depth-six forests with fixed seeds; seed 7794 is primary and final outcomes never choose a seed. Primary forest minus Ridge MSE difference−0.531635. Nine hundred whole-building paired bootstrap replicates give CI[−0.924254,−0.139002]; deliberately incorrect row bootstrap gives[−0.645618,−0.424682]. These condition on fitted models and omit source refitting variability. Eight-seed spread is not eight independent datasets. Visual B shows all 60 building differences and fixed low/middle/high load slices with394/379/427 records, 60 buildings each. Slice CIs are exploratory pointwise, not simultaneous; low-load interval spans zero. Counts and parent-unit weighting remain explicit.
- **195 / diagnosis and new evidence:** Independent 200 source/80 diagnostic/100 final buildings×4. Source new material is rare at low load; later cohorts broaden material/load support. Thirty-six source labels have verified 100×unit flags; deterministic conversion restores declared units. Post-outcome shortcut is excluded by timestamp. Intentionally defective Ridge diagnostic RMSE 6.650736; corrected legitimate-input fixed HGB 4.027567. These multiple repairs are not a causal ablation. Diagnostic new-material high-load RMSE 7.643184 motivates 80 genuinely new source buildings×4, new material/load0.8–1.8. Same fixed recipe refits source plus acquisition, no diagnostic/final observations fit it. On locked final buildings new-material high-load RMSE 6.631408→0.251737 but common-material RMSE 0.614856→3.630669; overall 3.011554→2.724976. This serious shared-model tradeoff is preserved. Final outcomes motivate no further model revision in this run.

## Execution and review boundaries

All eight first fresh-kernel executions pass, producing 33 code cells/17 inline figures with no current stderr or errors. Every current code cell also reruns in a separate exporter process; all deterministic numeric RESULTS match the actual kernel summaries exactly. No resource measurements or stored predictions substitute for computation. Seventeen original SVG/vector-PDF/PNG sets reproduce the experiments. Diagram, axis, legend, count and caption readability are inspected at notebook and book size, then in the compiled second preview. The raw PCA scales, misspecified Gaussian uncertainty, known-censor law, latent labels, exact equation and policy oracle are declared experiment-specific privileges. Initial source-access failures for two historical papers are distinguished from successful publisher records and accessible papers; no inaccessible PDF is claimed to have been inspected. Future chapter scopes and all previous sources remain preserved. Chapters 37–43 and the whole-book editorial/technical audit remain required.
