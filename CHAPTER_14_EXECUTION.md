# Chapter 14 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verification passed.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_067 | 14.1 | 4 | 2 | 1.661 |
| code_068 | 14.2 | 4 | 2 | 1.477 |
| code_069 | 14.3 | 4 | 2 | 1.536 |
| code_070 | 14.4 | 4 | 2 | 1.536 |
| code_071 | 14.5 | 4 | 2 | 1.616 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. All ten inline figures have been visually reviewed. Split patterns, arrival legends, empty-fold ticks and separate stress-panel scales are clear.

## Actual mechanisms and boundaries

Five self-contained generated-data CPU laboratories use seeds 1467–1471 and the existing Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0 environment. Initial kernels passed. Static preflight caught two escaped-newline errors before execution. Notebooks 068–071 subsequently reran for clearer legends, labels, empty-fold ticks and a two-panel stress plot; 068 reran once more to move its window legend off a bar. Numerical result dictionaries remain exactly unchanged. A runner command with an incorrect working-directory path failed before launching a kernel and was corrected. Current timings belong to current executed sources.

The repeated-measurement fixture has 60 buildings, 12 members and two readings per member. Forty-five buildings develop; fifteen remain locked. Fixed standardized KNN5 row CV MSE is 0.244185 versus building CV 0.921466. Five outer grouped folds each use three inner grouped folds to choose among KNN k=1,5,15 and Ridge alpha=.1,10, with locally fitted scalers. Nested outer MSE is 0.734813. The all-development search selects Ridge alpha10; final MSE is 1.006046. Outer models train on 36 buildings, final on 45. Equal-row and equal-building weighting coincide because each building has 24 rows. The split overview is explicitly schematic.

The daily replay evaluates one- and seven-day any-alarm targets at origins 110,150,190,230. Expanding and ninety-day rolling histories use only labels arrived by the refit origin. Each frozen model predicts twenty subsequent daily cutoffs, admitting covariates at their respective times. Fixed logistic C1, eventual retrospective outcomes, Brier/log loss, prevalence baselines and denominators are retained. The invalid earlier-cutoff-only comparator admits [4,3,5,5] unresolved one-day labels and [12,10,12,12] unresolved seven-day labels. Its score can improve or worsen without repairing invalidity. Adjacent cutoffs 80/81 share five context and six target days. Strict cutoffs 80/98 have disjoint complete raw intervals and latest training label arrival97. That stricter separation does not prove independence. Operational replay can legitimately reuse observed past context; overlapping horizons do not supply independent event trials.

A 25×25 synthetic field compares fixed KNN5 with 500 random training locations versus the 500 locations outside a held right-hand fifth. Both assess 125 locations; MSE is 0.010399 and 0.100484. Different held tasks preclude a causal interpretation of this difference. Thirty independent twelve-node paths compare fixed own-feature OLS to OLS with a label-free neighbor mean. Known-graph assessment holds 72 node labels in 24 graphs, with full topology/covariates admitted before fitting; training uses216 nodes. New-graph assessment trains on288 nodes in those24 graphs, then assesses72 nodes in six new graphs whose complete inputs are supplied per request. Equal-graph MSE is approximately 0.532/0.139 for known-graph held nodes and 0.508/0.177 for new graphs. Exact per-graph values remain in the result dictionaries. No held label enters features; no neural graph model or label propagation is run.

Rare-event data have 50 buildings with twelve rows each. Buildings [0,1,2,36,43,47] each contain four positives. Training has432 rows, twelve positives in three buildings; unused development has72 rows/four positives; final has96 rows/eight positives in two buildings. These prevalences are constructed. Five grouped validation folds have [4,0,0,4,4] positive rows; empty folds remain and undefined recall/precision are None. Fixed C1 logistic procedures use unweighted, balanced or training-only oversampled fitting. Scalers fit original training rows before duplication; assessment groups remain disjoint. Threshold .5 is fixed, with no development selection. Final unweighted accuracy is .9167, recall0/8, precisionundefined, Brier .066652. Balanced and oversampled procedures each detect6/8 positives with twelve false alarms, accuracy .8542 and precision1/3, while Brier worsens to .114270/.116313. A majority baseline also misses all positives. One thousand whole-building bootstrap draws include78 with no positive and undefined recall. Conditional percentiles [.5,1] among922 defined draws describe sensitivity to two observed positive buildings, not reliable population interval coverage.

Shift experiments fit 500 source steel-A members and select among fixed Ridge, histogram boosting and a mean baseline on150 separate source development members. Selection chooses Ridge before challenge generation; no development refit or final retuning occurs. Five locked cohorts of200 independent synthetic members isolate steel-A, steel-B, concrete-A, concrete-B and high-load steel-A. SiteB adds an unmodeled .8-unit offset; concrete adds .5(load/50)^2. Material is constant in training. Selected MSEs are approximately .0229,.6911,.1449,1.2285,.0221. Preserving the linear rule lets Ridge extrapolate well at high load; out-of-support status alone does not force poor numerical performance. Adding0/1/5 kN recorded-load bias while fixing truth gives Ridge MSE .022902/.025232/.067317. All frozen procedures remain reported. The detailed stress panel uses a finer vertical scale to reveal learned-model differences. Finite stresses are not worst-case bounds. No independently collected external field evidence is available or implied.

Ten original vector figure sets implement both agreed briefs and the actual numerical comparisons. Two equations define building weighting and arrival admission; seven exercises ask for defensible protocols. Official scikit-learn nested/temporal/grouped/weight documentation and Roberts et al.2017 primary author-hosted full text were inspected19 October2026. The Ecography record is40(8):913–929, DOI10.1111/ecog.02881. Live sklearn documentation1.9.1 versus executed1.9.0 is disclosed. No universal estimator ranking, external field validity or dependable few-positive confidence guarantee is asserted.

## Successful result dictionaries

### code_067

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1467.

```json
{
  "fixed_knn5": {
    "building_cv_mse": 0.9214659070082938,
    "development_buildings": 45,
    "final_buildings": 15,
    "row_cv_mse": 0.24418472612170622,
    "rows_per_building": 24
  },
  "nested": {
    "all_development_inner_scores": {
      "knn1": 1.0802666973565656,
      "knn15": 0.8527872983339524,
      "knn5": 1.0229249332124428,
      "ridge0.1": 0.7723972676113366,
      "ridge10": 0.7697412163392566
    },
    "final_choice": "ridge10",
    "locked_final_mse": 1.006046019645541,
    "outer_folds": [
      {
        "choice": "ridge10",
        "inner_scores": {
          "knn1": 1.1582752342001816,
          "knn15": 1.034578317360231,
          "knn5": 1.1143420891555198,
          "ridge0.1": 0.7185706853824056,
          "ridge10": 0.7141638144563024
        },
        "mse": 0.8721649165926745
      },
      {
        "choice": "ridge10",
        "inner_scores": {
          "knn1": 0.7694498726731323,
          "knn15": 0.6869698856826392,
          "knn5": 0.7280136454893751,
          "ridge0.1": 0.6476581865632653,
          "ridge10": 0.6462080215758255
        },
        "mse": 1.0268282630937373
      },
      {
        "choice": "ridge10",
        "inner_scores": {
          "knn1": 1.49200772828226,
          "knn15": 1.071481270067845,
          "knn5": 1.3294913338677983,
          "ridge0.1": 0.889748277335775,
          "ridge10": 0.8873628833165788
        },
        "mse": 0.19880536103625784
      },
      {
        "choice": "ridge10",
        "inner_scores": {
          "knn1": 0.8858932746325442,
          "knn15": 0.7274733804320809,
          "knn5": 0.8663226172479865,
          "ridge0.1": 0.6781972337923493,
          "ridge10": 0.6767906035530804
        },
        "mse": 1.0111889797668647
      },
      {
        "choice": "ridge10",
        "inner_scores": {
          "knn1": 1.4369081988780594,
          "knn15": 1.2213410120790915,
          "knn5": 1.3747060823533805,
          "ridge0.1": 0.7403157064524272,
          "ridge10": 0.7385497006650418
        },
        "mse": 0.5650772660429383
      }
    ],
    "outer_pooled_mse": 0.7348129573064945,
    "weighting": "equal rows = equal buildings (24 rows each)"
  }
}
```

### code_068

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1468.

```json
{
  "backtest": [
    {
      "assessment_rows": 20,
      "baseline_brier": 0.09485766758494033,
      "brier": 0.08408651056405533,
      "horizon": 1,
      "log_loss": 0.2653955308743356,
      "origin": 110,
      "positives": 2,
      "strategy": "expanding",
      "train_rows": 99,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.09424012979989185,
      "brier": 0.08316765421521058,
      "horizon": 1,
      "log_loss": 0.26164118975028344,
      "origin": 110,
      "positives": 2,
      "strategy": "rolling90",
      "train_rows": 86,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.09502309359977376,
      "brier": 0.08475960546523208,
      "horizon": 1,
      "log_loss": 0.26910920477481703,
      "origin": 110,
      "positives": 2,
      "strategy": "invalid_event_only",
      "train_rows": 103,
      "unarrived_admitted": 4
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.1825,
      "brier": 0.13873085138215938,
      "horizon": 1,
      "log_loss": 0.40925956146642595,
      "origin": 150,
      "positives": 4,
      "strategy": "expanding",
      "train_rows": 140,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.1742898665609724,
      "brier": 0.13503115332598353,
      "horizon": 1,
      "log_loss": 0.405223951507603,
      "origin": 150,
      "positives": 4,
      "strategy": "rolling90",
      "train_rows": 87,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.18281578561298845,
      "brier": 0.13883489193222065,
      "horizon": 1,
      "log_loss": 0.4092709647589092,
      "origin": 150,
      "positives": 4,
      "strategy": "invalid_event_only",
      "train_rows": 143,
      "unarrived_admitted": 3
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.04803055169801794,
      "brier": 0.027977686816606274,
      "horizon": 1,
      "log_loss": 0.11520220586829985,
      "origin": 190,
      "positives": 1,
      "strategy": "expanding",
      "train_rows": 178,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.05207612456747405,
      "brier": 0.030222161431747368,
      "horizon": 1,
      "log_loss": 0.12780669594212213,
      "origin": 190,
      "positives": 1,
      "strategy": "rolling90",
      "train_rows": 85,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.049838753023380825,
      "brier": 0.03157881556543528,
      "horizon": 1,
      "log_loss": 0.1241041335802244,
      "origin": 190,
      "positives": 1,
      "strategy": "invalid_event_only",
      "train_rows": 183,
      "unarrived_admitted": 5
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.20459136436326908,
      "brier": 0.1402467233321842,
      "horizon": 1,
      "log_loss": 0.41105652678999416,
      "origin": 230,
      "positives": 5,
      "strategy": "expanding",
      "train_rows": 218,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.1882006920415225,
      "brier": 0.1348447318790002,
      "horizon": 1,
      "log_loss": 0.39114432646892183,
      "origin": 230,
      "positives": 5,
      "strategy": "rolling90",
      "train_rows": 85,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.20529771360775406,
      "brier": 0.13944064580033458,
      "horizon": 1,
      "log_loss": 0.4092672948338215,
      "origin": 230,
      "positives": 5,
      "strategy": "invalid_event_only",
      "train_rows": 223,
      "unarrived_admitted": 5
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.3226723825624924,
      "brier": 0.229661127942295,
      "horizon": 7,
      "log_loss": 0.6382651610954703,
      "origin": 110,
      "positives": 9,
      "strategy": "expanding",
      "train_rows": 91,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.3074621959237344,
      "brier": 0.20451763017031616,
      "horizon": 7,
      "log_loss": 0.5759859060109649,
      "origin": 110,
      "positives": 9,
      "strategy": "rolling90",
      "train_rows": 78,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.3232585540578753,
      "brier": 0.21987845201922154,
      "horizon": 7,
      "log_loss": 0.6147854257252865,
      "origin": 110,
      "positives": 9,
      "strategy": "invalid_event_only",
      "train_rows": 103,
      "unarrived_admitted": 12
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.301303069704336,
      "brier": 0.15055663492460794,
      "horizon": 7,
      "log_loss": 0.458664273714393,
      "origin": 150,
      "positives": 9,
      "strategy": "expanding",
      "train_rows": 133,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.25749999999999995,
      "brier": 0.13539594446979403,
      "horizon": 7,
      "log_loss": 0.425018849666965,
      "origin": 150,
      "positives": 9,
      "strategy": "rolling90",
      "train_rows": 80,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.30189006797398416,
      "brier": 0.1480374908937875,
      "horizon": 7,
      "log_loss": 0.4533233886641903,
      "origin": 150,
      "positives": 9,
      "strategy": "invalid_event_only",
      "train_rows": 143,
      "unarrived_admitted": 10
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.13779453507061995,
      "brier": 0.08161298364446667,
      "horizon": 7,
      "log_loss": 0.2820194362749724,
      "origin": 190,
      "positives": 3,
      "strategy": "expanding",
      "train_rows": 171,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.15657462195923733,
      "brier": 0.08765945748036999,
      "horizon": 7,
      "log_loss": 0.30880955510392005,
      "origin": 190,
      "positives": 3,
      "strategy": "rolling90",
      "train_rows": 78,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.1485487772104273,
      "brier": 0.08437564871782537,
      "horizon": 7,
      "log_loss": 0.29366568307734175,
      "origin": 190,
      "positives": 3,
      "strategy": "invalid_event_only",
      "train_rows": 183,
      "unarrived_admitted": 12
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.3828137283529121,
      "brier": 0.16003835915052902,
      "horizon": 7,
      "log_loss": 0.4637072851899993,
      "origin": 230,
      "positives": 15,
      "strategy": "expanding",
      "train_rows": 211,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.27071005917159763,
      "brier": 0.10386752099413321,
      "horizon": 7,
      "log_loss": 0.3406215742409443,
      "origin": 230,
      "positives": 15,
      "strategy": "rolling90",
      "train_rows": 78,
      "unarrived_admitted": 0
    },
    {
      "assessment_rows": 20,
      "baseline_brier": 0.377682036638581,
      "brier": 0.15770778162843285,
      "horizon": 7,
      "log_loss": 0.45760628484417937,
      "origin": 230,
      "positives": 15,
      "strategy": "invalid_event_only",
      "train_rows": 223,
      "unarrived_admitted": 12
    }
  ],
  "overlap_fixture": {
    "adjacent_shared_context_days": [
      76,
      77,
      78,
      79,
      80
    ],
    "adjacent_shared_target_days": [
      82,
      83,
      84,
      85,
      86,
      87
    ],
    "independence_not_proved": true,
    "latest_training_label_arrival": 97,
    "strict_cutoffs": [
      80,
      98
    ],
    "strict_raw_overlap": 0
  },
  "protocol": {
    "assessment_cutoffs_per_origin": 20,
    "assessment_labels": "eventual retrospective only",
    "fixed_C": 1,
    "origins": [
      110,
      150,
      190,
      230
    ],
    "overlapping_horizon_targets": "not independent trials",
    "refit_within_block": false
  }
}
```

### code_069

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1469.

```json
{
  "graph": [
    {
      "assessment_graphs": 24,
      "assessment_nodes": 72,
      "features": "own",
      "macro_graph_mse": 0.5323617817755585,
      "per_graph_mse": [
        0.19195225887540027,
        0.526944617941351,
        0.24198444641654762,
        0.13692138402035683,
        0.2872711270476973,
        2.0678587479375516,
        0.6284109082620096,
        0.9374416771632813,
        0.7721223773228867,
        1.2676876360178488,
        0.36500033903028806,
        0.11032738469559324,
        0.17863930198535147,
        0.05608600129389798,
        0.6416692996802209,
        0.12102731900866374,
        0.33297133251984673,
        0.5367622034827776,
        0.11778582183935234,
        0.32762125508740314,
        0.21718838361707302,
        2.0596781512116222,
        0.3682880446598964,
        0.2850427434964843
      ],
      "protocol": "known_graph_nodes",
      "train_nodes": 216
    },
    {
      "assessment_graphs": 24,
      "assessment_nodes": 72,
      "features": "own_and_neighbor",
      "macro_graph_mse": 0.13922522233244353,
      "per_graph_mse": [
        0.029227460842114177,
        0.14006149953982236,
        0.2425428284995218,
        0.05947021832372341,
        0.010899717600751419,
        0.06329856147205039,
        0.24076123422074266,
        0.11129757255952187,
        0.3145084961041695,
        0.40561490121518456,
        0.012959406151932267,
        0.22206009593933185,
        0.004049476753806997,
        0.03875670049405946,
        0.12329577495338633,
        0.02647910396299286,
        0.06966921392728158,
        0.015468676286750352,
        0.010509293969460825,
        0.036792707900599644,
        0.03895661994290323,
        0.8734108635314088,
        0.053153039011076965,
        0.19816187277605132
      ],
      "protocol": "known_graph_nodes",
      "train_nodes": 216
    },
    {
      "assessment_graphs": 6,
      "assessment_nodes": 72,
      "features": "own",
      "macro_graph_mse": 0.508361653928513,
      "per_graph_mse": [
        0.831833516435459,
        0.3890188611632564,
        0.2914637929728147,
        0.3905240868699466,
        0.7600605169509831,
        0.3872691491786177
      ],
      "protocol": "new_graphs",
      "train_nodes": 288
    },
    {
      "assessment_graphs": 6,
      "assessment_nodes": 72,
      "features": "own_and_neighbor",
      "macro_graph_mse": 0.1770197544312949,
      "per_graph_mse": [
        0.30701894878057795,
        0.16276550112618218,
        0.09085215330296607,
        0.017721286519046805,
        0.17350663305809144,
        0.3102540038009049
      ],
      "protocol": "new_graphs",
      "train_nodes": 288
    }
  ],
  "graph_inputs": {
    "held_labels_used_in_features": false,
    "held_node_covariates": "known before fitting in transductive case",
    "topology": "complete path per request"
  },
  "spatial": [
    {
      "assessment_locations": 125,
      "mse": 0.010398911737336754,
      "protocol": "random_locations",
      "train_locations": 500
    },
    {
      "assessment_locations": 125,
      "mse": 0.10048379128054916,
      "protocol": "right_region",
      "train_locations": 500
    }
  ]
}
```

### code_070

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1470.

```json
{
  "building_bootstrap": {
    "conditional_percentiles_2_5_97_5": [
      0.5,
      1.0
    ],
    "defined_draws": 922,
    "draws": 1000,
    "final_positive_buildings": 2,
    "interpretation": "conditional descriptive sensitivity, not reliable population coverage",
    "undefined_zero_positive_draws": 78
  },
  "development_unused": {
    "positives": 4,
    "reason": "procedures and .5 threshold fixed, no selection",
    "rows": 72
  },
  "final_majority_baseline": {
    "accuracy": 0.9166666666666666,
    "brier": 0.08333333333333333,
    "false_positives": 0,
    "positive_buildings": 2,
    "positive_rows": 8,
    "precision": null,
    "recall": 0.0,
    "rows": 96,
    "true_positives": 0
  },
  "fold_metrics": [
    {
      "accuracy": 0.9583333333333334,
      "brier": 0.04074400408039767,
      "false_positives": 0,
      "fold": 0,
      "method": "unweighted",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": null,
      "recall": 0.0,
      "rows": 96,
      "true_positives": 0
    },
    {
      "accuracy": 1.0,
      "brier": 0.001507787203917582,
      "false_positives": 0,
      "fold": 1,
      "method": "unweighted",
      "positive_buildings": 0,
      "positive_rows": 0,
      "precision": null,
      "recall": null,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 1.0,
      "brier": 0.002446295591529659,
      "false_positives": 0,
      "fold": 2,
      "method": "unweighted",
      "positive_buildings": 0,
      "positive_rows": 0,
      "precision": null,
      "recall": null,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 0.9523809523809523,
      "brier": 0.0386445762061551,
      "false_positives": 0,
      "fold": 3,
      "method": "unweighted",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": null,
      "recall": 0.0,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 0.9642857142857143,
      "brier": 0.032962005169904704,
      "false_positives": 0,
      "fold": 4,
      "method": "unweighted",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 1.0,
      "recall": 0.25,
      "rows": 84,
      "true_positives": 1
    },
    {
      "accuracy": 0.7291666666666666,
      "brier": 0.17288170985853205,
      "false_positives": 24,
      "fold": 0,
      "method": "balanced",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 0.07692307692307693,
      "recall": 0.5,
      "rows": 96,
      "true_positives": 2
    },
    {
      "accuracy": 0.8571428571428571,
      "brier": 0.12154008666377256,
      "false_positives": 12,
      "fold": 1,
      "method": "balanced",
      "positive_buildings": 0,
      "positive_rows": 0,
      "precision": 0.0,
      "recall": null,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 0.7738095238095238,
      "brier": 0.14913150261845398,
      "false_positives": 19,
      "fold": 2,
      "method": "balanced",
      "positive_buildings": 0,
      "positive_rows": 0,
      "precision": 0.0,
      "recall": null,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 0.7738095238095238,
      "brier": 0.15883359665492172,
      "false_positives": 19,
      "fold": 3,
      "method": "balanced",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 0.17391304347826086,
      "recall": 1.0,
      "rows": 84,
      "true_positives": 4
    },
    {
      "accuracy": 0.8095238095238095,
      "brier": 0.11644741672318784,
      "false_positives": 14,
      "fold": 4,
      "method": "balanced",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 0.125,
      "recall": 0.5,
      "rows": 84,
      "true_positives": 2
    },
    {
      "accuracy": 0.71875,
      "brier": 0.17515927726554345,
      "false_positives": 25,
      "fold": 0,
      "method": "oversample",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 0.07407407407407407,
      "recall": 0.5,
      "rows": 96,
      "true_positives": 2
    },
    {
      "accuracy": 0.8571428571428571,
      "brier": 0.11296974812302468,
      "false_positives": 12,
      "fold": 1,
      "method": "oversample",
      "positive_buildings": 0,
      "positive_rows": 0,
      "precision": 0.0,
      "recall": null,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 0.7738095238095238,
      "brier": 0.14630598947866771,
      "false_positives": 19,
      "fold": 2,
      "method": "oversample",
      "positive_buildings": 0,
      "positive_rows": 0,
      "precision": 0.0,
      "recall": null,
      "rows": 84,
      "true_positives": 0
    },
    {
      "accuracy": 0.7857142857142857,
      "brier": 0.15542789583189837,
      "false_positives": 18,
      "fold": 3,
      "method": "oversample",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 0.18181818181818182,
      "recall": 1.0,
      "rows": 84,
      "true_positives": 4
    },
    {
      "accuracy": 0.8095238095238095,
      "brier": 0.11489007315771713,
      "false_positives": 14,
      "fold": 4,
      "method": "oversample",
      "positive_buildings": 1,
      "positive_rows": 4,
      "precision": 0.125,
      "recall": 0.5,
      "rows": 84,
      "true_positives": 2
    }
  ],
  "folds": [
    {
      "positive_buildings": 1,
      "positive_rows": 4,
      "validation_rows": 96
    },
    {
      "positive_buildings": 0,
      "positive_rows": 0,
      "validation_rows": 84
    },
    {
      "positive_buildings": 0,
      "positive_rows": 0,
      "validation_rows": 84
    },
    {
      "positive_buildings": 1,
      "positive_rows": 4,
      "validation_rows": 84
    },
    {
      "positive_buildings": 1,
      "positive_rows": 4,
      "validation_rows": 84
    }
  ],
  "procedures": [
    {
      "final": {
        "accuracy": 0.9166666666666666,
        "brier": 0.06665191840026997,
        "false_positives": 0,
        "positive_buildings": 2,
        "positive_rows": 8,
        "precision": null,
        "recall": 0.0,
        "rows": 96,
        "true_positives": 0
      },
      "method": "unweighted",
      "oof": {
        "accuracy": 0.9745370370370371,
        "brier": 0.02374657449565918,
        "false_positives": 0,
        "positive_buildings": 3,
        "positive_rows": 12,
        "precision": 1.0,
        "recall": 0.08333333333333333,
        "rows": 432,
        "true_positives": 1
      }
    },
    {
      "final": {
        "accuracy": 0.8541666666666666,
        "brier": 0.11426976517837023,
        "false_positives": 12,
        "positive_buildings": 2,
        "positive_rows": 8,
        "precision": 0.3333333333333333,
        "recall": 0.75,
        "rows": 96,
        "true_positives": 6
      },
      "method": "balanced",
      "oof": {
        "accuracy": 0.7870370370370371,
        "brier": 0.14457560826362803,
        "false_positives": 88,
        "positive_buildings": 3,
        "positive_rows": 12,
        "precision": 0.08333333333333333,
        "recall": 0.6666666666666666,
        "rows": 432,
        "true_positives": 8
      }
    },
    {
      "final": {
        "accuracy": 0.8541666666666666,
        "brier": 0.11631308274250586,
        "false_positives": 12,
        "positive_buildings": 2,
        "positive_rows": 8,
        "precision": 0.3333333333333333,
        "recall": 0.75,
        "rows": 96,
        "true_positives": 6
      },
      "method": "oversample",
      "oof": {
        "accuracy": 0.7870370370370371,
        "brier": 0.14190083789620841,
        "false_positives": 88,
        "positive_buildings": 3,
        "positive_rows": 12,
        "precision": 0.08333333333333333,
        "recall": 0.6666666666666666,
        "rows": 432,
        "true_positives": 8
      }
    }
  ]
}
```

### code_071

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1"}`; Darwin arm64 CPU; seed 1471.

```json
{
  "challenges": [
    {
      "cohort": "steel_A",
      "mean_residual_prediction_minus_truth": 0.008544072799142448,
      "members": 200,
      "model": "ridge",
      "mse": 0.02290167199917165,
      "selected_before_assessment": true
    },
    {
      "cohort": "steel_A",
      "mean_residual_prediction_minus_truth": 0.006496420039489771,
      "members": 200,
      "model": "boosting",
      "mse": 0.02858377136041251,
      "selected_before_assessment": false
    },
    {
      "cohort": "steel_A",
      "mean_residual_prediction_minus_truth": 0.07382035350790281,
      "members": 200,
      "model": "mean",
      "mse": 1.1966335492908384,
      "selected_before_assessment": false
    },
    {
      "cohort": "steel_B",
      "mean_residual_prediction_minus_truth": -0.8176647131205822,
      "members": 200,
      "model": "ridge",
      "mse": 0.6911275599726142,
      "selected_before_assessment": true
    },
    {
      "cohort": "steel_B",
      "mean_residual_prediction_minus_truth": -0.8110701362668732,
      "members": 200,
      "model": "boosting",
      "mse": 0.6921108570408512,
      "selected_before_assessment": false
    },
    {
      "cohort": "steel_B",
      "mean_residual_prediction_minus_truth": -0.6787716373921348,
      "members": 200,
      "model": "mean",
      "mse": 1.5036542194231777,
      "selected_before_assessment": false
    },
    {
      "cohort": "concrete_A",
      "mean_residual_prediction_minus_truth": -0.28064114092142306,
      "members": 200,
      "model": "ridge",
      "mse": 0.14492468834696054,
      "selected_before_assessment": true
    },
    {
      "cohort": "concrete_A",
      "mean_residual_prediction_minus_truth": -0.2759943644478963,
      "members": 200,
      "model": "boosting",
      "mse": 0.1533526952900808,
      "selected_before_assessment": false
    },
    {
      "cohort": "concrete_A",
      "mean_residual_prediction_minus_truth": -0.18138992115413477,
      "members": 200,
      "model": "mean",
      "mse": 1.5031636120396985,
      "selected_before_assessment": false
    },
    {
      "cohort": "concrete_B",
      "mean_residual_prediction_minus_truth": -1.0804244095324336,
      "members": 200,
      "model": "ridge",
      "mse": 1.2285322188990508,
      "selected_before_assessment": true
    },
    {
      "cohort": "concrete_B",
      "mean_residual_prediction_minus_truth": -1.0737993654518925,
      "members": 200,
      "model": "boosting",
      "mse": 1.2325394168085777,
      "selected_before_assessment": false
    },
    {
      "cohort": "concrete_B",
      "mean_residual_prediction_minus_truth": -0.9456096344493831,
      "members": 200,
      "model": "mean",
      "mse": 2.187813505269047,
      "selected_before_assessment": false
    },
    {
      "cohort": "high_load_steel_A",
      "mean_residual_prediction_minus_truth": 0.020350674863590844,
      "members": 200,
      "model": "ridge",
      "mse": 0.02205770391867917,
      "selected_before_assessment": true
    },
    {
      "cohort": "high_load_steel_A",
      "mean_residual_prediction_minus_truth": -1.0749385193407455,
      "members": 200,
      "model": "boosting",
      "mse": 1.2777967542203195,
      "selected_before_assessment": false
    },
    {
      "cohort": "high_load_steel_A",
      "mean_residual_prediction_minus_truth": -2.021871875019549,
      "members": 200,
      "model": "mean",
      "mse": 4.968329273205239,
      "selected_before_assessment": false
    }
  ],
  "external_field_evidence": {
    "available": false,
    "reason": "all cohorts are independent synthetic draws from author-declared mechanisms"
  },
  "sensor_bias_stress": [
    {
      "load_measurement_bias_kN": 0,
      "model": "ridge",
      "mse": 0.02290167199917165
    },
    {
      "load_measurement_bias_kN": 0,
      "model": "boosting",
      "mse": 0.02858377136041251
    },
    {
      "load_measurement_bias_kN": 0,
      "model": "mean",
      "mse": 1.1966335492908384
    },
    {
      "load_measurement_bias_kN": 1,
      "model": "ridge",
      "mse": 0.025231618475273443
    },
    {
      "load_measurement_bias_kN": 1,
      "model": "boosting",
      "mse": 0.03179432828618295
    },
    {
      "load_measurement_bias_kN": 1,
      "model": "mean",
      "mse": 1.1966335492908384
    },
    {
      "load_measurement_bias_kN": 5,
      "model": "ridge",
      "mse": 0.06731720758174936
    },
    {
      "load_measurement_bias_kN": 5,
      "model": "boosting",
      "mse": 0.0700678156937433
    },
    {
      "load_measurement_bias_kN": 5,
      "model": "mean",
      "mse": 1.1966335492908384
    }
  ],
  "source_selection": {
    "development_members": 150,
    "development_mse": {
      "boosting": 0.034300795085640275,
      "mean": 1.3138840914902334,
      "ridge": 0.023580140263327477
    },
    "features": [
      "load_kN",
      "age_years"
    ],
    "refit_on_development": false,
    "selected": "ridge",
    "train_members": 500
  }
}
```


## Remote content verification

Content commit [e82b686035bea86555b440ef8718cfe7ab894a43](https://github.com/ImeshEkanayake/MLBook-/commit/e82b686035bea86555b440ef8718cfe7ab894a43) is published on main. All 121 remote blobs match the local commit and the earlier 66 manifest records are unchanged. The final metadata commit is independently verified in the local book delivery evidence, including commit-addressed raw files.
