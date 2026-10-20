# Chapter 23 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_115 | 23.1 | 4 | 2 | 3.174 |
| code_116 | 23.2 | 4 | 2 | 3.176 |
| code_117 | 23.3 | 4 | 2 | 4.493 |
| code_118 | 23.4 | 4 | 2 | 2.546 |
| code_119 | 23.5 | 4 | 2 | 2.511 |
| code_120 | 23.6 | 4 | 2 | 3.091 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 23 mechanisms, evidence and boundaries

Six original self-contained CPU Torch laboratories implement actual graph calculations. No dependency was added. They do not claim execution of PyTorch Geometric, full GraphGPS/EGNN systems, complete paper benchmarks or field-valid engineering models. Core pins remain Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0, threadpoolctl 3.7.0 and Torch 2.14.1. Explicit CPU thread count one, float64, deterministic Torch algorithms and seeds 2515–2520. Ordinary runs require no files, downloads, credentials, GPU or private modules.

## Actual mechanisms and results

- **115 — prediction units:** sixty graphs, 10–16 members each, ring plus random chords; 40/10/10 whole buildings. Observed loads/material/capacity and known topology precede separate Bernoulli node-damage/existing-edge-failure targets. Training-only feature scaling. Own logistic versus relational-aggregate logistic, endpoint-symmetric edge logistic, and actual two-layer mean-aggregation encoder with node/symmetric edge heads. Shared neural fit has unit-weighted node/edge BCE, two rates × 250 updates, own joint-development checkpoint; selected rate 0.01/update 50, 722 parameters. Final node Brier own 0.214864132, relational 0.162630380, GNN 0.151053770. Final edge Brier endpoint logistic 0.168729007, GNN 0.185988129. Final 124 nodes/194 connections in ten independent buildings. Graph readout is mean marginal node probability, not a separately fitted graph classifier or a damage-count interval: fraction MSE own 0.048037003, relational 0.023010149, GNN 0.020210577. Known topology/features within final buildings are admitted, labels never enter messages; inductive whole-graph assessment, not a transductive node split. Neither existing-edge failure model predicts absent-link existence.
- **116 — message/operator contracts:** manual five-member chain, explicit stiffness/length edge factors, transformed messages and own-state ReLU update. Edge M1→M0 message [0.344, 0.232], first M0 state [0.564, 0.572], second [0.5914400000000001, 0.59752]. Dense versus indexed accumulation, node permutation equivariance, mean/sum pooling invariance and disconnected block batching pass. Two-layer M0 derivative at M3/M4 is exactly zero, while the reachable M2 derivative is nonzero. Separate sixty twelve-node graphs, 40/10/10, target generated from own/neighbor-mean/two-hop components plus noise 0.03; training-only scale. Actual GCN self-loop symmetric normalization, mean-SAGE separate own/neighbor maps, and GIN-style sum/learned epsilon/MLP. Two rates × 300 updates each, own development selection. Final MSE GCN 0.060759427, SAGE 0.002513548, GIN-style 0.058828733, parameters 353/657/899. Mechanism favors own/mean structure; no universal ranking. Multiset mean collision {1,3}/{2}, scalar-sum collision {1,3}/{0,4}, nonlinear summed squares distinguish latter. Finite learned references do not claim theorem-level injectivity.
- **117 — local/global graph attention:** 260 independent sixteen-node chains, 120/40/100 split. Admitted random loads plus root/terminal markers; root target equals terminal load fifteen hops away. Own two-layer local GAT-style attention (145 parameters) versus own global two-head width-eight graph transformer with shortest-path biases (673), two rates × 400 updates/own development checkpoint. Final root MSE 0.734211620 versus 2.252851e-5. Known marker selector is exact zero by constructed rule and remains visible. Same-weights root derivative outside two local hops zero; global derivative to terminal load 0.985839431. Joint feature/adjacency/distance permutation max errors 0 and 4.44e-16. Attention weights are not physical/causal explanations, and nonedge attention does not create physical adjacency. Separate fixed mean-diffusion fixture measures representation variance across depths, with original-feature reinjection; not a fitted-network comparison. Binary mean-aggregation tree verifies leaf derivatives 2^-depth for depths 1–8 as an explicit compression example, not a universal trained-GNN theorem.
- **118 — typed/time/link:** sixty buildings, each with four members/four sensors/three inspections, 40/10/10 split. Separate typed encoders and building→member, sensor→member, inspection→member and member-connectivity transformations, one actual heterogeneous update and member head; each type's scaler fits training buildings only. Day-ten sensor event/receipt clocks [4,7,9,8]/[4,7,11,9] exclude S2 despite its pre-cutoff event. Inspection creation [1,6,9], assignment [3,8,12], report receipt [5,9,13]; future creation-known entity retains known priority but no future edge/report. Historical assignment edges total 120. Changing unavailable readings leaves admitted values exactly unchanged. Future damage-report surrogate Brier zero is explicitly forbidden, never an admitted candidate. Typed aggregate logistic final Brier 0.189573088 beats relation-specific graph 0.216906630; graph 457 parameters, two rates × 300 update limits, selected 0.005/update 50. Separate inductive ten-parameter typed distance link decoder uses known member load/inspection priority, no identity embeddings; fixed rate 0.02/500 limits and historical-development checkpoint update 300. Enumerated same-building eligible pairs; future candidate set excludes historical positives. Forty historical training nonedges become positive later and are deliberately not removed using future knowledge. An inspection can add a second target member later. Final day10→12 candidates 70 with 20 additions on ten unseen buildings; Brier 0.167455384, AP 0.567720413, MRR 0.916666667. Complete synthetic candidate universe is explicit; real unobserved/censored nonedges require different observation assumptions. Decoder is a scoped relation model, not exhaustive knowledge-graph coverage.
- **119 — geometric/physical graph:** sixty eight-node ring/chord graphs, 40/10/10 split. Positive distance-dependent scalar stiffness, isotropic ground tethers; known dimensionless A=L_k+diag(g), exact U=solve(A,F) targets. This is an ideal isotropic vector network, not bar-direction mechanics, frame bending or structural assessment. Compare a 242-parameter coordinate MLP on seven local features; eight fixed Jacobi steps/eta=1/zero parameters; and eight graph residual steps with learned sigmoid eta/eight parameters. Learned graph explicitly receives the known physical operator, a strong prior absent from the MLP's local features; it is unrolling, not full EGNN execution or a data-only fair-capacity contest. Learned families two rates × 300 updates/own development checkpoint, MLP selected0.005/update240, learned steps0.1/update300; eight independent coefficients remain equal under symmetric initialization at 0.987092391. Final vector MSE MLP 0.090978829, fixed 0.004630261, learned 0.004928872. Residual MSE 0.218250967/0.001308652/0.001291034, so response and force-residual rankings differ slightly. Fixed method's better displacement result retained. Joint rotation0.7rad, reflection and position-translation audits pass for graph methods to rounding: rotation RMS fixed1.5588e-16/learned1.6763e-16 versus MLP0.117997553; reflection0/0 versus0.150239325; translation1.15e-16/1.44e-16 versus0.158647177. Exact equilibrium max error8.88e-16, ground-reaction balance2.66e-15; internal forces sum zero. Ground tethers are isotropic scalar supports, not untransformed fixed-axis restraints. The three-panel typed/time/geometric figure uses declared small semantic/time fixtures plus actual final rotated graph, not a secretly combined trained system.
- **120 — size/sampling/explanation:** eighty star-plus-leaf-ring graphs; forty train/ten dev/ten final at8–12 nodes, twenty additional final at24–40. One observed hub connection weight20 carries load near±2; other weights1. Response .4own+.6weighted-neighbor-mean+noise.02. Own actual weighted indexed aggregate, verified against dense reference; all disconnected edges stay within their building. Mean/sum graph networks use training-only aggregate centers/scales, two rates ×300updates/development selection; relational Ridge1e-6 baseline on own/mean. Final all-node MSE source Ridge0.000315433/mean0.000406300/sum0.024632003; large0.000391314/0.000452390/0.021338846. Hub MSE source0.000245458/0.000523411/0.006503516, large0.000804150/0.001145446/0.214793569. Keeping hub loss exposes sum size failure hidden by ordinary leaf count. Disconnected-batch separate/joined max error1.11e-16. Uniform sampling without replacement atfanouts1/2/4 uses known full weighted degree and degree/fanout correction; an exact single-neighbor expectation check passes. Linear conditional unbiasedness does not transfer through the nonlinear prediction. Frozen mean model, 100repeats per graph/every hub query retained. Source sampled MSE2.991508/1.538728/0.659295; larger5.043918/2.091489/1.005175. Observed important-edge miss fractions source0.890/0.769/0.532, larger0.967/0.9405/0.8785; analytic averages also recorded, finite empirical aggregate deviations retained. Repeats are not new independent buildings, and no measured inference-speed claim is made. Separate four-node opposite-sign fixture: own-sign Brier0/accuracy1; neighbor smoothingBrier1/accuracy0; signed contrastBrier0.0142093/accuracy1. One frozen final larger graph explanation differentiates shared physical edge weights with normalization recomputed, then removes incident connections explicitly. Top-gradient critical-edge removal changes prediction0.461690375 versus uniform incident mean0.020990854; gradient-times-weight estimate0.420683837. Top-two set Jaccard1 across20input-noise perturbationsSD.02. This observed stability and finite-change sensitivity are computational checks, not causal physical-intervention evidence.

## Execution, figures and repairs

All six initial fresh kernels passed without error or stderr warnings. Source/plot review then added the actually used member-connectivity edges to 118's typed diagram and expanded 119's coordinate limits to include complete load arrows. Both current notebook sources reran in fresh kernels and preserved exact deterministic RESULTS. The book-sized 117 plot uses more legible context ticks and shorter equivalent global-attention labeling. All twelve initial notebook images and twelve vector figures were visually inspected; repaired images are rechecked during the composed-page review. Figure generation reruns every current code cell and asserts exact equality with the fresh-kernel summary; no resource replay exception is needed in this chapter. Current notebooks contain 24 executed code cells and twelve inline images. Original plots are SVG/vector-PDF/PNG sets.

Primary papers and versioned official operator/type documentation were accessed20October2026. Version2.5.0 PyG documentation is a conceptual snapshot, not an installed or newest-version claim. All numerical evidence is generated teaching data with explicit task and knowledge boundaries; literature completeness, universal rankings and field validity are not asserted.

## Successful result dictionaries

### code_115

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2515.

```json
{
  "comparisons": [
    {
      "development_Brier": 0.20620721688841698,
      "final_Brier": 0.21486413177777014,
      "method": "Own features",
      "task": "Member damage"
    },
    {
      "development_Brier": 0.16576784864980104,
      "final_Brier": 0.16263038000942462,
      "method": "Relational logistic",
      "task": "Member damage"
    },
    {
      "development_Brier": 0.1662751325373752,
      "final_Brier": 0.168729006822111,
      "method": "Endpoint logistic",
      "task": "Connection failure"
    },
    {
      "development_Brier": 0.17340247857830987,
      "final_Brier": 0.15105377004342088,
      "method": "Graph encoder",
      "task": "Member damage"
    },
    {
      "development_Brier": 0.16056497191901492,
      "final_Brier": 0.18598812941230758,
      "method": "Graph encoder",
      "task": "Connection failure"
    }
  ],
  "final_connections": 194,
  "final_nodes": 124,
  "graph_readout": [
    {
      "final_fraction_MSE": 0.0480370026058475,
      "method": "Own features"
    },
    {
      "final_fraction_MSE": 0.02301014929470626,
      "method": "Relational logistic"
    },
    {
      "final_fraction_MSE": 0.020210577425914124,
      "method": "Graph encoder"
    }
  ],
  "neural_candidates": [
    {
      "best_step": 70,
      "development_sum_Brier": 0.336962212326429,
      "rate": 0.005
    },
    {
      "best_step": 50,
      "development_sum_Brier": 0.3339674504973248,
      "rate": 0.01
    }
  ],
  "node_counts": [
    10,
    11,
    15,
    14,
    14,
    11,
    15,
    11,
    15,
    16,
    12,
    11,
    16,
    12,
    16,
    14,
    12,
    11,
    11,
    10,
    16,
    12,
    13,
    16,
    13,
    13,
    12,
    14,
    10,
    16,
    16,
    14,
    13,
    15,
    15,
    14,
    15,
    10,
    11,
    12,
    12,
    10,
    15,
    15,
    15,
    12,
    12,
    15,
    11,
    11,
    12,
    12,
    16,
    10,
    16,
    13,
    10,
    12,
    10,
    13
  ],
  "selected_rate": 0.01,
  "selected_step": 50,
  "split_buildings": [
    40,
    10,
    10
  ],
  "stored_graph_parameters": 722
}
```

### code_116

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2516.

```json
{
  "candidates": [
    {
      "best_step": 120,
      "development_MSE": 0.08187525391690112,
      "kind": "GCN",
      "rate": 0.005
    },
    {
      "best_step": 120,
      "development_MSE": 0.08312726353943752,
      "kind": "GCN",
      "rate": 0.01
    },
    {
      "best_step": 300,
      "development_MSE": 0.0025000908947998427,
      "kind": "Mean SAGE",
      "rate": 0.005
    },
    {
      "best_step": 300,
      "development_MSE": 0.0019628000638798005,
      "kind": "Mean SAGE",
      "rate": 0.01
    },
    {
      "best_step": 110,
      "development_MSE": 0.08541049964247358,
      "kind": "GIN-style",
      "rate": 0.005
    },
    {
      "best_step": 140,
      "development_MSE": 0.0790247440849809,
      "kind": "GIN-style",
      "rate": 0.01
    }
  ],
  "comparisons": [
    {
      "best_step": 120,
      "development_MSE": 0.08187525391690112,
      "final_MSE": 0.060759427083330236,
      "kind": "GCN",
      "parameters": 353,
      "selected_rate": 0.005
    },
    {
      "best_step": 300,
      "development_MSE": 0.0019628000638798005,
      "final_MSE": 0.0025135482750546106,
      "kind": "Mean SAGE",
      "parameters": 657,
      "selected_rate": 0.01
    },
    {
      "best_step": 140,
      "development_MSE": 0.0790247440849809,
      "final_MSE": 0.058828732687711584,
      "kind": "GIN-style",
      "parameters": 899,
      "selected_rate": 0.01
    }
  ],
  "disconnected_batch_verified": true,
  "manual_trace": {
    "edge_1_to_0_message": [
      0.3440000000000001,
      0.23199999999999998
    ],
    "node_0_first": [
      0.5640000000000001,
      0.5720000000000001
    ],
    "node_0_second": [
      0.5914400000000001,
      0.59752
    ],
    "node_0_two_layer_input_derivative": [
      [
        0.3848000000000001,
        0.4352000000000001
      ],
      [
        0.4000000000000001,
        0.4
      ],
      [
        0.30720000000000003,
        0.1728
      ],
      [
        0.0,
        0.0
      ],
      [
        0.0,
        0.0
      ]
    ]
  },
  "multiset_collisions": [
    {
      "mean": 2.0,
      "square_sum": 10.0,
      "sum": 4.0,
      "values": [
        1.0,
        3.0
      ]
    },
    {
      "mean": 2.0,
      "square_sum": 4.0,
      "sum": 2.0,
      "values": [
        2.0
      ]
    },
    {
      "mean": 2.0,
      "square_sum": 16.0,
      "sum": 4.0,
      "values": [
        0.0,
        4.0
      ]
    }
  ],
  "nodes_per_graph": 12,
  "permutation_max_error": 2.220446049250313e-16,
  "pooling_mean_max_error": 0.0,
  "split_graphs": [
    40,
    10,
    10
  ],
  "two_hop_outside_derivative_max": 0.0
}
```

### code_117

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2517.

```json
{
  "candidates": [
    {
      "best_step": 10,
      "development_MSE": 0.7174568013886014,
      "model": "Local GAT",
      "rate": 0.005
    },
    {
      "best_step": 10,
      "development_MSE": 0.7222315660966523,
      "model": "Local GAT",
      "rate": 0.01
    },
    {
      "best_step": 400,
      "development_MSE": 0.00027299243240292353,
      "model": "Graph transformer",
      "rate": 0.005
    },
    {
      "best_step": 400,
      "development_MSE": 9.043462911806424e-05,
      "model": "Graph transformer",
      "rate": 0.01
    }
  ],
  "chain_nodes": 16,
  "comparisons": [
    {
      "best_step": 10,
      "development_MSE": 0.7174568013886014,
      "final_MSE": 0.7342116203993889,
      "model": "Local GAT",
      "parameters": 145,
      "selected_rate": 0.005
    },
    {
      "best_step": 400,
      "development_MSE": 9.043462911806424e-05,
      "final_MSE": 2.252851143182539e-05,
      "model": "Graph transformer",
      "parameters": 673,
      "selected_rate": 0.01
    }
  ],
  "global_terminal_load_derivative": 0.9858394311737252,
  "known_marker_rule_final_MSE": 0.0,
  "local_outside_two_hops_derivative_max": 0.0,
  "mean_tree_bottleneck": [
    {
      "binary_tree_depth": 1,
      "leaf_count": 2,
      "one_leaf_derivative": 0.5
    },
    {
      "binary_tree_depth": 2,
      "leaf_count": 4,
      "one_leaf_derivative": 0.25
    },
    {
      "binary_tree_depth": 3,
      "leaf_count": 8,
      "one_leaf_derivative": 0.125
    },
    {
      "binary_tree_depth": 4,
      "leaf_count": 16,
      "one_leaf_derivative": 0.0625
    },
    {
      "binary_tree_depth": 5,
      "leaf_count": 32,
      "one_leaf_derivative": 0.03125
    },
    {
      "binary_tree_depth": 6,
      "leaf_count": 64,
      "one_leaf_derivative": 0.015625
    },
    {
      "binary_tree_depth": 7,
      "leaf_count": 128,
      "one_leaf_derivative": 0.0078125
    },
    {
      "binary_tree_depth": 8,
      "leaf_count": 256,
      "one_leaf_derivative": 0.00390625
    }
  ],
  "mixing_fixture": [
    {
      "depth": 0,
      "diffusion_node_variance": 0.7361181088339783,
      "original_reinjection_variance": 0.7361181088339783
    },
    {
      "depth": 1,
      "diffusion_node_variance": 0.19527278664966546,
      "original_reinjection_variance": 0.1999535719927399
    },
    {
      "depth": 2,
      "diffusion_node_variance": 0.11502036771166785,
      "original_reinjection_variance": 0.13917529839795284
    },
    {
      "depth": 4,
      "diffusion_node_variance": 0.06617179553534835,
      "original_reinjection_variance": 0.09440106511375924
    },
    {
      "depth": 8,
      "diffusion_node_variance": 0.03315426383847156,
      "original_reinjection_variance": 0.06974710884774118
    },
    {
      "depth": 16,
      "diffusion_node_variance": 0.013518691026899572,
      "original_reinjection_variance": 0.059243223021524405
    },
    {
      "depth": 32,
      "diffusion_node_variance": 0.0048641198682658785,
      "original_reinjection_variance": 0.05690027290719456
    },
    {
      "depth": 64,
      "diffusion_node_variance": 0.001584356289011645,
      "original_reinjection_variance": 0.056742514425919516
    },
    {
      "depth": 128,
      "diffusion_node_variance": 0.00025827386714318,
      "original_reinjection_variance": 0.05674098178882765
    },
    {
      "depth": 256,
      "diffusion_node_variance": 7.09697393924386e-06,
      "original_reinjection_variance": 0.056740981291752576
    }
  ],
  "permutation_max_errors": {
    "Graph transformer": 4.440892098500626e-16,
    "Local GAT": 0.0
  },
  "split_graphs": [
    120,
    40,
    100
  ],
  "terminal_distance": 15
}
```

### code_118

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2518.

```json
{
  "decision_day": 10,
  "forbidden_future_report_Brier": 0.0,
  "historical_assignment_edges": 120,
  "inspection_assignment_days": [
    3,
    8,
    12
  ],
  "inspection_creation_days": [
    1,
    6,
    9
  ],
  "inspection_report_receipt_days": [
    5,
    9,
    13
  ],
  "link_assessment": {
    "best_step": 300,
    "development_historical_Brier": 0.13947323629838693,
    "future_candidate_pairs": 70,
    "future_final_AP": 0.5677204133177026,
    "future_final_Brier": 0.16745538352977443,
    "future_final_MRR": 0.9166666666666666,
    "future_positive_pairs": 20,
    "future_positive_pairs_retained_as_training_historical_nonedge": 40
  },
  "link_parameters": 10,
  "node_candidates": [
    {
      "best_step": 50,
      "development_Brier": 0.23663388777510425,
      "rate": 0.005
    },
    {
      "best_step": 30,
      "development_Brier": 0.2368085871605155,
      "rate": 0.01
    }
  ],
  "node_comparisons": [
    {
      "development_Brier": 0.21444906049421136,
      "final_Brier": 0.18957308756217203,
      "model": "Typed aggregate logistic"
    },
    {
      "development_Brier": 0.23663388777510425,
      "final_Brier": 0.21690662982457337,
      "model": "Relation-specific graph"
    }
  ],
  "selected_node_rate": 0.005,
  "selected_node_step": 50,
  "sensor_admitted": [
    true,
    true,
    false,
    true
  ],
  "sensor_event_days": [
    4,
    7,
    9,
    8
  ],
  "sensor_receipt_days": [
    4,
    7,
    11,
    9
  ],
  "split_buildings": [
    40,
    10,
    10
  ],
  "typed_graph_parameters": 457,
  "unavailable_reading_perturbation_changes_admitted_values": false
}
```

### code_119

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2519.

```json
{
  "candidates": [
    {
      "best_step": 240,
      "development_MSE": 0.08238714796614363,
      "model": "Coordinate MLP",
      "rate": 0.005
    },
    {
      "best_step": 140,
      "development_MSE": 0.08247523724065134,
      "model": "Coordinate MLP",
      "rate": 0.01
    },
    {
      "best_step": 300,
      "development_MSE": 0.004575326159200558,
      "model": "Learned graph steps",
      "rate": 0.03
    },
    {
      "best_step": 300,
      "development_MSE": 0.0036307750115217472,
      "model": "Learned graph steps",
      "rate": 0.1
    }
  ],
  "comparisons": [
    {
      "development_MSE": 0.08238714796614363,
      "final_equilibrium_residual_MSE": 0.2182509669054868,
      "final_vector_MSE": 0.09097882888429051,
      "model": "Coordinate MLP",
      "parameters": 242,
      "reflection_equivariance_RMS": 0.15023932504523513,
      "rotation_equivariance_RMS": 0.11799755333809782,
      "translation_response_RMS": 0.15864717719865998
    },
    {
      "development_MSE": 0.0034028461790736307,
      "final_equilibrium_residual_MSE": 0.0013086516034321281,
      "final_vector_MSE": 0.004630260613390566,
      "model": "Fixed Jacobi",
      "parameters": 0,
      "reflection_equivariance_RMS": 0.0,
      "rotation_equivariance_RMS": 1.5588141384418595e-16,
      "translation_response_RMS": 1.1523121852871145e-16
    },
    {
      "development_MSE": 0.0036307750115217472,
      "final_equilibrium_residual_MSE": 0.0012910337088742467,
      "final_vector_MSE": 0.004928872032886797,
      "model": "Learned graph steps",
      "parameters": 8,
      "reflection_equivariance_RMS": 0.0,
      "rotation_equivariance_RMS": 1.6762739306542907e-16,
      "translation_response_RMS": 1.4438987551354422e-16
    }
  ],
  "exact_equilibrium_max_error": 8.881784197001252e-16,
  "ground_reaction_balance_max_error": 2.6645352591003757e-15,
  "learned_relaxations": [
    0.9870923908242022,
    0.9870923908242022,
    0.9870923908242022,
    0.9870923908242022,
    0.9870923908242022,
    0.9870923908242022,
    0.9870923908242022,
    0.9870923908242022
  ],
  "minimum_operator_eigenvalue": 0.400710274975125,
  "nodes_per_graph": 8,
  "rotation_radians": 0.7,
  "split_graphs": [
    40,
    10,
    10
  ],
  "unrolled_steps": 8
}
```

### code_120

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2520.

```json
{
  "candidates": [
    {
      "aggregation": "Mean",
      "best_step": 300,
      "development_MSE": 0.0012762798599804171,
      "rate": 0.005
    },
    {
      "aggregation": "Mean",
      "best_step": 300,
      "development_MSE": 0.0005525438181066194,
      "rate": 0.01
    },
    {
      "aggregation": "Sum",
      "best_step": 300,
      "development_MSE": 0.022785491637766952,
      "rate": 0.005
    },
    {
      "aggregation": "Sum",
      "best_step": 300,
      "development_MSE": 0.021393945835010825,
      "rate": 0.01
    }
  ],
  "disconnected_batch_max_error": 1.1102230246251565e-16,
  "explanation_fixture": {
    "input_noise_SD": 0.02,
    "largest_removal_effects": [
      {
        "actual_removal_prediction_change": 0.46169037477553154,
        "edge_index": 0,
        "gradient_times_weight_magnitude": 0.4206838372027928,
        "other_member": 1
      },
      {
        "actual_removal_prediction_change": 0.012047729666387563,
        "edge_index": 33,
        "gradient_times_weight_magnitude": 0.017363762382504866,
        "other_member": 34
      },
      {
        "actual_removal_prediction_change": 0.01158869662171469,
        "edge_index": 18,
        "gradient_times_weight_magnitude": 0.01669134465580662,
        "other_member": 19
      },
      {
        "actual_removal_prediction_change": 0.011080059285530242,
        "edge_index": 29,
        "gradient_times_weight_magnitude": 0.015946263739998627,
        "other_member": 30
      },
      {
        "actual_removal_prediction_change": 0.010941504290068127,
        "edge_index": 30,
        "gradient_times_weight_magnitude": 0.01574330049769479,
        "other_member": 31
      },
      {
        "actual_removal_prediction_change": 0.010894102856422228,
        "edge_index": 20,
        "gradient_times_weight_magnitude": 0.015673864180147958,
        "other_member": 21
      }
    ],
    "mean_top_two_Jaccard_under_input_noise": 1.0,
    "mean_uniform_incident_removal_change": 0.020990853623811406,
    "original_hub_prediction": 0.4073787182110083,
    "perturbation_repeats": 20,
    "top_gradient_edge_other_member": 1,
    "top_gradient_removal_change": 0.46169037477553154
  },
  "heterophily_fixture": [
    {
      "Brier": 0.0,
      "accuracy": 1.0,
      "rule": "Own sign"
    },
    {
      "Brier": 1.0,
      "accuracy": 0.0,
      "rule": "Neighbor smoothing"
    },
    {
      "Brier": 0.014209336618611054,
      "accuracy": 1.0,
      "rule": "Signed contrast"
    }
  ],
  "larger_final_graphs": 20,
  "larger_node_range": [
    24,
    40
  ],
  "sampling": [
    {
      "analytic_critical_miss_fraction": 0.8798376623376625,
      "cohort": "Source size",
      "critical_edge_miss_fraction": 0.89,
      "fanout": 1,
      "finite_sample_aggregate_mean_error": -0.09087369662528158,
      "hub_query_repeats": 1000,
      "loss_SD_across_queries_and_samples": 8.388116650354485,
      "sampled_hub_MSE": 2.991508407085435
    },
    {
      "analytic_critical_miss_fraction": 0.7596753246753246,
      "cohort": "Source size",
      "critical_edge_miss_fraction": 0.769,
      "fanout": 2,
      "finite_sample_aggregate_mean_error": -0.07654796158035736,
      "hub_query_repeats": 1000,
      "loss_SD_across_queries_and_samples": 2.067362708643601,
      "sampled_hub_MSE": 1.53872795384247
    },
    {
      "analytic_critical_miss_fraction": 0.5193506493506493,
      "cohort": "Source size",
      "critical_edge_miss_fraction": 0.532,
      "fanout": 4,
      "finite_sample_aggregate_mean_error": 0.04171642499533226,
      "hub_query_repeats": 1000,
      "loss_SD_across_queries_and_samples": 0.33486956270546464,
      "sampled_hub_MSE": 0.65929493659541
    },
    {
      "analytic_critical_miss_fraction": 0.9680509355701451,
      "cohort": "Larger graphs",
      "critical_edge_miss_fraction": 0.967,
      "fanout": 1,
      "finite_sample_aggregate_mean_error": 0.15311858150496185,
      "hub_query_repeats": 2000,
      "loss_SD_across_queries_and_samples": 31.34417241117359,
      "sampled_hub_MSE": 5.04391750134364
    },
    {
      "analytic_critical_miss_fraction": 0.9361018711402906,
      "cohort": "Larger graphs",
      "critical_edge_miss_fraction": 0.9405,
      "fanout": 2,
      "finite_sample_aggregate_mean_error": 0.02981795464172167,
      "hub_query_repeats": 2000,
      "loss_SD_across_queries_and_samples": 9.200416326207046,
      "sampled_hub_MSE": 2.0914893245802397
    },
    {
      "analytic_critical_miss_fraction": 0.8722037422805812,
      "cohort": "Larger graphs",
      "critical_edge_miss_fraction": 0.8785,
      "fanout": 4,
      "finite_sample_aggregate_mean_error": -0.0256934227428724,
      "hub_query_repeats": 2000,
      "loss_SD_across_queries_and_samples": 2.6231940296453273,
      "sampled_hub_MSE": 1.0051745636975273
    }
  ],
  "size_assessment": [
    {
      "cohort": "Source size",
      "final_all_node_MSE": 0.00031543254027608633,
      "final_hub_MSE": 0.00024545754725648837,
      "graph_count": 10,
      "model": "Relational Ridge"
    },
    {
      "cohort": "Source size",
      "final_all_node_MSE": 0.00040629957802176315,
      "final_hub_MSE": 0.000523410822394403,
      "graph_count": 10,
      "model": "Mean graph"
    },
    {
      "cohort": "Source size",
      "final_all_node_MSE": 0.024632003055546938,
      "final_hub_MSE": 0.006503515665587082,
      "graph_count": 10,
      "model": "Sum graph"
    },
    {
      "cohort": "Larger graphs",
      "final_all_node_MSE": 0.0003913140201134412,
      "final_hub_MSE": 0.000804149986704177,
      "graph_count": 20,
      "model": "Relational Ridge"
    },
    {
      "cohort": "Larger graphs",
      "final_all_node_MSE": 0.0004523899850193947,
      "final_hub_MSE": 0.0011454455988182345,
      "graph_count": 20,
      "model": "Mean graph"
    },
    {
      "cohort": "Larger graphs",
      "final_all_node_MSE": 0.02133884565839691,
      "final_hub_MSE": 0.2147935687670369,
      "graph_count": 20,
      "model": "Sum graph"
    }
  ],
  "source_development_graphs": 10,
  "source_final_graphs": 10,
  "source_node_range": [
    8,
    12
  ],
  "source_train_graphs": 40,
  "training_only_aggregate_scaling": true
}
```

