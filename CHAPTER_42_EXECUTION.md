# Chapter 42 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_221 | 42.1 | 4 | 2 | 1.510 |
| code_222 | 42.2 | 4 | 2 | 1.795 |
| code_223 | 42.3 | 4 | 2 | 1.720 |
| code_224 | 42.4 | 4 | 2 | 1.514 |
| code_225 | 42.5 | 4 | 2 | 1.514 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 42 mechanisms, controls and interpretation

Five original laboratories retain all five scopes and both visual briefs: **20 fresh-kernel code cells and 10 embedded figures**. Imports, helpers and generated inputs are internal. Ordinary execution is offline and CPU-only, without files, credentials, a GPU or new dependencies/assets. Runtime: Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0. Complete outcomes and potential outcomes are privileged simulator audit controls. Operational comparisons respect declared availability. Owners and approvals are fictional fixtures. Access/execution: 22 October 2026, Australia/Melbourne; literature cutoff: 18 October 2026.

- **221 — monitoring clocks.** A logistic model fits 1,000 source records; 6,000 requests span 120 days. Missingness increases from 2% to 18% at day 40; the response law reverses at day 65. There are 5,132 scored, 814 invalid and 54 deferred requests. Latencies are generated scenario values, not measured service timings. A seven-day outcome window precedes reporting delays of three additional days for positives and seven for negatives. At day 80, 3,079 scored labels are visible, but only 2,997 belong to the conservative fourteen-day mature cohort. Recent days 67–73 contain 287 scored requests and 82 visible labels, all positive, versus complete privileged positive frequency 0.529617. Visible Brier is 0.355795 versus privileged full-cohort 0.339970. Pending outcomes are never assigned zero. Original probabilities and IDs support as-of joins; the last partial mature cohort contains 164 cases with Brier 0.276617. Fictional owner/cadence/response specifications cover score coverage below 0.9, timeout fraction above 0.02 and mature Brier above 0.27. These thresholds are teaching choices. Visual A shows input, prediction, action, outcome, reporting and maturity clocks.
- **222 — drift and alert quality.** Reference and current years each have 52 weeks of 100 independent records. Seasonal temperature is irrelevant to the response; severity drives the logistic event. Actual pooled-temperature KS tests alert in all 52 weeks under nominal and fixed-family Bonferroni rules. Same-phase references produce two nominal and zero corrected alerts. Each route has 52 predeclared looks; their null populations differ. A known response-law reversal at week 32 leaves inputs stable but raises Brier from 0.170982 to 0.478830. Mean predictions remain 0.488548/0.497140. A three-week label delay makes the first fixed-threshold 0.30 quality alert available at week 35. In 2,000 explicit independent-uniform null years, any nominal alert occurs in 0.9405, versus analytic 0.930557; corrected simulation frequency is 0.056, a finite Monte Carlo observation rather than a theoretical failure. Fixed-family control requires valid individual p-values and does not establish indefinite sequential validity. No ADWIN implementation is claimed.
- **223 — selective labels and feedback.** The model fits 1,000 complete source labels, then scores 4,000 candidates with a new low-severity risk term. Deterministic p≥0.6 inspection observes 1,522 labels: observed Brier 0.169399 versus complete privileged 0.249661, with zero low-score support. A separate generated audit samples high scores with probability one and low scores with probability 0.15, observing 1,884 labels. Its unweighted Brier is 0.194977 and known-propensity Horvitz–Thompson estimate 0.246976. Positive known support is essential; weighting cannot recover arbitrary unknown selection or zero-support regions. On 2,000 independent final cases, frozen/selected/audit-weighted/wrong zero-filled update Brier is 0.246126/0.250162/0.223609/0.359562. Final results do not select a release. Repair is assigned to 1,035 selected cases with probability 0.7; untreated selected positive frequency 0.764783 becomes 0.254271 after the policy. Actions, observation and target versions are logged. Full potential outcomes are simulator controls, not identified field counterfactuals. No consequential real randomization, contraction method or performative-convergence implementation occurs.
- **224 — updates and gate.** Eight independent 200-row blocks provide source 0–2 (600 rows), mature update 3–4 (400), development 5 (200) and untouched final 6–7 (400). The new sensor negates feature zero and adds 0.8 from block three; latent response is unchanged. Actual alternatives are frozen logistic, unconstrained sigmoid old-logit remapping, full old-plus-new refit, recent-only refit and SGD partial updates with an old-source fixed scaler. Remapping learns a negative slope and reverses ordering; it is broader than increasing calibration or positive-temperature scaling. Historical rolling Brier is 0.179815 before the boundary and 0.454545 at it, using no future information. Development selects recent refit at 0.192206 versus frozen 0.409977, under a fixed improvement≥0.01/Brier<0.25 gate. Final Brier is frozen 0.413714, remapped 0.222103, full 0.260416, recent 0.193326 and incremental 0.232649. Scheduled investigations and old mature-loss>0.30 triggers both occur at blocks three/four; neither bypasses validation. Injected rollback exactly restores retained old predictions, which does not establish their scientific adequacy for the new sensor. Visual B shows roles, gate, release fixture and recoverable prior; no actual human approval occurs.
- **225 — incident and retirement.** A 1,200-row source model uses kN load and age in decades. An authored eight-kN/thirty-year finding fixture passes through defective feature-v1, which always divides load by 1,000. Historical probability is 0.087094 with no alarm at 0.5; corrected feature-v2 gives 0.932916. Canonical raw snapshot, digest, data/schema, feature, model and decision versions are retained. Exact replay succeeds; replacing history with the latest feature would conceal the miss. Corrected eight-kN/eight-thousand-N equivalence and unknown-unit rejection pass. Fictional owner transitions are active → suspended → repair_verified → retired. A requested immediate structural-clearance use exceeds annual finding-priority evidence and returns rejected with no probability. The original snapshot stays unchanged; its digest does not establish identity or tamperproof storage. No live approval or structural clearance is claimed.

Initial kernels pass. Notebook 224 was rerun after adding its remapping slope and arranging the gate vertically for the book; 225 was rerun after replacing an illustrative numerical lifecycle display with categorical state transitions. Notebook 221 was rerun to separate crowded timeline labels. Current outputs have no errors/stderr. Independent vector exports rerun every code cell and require exact scientific RESULTS. All book and embedded figures are inspected during delivery.

Primary sources inspected: Bifet/Gavaldà's expanded author preprint dated 17 October 2006 (17 pages, distinguished from the six-page SDM 2007 proceedings paper); Perdomo/Zrnic/Mendler-Dünner/Hardt's eleven-page ICML 2020 paper; and Lakkaraju/Kleinberg/Leskovec/Ludwig/Mullainathan's KDD 2017 primary author manuscript at PMC5958915. The Stanford selective-label PDF fetch failed; the primary PMC full text was successfully inspected instead. Chapter 43 and the whole-book editorial/technical audit remain required.

## Successful result dictionaries

### code_221

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8021.

```json
{
  "asof_day": 80,
  "deferred_requests": 54,
  "eligible_requests": 6000,
  "historical_probabilities_preserved": true,
  "invalid_requests": 814,
  "latencies_are_generated_scenario_values": true,
  "mature_cohort_scores": [
    {
      "Brier": 0.19655221302726458,
      "n": 337,
      "prediction_start_day": 0
    },
    {
      "Brier": 0.2027564007441759,
      "n": 335,
      "prediction_start_day": 7
    },
    {
      "Brier": 0.1967051891825766,
      "n": 343,
      "prediction_start_day": 14
    },
    {
      "Brier": 0.19679582307797183,
      "n": 339,
      "prediction_start_day": 21
    },
    {
      "Brier": 0.20086160038891365,
      "n": 340,
      "prediction_start_day": 28
    },
    {
      "Brier": 0.19270384745233574,
      "n": 326,
      "prediction_start_day": 35
    },
    {
      "Brier": 0.18850372413728694,
      "n": 277,
      "prediction_start_day": 42
    },
    {
      "Brier": 0.18175245124559225,
      "n": 267,
      "prediction_start_day": 49
    },
    {
      "Brier": 0.19438036120361757,
      "n": 269,
      "prediction_start_day": 56
    },
    {
      "Brier": 0.27661669933232585,
      "n": 164,
      "prediction_start_day": 63
    }
  ],
  "mature_scored_labels": 2997,
  "monitoring_specification": {
    "input_coverage": {
      "cadence": "daily",
      "owner": "fictional data steward",
      "response": "investigate channel and report invalid count",
      "trigger": "coverage below 0.9"
    },
    "quality": {
      "cadence": "weekly mature cohorts",
      "owner": "fictional model owner",
      "response": "investigate; no automatic replacement",
      "trigger": "mature Brier above 0.27"
    },
    "serving": {
      "cadence": "daily",
      "owner": "fictional operations owner",
      "response": "inspect serving path; preserve dispositions",
      "trigger": "timeout fraction above 0.02"
    }
  },
  "pending_outcomes_are_zero": false,
  "recent_cohort_scored": 287,
  "recent_cohort_visible": 82,
  "recent_complete_privileged_Brier": 0.3399704102891845,
  "recent_full_simulator_positive_fraction": 0.5296167247386759,
  "recent_visible_Brier": 0.3557952218375712,
  "recent_visible_positive_fraction": 1.0,
  "scored_requests": 5132,
  "source_rows": 1000,
  "visible_labels": 3079
}
```

### code_222

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8022.

```json
{
  "ADWIN_implemented": false,
  "analytic_independent_nominal_family_probability": 0.9305571598127664,
  "changed_Brier": 0.4788300383660915,
  "changed_conditional_week": 32,
  "current_rows": 5200,
  "first_changed_quality_alert_available_week": 35,
  "null_p_values_assumed_independent_uniform": true,
  "null_years": 2000,
  "phase_matched_temperature_Bonferroni_alerts": 0,
  "phase_matched_temperature_nominal_alerts": 2,
  "pooled_temperature_Bonferroni_alerts": 52,
  "pooled_temperature_nominal_alerts": 52,
  "prechange_Brier": 0.17098218416967437,
  "prediction_mean_changed": 0.4971400801046323,
  "prediction_mean_prechange": 0.48854775208216794,
  "probability_any_Bonferroni_null_alert": 0.056,
  "probability_any_nominal_null_alert": 0.9405,
  "quality_label_delay_weeks": 3,
  "quality_threshold_fixed": 0.3,
  "reference_rows": 5200,
  "temperature_is_response_irrelevant": true,
  "weekly_temperature_looks": 52
}
```

### code_223

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8023.

```json
{
  "action_and_label_versions_logged": true,
  "audit_Horvitz_Thompson_Brier": 0.24697592278307665,
  "audit_low_score_probability": 0.15,
  "audit_observed_labels": 1884,
  "audit_observed_only_Brier": 0.19497719558312887,
  "contraction_or_performative_convergence_implemented": false,
  "deployment_candidates": 4000,
  "deterministic_low_score_observation_probability": 0.0,
  "deterministic_observed_labels": 1522,
  "deterministic_observed_only_Brier": 0.16939899730135952,
  "final_update_Brier": {
    "Audit update": 0.2236085591569637,
    "Frozen": 0.24612644810607953,
    "Selected update": 0.25016216738591474,
    "Zero-filled wrong": 0.35956237311255956
  },
  "full_potential_outcomes_are_privileged_simulator_controls": true,
  "full_privileged_Brier": 0.24966069468115987,
  "independent_final_candidates": 2000,
  "known_positive_propensity_assumption": true,
  "post_repair_selected_positive_rate": 0.2542706964520368,
  "repair_actions": 1035,
  "source_complete_labels": 1000,
  "unobserved_outcomes_are_zero": false,
  "untreated_selected_positive_rate": 0.7647831800262812
}
```

### code_224

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8024.

```json
{
  "development_Brier": {
    "Frozen": 0.40997707049005505,
    "Full refit": 0.2655020065119007,
    "Incremental": 0.2400404534475043,
    "Recalibration": 0.21331550015196002,
    "Recent refit": 0.1922055329761992
  },
  "development_block": 5,
  "development_gate_passed": true,
  "development_rows": 200,
  "development_selected_candidate": "Recent refit",
  "final_Brier": {
    "Frozen": 0.4137136818994276,
    "Full refit": 0.2604157071421511,
    "Incremental": 0.23264944669028118,
    "Recalibration": 0.22210339701942755,
    "Recent refit": 0.19332641203401132
  },
  "final_rows": 400,
  "gate_uses_final_outcomes": false,
  "incremental_scaler_fitted_on_old_source_only": true,
  "mature_evidence_trigger_blocks": [
    3,
    4
  ],
  "mature_update_blocks": [
    3,
    4
  ],
  "old_source_blocks": [
    0,
    1,
    2
  ],
  "real_human_approval_executed": false,
  "recalibration_logit_slope": -0.6694363150524726,
  "released_scenario_route": "Recent refit",
  "rollback_prior_predictions_exact": true,
  "rolling_origin_checks": [
    {
      "Brier": 0.17981497304476368,
      "target_block": 2,
      "training_blocks": [
        0,
        1
      ]
    },
    {
      "Brier": 0.45454512994852053,
      "target_block": 3,
      "training_blocks": [
        1,
        2
      ]
    }
  ],
  "scheduled_investigation_blocks": [
    3,
    4
  ],
  "source_rows": 600,
  "trigger_old_Brier": [
    0.4533081009715574,
    0.4116382959631424
  ],
  "untouched_final_blocks": [
    6,
    7
  ],
  "update_rows": 400
}
```

### code_225

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8025.

```json
{
  "corrected_latest_feature_probability": 0.9329164782400007,
  "equivalent_units_repair_passed": true,
  "historical_exact_replay": true,
  "historical_record": {
    "alarm": false,
    "data_version": "snapshot17/schema1",
    "decision_version": "policy-v1/threshold0.5",
    "feature_version": "feature-v1",
    "generated_observed_finding": 1,
    "model_version": "risk-v1",
    "probability": 0.0870942978348489,
    "snapshot_sha256": "f05e55a364671948b032b5cd03110df603b40416720ac1459185cb5c90049d9f",
    "threshold": 0.5
  },
  "incident_events": [
    {
      "from": "active",
      "owner": "incident_owner",
      "reason": "feature-v1 unit defect; retain snapshot17",
      "to": "suspended"
    },
    {
      "from": "suspended",
      "owner": "reviewer",
      "reason": "feature-v2 equivalent-unit and rejection fixtures pass",
      "to": "repair_verified"
    },
    {
      "from": "repair_verified",
      "owner": "decision_owner",
      "reason": "requested immediate structural clearance exceeds annual finding target",
      "to": "retired"
    }
  ],
  "latest_feature_would_conceal_missed_alarm": true,
  "original_snapshot_unchanged": true,
  "real_human_approval_or_structural_clearance": false,
  "retired_state": "retired",
  "source_rows": 1200,
  "unknown_unit_rejected": true,
  "unsupported_task_request": {
    "probability": null,
    "status": "rejected"
  }
}
```

