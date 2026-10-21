# Chapter 33: Causal learning and intervention — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_33_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 33.1 · Causal questions and estimands

- [Name the action, population and outcome before estimating anything](notebooks/173_Chapter_33_01_causal_questions_estimands_and_selection.ipynb#defined-treatment-and-target)
- [Cutting an assignment mechanism is an extra claim](notebooks/173_Chapter_33_01_causal_questions_estimands_and_selection.ipynb#prediction-versus-intervention)

Declared mechanisms: explicit potential outcomes for a defined inspection plus repair policy, observational assignment randomized assignment and simulator-only audit truth, ATE ATT target-population and time-window distinctions, selection changes the target estimand, intervention graph cuts assignment rather than predicting a group risk.

```bash
python scripts/run_notebook.py notebooks/173_Chapter_33_01_causal_questions_estimands_and_selection.ipynb
```

## 33.2 · Identification and study design

- [Compare adjustment rules under three known data-generating graphs](notebooks/174_Chapter_33_02_identification_design_and_bad_controls.ipynb#graph-specific-adjustment)
- [Observe when an adjustment set cannot supply a missing comparison](notebooks/174_Chapter_33_02_identification_design_and_bad_controls.ipynb#adjustment-sets-and-overlap)

Declared mechanisms: actual repeated confounder mediator and collider structural simulations, randomized treatment control and declared total versus direct effects, observed regression adjustment can remove or introduce bias, structural positivity failure diagnosed by load regions, three defined DAGs with proposed adjustment sets.

```bash
python scripts/run_notebook.py notebooks/174_Chapter_33_02_identification_design_and_bad_controls.ipynb
```

## 33.3 · Effect estimation with machine learning

- [Keep effect targets, nuisance fitting and oracle audits separate](notebooks/175_Chapter_33_03_cross_fitting_matching_weighting_and_heterogeneity.ipynb#cross-fitted-average-effects)
- [Use an independent target cohort and refuse tiny subgroup claims](notebooks/175_Chapter_33_03_cross_fitting_matching_weighting_and_heterogeneity.ipynb#held-out-effect-heterogeneity)

Declared mechanisms: actual regression adjustment propensity matching IPW and cross-fitted AIPW, five held-out nuisance folds with explicit misspecification contrasts, overlap clipping balance arm-specific effective sample sizes and matching retention, distinct ATE and retained-treated ATT targets, original pseudo-outcome effect learner with independent assessment and minimum support.

```bash
python scripts/run_notebook.py notebooks/175_Chapter_33_03_cross_fitting_matching_weighting_and_heterogeneity.ipynb
```

## 33.4 · Causal discovery and dynamical relationships

- [Discover candidates without inventing a unique direction](notebooks/176_Chapter_33_04_causal_discovery_equivalence_and_temporal_prediction.ipynb#equivalence-and-functional-assumptions)
- [Temporal prediction does not eliminate common causes](notebooks/176_Chapter_33_04_causal_discovery_equivalence_and_temporal_prediction.ipynb#lag-prediction-with-hidden-loading)

Declared mechanisms: actual Gaussian conditional-correlation skeleton tests, all 25 three-node DAGs scored with free-variance Gaussian BIC, Markov-equivalent orientations retained, held-out nonlinear additive-noise regression and kernel residual-dependence permutation tests, temporal predictive gain under a hidden common cause separated from intervention effect.

```bash
python scripts/run_notebook.py notebooks/176_Chapter_33_04_causal_discovery_equivalence_and_temporal_prediction.ipynb
```

## 33.5 · Counterfactuals, interventions and sensitivity

- [A changed prediction is not an identified action effect](notebooks/177_Chapter_33_05_counterfactual_interventions_and_transport_sensitivity.ipynb#structural-counterfactual-and-inverse-scenario)
- [State what an unobserved bias and a new setting could change](notebooks/177_Chapter_33_05_counterfactual_interventions_and_transport_sensitivity.ipynb#sensitivity-and-target-settings)

Declared mechanisms: explicit structural abduction action prediction with fixed exogenous residual, observational recourse contrasted with true structural load effect and feasibility, known-equation beam inverse scenario with units, hidden-confounding sensitivity can change an effect sign, covariate-shift transport versus changed response mechanism on independent targets.

```bash
python scripts/run_notebook.py notebooks/177_Chapter_33_05_counterfactual_interventions_and_transport_sensitivity.ipynb
```

## Interpretation and boundaries

### Chapter 33 evidence and runtime

The chapter is added only to the growing second preview, main_2.tex / output/pdf/main_2.pdf, with references_2.tex and its own How to use this preview. The first preview through Chapter 30 is fixed. Chapter 33 was prepared once with 204 preserved chapter/notebook hashes and 172 manifest records. All earlier second-preview body pages, prior source/manifest records and outline identities/scopes/visual briefs must pass preservation checks before delivery.

Five independent generated-data laboratories use the unchanged CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and Torch 2.14.1 CPU environment. One thread and deterministic operations; no new package, asset, network call, credential or GPU. Every notebook defines its imports, helpers, fitting data and assessment roles internally. Each has four executed code cells and two inline figures. Every current source cell is re-executed for vector figures and exact deterministic numeric RESULTS equality is required. No resource observation is replayed as computation.

### Actual mechanisms and preserved counterexamples

173: 20,000 independent generated buildings, binary severity and continuous load. The treatment is a specified inspection-plus-repair protocol before the year starts, not simply an inspection flag. Baseline annual failure probability 0.03+0.25severity+0.1load; reduction 0.02+0.12severity. Actual observational assignment probabilities 0.15/0.85. Paired potential outcomes use a common latent uniform for audit; each observed record contains only its assigned outcome. Observed association +0.060251 versus finite-population potential-outcome ATE −0.0775, independently randomized difference −0.080164 and observationally treated ATT −0.119249. Probability-scale mean ATE −0.079454 and ATT −0.121796 are distinct from realized binary differences. Selection with severity-dependent inclusion yields 10,042 cases, high-severity fraction 0.799642 and selected effect −0.113722. Two-year finite effect −0.12025 uses declared persistent annual risks and two annual latent draws, not observed follow-up. The intervention DAG cuts the incoming assignment arrow; displayed alternative outcomes remain unknown. Final bar labels were wrapped for clearance without changing metrics.

174: eighty independent repetitions, each 2,000 buildings, continuous maintenance intensity in three explicit linear structural systems. Confounding: true per-unit effect −1, raw estimate mean −0.272287/SD 0.026416; load-adjusted −1.002914/SD 0.021106; independently randomized raw −0.998447/SD 0.040864. Mediator: total coefficient −0.4+(−0.75×0.8)=−1; unadjusted −1.002675 and mediator-conditioned −0.399751, correctly labelled controlled-direct target −0.4 under its independent-error construction. Collider: randomized treatment has true effect zero, raw mean 0.001407 and collider-conditioned −0.938898. Study SDs are not a single-study confidence interval. Separate deterministic assignment by load sign leaves exactly one arm missing in all eight load intervals. The three DAGs define L/A/M/C/U/Y and proposed sets for a total effect.

175: 1,800 source buildings under each of two fixed assignment strengths 1/5, shared covariates and noise generator. Three measured covariates; nonlinear baseline deterioration, conditional effect −0.7−0.4x0, quadratic-logistic propensity. Five folds each fit 1,440 and predict 360 held-out records. Treated/untreated outcome models: HistGradientBoostingRegressor 80 iterations/max7 leaves/min20/l2=1 versus misspecified linear regression. Propensity: quadratic features/source-fitted scale/logistic C10/max500 versus intentionally constant0.5. Actual cross-fitted AIPW scores, regression standardization and ordinary IPW are implemented. All settings fixed before oracle assessment; no nuisance selection from oracle or final outcomes.

Moderate overlap oracle ATE −0.703131. Flexible regression −0.676826/IPW −0.700782/flexible-quadratic AIPW −0.682274 (score SE 0.016808, normal interval [−0.715218,−0.649330]). Other moderate AIPW contrasts −0.680248/−0.684646/−0.685344, with all four empirical intervals covering this oracle. Weak flexible-quadratic AIPW −0.736384 (SE 0.049502, interval [−0.833409,−0.639359]); flexible-constant −0.643334 (SE 0.015577, interval [−0.673865,−0.612804]) misses truth despite apparent precision. Weak linear-quadratic −0.673476 and linear-constant −0.653689; the latter interval also misses. These are single constructed cohorts, not coverage-rate experiments or guaranteed causal intervals.

Estimated denominator clipping [0.01,0.99] affects 233 weak records and zero moderate records. It changes the estimating score and can bias the full ATE; it is not relabelled as a new overlap-population estimand. Arm ESS moderate treated/control 938.936842/744.754990, weak 181.180205/100.212504. Max absolute SMD across original covariates and squares improves 0.375947→0.008204 moderate and 1.183694→0.205875 weak. Native weighting does not silently use oracle propensities. Actual nearest propensity-logit matching with replacement/caliper0.2logitSD targets retained-treated ATT. Moderate 985 retained/zero discarded/475 unique controls, estimate −0.724997 versus retained ATT oracle −0.742319. Weak 960 retained/94 discarded/214 unique controls, estimate −0.752432 versus target oracle −0.798669. Matching's changed target and reused controls are explicit; no naive independent-pair confidence interval is claimed.

An original 100-tree/minleaf60 regression forest fits cross-fitted flexible/quadratic AIPW pseudo-outcomes. It is not an honest causal forest. Independent 900-record covariates and known conditional-effect truth assess fixed low/high-load groups; outcomes never fit source nuisances. Moderate low/high mean estimates −0.439696/−0.900434 versus oracles −0.485454/−0.912453, conditional-effect MAE0.075027/0.056348. Weak low/high estimates −0.545281/−0.941887, MAE0.167936/0.116183. Prespecified minimum40source cases per arm and20final cases refuses a sparse joint tail (source controls/treated[0,1], one final record); estimated value and MAE remain null. Axis margins and refusal annotations were repaired and rerun without metric changes.

176: 3,000 independent Gaussian chain records, variables X/Z/Y. Actual marginal and one-variable partial-correlation tests use alpha0.01; conditional t test df2997. Skeleton [[X,Z],[Z,Y]]; endpoint conditional p0.274779. All25three-node DAGs are enumerated, acyclicity checked and free-variance Gaussian BIC fitted. Chain/reverse/fork BICs agree near −59.59999477 to below1e−9. No unsupported single orientation is selected. This is not full PC or LiNGAM. A separate nonlinear additive-noise system uses500fit/300held-out records, degree-five polynomial regression/Ridge1e−6/source-only scaling, centered Gaussian-kernel HSIC and99permutations. Forward residual p0.62/MSE0.097991; reverse p0.01/MSE0.042211. MSE targets have different units and do not rank causal direction. The p-values are not probabilities of independence or causal arrows. The partial-correlation degrees-of-freedom calculation was corrected before publication and its fresh source rerun; no model or threshold was selected from causal direction scores. Equivalent-score markers were added for visibility and rerun.

Temporal common-load example: hidden AR loading drives sensor at t−1 and outcome at t with no sensor→outcome structural edge. Models fit700earlier records and assess300later records. Y-lag MSE1.012002; adding X-lag0.180534 with X coefficient0.858028; adding the actual hidden U-lag in an explicitly oracle comparison0.038061 with X coefficient−0.018078. This exposes temporal predictive gain under a known zero sensor-intervention effect. It is not an intervention identification claim from arbitrary Granger tests or a field causal graph.

177: 3,000 source load/deterioration records, hidden common U. Load equation2+0.8U+noise0.2; outcome0.5load+1.2U+noise0.2. Observational load slope1.911923 versus declared structural0.5. Fixed eligible unit0 has load2.665762. Desired outcome reduction1, observational recourse proposes load change−0.523034 within action limit0.6/minimum load0.7. Prediction promises−1; structural counterfactual gives−0.261517 holding the combined residual fixed. True required load change−2 is infeasible. This is a declared structural scenario, not separately identified U/noise or verified individual field potential outcomes. Beam inverse: E200GPa/I8e−6m4/span4m/load10,000N gives8.333333mm; inverse target4mm yields4,800N and verified4mm. It validates equations/units only, not a failure-risk intervention or material-property estimate.

Hidden-bias sensitivity varies gamma0–2 assuming covariance(U,L)=0.8; the range crosses zero. The covariance and range are assumptions, not identified from observed load/outcome data or empirically calibrated plausible bounds. A separate source randomized study uses4,000buildings, binary high-load modifier prevalence0.2 and treatment effects−0.2/−0.7. Independent2,000-building target settings use high-load fraction0.7995. Estimated source mean−0.299994; target-standardized source effect−0.586887 versus invariant-mechanism target truth−0.59975 and target randomized difference−0.597517. Changed high-load response becomes+0.1, giving true target mean+0.03985 / randomized difference+0.052741 while the same standardization still predicts−0.586887. Target covariates support standardization; target outcomes never choose or refit source models.

### Primary sources and interpretation limits

Eight primary records support potential-outcome framing, graphical intervention/backdoor adjustment, propensity-score context, orthogonal scores/cross-fitting, honest-forest distinctions, Gaussian graph equivalence, nonlinear independent-noise models and structural recourse. Pearl's author-hosted R350 paper, DML v7 (3 November2024), Wager/Athey v4 (July2017), Kalisch/Bühlmann and Hoyer et al. primary method text, and Karimi et al. abduction/action discussion were inspected. Rubin's institutional record and Rosenbaum/Rubin's original journal/archive metadata were verified; the latter full publisher text was unavailable, so no claim to have inspected its full proof is made. Failed unrelated guessed lookups in the initial plan are excluded. Published JASA and FAccT venue details were verified against publisher/author-institution records. Sources predate18October2026; access21October2026.

Every task and effect is generated, and causal identification depends on the declared mechanism and study assumptions. Finite-cohort oracle outcomes, known structural coefficients, true hidden loading and counterfactual audit truth are not information secretly admitted to field estimators. Normal score intervals, descriptive repetition SD and a discovery p-value have distinct meanings. No claim of general interval coverage, universal double robustness, a complete causal-method library, field causal identification or verified individual action benefit is made. Runner transport notices remain in process logs; current notebook stderr is empty. Final exact-PDF visual and remote publication proofs are recorded after they pass.
