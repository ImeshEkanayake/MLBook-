# Chapter 11 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verification passed.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_052 | 11.1 | 5 | 2 | 1.487 |
| code_053 | 11.2 | 4 | 2 | 1.678 |
| code_054 | 11.3 | 5 | 2 | 1.317 |
| code_055 | 11.4 | 4 | 2 | 1.574 |
| code_056 | 11.5 | 5 | 2 | 1.460 |

Total: **23 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed. The foundation-model schematic is a documentary contract review, not an executed foundation model.

## Actual mechanisms and boundaries

All five numerical laboratories execute successfully in fresh kernels. The generator creates every numerical input locally; the foundation-model branch is an explicitly labeled documentary review and contributes no downloaded inputs or runtime predictions. A static syntax check caught an unterminated multiline diagram-label string in the initial code_056 source before its first kernel execution; the builder was corrected to construct line breaks explicitly. There were no failed reference kernel runs. All controls, information roles and limitations are retained in the notebooks.

The fold experiment uses 160 independent members, two inputs, 20% first-input dropout and a deliberately broad final block. Identical four-block validation and five-neighbor controls give mean squared error 9.956478941 mm² for fold-only imputation/scaling versus 10.557481933 for invalid all-input statistics. The invalid procedure is worse; score direction does not legalize leakage. Fold statistics match explicit training-only calculations, the independent pipeline CV call agrees, and a three-request batching check preserves predictions and stored state. This is a diagnostic boundary example, not a final performance estimate.

The scaling experiment uses 550 members and 300/100/150 roles, with the same physical data represented in kN or N. All model/transform candidates are predeclared: five neighbors, Ridge alpha=10, histogram boosting 80 iterations/seven leaves/minimum leaf 15/learning rate .1/no early stopping. Standard and robust column scaling preserve predictions under the unit conversion. Raw neighbor final MSE changes .143780387 to .192088485; standardized MSE is .016884561. Tree raw/standard/robust MSE coincides at .013526792. Raw ridge .010324980 slightly beats standardized .010527788, despite centered Gram condition numbers 813017630.861 versus 1.239890. Row normalization changes magnitude/geometry and is poor here; no universal scaling recommendation follows. Robust scaling is not tested under a contamination claim.

The encoding audit preserves an explicit three-category vocabulary, all-zero one-hot unknown fallback and ordinal unknown -1. Seventy-five buildings with six members each split by 50/10/15 buildings. Scikit-learn 1.9.0 TargetEncoder accepts explicit GroupKFold iterable folds, continuous targets and fixed smoothing 5. Training cross-fitted versus invalid same-building MSE is .463718499/.064653842; final new-building MSE is .979827643/1.017786639. New IDs fall back to 2.241868165 mm. Perturbing an entire held-out fold's labels leaves its cross-fitted representation unchanged. Eight singleton IDs expose exact unsmoothed same-row target recovery versus lawful other-fold means. Learned embeddings are explained conceptually, not claimed as an implemented network.

The missingness experiment preserves 450/150/200 member roles. Correlated inputs and a nonlinear target use one training/development acquisition mechanism; identical final reference members receive matched and reversed-dependence masks. Missing fractions are .415556 training, .395 matched and .425 shifted. Matched/shifted final MSE is .756603999/.854855265 for median-indicator Ridge, .581625356/.569484072 for KNN-imputed Ridge, .713605227/.678037783 for a five posterior-draw iterative-imputation mean, .673091982/.682731542 for native histogram boosting and .723850069/.773057954 for median-indicator boosting. All fitting is training-only. The two tree routes share controls; linear/tree comparisons also change family. Posterior imputers use BayesianRidge with ten iterations and separate seeds; reported spread is imputation sensitivity, not Rubin-pooled inference or calibrated predictive uncertainty. The transform draw sequence is explicitly stochastic. A changed acquisition process does not worsen every method on this cohort.

Positive load targets use the declared lognormal mechanism, 350/100/200 roles and three fixed raw/log/smearing fits. Final raw/exp-log/smearing MSE is 42.789361012/43.502081607/41.308347106 kN²; MAE is 4.413402017/4.073622155/4.283623476 kN. Objectives differ. The training smearing factor is 1.184698059 versus the mechanism's mean/median ratio 1.197217363. Yeo–Johnson input parameters fit training only, inverse reconstruction passes, and six final inputs meet learned clipping limits [-.972892215,.965682990]. Wrong unit, infinity and nonpositive log-target fixtures are rejected. No predictive benefit is claimed for clipping/power shape alone.

The foundation input branch records a primary maintainer README at PriorLabs/TabPFN commit `417c9877dbfe657afdbe0aee70af2a05ffe4abba`, inspected 19 October 2026. It documents default TabPFN-3.5, missing-value support and advice against generic external scaling/one-hot conversion. This is a pinned document review, not a foundation-model execution, acceptance test or accuracy benchmark. No checkpoint is downloaded or dependency installed. Earlier-release search results were not treated as the current contract. A tagged v2 landing-page attempt and a documentation-installation URL were unavailable; the immutable primary README was retrieved and inspected instead.

The chapter implements both agreed visual briefs with a fold fit/transform diagram and a model-dependent input-contract diagram, plus four numerical figures. Five numbered equations derive composition, metric/penalty geometry, smoothed encoding and lognormal output meanings. The primary/official source references distinguish live maintenance documentation from the executed 1.9.0 environment. No dependency was added.

## Successful result dictionaries

### code_052

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1152.

```json
{
  "batch_invariance_passed": true,
  "fold_MSE_mm2": {
    "all_input_statistics_invalid": [
      4.102840025924159,
      2.49456945004331,
      1.9399562005111204,
      33.69256205669055
    ],
    "fold_only": [
      3.93542322856005,
      2.094756612210793,
      1.772744127803391,
      32.02299179587952
    ]
  },
  "fold_states": [
    {
      "median0": -0.2312240501687607,
      "scale0": 2.2621103141518284,
      "training_rows": 120
    },
    {
      "median0": -0.015475131234732821,
      "scale0": 2.23468517306762,
      "training_rows": 120
    },
    {
      "median0": -0.13126423242964408,
      "scale0": 2.271700167885223,
      "training_rows": 120
    },
    {
      "median0": -0.2537863517330509,
      "scale0": 0.7884588954338944,
      "training_rows": 120
    }
  ],
  "mean_fold_MSE_mm2": {
    "all_input_statistics_invalid": 10.557481933292284,
    "fold_only": 9.956478941113438
  },
  "prediction_batch_size": 3
}
```

### code_053

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1153.

```json
{
  "centered_Gram_condition_number": {
    "raw_N": 813017630.8611307,
    "standard": 1.2398900663379773
  },
  "distance_fixture": {
    "raw_mixed_unit": [
      1000.0,
      1.0
    ],
    "standardized": [
      0.03919105246510313,
      1.1148522790638
    ]
  },
  "metrics": {
    "N": {
      "boosted_tree": {
        "none": {
          "development_MSE_mm2": 0.015497612234927224,
          "final_MSE_mm2": 0.013526792209823259
        },
        "robust": {
          "development_MSE_mm2": 0.015497612234927224,
          "final_MSE_mm2": 0.013526792209823259
        },
        "row_L2": {
          "development_MSE_mm2": 0.08671490706683346,
          "final_MSE_mm2": 0.0904525138964082
        },
        "standard": {
          "development_MSE_mm2": 0.015497612234927224,
          "final_MSE_mm2": 0.013526792209823259
        }
      },
      "neighbors": {
        "none": {
          "development_MSE_mm2": 0.18987284976912222,
          "final_MSE_mm2": 0.1920884845687235
        },
        "robust": {
          "development_MSE_mm2": 0.014804841774000242,
          "final_MSE_mm2": 0.016285974072908604
        },
        "row_L2": {
          "development_MSE_mm2": 0.18015500921450958,
          "final_MSE_mm2": 0.2067160046148446
        },
        "standard": {
          "development_MSE_mm2": 0.014692573147129568,
          "final_MSE_mm2": 0.016884560740150118
        }
      },
      "ridge": {
        "none": {
          "development_MSE_mm2": 0.00986326951228214,
          "final_MSE_mm2": 0.010324984666758682
        },
        "robust": {
          "development_MSE_mm2": 0.01190881834050791,
          "final_MSE_mm2": 0.013676263766189963
        },
        "row_L2": {
          "development_MSE_mm2": 0.3990355057607718,
          "final_MSE_mm2": 0.41529855678296884
        },
        "standard": {
          "development_MSE_mm2": 0.009697769564988176,
          "final_MSE_mm2": 0.010527787628052877
        }
      }
    },
    "kN": {
      "boosted_tree": {
        "none": {
          "development_MSE_mm2": 0.015497612234927224,
          "final_MSE_mm2": 0.013526792209823259
        },
        "robust": {
          "development_MSE_mm2": 0.015497612234927224,
          "final_MSE_mm2": 0.013526792209823259
        },
        "row_L2": {
          "development_MSE_mm2": 0.08375748240424069,
          "final_MSE_mm2": 0.088646687842918
        },
        "standard": {
          "development_MSE_mm2": 0.015497612234927224,
          "final_MSE_mm2": 0.013526792209823259
        }
      },
      "neighbors": {
        "none": {
          "development_MSE_mm2": 0.16672275887515614,
          "final_MSE_mm2": 0.14378038696916792
        },
        "robust": {
          "development_MSE_mm2": 0.014804841774000242,
          "final_MSE_mm2": 0.016285974072908604
        },
        "row_L2": {
          "development_MSE_mm2": 0.10750369855783601,
          "final_MSE_mm2": 0.12516745220950354
        },
        "standard": {
          "development_MSE_mm2": 0.014692573147129568,
          "final_MSE_mm2": 0.016884560740150118
        }
      },
      "ridge": {
        "none": {
          "development_MSE_mm2": 0.009862973856903606,
          "final_MSE_mm2": 0.01032498028330125
        },
        "robust": {
          "development_MSE_mm2": 0.011908818340507901,
          "final_MSE_mm2": 0.013676263766189951
        },
        "row_L2": {
          "development_MSE_mm2": 0.3236594390115026,
          "final_MSE_mm2": 0.34162028777366804
        },
        "standard": {
          "development_MSE_mm2": 0.00969776956498819,
          "final_MSE_mm2": 0.010527787628052898
        }
      }
    }
  },
  "scaled_unit_conversion_prediction_invariance": true
}
```

### code_054

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1154.

```json
{
  "held_out_target_perturbation_invariance": true,
  "new_building_fallback_mean_mm": 2.2418681650192864,
  "one_hot_columns": [
    "x0_bolted",
    "x0_pinned",
    "x0_welded"
  ],
  "role_buildings": {
    "development": 10,
    "final": 15,
    "train": 50
  },
  "singleton_OOF_difference_squared": 9.13888888888889,
  "singleton_same_row_MSE": 0.0,
  "target_encoding_metrics": {
    "cross_fitted": {
      "development_new_building_MSE_mm2": 0.5724644143634893,
      "final_new_building_MSE_mm2": 0.979827642860092,
      "training_MSE_mm2": 0.46371849940780485
    },
    "same_building_in_sample_invalid": {
      "development_new_building_MSE_mm2": 0.5711726221978698,
      "final_new_building_MSE_mm2": 1.0177866386529584,
      "training_MSE_mm2": 0.06465384206162933
    }
  },
  "unseen_one_hot": [
    0.0,
    0.0,
    0.0
  ],
  "unseen_ordinal": -1
}
```

### code_055

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1155.

```json
{
  "MSE_mm2": {
    "development": {
      "knn_impute_ridge": 0.8205669319965201,
      "median_indicator_ridge": 0.9486479720538982,
      "median_indicator_tree": 0.8808484521873167,
      "native_tree": 0.8870329809621571,
      "posterior_draw_mean_ridge": 0.9465186678789678
    },
    "matched_final": {
      "knn_impute_ridge": 0.58162535640604,
      "median_indicator_ridge": 0.756603998600206,
      "median_indicator_tree": 0.7238500694987222,
      "native_tree": 0.6730919817178064,
      "posterior_draw_mean_ridge": 0.7136052272049699
    },
    "shifted_final": {
      "knn_impute_ridge": 0.5694840722634279,
      "median_indicator_ridge": 0.8548552654394075,
      "median_indicator_tree": 0.7730579541623608,
      "native_tree": 0.6827315415247942,
      "posterior_draw_mean_ridge": 0.6780377834903721
    }
  },
  "mean_imputation_prediction_sd_mm": {
    "development": 0.27239585064058197,
    "matched_final": 0.27270504126592,
    "shifted_final": 0.31154691615844693
  },
  "missing_fraction": {
    "matched_final": 0.395,
    "shifted_final": 0.425,
    "train": 0.41555555555555557
  },
  "posterior_imputation_draws": 5
}
```

### code_056

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1156.

```json
{
  "final_clipped_cases": 6,
  "final_metrics": {
    "exp_log_OLS": {
      "MAE_kN": 4.073622155440274,
      "MSE_kN2": 43.502081606698766,
      "mean_squared_log_error": 0.3376046566036368
    },
    "raw_OLS": {
      "MAE_kN": 4.413402016889815,
      "MSE_kN2": 42.78936101246356,
      "mean_squared_log_error": 0.3834079183542199
    },
    "training_smear": {
      "MAE_kN": 4.283623476092593,
      "MSE_kN2": 41.308347106320205,
      "mean_squared_log_error": 0.3612742259859485
    }
  },
  "foundation_contract_document": {
    "commit": "417c9877dbfe657afdbe0aee70af2a05ffe4abba",
    "documented_default": "TabPFN-3.5",
    "repository": "PriorLabs/TabPFN",
    "runtime_executed": false
  },
  "generator_mean_median_ratio": 1.1972173631218102,
  "power_inverse_round_trip_passed": true,
  "power_lambda": [
    0.824380798821501
  ],
  "schema_violations_rejected": 3,
  "training_clip_limits": [
    -0.9728922146751968,
    0.9656829895010182
  ],
  "training_smearing_factor": 1.1846980590828
}
```


The first chapter-checker pass exposed an inherited literal-assert count that ignored numerical NumPy assertion calls. The checker now recognizes both forms. Code_055 also gained explicit pairwise role-separation and training-median audits and was re-executed successfully; all result dictionaries remain unchanged and timings reflect current sources.

## Publication verification

Content commit `37247bab506c16ac66fb34da3ad480604b57b139` was pushed normally to main. All 97 remote file blobs match the local tree by Git blob hash; remote main matches, the working tree was clean, and all 51 previous manifest records remain unchanged. Final metadata verification also retrieves commit-addressed raw registry, manifest, guide, report and five notebooks.
