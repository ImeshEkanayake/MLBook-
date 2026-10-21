# Chapter 31: Learning with limited labels and changing tasks — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_31_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 31.1 · Semi-supervised learning

- [Four real fitting mechanisms with one scarce-label budget](notebooks/161_Chapter_31_01_semi_supervision_and_unlabelled_regime_assumptions.ipynb#semi-supervised-assumptions)
- [Supervision sources have different epistemic roles](notebooks/161_Chapter_31_01_semi_supervision_and_unlabelled_regime_assumptions.ipynb#derived-inferred-and-acquired-targets)

Declared mechanisms: actual supervised pseudo-label graph and mean-teacher consistency fitting, same scarce source labels and source-only scaling, whole-building labelled unlabelled development and final roles, matched versus changed unlabelled operating regimes, pseudo-label mistakes and regime-specific final assessment retained.

```bash
python scripts/run_notebook.py notebooks/161_Chapter_31_01_semi_supervision_and_unlabelled_regime_assumptions.ipynb
```

## 31.2 · Self-supervised objectives for structured data

- [Compare objectives through a separate labelled task](notebooks/162_Chapter_31_02_self_supervised_objectives_and_augmentation_validity.ipynb#self-supervised-pretext-and-downstream)
- [A pretext success can discard the downstream target](notebooks/162_Chapter_31_02_self_supervised_objectives_and_augmentation_validity.ipynb#augmentation-and-identifiability)

Declared mechanisms: actual masked denoising contrastive and temporal pretraining, frozen representation evaluation at two downstream label budgets, random encoder and raw numeric controls with development-only ridge selection, source-only feature transforms and whole-building final isolation, destructive amplitude invariance tested with an exact target collision.

```bash
python scripts/run_notebook.py notebooks/162_Chapter_31_02_self_supervised_objectives_and_augmentation_validity.ipynb
```

## 31.3 · Active learning and experimental design

- [Acquire observed labels without acquiring a biased test set](notebooks/163_Chapter_31_03_active_learning_costs_and_independent_evaluation.ipynb#sequential-costed-acquisition)
- [The queried sample changes with the policy](notebooks/163_Chapter_31_03_active_learning_costs_and_independent_evaluation.ipynb#acquisition-is-not-evaluation)

Declared mechanisms: actual sequential random uncertainty diversity and committee acquisition, whole-building oracle admission and explicit cost budget, same initial labels and independent final population across policies, four generated cohort seeds and descriptive policy variability, query sample separated from deployment evaluation.

```bash
python scripts/run_notebook.py notebooks/163_Chapter_31_03_active_learning_costs_and_independent_evaluation.ipynb
```

## 31.4 · Transfer and multitask learning

- [Sharing changes gradients, capacity and supervision](notebooks/164_Chapter_31_04_multitask_scales_negative_transfer_and_adaptation.ipynb#multitask-loss-and-transfer)
- [A small adapter still consumes target labels and selection evidence](notebooks/164_Chapter_31_04_multitask_scales_negative_transfer_and_adaptation.ipynb#bounded-parameter-adaptation)

Declared mechanisms: actual shared-trunk and separate-model training on two mechanical teaching targets, raw versus source-scaled joint losses and task-specific assessment, source-family and changed-material whole-building evaluation, actual head-only and rank-one feature adaptation with frozen-backbone hashes, target fitting labels and target development outcomes counted separately.

```bash
python scripts/run_notebook.py notebooks/164_Chapter_31_04_multitask_scales_negative_transfer_and_adaptation.ipynb
```

## 31.5 · Meta-learning, few-shot and in-context adaptation

- [New tasks require new mechanisms, not only new rows](notebooks/165_Chapter_31_05_meta_learning_few_shot_and_fixed_weight_context.ipynb#task-episodes-and-meta-objective)
- [An episode has an information boundary of its own](notebooks/165_Chapter_31_05_meta_learning_few_shot_and_fixed_weight_context.ipynb#global-weights-and-request-conditioning)

Declared mechanisms: actual second-order gradient-based meta-training across task episodes, pooled source fitting scratch adaptation and support-only least-squares controls, actual frozen context network maps support statistics into task predictions, new task identities and changed task-parameter prior evaluated separately, development-only adaptation-step selection and audited source label access.

```bash
python scripts/run_notebook.py notebooks/165_Chapter_31_05_meta_learning_few_shot_and_fixed_weight_context.ipynb
```

## 31.6 · Continual learning and changing environments

- [Predict before the outcome enters training](notebooks/166_Chapter_31_06_continual_replay_regularization_and_delayed_feedback.ipynb#ordered-stream-and-feedback)
- [A periodic full refit is not an online parameter update](notebooks/166_Chapter_31_06_continual_replay_regularization_and_delayed_feedback.ipynb#retention-and-resource-boundaries)

Declared mechanisms: actual prequential predictions before five-event-delayed feedback, naive online bounded reservoir replay EWC-style regularization and periodic full refit, three ordered sensor generations with a newly observed third class, retention matrices restricted to already arrived generations, raw-record storage gradient updates and processed-example budgets measured.

```bash
python scripts/run_notebook.py notebooks/166_Chapter_31_06_continual_replay_regularization_and_delayed_feedback.ipynb
```

## Interpretation and boundaries

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
