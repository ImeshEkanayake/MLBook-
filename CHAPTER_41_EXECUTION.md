# Chapter 41 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** published and executed; content-tree verification passed.

All current sources ran in fresh kernels using the unchanged runner. Imports/helpers and generated observations are internal. code_218 additionally requires the explicitly acquired cached checkpoint in the [asset guide](CHAPTER_41_ASSETS.md); ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency or new asset was added; code_218 explicitly reuses the pinned Chapter35 checkpoint. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_216 | 41.1 | 4 | 2 | 1.689 |
| code_217 | 41.2 | 4 | 2 | 1.607 |
| code_218 | 41.3 | 4 | 2 | 3.268 |
| code_219 | 41.4 | 4 | 2 | 2.845 |
| code_220 | 41.5 | 4 | 2 | 1.587 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 41 mechanisms, controls and interpretation

Five original laboratories implement all five scopes and both visual briefs:20 code cells and10 inline figures. Four generate every input internally and need no ordinary-run files. **218 reuses an explicitly acquired, pinned Chapter35 TabPFN v2 classifier checkpoint**; it verifies29,009,539 bytes/SHA before native loading, fails if unavailable, then runs offline on CPU. No new asset or dependency is added and no credentials/GPU are required. The separate asset guide/manifest preserves acquisition, revision and licence instructions; weights remain ignored. Main runtime remains Python3.14.3, NumPy2.4.4, SciPy1.17.1, pandas3.0.3, Matplotlib3.11.0, scikit-learn1.9.0;218 uses TabPFN9.2.0/Torch2.14.1 with explicit float32 inference;219 uses deterministic Torch float64/one CPU thread. Access/execution22 October2026 Australia/Melbourne; literature cutoff18 October2026.

- **216 / complete package:**800 source structures, source-median imputation/standard scaling/fixed three-material encoding/logistic fit;200 independent final structures. Canonical600-byte JSON contains fitted state/schema/event/unit/format/environment. Actual fresh stdlib subprocess reconstructs from stdin with no parent helpers; maximum probability discrepancy1.1102230246251565e-16; final Brier0.225491. Fresh subprocess fixtures reject unknown material, wrong unit, extra control field and unsupported format. Missing numeric fields represented as explicit null use source medians. SHA checks consistency against a trusted expected digest, not publisher authentication. Visual A train/package/serve includes separate solver responsibility. Initial builder indentation error was repaired before216's first execution; no failed output was published.
- **217 / serving patterns:**1,000 source response records;200 final features. Actual batch/individual/coefficient-only edge predictions are exactly equal in this run. Two asset-keyed causal streams accept40 packets, reject one duplicate/one stale timestamp, and pass independent recurrence checks without future initialization.40 source spatial graphs×20 nodes, fixed radius1.5/no self-loops/neighbour aggregation; new30-node graph RMSE0.0538565. Eight nearest source records retrieved for20 queries form an actual weighted baseline, explicitly not a pretrained foundation model. Positive three-node stiffness solve returns displacements1/2/3 reference units and verifies equilibrium; singular fixture returns solver_failed_defer. No live service or edge hardware deployment.
- **218 / actual foundation resource profile:** Existing public TabPFN v2 classifier repository Prior-Labs/TabPFN-v2-clf, revisionf851f2a3c941544733b712d8c0f96dfae9b28862, classifier-v2_default checkpoint; SHA cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49. Generated source384/final64, balanced source contexts16/64 chosen without final labels. Actual TabPFN final Brier0.251376/0.242745; booster30 rounds/seven leaves fits384, Brier0.224736. Different fitting budgets/upstream pretraining prevent fair benchmark or method superiority claims. Initial218 assertion incorrectly hashed parameters before first inference numerical preparation; installed inference source and prior successful185 show explicit dtype/device initialization. Repaired by timing the first eight-query call, then hashing before/after subsequent64-query inference; unchanged initialized weights, no gradient updates. Fresh kernel rerun passes. Warm batch1/8/32 timings repeated three times for each context; booster five repeats. Actual four local requests decode eight queries, retrieve32 source neighbours around query mean, refit context, predict and serialize; final labels are never retrieved. Context fitting remains inside measured request work. Four-thread/eight-request booster-only workload matches serial predictions; mutable TabPFN thread safety is not claimed. Numeric native parameters28,978,216 bytes/source arrays15,360; checkpoint bytes and tracemalloc Python peak are distinct scopes, not total resident memory. Hypothetical0.5 currency units/CPU-hour is an assumed elapsed-compute scenario excluding idle/redundancy/storage/network/staffing, not a current price. Kernel and independent export resource observations are retained separately; timings are not deterministic RESULTS.
- **219 / actual compression/distillation:**1,200 generated source observations; own4–32–16–1 tanh teacher350 Adam steps. Separate dense60%-matrix-magnitude pruning, symmetric int8 matrix storage+float64 scales/bias with floating dequantized arithmetic, actual middle16×32 rank4 SVD factors and4–8–1 student400 steps on half observed BCE/half teacher soft-probability BCE. All fixed before600 independent final labels. Final Brier teacher0.281905/pruned0.499188/int8-storage0.281617/rank4 0.298219/student0.198375. Predeclared high-load x0>1.5 has41 records; rare Brier0.163826/0.865905/0.164639/0.142737/0.090121. Ten fixed-bin ECE0.245511/0.481770/0.242594/0.269392/0.031354. Load+0.1 negative finite differences209/385/213/181/0 expose teacher and transformed-model monotonicity failures; probability bounds pass but are not physical validity evidence. Stored numeric bytes5,640/5,640/1,072/3,080/392 exclude native/runtime/temporary allocations. Thirty actual warm256-row forward repetitions with median/p95 timings; implementation-specific NumPy/Torch overheads prevent a kernel/hardware theorem. Int8 is NOT integer-kernel inference; dense zeros are NOT sparse execution. Teacher quality failure and pruning damage retained without final-set tuning. Student agreement is not its quality target. Visual B actual local latency/storage/Brier+rare-slice comparison.
- **220 / local release rehearsal:** Old/candidate fit separate600-row generated regimes; independent300 updated-development gate requires at least0.005 Brier improvement,overall<0.25/bothgroups<0.30. Dev old0.231848/new0.186970,gate passes.500 final shadow outcomes old0.233160/new0.185924,groupBrier0.181920/0.189960,decision disagreement0.31. Gate uses no final outcomes. Stable-hash10%/25% staged fixtures route52/128 candidate requests, not real traffic/actual human approval/causal benefit estimation. Exact finite three-field unit schema; wrong unit/missing measurement invalid/no probability, valid-request timeout compatible old fallback, solver failure deferred/no probability. Operationally injected rollback routes500 to old-v1; retained coefficient/intercept reconstruction byte-identical to prior predictions/SHA. This validates declared local paths, not live system recovery or structural clearance.

All current fresh kernels pass assertions without errors/stderr. Independent vector-export runs reexecute every code cell and verify exact scientific RESULTS; resource observations are separately saved in manuscript tmp and reproduced in the companion report as distinct runs.10 original SVG/vector-PDF/PNG sets and10 embedded inline figures are inspected during delivery. Primary PDFs inspected for Sculley et al.2015 system debt, Hinton/Vinyals/Dean2015 distillation and Han/Mao/Dally2016 compression. The experiments do not reproduce full Deep Compression, sparse/integer hardware, production network serving, actual release approvals or field structural validity. Chapters42–43 and the whole-book editorial/technical audit remain required.

## Successful result dictionaries

### code_216

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8016.

```json
{
  "child_uses_parent_helpers": false,
  "final_Brier": 0.2254908834071111,
  "final_structures": 200,
  "fresh_process_max_probability_difference": 1.1102230246251565e-16,
  "incompatible_request_fixtures": [
    {
      "fixture": "unknown category",
      "rejected": true
    },
    {
      "fixture": "wrong unit",
      "rejected": true
    },
    {
      "fixture": "unexpected field",
      "rejected": true
    },
    {
      "fixture": "unsupported format",
      "rejected": true
    }
  ],
  "missing_numeric_policy": "source median imputation",
  "package_bytes": 600,
  "package_format_version": 1,
  "package_sha256": "a4bda227be935beb593fd5a449cc50c366cd09974c7c144dd495a46d1d910910",
  "schema_validity_is_not_structural_clearance": true,
  "source_structures": 800,
  "unknown_category_policy": "reject"
}
```

### code_217

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8017.

```json
{
  "batch_edge_max_difference": 0.0,
  "batch_online_max_difference": 0.0,
  "context_baseline_is_not_pretrained_foundation_model": true,
  "final_graph_RMSE": 0.05385648665841734,
  "final_graph_nodes": 30,
  "final_stateless_records": 200,
  "graph_radius": 1.5,
  "retrieval_context_records": 8,
  "retrieval_queries": 20,
  "retrieved_prediction_first_five": [
    -0.26937754557375776,
    -0.8373817324391728,
    -0.6875202045707544,
    -0.23185946447860936,
    -1.1277146202306843
  ],
  "singular_solver_status": "solver_failed_defer",
  "solver_displacement": [
    0.9999999999999998,
    1.9999999999999996,
    2.9999999999999996
  ],
  "source_graphs": 40,
  "source_nodes_per_graph": 20,
  "source_records": 1000,
  "stream_accepted_packets": 40,
  "stream_assets": 2,
  "stream_duplicate_or_stale_rejections": 2,
  "stream_uses_future_packets": false
}
```

### code_218

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "tabpfn": "9.2.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 8018.

```json
{
  "actual_retrieval_requests": 4,
  "booster_Brier": 0.2247357106872554,
  "booster_training_rows": 384,
  "checkpoint_bytes": 29009539,
  "concurrent_booster_predictions_match_serial": true,
  "context_sizes_chosen_without_final_labels": true,
  "final_rows": 64,
  "foundation_checkpoint": "TabPFN-v2 classifier f851f2a",
  "foundation_context_profiles": [
    {
      "Brier": 0.251376348898313,
      "context_rows": 16,
      "frozen_weights": true,
      "prediction_sha256": "74fdb91ac503a341bde0fb67f28aa466d3d04d52dcd16cc62f5cd2387d3d5d49"
    },
    {
      "Brier": 0.24274497166030395,
      "context_rows": 64,
      "frozen_weights": true,
      "prediction_sha256": "42c1bd132324ec4f91a068846443796b47008c233da54862523df180ca2d871b"
    }
  ],
  "inference_precision": "torch.float32",
  "native_parameter_bytes": 28978216,
  "request_probability_sha256": "5a21ae1b954ca201fec6368721c933a8e30199ca6578d0ba1d8d4d8336ada722",
  "request_rows": 8,
  "retrieval_uses_final_labels": false,
  "retrieved_context_rows": 32,
  "source_pool_array_bytes": 15360,
  "source_rows": 384
}
```

### code_219

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 8019.

```json
{
  "independent_final_rows": 600,
  "int8_is_storage_not_integer_kernel": true,
  "lowrank_middle_rank": 4,
  "prediction_sha256": {
    "Dense pruned": "1edd60903395e4186f0e051ec8bba77d627eebfdbcbb2ad1dfa0a67f9054dc77",
    "Int8 storage": "565231f6caf5f153937f123304510712f01da3bf1e1ab2c756c2f444193516ba",
    "Rank4": "4bd162e05e9e1bfb86bdb12934717a50590e74c271ed6e7d2ec05fff51eb5fbd",
    "Student": "3ef25adf551af851b2d33151b885bfaa3abdc8d6796049d927e2be5500935e3a",
    "Teacher": "52bcd96d8902f3a5710e96e80e5d8bb8cd4fcb9dd89dacbc2af1c1fce99468fe"
  },
  "pruned_arrays_remain_dense": true,
  "pruning_fraction": 0.6,
  "quality_does_not_select_release": true,
  "quality_profiles": [
    {
      "Brier": 0.2819045730629236,
      "ECE_ten_fixed_bins": 0.24551117164686342,
      "load_monotonicity_violations": 209,
      "log_loss": 1.1038350208809318,
      "model": "Teacher",
      "rare_Brier": 0.16382626775951048,
      "stored_numeric_parameter_bytes": 5640,
      "teacher_decision_disagreement": 0.0
    },
    {
      "Brier": 0.4991881359233666,
      "ECE_ten_fixed_bins": 0.4817696628878675,
      "load_monotonicity_violations": 385,
      "log_loss": 3.294199088429863,
      "model": "Dense pruned",
      "rare_Brier": 0.8659050385680952,
      "stored_numeric_parameter_bytes": 5640,
      "teacher_decision_disagreement": 0.565
    },
    {
      "Brier": 0.28161670534593203,
      "ECE_ten_fixed_bins": 0.24259441043386631,
      "load_monotonicity_violations": 213,
      "log_loss": 1.1025786086722895,
      "model": "Int8 storage",
      "rare_Brier": 0.16463878527658599,
      "stored_numeric_parameter_bytes": 1072,
      "teacher_decision_disagreement": 0.0033333333333333335
    },
    {
      "Brier": 0.2982188536123314,
      "ECE_ten_fixed_bins": 0.2693919497480024,
      "load_monotonicity_violations": 181,
      "log_loss": 1.5667591085716654,
      "model": "Rank4",
      "rare_Brier": 0.1427367573579545,
      "stored_numeric_parameter_bytes": 3080,
      "teacher_decision_disagreement": 0.32666666666666666
    },
    {
      "Brier": 0.1983750818730218,
      "ECE_ten_fixed_bins": 0.03135433593667342,
      "load_monotonicity_violations": 0,
      "log_loss": 0.5839485807049816,
      "model": "Student",
      "rare_Brier": 0.09012099172681645,
      "stored_numeric_parameter_bytes": 392,
      "teacher_decision_disagreement": 0.25
    }
  ],
  "rare_high_load_rows": 41,
  "source_rows": 1200,
  "student_objective": "half observed BCE plus half teacher soft-probability BCE",
  "student_steps": 400,
  "teacher_steps": 350
}
```

### code_220

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 8020.

```json
{
  "canary_candidate_requests": 52,
  "candidate_source_rows": 600,
  "development_candidate_Brier": 0.18697037926928034,
  "development_candidate_group_Brier": [
    0.18442978072763724,
    0.18968619150345054
  ],
  "development_gate_passed": true,
  "development_old_Brier": 0.23184783286356578,
  "development_rows": 300,
  "failure_fixture_statuses": [
    "valid",
    "invalid",
    "invalid",
    "valid_fallback",
    "deferred"
  ],
  "final_candidate_Brier": 0.18592402789735085,
  "final_candidate_group_Brier": [
    0.18192024107218321,
    0.18995997365284106
  ],
  "final_old_Brier": 0.23316046182963845,
  "final_shadow_rows": 500,
  "gate_uses_final_labels": false,
  "invalid_inputs_never_receive_fallback_probability": true,
  "live_service_or_human_approval_executed": false,
  "old_source_rows": 600,
  "rollback_old_requests": 500,
  "rollback_prior_probability_bytes_identical": true,
  "rollback_probability_sha256": "fbfb0481a0fe898c5ece133696ec963d5ba266c90f830a1713e5366e2e6aa14e",
  "shadow_decision_disagreement": 0.31,
  "staged_candidate_requests": 128
}
```


## Independent resource observations

Durations and Python peaks vary between runs and are intentionally outside deterministic RESULTS. Notebook outputs retain the fresh-kernel run; book figures use a separately executed export run. Both are actual computations. Numeric-buffer accounting is kept separate from Python allocation peak and total resident memory.

### code_218 fresh kernel

```json
{
  "assumed_cpu_hour_rate": 0.5,
  "booster_concurrent_requests": 8,
  "booster_concurrent_rows_per_second": 59365.760244747406,
  "booster_concurrent_seconds": 0.00215612500323914,
  "booster_concurrent_workers": 4,
  "context_profiles": [
    {
      "construct_and_fit_seconds": 0.020879624993540347,
      "context_rows": 16,
      "initial_8_query_seconds": 0.024058333016000688,
      "post_initialization_64_query_seconds": 0.021433625021018088
    },
    {
      "construct_and_fit_seconds": 0.009600292018149048,
      "context_rows": 64,
      "initial_8_query_seconds": 0.023521625000284985,
      "post_initialization_64_query_seconds": 0.0345417499775067
    }
  ],
  "mean_foundation_request_compute_cost": 4.268216180207674e-06,
  "native_parameter_bytes": 28978216,
  "python_tracemalloc_prediction_peak_bytes": 47117,
  "retrieval_requests": [
    {
      "context_fit_seconds": 0.03706783300731331,
      "decode_seconds": 1.8749997252598405e-05,
      "end_to_end_seconds": 0.05261279200203717,
      "model_seconds": 0.015147332975175232,
      "request": 0,
      "retrieval_seconds": 0.0003639170026872307,
      "serialization_seconds": 1.4959019608795643e-05
    },
    {
      "context_fit_seconds": 0.008234333014115691,
      "decode_seconds": 9.499985026195645e-06,
      "end_to_end_seconds": 0.023791874991729856,
      "model_seconds": 0.015219082997646183,
      "request": 1,
      "retrieval_seconds": 0.00031466700602322817,
      "serialization_seconds": 1.4291988918557763e-05
    },
    {
      "context_fit_seconds": 0.008056041988311335,
      "decode_seconds": 9.791983757168055e-06,
      "end_to_end_seconds": 0.023345916997641325,
      "model_seconds": 0.014966167014790699,
      "request": 2,
      "retrieval_seconds": 0.000300833024084568,
      "serialization_seconds": 1.3082986697554588e-05
    },
    {
      "context_fit_seconds": 0.008261166978627443,
      "decode_seconds": 1.0916992323473096e-05,
      "end_to_end_seconds": 0.023174041998572648,
      "model_seconds": 0.014549833023920655,
      "request": 3,
      "retrieval_seconds": 0.00034116601455025375,
      "serialization_seconds": 1.0958989150822163e-05
    }
  ],
  "source_pool_array_bytes": 15360,
  "warm_batches": [
    {
      "batch_rows": 1,
      "context_rows": 16,
      "median_seconds": 0.008443083002930507,
      "model": "TabPFN",
      "rows_per_second": 118.44014794748675
    },
    {
      "batch_rows": 8,
      "context_rows": 16,
      "median_seconds": 0.010090958996443078,
      "model": "TabPFN",
      "rows_per_second": 792.7888719813338
    },
    {
      "batch_rows": 32,
      "context_rows": 16,
      "median_seconds": 0.014845833997242153,
      "model": "TabPFN",
      "rows_per_second": 2155.4868528062825
    },
    {
      "batch_rows": 1,
      "context_rows": 64,
      "median_seconds": 0.019668875000206754,
      "model": "TabPFN",
      "rows_per_second": 50.84174870141217
    },
    {
      "batch_rows": 8,
      "context_rows": 64,
      "median_seconds": 0.021374333009589463,
      "model": "TabPFN",
      "rows_per_second": 374.2806849884321
    },
    {
      "batch_rows": 32,
      "context_rows": 64,
      "median_seconds": 0.02610429099877365,
      "model": "TabPFN",
      "rows_per_second": 1225.852102303921
    },
    {
      "batch_rows": 1,
      "context_rows": 384,
      "median_seconds": 8.579101995564997e-05,
      "model": "Histogram booster",
      "rows_per_second": 11656.231625605502
    },
    {
      "batch_rows": 8,
      "context_rows": 384,
      "median_seconds": 8.399999933317304e-05,
      "model": "Histogram booster",
      "rows_per_second": 95238.09599413488
    },
    {
      "batch_rows": 32,
      "context_rows": 384,
      "median_seconds": 8.64169851411134e-05,
      "model": "Histogram booster",
      "rows_per_second": 370297.5745768734
    }
  ]
}
```

### code_218 independent vector-export run

```json
{
  "context_profiles": [
    {
      "context_rows": 16,
      "construct_and_fit_seconds": 0.021563291986240074,
      "initial_8_query_seconds": 0.02569883401156403,
      "post_initialization_64_query_seconds": 0.022137666994240135
    },
    {
      "context_rows": 64,
      "construct_and_fit_seconds": 0.009345291007775813,
      "initial_8_query_seconds": 0.022707583993906155,
      "post_initialization_64_query_seconds": 0.03382949999650009
    }
  ],
  "warm_batches": [
    {
      "model": "TabPFN",
      "context_rows": 16,
      "batch_rows": 1,
      "median_seconds": 0.00828112501767464,
      "rows_per_second": 120.75653946362019
    },
    {
      "model": "TabPFN",
      "context_rows": 16,
      "batch_rows": 8,
      "median_seconds": 0.009942625008989125,
      "rows_per_second": 804.6164863672523
    },
    {
      "model": "TabPFN",
      "context_rows": 16,
      "batch_rows": 32,
      "median_seconds": 0.014671375014586374,
      "rows_per_second": 2181.1179912029647
    },
    {
      "model": "TabPFN",
      "context_rows": 64,
      "batch_rows": 1,
      "median_seconds": 0.019475250010145828,
      "rows_per_second": 51.34722273033927
    },
    {
      "model": "TabPFN",
      "context_rows": 64,
      "batch_rows": 8,
      "median_seconds": 0.02128662500763312,
      "rows_per_second": 375.82284637096296
    },
    {
      "model": "TabPFN",
      "context_rows": 64,
      "batch_rows": 32,
      "median_seconds": 0.026231124997138977,
      "rows_per_second": 1219.9248032057426
    },
    {
      "model": "Histogram booster",
      "context_rows": 384,
      "batch_rows": 1,
      "median_seconds": 8.81669984664768e-05,
      "rows_per_second": 11342.112325398306
    },
    {
      "model": "Histogram booster",
      "context_rows": 384,
      "batch_rows": 8,
      "median_seconds": 9.041701559908688e-05,
      "rows_per_second": 88478.92121846136
    },
    {
      "model": "Histogram booster",
      "context_rows": 384,
      "batch_rows": 32,
      "median_seconds": 8.625001646578312e-05,
      "rows_per_second": 371014.4219241391
    }
  ],
  "retrieval_requests": [
    {
      "request": 0,
      "decode_seconds": 1.7624988686293364e-05,
      "retrieval_seconds": 0.0002536670072004199,
      "context_fit_seconds": 0.010068916977616027,
      "model_seconds": 0.0145984580158256,
      "serialization_seconds": 1.3417011359706521e-05,
      "end_to_end_seconds": 0.024952084000688046
    },
    {
      "request": 1,
      "decode_seconds": 8.750008419156075e-06,
      "retrieval_seconds": 0.0002741249918472022,
      "context_fit_seconds": 0.00787287502316758,
      "model_seconds": 0.01436029199976474,
      "serialization_seconds": 1.0666990419849753e-05,
      "end_to_end_seconds": 0.02252670901361853
    },
    {
      "request": 2,
      "decode_seconds": 8.916016668081284e-06,
      "retrieval_seconds": 0.00022020898177288473,
      "context_fit_seconds": 0.007742250018054619,
      "model_seconds": 0.014302790979854763,
      "serialization_seconds": 1.0584015399217606e-05,
      "end_to_end_seconds": 0.022284750011749566
    },
    {
      "request": 3,
      "decode_seconds": 8.875009370967746e-06,
      "retrieval_seconds": 0.0002312079886905849,
      "context_fit_seconds": 0.007570667017716914,
      "model_seconds": 0.01406124999630265,
      "serialization_seconds": 9.082985343411565e-06,
      "end_to_end_seconds": 0.021881082997424528
    }
  ],
  "python_tracemalloc_prediction_peak_bytes": 42837,
  "native_parameter_bytes": 28978216,
  "source_pool_array_bytes": 15360,
  "booster_concurrent_requests": 8,
  "booster_concurrent_workers": 4,
  "booster_concurrent_seconds": 0.0021197079913690686,
  "booster_concurrent_rows_per_second": 60385.67600876377,
  "assumed_cpu_hour_rate": 0.5,
  "mean_foundation_request_compute_cost": 3.1821050702597456e-06
}
```

### code_219 fresh kernel

```json
{
  "forward_latency": [
    {
      "batch_rows": 256,
      "median_seconds": 8.437500218860805e-05,
      "model": "Teacher",
      "p95_seconds": 8.625188929727301e-05,
      "repetitions": 30
    },
    {
      "batch_rows": 256,
      "median_seconds": 8.425000123679638e-05,
      "model": "Dense pruned",
      "p95_seconds": 8.591003861511127e-05,
      "repetitions": 30
    },
    {
      "batch_rows": 256,
      "median_seconds": 4.587500006891787e-05,
      "model": "Int8 storage",
      "p95_seconds": 5.001248646294698e-05,
      "repetitions": 30
    },
    {
      "batch_rows": 256,
      "median_seconds": 4.9791502533480525e-05,
      "model": "Rank4",
      "p95_seconds": 5.3029654372949155e-05,
      "repetitions": 30
    },
    {
      "batch_rows": 256,
      "median_seconds": 2.387499262113124e-05,
      "model": "Student",
      "p95_seconds": 3.2057998760137685e-05,
      "repetitions": 30
    }
  ]
}
```

### code_219 independent vector-export run

```json
{
  "forward_latency": [
    {
      "model": "Teacher",
      "batch_rows": 256,
      "repetitions": 30,
      "median_seconds": 8.320799679495394e-05,
      "p95_seconds": 8.473519119434059e-05
    },
    {
      "model": "Dense pruned",
      "batch_rows": 256,
      "repetitions": 30,
      "median_seconds": 8.29579948913306e-05,
      "p95_seconds": 8.624373731436208e-05
    },
    {
      "model": "Int8 storage",
      "batch_rows": 256,
      "repetitions": 30,
      "median_seconds": 4.662499122787267e-05,
      "p95_seconds": 5.639985756715758e-05
    },
    {
      "model": "Rank4",
      "batch_rows": 256,
      "repetitions": 30,
      "median_seconds": 4.90829988848418e-05,
      "p95_seconds": 5.212529940763488e-05
    },
    {
      "model": "Student",
      "batch_rows": 256,
      "repetitions": 30,
      "median_seconds": 2.3542001144960523e-05,
      "p95_seconds": 2.5014401762746272e-05
    }
  ]
}
```


## Layout and publication verification

All ten inline figures and ten vector book figures were visually inspected. The separately compiled second preview includes fifteen Chapter41 pages, all reviewed with its five front-matter and nine reference pages; all194 previous body pages are pixel-identical. Content revision [b8379e47c6874d2604b205d0f5ca21caa0701adf](https://github.com/ImeshEkanayake/MLBook-/commit/b8379e47c6874d2604b205d0f5ca21caa0701adf) has375 remote blobs matching the clean local checkout. A subsequent metadata revision records publication flags and is separately checked for full-tree and commit-addressed raw-file equality. No weights or manuscript files are published.
