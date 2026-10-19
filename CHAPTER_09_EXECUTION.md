# Chapter 9 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** five executed; publication verification pending.

Fresh kernels executed every code cell using the unchanged runner. The reference environment printed CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0, Darwin arm64 CPU. No dependency was added. Inputs/helpers are internal and ordinary runs are offline and CPU-only. Initial runs started concurrently; revised support, symmetry and subgroup notebooks were rerun. Wall times include kernel lifecycle and are observations, not speed comparisons.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_042 | 9.1 | 5 | 2 | 1.357 |
| code_043 | 9.2 | 5 | 2 | 1.288 |
| code_044 | 9.3 | 5 | 2 | 1.261 |
| code_045 | 9.4 | 5 | 2 | 1.490 |
| code_046 | 9.5 | 5 | 2 | 1.445 |

Total: **25 executed code cells and ten inline figures**, seeds 942–946. All current executions pass assertions and contain no error outputs. The support laboratory's initial authoring run rejected an invalid NumPy string-concatenation expression; explicit array concatenation repaired it before its successful rerun. The symmetric nonlinear grid was made exactly symmetric in floating-point representation to retain intended ties, and subgroup cohort/finding denominators were made explicit.

## Actual evidence and boundaries

- Support: 403 raw records, 402 reviewed nonnegative records, three real zeros, 50,000 N converted to 50 kN and a retained 250-kN fixture. One negative-magnitude record remains flagged outside the view. Steel/concrete/timber counts 242/160/0. Logarithm domains and physical reference agreement are checked.
- Associations: pooled age slope .0566373834 mm/year versus material slopes -.0198680179/-.0193897600. Covariance decomposes exactly into -0.620506180 within and 20.242547676 between, total 19.622041497 year·mm. The symmetric square has essentially zero Pearson and exactly zero Spearman correlation despite exact dependence; monotone exponential Spearman is 1.
- Subgroups: fixed cohort counts 600/100/10 have 240/40/6 findings, distinct from conditional miss denominators. Miss counts 18/7/2 give rates .075/.175/.333333. Novel-group Wilson interval [.096771411,.700006685]; even zero of six has upper endpoint .390334288. Duplicating six outcomes into 120 rows narrows a deliberately invalid independent-row interval. No field adequacy follows.
- Dependence: sample ACF at lags 1/12/24 is .884425250/-.405254426/.432929120. Near/far simulated sensor correlations .377777199/.130428413. Physical components have sizes 5/4/3; alternating-node roles cross 9 edges. Under the separate random-intercept generator, mean variance is .041 mm² analytically and .039083316 over 3,000 datasets versus invalid independent-row .005; equivalent count for that mean is 24.390244, not a universal learning effective count.
- Hypothesis check: two training OLS fits use 72 buildings; 24 development buildings select the interaction, development MSE .043488492 versus .046844849 for additive. Twenty-four final buildings give .052811375/.058993378 mm², mean paired gain .006182002. Eleven final buildings lose; the 2,000-resample paired building interval [-.002440349,.015598027] includes zero while the illustrative .005 practical threshold is exceeded. The generator contains the candidate interaction, and no causal interpretation or universal advantage is claimed.

Seven original vector book figures reproduce selected outputs with exact result-dictionary agreement. All ten notebook figures are reviewed before delivery. The concept guide maps every main idea to executable cells or exercises. Only companion sources, outputs and evidence are published; the book and outline remain separate.

## Successful result dictionaries

### code_042

```json
{
  "converted_unit_fixture_kN": 50.0,
  "declared_material_counts": {
    "concrete": 160,
    "steel": 242,
    "timber": 0
  },
  "genuine_zeros": 3,
  "material_quantiles_0_50_90_100_kN": {
    "concrete": [
      0.0,
      67.63649852978091,
      124.08078625483887,
      230.1759787768046
    ],
    "steel": [
      0.0,
      36.0969461328602,
      56.93042390118565,
      250.0
    ]
  },
  "observed_max_kN": 250.0,
  "ordinary_log_excluded_zero_rows": 3,
  "raw_max_as_if_kN": 50000.0,
  "raw_rows": 403,
  "reviewed_rows": 402,
  "unresolved_negative_records": 1
}
```

### code_043

```json
{
  "covariance_decomposition_year_mm": {
    "between": 20.242547676186305,
    "total": 19.62204149667501,
    "within": -0.6205061795112922
  },
  "pooled_age_slope_mm_per_year": 0.05663738342305551,
  "symmetric_nonlinear_correlations": {
    "Pearson": -5.058306117529278e-17,
    "Spearman": 0.0,
    "monotone_exp_Spearman": 1.0
  },
  "within_material_slopes_mm_per_year": {
    "0": -0.019868017919542364,
    "1": -0.01938975998886825
  }
}
```

### code_044

```json
{
  "Wilson_95_intervals": {
    "Novel": [
      0.09677141110578041,
      0.700006684861608
    ],
    "Ordinary": [
      0.04796476535845924,
      0.11542606659186576
    ],
    "Uncommon": [
      0.0874541374603592,
      0.31949990331787714
    ]
  },
  "cohort_counts": {
    "Novel": 10,
    "Ordinary": 600,
    "Uncommon": 100
  },
  "constructed_finding_prevalence": {
    "Novel": 0.6,
    "Ordinary": 0.4,
    "Uncommon": 0.4
  },
  "counts": {
    "Novel": 6,
    "Ordinary": 240,
    "Uncommon": 40
  },
  "coverage_record": {
    "limits": [
      "independent Bernoulli assumptions",
      "simulated labels",
      "no field calibration",
      "no consequences supplied"
    ],
    "observed_unit": "one independent structure with a reference finding",
    "slice_policy": "three prespecified operational groups",
    "unseen_type": "no miss-rate denominator"
  },
  "invalid_row_interval": [
    0.25531740501258443,
    0.4216889837936501
  ],
  "misses": {
    "Novel": 2,
    "Ordinary": 18,
    "Uncommon": 7
  },
  "novel_duplicated_rows": 120,
  "novel_true_independent_count": 6,
  "observed_miss_rates": {
    "Novel": 0.3333333333333333,
    "Ordinary": 0.075,
    "Uncommon": 0.175
  },
  "unseen_category_count": 0,
  "zero_of_six_Wilson_upper": 0.3903342879021653
}
```

### code_045

```json
{
  "component_sizes": [
    5,
    4,
    3
  ],
  "empirical_far_sensor_correlation": 0.1304284128506657,
  "empirical_near_sensor_correlation": 0.3777771987719188,
  "equivalent_independent_count_for_mean": 24.390243902439025,
  "grand_mean_variance_MC_mm2": 0.03908331567263823,
  "grand_mean_variance_theory_mm2": 0.040999999999999995,
  "naive_independent_variance_mm2": 0.005,
  "random_node_split_cross_edges": 9,
  "sample_ACF_lags_1_12_24": {
    "1": 0.8844252495401046,
    "12": -0.40525442558166636,
    "24": 0.43292912042787457
  }
}
```

### code_046

```json
{
  "development_MSE_mm2": {
    "interaction": 0.04348849200219349,
    "linear": 0.04684484915338121
  },
  "final_MSE_mm2": {
    "interaction": 0.052811375210892166,
    "linear": 0.05899337765783036
  },
  "final_buildings_with_negative_gain": 11,
  "hypothesis_ledger": {
    "alternatives": [
      "non-additive response",
      "regime-linked sensor offset",
      "building mix",
      "chance"
    ],
    "eligible_predictors": [
      "linear",
      "interaction"
    ],
    "final_policy": "one paired assessment; no winner-based redesign",
    "fit_cases": "72 training buildings",
    "limits": [
      "synthetic interaction favors candidate",
      "development was used to propose and select",
      "no causal coefficient claim"
    ],
    "observed_on": "24 development buildings only",
    "pattern": "linear residual varies with temperature-load product",
    "practical_final_gain_mm2": 0.005,
    "selection_metric": "equal-building development MSE mm\u00b2"
  },
  "illustrative_practical_threshold_met": true,
  "paired_2000_bootstrap_percentile_95_mm2": [
    -0.0024403494763971735,
    0.015598026539101343
  ],
  "paired_mean_gain_mm2": 0.006182002446938191,
  "role_building_counts": {
    "development": 24,
    "final": 24,
    "train": 72
  },
  "selected_procedure": "interaction"
}
```

