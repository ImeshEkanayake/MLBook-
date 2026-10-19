# Chapter 8 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** five executed; publication verification pending.

All five sources ran in fresh kernels using the unchanged runner. All inputs and helpers are defined inside their notebooks; ordinary runs are offline and CPU-only. Reference: CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0, Darwin arm64. No dependency was added. Initial runs started concurrently; the joins notebook was rerun individually after clearing its plot legend from the data. Wall times include kernel lifecycle and are observations, not comparative speed claims.

| ID | Section | Executed cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_037 | 8.1 | 5 | 2 | 2.240 |
| code_038 | 8.2 | 5 | 2 | 1.256 |
| code_039 | 8.3 | 5 | 2 | 2.255 |
| code_040 | 8.4 | 5 | 2 | 2.224 |
| code_041 | 8.5 | 6 | 2 | 3.415 |

Total: **26 executed code cells and ten inline figures**, seeds 837–841. Current reference executions pass every assertion and contain no error outputs. Four laboratories validate construction mechanisms rather than fit predictive models. The sampling laboratory freezes two specified constants before opening its independent final population; it uses no tuning or model selection.

## Actual outputs and boundaries

- **Targets:** 465 candidate member-week keys; day 60 has 36 positive, 276 negative, 102 pending and 51 censored rows. Resolved fraction .115384615 differs from unsupported zero-filled .077419355. Twenty-one members share an event across multiple horizons. No first-event hazard or independent-row evidence is implied.
- **Relations:** 4 buildings, 12 members, 21 sensors, 42 readings and 30 inspections produce 96 unsafe combinations, dropping member 11. Repetition changes mean length from 7.5 to 7.166666667 m. Separate summaries restore 12 unique members and preserve the missing sensor state. All records are historical; this lab isolates cardinality.
- **Availability:** 12 historical queries retain 7 valid and 5 missing/stale features. Using current revisions admits 8 future-upload violations. Member 0 uses .02/.06/.10 mm at days 5/9/13. Appending a day-40 revision leaves every historical feature, timestamp and missingness state unchanged.
- **Sampling/labels:** frame prevalence .13, inspection prevalence .28, known-design weighted .135. Independent final Brier errors .13252/.108015 for inspection/weighted constants. Proxy has 44 abstentions; non-abstain accuracy .870786517, annotator A/B accuracy .9/.8325 and mutual agreement .7575. These depend on known simulator selection and error mechanisms, not empirical annotation or field reliability.
- **Storage:** 23 observations form a 6×4 view with one masked slot distinct from a genuine zero. A graph permutation test checks identity/adjacency consistency. Safe numeric archive loading preserves arrays, IDs and masks. Same mesh vertices/values but different diagonals yield center temperatures 300/297.5 K; no PDE is solved.

Seven book figures comprise six selected executed plots and one original relational diagram, with exact result-dictionary agreement against these runs. Snapshot labels, weights, joins and array identities have different evidential roles; none establishes measurement validity. The dataset card is a scoped, human-reviewable teaching record. Full original source and successful outputs are committed with the notebooks. No manuscript, outline or book figures are published here.

## Successful result dictionaries

### code_037

```json
{
  "candidate_examples": 465,
  "day60_status_counts": {
    "censored": 51,
    "negative": 276,
    "pending": 102,
    "positive": 36
  },
  "members": 80,
  "members_with_event_in_multiple_windows": 21,
  "resolved_counts_by_extract": {
    "45": 168,
    "60": 312,
    "80": 416
  },
  "resolved_prevalence_day60": 0.11538461538461539,
  "unsupported_zero_filled_prevalence_day60": 0.07741935483870968
}
```

### code_038

```json
{
  "cardinality_error_caught": true,
  "dropped_member_ids": [
    11
  ],
  "equal_member_mean_length_m": 7.5,
  "repaired_rows": 12,
  "rows_per_member_unsafe": [
    2,
    8,
    18,
    8,
    4,
    12,
    6,
    16,
    6,
    4,
    12,
    0
  ],
  "source_counts": {
    "buildings": 4,
    "inspections": 30,
    "members": 12,
    "readings": 42,
    "sensors": 21
  },
  "unsafe_row_mean_length_m": 7.166666666666667,
  "unsafe_rows": 96
}
```

### code_039

```json
{
  "future_append_preserves_past": true,
  "historical_cases": 12,
  "invalid_current_revision_cases": 8,
  "member0_features_days5_9_13": [
    0.02,
    0.06,
    0.1
  ],
  "missing_or_stale_cases": 5,
  "valid_cases": 7
}
```

### code_040

```json
{
  "dataset_card": {
    "availability": "all source labels resolved before final population is assessed",
    "frame": "2000 generated buildings; older share .2",
    "label_sources": [
      "reference inspection",
      "alarm proxy with abstention",
      "annotator A",
      "annotator B"
    ],
    "limitations": [
      "known positive inclusion probabilities",
      "same-stratum final simulator only",
      "no field validation",
      "no causal conclusion"
    ],
    "missing_labels": "uninspected and abstained are unknown, not negative",
    "provenance": "synthetic generator and seed printed in this notebook",
    "selection": "240/400 older;160/1600 newer, simple random within strata",
    "target": "reference inspection finding, not physical failure",
    "unit": "building at fixed baseline date",
    "version": "1.0"
  },
  "design_weighted_prevalence": 0.135,
  "final_Brier": {
    "inspection_constant": 0.13252,
    "weighted_constant": 0.10801500000000001
  },
  "final_prevalence": 0.123,
  "frame_finding_prevalence": 0.13,
  "frame_size": 2000,
  "inspection_prevalence": 0.28,
  "inspection_size": 400,
  "label_source_checks": {
    "A/B agreement": 0.7575,
    "Annotator A": 0.9,
    "Annotator B": 0.8325,
    "Proxy (non-abstain)": 0.8707865168539326
  },
  "older_share_frame": 0.2,
  "older_share_sample": 0.6,
  "proxy_abstentions": 44
}
```

### code_041

```json
{
  "graph_permutation_preserves_values": true,
  "mesh_center_temperature_K": {
    "diagonal_0_2": 300.0,
    "diagonal_1_3": 297.5
  },
  "missing_values": 1,
  "neighbor_mean_length_m": [
    3.0,
    3.0,
    3.0,
    3.5,
    3.5,
    3.5
  ],
  "observation_count": 23,
  "safe_numeric_roundtrip": true,
  "schema": {
    "days": [
      0,
      1,
      2,
      3
    ],
    "dtypes": {
      "ids": "int64",
      "mask": "bool",
      "values": "float64"
    },
    "edges": "undirected physical neighbors; each stored once",
    "missing": "boolean mask; zero is placeholder only where false",
    "node_key": "stable member_id",
    "node_order": [
      10,
      20,
      30,
      40,
      50,
      60
    ],
    "sequence_axes": [
      "member",
      "day"
    ],
    "units": {
      "length": "m",
      "reading": "mm"
    },
    "version": "1.0"
  },
  "schema_sha256": "e4d9da5c0d46e22a70deea3c653c4cfd179800e708f4e3b05af113199a73a811",
  "sequence_shape": [
    6,
    4
  ],
  "undirected_edges": 4
}
```

