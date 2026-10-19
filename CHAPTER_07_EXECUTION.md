# Chapter 7 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** all five executed and published; content tree verified.

Every current notebook ran all cells in order in a fresh kernel using the unchanged runner. Initial jobs ran concurrently and repaired notebooks were rerun individually; wall times include kernel lifecycle and are observations, not comparative performance guarantees. No dependency was added. All kernels printed CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0, Darwin arm64 CPU. Every import, helper and generated input is inside its notebook. Ordinary execution needs no files, downloads, API keys or GPU.

| Example | Section | Code cells | Inline figures | Wall seconds incl. kernel |
| --- | --- | ---: | ---: | ---: |
| [code_032](CODE_EXAMPLES.md#code_032) | 7.1 | 5 | 2 | 2.793 |
| [code_033](CODE_EXAMPLES.md#code_033) | 7.2 | 6 | 2 | 1.381 |
| [code_034](CODE_EXAMPLES.md#code_034) | 7.3 | 6 | 2 | 1.712 |
| [code_035](CODE_EXAMPLES.md#code_035) | 7.4 | 6 | 2 | 2.755 |
| [code_036](CODE_EXAMPLES.md#code_036) | 7.5 | 6 | 2 | 2.735 |

Total: **29 executed code cells and ten inline figures**, seeds 732–736. Current reference runs pass every assertion and contain no error outputs. The forecast's first authoring execution stopped on a literal-newline serialization error, which was corrected before the successful fresh-kernel reference run. This authoring repair is separate from the deliberately rejected optimization check in code_035. The final execution summaries retain actual outputs and timings.

## Actual results and checks

- **code_032:** the unit-checked simply supported central-load reference gives 2.8125 mm at 10 kN, 3 m, E=200 GPa,I=1e-5 m⁴. Five predeclared rules use 300/100/100 independent beams; each learned family has three development alpha candidates. Final MAE constant/heuristic/nominal-beam/raw-linear/residual is 2.889433081/2.609262725/.261785683/.936912649/.037383546 mm. Paired nominal-minus-residual absolute-error gain is .224402137 mm, exceeding a predeclared illustrative .03 mm threshold. The constructed correction favors the residual representation; no field benefit, universal family ranking or statistical-significance claim follows.
- **code_033:** building-disjoint training/development/final prediction cutoffs occur in 2024/2025/2026, with source labels available before the next period. A 720-row raw join is repaired to 240 unique cases by filtering event and arrival times and enforcing cardinality. An invalid reading split shares all 30 buildings. Changing one development label by 8 mm changes its eight-reading target aggregate by 1 mm. All-row scaler statistics differ from training-only statistics. Repaired versus unavailable-post-inspection development MSE is .0326479493 versus .00002609995 mm². Only the repaired model receives final assessment: MAE .153410527 mm on six independent new buildings.
- **code_034:** the full canonical sensor snapshot is retained in base64 in the executed summary, alongside schema and SHA-256. A one-value mutation is rejected. The critical executed training function has its own narrower hash; full notebook revision is recorded by publication. Identical snapshot/seed/environment replay yields exactly equal predictions. Five predeclared development seeds have MAE .131749415–.139609385; no best seed is selected. Original final rolling-one-step MAE .142216466 is worse than persistence .129592663. An independently generated series has a different snapshot hash and final MAE .142247763 under the same procedure; this is within-simulator replication, not field replication or fixed-origin multi-step forecasting.
- **code_035:** actual one-hop shared-weight graph computation and a matched relational table receive the same own/neighbor features, topology, 48/16/16 graph split, 49 coefficients, five initializations and two checkpoint candidates. All choose 250 updates. Graph/relational predictions agree to 4.44e-16 mm, with mean final MAE .156554467 mm for both. Own-only and misaligned summaries yield .510260096/.519553360 mm. These ablations change information and effective capacity; allocated parameter count alone does not make them identical families. A separately declared oversized rate is rejected after two steps at half MSE 4.943365e15 mm², before uncontrolled overflow. It is not a hidden eligible tuning candidate.
- **code_036:** two mechanisms have the same exact recorded P(A,Y), risks .25/.10 for unmaintained/maintained units, but average intervention effects 0/-.15. In mechanism 1 preparedness confounds assignment and outcome. An actual logistic predictor, using A only after its recording time, has final log loss .436218728 versus .461888728 for a frequency baseline; coefficient -1.000246722 explains fitted log odds, not intervention. A fresh randomized simulator sample has risk difference -.005832708 while paired author-known potential outcomes have exact effect zero. Additional observed variables could distinguish the mechanisms; equality is claimed only for recorded A,Y.

## Boundaries and provenance

Training-only transformations, development-only candidate/checkpoint selection, disjoint buildings/graphs, chronological information availability and fixed-rule final assessment are explicit. Repaired features are rebuilt before refitting. The invalid future-field model is a diagnostic counterexample, not a final candidate. Seed repetitions, changed datasets and actual source revisions have separate roles. Snapshot hashes establish byte identity, not measurement quality or provenance legitimacy. Recoverable reference bytes are supplied so the data record is more than a seed.

The graph/table equality is specific to a single mean-aggregation stage with corresponding weights; richer nonlinear message-passing methods are not declared equivalent. Ablations and initializations describe the given data and budgets rather than all population uncertainty. Runtime or general architecture superiority is not claimed. Predictive accuracy, fitted-rule explanation and causal identification remain distinct; the observational table alone cannot choose between the two constructed intervention stories.

All ten notebook figures are visually reviewed with reference units, labels, captions/text explanations and grayscale markers/styles. Five experiment plots rerun into vector book figures and match exact successful result dictionaries; two original diagrams explain leakage paths and matched comparisons. Schemas, sequential execution, no errors, meaningful assertions, source self-containment, local links/anchors and summary/manifest agreement pass scripts/check_chapter07.py. Snapshot decoding/hash and critical-program source agreement are independently checked there. All 31 prior notebooks and manifest records remain unchanged. Only companion artifacts are published, not the manuscript or outline.

## Actual successful result records

The following dictionaries come from fresh-kernel summaries. The long base64 payload is kept once in code_034's committed notebook output; its digest and configuration remain here.

### code_032

```json
{
  "development_MAE_candidates_mm": {
    "linear": [
      0.9568633457648077,
      0.95558599207781,
      1.0079489169488536
    ],
    "residual": [
      0.03354492303052639,
      0.033672512101506714,
      0.05559861666594625
    ]
  },
  "final_MAE_mm": {
    "beam_solver": 0.26178568281530823,
    "constant": 2.8894330809500484,
    "heuristic": 2.609262725028362,
    "linear": 0.9369126491670905,
    "residual": 0.037383545612102435
  },
  "final_RMSE_mm": {
    "beam_solver": 0.3586632715473802,
    "constant": 3.8070198065680114,
    "heuristic": 3.613950032550831,
    "linear": 1.3499587770884562,
    "residual": 0.04415430340598707
  },
  "linear_selected_alpha": 1.0,
  "paired_mean_MAE_gain_mm": 0.2244021372032058,
  "practical_MAE_gain_threshold_mm": 0.03,
  "practical_threshold_met": true,
  "reference_check_mm": 2.8124999999999996,
  "residual_selected_alpha": 0.01
}
```

### code_033

```json
{
  "aggregate_assessment_label_sensitivity": 1.0,
  "development_MSE_mm2": {
    "invalid_post_inspection": 2.6099953501522833e-05,
    "repaired": 0.03264794932026516
  },
  "final_independent_buildings": 6,
  "invalid_split_overlapping_buildings": 30,
  "raw_join_rows": 720,
  "repaired_final_MAE_mm": 0.1534105273827817,
  "repaired_rows": 240
}
```

### code_034

```json
{
  "configuration": {
    "bootstrap": true,
    "criterion": "squared_error",
    "critical_program_sha256": "2127bb623ba7952ce678e778faa93a6d2e1a10d6f15dfc894ccbe50eaee87c5a",
    "data_sha256": "11117b9985b5ee0efc7ed779a1e7c489e0f8c89fea2b57a1b0579aad372fc7dc",
    "development_windows": 60,
    "final_windows": 97,
    "hardware": "Darwin arm64 CPU",
    "horizon": "rolling one step",
    "max_depth": 4,
    "min_samples_leaf": 3,
    "n_estimators": 40,
    "n_jobs": 1,
    "scaling": "none; tree split model",
    "seed": 734,
    "train_windows": 200,
    "versions": {
      "matplotlib": "3.11.0",
      "numpy": "2.4.4",
      "pandas": "3.0.3",
      "python": "3.14.3",
      "scikit-learn": "1.9.0",
      "scipy": "1.17.1"
    }
  },
  "configuration_sha256": "ddcd580016f82388094f0a05fcebe3eb5a354c66ecfb9a7d67c76084f2108bcf",
  "critical_program_sha256": "2127bb623ba7952ce678e778faa93a6d2e1a10d6f15dfc894ccbe50eaee87c5a",
  "development_MAE_by_seed": {
    "0": 0.1383117729928186,
    "1": 0.13174941492443648,
    "2": 0.13849124212273525,
    "3": 0.1371252718157868,
    "4": 0.13960938476377857
  },
  "exact_replay": true,
  "final_MAE": 0.14221646626499926,
  "independent_series_final_MAE": 0.14224776339879633,
  "mutated_snapshot_rejected": true,
  "persistence_final_MAE": 0.1295926626155025,
  "replication_snapshot_sha256": "0e6cd3ea99054d79a3412b5a89a3d9f1164af09abcb2d3e38514e368c14f7f5f",
  "snapshot_sha256": "11117b9985b5ee0efc7ed779a1e7c489e0f8c89fea2b57a1b0579aad372fc7dc"
}
```

### code_035

```json
{
  "development_MAE_by_seed_checkpoint_mm": {
    "graph": [
      [
        0.6352449772113465,
        0.16694191801890126
      ],
      [
        0.6548641168821047,
        0.16763463086615146
      ],
      [
        0.5774028278159155,
        0.16835341166820106
      ],
      [
        0.6634227794932757,
        0.17320064812093283
      ],
      [
        0.4838465963337252,
        0.17054983202913962
      ]
    ],
    "misaligned": [
      [
        0.7048997311464436,
        0.5501434077213315
      ],
      [
        0.7449697575841023,
        0.5473418930224733
      ],
      [
        0.6714061749477499,
        0.5537906991702594
      ],
      [
        0.7437771252286101,
        0.5526960257412132
      ],
      [
        0.6742107018284826,
        0.5523989154382886
      ]
    ],
    "own_only": [
      [
        0.6706391876435512,
        0.578204944210567
      ],
      [
        0.7511559298587935,
        0.5798157701501261
      ],
      [
        0.6484238010292248,
        0.578944092551771
      ],
      [
        0.7498472365016373,
        0.5787965030143546
      ],
      [
        0.6898250866523753,
        0.5815102235368352
      ]
    ],
    "relational": [
      [
        0.6352449772113465,
        0.16694191801890124
      ],
      [
        0.6548641168821048,
        0.16763463086615146
      ],
      [
        0.5774028278159155,
        0.16835341166820106
      ],
      [
        0.6634227794932757,
        0.17320064812093283
      ],
      [
        0.4838465963337251,
        0.17054983202913962
      ]
    ]
  },
  "final_MAE_by_seed_mm": {
    "graph": [
      0.15462919927495045,
      0.1559594552111912,
      0.1568148677080694,
      0.15713191499713258,
      0.1582368981780093
    ],
    "misaligned": [
      0.5199229103543056,
      0.5186175604139622,
      0.5198824894097364,
      0.5190525867645661,
      0.520291251090593
    ],
    "own_only": [
      0.5108810879956996,
      0.510461013460953,
      0.5104007170102474,
      0.510508800736611,
      0.5090488588633838
    ],
    "relational": [
      0.15462919927495045,
      0.1559594552111912,
      0.1568148677080694,
      0.1571319149971326,
      0.1582368981780093
    ]
  },
  "maximum_graph_relational_prediction_difference_mm": 4.440892098500626e-16,
  "selected_steps": {
    "graph": 250,
    "misaligned": 250,
    "own_only": 250,
    "relational": 250
  },
  "trial_ledger": {
    "eligible_checkpoints": [
      50,
      250
    ],
    "eligible_families": 4,
    "failure_steps": 2,
    "failure_stop_half_MSE_mm2": 4943365127522707.0,
    "hidden_width": 8,
    "initializations_per_family": 5,
    "maximum_updates_per_fit": 250,
    "parameters_each": 49,
    "rejected_rate": 10000
  }
}
```

### code_036

```json
{
  "baseline_final_log_loss": 0.46188872812844345,
  "final_log_loss": 0.43621872780899923,
  "fitted_probability_A0_A1": [
    0.2686206217239512,
    0.11900578269320293
  ],
  "intervention_risk_model1": [
    0.175,
    0.175
  ],
  "intervention_risk_model2": [
    0.25,
    0.1
  ],
  "logistic_coefficient": -1.0002467216758537,
  "mechanism1_true_average_effect": 0.0,
  "observational_risk_difference": -0.15000000000000008,
  "observed_failure_risk_A0_A1": [
    0.25000000000000006,
    0.09999999999999999
  ],
  "observed_joint_A_Y": [
    [
      0.37499999999999994,
      0.125
    ],
    [
      0.45,
      0.049999999999999996
    ]
  ],
  "randomized_simulator_risk_difference": -0.005832708047822266
}
```

## Publication verification

Content commit [65643ec5279801dbc15a174a340d835deea63af4](https://github.com/ImeshEkanayake/MLBook-/commit/65643ec5279801dbc15a174a340d835deea63af4) was pushed to main. The GitHub API tree contains 65 file blobs, all matching the local commit tree; remote main resolves to this content revision. The following metadata commit marks only code_032–036 as published after that verification. Final tree and raw-file checks are retained in the local publication evidence.
