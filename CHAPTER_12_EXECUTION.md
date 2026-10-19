# Chapter 12 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verification passed.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_057 | 12.1 | 4 | 2 | 1.662 |
| code_058 | 12.2 | 4 | 2 | 1.440 |
| code_059 | 12.3 | 5 | 2 | 1.701 |
| code_060 | 12.4 | 5 | 2 | 1.668 |
| code_061 | 12.5 | 4 | 2 | 1.438 |

Total: **22 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed. Crowded ticks and a clipped axis label were repaired and re-executed with unchanged results.

## Actual mechanisms and boundaries

All five self-contained generated-data laboratories execute in fresh kernels with no failed reference runs. Construction audits and fitted prediction roles are explicitly distinguished. All numerical inputs are generated internally, without downloads, credentials or GPU; no dependency was added. The custom autoencoder's gradient is checked numerically and its fixed optimization budget is disclosed rather than claimed converged or globally optimal.

The physical-feature comparison uses 600 independent idealized central-load beam records with positive load/span/rigidity, an explicitly favorable affine beam mechanism, 300/100/200 roles and nested training sizes 40/80/160/300. Units and a dimensionless identity pass numerical checks. Raw main effects, quadratic expansion and the beam feature have 300-member final MSE 44.890505566/7.484463859/.009738991 mm². The physical slope is 1.079878951 against declared 1.08, and its 40-member MSE is .010481687. Different hypothesis classes and correct domain information are intentional. The outcomes do not validate field mechanics, uncertain stiffness or other supports/loading/material regimes; no final curve selects a representation.

The history construction fixes six members, ten daily 64-sample windows at 64 Hz, cutoff 7.5 and trailing interval (4.5,7.5]. Both end and arrival clocks apply. Member-0 day-6 payload arrives day 9 and is excluded, leaving two windows rather than three. Only day-1 inspections arrive before cutoff; each member has one known prior inspection and recency 6.5 days. One-sided Fourier weighting passes Parseval against time-domain mean square. RMS has acceleration units, while band contributions/mean square are squared acceleration, not physical mechanical energy. Ring-neighbor means use only individually eligible histories; appending huge future windows leaves all historical features exactly unchanged. These are construction audits, not predictive scores or causal graph claims.

The selection comparison generates 440 independent members with two proxies of u (training correlation .995017927), one v channel and five noise channels; 240/80/120 roles. Scaling/selection are refitted inside each of four training CV folds. Fixed two-column filter and RFE both retain the redundant u pair and omit v, with final MSE 1.048943984 mm². Lasso alpha .08 retains all three useful channels and gives .282530643. Forty training half-samples produce filter/RFE/Lasso mean Jaccard 1/.966666667/.819102564. The filter is perfectly stable yet predictively inadequate; the important u proxies do not exchange places in this run. Lasso's variation includes occasional noise columns. A predeclared .7-frequency threshold retains u_A/u_B/v_C; refitted ridge gives .250449342 final MSE. Frequencies are descriptive diagnostics, not posterior inclusion, causal relevance or the original stability-selection paper's false-discovery guarantees. An attempted author-hosted PDF was unavailable, so the primary arXiv record and publisher article were inspected for the framework; no unverified theorem conditions are asserted.

The representation experiment uses 550 independent 64-sample acceleration windows, random phases/amplitudes and 300/100/150 roles. Its target deliberately depends on squared amplitudes, privileging known two-bin spectral features with phase invariance. Raw-64/PCA-8/autoencoder-8/spectral-2 plus the same fixed linear ridge readout have final response-index MSE 2.086286224/1.895526944/1.965539342/.009810793. PCA/autoencoder final standardized reconstruction MSE is .002370630/.040967383. The eight-unit tanh/linear-output autoencoder uses full-batch gradients, rate .1, 2,000 fixed updates and weight penalty 1e-4; objective falls 1.069936954 to .037966299 and the central-difference encoder-gradient check passes. Reconstruction and downstream objectives differ. No best-encoder ranking, convergence certificate, end-to-end supervised training, foundation embedding or transfer to other acquisition conditions is claimed.

The feature-package experiment uses 700 independent members and 400/150/150 roles with a declared static latent condition. Acquisition costs/delays are teaching fixtures: base 0/0, vibration 5/.1 day, preplanned prior inspection 20/0 at decision time, combination 25/.1, new precise inspection 50/2, outcome proxy 0/7.1. Only the four available packages meet budget 25 and deadline .5. Lowest development error chooses the combination; final MSE is .495234390 mm² versus vibration .574102248, prior .861263602 and base 1.759124835. The new inspection/proxy apparent errors .088835502/.000103986 are invalid for the original decision. Their scores are retained as leakage findings, not deployable performance. The prior inspection requires advance scheduling; a later decision needs a different task and is not evaluated here. Reordered selected-request columns are explicitly rejected. Prediction MSE is not operational utility or a field cost-effectiveness estimate.

Seven original vector figure sets implement both planned visual briefs: cutoff-safe trailing and relational summaries, plus nested selection and resample frequencies. Four equations specify the physical combination, RMS, selection frequency and autoencoder. Primary/official references support the mechanics convention, spectral units, selector/PCA interfaces and formal-versus-diagnostic stability distinction. The underlying generated experiments and fixed-budget autoencoder are specified independently. All controls and limitations remain in the companion guide and execution evidence.

## Successful result dictionaries

### code_057

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1257.

```json
{
  "beam_feature_coefficient": 1.079878951075595,
  "learning_size_metrics": {
    "160": {
      "beam_feature": {
        "development_MSE_mm2": 0.012188318476849895,
        "final_MSE_mm2": 0.009739232833591011
      },
      "quadratic_basis": {
        "development_MSE_mm2": 5.099037732348179,
        "final_MSE_mm2": 7.893233289459147
      },
      "raw_main_effects": {
        "development_MSE_mm2": 28.55024268067333,
        "final_MSE_mm2": 46.29425219206833
      }
    },
    "300": {
      "beam_feature": {
        "development_MSE_mm2": 0.012181339506890447,
        "final_MSE_mm2": 0.00973899085170241
      },
      "quadratic_basis": {
        "development_MSE_mm2": 5.432559200310428,
        "final_MSE_mm2": 7.484463858930859
      },
      "raw_main_effects": {
        "development_MSE_mm2": 34.00655664391106,
        "final_MSE_mm2": 44.89050556643877
      }
    },
    "40": {
      "beam_feature": {
        "development_MSE_mm2": 0.013399277392638416,
        "final_MSE_mm2": 0.010481687420587886
      },
      "quadratic_basis": {
        "development_MSE_mm2": 12.292117717336057,
        "final_MSE_mm2": 15.520268378749227
      },
      "raw_main_effects": {
        "development_MSE_mm2": 30.660796351296035,
        "final_MSE_mm2": 43.861126471931954
      }
    },
    "80": {
      "beam_feature": {
        "development_MSE_mm2": 0.012488257073756592,
        "final_MSE_mm2": 0.009824129402632957
      },
      "quadratic_basis": {
        "development_MSE_mm2": 5.000147860117802,
        "final_MSE_mm2": 7.509547188863329
      },
      "raw_main_effects": {
        "development_MSE_mm2": 27.919304204730107,
        "final_MSE_mm2": 45.65391151976551
      }
    }
  },
  "unit_and_dimensionless_checks": true
}
```

### code_058

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1258.

```json
{
  "delayed_window_excluded": {
    "arrival": 9.0,
    "event_end": 6.2,
    "member": 0
  },
  "features_at_cutoff": {
    "0": {
      "RMS_mm_s2": 0.8634297245149338,
      "available_windows": 2,
      "days_since_latest_known_event": 6.5,
      "four_Hz_band_mean_square": 0.6990215038452515,
      "last_window_end": 7.2,
      "mean_square_mm2_s4": 0.7455108891759343,
      "neighbor_mean_available_RMS": 1.0667764815312548,
      "prior_inspections": 1
    },
    "1": {
      "RMS_mm_s2": 0.9295959659866798,
      "available_windows": 3,
      "days_since_latest_known_event": 6.5,
      "four_Hz_band_mean_square": 0.8185569166373061,
      "last_window_end": 7.2,
      "mean_square_mm2_s4": 0.8641486599787083,
      "neighbor_mean_available_RMS": 0.9305266831425463,
      "prior_inspections": 1
    },
    "2": {
      "RMS_mm_s2": 0.9976236417701586,
      "available_windows": 3,
      "days_since_latest_known_event": 6.5,
      "four_Hz_band_mean_square": 0.9497983008666546,
      "last_window_end": 7.2,
      "mean_square_mm2_s4": 0.9952529306187538,
      "neighbor_mean_available_RMS": 0.9983138943846341,
      "prior_inspections": 1
    },
    "3": {
      "RMS_mm_s2": 1.0670318227825883,
      "available_windows": 3,
      "days_since_latest_known_event": 6.5,
      "four_Hz_band_mean_square": 1.0931122982966046,
      "last_window_end": 7.2,
      "mean_square_mm2_s4": 1.138556910830733,
      "neighbor_mean_available_RMS": 1.070307232809502,
      "prior_inspections": 1
    },
    "4": {
      "RMS_mm_s2": 1.1429908238488453,
      "available_windows": 3,
      "days_since_latest_known_event": 6.5,
      "four_Hz_band_mean_square": 1.2587113929204037,
      "last_window_end": 7.2,
      "mean_square_mm2_s4": 1.3064280234026622,
      "neighbor_mean_available_RMS": 1.1354944099292092,
      "prior_inspections": 1
    },
    "5": {
      "RMS_mm_s2": 1.20395699707583,
      "available_windows": 3,
      "days_since_latest_known_event": 6.5,
      "four_Hz_band_mean_square": 1.4036422700084323,
      "last_window_end": 7.2,
      "mean_square_mm2_s4": 1.44951245080785,
      "neighbor_mean_available_RMS": 1.0032102741818896,
      "prior_inspections": 1
    }
  },
  "future_append_invariance": true
}
```

### code_059

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1259.

```json
{
  "fixed_procedure_metrics": {
    "Lasso": {
      "CV_MSE_mm2": [
        0.23069698297604932,
        0.3483778314692379,
        0.2652792413069464,
        0.30068098120397274
      ],
      "development_MSE_mm2": 0.3215390199032856,
      "final_MSE_mm2": 0.28253064345115475,
      "selected_channels": [
        "u_A",
        "u_B",
        "v_C"
      ]
    },
    "RFE_two": {
      "CV_MSE_mm2": [
        0.7028394144090669,
        0.9105859681898373,
        0.8940934629652694,
        0.809372459922805
      ],
      "development_MSE_mm2": 0.8034288006410609,
      "final_MSE_mm2": 1.0489439839979011,
      "selected_channels": [
        "u_A",
        "u_B"
      ]
    },
    "filter_two": {
      "CV_MSE_mm2": [
        0.7028394144090669,
        0.9105859681898373,
        0.8940934629652694,
        0.809372459922805
      ],
      "development_MSE_mm2": 0.8034288006410609,
      "final_MSE_mm2": 1.0489439839979011,
      "selected_channels": [
        "u_A",
        "u_B"
      ]
    }
  },
  "mean_pairwise_Jaccard": {
    "Lasso": 0.8191025641025641,
    "RFE_two": 0.9666666666666667,
    "filter_two": 1.0
  },
  "resampling_repeats": 40,
  "selection_frequencies": {
    "Lasso": [
      1.0,
      1.0,
      1.0,
      0.05,
      0.275,
      0.05,
      0.0,
      0.1
    ],
    "RFE_two": [
      0.975,
      1.0,
      0.025,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "filter_two": [
      1.0,
      1.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ]
  },
  "stable_Lasso_channels": [
    "u_A",
    "u_B",
    "v_C"
  ],
  "stable_set_final_MSE_mm2": 0.2504493424505097,
  "training_proxy_correlation": 0.995017927389866
}
```

### code_060

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1260.

```json
{
  "autoencoder_training_objective": {
    "final": 0.03796629886770185,
    "gradient_check_passed": true,
    "hidden_units": 8,
    "initial": 1.0699369541210484,
    "updates": 2000
  },
  "downstream_metrics": {
    "PCA_8": {
      "columns": 8,
      "development_MSE": 1.8328225142968833,
      "final_MSE": 1.8955269441641607
    },
    "autoencoder_8": {
      "columns": 8,
      "development_MSE": 1.8326634893644824,
      "final_MSE": 1.9655393418341154
    },
    "raw_64": {
      "columns": 64,
      "development_MSE": 1.8897926466318047,
      "final_MSE": 2.086286224061799
    },
    "spectral_2": {
      "columns": 2,
      "development_MSE": 0.009940248027750303,
      "final_MSE": 0.009810792690620657
    }
  },
  "final_standardized_reconstruction_MSE": {
    "PCA_8": 0.0023706296720713794,
    "autoencoder_8": 0.040967383476330485
  }
}
```

### code_061

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1261.

```json
{
  "budget": 25,
  "deadline_days": 0.5,
  "packages": {
    "base": {
      "columns": [
        "base"
      ],
      "cost": 0.0,
      "development_MSE_mm2": 1.715930323972142,
      "eligible": true,
      "final_or_invalid_apparent_MSE_mm2": 1.7591248352920565,
      "latency_days": 0.0
    },
    "both": {
      "columns": [
        "base",
        "vibration",
        "prior"
      ],
      "cost": 25.0,
      "development_MSE_mm2": 0.4139675596517586,
      "eligible": true,
      "final_or_invalid_apparent_MSE_mm2": 0.4952343898236713,
      "latency_days": 0.1
    },
    "late_new_INVALID": {
      "columns": [
        "base",
        "late_new"
      ],
      "cost": 50.0,
      "development_MSE_mm2": 0.05615321367081568,
      "eligible": false,
      "final_or_invalid_apparent_MSE_mm2": 0.08883550193584965,
      "latency_days": 2.0
    },
    "outcome_proxy_INVALID": {
      "columns": [
        "base",
        "outcome_proxy"
      ],
      "cost": 0.0,
      "development_MSE_mm2": 0.00011399254678148804,
      "eligible": false,
      "final_or_invalid_apparent_MSE_mm2": 0.00010398607132836271,
      "latency_days": 7.1
    },
    "prior": {
      "columns": [
        "base",
        "prior"
      ],
      "cost": 20.0,
      "development_MSE_mm2": 0.7277643880409228,
      "eligible": true,
      "final_or_invalid_apparent_MSE_mm2": 0.8612636024253838,
      "latency_days": 0.0
    },
    "vibration": {
      "columns": [
        "base",
        "vibration"
      ],
      "cost": 5.0,
      "development_MSE_mm2": 0.5827744655304166,
      "eligible": true,
      "final_or_invalid_apparent_MSE_mm2": 0.5741022483481185,
      "latency_days": 0.1
    }
  },
  "reordered_schema_rejected": true,
  "selected_final_MSE_mm2": 0.4952343898236713,
  "selected_on_development": "both"
}
```


Visual review prompted fresh-kernel reruns of code_060 and code_061 after separating neighboring tick labels and shortening a clipped axis label. Both pass with unchanged result dictionaries; current timings are recorded. The first PDF integrity pass also caught an overlong mechanics URL; its local reference typography was repaired. Closing practice was kept together after page review.

## Publication verification

Content commit `b7a2a0f7e21c8138560ea4b1c7155b1b75b316e3` was pushed normally to main. All 105 remote file blobs match the local Git tree; remote main matches and the working tree was clean. All 56 prior manifest records remain unchanged. Final metadata verification additionally retrieves commit-addressed raw registry, manifest, guide, report and five notebooks.
