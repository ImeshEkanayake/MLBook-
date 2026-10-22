# Chapter 40 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_211 | 40.1 | 4 | 2 | 1.586 |
| code_212 | 40.2 | 4 | 2 | 1.417 |
| code_213 | 40.3 | 5 | 3 | 1.536 |
| code_214 | 40.4 | 5 | 3 | 1.546 |
| code_215 | 40.5 | 4 | 2 | 1.465 |

Total: **22 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 40 mechanisms, controls and interpretation

Five original laboratories preserve all five scopes and both visual briefs. They execute22 code cells and embed12 figures. Every import, helper and input is internal. Ordinary execution is offline and CPU-only, without credentials or new files/dependencies/assets. All household identities, contacts, locations, role assignments and inspection candidates are fictional generated controls. Runtime remains CPython3.14.3, NumPy2.4.4, SciPy1.17.1, pandas3.0.3, Matplotlib3.11.0, scikit-learn1.9.0 and threadpoolctl3.7.0. Access/execution date22 October2026, Australia/Melbourne; literature cutoff18 October2026. No jurisdiction-specific legal conclusion is asserted.

- **211 / group assessment:** Generated source2,400 candidates, outcome observation depends on group and outcome,1,460 observed source labels. Logistic model omits group but that is not a fairness guarantee. Independent600-case development audit is completely labelled, assumed separately acquired; group thresholds are development-positive20th percentiles0.218083/0.183565, not a complete equalized-odds optimizer. No shared inspection capacity is imposed. Complete final simulator audit1,200 has groups1,052/148 and positives319/84. Common0.5 TPR0.388715/0.404762, FPR0.088677/0.0625, precision0.656085/0.894737, allocation0.179658/0.256757. Development group thresholds yield final TPR0.777429/0.821429, FPR0.306958/0.453125, precision0.524313/0.704082, allocation0.449620/0.662162. Wilson intervals retain true denominators and conditional frequency interpretation. Observed final label coverage0.697719/0.243243; observed group1 has only36 labelled candidates/19 positives, TPR0.315789 with interval[0.153642,0.539900], FPR0/precision1. Those apparently favourable rates do not characterize unobserved outcomes. Full truth is a privileged simulator audit. Four predeclared probability bins per group retain counts/empty bins and Wilson intervals, not simultaneous/refitting uncertainty. Visual A separates support, TPR uncertainty and workload.
- **212 / minimization:**100 fictional households×eight weekly records. HMAC tokens preserve household trajectories; public teaching key is explicitly not a production secret, and pseudonyms are not anonymity. Actual analyst export keeps token/week/temperature/response, removes identity/contact/exact coordinates/equipment serial; unsupported role rejected by an in-memory policy fixture, not production IAM. Raw retention week>=4 removes400/retains400 rows; model/log/backup retention is separate. Exact coordinate auxiliary join uniquely links100 households. Four-by-four coarsening gives zero unique households in this run, candidate-set minimum3/median6, without general linkage or anonymity guarantee. Household holdout tokens overlap0, random-row partitions overlap97 households. Minimize unnecessary disclosure while retaining restricted valid grouping.
- **213 / privacy mechanisms:**100 fictional households×eight bounded readings, mean of household means. Fixed-public-n replacement adjacency protects one whole trajectory; sensitivity0.01 versus row sensitivity0.00125. Worst-case neighbouring all-zero/one-all-one household verifies the bound.2,000 seeded Laplace utility draws for epsilon0.1/0.5/1/4 give MAE0.100269/0.019877/0.009858/0.002513, matching scale0.1/0.02/0.01/0.0025. One private release at each parameter would compose to epsilon5.6. Public seeded simulation on public generated data is explicitly NOT a protected release; real secret entropy/accounting/numerics require separate implementation. No DP training claim. Actual decentralized linear model averaging: ten sites×100 records, nonidentical input means,40 rounds×five local gradient steps, learning rate0.05; centralized200-gradient-step comparator. Independent500-case final RMSE0.321457 federated/0.321418 centralized. First zero-initialized intercept update reveals exact local mean target0.281382. Opposite pairwise float masks cancel arithmetically; no cryptographic secure-aggregation protocol, real key management, dropout or collusion protection is claimed. Source-resampling synthetic candidate copies100/100 rows and deliberately exposes canary[10,10,10], distance0; independent generator copies0, canary distance15.033015. Lack of exact copies is not membership or linkage privacy proof.
- **214 / access-specific threats:** Only own-model/generated-data sandbox exercises; no network/external target. Actual logistic fit1,200 source/500 final,80 high-logit label flips and separate120 appended negative records with trigger1/target1. Ordinary final error clean0.212/label-poison0.242/backdoor0.212. Triggered true-negative positive rates clean0.210526/backdoor0.995951. Rejecting the whole untrusted appended batch recovers clean decisions, but does not detect trusted-source poisoning. Bounded measured-feature evasion L-infinity0.25 flips0.190955 of199 originally detected true positives. Fifty own-model probability queries/log-odds least squares recover the known linear family with agreement1.0; query-volume limit50 is enforced but does not establish extraction resistance. Twenty misleading external-note strings leave the separate strict numeric interface exactly unchanged; unexpected control field rejected. No LLM is invoked and no general prompt-injection defense is claimed. Canonical own-parameter JSON digest detects one-byte alteration relative to a trusted-in-fixture expected digest; not publisher authentication or validation of a real dependency chain. Visual B labels record access, training writes, artifacts and serving interfaces.
- **215 / use and responsibility:** Actual logistic model1,000 source/500 final, Brier0.185435/error0.284. Fifteen-field record binds actual metrics/model digest, provenance, purpose, excluded clearance use, limitations and fictional decision-owner/incident roles. Missing owner fails; completeness does not establish adequacy. Fictional state/role sequence draft→verified→review_ready→suspended→retired; no actual human approval or production release. Only review-prioritization requests are allowed in review_ready; wrong role, excluded structural-clearance use, suspended review and retired reopening are rejected. Unit-metadata incident and dispositions persist in nine-event canonical SHA256 chain. Modified historical payload fails verification, while unkeyed-chain rewrite with a replaced trusted head remains possible. No automatic structural-safe judgment or legal compliance certificate.

All initial fresh kernels pass with assertions and no notebook errors/stderr. Numerical RESULTS rerun in isolated vector-export processes agree exactly. Plot-only book label wrapping repairs retain scientific results.12 original SVG/vector-PDF/PNG sets and actual inline versions are reviewed during delivery. Full primary PDFs inspected for Hardt/Price/Srebro2016 fairness, Dwork/Roth2014 DP definition/Laplace/composition, McMahan et al.2017 federated averaging, NIST AI100-2e2025 taxonomy/prompt-injection interfaces and Mitchell et al.2019 model cards. The original generated mechanisms are not benchmark reproductions, actual privacy releases, real IAM/cryptographic protocols, live dependency audits, LLM injection tests or real human approvals. Chapters41–43 and the whole-book audit remain required.

## Successful result dictionaries

### code_211

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8011.

```json
{
  "complete_final_truth_is_privileged_audit": true,
  "development_complete_audit_candidates": 600,
  "final_candidates": 1200,
  "final_observed_label_coverage": {
    "0": 0.6977186311787072,
    "1": 0.24324324324324326
  },
  "full_simulator_calibration_bins": {
    "0": [
      {
        "Wilson95": [
          0.11225276875217668,
          0.16604736216671181
        ],
        "finding_frequency": 0.13694267515923567,
        "mean_probability": 0.11079816171202975,
        "n": 628
      },
      {
        "Wilson95": [
          0.40116307619611696,
          0.5276600433944401
        ],
        "finding_frequency": 0.46382978723404256,
        "mean_probability": 0.3641223877760179,
        "n": 235
      },
      {
        "Wilson95": [
          0.5132427445954546,
          0.6731677893947803
        ],
        "finding_frequency": 0.5957446808510638,
        "mean_probability": 0.6153187535097716,
        "n": 141
      },
      {
        "Wilson95": [
          0.7042189996260375,
          0.9130458996054678
        ],
        "finding_frequency": 0.8333333333333334,
        "mean_probability": 0.8318927317987006,
        "n": 48
      }
    ],
    "1": [
      {
        "Wilson95": [
          0.2257039576708776,
          0.45001123772545737
        ],
        "finding_frequency": 0.328125,
        "mean_probability": 0.12268720442437929,
        "n": 64
      },
      {
        "Wilson95": [
          0.48599833149184785,
          0.7547644048569049
        ],
        "finding_frequency": 0.6304347826086957,
        "mean_probability": 0.351488815174392,
        "n": 46
      },
      {
        "Wilson95": [
          0.741507847985494,
          0.9768416721570266
        ],
        "finding_frequency": 0.9166666666666666,
        "mean_probability": 0.6228735376742596,
        "n": 24
      },
      {
        "Wilson95": [
          0.600580922361363,
          0.9599069262620787
        ],
        "finding_frequency": 0.8571428571428571,
        "mean_probability": 0.8097293306729184,
        "n": 14
      }
    ]
  },
  "full_simulator_group_audit": {
    "Common 0.5": {
      "0": {
        "Brier": 0.16284379523483358,
        "FPR": 0.08867667121418826,
        "TPR": 0.3887147335423197,
        "TPR_Wilson95": [
          0.3368485338739036,
          0.4432293743014987
        ],
        "allocation_fraction": 0.1796577946768061,
        "n": 1052,
        "positives": 319,
        "precision": 0.656084656084656,
        "selected": 189
      },
      "1": {
        "Brier": 0.24567595081967897,
        "FPR": 0.0625,
        "TPR": 0.40476190476190477,
        "TPR_Wilson95": [
          0.3061943608400985,
          0.511659594461262
        ],
        "allocation_fraction": 0.25675675675675674,
        "n": 148,
        "positives": 84,
        "precision": 0.8947368421052632,
        "selected": 38
      }
    },
    "Development group thresholds": {
      "0": {
        "Brier": 0.16284379523483358,
        "FPR": 0.3069577080491132,
        "TPR": 0.7774294670846394,
        "TPR_Wilson95": [
          0.7286323706579042,
          0.8196241117780644
        ],
        "allocation_fraction": 0.44961977186311786,
        "n": 1052,
        "positives": 319,
        "precision": 0.5243128964059197,
        "selected": 473
      },
      "1": {
        "Brier": 0.24567595081967897,
        "FPR": 0.453125,
        "TPR": 0.8214285714285714,
        "TPR_Wilson95": [
          0.7260538098918103,
          0.8886890909660974
        ],
        "allocation_fraction": 0.6621621621621622,
        "n": 148,
        "positives": 84,
        "precision": 0.7040816326530612,
        "selected": 98
      }
    }
  },
  "group_development_thresholds": {
    "0": 0.21808340159925,
    "1": 0.18356527358825228
  },
  "group_thresholds_are_not_full_equalized_odds_optimizer": true,
  "observed_label_only_group_audit": {
    "0": {
      "Brier": 0.12919106063884073,
      "FPR": 0.07118055555555555,
      "TPR": 0.4177215189873418,
      "TPR_Wilson95": [
        0.34366586483680284,
        0.4956832271148338
      ],
      "allocation_fraction": 0.14577656675749318,
      "n": 734,
      "positives": 158,
      "precision": 0.616822429906542,
      "selected": 107
    },
    "1": {
      "Brier": 0.25939770602995843,
      "FPR": 0.0,
      "TPR": 0.3157894736842105,
      "TPR_Wilson95": [
        0.15364171004428598,
        0.5398998982493537
      ],
      "allocation_fraction": 0.16666666666666666,
      "n": 36,
      "positives": 19,
      "precision": 1.0,
      "selected": 6
    }
  },
  "shared_capacity_constraint_imposed": false,
  "source_candidates": 2400,
  "source_observed_labels": 1460
}
```

### code_212

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8012.

```json
{
  "analyst_export_fields": [
    "group_token",
    "week",
    "temperature",
    "response"
  ],
  "coarse_candidate_set_median": 6.0,
  "coarse_candidate_set_min": 3,
  "coarsened_coordinate_unique_households": 0,
  "coordinate_omission_does_not_prevent_all_linkage": true,
  "exact_coordinate_unique_households": 100,
  "fictional_households": 100,
  "group_holdout_token_overlap": 0,
  "grouping_preserved": true,
  "in_memory_policy_is_not_production_IAM": true,
  "pseudonym_is_not_anonymity": true,
  "public_teaching_key_is_not_secret": true,
  "random_row_split_token_overlap": 97,
  "raw_fields": [
    "household_id",
    "group_token",
    "week",
    "temperature",
    "response",
    "contact",
    "x_coord",
    "y_coord",
    "equipment_serial"
  ],
  "removed_raw_records": 400,
  "retained_raw_records": 400,
  "unsupported_role_rejected": true,
  "weekly_records": 800
}
```

### code_213

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8013.

```json
{
  "DP_training_claimed": false,
  "adjacency": "replace one entire household trajectory at fixed public n=100",
  "arithmetic_masks_cancel": true,
  "cryptographic_secure_aggregation_implemented": false,
  "federated_clients": 10,
  "federated_final_RMSE": {
    "Centralized gradient": 0.32141807302192765,
    "Federated averaging": 0.3214568179367825
  },
  "federated_fit_has_DP_guarantee": false,
  "federated_rounds": 40,
  "fictional_households": 100,
  "first_site_mean_target": 0.2813824232123051,
  "household_mean_sensitivity": 0.01,
  "local_steps_per_round": 5,
  "mean_target_recovered_from_single_update": 0.2813824232123051,
  "no_exact_copy_is_not_privacy_proof": true,
  "privacy_utility_simulation": {
    "0.1": {
      "Laplace_scale": 0.09999999999999999,
      "analytic_MAE": 0.09999999999999999,
      "central95_absolute_error": 0.30243807844293186,
      "empirical_MAE": 0.10026899550874763
    },
    "0.5": {
      "Laplace_scale": 0.02,
      "analytic_MAE": 0.02,
      "central95_absolute_error": 0.061166895615582736,
      "empirical_MAE": 0.019877436042857886
    },
    "1.0": {
      "Laplace_scale": 0.01,
      "analytic_MAE": 0.01,
      "central95_absolute_error": 0.030026518283313382,
      "empirical_MAE": 0.009858052035634777
    },
    "4.0": {
      "Laplace_scale": 0.0025,
      "analytic_MAE": 0.0025,
      "central95_absolute_error": 0.007515247068549003,
      "empirical_MAE": 0.0025131496552979666
    }
  },
  "public_seeded_simulation_is_private_release": false,
  "records_per_client": 100,
  "row_level_sensitivity_understatement_factor": 8,
  "rows_per_household": 8,
  "sequential_one_each_epsilon": 5.6,
  "synthetic_disclosure_fixture": {
    "Independent generator": {
      "canary_nearest_release_distance": 15.033014851573554,
      "exact_source_copies": 0,
      "median_nearest_source_distance": 0.30268578175406097,
      "released_rows": 100
    },
    "Source resampling": {
      "canary_nearest_release_distance": 0.0,
      "exact_source_copies": 100,
      "median_nearest_source_distance": 0.0,
      "released_rows": 100
    }
  }
}
```

### code_214

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8014.

```json
{
  "artifact_digest_change_detected": true,
  "backdoor_appended_records": 120,
  "bounded_evasion_Linf": 0.25,
  "clean_final_error": {
    "Clean": 0.212,
    "Flipped labels": 0.242,
    "Trigger poisoned": 0.212
  },
  "digest_is_not_publisher_authentication": true,
  "evasion_detected_positive_denominator": 199,
  "evasion_flip_rate": 0.19095477386934673,
  "final_records": 500,
  "language_model_prompt_injection_tested": false,
  "note_instruction_fixtures": 20,
  "note_probability_unchanged": true,
  "own_model_extraction_agreement": 1.0,
  "own_model_extraction_queries": 50,
  "provenance_control_covers_trusted_poison": false,
  "query_limit_enforced": true,
  "real_dependency_chain_validated": false,
  "source_label_flips": 80,
  "source_records": 1200,
  "triggered_true_negative_positive_rate": {
    "Backdoor": 0.9959514170040485,
    "Clean": 0.21052631578947367
  },
  "unexpected_control_field_rejected": true,
  "untrusted_batch_rows_rejected": 120
}
```

### code_215

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8015.

```json
{
  "audit_chain_valid": true,
  "audit_head": "ef1e50b9f73bf90571e3b915d42743817e219e7bc1de6ac553712e6b947d6c64",
  "excluded_clearance_rejected": true,
  "final_state": "retired",
  "historical_payload_change_detected": true,
  "independent_final_metrics": {
    "Brier": 0.18543470961942962,
    "error": 0.284,
    "final_n": 500
  },
  "lifecycle_event_count": 9,
  "missing_owner_rejected": true,
  "real_human_approval_claimed": false,
  "record_completeness_is_not_validity": true,
  "required_fields": 15,
  "retired_reopen_rejected": true,
  "simulated_roles_are_not_real_approval": true,
  "source_candidates": 1000,
  "suspended_review_rejected": true,
  "unkeyed_chain_is_not_authentication": true,
  "use_record": {
    "data_provenance": "locally generated fictional candidates; no real household data",
    "decision_owner_role": "fictional qualified structural engineer",
    "evidence": {
      "Brier": 0.18543470961942962,
      "error": 0.284,
      "final_n": 500
    },
    "excluded_use": "structural_clearance",
    "group_evidence": "not established by this small lifecycle fixture; see separate group audit",
    "incident_route": "suspend review support and route to fictional service owner",
    "information_boundary": "source fit; independent frozen final assessment",
    "intended_use": "review_prioritization",
    "model_digest": "ac74def2d55e19a0ad205f8767e975d4d210fc834c31a3f1b4b2385e702c284e",
    "model_id": "fictional-review-model",
    "privacy_limit": "no private data; no DP trained model claim",
    "review_date": "2026-10-22",
    "security_limit": "in-memory test; no production IAM or supply-chain validation",
    "target_event": "generated actionable inspection finding",
    "version": "1.0-fixture"
  },
  "wrong_role_rejected": true
}
```

