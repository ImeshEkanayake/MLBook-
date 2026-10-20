# Chapter 18 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. Chapter18 adds pinned CPU XGBoost3.4.1,LightGBM4.7.0,CatBoost1.2.10 and their graphviz/plotly dependencies; core package versions remain unchanged. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_001 (preserved; rerun) | 18.1 | 21 | 19 | 3.010 |
| code_087 | 18.1 | 4 | 2 | 1.747 |
| code_088 | 18.2 | 4 | 2 | 2.317 |
| code_089 | 18.3 | 4 | 2 | 1.871 |
| code_090 | 18.4 | 4 | 2 | 2.007 |
| code_091 | 18.5 | 4 | 2 | 1.859 |
| code_092 | 18.6 | 4 | 2 | 1.819 |

New laboratories: **24 executed code cells and12inline figures**. Including the preserved original code_001rerun: **45executed code cells and31inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

Chapter18 has six original numbered sections, not five. The original code_001 notebook and its manifest record remain byte-for-byte unchanged. It reran independently into ignored build/chapter18-original001.executed.ipynb:21code cells/19inline figures,3.010s including kernel lifecycle, same selected depth6/minleaf20 and identical final metrics (balanced accuracy.933333, Brier.0550442,logloss.635775 on360final cases). The preserved manifest retains its historical3.011s publication evidence; the new rerun is reported separately rather than rewriting an old record.

Six new self-contained laboratories087–092 use seeds1887–1892,24code cells and12inline figures. Together the seven chapter notebooks supply45executed cells/31figures. The core Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/sklearn1.9.0 versions are unchanged. The native comparison adds pinned CPU XGBoost3.4.1,LightGBM4.7.0 andCatBoost1.2.10; graphviz.21 andplotly7.1.0 are their added dependencies. Existing threadpoolctl3.7.0 limits loaded numerical thread pools; native library thread controls are explicitly1. All inputs/helpers are internal and ordinary runs are offline. Package installation is a setup step, not a notebook cell. Initial087–091runs passed.092first failed an unmatched-parenthesis syntax error; after repair its actual monotonicity assertion failed for raw quantile predictions. That behavioral failure is retained and the final explicitly projected algorithm is described below.091reran to shorten diagram text after book-vector review found spill beyond boxes.092reran after projection/coverage naming clarified the actual fitted target. No warning is suppressed; final outputs contain no solver warnings or error outputs. Numerical result dictionaries stay identical across layout-only reruns; the092coverage-key rename is an explicitly semantic metadata change.

087supplements the complete original constructor/pruning lab. It generates320training/200final Bernoulli records with correlated load measurements and resistance. Fixed depth2/minleaf12 query[.7,.7,.3] follows load threshold.654788 and resistance.292261 toleaf6with75training rows and class-one fraction1/3. Weighted-mass root impurity decrease.0499680 is verified, along with actual path/leaf probabilities. Final Brier.170151 is a fixed-model diagnostic. Forty prescribed perturbations each flip8training labels; root-feature counts[24,16,0], query probabilities.290909–.625 and root thresholds.497744–.654788. No perturbation selects another deployed model. Separate numeric-missing fixture learns the right branch with probability1; a training-only one-hot material encoder maps unseenpolymer toallzeros. These are different contracts and do not imply native categorical support or physical validity. The versioned missing_go_to_left field is disclosed as internal storage.

088independent member fixture train240/dev120(diagnostic only)/final240has six descriptors and correlated firsttwo(.998675). Fixed deep tree/bag80/RF80/Extra80 final MSE .258810/.152220/.142916/.133614. Forest and Extra use max_features.5; bag/forest bootstrap, Extra doesnot. Direct constituent average equals bag prediction. Mean within-bag pair prediction correlation across queries.848997 is not substituted for fixed-query repeated-fit correlation. A separate24bootstrap-refit sensitivity audit gives mean query variance .115604single vs.0246683bag30. Bag80/RF80 OOB MSE .156174/.149110 is appropriate to the independent-row fixture. Deliberately dependent30buildings×8rows share random building labels and an asset-coordinate identity proxy: OOB accuracy.908333 vs20new-building accuracy.43125; all7050omitted-row/tree pairs retain a training sibling. This is a counterexample to an unseen-entity interpretation, not realistic failure evidence.

089thirty-point toy starts mean.345900, then fits two depth1residual corrections with rate.5; training MSE .409355→.183625→.112740. Residual-update identity and a logistic negative-gradient finite difference(.331812) pass. Separate manually specified binary exponential-loss AdaBoost rounds use weighted errors.125/.190476, alpha.972955/.723459 and normalized error mass.5each. This is not a coefficient-normalization claim for every library variant. Independent regression train160/dev100/final200selects200of[20,80,200]stages by development MSE, fixed depth2/minleaf5/rate.1. Development.0713936/final.0638595. Final is not reused to extend the endpoint grid.

090executes all three native libraries on exactly the same60building×8row fixture.45development buildings360rows and15final buildings120rows are disjoint; the same3GroupKFold masks each hold out15buildings120rows from30buildings240rows. Each library gets2depth candidates[3,5]×3fold fits+1full-development selected refit,80rounds/rate.1/thread1/noearlystop. Predeclared materials steel/concrete/timber/missing/unknown retain semantic identities;92development numeric load readings areNaN. Group ID is excluded from features. XGBhist/depthwise/reg_lambda1, LGBleafwise/maxdepth/numleaves2**depth/minchild10/reg_lambda1, CatBoostOrdered/SymmetricTree/l2_leaf_reg1 are executed, with other interface defaults preserved. Equal candidate count is not equal wall time, effective regularization or exhaustive tuning. All selectdepth3. Final XGB/LGB/Cat logloss .624030/.630004/.612130;Brier .216987/.220302/.212960;accuracy.65/.641667/.65.80trees each have536/503/524terminal leaves, not measured latency. Target-free ordinary/missingload/unseenmaterial-mapped-unknown probes all predict finitely and differently; unknown has no training examples. No universal ranking or field probability validity follows. Live XGBdocs3.4.2 vs execution3.4.1 and sklearndocs1.9.1 vs1.9.0 are disclosed; LGB4.7.0 matches inspected documentation.

091generates train180/dev80/final200, four normal features with nonlinear response. Base learners HGB60rounds/leaf7/minleaf10, standardized Ridge1, standardized trained MLP12tanh/LBFGS/alpha.1/maxiter2000 are fixed. Five folds fit entire pipelines inside144memory/36query boundaries; each target gets exactly one OOFprediction row, overlap0. Meta Ridge[.1,1,10] is chosen by development, with head fitting on OOFfeatures only; full bases refit180training cases for deployment. Selected meta10coeff[.097178,.064612,.908408],intercept-.061435. Final boosted/Ridge/neural MSE .319915/1.210945/.0723998, uniform mean.193206, OOFstack.0706745. The small improvement over neural is finite evidence, not a dominance guarantee. Neural in-sample MSE.0236907 vs OOF.194787 exposes invalid meta-training optimism. Full neural fit723iterations with no optimizer warning. Honestblend uses120base/60head disjoint records and retains120-case bases at deployment, finalMSE.180447. Separate original softstump uses fixed sigmoid4x0, only twoleafvalues fit; derivative/prediction identities pass but finalMSE1.262113. No trained deep differentiable forest is claimed.

092train500/dev160/final400/future60uses y=5+3load+sin2piT+NormalSD(.2+.8load), source load/T[0,1], future load[1.2,1.6]. Unrestricted mean, native constrained mean and explicit projected q.1/.9 each selectleaf7of[7,15]using their own devMSE/pinball,120rounds/rate.08/minleaf15/earlystopFalse. Constrained base fits request monotone[1,0]/interaction[{0},{1}]. Actual raw quantile monotonicity fails in pinned1.9.0; selected201point-grid minimum increments-.00417704/-.10078409 are reported. Installed/versioned _update_leaves_values source re-estimates non-smooth-loss leaves; direct prediction checks, not parameter names, supply the failed-behavior evidence. No claim that every version fails is made. Final quantile wrapper projects fixed201load-grid model predictions attemperature.5 with increasing isotonic interpolation/out-of-bounds clipping, then adds the base's additive temperature component anchored atload.5. It uses model predictions only, no dev/final targets, and is applied to every candidate BEFOREdevpinballselection. Additive form establishes the wrapper's interaction restriction; increasing interpolation establishes load monotonicity. Finite81point×5temperature and four-corner checks verify implementation. Native constrained mean passes without projection. This explicit output transformation changes the raw quantile estimate; it is not called native monotonic quantile success.

092final unrestricted/constrained mean MSE .469840/.446708. Projected q.1/.9pinball .113289/.119848; fractionsbelow .1375/.8575, central projected interval coverage.72, upper exceedance.1425, crossings0. There is no final-outcome interval repair/calibration. Future meanMSE3.634464/3.471480, upperpinball.715713 shows unsupported extension despite monotonicity. A separately frozen80recordtemperature.25slice supplies plotted observations at the same conditioning value. Each fitted base has120prediction trees. Version-specific node arrays count1560/1560/1488/1524nodes,840/840/804/822leaves,87360/87360/83328/85344bytes plus0/0/944/1008isotonic threshold-array bytes. Other model arrays, Python/binning/workspaces/processRSS are excluded. This is not full model memory or a timing benchmark.

Twelve original vector figure sets implement both original briefs: actual tree path then varied-tree averaging; baseline plus two residual corrections contrasted with out-of-fold stacking information arrows. Four numbered equations and twelve exercises cover the six exact scopes. Primary official tree/forest/boosting/HGB and XGB/LightGBM/CatBoost documentation, plus pinned1.9.0 leaf-update source, were inspected20October2026. Mechanism correctness, empirical prediction loss, output constraints, uncertainty evidence and defined computation costs remain separate claims.

## Successful result dictionaries

### code_087

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1887.

```json
{
  "observation_contract": {
    "missing_numeric_leaf": 2,
    "missing_probability": 1.0,
    "native_categorical_tree_claimed": false,
    "onehot_training_categories": [
      "concrete",
      "steel",
      "timber"
    ],
    "root_missing_goes_left": false,
    "unknown_category_block": [
      0.0,
      0.0,
      0.0
    ]
  },
  "perturbations": {
    "labels_flipped_per_run": 8,
    "query_probability_max": 0.625,
    "query_probability_min": 0.2909090909090909,
    "root_features": [
      24,
      16,
      0
    ],
    "root_threshold_max": 0.6547884047031403,
    "root_threshold_min": 0.49774351716041565,
    "runs": 40
  },
  "tree": {
    "final": 200,
    "final_brier": 0.170150590021329,
    "leaf": 6,
    "leaf_class1_fraction": 0.3333333333333333,
    "leaf_records": 75,
    "path": [
      {
        "feature": 0,
        "node": 0,
        "threshold": 0.6547884047031403
      },
      {
        "feature": 2,
        "node": 4,
        "threshold": 0.29226091504096985
      }
    ],
    "query": [
      0.7,
      0.7,
      0.3
    ],
    "root_impurity_decrease": 0.049968042590592454,
    "training": 320
  }
}
```

### code_088

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1888.

```json
{
  "dependent_OOB_fixture": {
    "OOB_accuracy": 0.9083333333333333,
    "asset_coordinate_is_identity_proxy": true,
    "fraction_with_training_sibling": 1.0,
    "new_building_accuracy": 0.43125,
    "new_buildings": 20,
    "omitted_row_tree_pairs": 7050,
    "rows_per_building": 8,
    "training_buildings": 30
  },
  "independent_members": {
    "bag30_mean_prediction_variance": 0.024668298292780808,
    "bag80_OOB_mse": 0.15617369358527905,
    "first_two_training_correlation": 0.9986751159995971,
    "fixed_candidates": [
      {
        "development_mse": 0.16497594492100195,
        "final_mse": 0.25881026845530947,
        "model": "Single tree",
        "trees": 1
      },
      {
        "development_mse": 0.11920647450341286,
        "final_mse": 0.15221978813114614,
        "model": "Bagging",
        "trees": 80
      },
      {
        "development_mse": 0.11918286883288728,
        "final_mse": 0.14291648060673592,
        "model": "Random forest",
        "trees": 80
      },
      {
        "development_mse": 0.10460925487150871,
        "final_mse": 0.13361431345371125,
        "model": "Extra trees",
        "trees": 80
      }
    ],
    "refit_resamples": 24,
    "rf80_OOB_mse": 0.14911003007530327,
    "roles": {
      "development_diagnostic_only": 120,
      "final": 240,
      "training": 240
    },
    "single_mean_prediction_variance": 0.11560368262737374,
    "within_bag_mean_pair_prediction_correlation": 0.8489966851619167
  }
}
```

### code_089

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1889.

```json
{
  "AdaBoost_rounds": [
    {
      "alpha": 0.9729550745276566,
      "mean_weight_error_to_correct_ratio": 7.0,
      "post_update_weight_mass_on_this_round_errors": 0.4999999999999999,
      "preupdate_weight_sum": 0.9999999999999999,
      "weighted_error": 0.125
    },
    {
      "alpha": 0.7234594914681627,
      "mean_weight_error_to_correct_ratio": 2.0,
      "post_update_weight_mass_on_this_round_errors": 0.5000000000000001,
      "preupdate_weight_sum": 0.9999999999999998,
      "weighted_error": 0.1904761904761905
    }
  ],
  "selected_gradient_boosting": {
    "candidate_development_mse": [
      {
        "mse": 0.12838929825404416,
        "stages": 20
      },
      {
        "mse": 0.0730960072654534,
        "stages": 80
      },
      {
        "mse": 0.07139362480418654,
        "stages": 200
      }
    ],
    "development_mse": 0.07139362480418654,
    "final_mse": 0.06385949843907347,
    "learning_rate": 0.1,
    "roles": {
      "development": 100,
      "final": 200,
      "training": 160
    },
    "selected_stages": 200,
    "stage_grid": [
      20,
      80,
      200
    ]
  },
  "two_steps": {
    "baseline": 0.3459000365836607,
    "final_prediction_identity_passed": true,
    "learning_rate": 0.5,
    "logistic_negative_gradient": 0.331812227805095,
    "toy_rows": 30,
    "training_mse_baseline_then_two_steps": [
      0.40935488609006193,
      0.18362529099960362,
      0.11274015937822009
    ]
  }
}
```

### code_090

Versions: `{"catboost": "1.2.10", "lightgbm": "4.7.0", "matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "xgboost": "3.4.1"}`; Darwin arm64 CPU; seed 1890.

```json
{
  "benchmark": [
    {
      "final_accuracy": 0.65,
      "final_brier": 0.21698741614818573,
      "final_log_loss": 0.6240301132202148,
      "fitted_trees": 80,
      "library": "XGBoost",
      "mean_group_fold_log_loss": 0.7037480473518372,
      "selected_depth_budget": 3,
      "total_terminal_leaves": 536
    },
    {
      "final_accuracy": 0.6416666666666667,
      "final_brier": 0.22030198196364115,
      "final_log_loss": 0.6300039513851837,
      "fitted_trees": 80,
      "library": "LightGBM",
      "mean_group_fold_log_loss": 0.7039211990528588,
      "selected_depth_budget": 3,
      "total_terminal_leaves": 503
    },
    {
      "final_accuracy": 0.65,
      "final_brier": 0.21296048585799998,
      "final_log_loss": 0.6121303036948329,
      "fitted_trees": 80,
      "library": "CatBoost",
      "mean_group_fold_log_loss": 0.5991419163575692,
      "selected_depth_budget": 3,
      "total_terminal_leaves": 524
    }
  ],
  "inference_probes": {
    "probabilities": {
      "CatBoost": [
        0.43656328751389467,
        0.3483929332185498,
        0.2961494781453852
      ],
      "LightGBM": [
        0.5857273415041347,
        0.5427090925308677,
        0.38523181147209795
      ],
      "XGBoost": [
        0.5948242545127869,
        0.5283788442611694,
        0.6060923337936401
      ]
    },
    "rows": [
      "ordinary steel",
      "missing numeric load",
      "unseen material mapped unknown"
    ],
    "unseen_material_has_training_examples": false
  },
  "protocol": {
    "CPU_threads": 1,
    "development_buildings": 45,
    "development_rows": 360,
    "domain_category_vocabulary": [
      "steel",
      "concrete",
      "timber",
      "__missing__",
      "__unknown__"
    ],
    "equal_wall_time_claimed": false,
    "feature_columns": [
      "load",
      "resistance",
      "temperature",
      "material"
    ],
    "final_buildings": 15,
    "final_rows": 120,
    "fold_ledger": [
      {
        "training_groups": 30,
        "training_rows": 240,
        "validation_groups": 15,
        "validation_rows": 120
      },
      {
        "training_groups": 30,
        "training_rows": 240,
        "validation_groups": 15,
        "validation_rows": 120
      },
      {
        "training_groups": 30,
        "training_rows": 240,
        "validation_groups": 15,
        "validation_rows": 120
      }
    ],
    "learning_rate": 0.1,
    "numeric_missing_training_rows": 92,
    "rounds_per_fit": 80,
    "search_budget": [
      {
        "candidate_count": 2,
        "candidate_scores": [
          {
            "depth": 3,
            "fold_log_losses": [
              0.6277747750282288,
              0.8212311863899231,
              0.6622381806373596
            ],
            "mean_log_loss": 0.7037480473518372
          },
          {
            "depth": 5,
            "fold_log_losses": [
              0.66070955991745,
              0.9164857268333435,
              0.7457401156425476
            ],
            "mean_log_loss": 0.7743118007977804
          }
        ],
        "fold_fits_per_candidate": 3,
        "full_development_refits": 1,
        "library": "XGBoost"
      },
      {
        "candidate_count": 2,
        "candidate_scores": [
          {
            "depth": 3,
            "fold_log_losses": [
              0.6078827525550174,
              0.8305842536858488,
              0.67329659091771
            ],
            "mean_log_loss": 0.7039211990528588
          },
          {
            "depth": 5,
            "fold_log_losses": [
              0.6651449746256165,
              0.8713235393403896,
              0.7432202057733921
            ],
            "mean_log_loss": 0.7598962399131327
          }
        ],
        "fold_fits_per_candidate": 3,
        "full_development_refits": 1,
        "library": "LightGBM"
      },
      {
        "candidate_count": 2,
        "candidate_scores": [
          {
            "depth": 3,
            "fold_log_losses": [
              0.5507672480186186,
              0.6620484230095917,
              0.584610078044497
            ],
            "mean_log_loss": 0.5991419163575692
          },
          {
            "depth": 5,
            "fold_log_losses": [
              0.5544122851598309,
              0.6708821346882899,
              0.5775996666392778
            ],
            "mean_log_loss": 0.6009646954957996
          }
        ],
        "fold_fits_per_candidate": 3,
        "full_development_refits": 1,
        "library": "CatBoost"
      }
    ]
  }
}
```

### code_091

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1891.

```json
{
  "ensemble": {
    "OOF_base_mse": [
      0.5752131473562362,
      1.8411197288159742,
      0.19478658089920317
    ],
    "OOF_fold_ledger": [
      {
        "OOF_query_rows": 36,
        "base_training_rows": 144,
        "overlap": 0
      },
      {
        "OOF_query_rows": 36,
        "base_training_rows": 144,
        "overlap": 0
      },
      {
        "OOF_query_rows": 36,
        "base_training_rows": 144,
        "overlap": 0
      },
      {
        "OOF_query_rows": 36,
        "base_training_rows": 144,
        "overlap": 0
      },
      {
        "OOF_query_rows": 36,
        "base_training_rows": 144,
        "overlap": 0
      }
    ],
    "blend_base_training_rows": 120,
    "blend_bases_refit_on_head_targets": false,
    "blend_head_training_rows": 60,
    "development_mse": 0.10573204950406963,
    "final_scores": [
      {
        "final_mse": 0.31991501363474895,
        "model": "Boosted tree"
      },
      {
        "final_mse": 1.2109448706600614,
        "model": "Ridge"
      },
      {
        "final_mse": 0.07239978086710516,
        "model": "Neural"
      },
      {
        "final_mse": 0.1932063393692994,
        "model": "Uniform mean"
      },
      {
        "final_mse": 0.07067451856142108,
        "model": "OOF stack"
      },
      {
        "final_mse": 0.18044698391880673,
        "model": "Disjoint blend"
      }
    ],
    "invalid_in_sample_base_mse": [
      0.1927351147431485,
      1.7746842692717668,
      0.02369070999987915
    ],
    "meta_alpha": 10,
    "meta_coefficients": [
      0.09717794326688003,
      0.06461234848289715,
      0.9084083665651228
    ],
    "meta_intercept": -0.06143487975452455,
    "roles": {
      "development": 80,
      "final": 200,
      "training": 180
    }
  },
  "neural_fit": {
    "activation": "tanh",
    "full_training_iterations": 723,
    "hidden_units": 12,
    "max_iter": 2000,
    "solver": "lbfgs"
  },
  "soft_stump": {
    "deep_differentiable_forest_executed": false,
    "final_mse": 1.262112826361171,
    "fitted_leaf_values": [
      0.19371465975205648,
      1.4671976091252275
    ],
    "fixed_gate_slope": 4,
    "fixed_threshold": 0
  }
}
```

### code_092

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0"}`; Darwin arm64 CPU; seed 1892.

```json
{
  "constraints": [
    {
      "constrained": false,
      "four_corner_interaction_contrast": -0.4417414775267643,
      "minimum_grid_load_increment": -0.4409037444949808,
      "model": "Mean unrestricted"
    },
    {
      "constrained": true,
      "four_corner_interaction_contrast": 1.7763568394002505e-15,
      "minimum_grid_load_increment": 0.0,
      "model": "Mean constrained"
    },
    {
      "constrained": true,
      "four_corner_interaction_contrast": 0.0,
      "minimum_grid_load_increment": 0.0,
      "model": "Quantile .1"
    },
    {
      "constrained": true,
      "four_corner_interaction_contrast": -8.881784197001252e-16,
      "minimum_grid_load_increment": 0.0,
      "model": "Quantile .9"
    }
  ],
  "fits": [
    {
      "constrained": false,
      "development_loss": 0.5347948631445805,
      "development_selection_loss": "squared error",
      "final_mse": 0.46984046939884466,
      "future_mse": 3.634464207786554,
      "model": "Mean unrestricted",
      "selected_max_leaf_nodes": 7
    },
    {
      "constrained": true,
      "development_loss": 0.47607120122491703,
      "development_selection_loss": "squared error",
      "final_mse": 0.4467079775071251,
      "future_mse": 3.471479993997746,
      "model": "Mean constrained",
      "selected_max_leaf_nodes": 7
    },
    {
      "constrained": true,
      "development_loss": 0.12626830935018213,
      "development_selection_loss": "pinball0.1",
      "final_fraction_below": 0.1375,
      "final_mse": 1.1648778193191567,
      "final_pinball": 0.11328918692769427,
      "future_mse": 5.642319252943782,
      "future_pinball": 0.23572400251778713,
      "model": "Quantile .1",
      "quantile": 0.1,
      "raw_201point_minimum_load_increment": -0.004177037514862647,
      "selected_max_leaf_nodes": 7,
      "training_model_only_projection": true
    },
    {
      "constrained": true,
      "development_loss": 0.12378156975683685,
      "development_selection_loss": "pinball0.9",
      "final_fraction_below": 0.8575,
      "final_mse": 0.8241853535871031,
      "final_pinball": 0.11984771801368826,
      "future_mse": 2.3869606275595663,
      "future_pinball": 0.7157134914033573,
      "model": "Quantile .9",
      "quantile": 0.9,
      "raw_201point_minimum_load_increment": -0.10078408812146655,
      "selected_max_leaf_nodes": 7,
      "training_model_only_projection": true
    }
  ],
  "interval_diagnostics": {
    "crossing_rows": 0,
    "final_repair_or_recalibration": false,
    "nominal_central_mass": 0.8,
    "projected_final_coverage_no_recalibration": 0.72,
    "upper_exceedance_fraction": 0.1425
  },
  "locked_slice": {
    "rows": 80,
    "temperature": 0.25,
    "used_for_selection": false
  },
  "roles": {
    "development": 160,
    "final": 400,
    "future_load_final": 60,
    "training": 500
  },
  "stored_node_arrays": [
    {
      "excludes": "bin mapper, Python/library overhead, other arrays, complete process RSS",
      "leaves": 840,
      "model": "Mean unrestricted",
      "nodes": 1560,
      "prediction_trees": 120,
      "private_node_array_bytes": 87360,
      "projection_threshold_array_bytes": 0
    },
    {
      "excludes": "bin mapper, Python/library overhead, other arrays, complete process RSS",
      "leaves": 840,
      "model": "Mean constrained",
      "nodes": 1560,
      "prediction_trees": 120,
      "private_node_array_bytes": 87360,
      "projection_threshold_array_bytes": 0
    },
    {
      "excludes": "bin mapper, Python/library overhead, other arrays, complete process RSS",
      "leaves": 804,
      "model": "Quantile .1",
      "nodes": 1488,
      "prediction_trees": 120,
      "private_node_array_bytes": 83328,
      "projection_threshold_array_bytes": 944
    },
    {
      "excludes": "bin mapper, Python/library overhead, other arrays, complete process RSS",
      "leaves": 822,
      "model": "Quantile .9",
      "nodes": 1524,
      "prediction_trees": 120,
      "private_node_array_bytes": 85344,
      "projection_threshold_array_bytes": 1008
    }
  ]
}
```

