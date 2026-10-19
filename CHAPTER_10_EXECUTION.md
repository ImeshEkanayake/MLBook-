# Chapter 10 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_047 | 10.1 | 6 | 2 | 1.347 |
| code_048 | 10.2 | 5 | 2 | 1.257 |
| code_049 | 10.3 | 5 | 2 | 1.285 |
| code_050 | 10.4 | 6 | 2 | 1.326 |
| code_051 | 10.5 | 5 | 2 | 1.442 |

Total: **27 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

All five laboratories pass fresh-kernel execution. The missingness experiment retains absent, structural, failed and censored states separately. Its three stipulated MCAR/MAR/MNAR generators use 600 independent members and train/development/final roles 300/150/150. Training medians exclude assessment inputs. Development selects the indicator in all three mechanisms, but it slightly loses on final MAR and MNAR cases (.048239224 versus .047677427 and .051192369 versus .050690067 mm²). The MCAR final errors are .037406610/.037558362. These outcomes do not identify missingness or establish valid inference under MNAR.

The identity audit preserves seven import rows, five event versions, four events and three composite-key members. It retains three e1 import IDs in lineage, keeps legitimate same-grade inspections and rejects a fabricated conflicting payload. Event e4 has grade one at cutoff 10 and grade three at cutoff 15. An invalid row split overlaps e1/e4; event separation repairs only that boundary, not building/time independence.

Quantity-aware conversion retains signed displacements [1.2,1.4,1.5,-.8] mm and flags a separate invalid negative length. Offset-aware repeated local clocks differ by 3,600 seconds in UTC and have verified timezone folds 0/1. An arrival-before-event record is flagged rather than guessed. Ten reference standards fit offset .199682692 mm and gain 1.050049495; five independent checks give raw/calibrated MAE .277852384/.003511267 mm. This is a simulated calibration check, not accreditation or operational target fitting.

The uncertain-label experiment uses a declared uniform severity prior and independent Gaussian annotation errors; the annotation-only posterior does not condition on all predictive information. Training annotators disagree on 54/400 cases; agreement-only training retains 346. Twenty new training-only adjudications change eleven labels and incur extra evidence. All four logistic policies are frozen, with disclosed normalization, slope penalty and gradient budget. On 150 final reference cases, hard/consensus/soft/adjudicated log losses are .394242010/.387891956/.391291221/.391860090 versus frequency .692359484. Soft targets have the lowest Brier error of the four, while consensus has the lowest log loss; no universal label-policy ranking follows.

The strain audit distinguishes a verified day-80 source-unit fault from a valid shared day-120 response to 65 kN loading. It preserves raw lineage and checks times, neighbors, units/calibration and load evidence; no single contextual clue proves physical validity. A separate fixed-delta (.15 mm) Huber IRLS response-corruption experiment converges in six iterations and passes a stationarity check. Raw OLS/Huber/verified-repair OLS final MAE is 3.381644184/.043884739/.043959975 mm. All five valid high-load training members remain; a blind three-standard-deviation rule flags all five even after unit correction. Residual robustness does not handle arbitrary input leverage or decide whether a rare case is task-relevant.

Eight original vector figure sets support the two agreed visual briefs and the numerical comparisons. The Bayesian label, calibration, missingness and robust-objective assumptions remain explicit. No dependency was added; ordinary execution is offline and CPU-only. There were no failed reference notebook runs or hidden final-set tuning. The original robust-loss article was not available through the retrieved DOI landing page, so the chapter cites the primary SciPy mathematical convention and distinguishes its custom fixed-threshold solver from scikit-learn's fitted-scale implementation.

## Successful result dictionaries

### code_047

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1047.

```json
{
  "development_MSE_mm2": {
    "MAR": {
      "median": 0.05686473232579734,
      "median_indicator": 0.05455313085636703
    },
    "MCAR": {
      "median": 0.04581673660218361,
      "median_indicator": 0.04574351574907466
    },
    "MNAR": {
      "median": 0.051527498096929816,
      "median_indicator": 0.04851179152247709
    }
  },
  "dropout_fraction": {
    "MAR": 0.3233333333333333,
    "MCAR": 0.22666666666666666,
    "MNAR": 0.30666666666666664
  },
  "final_MSE_mm2": {
    "MAR": {
      "median": 0.04767742690274684,
      "median_indicator": 0.04823922372614488
    },
    "MCAR": {
      "median": 0.03755836232001528,
      "median_indicator": 0.037406609880808746
    },
    "MNAR": {
      "median": 0.050690066881154336,
      "median_indicator": 0.05119236894639107
    }
  },
  "latent_training_mean_mm": 1.2335155003512952,
  "observed_training_means_mm": {
    "MAR": 1.1000546210178341,
    "MCAR": 1.2362181310656701,
    "MNAR": 1.0547612075211759
  },
  "selected_final_MSE_mm2": {
    "MAR": 0.04823922372614488,
    "MCAR": 0.037406609880808746,
    "MNAR": 0.05119236894639107
  },
  "selected_policy": {
    "MAR": "median_indicator",
    "MCAR": "median_indicator",
    "MNAR": "median_indicator"
  },
  "status_fixture": [
    "absent",
    "structural_unavailability",
    "instrument_failure",
    "left_censored"
  ],
  "training_medians_mm": {
    "MAR": 1.0771010383110893,
    "MCAR": 1.1873937416299567,
    "MNAR": 1.0368660050660674
  }
}
```

### code_048

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1048.

```json
{
  "conflicting_payload_rejected": true,
  "e1_import_lineage": [
    "r1",
    "r2",
    "r7"
  ],
  "e4_grade_by_cutoff": {
    "10": 1,
    "15": 3
  },
  "events": 4,
  "invalid_import_split_overlapping_events": [
    "e1",
    "e4"
  ],
  "raw_import_rows": 7,
  "resolved_event_count": 4,
  "retained_same_grade_distinct_events": [
    "e1",
    "e2"
  ],
  "stable_entities": 3,
  "unique_event_versions": 5
}
```

### code_049

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1049.

```json
{
  "arrival_before_event_flagged": true,
  "canonical_displacements_mm": [
    1.2,
    1.4,
    1.5,
    -0.8
  ],
  "estimated_calibration": {
    "gain": 1.0500494947212786,
    "offset_mm": 0.19968269207721817
  },
  "independent_standard_MAE_mm": {
    "calibrated": 0.003511266914833733,
    "raw": 0.2778523843817003
  },
  "invalid_length_records": 1,
  "same_local_clock_UTC_gap_seconds": 3600,
  "timezone_folds": [
    0,
    1
  ]
}
```

### code_050

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1050.

```json
{
  "adjudicated_labels_changed": 11,
  "development_noisy_A_logloss": {
    "adjudicated": 0.5108691467371568,
    "agreement_only": 0.5164861684550601,
    "hard_A": 0.5102147582194603,
    "soft_posterior": 0.5101360599447783
  },
  "final_reference_cases": 150,
  "final_reference_metrics": {
    "adjudicated": {
      "Brier": 0.12624093749137233,
      "log_loss": 0.3918600896111478
    },
    "agreement_only": {
      "Brier": 0.1263804647219115,
      "log_loss": 0.38789195559905904
    },
    "frequency": {
      "Brier": 0.24960624999999997,
      "log_loss": 0.692359483935645
    },
    "hard_A": {
      "Brier": 0.1264807756768904,
      "log_loss": 0.39424201015057203
    },
    "soft_posterior": {
      "Brier": 0.12575527952602647,
      "log_loss": 0.3912912205011074
    }
  },
  "new_training_adjudications": 20,
  "training_annotation_disagreement": 54,
  "training_cases_by_policy": {
    "adjudicated": 400,
    "agreement_only": 346,
    "hard_A": 400,
    "soft_posterior": 400
  },
  "training_consensus_cases": 346,
  "training_reference_accuracy": {
    "A": 0.895,
    "B": 0.91
  }
}
```

### code_051

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1051.

```json
{
  "Huber_iterations": 6,
  "blind_rule_flagged_valid_high_load_members": 5,
  "final_MAE_mm": {
    "Huber": {
      "ordinary": 0.04267696752971555,
      "overall": 0.04388473881748735,
      "valid_high_load": 0.05596245169520524
    },
    "raw_OLS": {
      "ordinary": 3.313611615850096,
      "overall": 3.381644184003581,
      "valid_high_load": 4.061969865538424
    },
    "verified_repair_OLS": {
      "ordinary": 0.0427690376133826,
      "overall": 0.043959975011618274,
      "valid_high_load": 0.05586934899397507
    }
  },
  "final_counts": {
    "ordinary": 100,
    "valid_high_load": 10
  },
  "fitted_coefficients": {
    "Huber": [
      0.19054346699215993,
      0.8047418062782723
    ],
    "raw_OLS": [
      3.2833023010042965,
      1.2391277893160837
    ],
    "verified_repair_OLS": [
      0.18984056847215566,
      0.8048293945475531
    ]
  },
  "retained_valid_event_day": 120,
  "spike_audit": {
    "day120": {
      "action": "retain valid rare response",
      "load": "known 65-kN event",
      "neighbors": "all three respond",
      "source": "units/calibration unchanged",
      "time": "aligned day120"
    },
    "day80": {
      "action": "convert verified source value; retain raw lineage",
      "neighbors": "no shared spike",
      "source": "sensor0 payload declares 1000x numeric unit conversion",
      "time": "aligned day80; arrival before use"
    }
  },
  "valid_high_load_members_retained": 5,
  "verified_unit_fault_day": 80
}
```


Visual review prompted fresh-kernel reruns of code_048 and code_049 to give timeline labels opaque backgrounds and separate neighboring subplot titles. Both reruns pass with unchanged result dictionaries; the recorded runtimes refer to the current sources.
