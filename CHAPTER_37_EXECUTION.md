# Chapter 37 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_196 | 37.1 | 4 | 2 | 2.421 |
| code_197 | 37.2 | 4 | 2 | 1.651 |
| code_198 | 37.3 | 5 | 3 | 1.849 |
| code_199 | 37.4 | 4 | 2 | 1.545 |
| code_200 | 37.5 | 4 | 2 | 1.582 |

Total: **21 executed code cells and 11 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

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

## Successful result dictionaries

### code_196

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7896.

```json
{
  "bin_intervals_not_simultaneous": true,
  "building_roles": [
    1000,
    600,
    600
  ],
  "final_prevalence": 0.4033333333333333,
  "plugin_ECE": {
    "Boost: Calibrated": 0.0397976094117098,
    "Boost: Stress raw": 0.1434606699822157,
    "Typed neural: Calibrated": 0.05420477512181288,
    "Typed neural: Stress raw": 0.14976961750934145
  },
  "probability_scores": {
    "Boost: Calibrated": {
      "AUC": 0.7948370192529665,
      "Brier": 0.1809794424364092,
      "log_loss": 0.536262515382947,
      "mean_probability": 0.43280831547264287,
      "negative_class_mean_probability": 0.33029547903945805,
      "positive_class_mean_probability": 0.5844595363118171,
      "probability_variance": 0.06178709711900827
    },
    "Boost: Stress raw": {
      "AUC": 0.7948370192529665,
      "Brier": 0.2006229647259891,
      "log_loss": 0.6650500294527525,
      "mean_probability": 0.4192674816497035,
      "negative_class_mean_probability": 0.2695727136330189,
      "positive_class_mean_probability": 0.6407167665669476,
      "probability_variance": 0.13834926858777577
    },
    "Typed neural: Calibrated": {
      "AUC": 0.8073433676531696,
      "Brier": 0.17545414216556002,
      "log_loss": 0.5203693147839429,
      "mean_probability": 0.4330808143130023,
      "negative_class_mean_probability": 0.3193973130646617,
      "positive_class_mean_probability": 0.6012572335150933,
      "probability_variance": 0.06957598547505531
    },
    "Typed neural: Stress raw": {
      "AUC": 0.8073433676531696,
      "Brier": 0.19852881539091033,
      "log_loss": 0.6590963455921396,
      "mean_probability": 0.4169110536845132,
      "negative_class_mean_probability": 0.2580172388701857,
      "positive_class_mean_probability": 0.6519688458478573,
      "probability_variance": 0.14730219102385078
    }
  },
  "raw_logit_stress_multiplier": 2,
  "reliability_bins": {
    "Boost: Calibrated": [
      {
        "Wilson95": [
          0.029204086165362186,
          0.1486119392585393
        ],
        "bin": 0,
        "frequency": 0.06756756756756757,
        "mean_probability": 0.05895861248076114,
        "n": 74
      },
      {
        "Wilson95": [
          0.07829411405317006,
          0.25343393711554596
        ],
        "bin": 1,
        "frequency": 0.14516129032258066,
        "mean_probability": 0.15064815421417502,
        "n": 62
      },
      {
        "Wilson95": [
          0.132425514176991,
          0.31974978216205835
        ],
        "bin": 2,
        "frequency": 0.2112676056338028,
        "mean_probability": 0.24924303380084353,
        "n": 71
      },
      {
        "Wilson95": [
          0.23714253215255424,
          0.45662760613335107
        ],
        "bin": 3,
        "frequency": 0.3382352941176471,
        "mean_probability": 0.3522084796952594,
        "n": 68
      },
      {
        "Wilson95": [
          0.27595007375002106,
          0.5061579719398692
        ],
        "bin": 4,
        "frequency": 0.38461538461538464,
        "mean_probability": 0.4523564156278095,
        "n": 65
      },
      {
        "Wilson95": [
          0.337425457881576,
          0.5414844567895197
        ],
        "bin": 5,
        "frequency": 0.4367816091954023,
        "mean_probability": 0.5461960073150665,
        "n": 87
      },
      {
        "Wilson95": [
          0.5192506510138936,
          0.731245773968965
        ],
        "bin": 6,
        "frequency": 0.631578947368421,
        "mean_probability": 0.6500143535024738,
        "n": 76
      },
      {
        "Wilson95": [
          0.582414363751211,
          0.8306343663031736
        ],
        "bin": 7,
        "frequency": 0.723404255319149,
        "mean_probability": 0.7461167847236047,
        "n": 47
      },
      {
        "Wilson95": [
          0.7745231869447662,
          0.9614029151019106
        ],
        "bin": 8,
        "frequency": 0.9024390243902439,
        "mean_probability": 0.8424457193830144,
        "n": 41
      },
      {
        "Wilson95": [
          0.5650002944233439,
          0.9801091123614551
        ],
        "bin": 9,
        "frequency": 0.8888888888888888,
        "mean_probability": 0.9338178316081766,
        "n": 9
      }
    ],
    "Boost: Stress raw": [
      {
        "Wilson95": [
          0.09934735698452568,
          0.19396051124306968
        ],
        "bin": 0,
        "frequency": 0.14009661835748793,
        "mean_probability": 0.02325643353666933,
        "n": 207
      },
      {
        "Wilson95": [
          0.23219082604215874,
          0.5016418580362314
        ],
        "bin": 1,
        "frequency": 0.35555555555555557,
        "mean_probability": 0.14701791832219646,
        "n": 45
      },
      {
        "Wilson95": [
          0.2218717823524236,
          0.5338382169773361
        ],
        "bin": 2,
        "frequency": 0.36363636363636365,
        "mean_probability": 0.24304492781182657,
        "n": 33
      },
      {
        "Wilson95": [
          0.21532512960965597,
          0.5577076558789761
        ],
        "bin": 3,
        "frequency": 0.37037037037037035,
        "mean_probability": 0.34413603021728423,
        "n": 27
      },
      {
        "Wilson95": [
          0.2070582950773768,
          0.5416969348557219
        ],
        "bin": 4,
        "frequency": 0.35714285714285715,
        "mean_probability": 0.44880962828569027,
        "n": 28
      },
      {
        "Wilson95": [
          0.18565932306911137,
          0.4642125437414931
        ],
        "bin": 5,
        "frequency": 0.3076923076923077,
        "mean_probability": 0.5501085149481771,
        "n": 39
      },
      {
        "Wilson95": [
          0.3818972506848375,
          0.6953398071159278
        ],
        "bin": 6,
        "frequency": 0.5428571428571428,
        "mean_probability": 0.6514751343008341,
        "n": 35
      },
      {
        "Wilson95": [
          0.3838404689217949,
          0.6896143019562697
        ],
        "bin": 7,
        "frequency": 0.5405405405405406,
        "mean_probability": 0.7503543146993029,
        "n": 37
      },
      {
        "Wilson95": [
          0.5418970269185592,
          0.7924178373934316
        ],
        "bin": 8,
        "frequency": 0.68,
        "mean_probability": 0.8564258439438805,
        "n": 50
      },
      {
        "Wilson95": [
          0.7195963938569909,
          0.8735496067880852
        ],
        "bin": 9,
        "frequency": 0.8080808080808081,
        "mean_probability": 0.9637526492222233,
        "n": 99
      }
    ],
    "Typed neural: Calibrated": [
      {
        "Wilson95": [
          0.007443352638267217,
          0.09329292516912502
        ],
        "bin": 0,
        "frequency": 0.02702702702702703,
        "mean_probability": 0.054958972084935935,
        "n": 74
      },
      {
        "Wilson95": [
          0.0795654064460579,
          0.23237331588651916
        ],
        "bin": 1,
        "frequency": 0.13924050632911392,
        "mean_probability": 0.15004784419067296,
        "n": 79
      },
      {
        "Wilson95": [
          0.16487913818578948,
          0.3692919453950009
        ],
        "bin": 2,
        "frequency": 0.2537313432835821,
        "mean_probability": 0.24848009523925133,
        "n": 67
      },
      {
        "Wilson95": [
          0.3047758590777194,
          0.5433441525515342
        ],
        "bin": 3,
        "frequency": 0.41935483870967744,
        "mean_probability": 0.35017320830653753,
        "n": 62
      },
      {
        "Wilson95": [
          0.2589572436016878,
          0.4802022912619641
        ],
        "bin": 4,
        "frequency": 0.36231884057971014,
        "mean_probability": 0.45180362887975417,
        "n": 69
      },
      {
        "Wilson95": [
          0.23884988425189946,
          0.4538338185724453
        ],
        "bin": 5,
        "frequency": 0.3380281690140845,
        "mean_probability": 0.5502422367920753,
        "n": 71
      },
      {
        "Wilson95": [
          0.5599646825583142,
          0.7841331334648034
        ],
        "bin": 6,
        "frequency": 0.6825396825396826,
        "mean_probability": 0.6543858007802748,
        "n": 63
      },
      {
        "Wilson95": [
          0.6277574244984441,
          0.8639672541377281
        ],
        "bin": 7,
        "frequency": 0.7659574468085106,
        "mean_probability": 0.7463319364290295,
        "n": 47
      },
      {
        "Wilson95": [
          0.6986022402737561,
          0.9111363612350974
        ],
        "bin": 8,
        "frequency": 0.8297872340425532,
        "mean_probability": 0.8420481127127122,
        "n": 47
      },
      {
        "Wilson95": [
          0.7108586092608176,
          0.9734812325619255
        ],
        "bin": 9,
        "frequency": 0.9047619047619048,
        "mean_probability": 0.926048700126586,
        "n": 21
      }
    ],
    "Typed neural: Stress raw": [
      {
        "Wilson95": [
          0.09721661085910067,
          0.1879917645555434
        ],
        "bin": 0,
        "frequency": 0.13636363636363635,
        "mean_probability": 0.0222743438509516,
        "n": 220
      },
      {
        "Wilson95": [
          0.2968272340851781,
          0.5777585300637057
        ],
        "bin": 1,
        "frequency": 0.4318181818181818,
        "mean_probability": 0.14860154258475525,
        "n": 44
      },
      {
        "Wilson95": [
          0.2070582950773768,
          0.5416969348557219
        ],
        "bin": 2,
        "frequency": 0.35714285714285715,
        "mean_probability": 0.24684884716478353,
        "n": 28
      },
      {
        "Wilson95": [
          0.21116659093865403,
          0.5305204593563113
        ],
        "bin": 3,
        "frequency": 0.3548387096774194,
        "mean_probability": 0.34812385841932264,
        "n": 31
      },
      {
        "Wilson95": [
          0.2356568654157959,
          0.5759095570340281
        ],
        "bin": 4,
        "frequency": 0.39285714285714285,
        "mean_probability": 0.45156211291934756,
        "n": 28
      },
      {
        "Wilson95": [
          0.18643261498715644,
          0.5217523949267991
        ],
        "bin": 5,
        "frequency": 0.3333333333333333,
        "mean_probability": 0.5414344817435096,
        "n": 27
      },
      {
        "Wilson95": [
          0.12218422442520088,
          0.42107601617811335
        ],
        "bin": 6,
        "frequency": 0.2413793103448276,
        "mean_probability": 0.6522570693838362,
        "n": 29
      },
      {
        "Wilson95": [
          0.3919730700081361,
          0.7262251442353347
        ],
        "bin": 7,
        "frequency": 0.5666666666666667,
        "mean_probability": 0.7464866418320106,
        "n": 30
      },
      {
        "Wilson95": [
          0.5833487630404344,
          0.8252582933408878
        ],
        "bin": 8,
        "frequency": 0.72,
        "mean_probability": 0.8560364253866541,
        "n": 50
      },
      {
        "Wilson95": [
          0.7325480865089783,
          0.8751129331035653
        ],
        "bin": 9,
        "frequency": 0.8141592920353983,
        "mean_probability": 0.9701757137426162,
        "n": 113
      }
    ]
  },
  "temperature": {
    "Boost": 2.6077170290222673,
    "Typed neural": 2.5800411621685266
  },
  "typed_record_schema_is_not_calibration": true,
  "typed_records_validated": 600
}
```

### code_197

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 7897.

```json
{
  "Bayesian_posterior_df": 804.0,
  "Bayesian_predictive_MC_draws": 20000,
  "Bayesian_predictive_independent_MC_quantile_max_error_mm": 0.003399377995904951,
  "Bayesian_prior_alpha": 2.0,
  "Bayesian_prior_beta": 0.1,
  "Bayesian_prior_precision_diagonal": 0.01,
  "assessment_familiar": 400,
  "assessment_new_load": 400,
  "bootstrap_members": 30,
  "bootstrap_predictive_draws_per_case": 300,
  "distributional_optimizer_success": true,
  "future_response_law_changes_above_load1": true,
  "interval_scores": {
    "Bayesian parameter only": {
      "Familiar": {
        "coverage": 0.0875,
        "mean_width_mm": 0.08730428703025513
      },
      "New load": {
        "coverage": 0.165,
        "mean_width_mm": 0.4396077833429034
      }
    },
    "Bayesian predictive": {
      "Familiar": {
        "coverage": 0.8925,
        "mean_width_mm": 1.3061448465805932
      },
      "New load": {
        "coverage": 0.5225,
        "mean_width_mm": 1.3891954037128251
      }
    },
    "Bootstrap mean only": {
      "Familiar": {
        "coverage": 0.0625,
        "mean_width_mm": 0.0704504381907341
      },
      "New load": {
        "coverage": 0.18,
        "mean_width_mm": 0.4848539907743952
      }
    },
    "Bootstrap predictive": {
      "Familiar": {
        "coverage": 0.8625,
        "mean_width_mm": 1.300805705695273
      },
      "New load": {
        "coverage": 0.53,
        "mean_width_mm": 1.3866531360104977
      }
    },
    "Gaussian conditional": {
      "Familiar": {
        "coverage": 0.86,
        "mean_width_mm": 1.22847705557233
      },
      "New load": {
        "coverage": 0.895,
        "mean_width_mm": 2.708897439461246
      }
    },
    "Quantiles": {
      "Familiar": {
        "coverage": 0.83,
        "mean_width_mm": 1.1349836828862818
      },
      "New load": {
        "coverage": 0.77,
        "mean_width_mm": 1.7731391889753656
      }
    }
  },
  "parameter_interval_outcome_coverage_is_diagnostic_only": true,
  "raw_quantile_crossing_fraction": 0.0,
  "source_records": 800
}
```

### code_198

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 7898.

```json
{
  "CQR_group_correction": 0.2689848610383958,
  "CQR_rank": 181,
  "CQR_scores": {
    "Familiar": {
      "building_all3_coverage": 0.8966666666666666,
      "mean_width": 1.8263036302583087,
      "row_coverage": 0.9622222222222222
    },
    "Shifted": {
      "building_all3_coverage": 0.19333333333333333,
      "mean_width": 1.8630334254713918,
      "row_coverage": 0.43444444444444447
    }
  },
  "alpha": 0.1,
  "building_roles": [
    1000,
    200,
    300,
    300
  ],
  "classification_set_scores": {
    "Familiar: Building max": {
      "building_all3_coverage": 0.8966666666666666,
      "empty_fraction": 0.0,
      "mean_set_size": 1.6244444444444444,
      "row_coverage": 0.9577777777777777
    },
    "Familiar: Pooled row diagnostic": {
      "building_all3_coverage": 0.7233333333333334,
      "empty_fraction": 0.0,
      "mean_set_size": 1.3388888888888888,
      "row_coverage": 0.8944444444444445
    },
    "Shifted: Building max": {
      "building_all3_coverage": 0.8766666666666667,
      "empty_fraction": 0.0,
      "mean_set_size": 1.7022222222222223,
      "row_coverage": 0.9422222222222222
    },
    "Shifted: Pooled row diagnostic": {
      "building_all3_coverage": 0.6933333333333334,
      "empty_fraction": 0.0,
      "mean_set_size": 1.4111111111111112,
      "row_coverage": 0.8366666666666667
    }
  },
  "group_exchangeability_claim": "marginal over a new building, simultaneous all three labels",
  "group_rank": 181,
  "group_threshold": 0.8374744251459233,
  "label_delay_buildings": 10,
  "pooled_row_rank": 541,
  "pooled_row_threshold": 0.6865064986654899,
  "records_per_building": 3,
  "rolling_window_buildings": 80,
  "shifted_law_violates_exchangeability": true,
  "temporal_blocks": [
    {
      "arrivals": [
        0,
        79
      ],
      "fixed_building_coverage": 0.95,
      "rolling_building_coverage": 0.875
    },
    {
      "arrivals": [
        80,
        159
      ],
      "fixed_building_coverage": 0.9,
      "rolling_building_coverage": 0.875
    },
    {
      "arrivals": [
        160,
        239
      ],
      "fixed_building_coverage": 0.925,
      "rolling_building_coverage": 0.9125
    }
  ],
  "temporal_exchangeability_guarantee_claimed": false
}
```

### code_199

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 7899.

```json
{
  "assumed_full_avoided_loss_not_estimated_effect": true,
  "candidates_per_day": 30,
  "capacity_each_day": 10,
  "day_roles": [
    60,
    15,
    10,
    35
  ],
  "decision_curve_all": [
    0.21102756892230576,
    0.1897039897039897,
    0.16719576719576718,
    0.14340136054421768,
    0.11820728291316523,
    0.09148629148629148,
    0.0630952380952381,
    0.03287250384024573,
    0.0006349206349206271,
    -0.03382594417077178,
    -0.07074829931972793,
    -0.11040564373897704,
    -0.15311355311355324,
    -0.19923809523809516,
    -0.2492063492063492,
    -0.3035196687370601,
    -0.3627705627705628,
    -0.42766439909297066,
    -0.499047619047619,
    -0.5779448621553887,
    -0.6656084656084658,
    -0.7635854341736696,
    -0.873809523809524,
    -0.9987301587301591,
    -1.1414965986394565,
    -1.3062271062271062,
    -1.4984126984126989,
    -1.7255411255411264,
    -1.998095238095239,
    -2.3312169312169333,
    -2.7476190476190485
  ],
  "decision_curve_is_descriptive_not_policy_selection": true,
  "decision_curve_model": [
    0.21644110275689224,
    0.2025997425997426,
    0.18867724867724867,
    0.17346938775510204,
    0.16280112044817924,
    0.15174603174603174,
    0.14523809523809522,
    0.13557603686635944,
    0.1307936507936508,
    0.1225944170771757,
    0.11714285714285713,
    0.10991181657848324,
    0.09912087912087911,
    0.096,
    0.08190476190476191,
    0.0743271221532091,
    0.07038961038961039,
    0.06480725623582764,
    0.0676190476190476,
    0.06110275689223057,
    0.05396825396825396,
    0.049859943977591026,
    0.04428571428571427,
    0.039365079365079346,
    0.04312925170068025,
    0.033186813186813185,
    0.03682539682539682,
    0.04268398268398268,
    0.03714285714285714,
    0.02878306878306877,
    0.030476190476190476
  ],
  "decision_curve_thresholds": [
    0.05,
    0.07500000000000001,
    0.1,
    0.125,
    0.15000000000000002,
    0.175,
    0.2,
    0.22500000000000003,
    0.25,
    0.275,
    0.3,
    0.325,
    0.35000000000000003,
    0.375,
    0.4,
    0.425,
    0.45,
    0.47500000000000003,
    0.5,
    0.525,
    0.55,
    0.5750000000000001,
    0.6000000000000001,
    0.6250000000000001,
    0.6500000000000001,
    0.675,
    0.7000000000000001,
    0.7250000000000001,
    0.7500000000000001,
    0.7750000000000001,
    0.8
  ],
  "first_day_admitted_sorted": [
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    true,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false,
    false
  ],
  "first_day_expected_net_utility_sorted": [
    7.957813592689039,
    6.160517279200798,
    5.100831368598177,
    2.7212059890219398,
    2.679979394645949,
    2.441739236135543,
    2.373527018495859,
    2.175320088394274,
    2.0528747430113845,
    1.4651115885701964,
    0.9219939512796729,
    0.6212137086254623,
    0.5592547947247624,
    0.362534778430359,
    0.24387720148726988,
    0.22661670711056825,
    0.08424607518275984,
    0.03767474098383827,
    -0.06271472901094555,
    -0.3867340447672638,
    -1.043398445477774,
    -1.5862306905362593,
    -1.842969380682812,
    -1.9740871775811513,
    -2.198880004444234,
    -2.2616813433344616,
    -2.682706019166668,
    -2.8474125321763397,
    -3.4274390225325484,
    -3.8925441100794447
  ],
  "first_final_day": 85,
  "policy_scores": {
    "Risk top10": {
      "daily_capacity_max_used": 10,
      "daily_realized_utility": [
        20.336793972020107,
        1.6097378990988633,
        52.44239265353071,
        35.82088898472098,
        62.80904742308543,
        62.03481082353278,
        49.803566827251046,
        24.466617861902186,
        35.60480610294749,
        12.84556597065582,
        23.952401301874104,
        36.0199253725713,
        27.226667224770488,
        43.50306055945151,
        -13.685791973687717,
        67.18538942032141,
        65.60691086596843,
        -2.5071769989929766,
        35.71371323136246,
        24.59385589468176,
        54.446823426971825,
        10.92019442140381,
        15.046563579350654,
        6.078185802031253,
        51.679629633406634,
        70.19959670484656,
        62.597244951864056,
        10.681396598745229,
        22.043739097280497,
        46.96268530409418,
        -9.04648908128988,
        30.590068194988817,
        56.8458115526662,
        41.423959721097425,
        24.298884760323148
      ],
      "inspections_per_day": 10.0,
      "realized_utility_per_day": 33.14718508813848,
      "simulator_expected_utility_per_day": 35.64567140494714
    },
    "Threshold": {
      "daily_capacity_max_used": 10,
      "daily_realized_utility": [
        20.336793972020107,
        1.6097378990988633,
        52.44239265353071,
        35.82088898472098,
        62.80904742308543,
        62.03481082353278,
        49.803566827251046,
        24.466617861902186,
        35.60480610294749,
        12.84556597065582,
        23.952401301874104,
        36.0199253725713,
        27.226667224770488,
        43.50306055945151,
        -13.685791973687717,
        67.18538942032141,
        65.60691086596843,
        -2.5071769989929766,
        35.71371323136246,
        24.59385589468176,
        54.446823426971825,
        10.92019442140381,
        15.046563579350654,
        6.078185802031253,
        51.679629633406634,
        70.19959670484656,
        62.597244951864056,
        10.681396598745229,
        22.043739097280497,
        46.96268530409418,
        -9.04648908128988,
        30.590068194988817,
        56.8458115526662,
        41.423959721097425,
        24.298884760323148
      ],
      "inspections_per_day": 10.0,
      "realized_utility_per_day": 33.14718508813848,
      "simulator_expected_utility_per_day": 35.64567140494714
    },
    "Utility": {
      "daily_capacity_max_used": 10,
      "daily_realized_utility": [
        23.833700182406936,
        18.064678899244583,
        51.165919492197304,
        32.559708873593436,
        64.73171593990492,
        74.15490710303833,
        68.46947781702089,
        30.1357175728431,
        31.400406310053437,
        37.66707828206601,
        34.04602063612513,
        42.91832935054748,
        17.324369938441443,
        32.00646617240113,
        9.806830077621736,
        78.7106933237174,
        90.00593101789339,
        -12.13979274394368,
        56.890448517021774,
        25.53685861714696,
        54.446823426971825,
        6.398725834671853,
        5.206985213842426,
        22.208990856455785,
        63.18554721127798,
        73.8927554284314,
        59.22796292268838,
        6.596508734752568,
        25.076338739256606,
        51.8054710792985,
        -7.958193779197192,
        26.780626879243684,
        45.184947143002134,
        43.76278554322513,
        22.70736322917712
      ],
      "inspections_per_day": 9.942857142857143,
      "realized_utility_per_day": 37.30894582406971,
      "simulator_expected_utility_per_day": 39.92745268035665
    }
  },
  "selected_probability_threshold": 0.05
}
```

### code_200

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 7900.

```json
{
  "arrivals_per_day": 10,
  "building_roles": [
    1000,
    400,
    400,
    1000
  ],
  "chosen_selection_policy": null,
  "days_with_any_accepted_error": 0.0,
  "development_constraint_is_not_risk_guarantee": true,
  "empirical_selection_max_review": 0.3,
  "empirical_selection_target_risk": 0.12,
  "eventual_combined_error": 0.016,
  "final_accepted_risk": null,
  "final_arrival_days": 100,
  "final_automation_coverage": 0.0,
  "final_curve_descriptive_only": {
    "Confidence only": [
      {
        "accepted_risk": 0.446,
        "automation_coverage": 1.0,
        "threshold": 0.5
      },
      {
        "accepted_risk": 0.4444444444444444,
        "automation_coverage": 0.99,
        "threshold": 0.51
      },
      {
        "accepted_risk": 0.4458077709611452,
        "automation_coverage": 0.978,
        "threshold": 0.52
      },
      {
        "accepted_risk": 0.44593202883625127,
        "automation_coverage": 0.971,
        "threshold": 0.53
      },
      {
        "accepted_risk": 0.4440961337513062,
        "automation_coverage": 0.957,
        "threshold": 0.54
      },
      {
        "accepted_risk": 0.4440928270042194,
        "automation_coverage": 0.948,
        "threshold": 0.55
      },
      {
        "accepted_risk": 0.4450317124735729,
        "automation_coverage": 0.946,
        "threshold": 0.56
      },
      {
        "accepted_risk": 0.4456404736275565,
        "automation_coverage": 0.929,
        "threshold": 0.5700000000000001
      },
      {
        "accepted_risk": 0.4452871072589382,
        "automation_coverage": 0.923,
        "threshold": 0.58
      },
      {
        "accepted_risk": 0.4472252448313384,
        "automation_coverage": 0.919,
        "threshold": 0.59
      },
      {
        "accepted_risk": 0.44945054945054946,
        "automation_coverage": 0.91,
        "threshold": 0.6
      },
      {
        "accepted_risk": 0.4481236203090508,
        "automation_coverage": 0.906,
        "threshold": 0.61
      },
      {
        "accepted_risk": 0.4497767857142857,
        "automation_coverage": 0.896,
        "threshold": 0.62
      },
      {
        "accepted_risk": 0.45106861642294716,
        "automation_coverage": 0.889,
        "threshold": 0.63
      },
      {
        "accepted_risk": 0.45307068366164543,
        "automation_coverage": 0.863,
        "threshold": 0.64
      },
      {
        "accepted_risk": 0.45507584597432904,
        "automation_coverage": 0.857,
        "threshold": 0.65
      },
      {
        "accepted_risk": 0.4594272076372315,
        "automation_coverage": 0.838,
        "threshold": 0.66
      },
      {
        "accepted_risk": 0.4601449275362319,
        "automation_coverage": 0.828,
        "threshold": 0.67
      },
      {
        "accepted_risk": 0.45985401459854014,
        "automation_coverage": 0.822,
        "threshold": 0.6799999999999999
      },
      {
        "accepted_risk": 0.46494464944649444,
        "automation_coverage": 0.813,
        "threshold": 0.69
      },
      {
        "accepted_risk": 0.4679245283018868,
        "automation_coverage": 0.795,
        "threshold": 0.7
      },
      {
        "accepted_risk": 0.46835443037974683,
        "automation_coverage": 0.79,
        "threshold": 0.71
      },
      {
        "accepted_risk": 0.46946564885496184,
        "automation_coverage": 0.786,
        "threshold": 0.72
      },
      {
        "accepted_risk": 0.4711168164313222,
        "automation_coverage": 0.779,
        "threshold": 0.73
      },
      {
        "accepted_risk": 0.4729381443298969,
        "automation_coverage": 0.776,
        "threshold": 0.74
      },
      {
        "accepted_risk": 0.47334200260078024,
        "automation_coverage": 0.769,
        "threshold": 0.75
      },
      {
        "accepted_risk": 0.4739583333333333,
        "automation_coverage": 0.768,
        "threshold": 0.76
      },
      {
        "accepted_risk": 0.47706422018348627,
        "automation_coverage": 0.763,
        "threshold": 0.77
      },
      {
        "accepted_risk": 0.4789473684210526,
        "automation_coverage": 0.76,
        "threshold": 0.78
      },
      {
        "accepted_risk": 0.4820717131474104,
        "automation_coverage": 0.753,
        "threshold": 0.79
      },
      {
        "accepted_risk": 0.4898785425101215,
        "automation_coverage": 0.741,
        "threshold": 0.8
      },
      {
        "accepted_risk": 0.49586776859504134,
        "automation_coverage": 0.726,
        "threshold": 0.81
      },
      {
        "accepted_risk": 0.5049365303244006,
        "automation_coverage": 0.709,
        "threshold": 0.8200000000000001
      },
      {
        "accepted_risk": 0.5071225071225072,
        "automation_coverage": 0.702,
        "threshold": 0.8300000000000001
      },
      {
        "accepted_risk": 0.5122655122655123,
        "automation_coverage": 0.693,
        "threshold": 0.8400000000000001
      },
      {
        "accepted_risk": 0.5183016105417276,
        "automation_coverage": 0.683,
        "threshold": 0.8500000000000001
      },
      {
        "accepted_risk": 0.5299401197604791,
        "automation_coverage": 0.668,
        "threshold": 0.86
      },
      {
        "accepted_risk": 0.5462962962962963,
        "automation_coverage": 0.648,
        "threshold": 0.87
      },
      {
        "accepted_risk": 0.5691056910569106,
        "automation_coverage": 0.615,
        "threshold": 0.88
      },
      {
        "accepted_risk": 0.584873949579832,
        "automation_coverage": 0.595,
        "threshold": 0.89
      },
      {
        "accepted_risk": 0.6017391304347826,
        "automation_coverage": 0.575,
        "threshold": 0.9
      },
      {
        "accepted_risk": 0.6123893805309735,
        "automation_coverage": 0.565,
        "threshold": 0.91
      },
      {
        "accepted_risk": 0.6245487364620939,
        "automation_coverage": 0.554,
        "threshold": 0.9199999999999999
      },
      {
        "accepted_risk": 0.634862385321101,
        "automation_coverage": 0.545,
        "threshold": 0.9299999999999999
      },
      {
        "accepted_risk": 0.6528301886792452,
        "automation_coverage": 0.53,
        "threshold": 0.94
      },
      {
        "accepted_risk": 0.6699029126213593,
        "automation_coverage": 0.515,
        "threshold": 0.95
      },
      {
        "accepted_risk": 0.6927710843373494,
        "automation_coverage": 0.498,
        "threshold": 0.96
      },
      {
        "accepted_risk": 0.7360515021459227,
        "automation_coverage": 0.466,
        "threshold": 0.97
      },
      {
        "accepted_risk": 0.8103896103896104,
        "automation_coverage": 0.385,
        "threshold": 0.98
      },
      {
        "accepted_risk": 0.8782051282051282,
        "automation_coverage": 0.312,
        "threshold": 0.99
      }
    ],
    "Support gate": [
      {
        "accepted_risk": 0.15933232169954475,
        "automation_coverage": 0.659,
        "threshold": 0.5
      },
      {
        "accepted_risk": 0.15254237288135594,
        "automation_coverage": 0.649,
        "threshold": 0.51
      },
      {
        "accepted_risk": 0.14913657770800628,
        "automation_coverage": 0.637,
        "threshold": 0.52
      },
      {
        "accepted_risk": 0.14603174603174604,
        "automation_coverage": 0.63,
        "threshold": 0.53
      },
      {
        "accepted_risk": 0.13636363636363635,
        "automation_coverage": 0.616,
        "threshold": 0.54
      },
      {
        "accepted_risk": 0.13179571663920922,
        "automation_coverage": 0.607,
        "threshold": 0.55
      },
      {
        "accepted_risk": 0.1322314049586777,
        "automation_coverage": 0.605,
        "threshold": 0.56
      },
      {
        "accepted_risk": 0.12414965986394558,
        "automation_coverage": 0.588,
        "threshold": 0.5700000000000001
      },
      {
        "accepted_risk": 0.12027491408934708,
        "automation_coverage": 0.582,
        "threshold": 0.58
      },
      {
        "accepted_risk": 0.12110726643598616,
        "automation_coverage": 0.578,
        "threshold": 0.59
      },
      {
        "accepted_risk": 0.1195079086115993,
        "automation_coverage": 0.569,
        "threshold": 0.6
      },
      {
        "accepted_risk": 0.11504424778761062,
        "automation_coverage": 0.565,
        "threshold": 0.61
      },
      {
        "accepted_risk": 0.11171171171171171,
        "automation_coverage": 0.555,
        "threshold": 0.62
      },
      {
        "accepted_risk": 0.10948905109489052,
        "automation_coverage": 0.548,
        "threshold": 0.63
      },
      {
        "accepted_risk": 0.09578544061302682,
        "automation_coverage": 0.522,
        "threshold": 0.64
      },
      {
        "accepted_risk": 0.09496124031007752,
        "automation_coverage": 0.516,
        "threshold": 0.65
      },
      {
        "accepted_risk": 0.08853118712273642,
        "automation_coverage": 0.497,
        "threshold": 0.66
      },
      {
        "accepted_risk": 0.08213552361396304,
        "automation_coverage": 0.487,
        "threshold": 0.67
      },
      {
        "accepted_risk": 0.07692307692307693,
        "automation_coverage": 0.481,
        "threshold": 0.6799999999999999
      },
      {
        "accepted_risk": 0.07838983050847458,
        "automation_coverage": 0.472,
        "threshold": 0.69
      },
      {
        "accepted_risk": 0.06828193832599119,
        "automation_coverage": 0.454,
        "threshold": 0.7
      },
      {
        "accepted_risk": 0.0645879732739421,
        "automation_coverage": 0.449,
        "threshold": 0.71
      },
      {
        "accepted_risk": 0.06292134831460675,
        "automation_coverage": 0.445,
        "threshold": 0.72
      },
      {
        "accepted_risk": 0.0593607305936073,
        "automation_coverage": 0.438,
        "threshold": 0.73
      },
      {
        "accepted_risk": 0.059770114942528735,
        "automation_coverage": 0.435,
        "threshold": 0.74
      },
      {
        "accepted_risk": 0.053738317757009345,
        "automation_coverage": 0.428,
        "threshold": 0.75
      },
      {
        "accepted_risk": 0.053864168618266976,
        "automation_coverage": 0.427,
        "threshold": 0.76
      },
      {
        "accepted_risk": 0.054502369668246446,
        "automation_coverage": 0.422,
        "threshold": 0.77
      },
      {
        "accepted_risk": 0.05489260143198091,
        "automation_coverage": 0.419,
        "threshold": 0.78
      },
      {
        "accepted_risk": 0.05339805825242718,
        "automation_coverage": 0.412,
        "threshold": 0.79
      },
      {
        "accepted_risk": 0.055,
        "automation_coverage": 0.4,
        "threshold": 0.8
      },
      {
        "accepted_risk": 0.04935064935064935,
        "automation_coverage": 0.385,
        "threshold": 0.81
      },
      {
        "accepted_risk": 0.04619565217391304,
        "automation_coverage": 0.368,
        "threshold": 0.8200000000000001
      },
      {
        "accepted_risk": 0.04155124653739612,
        "automation_coverage": 0.361,
        "threshold": 0.8300000000000001
      },
      {
        "accepted_risk": 0.03977272727272727,
        "automation_coverage": 0.352,
        "threshold": 0.8400000000000001
      },
      {
        "accepted_risk": 0.038011695906432746,
        "automation_coverage": 0.342,
        "threshold": 0.8500000000000001
      },
      {
        "accepted_risk": 0.039755351681957186,
        "automation_coverage": 0.327,
        "threshold": 0.86
      },
      {
        "accepted_risk": 0.04234527687296417,
        "automation_coverage": 0.307,
        "threshold": 0.87
      },
      {
        "accepted_risk": 0.032846715328467155,
        "automation_coverage": 0.274,
        "threshold": 0.88
      },
      {
        "accepted_risk": 0.027559055118110236,
        "automation_coverage": 0.254,
        "threshold": 0.89
      },
      {
        "accepted_risk": 0.021367521367521368,
        "automation_coverage": 0.234,
        "threshold": 0.9
      },
      {
        "accepted_risk": 0.022321428571428572,
        "automation_coverage": 0.224,
        "threshold": 0.91
      },
      {
        "accepted_risk": 0.023474178403755867,
        "automation_coverage": 0.213,
        "threshold": 0.9199999999999999
      },
      {
        "accepted_risk": 0.024509803921568627,
        "automation_coverage": 0.204,
        "threshold": 0.9299999999999999
      },
      {
        "accepted_risk": 0.026455026455026454,
        "automation_coverage": 0.189,
        "threshold": 0.94
      },
      {
        "accepted_risk": 0.022988505747126436,
        "automation_coverage": 0.174,
        "threshold": 0.95
      },
      {
        "accepted_risk": 0.025477707006369428,
        "automation_coverage": 0.157,
        "threshold": 0.96
      },
      {
        "accepted_risk": 0.016,
        "automation_coverage": 0.125,
        "threshold": 0.97
      },
      {
        "accepted_risk": 0.013513513513513514,
        "automation_coverage": 0.074,
        "threshold": 0.98
      },
      {
        "accepted_risk": 0.0,
        "automation_coverage": 0.038,
        "threshold": 0.99
      }
    ]
  },
  "final_labels_update_policy": false,
  "final_review_fraction": 1.0,
  "final_unsupported_fraction": 0.341,
  "locked_threshold": 1.01,
  "maximum_daily_backlog": 700,
  "maximum_review_completion_delay_days": 234,
  "mean_review_completion_delay_days": 116.667,
  "pending_reviews_at_day100": 700,
  "review_capacity_per_day": 3,
  "review_error_probability_simulator": 0.02,
  "review_outcome_additional_delay_days": 3,
  "selection_policy_feasible": false,
  "service_cost_per_case": 8.0,
  "temperature": 1.1078120727522234,
  "total_service_cost_units": 8000.0
}
```


## Publication and visual evidence

Content revision `9b1d45a5c330fb5e3e42e36f070f709c8cf4bfbb` matches remote main and all 341 remote file blobs. Five independent fresh-kernel notebooks execute21 code cells/11 reviewed inline figures. Every current cell reruns in an isolated exporter with exact scientific RESULTS equality; independent Bayesian posterior Monte Carlo quantile error0.003399 mm. All16 Chapter37 pages,11 book figures,5 equations,5-row map and20 exercises are reviewed, plus4 front-matter/7 references pages. Main2 has158 pages, SHA256 `491651faf6a0cc477dfb5b5942d9690e903038277fd1191ebae9466530db0f2a`; Chapter37 printed615–630/PDF136–151. The one-page preview guide was repaired after an observed spill and reviewed in the final build. All131 earliersecondbodypages are pixel-identical; firstPDFbyte-identical.231 prior source/notebook files and195 prior manifest rows preserved. No dependency or asset added. Final metadata/raw-byte checks follow separately. Only companion artifacts are published.
