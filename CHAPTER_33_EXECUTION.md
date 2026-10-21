# Chapter 33 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content tree verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_173 | 33.1 | 4 | 2 | 2.047 |
| code_174 | 33.2 | 4 | 2 | 2.071 |
| code_175 | 33.3 | 4 | 2 | 2.627 |
| code_176 | 33.4 | 4 | 2 | 2.139 |
| code_177 | 33.5 | 4 | 2 | 1.977 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

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

## Successful result dictionaries

### code_173

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 6473.

```json
{
  "buildings": 20000,
  "hidden_alternative_outcomes": 20000,
  "latent_potential_outcome_coupling": "shared uniform; audit only",
  "metrics": {
    "Finite population ATE": -0.0775,
    "Observed association": 0.0602513749190933,
    "Randomized difference": -0.0801641546151631,
    "Selected population ATE": -0.11372236606253734,
    "Treated population ATT": -0.11924854329917621,
    "Two-year population ATE": -0.12025
  },
  "observational_group_risk": {
    "0": 0.11676289070276727,
    "1": 0.17701426562186057
  },
  "observational_treatment_probability_by_severity": [
    0.15,
    0.85
  ],
  "observed_outcomes": 20000,
  "outcome": "failure within one year",
  "selected_buildings": 10042,
  "selected_high_severity_fraction": 0.7996415056761601,
  "treatment": "specified inspection plus repair before year starts",
  "true_mean_risk_ATE": -0.079454,
  "true_mean_risk_ATT": -0.12179626280892103,
  "two_year_assumption": "same annual risk and declared two annual latent draws"
}
```

### code_174

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 6474.

```json
{
  "adjustment_results": [
    {
      "estimand_truth": -1.0,
      "mean_bias": 0.7277134484010896,
      "mean_estimate": -0.27228655159891035,
      "procedure": "Confounded: raw",
      "study_SD": 0.026416356361621342
    },
    {
      "estimand_truth": -1.0,
      "mean_bias": -0.0029135487310258945,
      "mean_estimate": -1.002913548731026,
      "procedure": "Confounded: adjust L",
      "study_SD": 0.021106179926117637
    },
    {
      "estimand_truth": -1.0,
      "mean_bias": 0.00155280512285072,
      "mean_estimate": -0.9984471948771493,
      "procedure": "Randomized: raw",
      "study_SD": 0.04086405417308315
    },
    {
      "estimand_truth": -1.0,
      "mean_bias": -0.0026753174940536972,
      "mean_estimate": -1.0026753174940537,
      "procedure": "Mediator: total",
      "study_SD": 0.029749693018786123
    },
    {
      "estimand_truth": -0.4,
      "mean_bias": 0.0002485813652027824,
      "mean_estimate": -0.39975141863479724,
      "procedure": "Mediator: adjust M",
      "study_SD": 0.029054817636484223
    },
    {
      "estimand_truth": 0.0,
      "mean_bias": 0.0014071780367143397,
      "mean_estimate": 0.0014071780367143397,
      "procedure": "Collider: raw",
      "study_SD": 0.03235987124343244
    },
    {
      "estimand_truth": 0.0,
      "mean_bias": -0.9388984541288931,
      "mean_estimate": -0.9388984541288931,
      "procedure": "Collider: adjust C",
      "study_SD": 0.029754015344234094
    }
  ],
  "adjustment_sets": {
    "collider_total": [],
    "confounder_total": [
      "L"
    ],
    "mediator_total": []
  },
  "buildings_per_study": 2000,
  "collider_true_effect": 0.0,
  "continuous_treatment_unit": "one unit maintenance intensity",
  "deterministic_assignment_bin_counts": [
    [
      247,
      0
    ],
    [
      251,
      0
    ],
    [
      251,
      0
    ],
    [
      251,
      0
    ],
    [
      0,
      251
    ],
    [
      0,
      251
    ],
    [
      0,
      251
    ],
    [
      0,
      247
    ]
  ],
  "mediator_controlled_direct_effect": -0.4,
  "mediator_total_effect": -1.0,
  "positivity_failure_every_load_bin": true,
  "studies": 80
}
```

### code_175

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 6475.

```json
{
  "AIPW": [
    {
      "ATE": -0.6822740597834784,
      "clipped_records": 0,
      "normal_95": [
        -0.7152176962728313,
        -0.6493304232941256
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Flexible",
      "propensity": "Quadratic logistic",
      "scenario": "Moderate",
      "score_SE": 0.016807977800690228
    },
    {
      "ATE": -0.6802481521527965,
      "clipped_records": 0,
      "normal_95": [
        -0.710801527430925,
        -0.6496947768746681
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Flexible",
      "propensity": "Constant",
      "scenario": "Moderate",
      "score_SE": 0.015588456774555335
    },
    {
      "ATE": -0.6846457662617068,
      "clipped_records": 0,
      "normal_95": [
        -0.7272235682271196,
        -0.642067964296294
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Linear",
      "propensity": "Quadratic logistic",
      "scenario": "Moderate",
      "score_SE": 0.021723368349700418
    },
    {
      "ATE": -0.6853439755198908,
      "clipped_records": 0,
      "normal_95": [
        -0.7252922865703584,
        -0.6453956644694232
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Linear",
      "propensity": "Constant",
      "scenario": "Moderate",
      "score_SE": 0.0203817913522794
    },
    {
      "ATE": -0.7363841551161694,
      "clipped_records": 233,
      "normal_95": [
        -0.8334088902091108,
        -0.639359420023228
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Flexible",
      "propensity": "Quadratic logistic",
      "scenario": "Weak",
      "score_SE": 0.04950241586374563
    },
    {
      "ATE": -0.6433341899703766,
      "clipped_records": 0,
      "normal_95": [
        -0.6738645880680882,
        -0.612803791872665
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Flexible",
      "propensity": "Constant",
      "scenario": "Weak",
      "score_SE": 0.015576733723322262
    },
    {
      "ATE": -0.6734756596493883,
      "clipped_records": 233,
      "normal_95": [
        -0.7592238501545763,
        -0.5877274691442003
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Linear",
      "propensity": "Quadratic logistic",
      "scenario": "Weak",
      "score_SE": 0.04374907678836124
    },
    {
      "ATE": -0.6536890533903859,
      "clipped_records": 0,
      "normal_95": [
        -0.6940082908369737,
        -0.613369815943798
      ],
      "oracle_population_mean_effect": -0.7031309713740638,
      "outcome": "Linear",
      "propensity": "Constant",
      "scenario": "Weak",
      "score_SE": 0.020571039513565217
    }
  ],
  "denominator_clip": [
    0.01,
    0.99
  ],
  "diagnostics": [
    {
      "ESS_control": 744.7549897916251,
      "ESS_treated": 938.9368424624876,
      "IPW_ATE": -0.7007821847893094,
      "discarded_treated": 0,
      "matched_treated": 985,
      "matching_retained_ATT": -0.7249974074171263,
      "max_abs_IPW_SMD": 0.008203547178450886,
      "max_abs_raw_SMD": 0.3759466300088472,
      "oracle_propensity_range": [
        0.23182545039740446,
        0.8308156332898039
      ],
      "oracle_retained_ATT": -0.7423192323570162,
      "regression_ATE": -0.6768256612728558,
      "scenario": "Moderate",
      "unique_matched_controls": 475
    },
    {
      "ESS_control": 100.21250423391928,
      "ESS_treated": 181.18020511630533,
      "IPW_ATE": -0.5895058250986618,
      "discarded_treated": 94,
      "matched_treated": 960,
      "matching_retained_ATT": -0.7524315820592918,
      "max_abs_IPW_SMD": 0.20587510475696094,
      "max_abs_raw_SMD": 1.1836943670788782,
      "oracle_propensity_range": [
        0.0024970095030569374,
        0.9996499534508826
      ],
      "oracle_retained_ATT": -0.79866941043632,
      "regression_ATE": -0.6388958575095627,
      "scenario": "Weak",
      "unique_matched_controls": 214
    }
  ],
  "effect_learner": "original RF on cross-fitted AIPW pseudo-outcomes; not honest causal forest",
  "effect_learner_min_leaf": 60,
  "effect_learner_trees": 100,
  "final_buildings": 900,
  "final_outcomes_used_for_nuisance_fitting": 0,
  "fold_ledger": [
    {
      "fit": 1440,
      "fold": 0,
      "held": 360,
      "scenario": "Moderate"
    },
    {
      "fit": 1440,
      "fold": 1,
      "held": 360,
      "scenario": "Moderate"
    },
    {
      "fit": 1440,
      "fold": 2,
      "held": 360,
      "scenario": "Moderate"
    },
    {
      "fit": 1440,
      "fold": 3,
      "held": 360,
      "scenario": "Moderate"
    },
    {
      "fit": 1440,
      "fold": 4,
      "held": 360,
      "scenario": "Moderate"
    },
    {
      "fit": 1440,
      "fold": 0,
      "held": 360,
      "scenario": "Weak"
    },
    {
      "fit": 1440,
      "fold": 1,
      "held": 360,
      "scenario": "Weak"
    },
    {
      "fit": 1440,
      "fold": 2,
      "held": 360,
      "scenario": "Weak"
    },
    {
      "fit": 1440,
      "fold": 3,
      "held": 360,
      "scenario": "Weak"
    },
    {
      "fit": 1440,
      "fold": 4,
      "held": 360,
      "scenario": "Weak"
    }
  ],
  "heterogeneity": [
    {
      "conditional_effect_MAE": 0.0750271598218537,
      "final_buildings": 457,
      "mean_estimated_effect": -0.4396962959358481,
      "oracle_mean_effect": -0.4854541753416316,
      "region": "Low load",
      "reportable": true,
      "scenario": "Moderate",
      "source_controls_treated": [
        478,
        420
      ]
    },
    {
      "conditional_effect_MAE": 0.05634758722723598,
      "final_buildings": 443,
      "mean_estimated_effect": -0.9004337957254647,
      "oracle_mean_effect": -0.9124530112380621,
      "region": "High load",
      "reportable": true,
      "scenario": "Moderate",
      "source_controls_treated": [
        337,
        565
      ]
    },
    {
      "conditional_effect_MAE": null,
      "final_buildings": 1,
      "mean_estimated_effect": null,
      "oracle_mean_effect": -1.037151416831122,
      "region": "Sparse joint tail",
      "reportable": false,
      "scenario": "Moderate",
      "source_controls_treated": [
        0,
        1
      ]
    },
    {
      "conditional_effect_MAE": 0.1679355392620171,
      "final_buildings": 457,
      "mean_estimated_effect": -0.5452811648776629,
      "oracle_mean_effect": -0.4854541753416316,
      "region": "Low load",
      "reportable": true,
      "scenario": "Weak",
      "source_controls_treated": [
        602,
        296
      ]
    },
    {
      "conditional_effect_MAE": 0.11618281211832986,
      "final_buildings": 443,
      "mean_estimated_effect": -0.9418869110298631,
      "oracle_mean_effect": -0.9124530112380621,
      "region": "High load",
      "reportable": true,
      "scenario": "Weak",
      "source_controls_treated": [
        144,
        758
      ]
    },
    {
      "conditional_effect_MAE": null,
      "final_buildings": 1,
      "mean_estimated_effect": null,
      "oracle_mean_effect": -1.037151416831122,
      "region": "Sparse joint tail",
      "reportable": false,
      "scenario": "Weak",
      "source_controls_treated": [
        0,
        1
      ]
    }
  ],
  "matching_caliper_logit_SD": 0.2,
  "matching_target": "ATT among retained treated buildings; replacement allowed",
  "minimum_final_group": 20,
  "minimum_source_per_arm": 40,
  "nuisance_folds": 5,
  "source_buildings_per_scenario": 1800
}
```

### code_176

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 6476.

```json
{
  "ANM": [
    {
      "HSIC": 0.0004486816610743091,
      "direction": "X to Y",
      "held_out_MSE": 0.09799123622132133,
      "permutation_p": 0.62
    },
    {
      "HSIC": 0.0044814146895537,
      "direction": "Y to X",
      "held_out_MSE": 0.042211363226837356,
      "permutation_p": 0.01
    }
  ],
  "ANM_fit_records": 500,
  "ANM_test_records": 300,
  "DAGs": [
    {
      "BIC": 4183.776982714109,
      "edges": []
    },
    {
      "BIC": 1805.3983255862504,
      "edges": [
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": 3348.801689174522,
      "edges": [
        [
          2,
          0
        ]
      ]
    },
    {
      "BIC": 970.4230320466629,
      "edges": [
        [
          2,
          0
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": 1805.398325586251,
      "edges": [
        [
          1,
          2
        ]
      ]
    },
    {
      "BIC": 970.4230320466638,
      "edges": [
        [
          1,
          2
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "BIC": 2318.77866235926,
      "edges": [
        [
          1,
          0
        ]
      ]
    },
    {
      "BIC": -59.59999476859912,
      "edges": [
        [
          1,
          0
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": 2325.5909021413277,
      "edges": [
        [
          1,
          0
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "BIC": -52.78775498653158,
      "edges": [
        [
          1,
          0
        ],
        [
          2,
          0
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": -59.59999476859811,
      "edges": [
        [
          1,
          0
        ],
        [
          1,
          2
        ]
      ]
    },
    {
      "BIC": -52.78775498653057,
      "edges": [
        [
          1,
          0
        ],
        [
          1,
          2
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "BIC": 3348.801689174522,
      "edges": [
        [
          0,
          2
        ]
      ]
    },
    {
      "BIC": 970.4230320466631,
      "edges": [
        [
          0,
          2
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": 1812.2105653683186,
      "edges": [
        [
          0,
          2
        ],
        [
          1,
          2
        ]
      ]
    },
    {
      "BIC": 1483.8033688196729,
      "edges": [
        [
          0,
          2
        ],
        [
          1,
          0
        ]
      ]
    },
    {
      "BIC": -52.787754986530665,
      "edges": [
        [
          0,
          2
        ],
        [
          1,
          0
        ],
        [
          1,
          2
        ]
      ]
    },
    {
      "BIC": 2318.7786623592597,
      "edges": [
        [
          0,
          1
        ]
      ]
    },
    {
      "BIC": 782.1875385530559,
      "edges": [
        [
          0,
          1
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": 1483.8033688196724,
      "edges": [
        [
          0,
          1
        ],
        [
          2,
          0
        ]
      ]
    },
    {
      "BIC": -52.78775498653158,
      "edges": [
        [
          0,
          1
        ],
        [
          2,
          0
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": -59.59999476859841,
      "edges": [
        [
          0,
          1
        ],
        [
          1,
          2
        ]
      ]
    },
    {
      "BIC": 1483.8033688196726,
      "edges": [
        [
          0,
          1
        ],
        [
          0,
          2
        ]
      ]
    },
    {
      "BIC": -52.787754986531354,
      "edges": [
        [
          0,
          1
        ],
        [
          0,
          2
        ],
        [
          2,
          1
        ]
      ]
    },
    {
      "BIC": -52.78775498653096,
      "edges": [
        [
          0,
          1
        ],
        [
          0,
          2
        ],
        [
          1,
          2
        ]
      ]
    }
  ],
  "HSIC_permutations": 99,
  "conditional_tests": [
    {
      "condition_on": 2,
      "conditional_p": 5.3618260641958175e-226,
      "marginal_p": 0.0,
      "pair": [
        0,
        1
      ]
    },
    {
      "condition_on": 1,
      "conditional_p": 0.27477863627613625,
      "marginal_p": 3.462432828447513e-185,
      "pair": [
        0,
        2
      ]
    },
    {
      "condition_on": 0,
      "conditional_p": 0.0,
      "marginal_p": 0.0,
      "pair": [
        1,
        2
      ]
    }
  ],
  "equivalent_orientation_BIC": [
    -59.59999476859841,
    -59.59999476859912,
    -59.59999476859811
  ],
  "full_PC_or_LiNGAM_replication": false,
  "gaussian_records": 3000,
  "hidden_common_loading": true,
  "skeleton": [
    [
      0,
      1
    ],
    [
      1,
      2
    ]
  ],
  "temporal_final_records": 300,
  "temporal_fit_records": 700,
  "temporal_prediction": [
    {
      "X_lag_coefficient": null,
      "future_MSE": 1.01200165093624,
      "predictor": "Y lag"
    },
    {
      "X_lag_coefficient": 0.8580283553304864,
      "future_MSE": 0.1805338854741575,
      "predictor": "Y + X lag"
    },
    {
      "X_lag_coefficient": -0.01807839715408281,
      "future_MSE": 0.03806087133071627,
      "predictor": "Y + X + U lag"
    }
  ],
  "true_sensor_intervention_effect": 0.0,
  "variable_order": [
    "X",
    "Z",
    "Y"
  ]
}
```

### code_177

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 6477.

```json
{
  "beam": {
    "E_Pa": 200000000000.0,
    "I_m4": 8e-06,
    "inverse_load_N": 4800.0,
    "original_deflection_mm": 8.333333333333334,
    "original_load_N": 10000.0,
    "span_m": 4.0,
    "target_deflection_mm": 4.0,
    "verified_deflection_mm": 4.0
  },
  "declared_structural_load_effect": 0.5,
  "desired_outcome_change": -1.0,
  "feasible_applied_load_change": -0.5230335742327886,
  "individual_exogenous_residual_held_fixed": true,
  "observational_load_slope": 1.91192315228874,
  "prediction_change": -1.0,
  "recourse_proposed_load_change": -0.5230335742327886,
  "required_true_load_change": -2.0,
  "sensitivity": {
    "adjusted_effect": [
      1.91192315228874,
      1.8509920676029366,
      1.7900609829171332,
      1.7291298982313297,
      1.6681988135455261,
      1.6072677288597228,
      1.5463366441739193,
      1.4854055594881157,
      1.4244744748023122,
      1.3635433901165088,
      1.3026123054307055,
      1.2416812207449017,
      1.1807501360590984,
      1.119819051373295,
      1.0588879666874913,
      0.9979568820016879,
      0.9370257973158844,
      0.8760947126300809,
      0.8151636279442775,
      0.754232543258474,
      0.6933014585726707,
      0.6323703738868671,
      0.5714392892010636,
      0.51050820451526,
      0.4495771198294565,
      0.38864603514365337,
      0.3277149504578498,
      0.26678386577204627,
      0.20585278108624272,
      0.14492169640043917,
      0.08399061171463562,
      0.023059527028832294,
      -0.037871557656971255,
      -0.09880264234277503,
      -0.15973372702857835,
      -0.22066481171438168,
      -0.281595896400185,
      -0.3425269810859888,
      -0.4034580657717921,
      -0.4643891504575959,
      -0.5253202351433988
    ],
    "assumed_hidden_load_covariance": 0.8,
    "assumption_not_identified_from_observed_records": true,
    "gamma_grid": [
      0.0,
      0.05,
      0.1,
      0.15000000000000002,
      0.2,
      0.25,
      0.30000000000000004,
      0.35000000000000003,
      0.4,
      0.45,
      0.5,
      0.55,
      0.6000000000000001,
      0.65,
      0.7000000000000001,
      0.75,
      0.8,
      0.8500000000000001,
      0.9,
      0.9500000000000001,
      1.0,
      1.05,
      1.1,
      1.1500000000000001,
      1.2000000000000002,
      1.25,
      1.3,
      1.35,
      1.4000000000000001,
      1.4500000000000002,
      1.5,
      1.55,
      1.6,
      1.6500000000000001,
      1.7000000000000002,
      1.75,
      1.8,
      1.85,
      1.9000000000000001,
      1.9500000000000002,
      2.0
    ]
  },
  "source_buildings": 3000,
  "structural_counterfactual_change": -0.26151678711639414,
  "target_outcomes_used_for_source_fit_or_selection": 0,
  "transport": [
    {
      "independent_randomized_target_difference": -0.5975172813239462,
      "naive_source_average_effect": -0.29999368035340973,
      "setting": "Changed mix",
      "target_high_load_fraction": 0.7995,
      "target_standardized_source_effect": -0.5868872157144908,
      "true_target_effect": -0.59975
    },
    {
      "independent_randomized_target_difference": 0.05274125021690157,
      "naive_source_average_effect": -0.29999368035340973,
      "setting": "Changed response",
      "target_high_load_fraction": 0.7995,
      "target_standardized_source_effect": -0.5868872157144908,
      "true_target_effect": 0.03985
    }
  ],
  "transport_source_buildings": 4000,
  "transport_target_buildings_per_setting": 2000,
  "true_target_feasible": false,
  "unit_index": 0,
  "unit_observed_load": 2.665762048195564
}
```


## Publication and visual evidence

Content revision `e44ccc94dc2fd14ca7f3e0accd0e34eabf05a363` matches remote main and all 300 remote file blobs. Five independent fresh-kernel notebooks execute 20 code cells and produce ten reviewed inline figures. Every current source cell is rerun for vector-book export with exact deterministic numeric RESULTS equality. All 18 Chapter 33 pages, ten book figures, six equations, five-row companion map and twenty exercises are visually reviewed, together with updated front matter and all four reference pages. The separate second preview has 67 pages, SHA-256 `62794cff84b597e6ad9ba6dd61cb84ac9ecbe95d16d5b869fffbd965b6ed7b91`; Chapter 33 occupies printed 526–543 / PDF 46–63. Final explanatory additions clarify double robustness, faithfulness and population policy value; all changed pages were reviewed and other candidate renders match by hashes. The 42 earlier second-preview body pages are pixel-identical. The first preview through Chapter 30 remains byte-identical. All 204 prior chapter/notebook files and 172 prior manifest records are preserved. Final publication metadata and commit-addressed raw files are verified separately. Only companion artifacts are published here; manuscript pages and book figures remain local.
