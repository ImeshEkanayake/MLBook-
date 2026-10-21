# Chapter 31 execution evidence

**Date:** 21 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency added; unchanged CPython 3.14.3/Torch 2.14.1 CPU environment. Second PDF starts at Chapter 31 while the first preview remains unchanged. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_161 | 31.1 | 4 | 2 | 2.319 |
| code_162 | 31.2 | 4 | 2 | 2.826 |
| code_163 | 31.3 | 4 | 2 | 7.202 |
| code_164 | 31.4 | 4 | 2 | 2.932 |
| code_165 | 31.5 | 4 | 2 | 4.373 |
| code_166 | 31.6 | 4 | 2 | 2.908 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

### Chapter 31 evidence and runtime

The user requested a separate second preview from Chapter 31 onward. This chapter is compiled from main_2.tex to output/pdf/main_2.pdf, with its own How to use this preview, contents and references_2.tex. The first preview through Chapter 30 is preserved byte-identically. Chapter numbering continues at 31 and printed body pagination at 484. The two PDFs remain separate for the user's later assembly.

All six experiments use the unchanged main CPython 3.14.3/Torch 2.14.1 CPU environment with one thread and float 64. No package, model checkpoint, external dataset or network call is added. Every notebook is self-contained with four executed code cells and two inline figures. All task records are generated; models and controls are real fitted implementations, not canned predictions. All current sources are rerun by the book figure producer and deterministic RESULTS must match fresh-kernel summaries exactly. No resource replay is used.

### Actual mechanisms and retained failures

161: 12 source buildings×2 members=24 true labels;200 unlabelled buildings;40 development and 100 final buildings×2. Source-only scaling, fixed RBF support-vector classifier with group-preserving 3-fold probability calibration, one-round pseudo-labels at 0.85, native graph LabelPropagation, original 500-update mean-teacher EMA 0.95. The initially deprecated SVC(probability=True) interface was replaced with supported CalibratedClassifierCV and explicit GroupKFold before publication, preserving building boundaries and the same true-label budget. No final-score choice between APIs is made. Final supervised accuracy 0.52. Pseudo 0.505/0.515,graph 0.44/0.445,consistency 0.48/0.46 for familiar/mixed pools; changed-regime semantic failure retained. Pseudo-labels admitted 311/153 of 400, hidden audit errors 0.006431/0.006536. Hidden unlabelled outcomes are opened only after fitting for audit and never tune admissions. Development 80 labels are diagnostics, not selection. Final graph predictions do not add final nodes to the fitted graph. Current stderr is empty.

162: 256 source/64 development/64 final buildings×2 sensor windows. Own 32→32→8 encoder; random/masked/denoising/contrastive noise/contrastive unit-RMS/temporal-last 8 mechanisms,600 updatesbatch 64 lr 0.003 for each trained objective. Same initial encoder. Source-only scaling;16/64 source-building labels(onewindoweach)fit frozen ridge,128 development labels choose alpha 0.1 or 10. Normalized contrastive views invert global feature scaling, normalize raw signal RMS, then reapply that fixed scale: the exact 0.6 sin/1.8 sin collision matches the actual augmentation. The first unpublished version normalized centred feature coordinates and was corrected, rerun and not used as the reported raw-amplitude invariance. Final MAE at 64 labels: random 0.0864, masked 0.0683, denoising 0.0317, contrastive noise 0.1059, normalized 0.1007, temporal 0.0704, raw 0.0317. Pretext losses are different scales, not a quality ranking. Contrastive source batches can include same-building windows as nominal negatives; limitation disclosed. Not full VIME/SimCLR replications.

163: four cohort seeds;240 candidate/120 independent final buildings, one row each. Six initial labels cost 6; total budgets 6/16/26/36/46. Real 20-tree forest depth 5/minleaf 2 refitted after each query; random/entropy-per-cost/diversity-per-cost/committee-variance-per-cost. Oracle outcomes admitted only after selection; pool-only distance scale. At cost 46, mean final accuracy 0.7333/0.7833/0.76875/0.73542, mean labels 31.5/46/46/46. Equal cost does not isolate equal-label information value. Four-cohort SD is descriptive, not CI. Acquisition-set diagnostics do not replace independent population evaluation. No development search.

164: 180 source/40 source-development/60 familiar final buildings×2 cases, same two outcomes for all procedures; noisy midpoint-load deflection in mm and separate generated binary damage. Separate 178 parameters/shared 94, raw vs source-scaled losses,1200 offered updateslr 0.01, common standardized development checkpoint objective. Familiar separate deflection MAE 0.473949/damageaccuracy 0.941667; sharedraw 0.264267/0.958333; sharedscaled 0.552078/0.958333. Harm to one task beside gain to another retained; raw convention happens to win here. Changed damage mechanism preserves deflection law and yields source-trained damageaccuracy~0.58–0.59. Newmaterial 24 calibration/16 development/60 final groups. Head-only 10 trainable/rankone 18,200 offered updateslr 0.005,4/16 calibration groups=16/64 scalaroutcomes plus 64 target-development scalaroutcomes. Lowbudgetrankone finalaccuracy 0.458333/MAE 1.138370 versus frozen 0.583333/0.770615. Hash verifies frozen source parameters unchanged.

165: actual second-order MAML-style two-parameter initialization;70 source tasks×64 cases=4480 unique outcomes,800 outer updates with 8 task episodes,2 innerstepslr 0.1. Recorded episode support/query indices disjoint. Shared episode access for actual conditional contextMLP(7 supportstats→32→32→2), pooled sourceOLS/zero-gradient-initialization/support-onlyOLS controls.20 development tasks expose up to 160 support+640 query labels; source checkpoints every 100 updates and adaptation steps 1/5/20 selected only there for budgets 2/4/8.40 new familiar-prior and 40 changed-prior finaltasks. Both learned source checkpoints selected 800. With 8 labels: MAML/pooled/context MAE 0.0531/0.0515/0.0486 familiar,0.0760/0.0828/0.0987 changed. OLS two-label instability 2.4309 familiar/0.6484 changed retained;8 labelOLS 0.0265/0.0289. Log axis retains full error range. All 4480 source outcomes actually accessed. Context global parameter hash unchanged; task-specific predicted coefficients are inference outputs. Not an LLM in-context-learning replication.

166: three ordered sensor generations×120 events, common 30-label/200-update warm-up;330 prequential predictions before five-event-delayed feedback. Last 5 labels unadmitted,355 total labels admitted at end. Three logits preallocated; class 2 first observed generation 2. Naive/replay 64/EWC-style(lambda 50,diagonal empirical Fisher,anchor,importance decay 0.9,known generation metadata)/periodic full refit from same random initialization every 40 deliveredlabels. Incremental 1625 gradientupdates; naive 1625 processed examples,replay 27625. Periodic 1600 updates/336000 processedexamples/355 retainedrecords. Regularization additionally performs 128 labelled-gradient evaluations for importance;230 importance/anchor scalars. Ninety independent held-out cases per generation, future matrix cells absent. Final mean retention 0.32963/1/0.36667/1; generation 0 forgetting 1/0/1/0; last-generation prequentialaccuracy 0.86667/0.71667/0.875/0.70833. Old retention and immediate adaptation tradeoff retained. No retention or final score selects a checkpoint. Supervised replay and importance penalty are declared narrower mechanisms, not original CLEAR/EWC benchmark replications.

### Source and interpretation boundaries

Primary sources support Mean Teacher, graph harmonic inference, VIME/SimCLR objective context, active query strategies, MAML's differentiable adaptation, replay and EWC importance penalties. Settles'2009 report is identified with the inspected 26 January 2010 update. Developer/author benchmark gains are not transferred to generated building tasks. All task/label/compute budgets, control architectures, partial pooling assumptions, sensor conventions, source/development/final roles and failures are disclosed. Whole-group or whole-task splits reflect constructed dependence and do not establish field representativeness. Visual review, exact PDF hash and remote publication proofs are recorded after actual completion.

## Successful result dictionaries

### code_161

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm 64 CPU; seed 4261.

```json
{
  "consistency_updates": 500,
  "development_buildings": 40,
  "development_labels": 80,
  "development_labels_used_for_selection": 0,
  "ema_decay": 0.95,
  "final_buildings": 100,
  "final_labels": 200,
  "final_labels_used_for_fit_or_selection": 0,
  "labelled_source_buildings": 12,
  "metrics": [
    {
      "changed_final_accuracy": 0.14,
      "development_accuracy": 0.5125,
      "familiar_final_accuracy": 0.9,
      "final_Brier": 0.5316833532955788,
      "final_accuracy": 0.52,
      "method": "Supervised",
      "pool": "Familiar pool"
    },
    {
      "changed_final_accuracy": 0.1,
      "development_accuracy": 0.5125,
      "familiar_final_accuracy": 0.91,
      "final_Brier": 0.7201643370178753,
      "final_accuracy": 0.505,
      "method": "Pseudo-label",
      "pool": "Familiar pool"
    },
    {
      "changed_final_accuracy": 0.04,
      "development_accuracy": 0.5,
      "familiar_final_accuracy": 0.84,
      "final_Brier": 0.723090555305737,
      "final_accuracy": 0.44,
      "method": "Graph",
      "pool": "Familiar pool"
    },
    {
      "changed_final_accuracy": 0.1,
      "development_accuracy": 0.525,
      "familiar_final_accuracy": 0.86,
      "final_Brier": 0.9534464610869824,
      "final_accuracy": 0.48,
      "method": "Consistency",
      "pool": "Familiar pool"
    },
    {
      "changed_final_accuracy": 0.14,
      "development_accuracy": 0.5125,
      "familiar_final_accuracy": 0.9,
      "final_Brier": 0.5316833532955788,
      "final_accuracy": 0.52,
      "method": "Supervised",
      "pool": "Mixed pool"
    },
    {
      "changed_final_accuracy": 0.12,
      "development_accuracy": 0.5125,
      "familiar_final_accuracy": 0.91,
      "final_Brier": 0.6752821866513018,
      "final_accuracy": 0.515,
      "method": "Pseudo-label",
      "pool": "Mixed pool"
    },
    {
      "changed_final_accuracy": 0.02,
      "development_accuracy": 0.5,
      "familiar_final_accuracy": 0.87,
      "final_Brier": 0.6537331199288506,
      "final_accuracy": 0.445,
      "method": "Graph",
      "pool": "Mixed pool"
    },
    {
      "changed_final_accuracy": 0.06,
      "development_accuracy": 0.5,
      "familiar_final_accuracy": 0.86,
      "final_Brier": 1.004098723388361,
      "final_accuracy": 0.46,
      "method": "Consistency",
      "pool": "Mixed pool"
    }
  ],
  "pseudo_label_audit": [
    {
      "hidden_pseudo_error_for_audit_only": 0.006430868167202572,
      "pool": "Familiar pool",
      "pseudo_labels_admitted": 311,
      "unlabelled_records": 400
    },
    {
      "hidden_pseudo_error_for_audit_only": 0.006535947712418301,
      "pool": "Mixed pool",
      "pseudo_labels_admitted": 153,
      "unlabelled_records": 400
    }
  ],
  "pseudo_threshold": 0.85,
  "true_source_labels": 24,
  "unlabelled_buildings_per_pool": 200
}
```

### code_162

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm 64 CPU; seed 4262.

```json
{
  "augmentation_target_collision": true,
  "collision_amplitudes": [
    0.6,
    1.8
  ],
  "development_buildings": 64,
  "development_labels": 128,
  "embedding_dimensions": 8,
  "final_buildings": 64,
  "final_inputs_admitted_to_pretraining": false,
  "final_windows": 128,
  "metrics": [
    {
      "development_MAE": 0.07803358573071843,
      "development_labels": 128,
      "final_MAE": 0.09164963724625422,
      "labelled_source_buildings": 16,
      "representation": "Random",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.06646611253228142,
      "development_labels": 128,
      "final_MAE": 0.08644893021027589,
      "labelled_source_buildings": 64,
      "representation": "Random",
      "selected_ridge_alpha": 0.1,
      "source_labels": 64
    },
    {
      "development_MAE": 0.06650137042184316,
      "development_labels": 128,
      "final_MAE": 0.07522364800532483,
      "labelled_source_buildings": 16,
      "representation": "Masked",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.05864295401742116,
      "development_labels": 128,
      "final_MAE": 0.06831019486371614,
      "labelled_source_buildings": 64,
      "representation": "Masked",
      "selected_ridge_alpha": 0.1,
      "source_labels": 64
    },
    {
      "development_MAE": 0.04499625328498011,
      "development_labels": 128,
      "final_MAE": 0.0426670188124037,
      "labelled_source_buildings": 16,
      "representation": "Denoising",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.029328050612313594,
      "development_labels": 128,
      "final_MAE": 0.031745128731645936,
      "labelled_source_buildings": 64,
      "representation": "Denoising",
      "selected_ridge_alpha": 0.1,
      "source_labels": 64
    },
    {
      "development_MAE": 0.1371507683158778,
      "development_labels": 128,
      "final_MAE": 0.13820705665183808,
      "labelled_source_buildings": 16,
      "representation": "Contrastive noise",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.10593940069860205,
      "development_labels": 128,
      "final_MAE": 0.1058915483955859,
      "labelled_source_buildings": 64,
      "representation": "Contrastive noise",
      "selected_ridge_alpha": 0.1,
      "source_labels": 64
    },
    {
      "development_MAE": 0.10504278468618058,
      "development_labels": 128,
      "final_MAE": 0.11960830546719979,
      "labelled_source_buildings": 16,
      "representation": "Contrastive normalized",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.08298913333900507,
      "development_labels": 128,
      "final_MAE": 0.10072686839649161,
      "labelled_source_buildings": 64,
      "representation": "Contrastive normalized",
      "selected_ridge_alpha": 10.0,
      "source_labels": 64
    },
    {
      "development_MAE": 0.0795969617611711,
      "development_labels": 128,
      "final_MAE": 0.09541819987105857,
      "labelled_source_buildings": 16,
      "representation": "Temporal",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.06321267772331424,
      "development_labels": 128,
      "final_MAE": 0.07041194783147343,
      "labelled_source_buildings": 64,
      "representation": "Temporal",
      "selected_ridge_alpha": 0.1,
      "source_labels": 64
    },
    {
      "development_MAE": 0.03771786608462349,
      "development_labels": 128,
      "final_MAE": 0.03633820283794132,
      "labelled_source_buildings": 16,
      "representation": "Raw features",
      "selected_ridge_alpha": 0.1,
      "source_labels": 16
    },
    {
      "development_MAE": 0.025116366014756197,
      "development_labels": 128,
      "final_MAE": 0.03170955815489136,
      "labelled_source_buildings": 64,
      "representation": "Raw features",
      "selected_ridge_alpha": 0.1,
      "source_labels": 64
    }
  ],
  "pretext_first_last_losses": {
    "Contrastive noise": [
      3.58472983968971,
      1.9049148764381651
    ],
    "Contrastive normalized": [
      3.902171620710043,
      2.0642773384689144
    ],
    "Denoising": [
      1.0522317163906942,
      0.006645578365959203
    ],
    "Masked": [
      1.0527499607090558,
      0.05461262993132964
    ],
    "Random": [],
    "Temporal": [
      1.1204896531325033,
      0.006397494742693507
    ]
  },
  "pretraining_batch": 64,
  "pretraining_learning_rate": 0.003,
  "pretraining_updates_per_nonrandom_objective": 600,
  "source_buildings": 256,
  "source_unlabelled_windows": 512
}
```

### code_163

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm 64 CPU; seed 4263.

```json
{
  "candidate_buildings_per_repeat": 240,
  "cohort_repeats": 4,
  "final_outcomes_admitted_to_acquisition": 0,
  "final_query_sample_diagnostics": [
    {
      "independent_final_positive_fraction": 0.5166666666666667,
      "policy": "Random",
      "queried_positive_fraction": 0.6071428571428571,
      "queried_resubstitution_accuracy": 1.0,
      "repeat": 0
    },
    {
      "independent_final_positive_fraction": 0.5166666666666667,
      "policy": "Uncertainty",
      "queried_positive_fraction": 0.4782608695652174,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 0
    },
    {
      "independent_final_positive_fraction": 0.5166666666666667,
      "policy": "Diversity",
      "queried_positive_fraction": 0.5,
      "queried_resubstitution_accuracy": 0.9347826086956522,
      "repeat": 0
    },
    {
      "independent_final_positive_fraction": 0.5166666666666667,
      "policy": "Committee",
      "queried_positive_fraction": 0.4782608695652174,
      "queried_resubstitution_accuracy": 0.9565217391304348,
      "repeat": 0
    },
    {
      "independent_final_positive_fraction": 0.43333333333333335,
      "policy": "Random",
      "queried_positive_fraction": 0.4375,
      "queried_resubstitution_accuracy": 0.96875,
      "repeat": 1
    },
    {
      "independent_final_positive_fraction": 0.43333333333333335,
      "policy": "Uncertainty",
      "queried_positive_fraction": 0.5217391304347826,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 1
    },
    {
      "independent_final_positive_fraction": 0.43333333333333335,
      "policy": "Diversity",
      "queried_positive_fraction": 0.5652173913043478,
      "queried_resubstitution_accuracy": 1.0,
      "repeat": 1
    },
    {
      "independent_final_positive_fraction": 0.43333333333333335,
      "policy": "Committee",
      "queried_positive_fraction": 0.5,
      "queried_resubstitution_accuracy": 0.9347826086956522,
      "repeat": 1
    },
    {
      "independent_final_positive_fraction": 0.525,
      "policy": "Random",
      "queried_positive_fraction": 0.59375,
      "queried_resubstitution_accuracy": 1.0,
      "repeat": 2
    },
    {
      "independent_final_positive_fraction": 0.525,
      "policy": "Uncertainty",
      "queried_positive_fraction": 0.5217391304347826,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 2
    },
    {
      "independent_final_positive_fraction": 0.525,
      "policy": "Diversity",
      "queried_positive_fraction": 0.45652173913043476,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 2
    },
    {
      "independent_final_positive_fraction": 0.525,
      "policy": "Committee",
      "queried_positive_fraction": 0.45652173913043476,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 2
    },
    {
      "independent_final_positive_fraction": 0.575,
      "policy": "Random",
      "queried_positive_fraction": 0.6764705882352942,
      "queried_resubstitution_accuracy": 0.9411764705882353,
      "repeat": 3
    },
    {
      "independent_final_positive_fraction": 0.575,
      "policy": "Uncertainty",
      "queried_positive_fraction": 0.5434782608695652,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 3
    },
    {
      "independent_final_positive_fraction": 0.575,
      "policy": "Diversity",
      "queried_positive_fraction": 0.5434782608695652,
      "queried_resubstitution_accuracy": 0.9565217391304348,
      "repeat": 3
    },
    {
      "independent_final_positive_fraction": 0.575,
      "policy": "Committee",
      "queried_positive_fraction": 0.5434782608695652,
      "queried_resubstitution_accuracy": 0.9782608695652174,
      "repeat": 3
    }
  ],
  "first_query_log": [
    {
      "building": 8,
      "cost": 1,
      "cumulative_cost": 7,
      "label": 1
    },
    {
      "building": 22,
      "cost": 1,
      "cumulative_cost": 8,
      "label": 1
    },
    {
      "building": 18,
      "cost": 1,
      "cumulative_cost": 9,
      "label": 1
    },
    {
      "building": 134,
      "cost": 1,
      "cumulative_cost": 10,
      "label": 0
    },
    {
      "building": 60,
      "cost": 1,
      "cumulative_cost": 11,
      "label": 1
    }
  ],
  "forest_depth": 5,
  "forest_trees": 20,
  "independent_final_buildings_per_repeat": 120,
  "individual_checkpoint_results": [
    {
      "budget": 6,
      "final_Brier": 0.461824363425926,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Random",
      "repeat": 0,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.5143211689814815,
      "final_accuracy": 0.5666666666666667,
      "observed_building_labels": 12,
      "policy": "Random",
      "repeat": 0,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.3996193518518518,
      "final_accuracy": 0.625,
      "observed_building_labels": 16,
      "policy": "Random",
      "repeat": 0,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.4827222685185185,
      "final_accuracy": 0.625,
      "observed_building_labels": 22,
      "policy": "Random",
      "repeat": 0,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.39413751286008225,
      "final_accuracy": 0.7083333333333334,
      "observed_building_labels": 28,
      "policy": "Random",
      "repeat": 0,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.461824363425926,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Uncertainty",
      "repeat": 0,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.40758841435185184,
      "final_accuracy": 0.7083333333333334,
      "observed_building_labels": 16,
      "policy": "Uncertainty",
      "repeat": 0,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.3698319444444444,
      "final_accuracy": 0.7583333333333333,
      "observed_building_labels": 26,
      "policy": "Uncertainty",
      "repeat": 0,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3723123438681028,
      "final_accuracy": 0.7416666666666667,
      "observed_building_labels": 36,
      "policy": "Uncertainty",
      "repeat": 0,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3538179122603037,
      "final_accuracy": 0.725,
      "observed_building_labels": 46,
      "policy": "Uncertainty",
      "repeat": 0,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.461824363425926,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Diversity",
      "repeat": 0,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.3798198200113378,
      "final_accuracy": 0.725,
      "observed_building_labels": 16,
      "policy": "Diversity",
      "repeat": 0,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.38647843986205593,
      "final_accuracy": 0.675,
      "observed_building_labels": 26,
      "policy": "Diversity",
      "repeat": 0,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.4175540976421433,
      "final_accuracy": 0.7333333333333333,
      "observed_building_labels": 36,
      "policy": "Diversity",
      "repeat": 0,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.39637621965161896,
      "final_accuracy": 0.7166666666666667,
      "observed_building_labels": 46,
      "policy": "Diversity",
      "repeat": 0,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.461824363425926,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Committee",
      "repeat": 0,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.38968539351851855,
      "final_accuracy": 0.725,
      "observed_building_labels": 16,
      "policy": "Committee",
      "repeat": 0,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.41487746905706735,
      "final_accuracy": 0.6833333333333333,
      "observed_building_labels": 26,
      "policy": "Committee",
      "repeat": 0,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3952720266439909,
      "final_accuracy": 0.7333333333333333,
      "observed_building_labels": 36,
      "policy": "Committee",
      "repeat": 0,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.38936208753254387,
      "final_accuracy": 0.725,
      "observed_building_labels": 46,
      "policy": "Committee",
      "repeat": 0,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6425564236111111,
      "final_accuracy": 0.5666666666666667,
      "observed_building_labels": 6,
      "policy": "Random",
      "repeat": 1,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.4235083478009259,
      "final_accuracy": 0.575,
      "observed_building_labels": 14,
      "policy": "Random",
      "repeat": 1,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.38754303406084656,
      "final_accuracy": 0.6083333333333333,
      "observed_building_labels": 20,
      "policy": "Random",
      "repeat": 1,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3702987470474301,
      "final_accuracy": 0.7083333333333334,
      "observed_building_labels": 26,
      "policy": "Random",
      "repeat": 1,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3195339903523138,
      "final_accuracy": 0.8083333333333333,
      "observed_building_labels": 32,
      "policy": "Random",
      "repeat": 1,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6425564236111111,
      "final_accuracy": 0.5666666666666667,
      "observed_building_labels": 6,
      "policy": "Uncertainty",
      "repeat": 1,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.4493289670138889,
      "final_accuracy": 0.675,
      "observed_building_labels": 16,
      "policy": "Uncertainty",
      "repeat": 1,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.36155008149092965,
      "final_accuracy": 0.7166666666666667,
      "observed_building_labels": 26,
      "policy": "Uncertainty",
      "repeat": 1,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.2992885262345679,
      "final_accuracy": 0.8,
      "observed_building_labels": 36,
      "policy": "Uncertainty",
      "repeat": 1,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3181710403588393,
      "final_accuracy": 0.8,
      "observed_building_labels": 46,
      "policy": "Uncertainty",
      "repeat": 1,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6425564236111111,
      "final_accuracy": 0.5666666666666667,
      "observed_building_labels": 6,
      "policy": "Diversity",
      "repeat": 1,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.38044825514928193,
      "final_accuracy": 0.725,
      "observed_building_labels": 16,
      "policy": "Diversity",
      "repeat": 1,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.37347742016250945,
      "final_accuracy": 0.7166666666666667,
      "observed_building_labels": 26,
      "policy": "Diversity",
      "repeat": 1,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.33426752897455275,
      "final_accuracy": 0.75,
      "observed_building_labels": 36,
      "policy": "Diversity",
      "repeat": 1,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.29897951377855064,
      "final_accuracy": 0.8166666666666667,
      "observed_building_labels": 46,
      "policy": "Diversity",
      "repeat": 1,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6425564236111111,
      "final_accuracy": 0.5666666666666667,
      "observed_building_labels": 6,
      "policy": "Committee",
      "repeat": 1,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.425067962962963,
      "final_accuracy": 0.6333333333333333,
      "observed_building_labels": 16,
      "policy": "Committee",
      "repeat": 1,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.3762946891534391,
      "final_accuracy": 0.675,
      "observed_building_labels": 26,
      "policy": "Committee",
      "repeat": 1,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3953673611111111,
      "final_accuracy": 0.6833333333333333,
      "observed_building_labels": 36,
      "policy": "Committee",
      "repeat": 1,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3809124150023257,
      "final_accuracy": 0.7,
      "observed_building_labels": 46,
      "policy": "Committee",
      "repeat": 1,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.49719704861111114,
      "final_accuracy": 0.525,
      "observed_building_labels": 6,
      "policy": "Random",
      "repeat": 2,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.390927025462963,
      "final_accuracy": 0.7333333333333333,
      "observed_building_labels": 12,
      "policy": "Random",
      "repeat": 2,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.37733561673280425,
      "final_accuracy": 0.725,
      "observed_building_labels": 18,
      "policy": "Random",
      "repeat": 2,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3537509176587302,
      "final_accuracy": 0.7916666666666666,
      "observed_building_labels": 26,
      "policy": "Random",
      "repeat": 2,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.33097317318594105,
      "final_accuracy": 0.7916666666666666,
      "observed_building_labels": 32,
      "policy": "Random",
      "repeat": 2,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.49719704861111114,
      "final_accuracy": 0.525,
      "observed_building_labels": 6,
      "policy": "Uncertainty",
      "repeat": 2,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.3579089247921391,
      "final_accuracy": 0.7416666666666667,
      "observed_building_labels": 16,
      "policy": "Uncertainty",
      "repeat": 2,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.32051787745653815,
      "final_accuracy": 0.7666666666666667,
      "observed_building_labels": 26,
      "policy": "Uncertainty",
      "repeat": 2,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3029075578703704,
      "final_accuracy": 0.825,
      "observed_building_labels": 36,
      "policy": "Uncertainty",
      "repeat": 2,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3111628869912398,
      "final_accuracy": 0.8583333333333333,
      "observed_building_labels": 46,
      "policy": "Uncertainty",
      "repeat": 2,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.49719704861111114,
      "final_accuracy": 0.525,
      "observed_building_labels": 6,
      "policy": "Diversity",
      "repeat": 2,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.43041153935185184,
      "final_accuracy": 0.6666666666666666,
      "observed_building_labels": 16,
      "policy": "Diversity",
      "repeat": 2,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.3575056417705972,
      "final_accuracy": 0.7166666666666667,
      "observed_building_labels": 26,
      "policy": "Diversity",
      "repeat": 2,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.32352244378306877,
      "final_accuracy": 0.8083333333333333,
      "observed_building_labels": 36,
      "policy": "Diversity",
      "repeat": 2,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3071053859599395,
      "final_accuracy": 0.8083333333333333,
      "observed_building_labels": 46,
      "policy": "Diversity",
      "repeat": 2,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.49719704861111114,
      "final_accuracy": 0.525,
      "observed_building_labels": 6,
      "policy": "Committee",
      "repeat": 2,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.4033022685185185,
      "final_accuracy": 0.6916666666666667,
      "observed_building_labels": 16,
      "policy": "Committee",
      "repeat": 2,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.4172222453703703,
      "final_accuracy": 0.6583333333333333,
      "observed_building_labels": 26,
      "policy": "Committee",
      "repeat": 2,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.3619265522841081,
      "final_accuracy": 0.7833333333333333,
      "observed_building_labels": 36,
      "policy": "Committee",
      "repeat": 2,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.3332024435468632,
      "final_accuracy": 0.8166666666666667,
      "observed_building_labels": 46,
      "policy": "Committee",
      "repeat": 2,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6218194444444445,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Random",
      "repeat": 3,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.43786230902777773,
      "final_accuracy": 0.625,
      "observed_building_labels": 14,
      "policy": "Random",
      "repeat": 3,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.47530505857898714,
      "final_accuracy": 0.525,
      "observed_building_labels": 18,
      "policy": "Random",
      "repeat": 3,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.4889005555555555,
      "final_accuracy": 0.5833333333333334,
      "observed_building_labels": 24,
      "policy": "Random",
      "repeat": 3,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.4478081061626039,
      "final_accuracy": 0.625,
      "observed_building_labels": 34,
      "policy": "Random",
      "repeat": 3,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6218194444444445,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Uncertainty",
      "repeat": 3,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.3985925925925926,
      "final_accuracy": 0.7,
      "observed_building_labels": 16,
      "policy": "Uncertainty",
      "repeat": 3,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.42337674933862435,
      "final_accuracy": 0.7416666666666667,
      "observed_building_labels": 26,
      "policy": "Uncertainty",
      "repeat": 3,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.40969193133454596,
      "final_accuracy": 0.725,
      "observed_building_labels": 36,
      "policy": "Uncertainty",
      "repeat": 3,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.367790318510554,
      "final_accuracy": 0.75,
      "observed_building_labels": 46,
      "policy": "Uncertainty",
      "repeat": 3,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6218194444444445,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Diversity",
      "repeat": 3,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.4457170313681027,
      "final_accuracy": 0.7083333333333334,
      "observed_building_labels": 16,
      "policy": "Diversity",
      "repeat": 3,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.4233726778628118,
      "final_accuracy": 0.7166666666666667,
      "observed_building_labels": 26,
      "policy": "Diversity",
      "repeat": 3,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.409063770313681,
      "final_accuracy": 0.75,
      "observed_building_labels": 36,
      "policy": "Diversity",
      "repeat": 3,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.39167614101790604,
      "final_accuracy": 0.7333333333333333,
      "observed_building_labels": 46,
      "policy": "Diversity",
      "repeat": 3,
      "spent": 46
    },
    {
      "budget": 6,
      "final_Brier": 0.6218194444444445,
      "final_accuracy": 0.575,
      "observed_building_labels": 6,
      "policy": "Committee",
      "repeat": 3,
      "spent": 6
    },
    {
      "budget": 16,
      "final_Brier": 0.4640712055933484,
      "final_accuracy": 0.6833333333333333,
      "observed_building_labels": 16,
      "policy": "Committee",
      "repeat": 3,
      "spent": 16
    },
    {
      "budget": 26,
      "final_Brier": 0.4619385064720332,
      "final_accuracy": 0.7166666666666667,
      "observed_building_labels": 26,
      "policy": "Committee",
      "repeat": 3,
      "spent": 26
    },
    {
      "budget": 36,
      "final_Brier": 0.4661660881991686,
      "final_accuracy": 0.6833333333333333,
      "observed_building_labels": 36,
      "policy": "Committee",
      "repeat": 3,
      "spent": 36
    },
    {
      "budget": 46,
      "final_Brier": 0.45078961438970555,
      "final_accuracy": 0.7,
      "observed_building_labels": 46,
      "policy": "Committee",
      "repeat": 3,
      "spent": 46
    }
  ],
  "initial_observed_labels": 6,
  "metrics": [
    {
      "budget": 6,
      "cohort_SD_accuracy": 0.023935677693908423,
      "mean_final_accuracy": 0.5604166666666666,
      "mean_observed_building_labels": 6.0,
      "mean_spent": 6.0,
      "policy": "Random"
    },
    {
      "budget": 16,
      "cohort_SD_accuracy": 0.07667874301023477,
      "mean_final_accuracy": 0.625,
      "mean_observed_building_labels": 13.0,
      "mean_spent": 16.0,
      "policy": "Random"
    },
    {
      "budget": 26,
      "cohort_SD_accuracy": 0.08207381501496754,
      "mean_final_accuracy": 0.6208333333333333,
      "mean_observed_building_labels": 18.0,
      "mean_spent": 26.0,
      "policy": "Random"
    },
    {
      "budget": 36,
      "cohort_SD_accuracy": 0.09238982427534768,
      "mean_final_accuracy": 0.6770833333333334,
      "mean_observed_building_labels": 24.5,
      "mean_spent": 36.0,
      "policy": "Random"
    },
    {
      "budget": 46,
      "cohort_SD_accuracy": 0.08443713418650368,
      "mean_final_accuracy": 0.7333333333333333,
      "mean_observed_building_labels": 31.5,
      "mean_spent": 46.0,
      "policy": "Random"
    },
    {
      "budget": 6,
      "cohort_SD_accuracy": 0.023935677693908423,
      "mean_final_accuracy": 0.5604166666666666,
      "mean_observed_building_labels": 6.0,
      "mean_spent": 6.0,
      "policy": "Uncertainty"
    },
    {
      "budget": 16,
      "cohort_SD_accuracy": 0.02753364944666529,
      "mean_final_accuracy": 0.70625,
      "mean_observed_building_labels": 16.0,
      "mean_spent": 16.0,
      "policy": "Uncertainty"
    },
    {
      "budget": 26,
      "cohort_SD_accuracy": 0.022047927592204926,
      "mean_final_accuracy": 0.7458333333333333,
      "mean_observed_building_labels": 26.0,
      "mean_spent": 26.0,
      "policy": "Uncertainty"
    },
    {
      "budget": 36,
      "cohort_SD_accuracy": 0.04732423621500227,
      "mean_final_accuracy": 0.7729166666666667,
      "mean_observed_building_labels": 36.0,
      "mean_spent": 36.0,
      "policy": "Uncertainty"
    },
    {
      "budget": 46,
      "cohort_SD_accuracy": 0.05892556509887895,
      "mean_final_accuracy": 0.7833333333333333,
      "mean_observed_building_labels": 46.0,
      "mean_spent": 46.0,
      "policy": "Uncertainty"
    },
    {
      "budget": 6,
      "cohort_SD_accuracy": 0.023935677693908423,
      "mean_final_accuracy": 0.5604166666666666,
      "mean_observed_building_labels": 6.0,
      "mean_spent": 6.0,
      "policy": "Diversity"
    },
    {
      "budget": 16,
      "cohort_SD_accuracy": 0.0275336494466653,
      "mean_final_accuracy": 0.70625,
      "mean_observed_building_labels": 16.0,
      "mean_spent": 16.0,
      "policy": "Diversity"
    },
    {
      "budget": 26,
      "cohort_SD_accuracy": 0.020833333333333315,
      "mean_final_accuracy": 0.70625,
      "mean_observed_building_labels": 26.0,
      "mean_spent": 26.0,
      "policy": "Diversity"
    },
    {
      "budget": 36,
      "cohort_SD_accuracy": 0.032896442450908385,
      "mean_final_accuracy": 0.7604166666666667,
      "mean_observed_building_labels": 36.0,
      "mean_spent": 36.0,
      "policy": "Diversity"
    },
    {
      "budget": 46,
      "cohort_SD_accuracy": 0.05108770599374868,
      "mean_final_accuracy": 0.76875,
      "mean_observed_building_labels": 46.0,
      "mean_spent": 46.0,
      "policy": "Diversity"
    },
    {
      "budget": 6,
      "cohort_SD_accuracy": 0.023935677693908423,
      "mean_final_accuracy": 0.5604166666666666,
      "mean_observed_building_labels": 6.0,
      "mean_spent": 6.0,
      "policy": "Committee"
    },
    {
      "budget": 16,
      "cohort_SD_accuracy": 0.037883838047182934,
      "mean_final_accuracy": 0.6833333333333333,
      "mean_observed_building_labels": 16.0,
      "mean_spent": 16.0,
      "policy": "Committee"
    },
    {
      "budget": 26,
      "cohort_SD_accuracy": 0.02453266907313291,
      "mean_final_accuracy": 0.6833333333333333,
      "mean_observed_building_labels": 26.0,
      "mean_spent": 26.0,
      "policy": "Committee"
    },
    {
      "budget": 36,
      "cohort_SD_accuracy": 0.047871355387816894,
      "mean_final_accuracy": 0.7208333333333332,
      "mean_observed_building_labels": 36.0,
      "mean_spent": 36.0,
      "policy": "Committee"
    },
    {
      "budget": 46,
      "cohort_SD_accuracy": 0.05543389456520864,
      "mean_final_accuracy": 0.7354166666666666,
      "mean_observed_building_labels": 46.0,
      "mean_spent": 46.0,
      "policy": "Committee"
    }
  ],
  "query_costs": [
    1,
    3
  ],
  "total_cost_checkpoints": [
    6,
    16,
    26,
    36,
    46
  ]
}
```

### code_164

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm 64 CPU; seed 4264.

```json
{
  "changed_final_buildings": 60,
  "familiar_final_buildings": 60,
  "final_labels_used_for_selection": 0,
  "frozen_source_unchanged": true,
  "source_buildings": 180,
  "source_development_buildings": 40,
  "source_development_scalar_outcomes": 160,
  "source_metrics": [
    {
      "damage_Brier": 0.03238728017278983,
      "damage_accuracy": 0.9416666666666667,
      "deflection_MAE_mm": 0.47394868949956287,
      "domain": "Familiar",
      "method": "Separate scaled",
      "parameters": 178,
      "source_records": 360
    },
    {
      "damage_Brier": 0.357945065789577,
      "damage_accuracy": 0.5833333333333334,
      "deflection_MAE_mm": 1.0426940482817766,
      "domain": "Changed material",
      "method": "Separate scaled",
      "parameters": 178,
      "source_records": 360
    },
    {
      "damage_Brier": 0.03556684557932727,
      "damage_accuracy": 0.9583333333333334,
      "deflection_MAE_mm": 0.2642669465195777,
      "domain": "Familiar",
      "method": "Shared raw",
      "parameters": 94,
      "source_records": 360
    },
    {
      "damage_Brier": 0.3726379455975189,
      "damage_accuracy": 0.5916666666666667,
      "deflection_MAE_mm": 0.4196369328962399,
      "domain": "Changed material",
      "method": "Shared raw",
      "parameters": 94,
      "source_records": 360
    },
    {
      "damage_Brier": 0.03455301721643337,
      "damage_accuracy": 0.9583333333333334,
      "deflection_MAE_mm": 0.5520784211774654,
      "domain": "Familiar",
      "method": "Shared scaled",
      "parameters": 94,
      "source_records": 360
    },
    {
      "damage_Brier": 0.4056938250286875,
      "damage_accuracy": 0.5833333333333334,
      "deflection_MAE_mm": 0.7706150203542512,
      "domain": "Changed material",
      "method": "Shared scaled",
      "parameters": 94,
      "source_records": 360
    }
  ],
  "source_records": 360,
  "source_selected_updates": {
    "Separate scaled": 100,
    "Shared raw": 1200,
    "Shared scaled": 1000
  },
  "source_target_mean_mm": 4.408971111092788,
  "source_target_scale_mm": 5.798347597334196,
  "source_updates_offered": 1200,
  "target_adaptation_metrics": [
    {
      "damage_Brier": 0.37140154333381453,
      "damage_accuracy": 0.6,
      "deflection_MAE_mm": 0.8556674249168926,
      "domain": "Changed material",
      "method": "Head-only",
      "selected_update": 200,
      "target_calibration_buildings": 4,
      "target_development_records": 32,
      "target_development_scalar_outcomes": 64,
      "target_records": 8,
      "target_scalar_outcomes": 16,
      "trainable_parameters": 10
    },
    {
      "damage_Brier": 0.33025521168114813,
      "damage_accuracy": 0.4583333333333333,
      "deflection_MAE_mm": 1.1383702610506354,
      "domain": "Changed material",
      "method": "Rank-one adapter",
      "selected_update": 100,
      "target_calibration_buildings": 4,
      "target_development_records": 32,
      "target_development_scalar_outcomes": 64,
      "target_records": 8,
      "target_scalar_outcomes": 16,
      "trainable_parameters": 18
    },
    {
      "damage_Brier": 0.3714305885750316,
      "damage_accuracy": 0.6,
      "deflection_MAE_mm": 0.8729069502615172,
      "domain": "Changed material",
      "method": "Head-only",
      "selected_update": 200,
      "target_calibration_buildings": 16,
      "target_development_records": 32,
      "target_development_scalar_outcomes": 64,
      "target_records": 32,
      "target_scalar_outcomes": 64,
      "trainable_parameters": 10
    },
    {
      "damage_Brier": 0.23443793770917462,
      "damage_accuracy": 0.6,
      "deflection_MAE_mm": 0.8800872722310732,
      "domain": "Changed material",
      "method": "Rank-one adapter",
      "selected_update": 150,
      "target_calibration_buildings": 16,
      "target_development_records": 32,
      "target_development_scalar_outcomes": 64,
      "target_records": 32,
      "target_scalar_outcomes": 64,
      "trainable_parameters": 18
    }
  ]
}
```

### code_165

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm 64 CPU; seed 4265.

```json
{
  "context_global_parameters": 1378,
  "context_weights_unchanged": true,
  "development_query_labels": 640,
  "development_support_labels_max": 160,
  "development_tasks": 20,
  "final_changed_tasks": 40,
  "final_familiar_tasks": 40,
  "final_support_query_overlap": 0,
  "final_task_overlap_with_source": 0,
  "meta_inner_learning_rate": 0.1,
  "meta_inner_steps": 2,
  "metrics": [
    {
      "SD_task_MAE": 0.05294242071038682,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.06946376376733883,
      "method": "Meta initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.05285529605638419,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.06706000737726465,
      "method": "Pooled initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.17222454659096953,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.19043853313022102,
      "method": "Zero initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.06610179041173624,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.07344585654081395,
      "method": "Frozen context network",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 13.979432060805442,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 2.430940013330514,
      "method": "Support least squares",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.04080748621581526,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.058928850802786426,
      "method": "Meta initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.03937100867387257,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.056907090908840476,
      "method": "Pooled initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.15607286794256506,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.16642999406290787,
      "method": "Zero initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.058183160018026675,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.06127119770913727,
      "method": "Frozen context network",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.12887250025244146,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.0637214745295285,
      "method": "Support least squares",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.02606075428358449,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.05306152624487899,
      "method": "Meta initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.025319713874145378,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.0515341286833396,
      "method": "Pooled initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.0924179250609573,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.14358837425730028,
      "method": "Zero initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.03419559525464833,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.04855782938057869,
      "method": "Frozen context network",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.005674962038408653,
      "domain": "New familiar-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.026494573312596147,
      "method": "Support least squares",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.09810594076779847,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.12172653530128322,
      "method": "Meta initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.09453945734690009,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.12788020159126856,
      "method": "Pooled initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.24995753727571085,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.261256019451254,
      "method": "Zero initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.11551007841178143,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.14893387839751798,
      "method": "Frozen context network",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 1.5696501801399179,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.6484055246253734,
      "method": "Support least squares",
      "query_cases_per_task": 32,
      "support_labels_per_task": 2
    },
    {
      "SD_task_MAE": 0.07962062850052704,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.09095742495320348,
      "method": "Meta initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.07711065374566038,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.09746807591629773,
      "method": "Pooled initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.19562736817337265,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.18523243240296577,
      "method": "Zero initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.08975828021529342,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.11964900934333556,
      "method": "Frozen context network",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.10299276932316462,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.06603920515678272,
      "method": "Support least squares",
      "query_cases_per_task": 32,
      "support_labels_per_task": 4
    },
    {
      "SD_task_MAE": 0.038305492302384996,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.0760107619446291,
      "method": "Meta initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.038604398359377824,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.08278096274096149,
      "method": "Pooled initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.0928191915593324,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 20,
      "mean_task_MAE": 0.1419523652806442,
      "method": "Zero initialization",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.03725072370009188,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.09868827884674877,
      "method": "Frozen context network",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    },
    {
      "SD_task_MAE": 0.009938800041851518,
      "domain": "Changed-prior tasks",
      "final_tasks": 40,
      "inner_gradient_steps": 0,
      "mean_task_MAE": 0.028919651968080447,
      "method": "Support least squares",
      "query_cases_per_task": 32,
      "support_labels_per_task": 8
    }
  ],
  "second_order_meta_gradients": true,
  "selected_context_update": 800,
  "selected_inner_steps": [
    {
      "method": "Meta initialization",
      "steps": 20,
      "support_labels": 2
    },
    {
      "method": "Meta initialization",
      "steps": 20,
      "support_labels": 4
    },
    {
      "method": "Meta initialization",
      "steps": 20,
      "support_labels": 8
    },
    {
      "method": "Pooled initialization",
      "steps": 20,
      "support_labels": 2
    },
    {
      "method": "Pooled initialization",
      "steps": 20,
      "support_labels": 4
    },
    {
      "method": "Pooled initialization",
      "steps": 20,
      "support_labels": 8
    },
    {
      "method": "Zero initialization",
      "steps": 20,
      "support_labels": 2
    },
    {
      "method": "Zero initialization",
      "steps": 20,
      "support_labels": 4
    },
    {
      "method": "Zero initialization",
      "steps": 20,
      "support_labels": 8
    }
  ],
  "selected_meta_update": 800,
  "source_labels_per_task": 64,
  "source_optimizer_updates": 800,
  "source_tasks": 70,
  "source_tasks_per_episode_batch": 8,
  "source_unique_labels": 4480
}
```

### code_166

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm 64 CPU; seed 4266.

```json
{
  "feedback_delay_events": 5,
  "final_admitted_labels": 355,
  "first_class2_generation": 2,
  "first_feedback_audit": [
    {
      "delay": 5,
      "feedback_event_admitted": 30,
      "prediction_event": 35
    },
    {
      "delay": 5,
      "feedback_event_admitted": 31,
      "prediction_event": 36
    },
    {
      "delay": 5,
      "feedback_event_admitted": 32,
      "prediction_event": 37
    },
    {
      "delay": 5,
      "feedback_event_admitted": 33,
      "prediction_event": 38
    },
    {
      "delay": 5,
      "feedback_event_admitted": 34,
      "prediction_event": 39
    }
  ],
  "future_generation_retention_cells_reported": false,
  "importance_labelled_gradient_evaluations": 128,
  "last_five_labels_unadmitted": 5,
  "metrics": [
    {
      "final_mean_retention_accuracy": 0.32962962962962966,
      "generation0_forgetting_from_best": 1.0,
      "gradient_updates_after_warmup": 1625,
      "method": "Naive",
      "peak_retained_labelled_records": 0,
      "prequential_generation0_accuracy": 1.0,
      "prequential_generation1_accuracy": 0.9666666666666667,
      "prequential_generation2_accuracy": 0.8666666666666667,
      "processed_examples_after_warmup": 1625
    },
    {
      "final_mean_retention_accuracy": 1.0,
      "generation0_forgetting_from_best": 0.0,
      "gradient_updates_after_warmup": 1625,
      "method": "Replay",
      "peak_retained_labelled_records": 64,
      "prequential_generation0_accuracy": 1.0,
      "prequential_generation1_accuracy": 0.9666666666666667,
      "prequential_generation2_accuracy": 0.7166666666666667,
      "processed_examples_after_warmup": 27625
    },
    {
      "final_mean_retention_accuracy": 0.3666666666666667,
      "generation0_forgetting_from_best": 1.0,
      "gradient_updates_after_warmup": 1625,
      "method": "Regularized",
      "peak_retained_labelled_records": 64,
      "prequential_generation0_accuracy": 1.0,
      "prequential_generation1_accuracy": 0.9666666666666667,
      "prequential_generation2_accuracy": 0.875,
      "processed_examples_after_warmup": 1625
    },
    {
      "final_mean_retention_accuracy": 1.0,
      "generation0_forgetting_from_best": 0.0,
      "gradient_updates_after_warmup": 1600,
      "method": "Periodic refit",
      "peak_retained_labelled_records": 355,
      "prequential_generation0_accuracy": 1.0,
      "prequential_generation1_accuracy": 0.9083333333333333,
      "prequential_generation2_accuracy": 0.7083333333333334,
      "processed_examples_after_warmup": 336000
    }
  ],
  "periodic_refit_every_delivered_labels": 40,
  "periodic_refit_updates": 200,
  "preallocated_classes": 3,
  "predictions_before_feedback": 330,
  "regularization_parameter_snapshots": 230,
  "regularization_strength": 50.0,
  "replay_capacity": 64,
  "retention_matrices": {
    "Naive": [
      [
        1.0,
        null,
        null
      ],
      [
        0.9333333333333333,
        1.0,
        null
      ],
      [
        0.0,
        0.0,
        0.9888888888888889
      ]
    ],
    "Periodic refit": [
      [
        1.0,
        null,
        null
      ],
      [
        1.0,
        1.0,
        null
      ],
      [
        1.0,
        1.0,
        1.0
      ]
    ],
    "Regularized": [
      [
        1.0,
        null,
        null
      ],
      [
        0.9333333333333333,
        1.0,
        null
      ],
      [
        0.0,
        0.1,
        1.0
      ]
    ],
    "Replay": [
      [
        1.0,
        null,
        null
      ],
      [
        1.0,
        1.0,
        null
      ],
      [
        1.0,
        1.0,
        1.0
      ]
    ]
  },
  "stream_events": 360,
  "warmup_observed_labels": 30,
  "warmup_processed_examples": 6000,
  "warmup_updates": 200
}
```

