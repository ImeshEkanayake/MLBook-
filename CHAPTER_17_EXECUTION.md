# Chapter 17 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_082 | 17.1 | 4 | 2 | 1.523 |
| code_083 | 17.2 | 4 | 2 | 1.619 |
| code_084 | 17.3 | 4 | 2 | 1.514 |
| code_085 | 17.4 | 4 | 2 | 1.659 |
| code_086 | 17.5 | 4 | 2 | 1.761 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed after repairing panel-title collisions. The book delivery review also inspects all vector figures and composed pages.

## Actual mechanisms and boundaries

Five self-contained CPU laboratories use seeds1782–1786 and the existing Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/scikit-learn1.9.0 environment. Already-pinned threadpoolctl3.7.0 explicitly limits loaded BLAS pools to one thread for reproducible kernel/figure arithmetic. All five initial experiments passed. Notebook085 initially emitted a FutureWarning because version1.9 deprecates the explicit probability argument even when false; it reran with the documented margin-only default and asserts that the public probability-prediction interface is unavailable. An intermediate rerun also exposed deprecated probability-array inspection; the final source checks public interface availability instead. No warning is suppressed. All five reran with shorter panel titles after visual review found collisions in the notebook outputs. Exact numerical result dictionaries are preserved across layout reruns. No dependency was added; ordinary execution is offline. Counts and geometry are synthetic or declared, with no field-validity or population-prevalence assertion.

082 fixes a query40000N/4m/steel with complete A/B/C/D. Raw stored N/m Euclidean selectsA; force conversion to kN alone selectsB. Reference scales50000N/2m selectB under consistent unit conversion. An80-record separately generated admitted training covariance with10%diagonal shrinkage gives Mahalanobis distances[6.223457,.227165,.733822,1.723058] and unit-conversion invariance. This is numerical geometry, not a validated mechanical similarity law. Custom mixed mean absolute normalized numeric/material mismatch gives E zero distance on two shared fields but excludes it under the declared three-field rule. F shares no fields and returnsNone, not zero. Pair-dependent missingness rules need not satisfy metric assumptions. A200-record origin-query diagnostic adds50independent nuisance dimensions to2D: distance coefficient of variation falls .498302→.098003 and top-five overlap is0. No prediction-accuracy claim follows from those geometric checks.

083 generates train300/development120 inside[0,1]^2, response sin5load+.6span+NormalSD.15. Training-only StandardScaler and six k/weight candidates select k9/distance by development MSE .0336259. Final source-like200 has MSE .0313019 and mean ninth-distance .345589; unusual40 in[1.5,2]^2 has MSE3.951934 and distance4.361285. Distances are support diagnostics, not intervals. Exact brute/KDtree top-five IDs/distances agree. A predeclared100-of300candidate subset has exact-top5recall .2975; fixed selected predictor source MSE worsens .0504737 while unusual MSE happens to improve3.003388. Retain both outcomes: retrieval recall is not monotone predictive quality, and subset search does not repair extrapolation.300vs100 distance candidates are not wall-time speedups or HNSW/FAISS results. A separate duplicate-zero fixture predicts2from co-located responses1and3, excluding response10atdistance1; it audits weighting, not duplicate evidence validity.

084 generates train120/development80/final200within seasonal months0–12 and future60within12–24. Response=.8load+sin(2pi*time/12)+NormalSD.15; known period12 and kernel shape controls are fixed. Training-only load scaling/time centering and fixed training-response offset .0145226 precede common KRR solves(K+n*lambda I). Linear/RBFgamma1/additive-load-plus-periodiclength.7 choose lambda .01/.001/.001 by development. Source-final MSE .215424/.168332/.0222264; future3.227959/1.324875/.0240803. An independent locked80-record load-zero slice gives1.855413/.597297/.0249532. Curves/observations share that slice. Periodic success reflects the constructed generator, not discovered future physics. Six-dimensional polynomial map exactly matches(1+u.v)^2; symmetric[[1,2],[2,1]]has eigenvalues[-1,3] and is rejected. No finite exact RBF-map or probability-output claim.

085 rare circular positives with .01flips have43/500training,25/200development,27/200calibration,45/400final positives. Stored[1000*x1,x2] uses training-only scaling. Balanced-penalty linear SVC grid3 and RBF grid9 select C.1linear and C1/gamma1RBF by development balanced accuracy. Final margin-zero balanced accuracy .664006/.939906, separately sigmoid-calibrated probability-half .5/.9. Calibration logistic C1 fits calibration margins at natural generated prevalence only; no final threshold/model tuning. Final Brier .100561/.0229856 and logloss .354071/.107403. Support counts496/127 and training hinge violations496/121 are observed, not set byC. Five final calibration groups each contain80records. Schematic radius-squared map is explicitly not the exact RBF feature map. Separate fixed SVR train100/final120,C5/epsilon.1/gamma4 has57support vectors,.49training fraction inside the tube with .002numerical tolerance and finalMSE .0190589. The epsilon band is a loss tolerance, not a probability interval.

086 generates train240/development120/final300,12independent normal descriptors, XOR signal in first2 plus.05label flips. Baseline scaled kNN and linear2D NCA kNN each select six k/weight candidates by development Brier. Both select15neighbors, baseline distance/NCAuniform. NCA PCA initialization/max_iter50/tol1e-5 and norm rescaling are fixed; public n_iter_ full/folds[28,33,36,46,46,51] is retained honestly, including the51counter, without a convergence certificate. The separately specified retrieval-context stack uses top15 soft NCA neighbors and26features(rawquery12,labelmean1,original-feature differences12,weighted sqdistance1). Entire scaler/NCA fit is contained within each of five OOFmemory folds; query labels never enter their own first-level encoder or neighbor values. Rotation-sensitive embedding-coordinate differences are avoided. Fixed C1 logistic meta-head plus training-only meta scaling fits OOFfeatures; development selects temperature1of[.05,.2,1]. Deployment encoder/memory uses alltraining only. This is not a neural TabR/ModernNCA execution or paper reproduction. Final baseline/NCA/stack Brier .235156/.214548/.226626, clipped1e-6logloss .662730/.772107/.652284, probability-half accuracy .61/.68/.67. NCA improvesBrier but worsenslogloss. Invalid1NNselftrainingaccuracy1is flagged and excluded. Fixed60-of240subset top15recall .249778; distance candidates240vs60 are not timings. Array ledger rawtraining23040B/keys3840B/labels1920B/NCAmap192B excludes process/Python/temporary overhead.

The isolated RBFgamma.2 approximation audit uses64Fourier features or64Nystroem landmarks on training-standardized inputs. Development Gram relative Frobenius error is1.184026/.807916; each training feature matrix122880B plus transform arrays6656/38912B versus dense training Gram460800B. Shared inputs/workspaces/Python/process overhead are excluded consistently. Manual cosine map matches RBFSampler; approximate Grams are PSD within arithmetic tolerance. No response-model comparison or claim that lower Gram error implies better prediction is attached.

Ten original vector figure sets implement both planned visual briefs, with four numbered equations and ten exercises. Official neighbor/SVC/NCA/kernel-approximation references and TabR primary preprintv2Section3.2 were inspected20October2026. TabR's retrieved features/labels and learned architecture are documentary context; its original neural implementation/benchmark and neural ModernNCA are not executed. Live sklearn1.9.1 versus executed1.9.0 is disclosed. Every cost, score, transformation and memory boundary remains explicitly scoped.

## Successful result dictionaries

### code_082

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1782.

```json
{
  "geometry": {
    "dimensionless_distances": [
      1.0000079999680003,
      0.053851648071344876,
      0.15524174696260015,
      0.2
    ],
    "dimensionless_nearest": "B",
    "dimensionless_unit_invariance_passed": true,
    "names": [
      "A",
      "B",
      "C",
      "D"
    ],
    "raw_N_m_numeric_distances": [
      200.0099997500125,
      1000.000005,
      2000.0000225,
      10000.0
    ],
    "raw_kN_m_numeric_distances": [
      2.009975124224178,
      1.004987562112089,
      2.0223748416156684,
      10.0
    ],
    "raw_nearest": "A",
    "reference_load_N": 50000,
    "reference_span_m": 2
  },
  "irrelevant_dimensions": {
    "distance_CV_2d": 0.4983022081056885,
    "distance_CV_52d": 0.09800329216737635,
    "extra_independent_noise_dimensions": 50,
    "query": "origin in both spaces; diagnostic geometry only",
    "records": 200,
    "signal_dimensions": 2,
    "top5_neighbor_overlap": 0.0
  },
  "mixed_missing": [
    {
      "distance": 0.33466666666666667,
      "eligible_all_three_fields": true,
      "record": "A",
      "shared_fields": 3
    },
    {
      "distance": 0.023333333333333275,
      "eligible_all_three_fields": true,
      "record": "B",
      "shared_fields": 3
    },
    {
      "distance": 0.39666666666666667,
      "eligible_all_three_fields": true,
      "record": "C",
      "shared_fields": 3
    },
    {
      "distance": 0.06666666666666667,
      "eligible_all_three_fields": true,
      "record": "D",
      "shared_fields": 3
    },
    {
      "distance": 0.0,
      "eligible_all_three_fields": false,
      "record": "E",
      "shared_fields": 2
    },
    {
      "distance": null,
      "eligible_all_three_fields": false,
      "record": "F",
      "shared_fields": 0
    }
  ],
  "training_covariance_metric": {
    "Mahalanobis_distances": [
      6.2234569321457665,
      0.22716450606930885,
      0.7338224070191073,
      1.7230580780346991
    ],
    "diagonal_shrinkage": 0.1,
    "fit_rows": 80,
    "unit_conversion_invariance_passed": true
  }
}
```

### code_083

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1783.

```json
{
  "final_cohorts": [
    {
      "cohort": "Inside",
      "max_kth_neighbor_distance": 0.5700481121141091,
      "mean_kth_neighbor_distance": 0.34558874824950175,
      "mse": 0.03130193480173695,
      "rows": 200
    },
    {
      "cohort": "Unusual",
      "max_kth_neighbor_distance": 5.186583897747085,
      "mean_kth_neighbor_distance": 4.361285473261903,
      "mse": 3.951933500480041,
      "rows": 40
    }
  ],
  "roles": {
    "development": 120,
    "inside_final": 200,
    "training": 300,
    "unusual_final": 40
  },
  "search": {
    "algorithm_claim": "uniform candidate-subset demonstration only",
    "distance_candidates_per_query_exact": 300,
    "distance_candidates_per_query_subset": 100,
    "duplicate_zero_distance_prediction": 2.0,
    "exact_brute_KDtree_agreement": true,
    "full_records": 300,
    "mean_top5_recall": 0.29750000000000004,
    "subset_prediction": [
      {
        "cohort": "Inside",
        "mse": 0.050473720020967595
      },
      {
        "cohort": "Unusual",
        "mse": 3.0033883410233964
      }
    ],
    "subset_records": 100
  },
  "selection": {
    "candidate_scores": [
      {
        "development_mse": 0.03815668485378478,
        "k": 3,
        "weights": "uniform"
      },
      {
        "development_mse": 0.03701058694762859,
        "k": 3,
        "weights": "distance"
      },
      {
        "development_mse": 0.03604805780463189,
        "k": 9,
        "weights": "uniform"
      },
      {
        "development_mse": 0.03362587953538017,
        "k": 9,
        "weights": "distance"
      },
      {
        "development_mse": 0.0575951839149385,
        "k": 25,
        "weights": "uniform"
      },
      {
        "development_mse": 0.04295969263353329,
        "k": 25,
        "weights": "distance"
      }
    ],
    "development_mse": 0.03362587953538017,
    "k": 9,
    "weights": "distance"
  }
}
```

### code_084

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1784.

```json
{
  "feature_geometry": {
    "RBF_finite_map_claimed": false,
    "indefinite_similarity_eigenvalues": [
      -1.0,
      3.0
    ],
    "polynomial_feature_dimensions": 6,
    "polynomial_identity_passed": true
  },
  "kernel_fits": [
    {
      "development_mse": 0.2544115490319677,
      "future_mse": 3.2279586872258172,
      "kernel": "Linear",
      "lambda": 0.01,
      "source_final_mse": 0.21542351656424344
    },
    {
      "development_mse": 0.19945319632763142,
      "future_mse": 1.324874896471943,
      "kernel": "RBF",
      "lambda": 0.001,
      "source_final_mse": 0.16833236201694746
    },
    {
      "development_mse": 0.022391579068339818,
      "future_mse": 0.02408029200875308,
      "kernel": "Periodic additive",
      "lambda": 0.001,
      "source_final_mse": 0.02222641182906238
    }
  ],
  "locked_slice": {
    "kernel_mse": {
      "Linear": 1.8554130287082835,
      "Periodic additive": 0.024953225575150596,
      "RBF": 0.5972974717543093
    },
    "rows": 80
  },
  "roles": {
    "development": 80,
    "fixed_training_mean_offset": 0.014522616328171015,
    "future_final": 60,
    "known_period_months": 12,
    "source_final": 200,
    "source_train": 120
  }
}
```

### code_085

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1785.

```json
{
  "SVR": {
    "C": 5,
    "epsilon": 0.1,
    "final": 120,
    "final_mse": 0.019058873595206187,
    "gamma": 4,
    "interval_claimed": false,
    "support_vectors": 57,
    "training": 100,
    "training_fraction_in_epsilon_tube": 0.49
  },
  "families": [
    {
      "C": 0.1,
      "calibration_intercept": -1.8962714162964025,
      "calibration_slope": 0.20761923584548644,
      "development_balanced_accuracy": 0.62,
      "development_candidates": 3,
      "family": "Linear",
      "final_brier": 0.10056130917333411,
      "final_log_loss": 0.3540707130552716,
      "final_margin_zero_balanced_accuracy": 0.6640062597809077,
      "final_probability_half_balanced_accuracy": 0.5,
      "gamma": "scale",
      "support_vectors": 496,
      "training_hinge_violations": 496
    },
    {
      "C": 1,
      "calibration_intercept": -1.7732639752276231,
      "calibration_slope": 1.8621673763039739,
      "development_balanced_accuracy": 0.9771428571428571,
      "development_candidates": 9,
      "family": "RBF",
      "final_brier": 0.02298563243269006,
      "final_log_loss": 0.10740281539181344,
      "final_margin_zero_balanced_accuracy": 0.9399061032863849,
      "final_probability_half_balanced_accuracy": 0.9,
      "gamma": 1,
      "support_vectors": 127,
      "training_hinge_violations": 121
    }
  ],
  "final_calibration_groups": {
    "Linear": [
      {
        "mean_probability": 0.11540484608566245,
        "n": 80,
        "positive_fraction": 0.0
      },
      {
        "mean_probability": 0.12609728089826241,
        "n": 80,
        "positive_fraction": 0.05
      },
      {
        "mean_probability": 0.1352853725232353,
        "n": 80,
        "positive_fraction": 0.3375
      },
      {
        "mean_probability": 0.14518017467518213,
        "n": 80,
        "positive_fraction": 0.175
      },
      {
        "mean_probability": 0.1593517309352896,
        "n": 80,
        "positive_fraction": 0.0
      }
    ],
    "RBF": [
      {
        "mean_probability": 0.002930712082958758,
        "n": 80,
        "positive_fraction": 0.0125
      },
      {
        "mean_probability": 0.00972546952243169,
        "n": 80,
        "positive_fraction": 0.0125
      },
      {
        "mean_probability": 0.017886000146785718,
        "n": 80,
        "positive_fraction": 0.0125
      },
      {
        "mean_probability": 0.03529940507264413,
        "n": 80,
        "positive_fraction": 0.0
      },
      {
        "mean_probability": 0.4951043734983308,
        "n": 80,
        "positive_fraction": 0.525
      }
    ]
  },
  "roles": {
    "calibration": {
      "positives": 27,
      "rows": 200
    },
    "development": {
      "positives": 25,
      "rows": 200
    },
    "final": {
      "positives": 45,
      "rows": 400
    },
    "training": {
      "positives": 43,
      "rows": 500
    }
  }
}
```

### code_086

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1786.

```json
{
  "NCA": {
    "convergence_asserted": false,
    "fit_n_iter_full_then_folds": [
      28,
      33,
      36,
      46,
      46,
      51
    ],
    "map_dimensions": 2,
    "max_iter": 50,
    "neural_ModernNCA_executed": false,
    "tol": 1e-05
  },
  "candidates": [
    {
      "candidate": "Scaled kNN",
      "development_brier": 0.21819303109176136,
      "development_candidates": 6,
      "final_accuracy_probability_half": 0.61,
      "final_brier": 0.23515568290757416,
      "final_log_loss_clipped_1e6": 0.6627299830520978,
      "k": 15,
      "weights": "distance"
    },
    {
      "candidate": "NCA kNN",
      "development_brier": 0.1628888888888889,
      "development_candidates": 6,
      "final_accuracy_probability_half": 0.68,
      "final_brier": 0.21454814814814815,
      "final_log_loss_clipped_1e6": 0.7721073270072535,
      "k": 15,
      "weights": "uniform"
    },
    {
      "OOF_folds": 5,
      "candidate": "Retrieval context stack",
      "development_brier": 0.2087804591897378,
      "development_candidates": 3,
      "final_accuracy_probability_half": 0.67,
      "final_brier": 0.22662554757589765,
      "final_log_loss_clipped_1e6": 0.6522836027450428,
      "meta_features": 26,
      "neighbor_context_size": 15,
      "reference_TabR_executed": false,
      "temperature": 1
    }
  ],
  "invalid_self_lookup": {
    "training_accuracy": 1.0,
    "used_for_selection": false,
    "valid_assessment": false
  },
  "kernel_approximations": [
    {
      "dense_training_Gram_bytes_reference": 460800,
      "development_Gram_relative_Frobenius_error": 1.1840258030501398,
      "features": 64,
      "method": "Random Fourier",
      "training_feature_bytes": 122880,
      "transform_parameter_bytes": 6656
    },
    {
      "dense_training_Gram_bytes_reference": 460800,
      "development_Gram_relative_Frobenius_error": 0.807916330981272,
      "features": 64,
      "method": "Nystroem",
      "training_feature_bytes": 122880,
      "transform_parameter_bytes": 38912
    }
  ],
  "retrieval_array_bytes": {
    "excludes": "Python objects, library overhead, temporary arrays, complete process RSS",
    "int_labels": 1920,
    "linear_NCA_map": 192,
    "raw_training_float64": 23040,
    "two_dimensional_keys": 3840
  },
  "roles": {
    "development": 120,
    "final": 300,
    "first_level_OOF_query_overlap_with_memory": 0,
    "nuisance_dimensions": 10,
    "query_label_in_own_first_level_fit": false,
    "training": 240
  },
  "search_budget": {
    "exact_distance_candidates_per_query": 240,
    "full_records": 240,
    "named_ANN_index_claimed": false,
    "subset_distance_candidates_per_query": 60,
    "subset_records": 60,
    "top15_recall": 0.24977777777777774
  }
}
```


## Publication verification

Content commit `c33055250915d68213b5e721003a8368fad0e2bf` matches remote main and all145file blobs; the companion working tree was clean at content verification. The final metadata commit is verified separately through commit-addressed raw files in the local delivery evidence. Only companion artifacts are published.
