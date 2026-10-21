# Chapter 30: LLMs and typed decision models — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Use the [dedicated Python 3.12 runtime](CHAPTER_30_RUNTIME.md). Five examples require [explicit public checkpoint acquisition](CHAPTER_30_ASSETS.md);157 generates its own fitted model. Ordinary inference is offline and CPU-only. Use the [quickstart](README.md), [dedicated pinned environment](requirements-chapter30-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_30_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 30.1 · LLMs for structured and scientific tasks

- [Ask an actual instruction model a bounded structured question](notebooks/155_Chapter_30_01_structured_records_and_native_language_prediction.ipynb#record-to-language-prediction)
- [Keep model judgment and software authority separate](notebooks/155_Chapter_30_01_structured_records_and_native_language_prediction.ipynb#serialization-and-action-authority)

Declared mechanisms: actual pinned instruction-LLM prediction from bounded generated states, units and explicit choice-rule serialization, free generation versus conditional allowed-label projection, syntax correctness and probability mass measured separately, frozen weights and evidence-only field handling.

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/155_Chapter_30_01_structured_records_and_native_language_prediction.ipynb
```

## 30.2 · Prompting, context and adaptation

- [Compare prompts without moving the evidence boundary](notebooks/156_Chapter_30_02_prompt_context_and_source_example_policies.ipynb#fixed-access-prompt-comparison)
- [Examples are supervised information even when weights are frozen](notebooks/156_Chapter_30_02_prompt_context_and_source_example_policies.ipynb#context-budget-and-adaptation)

Declared mechanisms: actual fixed-checkpoint prompt comparison on unseen building groups, equivalent JSON and prose measurement representations, zero-example random-example and source-only nearest-example policies, source-fitted retrieval scale and explicit label-access audit, weight invariance and prompt-token budgets without native fine-tuning claims.

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/156_Chapter_30_02_prompt_context_and_source_example_policies.ipynb
```

## 30.3 · Typed decisions and System One terminology

- [Train three actual heads without claiming an open-language interface](notebooks/157_Chapter_30_03_typed_heads_schema_and_action_policy.ipynb#own-typed-interface)
- [A typed interface does not create a new scientific task category](notebooks/157_Chapter_30_03_typed_heads_schema_and_action_policy.ipynb#typed-contract-and-policy)

Declared mechanisms: actual own multihead neural prediction from structured generated states, separate choice ordinal-score and yes-no output contracts, whole-building training and development selection, schema-valid yet incorrect counterexample and rejected invalid fixtures, deterministic software policy separated from model judgment.

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/157_Chapter_30_03_typed_heads_schema_and_action_policy.ipynb
```

## 30.4 · Jev, Laya and Kev as concrete families

- [Execute two native families and identify the documented third](notebooks/158_Chapter_30_04_native_laya_kev_and_documented_jev.ipynb#native-decision-families)
- [Preserve release, runtime and confidence boundaries](notebooks/158_Chapter_30_04_native_laya_kev_and_documented_jev.ipynb#family-provenance-and-limits)

Declared mechanisms: actual pinned Laya and Kev CPU inference with required Qwen base, native choice ordinal-score and noul output contracts, same generated states and literal questions across executed families, unused dummy label metadata verified absent from predictive inputs, documented unexecuted Jev and explicitly bounded developer claims.

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/158_Chapter_30_04_native_laya_kev_and_documented_jev.ipynb
```

## 30.5 · Evaluation, calibration and deferral

- [Fit calibration and select review thresholds before opening final outcomes](notebooks/159_Chapter_30_05_calibration_and_validation_chosen_deferral.ipynb#held-out-calibration-and-deferral)
- [A confident answer does not repair absent measurements](notebooks/159_Chapter_30_05_calibration_and_validation_chosen_deferral.ipynb#missing-evidence-is-a-policy-input)

Declared mechanisms: actual native Laya probabilities versus a fitted numeric tree control, whole-building source calibration development and final evidence roles, calibration-only temperature selection and development-only deferral, option-order and missing-evidence diagnostics, returned confidence separated from observed correctness and policy authority.

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/159_Chapter_30_05_calibration_and_validation_chosen_deferral.ipynb
```

## 30.6 · Scientific workflows and security boundaries

- [Let a model propose a calculation; make software check its authority](notebooks/160_Chapter_30_06_verified_scientific_tools_and_security_boundaries.ipynb#model-proposal-and-verified-tool)
- [A scientific workflow records proposals, evidence and checks separately](notebooks/160_Chapter_30_06_verified_scientific_tools_and_security_boundaries.ipynb#auditable-authority-boundary)

Declared mechanisms: actual small language model proposes bounded mechanical tool choices, typed whitelist and evidence consistency gate separate from model text, independent Euler-Bernoulli finite-element verification of exact formulas, generated adversarial note diagnostic and private-field minimization, auditable numeric inputs without arbitrary code or external actions.

```bash
build/chapter30-runtime/bin/python scripts/run_notebook.py notebooks/160_Chapter_30_06_verified_scientific_tools_and_security_boundaries.ipynb
```

## Interpretation and boundaries

### Execution and runtime boundaries

Chapter 30 uses a separate CPython 3.12.13 environment because upstream Kev explicitly excludes3.14 and requires Torch below2.9. Actual pins include Torch 2.8.0, NumPy 2.5.3, scikit-learn 1.9.1, Laya 0.4.11 and Kev 0.1.0 from immutable15 October 2026 source. All installed release selections were checked against the 18 October 2026cutoff; six newer resolver defaults were replaced before installation. The earlier119-package environment is unchanged. The dedicated requirements/lock and runtime guide are publication artifacts. All six notebooks execute independently, four code cells and two inline figures each, with explicit one-thread CPU float32.

All task records are generated. Five notebooks require declared public checkpoints after explicit acquisition;157 needs no checkpoint. All33 files across four repositories are size/SHA-256 verified, inference is offline and no weights are redistributed. No Jev hosted call, API credential, spending, private input or external action occurs. Laya/Kev are actual native implementations; the original157network is explicitly distinct and supports only fixed numeric heads. SmolLM is actually loaded and called, not replaced with a rule or canned output.

### Retained results and counterexamples

155: twelve free generations are valid and four correct. Constrained projection on 24 cases also has one-third accuracy; mean retained vocabulary mass0.227543. There is no observed syntax advantage in this run.156: all six predeclared representation/example policies are reported. Source-only retrieval,45 source states15 groups and24 final states8 groups; generated group labels are not a claim of realistic within-building correlation. No final labels are admitted to prompts; all six configurations remain visible without final-set selection. Nearest JSON accuracy 23/24versus nearest prose16/24 is local evidence, not a universal representation ranking.

157: original shared trunk with three fixed numeric heads,80 source/20 development/20 final groups×6 members,600 offered Adam updates, development checkpoint selected at50. Four invalid fixtures rejected; schema-valid wrong fixture accepted. Priority accuracy 0.825; severity-position MAE 0.285161; event Brier 0.065367. Fixed0.7routing gate is illustrative, not validated. All missing evidence routes to review.158: actual native models on 24same states/questions. Laya choice accuracy 0.25/Kev0.541667; ordinal MAE 0.525258/0.564146; yes-no Brier 0.011755/0.044187. No invented Jev score. Native rounded distributions normalized only for probability metrics. Kev's constant dummy training/benchmark labels do not affect predictive encoded inputs, verified by mutation. All weights unchanged and no admitted state truncation.

159:120 groups×3 members;60 source tree training/20 calibration/20 development/20 final. Temperatures selected only by calibration NLL; deferral only by development. Laya has no eligible threshold, defers all 60 final records; selective error is undefined, not zero. Final overall accuracy 0.183333, Brier 0.810014→0.691919 after temperature 4. Tree final accuracy 1.0 and all 60accepted, Brier 0.000124→0.001728 after calibration-selected temperature 1.5; adverse final probability change is retained. Order changes4/60decisions, removing crack width8/60; all 60incomplete states independently reviewed. Native returned confidence is a distribution statistic, not correctness probability, and is not compared across families. No final selection labels used.

160:24 cases, two load types, actual model chooses correct tool12/24 in clean and adversarial-note conditions. Evidence gate admits12 and rejects/reviews12, retaining wrong proposals. Sixteen-element independently assembled beam FE verifies all 24analytic cases, max relative difference6.3101e-12. No choice change for this one attack; no universal security claim. Whitelist rejects unauthorized tool independently. Generated contact fields excluded, no external actions. Audit hashes support reproducibility and do not anonymize private evidence. Numerical agreement validates implementations under assumed linear cantilever mechanics, not field assumptions.

### Native diagnostics and source attribution

All native diagnostics remain visible in notebook stderr: Torch's macOS redirect-support note, optional IProgress/TqdmWarning, Laya's invalid choice:11+temperature bucket warning and Kev's two CPU reference-kernel notes where applicable. The affected Laya bucket is unused by the three-choice experiments, and checkpoint bytes are not edited. Only progress displays are disabled; warnings/messages are not filtered. Stable warning locations avoid account-specific paths. No warning-free output claim is made.

Jev's interface and System One terminology come from developer documentation accessed21 October 2026; live page access is not an archived snapshot. Native Kev source is pinned15October and Laya source inspected18 October; installed Laya release17 October is identified separately. Public artifact revisions predate the cutoff. Developer speed/quality claims remain attributed and unreplicated. Native Laya confidence differs from TypeSafe/Kev formulas; returned field names alone do not establish equivalence. No unsupported multimedia or arbitrary-question capability is inferred from a family name.

Every code cell is re-executed by the book figure producer, with exact numeric RESULTS agreement against successful fresh-kernel summaries. No resource/timing replay exception is used. Observed runtimes are outside deterministic result dictionaries. Final visual review, exact PDF hash, earlier-page preservation and remote publication checks are recorded separately after compilation.
