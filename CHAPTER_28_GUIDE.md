# Chapter 28: Tabular and relational foundation models — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; task helpers and generated inputs are internal; declared checkpoint assets are separate. Examples 144/147 generate all inputs internally. Examples 145/146/148/149 need explicitly acquired, hash-verified public checkpoints before offline CPU inference; use the [asset guide and licence notices](CHAPTER_28_ASSETS.md). Example149 also uses three public tables bundled with scikit-learn. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_28_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 28.1 · What makes a reusable tabular model

- [Reuse learned weights without hiding the labelled context](notebooks/144_Chapter_28_01_reusable_predictor_pretraining_and_context.ipynb#pretraining-context-contract)
- [An amortized learning rule inherits its task distribution](notebooks/144_Chapter_28_01_reusable_predictor_pretraining_and_context.ipynb#reuse-and-prior-limits)

Declared mechanisms: actual cross-task synthetic pretraining, separate frozen labelled-context inference, heterogeneous feature-count masks, task-level development and assessment, parameter invariance and context permutation checks.

```bash
python scripts/run_notebook.py notebooks/144_Chapter_28_01_reusable_predictor_pretraining_and_context.ipynb
```

## 28.2 · The TabPFN family and prior-data learning

- [A family name does not identify the executed model](notebooks/145_Chapter_28_02_pinned_tabpfn_and_grouped_comparison.ipynb#pinned-tabpfn-contract)
- [Native fitting controls do not erase unequal upstream budgets](notebooks/145_Chapter_28_02_pinned_tabpfn_and_grouped_comparison.ipynb#checkpoint-context-and-evidence)

Declared mechanisms: actual pinned TabPFN v2 CPU inference, explicit offline checkpoint hash verification, whole-building development selection versus final assessment, native missing-value handling and fixed tree controls, unchanged pretrained weights with labelled context.

```bash
python scripts/run_notebook.py notebooks/145_Chapter_28_02_pinned_tabpfn_and_grouped_comparison.ipynb
```

## 28.3 · TabICL, TabFM and cross-table approaches

- [Read task support from the actual checkpoint](notebooks/146_Chapter_28_03_tabicl_tasks_and_checkpoint_contracts.ipynb#tabicl-and-model-report-contract)
- [Zero new-task gradient updates still use new-task supervision](notebooks/146_Chapter_28_03_tabicl_tasks_and_checkpoint_contracts.ipynb#family-reports-and-context)

Declared mechanisms: actual pinned TabICLv2 classifier and regressor, separate labelled-context task heads, checkpoint and source-package identity audit, development-selected native ensemble and tree controls, regression quantile assessment without calibration guarantee.

```bash
python scripts/run_notebook.py notebooks/146_Chapter_28_03_tabicl_tasks_and_checkpoint_contracts.ipynb
```

## 28.4 · Relational foundation models

- [Reusing a graph architecture is different from reusing pretrained weights](notebooks/147_Chapter_28_04_relational_pretraining_and_historical_queries.ipynb#relational-query-contract)
- [Preserve the distinction between representation and training provenance](notebooks/147_Chapter_28_04_relational_pretraining_and_historical_queries.ipynb#relational-pretraining-and-controls)

Declared mechanisms: actual own cross-database relational pretraining, historical event messages and parent-key gathers, frozen labelled-context prediction on new databases, per-database neural and flat-feature controls, future-row intervention with invariant admitted predictions.

```bash
python scripts/run_notebook.py notebooks/147_Chapter_28_04_relational_pretraining_and_historical_queries.ipynb
```

## 28.5 · Adaptation, input handling and resource limits

- [A frozen model still stores task data and computation state](notebooks/148_Chapter_28_05_context_caches_inputs_and_distillation.ipynb#context-cache-input-contract)
- [Cached inference and a student change different parts of the workflow](notebooks/148_Chapter_28_05_context_caches_inputs_and_distillation.ipynb#cache-and-distillation-limits)

Declared mechanisms: actual native mixed-type and missing-value handling, labelled-context size selection, native KV-cache numerical and storage audit, measured CPU fit and repeat-prediction observations, actual teacher-probability distillation with held-out evaluation.

```bash
python scripts/run_notebook.py notebooks/148_Chapter_28_05_context_caches_inputs_and_distillation.ipynb
```

## 28.6 · Benchmark evidence and applicability limits

- [A public benchmark score is not an independent-site guarantee](notebooks/149_Chapter_28_06_benchmark_provenance_and_applicability.ipynb#benchmark-evidence-contract)
- [Match the evidence unit, provenance and recommendation](notebooks/149_Chapter_28_06_benchmark_provenance_and_applicability.ipynb#bounded-benchmark-conclusions)

Declared mechanisms: actual pinned native model and tree comparisons across public and generated tables, separate random-row versus whole-entity assessment, equal explicit candidate counts without lifetime-compute claims, table-level paired uncertainty with named task families, actual final-label context leakage fixture and overlap hashes.

```bash
python scripts/run_notebook.py notebooks/149_Chapter_28_06_benchmark_provenance_and_applicability.ipynb
```

## Interpretation and boundaries

## Models, provenance and controls

Chapter28 distinguishes cross-task parameter training, labelled-context conditioning and parameter adaptation. The own small pretraining laboratories144/147 are not TabPFN, TabICL, TabFM, KumoRFM or OpenRFM reproductions. Actual named checkpoint inference occurs in145/146/148/149. All model outputs and comparisons are generated by executed current sources; no absent model is silently replaced. Nineteen exercises and the six-scope map retain all planned topics.

### Explicit artifacts and the unchanged prior environment

The prior80installed package versions remain unchanged, including CPython3.14.3, NumPy2.4.4, SciPy1.17.1, pandas3.0.3, Matplotlib3.11.0, scikit-learn1.9.0 and Torch2.14.1. Native TabPFN9.2.0 (released12October2026) and TabICL2.2.0 (2September2026), plus25transitive packages, were added with explicit constraints. All27additions have verified pre-cutoff release uploads; HF Hub1.33.0 follows the author repository's below-two compatibility constraint. Post-cutoff default selections were rejected before installation; certifi2026.10.18, pydantic-settings2.16.0 and skrub0.10.1 are fixed. The lock records the complete107-package environment. Pip check passes. New laboratories use explicit CPU float32 and one-thread settings; no GPU or private input is required.

Task generators and helpers are internal. Four notebooks require a separate, explicit one-time acquisition of three ungated public checkpoints, about254MB total. The acquisition script and every dependent notebook check immutable revision, SHA-256 and byte length; ordinary inference sets Hub offline mode. Missing assets fail with instructions. No automatic gated-terms acceptance, credentials, external inference service, hidden helper or model substitution is involved. Weights remain in ignored build/model-cache and are not redistributed.

- TabPFNv2default classifier: `Prior-Labs/TabPFN-v2-clf` revision `f851f2a3c941544733b712d8c0f96dfae9b28862`; `tabpfn-v2-classifier-v2_default.ckpt`;29,009,539bytes; SHA-256 `cf8c519c01eaf1613ee91239006d57b1c806ff5f23ac1aeb1315ba1015210e49`. The Hub object matches these actual bytes. Its v2PriorLabsLicense1.1 is distinct from later weight terms; the companion includes the licence and prominent **Built with PriorLabs-TabPFN** attribution. It does not distil TabPFN outputs into an unnamed distributed model.
- TabICLv2classifier: `jingang/TabICL` revision `4dcd344ece2c00be9e831fdd35bed57b5ad83e19`; `tabicl-classifier-v2-20260212.ckpt`;110,368,038bytes; SHA-256 `bdc7dbd5e4ff21f8f0456fcf90c6b7cdf72dbea960f2d05b19bec19f9b3d4ed0`.
- TabICLv2regressor: same repository/revision; `tabicl-regressor-v2-20260212.ckpt`;114,324,594bytes; SHA-256 `0db9cb538f114e79026bf08f45f41ad8dd7ad2de2aaca9a5ca8cd3bd9748ae7a`. Both TabICL hashes/sizes match Hub objects. Version labels do not by themselves assert first publication dates. The model card specifies BSD3-Clause, and the full author notice is retained; an unused forecast subdirectory has its own additional licence text.

The15October2026TabPFN repository snapshot already defaults to3.5; the executed v2 is deliberately historical, not misreported as current. TabICL source is pinned to9October2026, and TabFM source to18August2026. Google TabFM1.0.0's primary announcement is30June2026; its public metadata/config/licence were inspected, but restricted default weights were not acquired or executed. Their non-commercial/non-production and redistribution terms, including outputs, are separated from Apache source terms. No TabFM performance number is fabricated. Code/weight licensing, pretraining range, runtime support and measured workload are different records.

### Actual experiments

**144 · cross-task pretraining.** Original7170-parameter query-to-context attention predictor;1024source tasks,128development,128final and128changed-XOR tasks. Each task has64rows,32labelled context/32queries and2/4/6active numeric columns with explicit availability masks. All tasks/functions remain whole evidence units.2000Adam updates at0.002,16tasks/update; development selects1400. Familiar-task Brier: scratch0.25024, frozen pretrained0.12525, context prevalence0.25119, fixed per-task histogram0.13389. Changed-XOR:0.25049/0.20659/0.23844/0.20431. Context4/8/16/32rows gives0.28209/0.21143/0.15808/0.12525. Weight bytes remain unchanged by inference, context permutation agrees within float32 tolerance and label flipping changes logits. Padding does not confer arbitrary schema understanding. VisualA's lanes were changed to a clear three-row diagram and the full notebook rerun without changing numerical results.

**145 · native pinned TabPFNv2.**7,244,554parameters, numeric inputs with20source missing sensor records, generated building split40/10/10×10records (400/100/100), plus20changed-mechanism buildings/200records. Native ensemble candidates1/4 and four HGB rate0.05/0.1×leaves7/15candidates,100rounds, no early stopping, source-only native preprocessing. Development selects1ensemble and tree rate0.05/leaves7. Final Brier0.18300vs0.20216, AUC0.78733vs0.74175. Changed-mechanism Brier0.27231/0.31309and AUC0.43731/0.46471; the constant source-prevalence baseline has Brier0.14828there. Retain both failures. Actual network-parameter hashes remain unchanged across predictions, repeated probabilities agree and final data select nothing. The native package emits its CPU-above-200-record advisory twice. Messages are preserved, not suppressed; a rendering hook prints package-relative source locations to avoid publishing a local account path. The checkpoint's supported ceiling, its observed400-row run and the CPU advisory are different limits. A deprecated redundant auto_scale argument appeared only in an initial probe and was removed because explicit ensemble counts already fix the budget. No warning filter hides a current warning.

**146 · native TabICLv2classification/regression.**100buildings×8records split60/20/20 (480/160/160); six shared inputs, separately defined binary event and continuous cost outcomes. Distinct classifiers/regressors contain27,552,258/28,544,991parameters. Each task gets ensemble1/4and tree leaves7/15,100rounds/rate0.05; development selects1/7forboth. Final classification Brier0.18167/0.18717and AUC0.7905/0.76833; regression RMSE3.23098/3.55584cost units. Native regressor mean and0.1/0.9quantiles are actually called; nominal80% band coverage0.775and mean width8.1453. Sorting by reference outcome is display-only, not an inference input. Different target units are not pooled. A model-report table explicitly marks TabPFN as executed in145, TabICL as executed here and GoogleTabFM as documented but unexecuted.

**147 · own cross-database relational reuse.** Original7930-parameter timestamp-aware event pooling/parent-key gather/context model;512source databases,64development and32final. Each database has16parents,64members and384event rows;320pre-anchor reports are admitted.32context members have parents0–7and32queries parents8–15. Crucial temporal contract: context anchors−2with label report−0.8before the global request0; query anchors0with label report1.2after it. Features replay only history at each member's own anchor. Explicit assertions check both label maturity and report boundaries. This clarifies historical replay without changing learned numbers. A deliberate post-anchor event encodes the outcome but is excluded; mutating it leaves predictions exactly unchanged.1500pretraining updates0.002, batch8; development selects1500. Per-database fresh neural control gets100updates0.01. Final mean database Brier: pretrained0.14046, naive mean flat0.12972, engineered trend flat0.08873, fresh neural0.18320. Both flat controls beat the pretrained neural reference. Nonzero historical mean time lets even the naive mean retain some correlated slope information; it is not an intentionally uninformative baseline. The invalid future oracle's zero Brier is labelled invalid, not accepted performance. Relational/query diagram routes were corrected and all current code rerun. No native Kumo/OpenRFM execution or original benchmark gain is claimed.

**148 · native inputs, caches and distillation.** Generated cohorts480source/160development/160final, with shared building effects; source78numeric missing/42category missing, final16unseencomposite materials. Dataframe reaches native TabICL directly. Whole-building contexts64/128/256/480 yield development Brier0.23479/0.22375/0.21480/0.22374;256selects. Cached/uncached probabilities agree exactly in these runs, tested within float32 tolerance. Unique cache tensor storages are6/9/15/25.5MiB. Real fit times include local load/cache construction; prediction timing uses the median of three warmed calls on the same160rows. RSS is post-fit state of one process retaining multiple wrappers and allocator history, not isolated or peak model memory. At480rows measured fit uncached/cached≈0.0798/0.1760seconds; repeat prediction≈0.1254/0.0298seconds. These observations are not portable throughput claims.

The teacher is selected using256real context labels. A histogram regressor student fits2000teacher probabilities on480source feature rows plus1520new generated feature rows, discarding the latter's true labels. Its two leaf counts7/15select using160real development labels;15wins. Distillation fitting uses zero observed outcome labels directly, but teacher context and student selection explicitly use them. Final teacher/student/source480-label-tree Brier0.206978/0.206792/0.211125; student/teacher probability MSE0.00067679. Tiny single-seed differences are not precise improvements. An initial unpublished source redundantly drew an unused extra cohort and lacked the declared shared-building offset; it was cleaned up to generate source/development640once and final160once with an explicit shared offset. Same candidate budgets were rerun, with the old summary retained locally as148-before-cohort-cleanup.summary.json. The cached student is from TabICL, not restricted TabPFN outputs. Native fine-tuning is not executed or mislabelled as ordinary fit.

**149 · benchmark boundaries.** Actual TabICL and HGB on three public scikit-learn-bundled references (Iris, Wine, Wisconsin diagnostic) and twelve newly generated60-building×8tables. Public row splits are60/20/20; generated splits are40/10/10whole buildings. Six generated final cohorts keep the source mechanism; six shift an input/reverse a coefficient. Per-table candidates are1/4ensembles or7/15treeleaves (100rounds, rate0.05),60total candidates/30final comparison rows. Small public tasks90/106source rows extrapolate below the author's stated300-row pretraining-size range. Public upstream benchmark-development/pretraining overlap is unverified; generated tasks are not private-site evidence or a deployment-shift survey. Local source/final feature hashes have zero overlaps for all15valid tables, which does not certify upstream novelty.

Paired TabICL-minus-tree log loss across six familiar generated tables is−0.02130, table-bootstrap95% interval[−0.04144,−0.003693]; six changed-mechanism tables give+0.03765and[−0.03141,0.13897].2000resamples use whole tables, not correlated rows. Public results remain separate. An actual invalid context adds20final outcomes and matching features:20overlaps are detected; final log loss moves0.49368→0.48244and leaked-subset loss0.62283→0.58658. Those are contaminated scores despite frozen weights. The zero-overlap display axis was corrected to nonnegative count limits and the full notebook rerun; numerical results did not change.

### Reproduction and source boundaries

All six notebooks execute independently in fresh kernels, four code cells and two inline plots each. Checkpoints are explicitly acquired and verified by the companion script; bundled public table inputs come from the pinned scikit-learn package. No private datasets, hidden helpers, API key or GPU enter ordinary runs.145's two native advisories remain; all other current notebook stderr is empty. The explicit-asset registration/checker records those roles rather than falsely claiming every notebook needs no files.

Book figure generation reruns every current source cell and requires exact numeric RESULTS agreement. **148 is an intentional resource-observation exception:** all fitting, timings, cache construction and numerical assertions execute again, but the book timing plot reuses the fresh-kernel run's captured observations. Timings/RSS live outside deterministic RESULTS. No learned predictions or numeric checks are replayed from stored outputs. No other28resource exception is used.

Primary records include PFNs; original TabPFNv2Nature and pinned current-family documentation; author TabICL2025/TabICLv2ICML2026reports; GoogleTabFM30June2026announcement and pinned source/model card/licence; verified KumoRFM-2arXiv2604.12596and OpenRFM2606.04320. The old Kumo PDF URL still redirects to vendor documentation and is not represented as a verified archived paper. All publication/model artifact dates and author lists are recorded. Access21October2026 does not alter the18October2026literature cutoff. The book's own generated controls and native results are separated from developer benchmark claims, hosted-service availability and unexecuted named models.
