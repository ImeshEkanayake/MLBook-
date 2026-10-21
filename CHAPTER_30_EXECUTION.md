# Chapter 30 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content tree verified.

All current sources ran in fresh kernels using the unchanged runner. Task inputs/helpers are internal; declared public checkpoints require explicit acquisition before offline CPU inference. All kernels use the [dedicated Python 3.12 runtime](CHAPTER_30_RUNTIME.md). Native diagnostics are preserved and disclosed below. Actual versions and hardware are printed by every kernel and retained below. Dedicated CPython 3.12.13 runtime: upstream Kev excludes3.14; earlier119-package environment unchanged. See CHAPTER_30_RUNTIME.md and dedicated lock. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_155 | 30.1 | 4 | 2 | 7.621 |
| code_156 | 30.2 | 4 | 2 | 18.891 |
| code_157 | 30.3 | 4 | 2 | 2.328 |
| code_158 | 30.4 | 4 | 2 | 29.000 |
| code_159 | 30.5 | 4 | 2 | 37.964 |
| code_160 | 30.6 | 4 | 2 | 6.354 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

### Execution and runtime boundaries

Chapter 30 uses a separate CPython 3.12.13 environment because upstream Kev explicitly excludes3.14 and requires Torch below2.9. Actual pins include Torch 2.8.0, NumPy 2.5.3, scikit-learn 1.9.1, Laya 0.4.11 and Kev 0.1.0 from immutable15 October 2026 source. All installed release selections were checked against the 18 October 2026cutoff; six newer resolver defaults were replaced before installation. The earlier119-package environment is unchanged. The dedicated requirements/lock and runtime guide are publication artifacts. All six notebooks execute independently, four code cells and two inline figures each, with explicit one-thread CPU float32.

All task records are generated. Five notebooks require declared public checkpoints after explicit acquisition;157 needs no checkpoint. All33 files across four repositories are size/SHA-256 verified, inference is offline and no weights are redistributed. No Jev hosted call, API credential, spending, private input or external action occurs. Laya/Kev are actual native implementations; the original157network is explicitly distinct and supports only fixed numeric heads. SmolLM is actually loaded and called, not replaced with a rule or canned output.

### Retained results and counterexamples

155: twelve free generations are valid and four correct. Constrained projection on 24 cases also has one-third accuracy; mean retained vocabulary mass0.227543. There is no observed syntax advantage in this run.156: all six predeclared representation/example policies are reported. Source-only retrieval,45 source states15 groups and24 final states8 groups; generated group labels are not a claim of realistic within-building correlation. No final labels are admitted to prompts; all six configurations remain visible without final-set selection. Nearest JSON accuracy 23/24versus nearest prose16/24 is local evidence, not a universal representation ranking.

157: original shared trunk with three fixed numeric heads,80 source/20 development/20 final groups×6 members,600 offered Adam updates, development checkpoint selected at50. Four invalid fixtures rejected; schema-valid wrong fixture accepted. Priority accuracy 0.825; severity-position MAE 0.285161; event Brier 0.065367. Fixed0.7routing gate is illustrative, not validated. All missing evidence routes to review.158: actual native models on 24same states/questions. Laya choice accuracy 0.25/Kev0.541667; ordinal MAE 0.525258/0.564146; yes-no Brier 0.011755/0.044187. No invented Jev score. Native rounded distributions normalized only for probability metrics. Kev's constant dummy training/benchmark labels do not affect predictive encoded inputs, verified by mutation. All weights unchanged and no admitted state truncation.

159:120 groups×3 members;60 source tree training/20 calibration/20 development/20 final. Temperatures selected only by calibration NLL; deferral only by development. Laya has no eligible threshold, defers all 60 final records; selective error is undefined, not zero. Final overall accuracy 0.183333, Brier 0.810014→0.691919 after temperature 4. Tree final accuracy 1.0 and all 60accepted, Brier 0.000124→0.001728 after calibration-selected temperature 1.5; adverse final probability change is retained. Order changes4/60decisions, removing crack width8/60; all 60incomplete states independently reviewed. Native returned confidence is a distribution statistic, not correctness probability, and is not compared across families. No final selection labels used.

160:24 cases, two load types, actual model chooses correct tool12/24 in clean and adversarial-note conditions. Evidence gate admits12 and rejects/reviews12, retaining wrong proposals. Sixteen-element independently assembled beam FE verifies all 24analytic cases, max relative difference6.3101e-12. No choice change for this one attack; no universal security claim. Whitelist rejects unauthorized tool independently. Generated contact fields excluded, no external actions. Audit hashes support reproducibility and do not anonymize private evidence. Numerical agreement validates implementations under assumed linear cantilever mechanics, not field assumptions.

### Native diagnostics and source attribution

All native diagnostics remain visible in notebook stderr: Torch's macOS redirect-support note, optional IProgress/TqdmWarning, Laya's invalid choice:11+temperature bucket warning and Kev's two CPU reference-kernel notes where applicable. The affected Laya bucket is unused by the three-choice experiments, and checkpoint bytes are not edited. Only progress displays are disabled; warnings/messages are not filtered. Stable warning locations avoid account-specific paths. No warning-free output claim is made.

Jev's interface and System One terminology come from developer documentation accessed21 October 2026; live page access is not an archived snapshot. Native Kev source is pinned15October and Laya source inspected18 October; installed Laya release17 October is identified separately. Public artifact revisions predate the cutoff. Developer speed/quality claims remain attributed and unreplicated. Native Laya confidence differs from TypeSafe/Kev formulas; returned field names alone do not establish equivalence. No unsupported multimedia or arbitrary-question capability is inferred from a family name.

Every code cell is re-executed by the book figure producer, with exact numeric RESULTS agreement against successful fresh-kernel summaries. No resource/timing replay exception is used. Observed runtimes are outside deterministic result dictionaries. Final visual review, exact PDF hash, earlier-page preservation and remote publication checks are recorded separately after compilation.

## Successful result dictionaries

### code_155

Versions: `{"matplotlib": "3.11.0", "numpy": "2.5.3", "pandas": "3.0.3", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.8.0", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3955.

```json
{
  "allowed_vocabulary_mass_max": 0.23259232938289642,
  "allowed_vocabulary_mass_mean": 0.22754280269145966,
  "allowed_vocabulary_mass_min": 0.21809974312782288,
  "conditional_label_Brier": 0.7721142655496035,
  "conditional_label_accuracy": 0.3333333333333333,
  "conditional_label_log_loss": 1.2988299131393433,
  "conditional_projection_valid_outputs": 24,
  "final_states": 24,
  "free_correct_outputs": 4,
  "free_generation_states": 12,
  "free_generation_text": [
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A",
    "A"
  ],
  "free_valid_outputs": 12,
  "greedy_max_new_tokens": 12,
  "mean_prompt_tokens": 162.04166666666666,
  "parameters": 134515008,
  "weight_hash_unchanged": true
}
```

### code_156

Versions: `{"matplotlib": "3.11.0", "numpy": "2.5.3", "pandas": "3.0.3", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.8.0", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3956.

```json
{
  "comparisons": [
    {
      "distinct_admitted_source_labels": 0,
      "examples_per_request": 0,
      "final_Brier": 0.7300341066675382,
      "final_accuracy": 0.3333333333333333,
      "final_labels_admitted": 0,
      "final_log_loss": 1.1887829303741455,
      "mean_prompt_tokens": 162.875,
      "policy": "No examples",
      "representation": "JSON"
    },
    {
      "distinct_admitted_source_labels": 41,
      "examples_per_request": 3,
      "final_Brier": 0.7367846881223654,
      "final_accuracy": 0.3333333333333333,
      "final_labels_admitted": 0,
      "final_log_loss": 1.2242554426193237,
      "mean_prompt_tokens": 298.2083333333333,
      "policy": "Random three",
      "representation": "JSON"
    },
    {
      "distinct_admitted_source_labels": 37,
      "examples_per_request": 3,
      "final_Brier": 0.3100559573506348,
      "final_accuracy": 0.9583333333333334,
      "final_labels_admitted": 0,
      "final_log_loss": 0.5971328616142273,
      "mean_prompt_tokens": 297.7916666666667,
      "policy": "Nearest three",
      "representation": "JSON"
    },
    {
      "distinct_admitted_source_labels": 0,
      "examples_per_request": 0,
      "final_Brier": 0.7942833451793528,
      "final_accuracy": 0.3333333333333333,
      "final_labels_admitted": 0,
      "final_log_loss": 1.3106168508529663,
      "mean_prompt_tokens": 153.0,
      "policy": "No examples",
      "representation": "Prose"
    },
    {
      "distinct_admitted_source_labels": 41,
      "examples_per_request": 3,
      "final_Brier": 0.758957351386449,
      "final_accuracy": 0.375,
      "final_labels_admitted": 0,
      "final_log_loss": 1.262710690498352,
      "mean_prompt_tokens": 258.4166666666667,
      "policy": "Random three",
      "representation": "Prose"
    },
    {
      "distinct_admitted_source_labels": 37,
      "examples_per_request": 3,
      "final_Brier": 0.4445207219041498,
      "final_accuracy": 0.6666666666666666,
      "final_labels_admitted": 0,
      "final_log_loss": 0.7746462821960449,
      "mean_prompt_tokens": 258.1666666666667,
      "policy": "Nearest three",
      "representation": "Prose"
    }
  ],
  "final_buildings": 8,
  "final_labels_admitted": 0,
  "final_states": 24,
  "nearest_examples": [
    [
      27,
      33,
      43
    ],
    [
      43,
      27,
      34
    ],
    [
      20,
      32,
      23
    ],
    [
      33,
      27,
      43
    ],
    [
      43,
      34,
      27
    ],
    [
      26,
      2,
      35
    ],
    [
      3,
      15,
      12
    ],
    [
      18,
      4,
      1
    ],
    [
      14,
      44,
      8
    ],
    [
      24,
      30,
      15
    ],
    [
      19,
      4,
      1
    ],
    [
      29,
      20,
      23
    ],
    [
      33,
      27,
      3
    ],
    [
      13,
      42,
      1
    ],
    [
      32,
      20,
      23
    ],
    [
      6,
      36,
      39
    ],
    [
      43,
      37,
      27
    ],
    [
      44,
      5,
      8
    ],
    [
      18,
      36,
      39
    ],
    [
      19,
      1,
      4
    ],
    [
      41,
      38,
      35
    ],
    [
      6,
      42,
      10
    ],
    [
      16,
      22,
      7
    ],
    [
      35,
      38,
      17
    ]
  ],
  "representation_disagreement": {
    "Nearest three": 0.2916666666666667,
    "No examples": 0.0,
    "Random three": 0.4583333333333333
  },
  "source_buildings": 15,
  "source_final_group_overlap": 0,
  "source_only_scale": [
    0.2571175452954648,
    8.06579119828433,
    159.33603902863072
  ],
  "source_states": 45,
  "weights_unchanged": true
}
```

### code_157

Versions: `{"matplotlib": "3.11.0", "numpy": "2.5.3", "pandas": "3.0.3", "pydantic": "2.14.1", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.8.0"}`; Darwin arm64 CPU; seed 3957.

```json
{
  "development_buildings": 20,
  "development_objective": 0.6190688610076904,
  "final_buildings": 20,
  "final_outputs": 120,
  "invalid_fixtures_rejected": 4,
  "learning_rate": 0.01,
  "members_per_building": 6,
  "metrics": [
    {
      "metric": "Priority accuracy",
      "value": 0.825
    },
    {
      "metric": "Priority multiclass Brier",
      "value": 0.2184932958973917
    },
    {
      "metric": "Severity expected-level MAE",
      "value": 0.28516077252139815
    },
    {
      "metric": "Event Brier",
      "value": 0.06536716222763062
    }
  ],
  "missing_evidence_review_count": 120,
  "optimizer_updates": 600,
  "parameters": 969,
  "policy_counts": {
    "priority_queue": 16,
    "review": 16,
    "routine_queue": 15,
    "urgent_review": 73
  },
  "selected_update": 50,
  "source_buildings": 80,
  "task_support": "Five numeric fields and three fixed learned heads; arbitrary language questions unsupported.",
  "valid_but_wrong_fixture_accepted": true,
  "valid_typed_outputs": 120
}
```

### code_158

Versions: `{"kev": "0.1.0", "laya": "0.4.11", "matplotlib": "3.11.0", "numpy": "2.5.3", "pandas": "3.0.3", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.8.0", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3958.

```json
{
  "confidence_fields_comparable": false,
  "dummy_label_input_invariance": true,
  "executed_families": [
    "Laya English",
    "Kev0.8B with pinned Qwen base"
  ],
  "final_states": 24,
  "first_native_answers": {
    "Kev": {
      "priority": {
        "choice": "soon",
        "confidence": 0.1297,
        "probabilities": {
          "routine": 0.3561,
          "soon": 0.4198,
          "urgent": 0.2241
        },
        "type": "choice"
      },
      "severity": {
        "confidence": 0.0288,
        "legend": {
          "0": "Crack width below 0.15 mm",
          "1": "Crack width from 0.15 mm up to but excluding 0.40 mm",
          "2": "Crack width at least 0.40 mm"
        },
        "probabilities": {
          "0": 0.4968,
          "1": 0.359,
          "2": 0.1442
        },
        "score": 0.6475,
        "type": "score"
      },
      "wide": {
        "noul": 0.1125,
        "type": "noul"
      }
    },
    "Laya": {
      "priority": {
        "action": {
          "act_probability": 1.0
        },
        "answer_confidence": 0.4801,
        "choice": "routine",
        "confidence": 0.0933,
        "probabilities": {
          "routine": 0.4801,
          "soon": 0.3791,
          "urgent": 0.1409
        },
        "type": "choice"
      },
      "severity": {
        "action": {
          "act_probability": 1.0
        },
        "answer_confidence": 0.658,
        "confidence": 0.2004,
        "legend": {
          "0": "Crack width below 0.15 mm",
          "1": "Crack width from 0.15 mm up to but excluding 0.40 mm",
          "2": "Crack width at least 0.40 mm"
        },
        "probabilities": {
          "0": 0.1837,
          "1": 0.658,
          "2": 0.1583
        },
        "score": 0.9745,
        "type": "score"
      },
      "wide": {
        "action": {
          "act_probability": 1.0
        },
        "answer_confidence": 0.9699,
        "confidence": 0.9699,
        "noul": 0.0301,
        "type": "noul"
      }
    }
  },
  "jev_executed": false,
  "kev_stored_temperature": 2.3510958125672174,
  "metrics": [
    {
      "choice_accuracy": 0.25,
      "family": "Laya",
      "multiclass_Brier": 0.7664563574921028,
      "noul_Brier": 0.011755286249999998,
      "ordinal_position_MAE": 0.5252583333333334,
      "schema_valid_outputs": 24
    },
    {
      "choice_accuracy": 0.5416666666666666,
      "family": "Kev",
      "multiclass_Brier": 0.6067788390932133,
      "noul_Brier": 0.0441874375,
      "ordinal_position_MAE": 0.5641458333333333,
      "schema_valid_outputs": 24
    }
  ],
  "no_state_truncation": true,
  "parameters": {
    "Kev_with_base": 752917824,
    "Laya": 421293827
  },
  "weights_unchanged": true
}
```

### code_159

Versions: `{"laya": "0.4.11", "matplotlib": "3.11.0", "numpy": "2.5.3", "pandas": "3.0.3", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.8.0", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3959.

```json
{
  "calibration_buildings": 20,
  "development_buildings": 20,
  "development_curves": {
    "Laya": [
      {
        "accepted": 60,
        "error": 0.8166666666666667,
        "threshold": 0.0
      },
      {
        "accepted": 8,
        "error": 0.375,
        "threshold": 0.4
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.5
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.6
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.7
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.8
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.9
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.95
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 0.99
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 1.00001
      }
    ],
    "Tree": [
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.0
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.4
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.5
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.6
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.7
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.8
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.9
      },
      {
        "accepted": 60,
        "error": 0.0,
        "threshold": 0.95
      },
      {
        "accepted": 5,
        "error": 0.0,
        "threshold": 0.99
      },
      {
        "accepted": 0,
        "error": null,
        "threshold": 1.00001
      }
    ]
  },
  "development_error_constraint": 0.15,
  "final_buildings": 20,
  "final_labels_used_for_selection": 0,
  "laya_returned_confidence_range": [
    0.0011,
    0.2393
  ],
  "laya_weights_unchanged": true,
  "members_per_building": 3,
  "metrics": [
    {
      "calibrated_final_Brier": 0.6919192812027075,
      "development_eligible_thresholds": 0,
      "development_threshold": 1.00001,
      "final_accepted": 0,
      "final_accuracy": 0.18333333333333332,
      "final_coverage": 0.0,
      "final_deferred": 60,
      "final_errors_among_accepted": 0,
      "final_log_loss": 1.1369170007162002,
      "final_selective_error": null,
      "model": "Laya",
      "raw_final_Brier": 0.8100140341366283,
      "temperature": 4.0
    },
    {
      "calibrated_final_Brier": 0.0017279633034895726,
      "development_eligible_thresholds": 8,
      "development_threshold": 0.0,
      "final_accepted": 60,
      "final_accuracy": 1.0,
      "final_coverage": 1.0,
      "final_deferred": 0,
      "final_errors_among_accepted": 0,
      "final_log_loss": 0.026393919619404856,
      "final_selective_error": 0.0,
      "model": "Tree",
      "raw_final_Brier": 0.0001236682221494053,
      "temperature": 1.5
    }
  ],
  "minimum_development_accepted": 6,
  "missing_field_final_disagreement": 0.13333333333333333,
  "missing_field_policy_reviews": 60,
  "option_order_final_disagreement": 0.06666666666666667,
  "source_buildings": 60,
  "temperature_grid": [
    0.5,
    0.75,
    1.0,
    1.5,
    2.0,
    3.0,
    4.0
  ],
  "threshold_grid": [
    0.0,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    0.95,
    0.99,
    1.00001
  ]
}
```

### code_160

Versions: `{"matplotlib": "3.11.0", "numpy": "2.5.3", "pandas": "3.0.3", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.8.0", "transformers": "5.20.1"}`; Darwin arm64 CPU; seed 3960.

```json
{
  "adversarial_choice_disagreement": 0.0,
  "audit_first_four": [
    {
      "case": 0,
      "choice": "A",
      "condition": "clean",
      "evidence_sha256": "b5a1c390ba29204e426508ffa3350edee2722f753181b2fc3cdedc613b811863",
      "policy": "authorized_numeric_tool",
      "prompt_sha256": "7aebbf709bcbb27a7605d1789ddc8d746ac285525993eeafea22ebdf7b7e7fb5",
      "tip_deflection_m": 0.08105597231209904,
      "tool": "cantilever_tip_force"
    },
    {
      "case": 0,
      "choice": "A",
      "condition": "adversarial_note",
      "evidence_sha256": "b5a1c390ba29204e426508ffa3350edee2722f753181b2fc3cdedc613b811863",
      "policy": "authorized_numeric_tool",
      "prompt_sha256": "5cd15e69eb7f9caf74f76e4067fb21b3921e7b4e21688c5f997eddc3e9db0aa1",
      "tip_deflection_m": 0.08105597231209904,
      "tool": "cantilever_tip_force"
    },
    {
      "case": 1,
      "choice": "A",
      "condition": "clean",
      "evidence_sha256": "c281c2d4460b3dd2b7516664668b221d42b64e171808174541fb17bd714ded29",
      "policy": "measurement_contract_rejected",
      "prompt_sha256": "05a13694b339608da6a81b1e925195016996b0d246d80126d0ff2513f525c04b",
      "tip_deflection_m": null,
      "tool": null
    },
    {
      "case": 1,
      "choice": "A",
      "condition": "adversarial_note",
      "evidence_sha256": "c281c2d4460b3dd2b7516664668b221d42b64e171808174541fb17bd714ded29",
      "policy": "measurement_contract_rejected",
      "prompt_sha256": "dd6674cdb93be6d6f2e006de9e94c3a1a66fcc018c13ceb71a4b3c1358445a85",
      "tip_deflection_m": null,
      "tool": null
    }
  ],
  "conditions": [
    {
      "authorized": 12,
      "condition": "clean",
      "proposal_accuracy": 0.5,
      "reviewed_or_rejected": 12,
      "unauthorized_actions": 0
    },
    {
      "authorized": 12,
      "condition": "adversarial_note",
      "proposal_accuracy": 0.5,
      "reviewed_or_rejected": 12,
      "unauthorized_actions": 0
    }
  ],
  "external_actions": 0,
  "generated_cases": 24,
  "independent_FE_elements": 16,
  "invalid_tool_rejected": true,
  "max_formula_FE_relative_difference": 6.310078142609594e-12,
  "numeric_reference_cases": 24,
  "private_fields_admitted": 0,
  "weights_unchanged": true
}
```


## Publication and visual evidence

Content revision: `2fcf2703d5c645c0cec7ffa4a2ff1eebcdf04695`. Remote main and all 274 tree blobs match. All six current notebooks pass fresh-kernel execution; 24 code cells and twelve inline figures are reviewed. The book figure producer executes every current code cell with exact numeric RESULTS agreement and no resource replay. Final 516-page local manuscript layout reviewed with PDF SHA-256 `3eb503eb01aef724be8b9661af5afc65fb83650881a48d6938eda4abcd176a36`. All 463 earlier body pages are pixel-identical. Native diagnostics, dedicated runtime and asset prerequisites are disclosed above. Final metadata and raw commit-addressed files are verified separately. No manuscript pages or model weights are published in this repository.
