# Chapter 6: concept-to-code guide

Permanent IDs code_027–code_031 map one-to-one to sections 6.1–6.5. Read the prediction prompt, run every cell in a fresh kernel, then interpret outcomes before changing settings. All imports, helpers and generated data live inside each notebook. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [measured execution evidence](CHAPTER_06_EXECUTION.md). Ordinary execution requires no files, downloads, credentials or GPU.

## 6.1 · Learning from labelled examples

- [availability](notebooks/027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb#availability): Prediction-time features versus training-time label eligibility; pending cases are not negatives.
- [formulations](notebooks/027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb#formulations): Actual scalar, binary and vector fits, training-only scalers and declared fixed controls.
- [final](notebooks/027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb#final): Separate metrics and training-only baselines, with fixed-rule final assessment.
- [exercises](notebooks/027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb#exercises): Label delays, repeated cases, physical output structure and decision thresholds.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/027_Chapter_06_01_Learning_From_Labelled_Examples.ipynb
```

## 6.2 · Learning structure without target labels

- [objectives](notebooks/028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb#objectives): Different clustering, density and representation objectives; external labels kept out of fits.
- [autoencoder](notebooks/028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb#autoencoder): Actual nonlinear compression training, decoder finite differences and reconstruction curve.
- [interpretation](notebooks/028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb#interpretation): External regime/finding agreement, final reconstruction baseline and fixed-coordinate density stress.
- [exercises](notebooks/028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb#exercises): Nuisance regimes, bottleneck identity shortcut, unit/density changes and consequence.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/028_Chapter_06_02_Learning_Structure_Without_Target_Labels.ipynb
```

## 6.3 · Self-supervision and partial supervision

- [masking](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb#masking): Historical source-only scaling, missing-value indicators and real masked pretraining.
- [contrastive](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb#contrastive): Declared noisy-view positives, normalized contrastive loss, collapse identity and consistency diagnostics.
- [adaptation](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb#adaptation): Forty human labels; frozen head versus actual copied-encoder fine-tuning.
- [partial](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb#partial): Training-only pseudo-label provenance, confidence/agreement filter and weighted one-pass student.
- [final](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb#final): Predeclared final log losses retained even when added adaptation does not help.
- [exercises](notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb#exercises): Future-data leakage, invalid positives/consistency, confidence selection and scratch baseline.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/029_Chapter_06_03_Self_Supervision_And_Partial_Supervision.ipynb
```

## 6.4 · Transfer, adaptation and learning across tasks

- [tasks](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb#tasks): Source-task generation, pooled rule and actual multitask shared slope with task heads.
- [meta](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb#meta): Post-adaptation source-query objective, real meta-training and finite-difference meta-gradient.
- [context](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb#context): Actually pretrained bandwidth, fixed-state context inference and label-shift identity.
- [final](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb#final): Task-disjoint support/query assessment, state preservation and differing update budgets.
- [shift](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb#shift): Reversed-slope stress and the need for matched target-only transfer baselines.
- [exercises](notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb#exercises): Task diversity, state inventories, out-of-context queries and shared versus meta objectives.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/030_Chapter_06_04_Transfer_Adaptation_And_Learning_Across_Tasks.ipynb
```

## 6.5 · Learning from actions and overlapping categories

- [bandit](notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb#bandit): Actual reward learning under action selection, exploration and action-specific counts.
- [final](notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb#final): Fresh frozen-policy simulator assessment and offline missing-action evidence.
- [sequential](notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb#sequential): Known-model value iteration and Bellman check, explicitly separate from empirical learning.
- [taxonomy](notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb#taxonomy): Four-axis illustrative transformer/policy worksheet and the distinct executed bandit.
- [exercises](notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb#exercises): Exploration failure, changed rewards, offline support and evidence needed for an actual policy.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/031_Chapter_06_05_Learning_From_Actions_And_Overlapping_Categories.ipynb
```

## What is implemented and what is a worksheet

Actual learned mechanisms include supervised scalar/binary/vector rules, K-means/GMM, a nonlinear autoencoder, masked encoder pretraining, sparse-label fine-tuning, weighted pseudo-label fitting, multitask shared parameters, exact linear one-step meta-training, a pretrained contextual kernel and a contextual bandit. The contrastive cell evaluates an actual objective using an encoder trained by masking; it does not train by contrastive loss. The Markov model is explicitly known and solved by planning. The transformer/offline-policy card is a validated non-computational design worksheet, not an executed transformer or offline policy.

These scoped concept laboratories disclose their fixed controls rather than claim exhaustive constructor coverage. Final outcomes already read are spent for redesign. Unlabelled final-input access, future measurements, unsupported actions and delayed labels require explicit contracts. Synthetic reconstructions, grouping agreement, reward means and solver residuals do not establish real engineering performance or causal policy benefit. Four complementary axes—architecture, objective, adaptation and task—allow overlapping descriptions without forcing exclusive categories.
