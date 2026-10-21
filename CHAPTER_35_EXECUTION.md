# Chapter 35 execution evidence

**Date:** 22 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and generated cohort is internal. Ordinary execution is offline and CPU-only after the explicit [checkpoint acquisition](CHAPTER_35_ASSETS.md) for 185 and [separate runtime setup](CHAPTER_35_RUNTIME.md) for 186. Actual versions and hardware are printed by every kernel and retained below. A separate CPython 3.12 environment with 81 pinned packages supports native AutoGluon in code_186; code_185 reuses a verified 29 MB TabPFN asset. See the runtime and asset guides. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_183 | 35.1 | 4 | 2 | 2.833 |
| code_184 | 35.2 | 4 | 2 | 3.287 |
| code_185 | 35.3 | 4 | 2 | 3.950 |
| code_186 | 35.4 | 4 | 2 | 2.825 |
| code_187 | 35.5 | 4 | 3 | 2.584 |

Total: **20 executed code cells and 11 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

# Chapter 35 mechanisms, controls and interpretation

Five laboratories preserve all five numbered scopes and both visual briefs. They execute 20 code cells and produce 11 inline figures. All imports, helpers and generated observations are internal. Ordinary runs are offline and CPU-only, but laboratory 185 needs the explicitly acquired, hash-verified TabPFN v2 checkpoint; laboratory 186 needs a dedicated Python environment. Literature cutoff: 18 October 2026. Execution and primary-source access: 22 October 2026 Australia/Melbourne.

## Environments and assets

Laboratories 183–185 and 187 use the unchanged CPython 3.14.3 environment: NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and Torch 2.14.1 CPU; 185 additionally uses already installed TabPFN 9.2.0. The explicit v2 classifier weights are reused from the verified Chapter 28 cache: Prior-Labs/TabPFN-v2-clf revision f851f2a3c941544733b712d8c0f96dfae9b28862, filename tabpfn-v2-classifier-v2_default.ckpt, 29, 009, 539 bytes, SHA 256 cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49. The asset guide, acquisition script and licence notice accompany the notebook. No new model download occurred; missing or different bytes fail explicitly rather than substitute a model.

AutoGluon 1.6.3 excludes Python 3.14. Laboratory 186 therefore uses a separate CPython 3.12.13 environment with AutoGluon tabular/core/features/common1.6.3, Torch 2.14.1 CPU, NumPy 2.5.4, SciPy 1.18.1, pandas 2.3.3, scikit-learn 1.9.1, LightGBM 4.7.0 and Matplotlib 3.11.2. Direct requirements and all 81 installed package pins are published separately. Primary PyPI release metadata verifies all 81 versions were available before 19 OctoberUTC. Both environments pass pip checks; neither the main environment nor the separate Chapter 30 environment is changed. Native fitting imports Torch first, uses float 32 and one CPU thread; the other Torch laboratories use float 64. The runtime guide records exact commands and boundaries.

## Actual mechanisms

- **183 / conditional spaces:**180 buildings with four records each split 108 source/36 development/36 final. Twelve pre-drawn configurations cross six native-missing histogram-boosting recipes and six source-median-imputed neural recipes with StandardScaler or RobustScaler. Tree depth/leaf minimum/rate and neural width/rate/decay/scaler are genuinely conditional. Trees train 60 iterations with automatic stopping disabled; networks train 150 full-batch updates. Assertions independently verify source-fitted transformation statistics. Development RMSE chooses one recipe, refitted using the same source, seed and fixed resources before one final assessment. Trial 11, neural width 8 with standard scaling, scores development 0.7509 and final 0.916687 RMSE. Source scores for all candidates remain descriptive rather than a selection objective.
- **184 / search and scheduling:**A fixed 6→12→1 Tanh network and a declared 64-point log-uniform learning-rate/decay pool support actual random search, Gaussian-process expected improvement, successive halving and Hyperband. Random/GP each fit 16 candidates for 27 updates, spending 432 updates; their first four candidates coincide. The GP uses a fixed Matern kernel and actual untried-pool EI, without a claim to reproduce the paper's full inference scheme. Four halving brackets restart27/9/3/1 candidates at1/3/9/27 updates, each spending 108. Hyperband's four brackets spend108/99/108/108=423 under a432 ceiling, leaving 9 unused. The declared return rule considers full 27-update candidates only; this differs from the original algorithm's minimum over intermediate losses. Actual synchronous population training uses four slots, 108 updates each, development checks every nine updates, 11 weight-and-Adam-state exploit copies and multiplicative clipped rate/decay exploration. Its longer effective horizon differs from static search; sequential CPU execution does not reproduce asynchronous scheduling. Final RMSE random/GP1.463158, halving/Hyperband1.382326, population 1.552595. Final scores never choose among policies. Visual B displays actual resources and eliminations rather than a conceptual learning curve.
- **185 / staged family and architecture choice:**64 buildings split 32 source/16 development/16 final, with five records each. Four actual screening fits are median-imputed scaled logistic, native histogram boosting, a small neural network and frozen TabPFN v2 with 160 source-context labels. Development Brier shortlists TabPFN and linear; predeclared expansion adds a four-member TabPFN prediction ensemble and degree-two polynomial logistic. Other potential expansions are declared but not executed or counted. Six actual fits enter the attempt log. Development chooses the original single-member TabPFN; an independently fitted convex combination of the top two assigns weight 1.0 to it, so the ensemble is honestly degenerate. Final Brier 0.240192 versus source-prevalence0.248008; log loss 0.666231 versus 0.689161. A source-only eight-row warm-up precedes the pretrained-parameter hash: native inference preparation can change dtype/state before that boundary. Subsequent development/final prediction leaves the hashed state unchanged. No final outcome fits any choice.
- **186 / native AutoML:**120 buildings split 72 source/24 development/24 final, four records each, with numerical missing values and categorical zones. Six manual logistic/boosting candidates and native AutoGluon LightGBM 80, random forest 80, NeuralNetTorch 25 and weighted ensemble use the same development-log-loss objective and separate 15-second ceilings. Feature generation is inside each allowance; short finite lists finish well below the ceilings, so measured time is not equal consumption or a portable speed claim. The native SourceOnlyGenerator subclasses AutoMLPipelineFeatureGenerator, fits once on source indices and is passed already fitted; the learner transforms its otherwise combined train/tuning frame. Assertions verify its one fit call and all four native model names. No bagging, GPU, dynamic stacking or threshold calibration. Selected manual HGB final Brier0.272414/log loss 0.755003; native weighted ensemble0.249746/0.692315; prevalence0.247287/0.687712. Automation does not beat the prevalence control here. Resource observations are freshly measured outside deterministic RESULTS and retained in actual kernel/export evidence. Three proposed requests then exercise a deterministic role/budget validator: reject final-role fitting, reject 1000 updates over remaining budget, admit a50-update source request. This last step performs no extra fit and executes no language-model agent; AIDE and auto-sklearn are explained from primary sources, not claimed as installed executions.
- **187 / selection and refit:**160 independent buildings with four records each: 120 source/40 locked final. Three outer grouped folds fit 80 and assess 40 buildings; each has three inner grouped folds. Four boosting recipes cross depth2/5 and rate0.05/0.15; every inner fit actually trains 40 trees and examines staged5/15/40 checkpoints. Source-median imputation is fitted separately within each inner fold. All 48 inner fits, including selection on all 120 source buildings, spend 1920 trees; retrospective checkpoint selection is not early-saving computation. Outer labels assess their own selected procedure without selecting it. Final selection reruns inside all source buildings, refits 480 records at the chosen fixed 40-tree count and assesses final buildings once. Mean outer MSE 0.856796; locked-final MSE 0.715585. Different training sizes and data draws prevent attributing their difference solely to bias. Visual A explicitly encloses inner selection inside outer fitting and keeps final assessment outside. A separate 100-study null experiment considers1/8/64 equal-population-risk predictors, using 40 reused and 200 fresh observations. Mean reused minima1.07015/0.94250/0.86280 improve spuriously while fresh errors1.10167/1.10736/1.10226 stay near the common 1.09 population risk.

## Execution, repairs and figure evidence

All five final notebooks execute in fresh kernels using the unchanged runner; all assertions pass, current outputs have no errors or stderr. The first TabPFN hash assertion preceded native inference preparation; it was moved after an explicitly source-only warm-up and rerun. Explicit median imputation repaired defaults that initially used means in 185 and 187. Manual 186 selection was changed from Brier to log loss to match AutoGluon's declared objective, then rerun. An authoring text edit briefly corrupted the 187 builder tail; recovery from its actual saved notebook preceded fresh186/187 runs. Initial failures and preflight logs are retained locally. An early Torch-enabled preflight produced no result JSON and an empty log; a later shell command's exit does not establish that fit's success. Torch-first native preflight and final laboratory 186 do succeed.

Every current code cell reruns in an isolated exporter process, including the dedicated 3.12 process for 186; deterministic scientific RESULTS match kernel summaries exactly. Resource observations are measured anew and not falsely compared as deterministic results. Eleven SVG/vector-PDF/PNG sets reproduce the experiments. Review corrected wrapped diagram text and long axis labels at book size without changing scientific results. Notebook orientations and chapter prose retain fitted-information boundaries, failed controls, native/original distinctions and limited generated-study claims. Chapters 36–43 and the whole-book audit remain required.

## Successful result dictionaries

### code_183

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7683.

```json
{
  "candidate_results": [
    {
      "development_RMSE": 0.8246588849775117,
      "family": "Boost",
      "fitted_parameters": {
        "fitted_trees": 60,
        "source_fitted_rows": 432,
        "transform": "native missing-value routing"
      },
      "source_RMSE": 0.4009852502863363,
      "trial": 0
    },
    {
      "development_RMSE": 0.8197356918286526,
      "family": "Boost",
      "fitted_parameters": {
        "fitted_trees": 60,
        "source_fitted_rows": 432,
        "transform": "native missing-value routing"
      },
      "source_RMSE": 0.6886729268626555,
      "trial": 1
    },
    {
      "development_RMSE": 0.7760164723714518,
      "family": "Boost",
      "fitted_parameters": {
        "fitted_trees": 60,
        "source_fitted_rows": 432,
        "transform": "native missing-value routing"
      },
      "source_RMSE": 0.4660910661786027,
      "trial": 2
    },
    {
      "development_RMSE": 0.7924303206993282,
      "family": "Boost",
      "fitted_parameters": {
        "fitted_trees": 60,
        "source_fitted_rows": 432,
        "transform": "native missing-value routing"
      },
      "source_RMSE": 0.5291424375863846,
      "trial": 3
    },
    {
      "development_RMSE": 0.8037085843407519,
      "family": "Boost",
      "fitted_parameters": {
        "fitted_trees": 60,
        "source_fitted_rows": 432,
        "transform": "native missing-value routing"
      },
      "source_RMSE": 0.7480847884285244,
      "trial": 4
    },
    {
      "development_RMSE": 0.787760612085425,
      "family": "Boost",
      "fitted_parameters": {
        "fitted_trees": 60,
        "source_fitted_rows": 432,
        "transform": "native missing-value routing"
      },
      "source_RMSE": 0.5779317912131623,
      "trial": 5
    },
    {
      "development_RMSE": 0.7680691518191318,
      "family": "Neural",
      "fitted_parameters": {
        "imputer_medians": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "learned_neural_weights": 65,
        "scaler_centre": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "source_fitted_rows": 432,
        "updates": 150
      },
      "source_RMSE": 0.7619618202150923,
      "trial": 6
    },
    {
      "development_RMSE": 0.8421368292327458,
      "family": "Neural",
      "fitted_parameters": {
        "imputer_medians": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "learned_neural_weights": 65,
        "scaler_centre": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "source_fitted_rows": 432,
        "updates": 150
      },
      "source_RMSE": 0.9229459747331812,
      "trial": 7
    },
    {
      "development_RMSE": 0.8480335506173484,
      "family": "Neural",
      "fitted_parameters": {
        "imputer_medians": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "learned_neural_weights": 193,
        "scaler_centre": [
          0.056631472621379325,
          0.10324188070173644,
          0.1004151685728376,
          -2.0523011533834245e-05,
          0.006679119503604249,
          0.013173576337190884
        ],
        "source_fitted_rows": 432,
        "updates": 150
      },
      "source_RMSE": 0.6464751371587968,
      "trial": 8
    },
    {
      "development_RMSE": 0.7731967672543426,
      "family": "Neural",
      "fitted_parameters": {
        "imputer_medians": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "learned_neural_weights": 65,
        "scaler_centre": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "source_fitted_rows": 432,
        "updates": 150
      },
      "source_RMSE": 0.7259765266298045,
      "trial": 9
    },
    {
      "development_RMSE": 0.8491972531999961,
      "family": "Neural",
      "fitted_parameters": {
        "imputer_medians": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "learned_neural_weights": 65,
        "scaler_centre": [
          0.056631472621379325,
          0.10324188070173644,
          0.1004151685728376,
          -2.0523011533834245e-05,
          0.006679119503604249,
          0.013173576337190884
        ],
        "source_fitted_rows": 432,
        "updates": 150
      },
      "source_RMSE": 0.717285838068129,
      "trial": 10
    },
    {
      "development_RMSE": 0.7508530415763432,
      "family": "Neural",
      "fitted_parameters": {
        "imputer_medians": [
          0.09103754511751358,
          0.21078019615416418,
          0.17912011701194078,
          0.035940599356662384,
          0.005292699695975331,
          0.060668705833320395
        ],
        "learned_neural_weights": 65,
        "scaler_centre": [
          0.056631472621379325,
          0.10324188070173644,
          0.1004151685728376,
          -2.0523011533834245e-05,
          0.006679119503604249,
          0.013173576337190884
        ],
        "source_fitted_rows": 432,
        "updates": 150
      },
      "source_RMSE": 0.7342315207429789,
      "trial": 11
    }
  ],
  "configs_drawn_before_scores": [
    {
      "depth": 5,
      "family": "Boost",
      "learning_rate": 0.07515910272997935,
      "min_leaf": 8,
      "missingness": "native",
      "trees": 60
    },
    {
      "depth": 2,
      "family": "Boost",
      "learning_rate": 0.12527763048822718,
      "min_leaf": 8,
      "missingness": "native",
      "trees": 60
    },
    {
      "depth": 3,
      "family": "Boost",
      "learning_rate": 0.14956023734145993,
      "min_leaf": 8,
      "missingness": "native",
      "trees": 60
    },
    {
      "depth": 5,
      "family": "Boost",
      "learning_rate": 0.06409724458800518,
      "min_leaf": 16,
      "missingness": "native",
      "trees": 60
    },
    {
      "depth": 2,
      "family": "Boost",
      "learning_rate": 0.08334689764204377,
      "min_leaf": 8,
      "missingness": "native",
      "trees": 60
    },
    {
      "depth": 3,
      "family": "Boost",
      "learning_rate": 0.08877388716934015,
      "min_leaf": 8,
      "missingness": "native",
      "trees": 60
    },
    {
      "family": "Neural",
      "learning_rate": 0.015360707612275261,
      "scaling": "robust",
      "updates": 150,
      "weight_decay": 2.837497612222862e-05,
      "width": 8
    },
    {
      "family": "Neural",
      "learning_rate": 0.004137377247975194,
      "scaling": "robust",
      "updates": 150,
      "weight_decay": 0.0001086540987230855,
      "width": 8
    },
    {
      "family": "Neural",
      "learning_rate": 0.023233606712797995,
      "scaling": "standard",
      "updates": 150,
      "weight_decay": 0.0006691480346797412,
      "width": 24
    },
    {
      "family": "Neural",
      "learning_rate": 0.027492351664789638,
      "scaling": "robust",
      "updates": 150,
      "weight_decay": 3.8671039388240895e-05,
      "width": 8
    },
    {
      "family": "Neural",
      "learning_rate": 0.02986568417395957,
      "scaling": "standard",
      "updates": 150,
      "weight_decay": 2.500897063594782e-05,
      "width": 8
    },
    {
      "family": "Neural",
      "learning_rate": 0.015437650869736004,
      "scaling": "standard",
      "updates": 150,
      "weight_decay": 2.781525940152356e-05,
      "width": 8
    }
  ],
  "development_added_to_refit": false,
  "development_buildings": 36,
  "final_assessed_candidate_count": 1,
  "final_building_IDs": [
    64,
    45,
    170,
    34,
    166,
    19,
    105,
    86,
    162,
    79,
    152,
    11,
    161,
    132,
    88,
    112,
    29,
    35,
    131,
    143,
    144,
    42,
    49,
    102,
    165,
    18,
    100,
    172,
    139,
    30,
    80,
    94,
    1,
    17,
    74,
    128
  ],
  "final_buildings": 36,
  "group_identity_used_as_feature": false,
  "records_per_building": 4,
  "refit_data": "same source only, same seed and fixed resource",
  "selected_configuration": {
    "family": "Neural",
    "learning_rate": 0.015437650869736004,
    "scaling": "standard",
    "updates": 150,
    "weight_decay": 2.781525940152356e-05,
    "width": 8
  },
  "selected_final_RMSE": 0.916686586568217,
  "selected_trial": 11,
  "selection_rule": "lowest development RMSE; first trial on ties",
  "source_buildings": 108
}
```

### code_184

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7684.

```json
{
  "GP_acquisition_candidate_ids": [
    54,
    24,
    9,
    39,
    16,
    15,
    53,
    56,
    34,
    1,
    37,
    45,
    44,
    60,
    59,
    62
  ],
  "GP_kernel_parameters_fixed": true,
  "PBT_history": [
    {
      "learning_rates": [
        0.0005009966984900764,
        0.00014578241768560193,
        0.0075576460462713135,
        0.0025158955176194714
      ],
      "losses": [
        1.5276416067916028,
        1.544607748284166,
        1.1914610443451439,
        1.4346048822726611
      ],
      "updates_per_slot": 9
    },
    {
      "learning_rates": [
        0.0005009966984900764,
        0.006046116837017051,
        0.0075576460462713135,
        0.0025158955176194714
      ],
      "losses": [
        1.5034829692998997,
        0.9518303913924108,
        0.9032451949686299,
        1.3190253939712475
      ],
      "updates_per_slot": 18
    },
    {
      "learning_rates": [
        0.006046116837017051,
        0.006046116837017051,
        0.0075576460462713135,
        0.0025158955176194714
      ],
      "losses": [
        0.7659862137829764,
        0.7905377732214417,
        0.7460019663629981,
        1.2054515758963895
      ],
      "updates_per_slot": 27
    },
    {
      "learning_rates": [
        0.006046116837017051,
        0.006046116837017051,
        0.0075576460462713135,
        0.006046116837017051
      ],
      "losses": [
        0.7200990518158429,
        0.7244012736015802,
        0.7125236972625267,
        0.715699733996708
      ],
      "updates_per_slot": 36
    },
    {
      "learning_rates": [
        0.006046116837017051,
        0.009069175255525575,
        0.0075576460462713135,
        0.006046116837017051
      ],
      "losses": [
        0.7326247308167989,
        0.7471915155594475,
        0.741937452430265,
        0.7366933741127561
      ],
      "updates_per_slot": 45
    },
    {
      "learning_rates": [
        0.006046116837017051,
        0.0072553402044204605,
        0.0075576460462713135,
        0.006046116837017051
      ],
      "losses": [
        0.7528001364032176,
        0.7548494614311198,
        0.7557901073095389,
        0.7552922498036377
      ],
      "updates_per_slot": 54
    },
    {
      "learning_rates": [
        0.006046116837017051,
        0.0072553402044204605,
        0.0048368934696136415,
        0.006046116837017051
      ],
      "losses": [
        0.7489847785830862,
        0.7444071953060011,
        0.7497168043602412,
        0.747272601040397
      ],
      "updates_per_slot": 63
    },
    {
      "learning_rates": [
        0.006046116837017051,
        0.0072553402044204605,
        0.0058042721635363686,
        0.006046116837017051
      ],
      "losses": [
        0.7250896293137794,
        0.7085681217563696,
        0.7164234360816311,
        0.7200004493248006
      ],
      "updates_per_slot": 72
    },
    {
      "learning_rates": [
        0.0058042721635363686,
        0.0072553402044204605,
        0.0058042721635363686,
        0.006046116837017051
      ],
      "losses": [
        0.6677628434181629,
        0.656219469956635,
        0.6772403037232001,
        0.6825734694098676
      ],
      "updates_per_slot": 81
    },
    {
      "learning_rates": [
        0.0058042721635363686,
        0.0072553402044204605,
        0.0058042721635363686,
        0.0058042721635363686
      ],
      "losses": [
        0.6136638343529028,
        0.5856453755809222,
        0.6258125599040799,
        0.6003747797408568
      ],
      "updates_per_slot": 90
    },
    {
      "learning_rates": [
        0.0058042721635363686,
        0.0072553402044204605,
        0.008706408245304552,
        0.0058042721635363686
      ],
      "losses": [
        0.5539865700374208,
        0.5110854201360451,
        0.4963174560809956,
        0.5403148078608688
      ],
      "updates_per_slot": 99
    },
    {
      "learning_rates": [
        0.006965126596243642,
        0.0072553402044204605,
        0.008706408245304552,
        0.0058042721635363686
      ],
      "losses": [
        0.4301921206811197,
        0.44188638916171347,
        0.4156744558668934,
        0.4831527703294967
      ],
      "updates_per_slot": 108
    }
  ],
  "PBT_selected_slot": 2,
  "PBT_state_transfers": [
    {
      "at_updates": 9,
      "donor": 2,
      "new_learning_rate": 0.006046116837017051,
      "new_weight_decay": 0.00818610569684152,
      "recipient": 1
    },
    {
      "at_updates": 18,
      "donor": 2,
      "new_learning_rate": 0.006046116837017051,
      "new_weight_decay": 0.01227915854526228,
      "recipient": 0
    },
    {
      "at_updates": 27,
      "donor": 2,
      "new_learning_rate": 0.006046116837017051,
      "new_weight_decay": 0.01227915854526228,
      "recipient": 3
    },
    {
      "at_updates": 36,
      "donor": 2,
      "new_learning_rate": 0.009069175255525575,
      "new_weight_decay": 0.01227915854526228,
      "recipient": 1
    },
    {
      "at_updates": 45,
      "donor": 0,
      "new_learning_rate": 0.0072553402044204605,
      "new_weight_decay": 0.009823326836209824,
      "recipient": 1
    },
    {
      "at_updates": 54,
      "donor": 0,
      "new_learning_rate": 0.0048368934696136415,
      "new_weight_decay": 0.009823326836209824,
      "recipient": 2
    },
    {
      "at_updates": 63,
      "donor": 1,
      "new_learning_rate": 0.0058042721635363686,
      "new_weight_decay": 0.011787992203451789,
      "recipient": 2
    },
    {
      "at_updates": 72,
      "donor": 1,
      "new_learning_rate": 0.0058042721635363686,
      "new_weight_decay": 0.011787992203451789,
      "recipient": 0
    },
    {
      "at_updates": 81,
      "donor": 1,
      "new_learning_rate": 0.0058042721635363686,
      "new_weight_decay": 0.011787992203451789,
      "recipient": 3
    },
    {
      "at_updates": 90,
      "donor": 1,
      "new_learning_rate": 0.008706408245304552,
      "new_weight_decay": 0.007858661468967859,
      "recipient": 2
    },
    {
      "at_updates": 99,
      "donor": 2,
      "new_learning_rate": 0.006965126596243642,
      "new_weight_decay": 0.0062869291751742875,
      "recipient": 0
    }
  ],
  "PBT_updates": 432,
  "actual_update_costs": {
    "GP EI": 432,
    "Halving": 432,
    "Hyperband": 423,
    "Random": 432
  },
  "building_roles": [
    36,
    12,
    12
  ],
  "common_search_ceiling": 432,
  "final_assessments": [
    {
      "final_RMSE": 1.4631580144250977,
      "method": "Random",
      "search_update_cost": 432,
      "selected_candidate": 37
    },
    {
      "final_RMSE": 1.4631580144250977,
      "method": "GP EI",
      "search_update_cost": 432,
      "selected_candidate": 37
    },
    {
      "final_RMSE": 1.3823255409709647,
      "method": "Halving",
      "search_update_cost": 432,
      "selected_candidate": 7
    },
    {
      "final_RMSE": 1.3823255409709647,
      "method": "Hyperband",
      "search_update_cost": 423,
      "selected_candidate": 7
    },
    {
      "final_RMSE": 1.552595145413988,
      "method": "PBT schedule",
      "search_update_cost": 432,
      "selected_candidate": 2
    }
  ],
  "final_used_for_search": false,
  "hyperband_brackets": [
    {
      "actual_cost": 108,
      "initial_updates": 1,
      "n": 27,
      "s": 3
    },
    {
      "actual_cost": 99,
      "initial_updates": 3,
      "n": 12,
      "s": 2
    },
    {
      "actual_cost": 108,
      "initial_updates": 9,
      "n": 6,
      "s": 1
    },
    {
      "actual_cost": 108,
      "initial_updates": 27,
      "n": 4,
      "s": 0
    }
  ],
  "records_per_building": 4,
  "selected_static_candidates": {
    "GP EI": 37,
    "Halving": 7,
    "Hyperband": 7,
    "Random": 37
  },
  "static_horizon_equals_PBT_horizon": false,
  "static_maximum_updates": 27,
  "static_search_records": {
    "GP EI": [
      {
        "bracket": 0,
        "candidate": 54,
        "cumulative_updates": 27,
        "loss": 1.4440440598436899,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 24,
        "cumulative_updates": 54,
        "loss": 0.7313636346685547,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 9,
        "cumulative_updates": 81,
        "loss": 1.2054515758963895,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 39,
        "cumulative_updates": 108,
        "loss": 0.45157200112353113,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 16,
        "cumulative_updates": 135,
        "loss": 0.4625088029320754,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 15,
        "cumulative_updates": 162,
        "loss": 0.4156947758983289,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 53,
        "cumulative_updates": 189,
        "loss": 0.4621237448945306,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 216,
        "loss": 0.5606252461381406,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 34,
        "cumulative_updates": 243,
        "loss": 0.5535020828318479,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 1,
        "cumulative_updates": 270,
        "loss": 0.727829608395875,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 37,
        "cumulative_updates": 297,
        "loss": 0.3763249216900293,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 45,
        "cumulative_updates": 324,
        "loss": 0.725947496732517,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 44,
        "cumulative_updates": 351,
        "loss": 1.4210603680294074,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 60,
        "cumulative_updates": 378,
        "loss": 1.5268955060305416,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 59,
        "cumulative_updates": 405,
        "loss": 0.6980942717506862,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 62,
        "cumulative_updates": 432,
        "loss": 0.6060944864652579,
        "rung": 0,
        "updates": 27
      }
    ],
    "Halving": [
      {
        "bracket": 0,
        "candidate": 60,
        "cumulative_updates": 1,
        "loss": 1.550700305383396,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 5,
        "cumulative_updates": 2,
        "loss": 1.5431301057128415,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 6,
        "cumulative_updates": 3,
        "loss": 1.5081606886099987,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 26,
        "cumulative_updates": 4,
        "loss": 1.5384625793739106,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 23,
        "cumulative_updates": 5,
        "loss": 1.5433326487305414,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 43,
        "cumulative_updates": 6,
        "loss": 1.516774614158144,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 49,
        "cumulative_updates": 7,
        "loss": 1.5504450717476381,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 48,
        "cumulative_updates": 8,
        "loss": 1.5431412565504379,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 35,
        "cumulative_updates": 9,
        "loss": 1.5317318820161894,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 34,
        "cumulative_updates": 10,
        "loss": 1.3787448040371153,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 32,
        "cumulative_updates": 11,
        "loss": 1.3621807770049328,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 36,
        "cumulative_updates": 12,
        "loss": 1.5375262103003289,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 31,
        "cumulative_updates": 13,
        "loss": 1.5460491680953856,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 58,
        "cumulative_updates": 14,
        "loss": 1.5504070594008097,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 46,
        "cumulative_updates": 15,
        "loss": 1.4156570317937007,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 51,
        "cumulative_updates": 16,
        "loss": 1.550267282877272,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 52,
        "cumulative_updates": 17,
        "loss": 1.5189684197935414,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 28,
        "cumulative_updates": 18,
        "loss": 1.5083721717745224,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 11,
        "cumulative_updates": 19,
        "loss": 1.5287697735642496,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 20,
        "loss": 1.1244683129651492,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 2,
        "cumulative_updates": 21,
        "loss": 1.5484982871119788,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 39,
        "cumulative_updates": 22,
        "loss": 1.3124695151584602,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 8,
        "cumulative_updates": 23,
        "loss": 1.4184687669133507,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 54,
        "cumulative_updates": 24,
        "loss": 1.5477216999911196,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 44,
        "cumulative_updates": 25,
        "loss": 1.5469138115151457,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 59,
        "cumulative_updates": 26,
        "loss": 1.4959538216518478,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 38,
        "cumulative_updates": 27,
        "loss": 1.5491445084566777,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 30,
        "loss": 0.722827951988426,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 39,
        "cumulative_updates": 33,
        "loss": 0.8748621271310979,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 32,
        "cumulative_updates": 36,
        "loss": 0.979284901077985,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 34,
        "cumulative_updates": 39,
        "loss": 1.0391282993772204,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 46,
        "cumulative_updates": 42,
        "loss": 1.130373783737886,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 8,
        "cumulative_updates": 45,
        "loss": 1.143368245664722,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 59,
        "cumulative_updates": 48,
        "loss": 1.3779501180783391,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 6,
        "cumulative_updates": 51,
        "loss": 1.4171241784394377,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 28,
        "cumulative_updates": 54,
        "loss": 1.4176666487895602,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 63,
        "loss": 0.7295456750818502,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 0,
        "candidate": 39,
        "cumulative_updates": 72,
        "loss": 0.6741835172873127,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 0,
        "candidate": 32,
        "cumulative_updates": 81,
        "loss": 0.6781403727124159,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 0,
        "candidate": 39,
        "cumulative_updates": 108,
        "loss": 0.45157200112353113,
        "rung": 3,
        "updates": 27
      },
      {
        "bracket": 1,
        "candidate": 50,
        "cumulative_updates": 109,
        "loss": 1.5503280438913922,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 37,
        "cumulative_updates": 110,
        "loss": 1.2145171911485024,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 1,
        "cumulative_updates": 111,
        "loss": 1.447282645169949,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 30,
        "cumulative_updates": 112,
        "loss": 1.5508158749239815,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 23,
        "cumulative_updates": 113,
        "loss": 1.5433326487305414,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 7,
        "cumulative_updates": 114,
        "loss": 1.275444891852888,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 24,
        "cumulative_updates": 115,
        "loss": 1.5087108988177393,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 36,
        "cumulative_updates": 116,
        "loss": 1.5375262103003289,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 62,
        "cumulative_updates": 117,
        "loss": 1.3929881741724157,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 32,
        "cumulative_updates": 118,
        "loss": 1.3621807770049328,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 33,
        "cumulative_updates": 119,
        "loss": 1.2645451159471108,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 26,
        "cumulative_updates": 120,
        "loss": 1.5384625793739106,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 2,
        "cumulative_updates": 121,
        "loss": 1.5484982871119788,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 57,
        "cumulative_updates": 122,
        "loss": 1.5393302950102863,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 0,
        "cumulative_updates": 123,
        "loss": 1.54601058126974,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 9,
        "cumulative_updates": 124,
        "loss": 1.5392612684674971,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 44,
        "cumulative_updates": 125,
        "loss": 1.5469138115151457,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 52,
        "cumulative_updates": 126,
        "loss": 1.5189684197935414,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 53,
        "cumulative_updates": 127,
        "loss": 1.224307006800289,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 25,
        "cumulative_updates": 128,
        "loss": 1.5430882568673967,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 21,
        "cumulative_updates": 129,
        "loss": 1.5262953502499268,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 5,
        "cumulative_updates": 130,
        "loss": 1.5431301057128415,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 49,
        "cumulative_updates": 131,
        "loss": 1.5504450717476381,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 39,
        "cumulative_updates": 132,
        "loss": 1.3124695151584602,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 3,
        "cumulative_updates": 133,
        "loss": 1.5507589768869714,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 22,
        "cumulative_updates": 134,
        "loss": 1.5299969343861983,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 4,
        "cumulative_updates": 135,
        "loss": 1.4040406076016998,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 1,
        "candidate": 37,
        "cumulative_updates": 138,
        "loss": 0.7478814670014766,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 53,
        "cumulative_updates": 141,
        "loss": 0.7690005451158145,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 33,
        "cumulative_updates": 144,
        "loss": 0.7930661188786745,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 7,
        "cumulative_updates": 147,
        "loss": 0.8290121543010812,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 39,
        "cumulative_updates": 150,
        "loss": 0.8748621271310979,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 32,
        "cumulative_updates": 153,
        "loss": 0.979284901077985,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 62,
        "cumulative_updates": 156,
        "loss": 1.0756033445629107,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 4,
        "cumulative_updates": 159,
        "loss": 1.1023393440138236,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 1,
        "cumulative_updates": 162,
        "loss": 1.2273382550375618,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 37,
        "cumulative_updates": 171,
        "loss": 0.7762703197989129,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 53,
        "cumulative_updates": 180,
        "loss": 0.6965742347412195,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 33,
        "cumulative_updates": 189,
        "loss": 0.7125182148757668,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 53,
        "cumulative_updates": 216,
        "loss": 0.4621237448945306,
        "rung": 3,
        "updates": 27
      },
      {
        "bracket": 2,
        "candidate": 40,
        "cumulative_updates": 217,
        "loss": 1.549717775726051,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 11,
        "cumulative_updates": 218,
        "loss": 1.5287697735642496,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 29,
        "cumulative_updates": 219,
        "loss": 1.5429733685249911,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 54,
        "cumulative_updates": 220,
        "loss": 1.5477216999911196,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 33,
        "cumulative_updates": 221,
        "loss": 1.2645451159471108,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 19,
        "cumulative_updates": 222,
        "loss": 1.5469387948928037,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 5,
        "cumulative_updates": 223,
        "loss": 1.5431301057128415,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 9,
        "cumulative_updates": 224,
        "loss": 1.5392612684674971,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 52,
        "cumulative_updates": 225,
        "loss": 1.5189684197935414,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 60,
        "cumulative_updates": 226,
        "loss": 1.550700305383396,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 42,
        "cumulative_updates": 227,
        "loss": 1.4655224036587773,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 8,
        "cumulative_updates": 228,
        "loss": 1.4184687669133507,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 3,
        "cumulative_updates": 229,
        "loss": 1.5507589768869714,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 28,
        "cumulative_updates": 230,
        "loss": 1.5083721717745224,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 61,
        "cumulative_updates": 231,
        "loss": 1.5417257334809236,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 32,
        "cumulative_updates": 232,
        "loss": 1.3621807770049328,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 14,
        "cumulative_updates": 233,
        "loss": 1.5271590389738592,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 44,
        "cumulative_updates": 234,
        "loss": 1.5469138115151457,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 62,
        "cumulative_updates": 235,
        "loss": 1.3929881741724157,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 7,
        "cumulative_updates": 236,
        "loss": 1.275444891852888,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 22,
        "cumulative_updates": 237,
        "loss": 1.5299969343861983,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 41,
        "cumulative_updates": 238,
        "loss": 1.5509989073897803,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 57,
        "cumulative_updates": 239,
        "loss": 1.5393302950102863,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 43,
        "cumulative_updates": 240,
        "loss": 1.516774614158144,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 20,
        "cumulative_updates": 241,
        "loss": 1.4740793797713554,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 39,
        "cumulative_updates": 242,
        "loss": 1.3124695151584602,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 0,
        "cumulative_updates": 243,
        "loss": 1.54601058126974,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 2,
        "candidate": 33,
        "cumulative_updates": 246,
        "loss": 0.7930661188786745,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 7,
        "cumulative_updates": 249,
        "loss": 0.8290121543010812,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 39,
        "cumulative_updates": 252,
        "loss": 0.8748621271310979,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 32,
        "cumulative_updates": 255,
        "loss": 0.979284901077985,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 62,
        "cumulative_updates": 258,
        "loss": 1.0756033445629107,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 8,
        "cumulative_updates": 261,
        "loss": 1.143368245664722,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 42,
        "cumulative_updates": 264,
        "loss": 1.2825187876163764,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 20,
        "cumulative_updates": 267,
        "loss": 1.3096371558124886,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 28,
        "cumulative_updates": 270,
        "loss": 1.4176666487895602,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 2,
        "candidate": 33,
        "cumulative_updates": 279,
        "loss": 0.7125182148757668,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 7,
        "cumulative_updates": 288,
        "loss": 0.6674142475145358,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 39,
        "cumulative_updates": 297,
        "loss": 0.6741835172873127,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 7,
        "cumulative_updates": 324,
        "loss": 0.4310350325682733,
        "rung": 3,
        "updates": 27
      },
      {
        "bracket": 3,
        "candidate": 33,
        "cumulative_updates": 325,
        "loss": 1.2645451159471108,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 26,
        "cumulative_updates": 326,
        "loss": 1.5384625793739106,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 1,
        "cumulative_updates": 327,
        "loss": 1.447282645169949,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 60,
        "cumulative_updates": 328,
        "loss": 1.550700305383396,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 30,
        "cumulative_updates": 329,
        "loss": 1.5508158749239815,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 45,
        "cumulative_updates": 330,
        "loss": 1.389632856197695,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 43,
        "cumulative_updates": 331,
        "loss": 1.516774614158144,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 25,
        "cumulative_updates": 332,
        "loss": 1.5430882568673967,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 44,
        "cumulative_updates": 333,
        "loss": 1.5469138115151457,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 14,
        "cumulative_updates": 334,
        "loss": 1.5271590389738592,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 55,
        "cumulative_updates": 335,
        "loss": 1.5506902925999413,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 4,
        "cumulative_updates": 336,
        "loss": 1.4040406076016998,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 53,
        "cumulative_updates": 337,
        "loss": 1.224307006800289,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 36,
        "cumulative_updates": 338,
        "loss": 1.5375262103003289,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 54,
        "cumulative_updates": 339,
        "loss": 1.5477216999911196,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 17,
        "cumulative_updates": 340,
        "loss": 1.548668811654176,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 39,
        "cumulative_updates": 341,
        "loss": 1.3124695151584602,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 12,
        "cumulative_updates": 342,
        "loss": 1.5489203434651342,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 49,
        "cumulative_updates": 343,
        "loss": 1.5504450717476381,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 56,
        "cumulative_updates": 344,
        "loss": 1.1244683129651492,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 11,
        "cumulative_updates": 345,
        "loss": 1.5287697735642496,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 2,
        "cumulative_updates": 346,
        "loss": 1.5484982871119788,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 13,
        "cumulative_updates": 347,
        "loss": 1.220405952104851,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 10,
        "cumulative_updates": 348,
        "loss": 1.543542857030139,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 31,
        "cumulative_updates": 349,
        "loss": 1.5460491680953856,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 42,
        "cumulative_updates": 350,
        "loss": 1.4655224036587773,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 3,
        "cumulative_updates": 351,
        "loss": 1.5507589768869714,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 3,
        "candidate": 56,
        "cumulative_updates": 354,
        "loss": 0.722827951988426,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 13,
        "cumulative_updates": 357,
        "loss": 0.7657198144170779,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 53,
        "cumulative_updates": 360,
        "loss": 0.7690005451158145,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 33,
        "cumulative_updates": 363,
        "loss": 0.7930661188786745,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 39,
        "cumulative_updates": 366,
        "loss": 0.8748621271310979,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 45,
        "cumulative_updates": 369,
        "loss": 1.0499939177783817,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 4,
        "cumulative_updates": 372,
        "loss": 1.1023393440138236,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 1,
        "cumulative_updates": 375,
        "loss": 1.2273382550375618,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 42,
        "cumulative_updates": 378,
        "loss": 1.2825187876163764,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 3,
        "candidate": 56,
        "cumulative_updates": 387,
        "loss": 0.7295456750818502,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 3,
        "candidate": 13,
        "cumulative_updates": 396,
        "loss": 0.699194461918852,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 3,
        "candidate": 53,
        "cumulative_updates": 405,
        "loss": 0.6965742347412195,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 3,
        "candidate": 53,
        "cumulative_updates": 432,
        "loss": 0.4621237448945306,
        "rung": 3,
        "updates": 27
      }
    ],
    "Hyperband": [
      {
        "bracket": 0,
        "candidate": 10,
        "cumulative_updates": 1,
        "loss": 1.543542857030139,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 21,
        "cumulative_updates": 2,
        "loss": 1.5262953502499268,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 51,
        "cumulative_updates": 3,
        "loss": 1.550267282877272,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 12,
        "cumulative_updates": 4,
        "loss": 1.5489203434651342,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 58,
        "cumulative_updates": 5,
        "loss": 1.5504070594008097,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 9,
        "cumulative_updates": 6,
        "loss": 1.5392612684674971,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 13,
        "cumulative_updates": 7,
        "loss": 1.220405952104851,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 59,
        "cumulative_updates": 8,
        "loss": 1.4959538216518478,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 29,
        "cumulative_updates": 9,
        "loss": 1.5429733685249911,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 33,
        "cumulative_updates": 10,
        "loss": 1.2645451159471108,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 7,
        "cumulative_updates": 11,
        "loss": 1.275444891852888,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 12,
        "loss": 1.1244683129651492,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 27,
        "cumulative_updates": 13,
        "loss": 1.5475201501954967,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 14,
        "cumulative_updates": 14,
        "loss": 1.5271590389738592,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 57,
        "cumulative_updates": 15,
        "loss": 1.5393302950102863,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 30,
        "cumulative_updates": 16,
        "loss": 1.5508158749239815,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 42,
        "cumulative_updates": 17,
        "loss": 1.4655224036587773,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 47,
        "cumulative_updates": 18,
        "loss": 1.533215993715079,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 44,
        "cumulative_updates": 19,
        "loss": 1.5469138115151457,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 46,
        "cumulative_updates": 20,
        "loss": 1.4156570317937007,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 16,
        "cumulative_updates": 21,
        "loss": 1.2389032359337822,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 61,
        "cumulative_updates": 22,
        "loss": 1.5417257334809236,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 11,
        "cumulative_updates": 23,
        "loss": 1.5287697735642496,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 3,
        "cumulative_updates": 24,
        "loss": 1.5507589768869714,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 37,
        "cumulative_updates": 25,
        "loss": 1.2145171911485024,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 25,
        "cumulative_updates": 26,
        "loss": 1.5430882568673967,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 43,
        "cumulative_updates": 27,
        "loss": 1.516774614158144,
        "rung": 0,
        "updates": 1
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 30,
        "loss": 0.722827951988426,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 37,
        "cumulative_updates": 33,
        "loss": 0.7478814670014766,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 13,
        "cumulative_updates": 36,
        "loss": 0.7657198144170779,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 16,
        "cumulative_updates": 39,
        "loss": 0.7808952216670946,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 33,
        "cumulative_updates": 42,
        "loss": 0.7930661188786745,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 7,
        "cumulative_updates": 45,
        "loss": 0.8290121543010812,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 46,
        "cumulative_updates": 48,
        "loss": 1.130373783737886,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 42,
        "cumulative_updates": 51,
        "loss": 1.2825187876163764,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 59,
        "cumulative_updates": 54,
        "loss": 1.3779501180783391,
        "rung": 1,
        "updates": 3
      },
      {
        "bracket": 0,
        "candidate": 56,
        "cumulative_updates": 63,
        "loss": 0.7295456750818502,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 0,
        "candidate": 37,
        "cumulative_updates": 72,
        "loss": 0.7762703197989129,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 0,
        "candidate": 13,
        "cumulative_updates": 81,
        "loss": 0.699194461918852,
        "rung": 2,
        "updates": 9
      },
      {
        "bracket": 0,
        "candidate": 13,
        "cumulative_updates": 108,
        "loss": 0.46323099276377233,
        "rung": 3,
        "updates": 27
      },
      {
        "bracket": 1,
        "candidate": 5,
        "cumulative_updates": 111,
        "loss": 1.5261668983756238,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 48,
        "cumulative_updates": 114,
        "loss": 1.5262014723174833,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 37,
        "cumulative_updates": 117,
        "loss": 0.7478814670014766,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 19,
        "cumulative_updates": 120,
        "loss": 1.537634887569535,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 56,
        "cumulative_updates": 123,
        "loss": 0.722827951988426,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 28,
        "cumulative_updates": 126,
        "loss": 1.4176666487895602,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 9,
        "cumulative_updates": 129,
        "loss": 1.5144534345443195,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 16,
        "cumulative_updates": 132,
        "loss": 0.7808952216670946,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 46,
        "cumulative_updates": 135,
        "loss": 1.130373783737886,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 51,
        "cumulative_updates": 138,
        "loss": 1.5476187800098684,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 4,
        "cumulative_updates": 141,
        "loss": 1.1023393440138236,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 21,
        "cumulative_updates": 144,
        "loss": 1.473479334241097,
        "rung": 0,
        "updates": 3
      },
      {
        "bracket": 1,
        "candidate": 56,
        "cumulative_updates": 153,
        "loss": 0.7295456750818502,
        "rung": 1,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 37,
        "cumulative_updates": 162,
        "loss": 0.7762703197989129,
        "rung": 1,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 16,
        "cumulative_updates": 171,
        "loss": 0.6868393871108673,
        "rung": 1,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 4,
        "cumulative_updates": 180,
        "loss": 0.7091737582681876,
        "rung": 1,
        "updates": 9
      },
      {
        "bracket": 1,
        "candidate": 16,
        "cumulative_updates": 207,
        "loss": 0.4625088029320754,
        "rung": 2,
        "updates": 27
      },
      {
        "bracket": 2,
        "candidate": 0,
        "cumulative_updates": 216,
        "loss": 1.5010764445773812,
        "rung": 0,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 7,
        "cumulative_updates": 225,
        "loss": 0.6674142475145358,
        "rung": 0,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 63,
        "cumulative_updates": 234,
        "loss": 1.1914610443451439,
        "rung": 0,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 19,
        "cumulative_updates": 243,
        "loss": 1.509451973085601,
        "rung": 0,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 55,
        "cumulative_updates": 252,
        "loss": 1.5434776914273272,
        "rung": 0,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 28,
        "cumulative_updates": 261,
        "loss": 1.1654084859285796,
        "rung": 0,
        "updates": 9
      },
      {
        "bracket": 2,
        "candidate": 7,
        "cumulative_updates": 288,
        "loss": 0.4310350325682733,
        "rung": 1,
        "updates": 27
      },
      {
        "bracket": 2,
        "candidate": 28,
        "cumulative_updates": 315,
        "loss": 0.7300227157238629,
        "rung": 1,
        "updates": 27
      },
      {
        "bracket": 3,
        "candidate": 32,
        "cumulative_updates": 342,
        "loss": 0.7043554557047805,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 3,
        "candidate": 57,
        "cumulative_updates": 369,
        "loss": 1.2164602663831519,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 3,
        "candidate": 6,
        "cumulative_updates": 396,
        "loss": 0.7291277253151387,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 3,
        "candidate": 2,
        "cumulative_updates": 423,
        "loss": 1.4659017696773604,
        "rung": 0,
        "updates": 27
      }
    ],
    "Random": [
      {
        "bracket": 0,
        "candidate": 54,
        "cumulative_updates": 27,
        "loss": 1.4440440598436899,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 24,
        "cumulative_updates": 54,
        "loss": 0.7313636346685547,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 9,
        "cumulative_updates": 81,
        "loss": 1.2054515758963895,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 39,
        "cumulative_updates": 108,
        "loss": 0.45157200112353113,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 34,
        "cumulative_updates": 135,
        "loss": 0.5535020828318479,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 55,
        "cumulative_updates": 162,
        "loss": 1.5270866621928167,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 37,
        "cumulative_updates": 189,
        "loss": 0.3763249216900293,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 31,
        "cumulative_updates": 216,
        "loss": 1.3970395230260468,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 8,
        "cumulative_updates": 243,
        "loss": 0.7043100552618554,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 60,
        "cumulative_updates": 270,
        "loss": 1.5268955060305416,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 23,
        "cumulative_updates": 297,
        "loss": 1.3227607750504988,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 27,
        "cumulative_updates": 324,
        "loss": 1.436913877032395,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 19,
        "cumulative_updates": 351,
        "loss": 1.4217593303355198,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 16,
        "cumulative_updates": 378,
        "loss": 0.4625088029320754,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 7,
        "cumulative_updates": 405,
        "loss": 0.4310350325682733,
        "rung": 0,
        "updates": 27
      },
      {
        "bracket": 0,
        "candidate": 10,
        "cumulative_updates": 432,
        "loss": 1.3287621431241423,
        "rung": 0,
        "updates": 27
      }
    ]
  },
  "winner_eligibility": "27-update evaluations only; declared adaptation of Hyperband return rule"
}
```

### code_185

Versions: `{"huggingface-hub": "1.33.0", "matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "tabpfn": "9.2.0", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7685.

```json
{
  "all_attempts": [
    {
      "candidate": "Linear screen",
      "configuration": {
        "C": 1.0,
        "representation": "raw four fields"
      },
      "development_Brier": 0.20238735495223076,
      "family": "Linear",
      "stage": "screen"
    },
    {
      "candidate": "Tree screen",
      "configuration": {
        "leaves": 7,
        "trees": 60
      },
      "development_Brier": 0.21244039618082025,
      "family": "Tree",
      "stage": "screen"
    },
    {
      "candidate": "Neural screen",
      "configuration": {
        "architecture": [
          4,
          8,
          1
        ],
        "updates": 200,
        "weights": 49
      },
      "development_Brier": 0.256309152710877,
      "family": "Neural",
      "stage": "screen"
    },
    {
      "candidate": "TabPFN v2 screen",
      "configuration": {
        "checkpoint_sha256": "cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49",
        "ensemble_members": 1,
        "gradient_updates": 0,
        "pretrained_parameters": 7244554
      },
      "development_Brier": 0.19820962846279144,
      "family": "TabPFN v2",
      "stage": "screen"
    },
    {
      "candidate": "TabPFN v2 expanded",
      "configuration": {
        "checkpoint_sha256": "cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49",
        "ensemble_members": 4,
        "gradient_updates": 0,
        "pretrained_parameters": 7244554
      },
      "development_Brier": 0.20173592865467072,
      "family": "TabPFN v2",
      "stage": "expanded"
    },
    {
      "candidate": "Linear expanded",
      "configuration": {
        "C": 0.1,
        "representation": "quadratic interactions"
      },
      "development_Brier": 0.20188143797020644,
      "family": "Linear",
      "stage": "expanded"
    }
  ],
  "building_roles": [
    32,
    16,
    16
  ],
  "checkpoint_bytes": 29009539,
  "checkpoint_filename": "tabpfn-v2-classifier-v2_default.ckpt",
  "checkpoint_repository": "Prior-Labs/TabPFN-v2-clf",
  "checkpoint_revision": "f851f2a3c941544733b712d8c0f96dfae9b28862",
  "checkpoint_sha256": "cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49",
  "ensemble_members": [
    "TabPFN v2 screen",
    "TabPFN v2 expanded"
  ],
  "ensemble_weight_first": 1.0,
  "ensemble_weights_fit_role": "development only",
  "final_assessments": [
    {
      "final_Brier": 0.2401917278766632,
      "final_log_loss": 0.6662309765815735,
      "method": "Selected single"
    },
    {
      "final_Brier": 0.2401917278766632,
      "final_log_loss": 0.6662309765815735,
      "method": "Development ensemble"
    },
    {
      "final_Brier": 0.24800781249999998,
      "final_log_loss": 0.6891611012872539,
      "method": "Source prevalence"
    }
  ],
  "final_used_for_selection": false,
  "pretrained_weights_unchanged": true,
  "records_per_building": 5,
  "screen_candidates": [
    {
      "candidate": "Linear screen",
      "configuration": {
        "C": 1.0,
        "representation": "raw four fields"
      },
      "development_Brier": 0.20238735495223076,
      "family": "Linear",
      "stage": "screen"
    },
    {
      "candidate": "Tree screen",
      "configuration": {
        "leaves": 7,
        "trees": 60
      },
      "development_Brier": 0.21244039618082025,
      "family": "Tree",
      "stage": "screen"
    },
    {
      "candidate": "Neural screen",
      "configuration": {
        "architecture": [
          4,
          8,
          1
        ],
        "updates": 200,
        "weights": 49
      },
      "development_Brier": 0.256309152710877,
      "family": "Neural",
      "stage": "screen"
    },
    {
      "candidate": "TabPFN v2 screen",
      "configuration": {
        "checkpoint_sha256": "cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49",
        "ensemble_members": 1,
        "gradient_updates": 0,
        "pretrained_parameters": 7244554
      },
      "development_Brier": 0.19820962846279144,
      "family": "TabPFN v2",
      "stage": "screen"
    }
  ],
  "selected_single": "TabPFN v2 screen",
  "shortlisted_families": [
    "TabPFN v2",
    "Linear"
  ],
  "upstream_pretraining_compute_equal": false
}
```

### code_186

Versions: `{"autogluon.tabular": "1.6.3", "lightgbm": "4.7.0", "matplotlib": "3.11.2", "numpy": "2.5.4", "pandas": "2.3.3", "python": "3.12.13", "scikit-learn": "1.9.1", "scipy": "1.18.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7686.

```json
{
  "CPU_count": 1,
  "GPU_count": 0,
  "budget_ceiling_seconds": 15.0,
  "building_roles": [
    72,
    24,
    24
  ],
  "feature_generator_fit_calls": 1,
  "feature_generator_fit_rows": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    82,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
    123,
    124,
    125,
    126,
    127,
    128,
    129,
    130,
    131,
    132,
    133,
    134,
    135,
    136,
    137,
    138,
    139,
    140,
    141,
    142,
    143,
    144,
    145,
    146,
    147,
    148,
    149,
    150,
    151,
    152,
    153,
    154,
    155,
    156,
    157,
    158,
    159,
    160,
    161,
    162,
    163,
    164,
    165,
    166,
    167,
    168,
    169,
    170,
    171,
    172,
    173,
    174,
    175,
    176,
    177,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    185,
    186,
    187,
    188,
    189,
    190,
    191,
    192,
    193,
    194,
    195,
    196,
    197,
    198,
    199,
    200,
    201,
    202,
    203,
    204,
    205,
    206,
    207,
    208,
    209,
    210,
    211,
    212,
    213,
    214,
    215,
    216,
    217,
    218,
    219,
    220,
    221,
    222,
    223,
    224,
    225,
    226,
    227,
    228,
    229,
    230,
    231,
    232,
    233,
    234,
    235,
    236,
    237,
    238,
    239,
    240,
    241,
    242,
    243,
    244,
    245,
    246,
    247,
    248,
    249,
    250,
    251,
    252,
    253,
    254,
    255,
    256,
    257,
    258,
    259,
    260,
    261,
    262,
    263,
    264,
    265,
    266,
    267,
    268,
    269,
    270,
    271,
    272,
    273,
    274,
    275,
    276,
    277,
    278,
    279,
    280,
    281,
    282,
    283,
    284,
    285,
    286,
    287
  ],
  "feature_generator_source_only": true,
  "final_assessments": [
    {
      "final_Brier": 0.2724144321917368,
      "final_log_loss": 0.7550031217707712,
      "workflow": "Manual selected"
    },
    {
      "final_Brier": 0.24974568012176393,
      "final_log_loss": 0.6923151601492786,
      "workflow": "Native AutoML"
    },
    {
      "final_Brier": 0.24728732638888892,
      "final_log_loss": 0.6877119790398609,
      "workflow": "Source prevalence"
    }
  ],
  "final_used_for_selection": false,
  "language_model_agent_executed": false,
  "manual_selected_trial": 3,
  "manual_trials": [
    {
      "development_Brier": 0.2132357925043419,
      "development_log_loss": 0.6155977201598616,
      "family": "Logistic",
      "setting": 0.1
    },
    {
      "development_Brier": 0.21271911293934653,
      "development_log_loss": 0.6148370469157503,
      "family": "Logistic",
      "setting": 1.0
    },
    {
      "development_Brier": 0.21276893790132978,
      "development_log_loss": 0.6150668402712755,
      "family": "Logistic",
      "setting": 10.0
    },
    {
      "development_Brier": 0.2085514310225872,
      "development_log_loss": 0.6085611049190124,
      "family": "HGB",
      "setting": 2.0
    },
    {
      "development_Brier": 0.21229295815063673,
      "development_log_loss": 0.6227455781502277,
      "family": "HGB",
      "setting": 3.0
    },
    {
      "development_Brier": 0.23053175762150438,
      "development_log_loss": 0.6780014323547136,
      "family": "HGB",
      "setting": 5.0
    }
  ],
  "native_models": [
    {
      "development_negative_log_loss": -0.6332177234431174,
      "model": "LightGBM"
    },
    {
      "development_negative_log_loss": -0.5980751678734375,
      "model": "NeuralNetTorch"
    },
    {
      "development_negative_log_loss": -0.7018156041392506,
      "model": "RandomForest"
    },
    {
      "development_negative_log_loss": -0.5966726501243513,
      "model": "WeightedEnsemble_L2"
    }
  ],
  "native_selected": "WeightedEnsemble_L2",
  "proposal_contract_audit": [
    {
      "decision": "Rejected: final role is not fitting information",
      "family": "HGB",
      "fit_role": "final",
      "remaining_updates": 100,
      "updates": 50
    },
    {
      "decision": "Rejected: allocation exceeds remaining budget",
      "family": "HGB",
      "fit_role": "source",
      "remaining_updates": 100,
      "updates": 1000
    },
    {
      "decision": "Admitted source request; not executed by this validator",
      "family": "HGB",
      "fit_role": "source",
      "remaining_updates": 50,
      "updates": 50
    }
  ],
  "records_per_building": 4,
  "validator_requests_executed_as_model_fits": 0
}
```

### code_187

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 7687.

```json
{
  "all_attempted_inner_recipes": [
    {
      "depth": 2,
      "rate": 0.05
    },
    {
      "depth": 2,
      "rate": 0.15
    },
    {
      "depth": 5,
      "rate": 0.05
    },
    {
      "depth": 5,
      "rate": 0.15
    }
  ],
  "all_source_inner_mean_table": [
    [
      1.4898937659983857,
      1.2963745818479073,
      1.1557606614841325
    ],
    [
      1.30535829861165,
      1.129305170489442,
      0.9738515053575304
    ],
    [
      1.4179577915924495,
      1.192873920327976,
      1.0417858017979136
    ],
    [
      1.197062544931343,
      1.022444712002174,
      0.856795546892598
    ]
  ],
  "all_source_inner_selected_MSE": 0.856795546892598,
  "equal_risk_selection_records": [
    {
      "candidates": 1,
      "fresh_MSE": 1.3024644083489108,
      "reused_MSE": 1.1511898088511576,
      "selected_index": 0,
      "study": 0
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.249619205627585,
      "reused_MSE": 1.1351996041078842,
      "selected_index": 4,
      "study": 0
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2706925081618845,
      "reused_MSE": 1.0513927419957692,
      "selected_index": 49,
      "study": 0
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0569387090904545,
      "reused_MSE": 0.9779751230215353,
      "selected_index": 0,
      "study": 1
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1696572082948964,
      "reused_MSE": 0.8795676397828593,
      "selected_index": 3,
      "study": 1
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1917296455935797,
      "reused_MSE": 0.6330064750867571,
      "selected_index": 44,
      "study": 1
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1476858246587036,
      "reused_MSE": 0.9656836160904824,
      "selected_index": 0,
      "study": 2
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1066442496218998,
      "reused_MSE": 0.9571669566495447,
      "selected_index": 5,
      "study": 2
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1518291529393196,
      "reused_MSE": 0.8309207583142921,
      "selected_index": 29,
      "study": 2
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0331627126787515,
      "reused_MSE": 1.2312256906614674,
      "selected_index": 0,
      "study": 3
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0453005851864239,
      "reused_MSE": 1.2028197502640343,
      "selected_index": 2,
      "study": 3
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.052609744118705,
      "reused_MSE": 1.0736530540828124,
      "selected_index": 9,
      "study": 3
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1959604923428924,
      "reused_MSE": 1.3359020549592553,
      "selected_index": 0,
      "study": 4
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1395496811410226,
      "reused_MSE": 1.0169420988046016,
      "selected_index": 4,
      "study": 4
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1395496811410226,
      "reused_MSE": 1.0169420988046016,
      "selected_index": 4,
      "study": 4
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9081882069522256,
      "reused_MSE": 0.9244145402913697,
      "selected_index": 0,
      "study": 5
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9200562812053045,
      "reused_MSE": 0.8016903901083599,
      "selected_index": 6,
      "study": 5
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.8868512475852488,
      "reused_MSE": 0.7484161861026671,
      "selected_index": 12,
      "study": 5
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0997893292512528,
      "reused_MSE": 0.988930257400435,
      "selected_index": 0,
      "study": 6
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0104435695930294,
      "reused_MSE": 0.8201280746296501,
      "selected_index": 2,
      "study": 6
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0104435695930294,
      "reused_MSE": 0.8201280746296501,
      "selected_index": 2,
      "study": 6
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2145031058160018,
      "reused_MSE": 0.9734797160027056,
      "selected_index": 0,
      "study": 7
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.14130871972036,
      "reused_MSE": 0.9198212220747564,
      "selected_index": 6,
      "study": 7
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1125029777363822,
      "reused_MSE": 0.717450231764969,
      "selected_index": 36,
      "study": 7
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1716832144330191,
      "reused_MSE": 1.239006773269216,
      "selected_index": 0,
      "study": 8
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.125026915333742,
      "reused_MSE": 0.8108026709261298,
      "selected_index": 4,
      "study": 8
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.125026915333742,
      "reused_MSE": 0.8108026709261298,
      "selected_index": 4,
      "study": 8
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.057533990110606,
      "reused_MSE": 1.221793766904881,
      "selected_index": 0,
      "study": 9
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1096802218071442,
      "reused_MSE": 1.0780537034530184,
      "selected_index": 6,
      "study": 9
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.059791049167507,
      "reused_MSE": 0.9737753122446051,
      "selected_index": 53,
      "study": 9
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9992516075218085,
      "reused_MSE": 1.0654586130470585,
      "selected_index": 0,
      "study": 10
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9992516075218085,
      "reused_MSE": 1.0654586130470585,
      "selected_index": 0,
      "study": 10
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.100989722712598,
      "reused_MSE": 0.9427430637673678,
      "selected_index": 13,
      "study": 10
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.079272398767981,
      "reused_MSE": 0.974100614675139,
      "selected_index": 0,
      "study": 11
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0877708092019112,
      "reused_MSE": 0.9410739560775229,
      "selected_index": 3,
      "study": 11
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0749026309311185,
      "reused_MSE": 0.8196159216292205,
      "selected_index": 11,
      "study": 11
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.89528875262957,
      "reused_MSE": 0.8359233546744551,
      "selected_index": 0,
      "study": 12
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9194308129323026,
      "reused_MSE": 0.7961616758121643,
      "selected_index": 2,
      "study": 12
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0100931036675391,
      "reused_MSE": 0.6805095742212217,
      "selected_index": 15,
      "study": 12
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.032638731306591,
      "reused_MSE": 1.129784496769487,
      "selected_index": 0,
      "study": 13
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.032638731306591,
      "reused_MSE": 1.129784496769487,
      "selected_index": 0,
      "study": 13
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0874637898610706,
      "reused_MSE": 1.050713147309294,
      "selected_index": 53,
      "study": 13
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0416060756373253,
      "reused_MSE": 0.9800282501931203,
      "selected_index": 0,
      "study": 14
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0605350456799092,
      "reused_MSE": 0.9668582844430063,
      "selected_index": 1,
      "study": 14
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9700656733110935,
      "reused_MSE": 0.8489439666577819,
      "selected_index": 49,
      "study": 14
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2441387632769654,
      "reused_MSE": 1.3041185991786057,
      "selected_index": 0,
      "study": 15
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2336510750585887,
      "reused_MSE": 1.2578557586127252,
      "selected_index": 7,
      "study": 15
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2176220235869986,
      "reused_MSE": 1.008399426282372,
      "selected_index": 59,
      "study": 15
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2066254170987711,
      "reused_MSE": 1.0244400547256007,
      "selected_index": 0,
      "study": 16
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.193051995636854,
      "reused_MSE": 0.8289214976441033,
      "selected_index": 7,
      "study": 16
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.227028165373664,
      "reused_MSE": 0.8013953118845981,
      "selected_index": 43,
      "study": 16
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.172596725316258,
      "reused_MSE": 0.9338389294849196,
      "selected_index": 0,
      "study": 17
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0998433055598766,
      "reused_MSE": 0.8052982704955381,
      "selected_index": 6,
      "study": 17
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1538142277868,
      "reused_MSE": 0.7048302455394759,
      "selected_index": 61,
      "study": 17
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1313410200659506,
      "reused_MSE": 1.9375367130465235,
      "selected_index": 0,
      "study": 18
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1789143218631484,
      "reused_MSE": 1.7660770999550017,
      "selected_index": 4,
      "study": 18
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.213075786219163,
      "reused_MSE": 1.7146938445936826,
      "selected_index": 38,
      "study": 18
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.900096250183808,
      "reused_MSE": 0.9157960862215816,
      "selected_index": 0,
      "study": 19
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9950555988602879,
      "reused_MSE": 0.7892544857941866,
      "selected_index": 2,
      "study": 19
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9670032702907545,
      "reused_MSE": 0.717861116959926,
      "selected_index": 27,
      "study": 19
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1270896473705263,
      "reused_MSE": 0.7093525649351441,
      "selected_index": 0,
      "study": 20
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1786706485917495,
      "reused_MSE": 0.5493368390464398,
      "selected_index": 1,
      "study": 20
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1984621274804788,
      "reused_MSE": 0.5458558416598249,
      "selected_index": 63,
      "study": 20
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9740954443082068,
      "reused_MSE": 0.9718885430445348,
      "selected_index": 0,
      "study": 21
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0316359277695648,
      "reused_MSE": 0.6441343083131371,
      "selected_index": 6,
      "study": 21
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9869138441682331,
      "reused_MSE": 0.6130500489948283,
      "selected_index": 8,
      "study": 21
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1191725272538644,
      "reused_MSE": 1.2725943765677046,
      "selected_index": 0,
      "study": 22
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.098731752729276,
      "reused_MSE": 1.0816417269844947,
      "selected_index": 5,
      "study": 22
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0473296093669355,
      "reused_MSE": 0.9631132493572379,
      "selected_index": 36,
      "study": 22
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0959280390547566,
      "reused_MSE": 1.42521703827524,
      "selected_index": 0,
      "study": 23
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.110964137028229,
      "reused_MSE": 1.3853505200580365,
      "selected_index": 5,
      "study": 23
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0072223025483948,
      "reused_MSE": 1.1571088827301879,
      "selected_index": 30,
      "study": 23
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0061723065212604,
      "reused_MSE": 1.2316134920091126,
      "selected_index": 0,
      "study": 24
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0303351870928248,
      "reused_MSE": 1.0063221624511265,
      "selected_index": 7,
      "study": 24
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0605787251268175,
      "reused_MSE": 1.0046819258690034,
      "selected_index": 44,
      "study": 24
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0712000061811138,
      "reused_MSE": 1.2578007032161083,
      "selected_index": 0,
      "study": 25
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0712000061811138,
      "reused_MSE": 1.2578007032161083,
      "selected_index": 0,
      "study": 25
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0740780720134628,
      "reused_MSE": 1.095548863680333,
      "selected_index": 14,
      "study": 25
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9745171793000202,
      "reused_MSE": 1.5899413782578955,
      "selected_index": 0,
      "study": 26
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9642421623158995,
      "reused_MSE": 1.274020754656519,
      "selected_index": 1,
      "study": 26
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9642421623158995,
      "reused_MSE": 1.274020754656519,
      "selected_index": 1,
      "study": 26
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9892987767586877,
      "reused_MSE": 1.0660748684378905,
      "selected_index": 0,
      "study": 27
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9892987767586877,
      "reused_MSE": 1.0660748684378905,
      "selected_index": 0,
      "study": 27
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0974928178568926,
      "reused_MSE": 0.9818082371009235,
      "selected_index": 20,
      "study": 27
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.259779987203142,
      "reused_MSE": 1.150094038878946,
      "selected_index": 0,
      "study": 28
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2483494602431844,
      "reused_MSE": 0.895296179508407,
      "selected_index": 5,
      "study": 28
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.27023803580022,
      "reused_MSE": 0.7971523340410391,
      "selected_index": 28,
      "study": 28
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2062338707483313,
      "reused_MSE": 1.0392366018677297,
      "selected_index": 0,
      "study": 29
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.3332601780543933,
      "reused_MSE": 1.0090319388452307,
      "selected_index": 3,
      "study": 29
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2069130688401728,
      "reused_MSE": 0.9289440255119891,
      "selected_index": 29,
      "study": 29
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.044089321102052,
      "reused_MSE": 1.421370458925555,
      "selected_index": 0,
      "study": 30
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.046411179977172,
      "reused_MSE": 1.2895016150935557,
      "selected_index": 5,
      "study": 30
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9822005586402515,
      "reused_MSE": 1.2454662029288681,
      "selected_index": 32,
      "study": 30
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.193507156349428,
      "reused_MSE": 0.6058414450257573,
      "selected_index": 0,
      "study": 31
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.193507156349428,
      "reused_MSE": 0.6058414450257573,
      "selected_index": 0,
      "study": 31
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.240027641323112,
      "reused_MSE": 0.5006384916335508,
      "selected_index": 30,
      "study": 31
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.095853829947802,
      "reused_MSE": 1.0212709353194673,
      "selected_index": 0,
      "study": 32
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0828964069837705,
      "reused_MSE": 0.8122015501420327,
      "selected_index": 4,
      "study": 32
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0828964069837705,
      "reused_MSE": 0.8122015501420327,
      "selected_index": 4,
      "study": 32
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9972060088262182,
      "reused_MSE": 1.0701967245171355,
      "selected_index": 0,
      "study": 33
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.054284981538851,
      "reused_MSE": 0.8912200877110591,
      "selected_index": 3,
      "study": 33
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9857082756669294,
      "reused_MSE": 0.8071042507258788,
      "selected_index": 49,
      "study": 33
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0875249879787992,
      "reused_MSE": 0.9424524633379905,
      "selected_index": 0,
      "study": 34
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1337469196970502,
      "reused_MSE": 0.8421624263735106,
      "selected_index": 1,
      "study": 34
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0823761821634057,
      "reused_MSE": 0.7487419292774347,
      "selected_index": 29,
      "study": 34
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9842288322904676,
      "reused_MSE": 1.1044376433061194,
      "selected_index": 0,
      "study": 35
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9793649384794262,
      "reused_MSE": 0.8385922981005752,
      "selected_index": 1,
      "study": 35
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0664027030247913,
      "reused_MSE": 0.8285093834378519,
      "selected_index": 36,
      "study": 35
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0669056358492255,
      "reused_MSE": 1.016889530022173,
      "selected_index": 0,
      "study": 36
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0744740963602433,
      "reused_MSE": 0.7211449892013974,
      "selected_index": 7,
      "study": 36
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0744740963602433,
      "reused_MSE": 0.7211449892013974,
      "selected_index": 7,
      "study": 36
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0044239319215387,
      "reused_MSE": 0.7803599121457757,
      "selected_index": 0,
      "study": 37
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0749193215874058,
      "reused_MSE": 0.6516069179371935,
      "selected_index": 5,
      "study": 37
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.103681849636874,
      "reused_MSE": 0.58714565670688,
      "selected_index": 32,
      "study": 37
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0502670509845926,
      "reused_MSE": 1.2323921765916181,
      "selected_index": 0,
      "study": 38
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0502670509845926,
      "reused_MSE": 1.2323921765916181,
      "selected_index": 0,
      "study": 38
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9903417665720674,
      "reused_MSE": 1.12916547753026,
      "selected_index": 20,
      "study": 38
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0048155709262696,
      "reused_MSE": 1.1111089001910903,
      "selected_index": 0,
      "study": 39
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1430824011610476,
      "reused_MSE": 0.9998703767760626,
      "selected_index": 5,
      "study": 39
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0812832307921176,
      "reused_MSE": 0.8963231823745078,
      "selected_index": 58,
      "study": 39
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2923661772401953,
      "reused_MSE": 0.8525971385376009,
      "selected_index": 0,
      "study": 40
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1660734956227319,
      "reused_MSE": 0.7176941694826247,
      "selected_index": 4,
      "study": 40
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2585964164956938,
      "reused_MSE": 0.5867055078561874,
      "selected_index": 49,
      "study": 40
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2179171513417077,
      "reused_MSE": 1.0326617816970338,
      "selected_index": 0,
      "study": 41
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.3123206155430847,
      "reused_MSE": 0.7871253546736884,
      "selected_index": 4,
      "study": 41
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.29662619103145,
      "reused_MSE": 0.7614290643716213,
      "selected_index": 8,
      "study": 41
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1968015138924653,
      "reused_MSE": 1.1068498472190202,
      "selected_index": 0,
      "study": 42
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2542470761303566,
      "reused_MSE": 0.9130240270889798,
      "selected_index": 7,
      "study": 42
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2542470761303566,
      "reused_MSE": 0.9130240270889798,
      "selected_index": 7,
      "study": 42
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1794631482937061,
      "reused_MSE": 0.8476328759132119,
      "selected_index": 0,
      "study": 43
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.167036340692986,
      "reused_MSE": 0.6010671305711418,
      "selected_index": 2,
      "study": 43
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.127235304936702,
      "reused_MSE": 0.5365368432232253,
      "selected_index": 39,
      "study": 43
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.8701617781089683,
      "reused_MSE": 1.1717957880941001,
      "selected_index": 0,
      "study": 44
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9521280428638299,
      "reused_MSE": 0.9929096115742422,
      "selected_index": 2,
      "study": 44
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9528071028726202,
      "reused_MSE": 0.9855648767247566,
      "selected_index": 12,
      "study": 44
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.130530448725352,
      "reused_MSE": 1.1983633689046296,
      "selected_index": 0,
      "study": 45
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1921681490934966,
      "reused_MSE": 0.852171446739512,
      "selected_index": 4,
      "study": 45
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1921681490934966,
      "reused_MSE": 0.852171446739512,
      "selected_index": 4,
      "study": 45
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0780846214764808,
      "reused_MSE": 1.3875870723678028,
      "selected_index": 0,
      "study": 46
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.075755730738504,
      "reused_MSE": 1.2823126099960034,
      "selected_index": 7,
      "study": 46
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0864319590691436,
      "reused_MSE": 1.147542513353606,
      "selected_index": 10,
      "study": 46
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0665745925693437,
      "reused_MSE": 1.0938521655113707,
      "selected_index": 0,
      "study": 47
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0544255120999209,
      "reused_MSE": 1.063907366077178,
      "selected_index": 7,
      "study": 47
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9800709220835182,
      "reused_MSE": 0.7960290525404787,
      "selected_index": 12,
      "study": 47
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.3888776240921124,
      "reused_MSE": 1.2389576729933633,
      "selected_index": 0,
      "study": 48
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.4214842831540648,
      "reused_MSE": 1.0872191956328383,
      "selected_index": 5,
      "study": 48
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.4217475189430393,
      "reused_MSE": 0.954154443287293,
      "selected_index": 33,
      "study": 48
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0688648480586347,
      "reused_MSE": 1.0910312227066488,
      "selected_index": 0,
      "study": 49
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1130973885824844,
      "reused_MSE": 1.089330071491871,
      "selected_index": 5,
      "study": 49
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1240655166071563,
      "reused_MSE": 0.9911660593396101,
      "selected_index": 48,
      "study": 49
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2149337033474592,
      "reused_MSE": 0.6284481570686845,
      "selected_index": 0,
      "study": 50
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2668472304225746,
      "reused_MSE": 0.5396982085639357,
      "selected_index": 3,
      "study": 50
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2668472304225746,
      "reused_MSE": 0.5396982085639357,
      "selected_index": 3,
      "study": 50
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0501269800994584,
      "reused_MSE": 1.1737965354621989,
      "selected_index": 0,
      "study": 51
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0447071544935858,
      "reused_MSE": 0.9627776108009126,
      "selected_index": 2,
      "study": 51
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.021636274020023,
      "reused_MSE": 0.9328787621318254,
      "selected_index": 41,
      "study": 51
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0953883491340948,
      "reused_MSE": 0.5768550028132965,
      "selected_index": 0,
      "study": 52
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1091291946036286,
      "reused_MSE": 0.5678562917504549,
      "selected_index": 1,
      "study": 52
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1091291946036286,
      "reused_MSE": 0.5678562917504549,
      "selected_index": 1,
      "study": 52
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0485709722685397,
      "reused_MSE": 0.9384086467578582,
      "selected_index": 0,
      "study": 53
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0294087231941698,
      "reused_MSE": 0.8411329066484428,
      "selected_index": 5,
      "study": 53
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0872478047167085,
      "reused_MSE": 0.7821293467975495,
      "selected_index": 11,
      "study": 53
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.080431451954533,
      "reused_MSE": 0.7295336413160718,
      "selected_index": 0,
      "study": 54
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.080431451954533,
      "reused_MSE": 0.7295336413160718,
      "selected_index": 0,
      "study": 54
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1531574056710503,
      "reused_MSE": 0.6994807736328945,
      "selected_index": 26,
      "study": 54
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.078879797625349,
      "reused_MSE": 0.9226051466210269,
      "selected_index": 0,
      "study": 55
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1801324160493922,
      "reused_MSE": 0.7897388298676515,
      "selected_index": 6,
      "study": 55
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.097871595924969,
      "reused_MSE": 0.696272605433625,
      "selected_index": 19,
      "study": 55
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1695868111611438,
      "reused_MSE": 1.0184118893037521,
      "selected_index": 0,
      "study": 56
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1001934534389457,
      "reused_MSE": 0.9335283998813042,
      "selected_index": 6,
      "study": 56
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.185886878327803,
      "reused_MSE": 0.8279320954393927,
      "selected_index": 8,
      "study": 56
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0304451958359404,
      "reused_MSE": 1.3683248195912712,
      "selected_index": 0,
      "study": 57
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9859798222625074,
      "reused_MSE": 1.1994197956177381,
      "selected_index": 2,
      "study": 57
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9859798222625074,
      "reused_MSE": 1.1994197956177381,
      "selected_index": 2,
      "study": 57
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0757092043625023,
      "reused_MSE": 0.756929002010222,
      "selected_index": 0,
      "study": 58
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0198856131280671,
      "reused_MSE": 0.7262062476404461,
      "selected_index": 4,
      "study": 58
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1139189486365808,
      "reused_MSE": 0.7021441959186623,
      "selected_index": 23,
      "study": 58
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0036212598498597,
      "reused_MSE": 1.112453250571662,
      "selected_index": 0,
      "study": 59
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.080919907235686,
      "reused_MSE": 0.9806043717571452,
      "selected_index": 5,
      "study": 59
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9984755264479052,
      "reused_MSE": 0.841394726501572,
      "selected_index": 24,
      "study": 59
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1698016618577909,
      "reused_MSE": 0.8152731412924933,
      "selected_index": 0,
      "study": 60
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1496424262207747,
      "reused_MSE": 0.64718727230505,
      "selected_index": 4,
      "study": 60
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1918488951858621,
      "reused_MSE": 0.643536654176677,
      "selected_index": 54,
      "study": 60
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.052200432107482,
      "reused_MSE": 1.0182423556890503,
      "selected_index": 0,
      "study": 61
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1323419450188352,
      "reused_MSE": 0.9929569485588114,
      "selected_index": 2,
      "study": 61
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0615730197131952,
      "reused_MSE": 0.927009879722759,
      "selected_index": 37,
      "study": 61
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2521707043310553,
      "reused_MSE": 1.275894490440687,
      "selected_index": 0,
      "study": 62
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2772803291364518,
      "reused_MSE": 1.1511696762434998,
      "selected_index": 3,
      "study": 62
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1764660487253342,
      "reused_MSE": 0.901688611311695,
      "selected_index": 60,
      "study": 62
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9995784249115408,
      "reused_MSE": 0.8651152414333317,
      "selected_index": 0,
      "study": 63
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.059655746772976,
      "reused_MSE": 0.6432000529423045,
      "selected_index": 2,
      "study": 63
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0181397331974855,
      "reused_MSE": 0.5392624221325805,
      "selected_index": 46,
      "study": 63
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.915270756341729,
      "reused_MSE": 1.173097817542439,
      "selected_index": 0,
      "study": 64
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.996652756805054,
      "reused_MSE": 1.0757258283602558,
      "selected_index": 6,
      "study": 64
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9247786444343801,
      "reused_MSE": 0.9698660563097299,
      "selected_index": 45,
      "study": 64
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2698217964254874,
      "reused_MSE": 1.0872970360464564,
      "selected_index": 0,
      "study": 65
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1918792908918465,
      "reused_MSE": 0.9874249959260775,
      "selected_index": 5,
      "study": 65
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.255955199761371,
      "reused_MSE": 0.9613541200520475,
      "selected_index": 22,
      "study": 65
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1293215277373978,
      "reused_MSE": 1.0865066686302747,
      "selected_index": 0,
      "study": 66
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.07351460708733,
      "reused_MSE": 0.9111299515188349,
      "selected_index": 1,
      "study": 66
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.07351460708733,
      "reused_MSE": 0.9111299515188349,
      "selected_index": 1,
      "study": 66
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.9178924223063857,
      "reused_MSE": 1.0130551223384887,
      "selected_index": 0,
      "study": 67
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.001867193613176,
      "reused_MSE": 0.9711883966039598,
      "selected_index": 4,
      "study": 67
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.944216391172222,
      "reused_MSE": 0.834971044793509,
      "selected_index": 27,
      "study": 67
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1877135277875417,
      "reused_MSE": 0.7851614414463086,
      "selected_index": 0,
      "study": 68
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.3047934597495472,
      "reused_MSE": 0.7729946536772921,
      "selected_index": 3,
      "study": 68
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2941318458075022,
      "reused_MSE": 0.6845690898091491,
      "selected_index": 43,
      "study": 68
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1722569454394685,
      "reused_MSE": 0.8579298991518668,
      "selected_index": 0,
      "study": 69
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1361054973218427,
      "reused_MSE": 0.7913705907943089,
      "selected_index": 7,
      "study": 69
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.062706386555117,
      "reused_MSE": 0.657738875401001,
      "selected_index": 37,
      "study": 69
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0070862753375562,
      "reused_MSE": 0.9003876706703016,
      "selected_index": 0,
      "study": 70
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9958917803489455,
      "reused_MSE": 0.845963656286912,
      "selected_index": 7,
      "study": 70
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9958917803489455,
      "reused_MSE": 0.845963656286912,
      "selected_index": 7,
      "study": 70
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1363399042370277,
      "reused_MSE": 0.7537256571169022,
      "selected_index": 0,
      "study": 71
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.105081751833357,
      "reused_MSE": 0.7377963456411297,
      "selected_index": 2,
      "study": 71
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.068669532021512,
      "reused_MSE": 0.6103131978405155,
      "selected_index": 13,
      "study": 71
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0253244342366188,
      "reused_MSE": 1.0436810461203778,
      "selected_index": 0,
      "study": 72
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0185269315174912,
      "reused_MSE": 0.9220778652546378,
      "selected_index": 2,
      "study": 72
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0967327055528693,
      "reused_MSE": 0.8846196580152359,
      "selected_index": 53,
      "study": 72
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.3151432838773751,
      "reused_MSE": 1.2365950205683487,
      "selected_index": 0,
      "study": 73
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.3403489355441176,
      "reused_MSE": 0.880482175754117,
      "selected_index": 4,
      "study": 73
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2838929951285576,
      "reused_MSE": 0.8680935010769261,
      "selected_index": 55,
      "study": 73
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.103033540332826,
      "reused_MSE": 1.029013769102217,
      "selected_index": 0,
      "study": 74
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.059356660585434,
      "reused_MSE": 0.7882879233224787,
      "selected_index": 5,
      "study": 74
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0717514416821723,
      "reused_MSE": 0.7527189801866803,
      "selected_index": 35,
      "study": 74
    },
    {
      "candidates": 1,
      "fresh_MSE": 0.8835883030895357,
      "reused_MSE": 1.1110432648617874,
      "selected_index": 0,
      "study": 75
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9086254209757485,
      "reused_MSE": 0.9947949053358822,
      "selected_index": 7,
      "study": 75
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9475836237648653,
      "reused_MSE": 0.8669280244938294,
      "selected_index": 15,
      "study": 75
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.165205862471922,
      "reused_MSE": 1.0560223111444755,
      "selected_index": 0,
      "study": 76
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1471214417722841,
      "reused_MSE": 0.7241167681012252,
      "selected_index": 6,
      "study": 76
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1471214417722841,
      "reused_MSE": 0.7241167681012252,
      "selected_index": 6,
      "study": 76
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.3636198607049936,
      "reused_MSE": 1.0089684746065801,
      "selected_index": 0,
      "study": 77
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.3677482852773182,
      "reused_MSE": 0.9328575474184708,
      "selected_index": 6,
      "study": 77
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.3709446453795722,
      "reused_MSE": 0.8467201015978594,
      "selected_index": 18,
      "study": 77
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0348750128332511,
      "reused_MSE": 1.0153432715463393,
      "selected_index": 0,
      "study": 78
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9931043486183136,
      "reused_MSE": 0.9194376466405483,
      "selected_index": 3,
      "study": 78
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0153837205115699,
      "reused_MSE": 0.7725724928036087,
      "selected_index": 40,
      "study": 78
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1697334254379168,
      "reused_MSE": 1.437899982716108,
      "selected_index": 0,
      "study": 79
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0910827831301404,
      "reused_MSE": 1.3610531834403776,
      "selected_index": 7,
      "study": 79
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9925125491267337,
      "reused_MSE": 1.259232026312119,
      "selected_index": 46,
      "study": 79
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0892423108915166,
      "reused_MSE": 1.092194880316234,
      "selected_index": 0,
      "study": 80
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9317683403464037,
      "reused_MSE": 1.0140148897178736,
      "selected_index": 7,
      "study": 80
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9566986039291454,
      "reused_MSE": 0.7505096588645243,
      "selected_index": 62,
      "study": 80
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2322260672930005,
      "reused_MSE": 1.3306336069669626,
      "selected_index": 0,
      "study": 81
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.152772888397209,
      "reused_MSE": 1.048164804537794,
      "selected_index": 1,
      "study": 81
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1537008427514268,
      "reused_MSE": 1.0222182499147565,
      "selected_index": 42,
      "study": 81
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0372095384114037,
      "reused_MSE": 0.9466206013301459,
      "selected_index": 0,
      "study": 82
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0372095384114037,
      "reused_MSE": 0.9466206013301459,
      "selected_index": 0,
      "study": 82
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9859282593694942,
      "reused_MSE": 0.9422294375398643,
      "selected_index": 48,
      "study": 82
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1638591861589893,
      "reused_MSE": 1.1634621210758418,
      "selected_index": 0,
      "study": 83
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1638986925423283,
      "reused_MSE": 1.006692876539782,
      "selected_index": 3,
      "study": 83
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.102898933906152,
      "reused_MSE": 0.9806946095677442,
      "selected_index": 44,
      "study": 83
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1391066156023757,
      "reused_MSE": 1.1251350240025995,
      "selected_index": 0,
      "study": 84
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1064534278666809,
      "reused_MSE": 0.9027603506945008,
      "selected_index": 6,
      "study": 84
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.157672455566439,
      "reused_MSE": 0.8830057518118087,
      "selected_index": 48,
      "study": 84
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0397865007270797,
      "reused_MSE": 1.5060292967259663,
      "selected_index": 0,
      "study": 85
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.096736676263228,
      "reused_MSE": 1.2681172931203577,
      "selected_index": 5,
      "study": 85
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.027240313764741,
      "reused_MSE": 1.1051593785490426,
      "selected_index": 34,
      "study": 85
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0405261436217312,
      "reused_MSE": 0.7191638755935568,
      "selected_index": 0,
      "study": 86
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2107844511041856,
      "reused_MSE": 0.6900082274473026,
      "selected_index": 7,
      "study": 86
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.089105866784364,
      "reused_MSE": 0.5374499246683518,
      "selected_index": 58,
      "study": 86
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2408183582500478,
      "reused_MSE": 1.17670372565328,
      "selected_index": 0,
      "study": 87
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2714986663368013,
      "reused_MSE": 0.9577736382317017,
      "selected_index": 1,
      "study": 87
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2952944570669334,
      "reused_MSE": 0.8882108655520551,
      "selected_index": 11,
      "study": 87
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.25586888536728,
      "reused_MSE": 0.9319576432161234,
      "selected_index": 0,
      "study": 88
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1930731782163506,
      "reused_MSE": 0.776096549836162,
      "selected_index": 1,
      "study": 88
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2432118848234197,
      "reused_MSE": 0.6894013883798762,
      "selected_index": 51,
      "study": 88
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.2771463994476906,
      "reused_MSE": 0.9388023706213078,
      "selected_index": 0,
      "study": 89
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.2248183134646502,
      "reused_MSE": 0.9257261992306611,
      "selected_index": 2,
      "study": 89
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.2763533667667462,
      "reused_MSE": 0.8118893389148868,
      "selected_index": 54,
      "study": 89
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0442537520652018,
      "reused_MSE": 0.7931267760727048,
      "selected_index": 0,
      "study": 90
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0442537520652018,
      "reused_MSE": 0.7931267760727048,
      "selected_index": 0,
      "study": 90
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9840178527352367,
      "reused_MSE": 0.7748461728191482,
      "selected_index": 32,
      "study": 90
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.013234274347465,
      "reused_MSE": 1.2465288905266054,
      "selected_index": 0,
      "study": 91
    },
    {
      "candidates": 8,
      "fresh_MSE": 0.9928274286693529,
      "reused_MSE": 1.1163031002795907,
      "selected_index": 2,
      "study": 91
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0064088267416682,
      "reused_MSE": 1.0524082966742,
      "selected_index": 26,
      "study": 91
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.129523991111688,
      "reused_MSE": 0.8788626860357412,
      "selected_index": 0,
      "study": 92
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1234679768339353,
      "reused_MSE": 0.7682226718081491,
      "selected_index": 5,
      "study": 92
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.079886366102484,
      "reused_MSE": 0.7474094277335049,
      "selected_index": 44,
      "study": 92
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0724240866387043,
      "reused_MSE": 1.5982375390328447,
      "selected_index": 0,
      "study": 93
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0016852005436154,
      "reused_MSE": 1.4361983032465235,
      "selected_index": 7,
      "study": 93
    },
    {
      "candidates": 64,
      "fresh_MSE": 0.9937439574501653,
      "reused_MSE": 1.2725559930669852,
      "selected_index": 21,
      "study": 93
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0489194379688653,
      "reused_MSE": 0.928441799272137,
      "selected_index": 0,
      "study": 94
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0489194379688653,
      "reused_MSE": 0.928441799272137,
      "selected_index": 0,
      "study": 94
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1428698392468335,
      "reused_MSE": 0.8755913825508991,
      "selected_index": 16,
      "study": 94
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.058349145318887,
      "reused_MSE": 0.9219064475933534,
      "selected_index": 0,
      "study": 95
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0685843889206643,
      "reused_MSE": 0.7793178907931345,
      "selected_index": 4,
      "study": 95
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0685843889206643,
      "reused_MSE": 0.7793178907931345,
      "selected_index": 4,
      "study": 95
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.1802537038457894,
      "reused_MSE": 1.3176945133161329,
      "selected_index": 0,
      "study": 96
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.1978235265098098,
      "reused_MSE": 1.2574981568840766,
      "selected_index": 5,
      "study": 96
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.088938957243706,
      "reused_MSE": 1.2080332955346846,
      "selected_index": 58,
      "study": 96
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.085072985618501,
      "reused_MSE": 1.582717337507947,
      "selected_index": 0,
      "study": 97
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.106827009318876,
      "reused_MSE": 1.3706397338593956,
      "selected_index": 7,
      "study": 97
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.1748431469637954,
      "reused_MSE": 1.2130770177353858,
      "selected_index": 9,
      "study": 97
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.0578486285639708,
      "reused_MSE": 0.6151804552528818,
      "selected_index": 0,
      "study": 98
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.0578486285639708,
      "reused_MSE": 0.6151804552528818,
      "selected_index": 0,
      "study": 98
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0578486285639708,
      "reused_MSE": 0.6151804552528818,
      "selected_index": 0,
      "study": 98
    },
    {
      "candidates": 1,
      "fresh_MSE": 1.110738154480548,
      "reused_MSE": 1.2536379083562443,
      "selected_index": 0,
      "study": 99
    },
    {
      "candidates": 8,
      "fresh_MSE": 1.040639962727263,
      "reused_MSE": 0.9178189815098682,
      "selected_index": 4,
      "study": 99
    },
    {
      "candidates": 64,
      "fresh_MSE": 1.0064678910295006,
      "reused_MSE": 0.7514232712652446,
      "selected_index": 60,
      "study": 99
    }
  ],
  "equal_risk_selection_summary": [
    {
      "candidates": 1,
      "mean_fresh_MSE": 1.1016679774333762,
      "mean_reused_MSE": 1.0701514706073625,
      "population_MSE_each": 1.09
    },
    {
      "candidates": 8,
      "mean_fresh_MSE": 1.1073595730963293,
      "mean_reused_MSE": 0.9424967710488488,
      "population_MSE_each": 1.09
    },
    {
      "candidates": 64,
      "mean_fresh_MSE": 1.10225625246745,
      "mean_reused_MSE": 0.8628046605580253,
      "population_MSE_each": 1.09
    }
  ],
  "equal_risk_studies": 100,
  "final_buildings": 40,
  "final_fixed_trees": 40,
  "final_refit_records": 480,
  "final_selected_recipe": {
    "depth": 5,
    "rate": 0.15
  },
  "final_used_for_stopping_or_selection": false,
  "fresh_assessment_records": 200,
  "inner_fit_audit": [
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 53,
      "trees_spent": 40,
      "validation_buildings": 27
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 54,
      "trees_spent": 40,
      "validation_buildings": 26
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    },
    {
      "role": "inner",
      "train_buildings": 80,
      "trees_spent": 40,
      "validation_buildings": 40
    }
  ],
  "inner_trees_actually_spent": 1920,
  "locked_final_MSE": 0.7155853764385919,
  "outer_mean_MSE": 0.856795546892598,
  "outer_results": [
    {
      "inner_mean_table": [
        [
          1.6131552551490043,
          1.3928309223568716,
          1.251985238569895
        ],
        [
          1.390474715795926,
          1.2495704891901325,
          1.1725661073719236
        ],
        [
          1.5564743601403006,
          1.3274151800668392,
          1.149855001365441
        ],
        [
          1.3211706861382955,
          1.1515195286533177,
          0.9685110578031552
        ]
      ],
      "inner_selected_MSE": 0.9685110578031552,
      "outer_MSE": 0.7683610969114845,
      "outer_assessment_buildings": 40,
      "outer_fold": 0,
      "outer_train_buildings": 80,
      "selected_recipe": {
        "depth": 5,
        "rate": 0.15
      },
      "selected_trees": 40
    },
    {
      "inner_mean_table": [
        [
          1.4460230728943804,
          1.2801995260036616,
          1.131692817451328
        ],
        [
          1.2834317209984933,
          1.1285947777768233,
          1.0489211937559542
        ],
        [
          1.3911565136280355,
          1.1956584056662118,
          1.0245267400720113
        ],
        [
          1.1926228761820283,
          1.0090881806025096,
          0.8944643804718052
        ]
      ],
      "inner_selected_MSE": 0.8944643804718052,
      "outer_MSE": 0.8496467323569968,
      "outer_assessment_buildings": 40,
      "outer_fold": 1,
      "outer_train_buildings": 80,
      "selected_recipe": {
        "depth": 5,
        "rate": 0.15
      },
      "selected_trees": 40
    },
    {
      "inner_mean_table": [
        [
          1.4338319676769615,
          1.2312337595111533,
          1.1046910905656055
        ],
        [
          1.2247398648011585,
          1.090806835396034,
          0.9717285354216981
        ],
        [
          1.3710952809808452,
          1.1477826203164243,
          1.019609764984881
        ],
        [
          1.1402261264772016,
          0.9999340182441813,
          0.9273183689836716
        ]
      ],
      "inner_selected_MSE": 0.9273183689836716,
      "outer_MSE": 0.9523788114093126,
      "outer_assessment_buildings": 40,
      "outer_fold": 2,
      "outer_train_buildings": 80,
      "selected_recipe": {
        "depth": 5,
        "rate": 0.15
      },
      "selected_trees": 40
    }
  ],
  "records_per_building": 4,
  "reused_assessment_records": 40,
  "source_buildings": 120,
  "stopping_checkpoints_considered": [
    5,
    15,
    40
  ]
}
```


## Measured kernel resource observations for code_186

These are actual fresh-kernel measurements; vector export measures anew. They are excluded from exact scientific RESULTS equality.

```json
{
  "AutoML_fit_time_request_seconds": 14.995117291982751,
  "AutoML_overrun_seconds": 0.0,
  "AutoML_seconds": 0.42719433302409016,
  "manual_overrun_seconds": 0.0,
  "manual_seconds": 0.03477816600934602,
  "seconds_ceiling_each": 15.0
}
```

## Publication and visual evidence

Content revision `06b97fb9ef141086cc6336112b341a778bbadf2a` matches remote main and all 322 remote file blobs. All five notebooks execute 20 code cells and produce 11 reviewed inline figures. All 20 Chapter 35 pages, 11 book figures, four equations, five-row map and 20 exercises are reviewed, together with four front-matter and six reference pages. The separate second preview has 116 pages, SHA256 `aab9b6dba47ddc986242748c292d74d803803c5102c92c05f52f2893ef1c71a8`; Chapter 35 occupies printed 570–589/PDF 91–110. All 86 earlier second-preview body pages are pixel-identical; the first preview remains byte-identical. All 216 previous source/notebook hashes and 182 manifest records are preserved. Exact deterministic RESULTS match fresh vector exports; native AutoML resources are newly measured separately. Final metadata and commit-addressed raw files are verified separately. Only companion artifacts are published here.
