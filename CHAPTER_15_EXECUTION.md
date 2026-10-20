# Chapter 15 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verification passed.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_072 | 15.1 | 4 | 2 | 1.545 |
| code_073 | 15.2 | 4 | 2 | 1.462 |
| code_074 | 15.3 | 4 | 2 | 1.996 |
| code_075 | 15.4 | 4 | 2 | 1.551 |
| code_076 | 15.5 | 4 | 2 | 1.488 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed. Shorter panel titles repair the identified collisions; labels, shared axes and distinct line styles are clear.

## Actual mechanisms and boundaries

Five generated-data CPU laboratories use seeds 1572–1576 and the unchanged Python 3.14.3 / NumPy 2.4.4 / SciPy 1.17.1 / pandas 3.0.3 / Matplotlib 3.11.0 / scikit-learn 1.9.0 environment. All current notebooks execute in fresh kernels without error outputs or solver warnings. code_076 initially reached its summary with a NumPy int 64 leaf count that JSON could not serialize; converting that count to Python int repaired the reporting boundary and its fresh run passes. code_072 reran after clarifying a reporting-loss field; code_074 reran after adding the separate p>n algebra audit. code_075 reran after clarifying that its clipped ramps form a piecewise-linear load spline; the current result dictionaries agree exactly with the original registered report. Visual review caught colliding titles in notebook panels073,075,076; shorter titles repaired them and fresh kernels retained exactly the registered result dictionaries. Current timings belong to current sources. No dependency was added; ordinary execution is offline and self-contained.

The strain laboratory uses 240 training, 100 unused reserved development and 400 clean final observations. Exactly twelve training responses receive +180 microstrain contamination. Fixed OLS, Huber(epsilon 1.35, alpha 0) and quantile(.1,.5,.9, alpha 0) models use the same load feature. OLS/Huber/median slopes are 1.863631/2.001519/2.032093 microstrain per kN; final MSE is 158.5001/79.1505/80.1145. Final fractions below q 10/q 90 are .0825/.95 and their empirical interval coverage is .8675, not guaranteed nominal .8. Orthogonality of the OLS residual to its fitted design is numerically verified; duplicate load columns have rank 2 with three columns, and a [0,7,-7] coefficient perturbation preserves predictions. Neither audit establishes inference assumptions, a causal law or robustness to predictor leverage.

The GLM laboratory has 600 training, 200 unused development and 400 final records. Bernoulli failure and inspection counts are separate outcomes. Counts have log exposure offset and a Gamma(shape2,scale.5) rate multiplier, giving variance mu+mu²/2. The explicit Poisson working likelihood passes gradient error 1.64e-8 and matches an unpenalized exposure-weighted rate fit within 2e-5 coefficient tolerance. Fitted coefficients [.1223195,.6615078] compare with declared [.1,.7]; training Pearson dispersion is 1.6200 and final mean Pearson residual square is 1.5804. Final observed/predicted mean counts are 1.5225/1.5447. Mean count two gives positive-event chance .864665 under Poisson and .75 under the generated mixture. No negative-binomial fit or significance test is claimed. Failure Brier/log loss is .205868/.602950 on 121 events in 400 rows.

Correlated sensors use training 90/development 120/final 400 with twelve features and A/B correlation .999721. Common objective SSE/(2 n)+lambda*(rho*L 1+(1-rho)*L 2²/2) implies Ridge alpha=n*lambda, Lasso alpha=lambda and ElasticNet alpha=lambda,rho=.5. Each family independently selects lambda .0811131 using development MSE. Final MSEs Ridge/Lasso/ElasticNet are .339376/.329724/.330161. Sixty training-row bootstrap draws refit scalers but condition on each selected penalty; they do not repeat tuning. Lasso A/B coefficient SDs .735086/.738685 contrast with summed SD .056579 and selection frequencies .4/.816667. Mean fixed-final-covariate prediction SDs are .175774/.105886/.128567 for the three families. A separate24-row/40-column algebra fixture interpolates with rank 24 and a null direction preserving every prediction; Ridge at penalty .1 reduces norm with training MSE 2.06e-5. That separate audit makes no held-out generalization claim. Paths use exactly the same data/common lambda and highlight the correlated pair.

The additive logistic laboratory uses train 350/development 150/calibration 300/final 400 plus a locked 200-record temperature-zero slice. Generated risk is sigmoid(-2+3*load²+1.5*temperature²). Four clipped ramps with nonnegative coefficients enforce nondecreasing load logits; a training-fitted cubic temperature B-spline has free coefficients. Development chooses penalty .001. Load increments [0,.217827,1.671465,.902634] and a dense-grid check verify the stated shape. Raw final linear/additive log loss is .586065/.575679 and Brier .199369/.193511. Locked-slice log loss is .566530/.553058. Independent isotonic calibration changes final Brier to .193496 but worsens 1e-6-clipped log loss to .652219, with 22 empirical endpoint predictions. The worse result is retained. Additivity is on the link scale; the load ramps saturate and temperature spline has constant extension outside declared support. No causal interpretation, comprehensive GAM library or out-of-support physical validity is asserted.

Finite expression search uses train 250/development 120/final 300 under the declared simply supported central-load relation delta=P*L³/(48EI) with .1 mm noise. Three predeclared dimensionally valid dictionaries fit dimensionless coefficients; development MSE+1e-9 m² per term selects the beam term alone. Coefficient .0208438668 compares with 1/48; final MSE 1.06857738e-8 m² is .010685774 mm². A unitless coefficient multiplying P/EI is rejected because it cannot produce a length; a differently dimensioned coefficient would describe another contract. Unit conversion is checked. This favorable finite dictionary already contains the true synthetic form and is not unrestricted symbolic discovery. Fixed decision list, sparse integer score, four-leaf tree and a logistic ensemble of four fixed rules achieve observed >3 mm flag accuracy .563333/.716667/.876667/.856667, separately expression-flag agreement .56/.713333/.88/.86. No final-driven rule changes, field safety threshold or RuleFit implementation is claimed.

Ten original SVG/vector-PDF/PNG figure sets implement the linear/additive common-cohort and correlated shrinkage-path briefs plus loss, count, resampling, calibration and dimensional-fidelity mechanisms. Five equations and eight connected exercises retain the fitting/inference distinction. Official quantile, Poisson, spline and isotonic documentation and the primary Friedman/Hastie/Tibshirani 2010 JSS path paper were inspected 20 October 2026. Documentation maintenance version 1.9.1 versus executed 1.9.0 is disclosed. The book is a bounded synthetic teaching draft, not external empirical validation.

## Successful result dictionaries

### code_072

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1572.

```json
{
  "fits": [
    {
      "final_fraction_below_prediction": 0.8325,
      "final_mae": 10.56828289252839,
      "final_mse": 158.50005855697137,
      "final_pinball_at_reporting_quantile": 5.284141446264195,
      "intercept_microstrain": 114.31805481208684,
      "model": "OLS",
      "slope_microstrain_per_kN": 1.8636314295835532
    },
    {
      "final_fraction_below_prediction": 0.5025,
      "final_mae": 7.012372051343032,
      "final_mse": 79.15053058065752,
      "final_pinball_at_reporting_quantile": 3.506186025671516,
      "intercept_microstrain": 100.31304915629819,
      "model": "Huber",
      "slope_microstrain_per_kN": 2.0015190321003997
    },
    {
      "final_fraction_below_prediction": 0.46,
      "final_mae": 7.041545840264938,
      "final_mse": 80.1145378360066,
      "final_pinball_at_reporting_quantile": 3.520772920132469,
      "intercept_microstrain": 98.42688480625068,
      "model": "Median",
      "slope_microstrain_per_kN": 2.0320928319584635
    },
    {
      "final_fraction_below_prediction": 0.0825,
      "final_mae": 12.490054790246226,
      "final_mse": 222.092805132007,
      "final_pinball_at_reporting_quantile": 1.5210403030343942,
      "intercept_microstrain": 92.84607230391126,
      "model": "q10",
      "slope_microstrain_per_kN": 1.8912267948998345
    },
    {
      "final_fraction_below_prediction": 0.95,
      "final_mae": 14.967871680915282,
      "final_mse": 298.2719438386823,
      "final_pinball_at_reporting_quantile": 1.6315543440616478,
      "intercept_microstrain": 110.2386157700555,
      "model": "q90",
      "slope_microstrain_per_kN": 2.1246937840018187
    }
  ],
  "geometry": {
    "duplicate_design_columns": 3,
    "inference_assumptions_established": false,
    "null_direction": [
      0,
      7,
      -7
    ],
    "rank": 2,
    "training_normal_equations_checked": true
  },
  "protocol": {
    "clean_final": 400,
    "contaminated_training_rows": 12,
    "final_q10_q90_coverage": 0.8675,
    "quantile_crossings_in_final": 0,
    "train": 240,
    "unused_development": 100
  }
}
```

### code_073

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1573.

```json
{
  "count_fit": {
    "final_count_mean": 1.5225,
    "final_mean_squared_count_error": 2.6455478142285913,
    "final_pearson_ratio_mean": 1.5804343798376632,
    "final_prediction_mean": 1.5447327258397672,
    "gradient_error": 1.64063485248818e-08,
    "offset_coefficients": [
      0.1223195428924368,
      0.6615077773916107
    ],
    "training_pearson_dispersion": 1.6200140460636812,
    "true_coefficients": [
      0.1,
      0.7
    ],
    "weighted_rate_equivalence_passed": true
  },
  "count_probability_at_mean_two": {
    "Poisson_probability_positive": 0.8646647167633873,
    "generated_mixture_probability_positive": 0.75,
    "mean": 2.0,
    "variance_of_generated_count": 4.0
  },
  "failure_fit": {
    "final_brier": 0.20586770115377356,
    "final_events": 121,
    "final_log_loss": 0.6029500863649523,
    "final_rows": 400
  },
  "roles": {
    "final": 400,
    "no_selection": true,
    "reserved_development_unused": 200,
    "train": 600
  }
}
```

### code_074

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1574.

```json
{
  "bootstrap_draws": 60,
  "common_objective": "SSE/(2n)+lambda*(rho*L1+(1-rho)*L2_squared/2); intercept unpenalized",
  "conditional_bootstrap": [
    {
      "A_B_coefficient_sd": [
        0.029083791637830026,
        0.03202504772942464
      ],
      "A_B_sum_sd": 0.059038123299848144,
      "family": "Ridge",
      "mean_final_probe_prediction_sd": 0.1757744253296349,
      "selection_frequency": [
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0
      ]
    },
    {
      "A_B_coefficient_sd": [
        0.7350855049614079,
        0.7386845928856243
      ],
      "A_B_sum_sd": 0.056579183487905624,
      "family": "Lasso",
      "mean_final_probe_prediction_sd": 0.1058860293589634,
      "selection_frequency": [
        0.4,
        0.8166666666666667,
        1.0,
        0.15,
        0.5833333333333334,
        0.11666666666666667,
        0.7166666666666667,
        0.25,
        0.26666666666666666,
        0.1,
        0.38333333333333336,
        0.21666666666666667
      ]
    },
    {
      "A_B_coefficient_sd": [
        0.02990092002647073,
        0.033550851909194726
      ],
      "A_B_sum_sd": 0.05554480363029218,
      "family": "ElasticNet",
      "mean_final_probe_prediction_sd": 0.1285669941913251,
      "selection_frequency": [
        1.0,
        1.0,
        1.0,
        0.4666666666666667,
        0.9,
        0.38333333333333336,
        0.95,
        0.5333333333333333,
        0.48333333333333334,
        0.3333333333333333,
        0.6166666666666667,
        0.5666666666666667
      ]
    }
  ],
  "p_greater_than_n_audit": {
    "Ridge_training_mse_at_penalty_point_1": 2.0585766918853866e-05,
    "columns": 40,
    "held_out_generalization_tested": false,
    "minimum_norm_training_mse": 2.6361487102124354e-30,
    "null_direction_preserves_interpolation": true,
    "rank": 24,
    "rows": 24
  },
  "roles": {
    "development": 120,
    "final": 400,
    "train": 90
  },
  "selected_fits": [
    {
      "development_mse": 0.3154080389968245,
      "family": "Ridge",
      "final_mse": 0.33937554751983723,
      "lambda": 0.08111308307896872,
      "original_scale_coefficients": [
        0.9424957633285144,
        0.9486923952373308,
        0.5580078743683821,
        -0.028314114128150276,
        0.09085799062300592,
        0.023095307477141207,
        -0.12037290556818622,
        -0.028369429157712032,
        0.03351660496331014,
        0.005736306565754103,
        0.056541173014116486,
        -0.013310300486880035
      ]
    },
    {
      "development_mse": 0.2972637313655271,
      "family": "Lasso",
      "final_mse": 0.32972359306416493,
      "lambda": 0.08111308307896872,
      "original_scale_coefficients": [
        0.0,
        1.8467277560685165,
        0.5418819261005448,
        -0.0,
        0.0364354281134725,
        0.0,
        -0.04759135820919385,
        -0.0,
        0.0,
        -0.0,
        0.0,
        -0.0
      ]
    },
    {
      "development_mse": 0.3074256608497054,
      "family": "ElasticNet",
      "final_mse": 0.33016067890906925,
      "lambda": 0.08111308307896872,
      "original_scale_coefficients": [
        0.9255708733901267,
        0.9430779593163394,
        0.5552470594762312,
        -0.0,
        0.06726222024833287,
        0.0,
        -0.08517409795845984,
        -0.0,
        0.0002691360404772354,
        0.0,
        0.014471524393284986,
        -0.0
      ]
    }
  ],
  "sensor_A_B_correlation": 0.9997212634062598
}
```

### code_075

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1575.

```json
{
  "calibration": {
    "calibration_rows": 300,
    "final_endpoint_probabilities": 22,
    "final_rows": 400,
    "isotonic_brier": 0.19349627549888304,
    "isotonic_log_loss_clipped_1e_6": 0.6522185413388685,
    "raw_brier": 0.19351061858965393,
    "raw_log_loss_clipped_1e_6": 0.5756794966156943
  },
  "fit": {
    "additive_final_brier": 0.19351061858965393,
    "additive_final_log_loss": 0.5756794966156943,
    "development_log_losses": [
      0.5542417938817957,
      0.5553526989254605,
      0.5997306994635
    ],
    "linear_final_brier": 0.19936902495199774,
    "linear_final_log_loss": 0.5860649542591362,
    "load_logit_increments": [
      0.0,
      0.21782717292982626,
      1.6714651381944252,
      0.9026336249002458
    ],
    "monotone_within_unit_load_support": true,
    "selected_penalty": 0.001
  },
  "locked_slice": {
    "additive_log_loss": 0.5530576999779282,
    "linear_log_loss": 0.5665296217088539,
    "rows": 200
  },
  "roles": {
    "calibration": 300,
    "development": 150,
    "final": 400,
    "locked_zero_temperature_slice": 200,
    "train": 350
  }
}
```

### code_076

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1576.

```json
{
  "rule_ensemble": {
    "features": [
      "load>30kN",
      "span>3.5m",
      "EI<4MN_m2",
      "span>4m AND EI<3MN_m2"
    ],
    "intercept": -2.03739955825395,
    "threshold": 0.5,
    "weights": [
      1.374671986719648,
      3.9493918394557146,
      2.077797805704131,
      0.2281030798180117
    ]
  },
  "rules": [
    {
      "agreement_with_selected_expression_flag": 0.56,
      "final_rows": 300,
      "final_target_accuracy": 0.5633333333333334,
      "method": "Decision list",
      "positive_targets": 217
    },
    {
      "agreement_with_selected_expression_flag": 0.7133333333333334,
      "final_rows": 300,
      "final_target_accuracy": 0.7166666666666667,
      "method": "Sparse score",
      "positive_targets": 217
    },
    {
      "agreement_with_selected_expression_flag": 0.88,
      "final_rows": 300,
      "final_target_accuracy": 0.8766666666666667,
      "method": "Four-leaf tree",
      "positive_targets": 217
    },
    {
      "agreement_with_selected_expression_flag": 0.86,
      "final_rows": 300,
      "final_target_accuracy": 0.8566666666666667,
      "method": "Rule ensemble",
      "positive_targets": 217
    }
  ],
  "symbolic": {
    "candidates": [
      {
        "coefficient_dimensionless": [
          0.02084386678432297
        ],
        "development_mse_m2": 8.079436689253795e-09,
        "expression": "beam",
        "selection_score_m2": 9.079436689253796e-09,
        "terms": 1
      },
      {
        "coefficient_dimensionless": [
          0.02082728603930857,
          1.4842228742175649e-05
        ],
        "development_mse_m2": 8.112191881457157e-09,
        "expression": "beam + load interaction",
        "selection_score_m2": 1.0112191881457157e-08,
        "terms": 2
      },
      {
        "coefficient_dimensionless": [
          0.020918523570393692,
          -5.1549922198477234e-05
        ],
        "development_mse_m2": 7.966430487198675e-09,
        "expression": "beam + span interaction",
        "selection_score_m2": 9.966430487198675e-09,
        "terms": 2
      }
    ],
    "dimension_guard_rejected_P_over_EI_with_unitless_coefficient": true,
    "roles": {
      "development": 120,
      "final": 300,
      "train": 250
    },
    "search_scope": "three fixed dictionaries only",
    "selected": "beam",
    "selected_final_mse_m2": 1.0685773849594419e-08,
    "true_beam_coefficient": 0.020833333333333332
  },
  "tree_leaves": 4
}
```


## Remote content verification

Content commit [8e7e6c085ba4e287dbc3921de1363c6e5ff225d3](https://github.com/ImeshEkanayake/MLBook-/commit/8e7e6c085ba4e287dbc3921de1363c6e5ff225d3) is published on main. All 129 remote blobs match the local commit and the earlier 71 manifest records are unchanged. The final metadata revision is independently verified in the local book delivery evidence, including commit-addressed raw-file bytes.
