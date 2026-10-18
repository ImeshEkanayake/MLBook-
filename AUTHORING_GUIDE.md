# Companion example authoring standard

Every code marker in the book should lead to a complete, understandable learning experiment. A notebook should help a reader operate a model, explain its mechanism, predict how a control might change behaviour, inspect the actual outcome and decide what to investigate next. A collection of unexplained estimator calls is insufficient. Use [code_001](CODE_EXAMPLES.md#code_001) as the working reference.

## Permanent identity and filenames

Allocate one unused permanent ID, such as `code_001`, in [CODE_EXAMPLES.md](CODE_EXAMPLES.md) and [examples.json](examples.json). Add an explicit HTML anchor `<a id="code_001"></a>` in the Markdown directory. Record chapter, numbered subtopic, title, notebook path, dataset provenance, dependencies, runtime, tested versions, verification date and status. IDs are independent of chapter numbering and must never be reassigned. If reorganizing, preserve the anchor and update both directory destinations.

Use `NNN_Chapter_CC_SS_Descriptive_Topic.ipynb`. The current reference is `001_Chapter_18_01_Decision_Tree.ipynb`; its book home is 18.1. The notebook extension already identifies the artifact, so adding the word `notebook` is unnecessary. Use a book link such as:

```markdown
[#code_001](https://github.com/ImeshEkanayake/MLBook-/blob/main/CODE_EXAMPLES.md#code_001)
```

A plain hashtag has no automatic remote destination. Publish and verify the registry and notebook before marking a book link as live. Registry status must distinguish prepared locally, executed locally and published, rather than presenting an intended URL as evidence of publication. A direct notebook or optional hosted-run link may supplement the stable directory link; it must resolve to an actual published file.

## The learning sequence inside each notebook

1. **Orientation and usage guide:** identify ID, chapter/subtopic, learning objectives, prerequisites, tested CPU/GPU assumptions, installation steps, expected runtime and data needs. Tell the reader how to run from a clean kernel and what the estimator's `fit`, `predict`, probabilities or other relevant outputs mean.
2. **Mechanism before switches:** explain how the model transforms input into output, using a simple conceptual diagram and a concrete worked example. State assumptions and distinguish architecture, objective, training, adaptation and task. Include mathematical detail where it clarifies the mechanism.
3. **Task and data:** define observation units, labels, prediction timing, feature meanings, units and sampling. Include provenance, generation code or a lawful accessible data reference. Make synthetic/simulated examples explicit and do not present them as empirical scientific findings.
4. **Evaluation contract and baseline:** define split units, metric, baseline, selection rule and final assessment boundary before inspecting results. Fit preprocessing and feature selection only within training data. Do not prescribe scaling universally; explain the selected model's input contract.
5. **A meaningful first fit:** show actual learned behaviour, API output shapes, an interpretable prediction and limitations. Use a tree view, response plot, graph messages, forecast or field diagram suited to the family. Give a textual alternative and numeric diagnostics where possible.
6. **Controlled sub-experiments:** cover exposed model parameters in a table with defaults, role, practical explanation, demonstration cell, diagnostic and prediction-before-running question. Change one factor at a time first. Distinguish meaningful model controls, randomness, resource controls and constraints; give a justified operational demonstration where an accuracy sweep would be misleading. Verify the installed constructor so coverage does not silently lag the API.
7. **Interactions and justified choice:** study a small motivated interaction separately. Predeclare the eligible candidates and selection rule, report resource limits, and evaluate stochastic variation with a modest fixed seed budget when relevant. Never select a best random seed and call that a general advantage.
8. **Final interpretation:** open the protected assessment only after choices are fixed. Report actual outputs, baseline comparisons, failure cases and uncertainty limits. Explain what the result supports and where new data, calibration, physical checks or independent replication are required.
9. **Exercises and next experiments:** include prediction-before-running prompts, underfit/overfit comparisons, label/noise or support challenges, controlled parameter changes and a real-world adaptation checklist. Put optional hints separately and avoid invented numeric answers. Tell readers to preserve a fresh assessment boundary when extending the example.
10. **Troubleshooting and evidence:** address likely data/API/runtime failures and meaningful diagnostics. Link official versioned documentation or primary papers; record the tested patch version even if a maintenance URL updates. Include an executed run report with exact versions and hardware, not a claim that unexecuted code works.

These are a coherent teaching progression, not a requirement to create ten shallow paragraphs. Develop substantial explanations around the model and experiments. The book's separate minimum of 500 substantive prose words per numbered manuscript subtopic remains intact; notebook code, captions, tables and diagrams do not count toward that manuscript floor.

## Self-containment and reproducibility

Put every import, data generator and helper definition in the notebook. Avoid private project imports, machine-specific paths, hidden prior cells, credentials, unannounced downloads or state inherited from another example. Ordinary runs should be offline where practical. Explain any unavoidable installation/download step before execution; never fetch it silently inside the model experiment. Use pinned dependencies, named seeds and bounded datasets. Print versions, hardware assumptions and elapsed time. Record actual tested scope rather than implying portability to untested platforms.

Use at least training/validation/final-test separation where appropriate; grouped, temporal, spatial or graph-dependent tasks need matching information boundaries. A training-only pruning path, label-derived encoding or representation fit must not see test labels. Do not repeatedly retune after the final assessment. Auxiliary datasets may isolate mechanisms if their purpose and assessment scope are clearly distinguished. Constrained examples must use features with meaningful ordering or valid physical semantics; a successfully accepted parameter is not sufficient evidence that the feature works.

For `code_001`, the live constructor assertion and final coverage assertion ensure all 13 controls were demonstrated. Weighted-leaf mass, entropy/log-loss equivalence, row disjointness, repeated-seed equality and monotonic shape checks test substantive properties. Future examples should use similarly targeted checks when they protect the learning claim; avoid tests that merely repeat implementation line by line.

## Visual explanation and accessibility

Use large clear groupings, short labels, simple meaningful icons and a consistent visual vocabulary for conceptual diagrams. Distinguish data flow, parameter updates, relations and causal arrows; define symbols locally. A sketched feel may support an overview, while numerical plots and physical schematics must be exact and reproducible whenever the claim depends on magnitude or geometry.

Use readable axes, units, legends, meaningful reading order and whitespace. Design for grayscale with shapes, patterns, line styles and explicit numbers; colour alone is insufficient. Add captions and nearby textual explanations, and retain numeric tables when they help nonvisual readers inspect results. State whether values are illustrative, generated or measured. Inspect representative rendered outputs at their intended size and repair clipping, crowded labels or misleading arrow endpoints. Do not substitute decorative pictures for a mechanism explanation or assert fixed learner-style categories.

## Acceptance and publication

Execute the complete notebook in a new kernel using the pinned environment. `python scripts/run_notebook.py` provides this for the reference example and stops on errors. Check every code cell ran, outputs reflect the code, no exceptions are hidden, the final test is used only for assessment, and coverage entries have real demonstrations. Inspect representative mechanism/model/experiment figures and final metrics. Keep reasonable executed outputs inline; regenerate bulky artifacts in ignored `build/` or `outputs/` and explain how.

Validate notebook format, registry uniqueness, file paths, explicit anchors and book URLs. Run a clean environment install when pinning new dependencies and record `pip check`. Commit only useful source, reference outputs and documentation. Exclude environments, caches, credentials, private data, model checkpoints and unrelated book files. Publish through a normal commit/push or review workflow with no force replacement, then verify the actual remote branch and contents before updating publication status. Annual update automation is outside this standard's present scope.

## Introductory concept notebooks

Task-framing chapters can use explicitly scoped concept laboratories rather than pretending to teach every estimator constructor. Map every major concept to an executable section, an exercise or a validated non-computational worksheet, as in [the Chapter 1 traceability guide](CHAPTER_01_GUIDE.md). Identify task/data/decision controls separately from model hyperparameters; document the fixed model settings actually used. Link full model-specific constructor laboratories to their later chapters, and never label a partial control demonstration as exhaustive API coverage. The general clean-kernel, self-containment, figure, evidence and final-assessment requirements still apply.
