# Chapter 1 execution evidence

**Date:** 18 October 2026 (Australia/Melbourne). **Status:** executed locally, awaiting remote verification.

All five new notebooks were executed from first to last cell in fresh kernels using the existing `scripts/run_notebook.py` and unchanged pinned environment. They require no external data, keys, project imports or network downloads during an ordinary run. `code_001` is unchanged; its separate [reference report](EXECUTION_REPORT.md) remains valid. These are concept notebooks, not full constructor laboratories for every estimator named in Chapter 1.

| Example | Section | Executed code cells | Inline figures | Wall seconds incl. kernel lifecycle |
| --- | --- | ---: | ---: | ---: |
| [code_002](CODE_EXAMPLES.md#code_002) | 1.1 | 5 | 1 | 1.296 |
| [code_003](CODE_EXAMPLES.md#code_003) | 1.2 | 5 | 2 | 5.389 |
| [code_004](CODE_EXAMPLES.md#code_004) | 1.3 | 5 | 2 | 1.956 |
| [code_005](CODE_EXAMPLES.md#code_005) | 1.4 | 4 | 2 | 1.825 |
| [code_006](CODE_EXAMPLES.md#code_006) | 1.5 | 5 | 2 | 1.298 |

Total: **24 new code cells and 9 inline figures**. Runtime is an observation on this machine, not a performance guarantee. CPython 3.14.3, scikit-learn 1.9.0, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3 and Matplotlib 3.11.0 were recorded by each kernel. Full pins remain in [requirements-lock.txt](requirements-lock.txt); hardware is macOS ARM64 CPU.

## Actual results and checks

- **code_002:** the event-only availability rule admits `late_sensor_revision`; checking availability removes it and the future inspection field. On the four member-week rows, the 3-day horizon has one positive and the 7-day horizon has two. Keys, repeated members, boundary inclusion and deliberately incomplete follow-up are checked. A mixed timestamp-format parsing defect was corrected before the successful complete run.
- **code_003:** fixed supervised models use disjoint 60/20/20 row splits without hyperparameter search. Sealed final regression MAE is 0.312459 synthetic mm versus 0.860957 for the mean baseline; classifier log loss is 0.507663. Precision at 20 is 0.75000, recall at 20 is 0.15625. Clustering does not fit regime labels. A separate reference-fit anomaly model scores injected cases; its easy-case AUC of 1.0 does not establish real-world detection reliability.
- **code_004:** paired scenario correlation is 0.957300; independent-column correlation is 0.000644. Units and endpoint displacement are asserted for the static ideal series-spring model. Three distinct stiffness pairs have equal endpoint compliance and different internal displacements. The positive fitted compliance is estimated only on calibration loads, with a fixed held-out force diagnostic. Recovery of individual stiffnesses is explicitly not claimed.
- **code_005:** static expected costs are {'expected_benefit': 19.9, 'none': 30.5, 'risk_only': 21.1}, in invented loss units conditional on assumed prevention. The battery comparison gives {'idle': 19.0, 'myopic': 11.0, 'planned': 10.0}; all policies have the same initial/terminal energy, published tariff information, capacity and power limits. The planner checks 99 feasible strings. It is a finite-horizon planning baseline, not a trained RL algorithm.
- **code_006:** four members, eight sensors and 48 readings preserve entity/reading distinctions. One-to-many cardinality, symmetric zero-diagonal adjacency, consistent permutation and same-mean/variance opposite-order sequences are checked. Preprocessing, pretraining, context adaptation and fine-tuning appear in an explicitly validated operation worksheet. Dense storage is reported for this tiny graph, not advertised as a scalable graph implementation.

Notebook schemas, sequential execution counts, absence of error outputs, source self-containment, local links and permanent IDs are validated. Representative timeline, regression/ranking, generation/inverse, policy and representation outputs are visually reviewed. The chapter's numerical statements come from the recorded run or exact declared algebra. Scientific-domain claims remain bounded by stated toy assumptions; no empirical building reliability or causal prevention effect is established.

These observations support Chapter 1 teaching mechanisms. They do not establish model optimality, population performance, physical correctness beyond the model, or exhaustive literature coverage. The LaTeX manuscript and book figure sources remain in the separate local book project and are not published in this companion-code repository.
