# Chapter 13 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verification passed.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_062 | 13.1 | 4 | 2 | 1.315 |
| code_063 | 13.2 | 4 | 2 | 1.366 |
| code_064 | 13.3 | 4 | 2 | 1.396 |
| code_065 | 13.4 | 4 | 2 | 1.350 |
| code_066 | 13.5 | 5 | 2 | 1.370 |

Total: **21 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed; relation legends, node IDs, initial-state callouts and masks are clear.

## Actual mechanisms and boundaries

All five laboratories are self-contained generated construction audits and execute successfully in fresh kernels. No advanced graph/sequence/scientific architecture is trained, and no benchmark or field validation is claimed. Ordinary execution requires no network, credentials, GPU or additional dependency. A static builder check caught derivative apostrophes prematurely closing a source string; derivative notation and an inadvertently rewritten dictionary key were corrected before kernel execution. There were no failed reference kernel runs. Diagram review prompted successful reruns of code_062/064/065/066 for a physical-to-typed-graph panel, relation legends, unobstructed mesh IDs, shorter field labels, explicit dynamic initial-state text and integer mask indices. Current sources retain the same result dictionaries.

The typed graph has four members/four sensors, four undirected mechanical connections (eight directed entries) and four sensor-to-member measurement links. A[target,source] is explicit; equal weights and empty-neighborhood placeholders are declared choices. The top member carries [0,-10] kN. Row normalization/self-loops differ; consistent node reordering preserves both relation-specific aggregations. Eighty admitted sensor observations give two .8-threshold absolute-correlation edges; invalid use of all 120 observations with a later shared component yields six. Future-input perturbation leaves the training-only graph unchanged. These associations are neither physical connectivity nor causal identification, and no learned graph is fitted.

Irregular sequence context (c-5,c] and future-record-mean target (c,c+2] use stride one and a c+3 label-resolution rule. Seventeen training cutoffs 8–24 and nineteen final cutoffs 32–50 have disjoint raw context/target IDs; alternating-window splitting shares forty-four IDs. Four training and three final windows remain unresolved under the reporting rule. At cutoff 15, grid times [11,12,13,14,15] have validity [true,false,true,false,false], with only two bounded-hold measurements available. A true observed zero remains valid; placeholders require masks. The conservative replay checks arrival at each grid time and maximum observation age 1.5 s; future-value perturbation leaves its inputs unchanged. This is a construction audit of a recorded-mean target, not an unobserved continuous-process estimate or independence guarantee.

The six-node/four-triangle mesh has nine unique edges, positive CCW areas totaling 2 m², stable noncontiguous IDs, nodal temperature and separate cell conductivities. Left boundary IDs [101,401] and right [310,612] retain their meanings through reindexing. Consistent coordinate/connectivity/field/tag permutation preserves areas and the exact linear-field temperature integral 652 K m²; a coordinates-only permutation fails. A 30-degree rotation and origin translation preserve edge lengths/areas/scalars while rotating gradient [25,2] to [20.650635095,14.232050808] K/m. Tag 0 means neither named side, not a claim that every such node is physically interior. No mesh file parser, Gmsh execution or finite-element solution is asserted.

The static cantilever contract declares L=3 m, EI=8 MN m², q=5 kN/m, a homogeneous small-deflection linear Euler–Bernoulli law, clamped displacement/slope and free-end zero curvature/third derivative. Analytic boundary/balance/tip checks pass and tip displacement is 6.328125 mm. A separate dynamic schema states initial rest and additional mass/forcing/time inputs, without computing a transient. Doubling q and EI leaves the full field identical, exposing inverse ratio ambiguity. With q known independently, twenty .02-mm-noise repeated tip measurements give mean EI 7.997917125 MN m², sample SD .022526972, range 7.947596971–8.032825961. This is repeated-reading sensitivity, not a posterior interval or inclusion of support/model uncertainty. MIT's primary formula-sheet text was retrieved and inspected; the complete reference and derivatives are checked independently in code.

The batching audit combines a three-node chain and a two-node graph into a five-node disconnected union with correct offsets and membership. Joint aggregation equals separate calls; pooled means are [2,15]. Two masked sequence means [1.5,5] survive replacing padding with 1e9 while preserving a real zero. Uniform pairs of [0,0,0,100] yield means [0,0,50,0,50,50], whose average is the full mean 25; a single sampled neighborhood varies, and no nonlinear-network unbiasedness claim follows. Rotating anisotropic stiffness, force, geometry and displacement consistently gives original u=[.714285714,-.857142857] mm and rotated [1.099450346,.190018146], preserving norm 1.115749954 mm and work. Leaving anisotropic stiffness unchanged fails covariance. Diagram arrow drawing scales are stated explicitly. Mesh coarsening and normalization/nondimensionalization are explained as contracts, not claimed as implemented solvers.

Nine original vector figures implement both agreed visual briefs: the physical-frame conversion to typed relations with loads/directions, and context/forecast windows paired with a supported physical domain and declared initial-state distinction. Five equations state relation aggregation, coordinate transformation, cantilever conditions/reference, and mechanical covariance. Primary/official Gmsh, PyTorch Geometric and MIT sources support concepts only where inspected; the NumPy audit mechanisms are independent and no unavailable dependency is hidden in the examples.

## Successful result dictionaries

### code_062

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1362.

```json
{
  "correlation_graph": {
    "construction_uses_no_targets": true,
    "fit_observations": 80,
    "invalid_all_history_edges": 6,
    "threshold": 0.8,
    "training_undirected_edges": 2
  },
  "typed_graph": {
    "adjacency_convention": "target,source",
    "measurement_directed_entries": 4,
    "member_nodes": 4,
    "nodes": 8,
    "permutation_equivariance_passed": true,
    "sensor_nodes": 4,
    "structural_directed_entries": 8,
    "top_member_load_kN": [
      0.0,
      -10.0
    ]
  }
}
```

### code_063

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1363.

```json
{
  "future_value_perturbation_invariance": true,
  "grid_at_15": {
    "observed_mask": [
      true,
      false,
      true,
      false,
      false
    ],
    "source_ids": [
      10,
      -1,
      12,
      -1,
      -1
    ],
    "times": [
      11.0,
      12.0,
      13.0,
      14.0,
      15.0
    ],
    "values": [
      -0.7505928372855579,
      0.0,
      -0.9922499357853239,
      0.0,
      0.0
    ]
  },
  "separated_raw_records": true,
  "window_counts": {
    "final": 19,
    "invalid_alternating_raw_overlap": 44,
    "train": 17,
    "unresolved_final": 3,
    "unresolved_train": 4
  }
}
```

### code_064

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1364.

```json
{
  "mesh": {
    "area_m2": 2.0,
    "consistent_reindexing_passed": true,
    "left_boundary_ids": [
      101,
      401
    ],
    "nodes": 6,
    "right_boundary_ids": [
      310,
      612
    ],
    "temperature_integral_K_m2": 652.0,
    "triangles": 4,
    "undirected_edges": 9
  },
  "rigid_frame_checks_passed": true,
  "rotated_gradient_K_per_m": [
    20.65063509461097,
    14.232050807568875
  ]
}
```

### code_065

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1365.

```json
{
  "boundary_and_balance_checks_passed": true,
  "dynamic_schema_only": {
    "additional_inputs": [
      "mass_per_length_kg_per_m",
      "q(x,t)",
      "time_domain"
    ],
    "initial_displacement": "w(x,0)=0 m",
    "initial_velocity": "dw/dt(x,0)=0 m/s",
    "not_solved": true
  },
  "inverse_known_load_EI_MN_m2": {
    "max": 8.032825960928387,
    "mean": 7.997917124679079,
    "min": 7.947596971229724,
    "observations": 20,
    "sd_across_readings": 0.02252697177459991
  },
  "static_contract": {
    "boundary": {
      "x0": [
        "w=0",
        "slope=0"
      ],
      "xL": [
        "curvature=0",
        "third_derivative=0"
      ]
    },
    "forcing": {
      "uniform_q_N_per_m": 5000.0
    },
    "geometry": {
      "length_m": 3.0
    },
    "initial_state": "not applicable to static task",
    "material": {
      "EI_N_m2": 8000000.0,
      "law": "homogeneous linear Euler-Bernoulli"
    },
    "output": "w in m, positive downward",
    "task": "static cantilever forward displacement"
  },
  "tip_displacement_mm": 6.328125,
  "unknown_load_stiffness_ratio_ambiguity_passed": true
}
```

### code_066

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1366.

```json
{
  "graph_batch": {
    "entities": 2,
    "no_cross_entity_edges": true,
    "nodes": 5,
    "pooled_means": [
      2.0,
      15.0
    ]
  },
  "masked_sequence_means": [
    1.5,
    5.0
  ],
  "neighbor_sampling": {
    "all_uniform_pair_means": [
      0.0,
      0.0,
      50.0,
      0.0,
      50.0,
      50.0
    ],
    "full_mean": 25.0,
    "mean_over_pairs": 25.0
  },
  "padding_perturbation_invariance": true,
  "rotation": {
    "covariance_checks_passed": true,
    "magnitude_mm": 1.1157499537009505,
    "original_displacement_mm": [
      0.7142857142857143,
      -0.8571428571428571
    ],
    "rotated_displacement_mm": [
      1.0994503461009473,
      0.19001814556031324
    ],
    "unchanged_anisotropic_stiffness_detected_as_invalid": true
  }
}
```


Book-page inspection caught an oversized tightly cropped vertical graph figure. Its export now retains the full declared canvas so print scaling preserves the intended height; node/legend positions were repaired and the current code_062 source reran successfully with unchanged results. The preview integrity checker now rejects the oversized-float warning as well as overflow/reference errors. The other completed cumulative builds were checked for this warning and contain none.

## Publication verification

Content commit `dbf53f34b4214618f97c8325151bf91a6d0263fe` was pushed normally to main. All 113 remote file blobs match the local Git tree; remote main matches and the working tree was clean. All 61 prior manifest records remain unchanged. Final metadata verification additionally retrieves commit-addressed raw registry, manifest, guide, report and five notebooks.
