# Chapter 42: Monitoring and maintaining models — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_42_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 42.1 · What to monitor and when labels arrive


Declared mechanisms: actual request ledger with invalid deferred scored denominators and daily input-health summaries, as-of delayed-label joins retaining original prediction-time probabilities, fixed maturity horizon separated from label-dependent early arrivals and privileged full truth, delayed-outcome monitoring-loop visual with explicit fictional owners and response thresholds.

```bash
python scripts/run_notebook.py notebooks/221_Chapter_42_01_daily_input_health_and_asof_delayed_outcome_monitoring.ipynb
```

## 42.2 · Drift, degradation and alert quality


Declared mechanisms: actual pooled-reference and season-matched two-sample distribution tests, same-feature conditional response change with stable prediction distribution but degraded Brier, predeclared fixed-family Bonferroni thresholds and independent-uniform null monitoring simulation, delayed quality evidence separated from nuisance seasonal input alerts.

```bash
python scripts/run_notebook.py notebooks/222_Chapter_42_02_seasonal_drift_conditional_degradation_and_repeated_alerts.ipynb
```

## 42.3 · Feedback loops and changing labels


Declared mechanisms: actual high-score selection with zero outcome support in low-score region, positive-probability audit sampling with known propensity weighted loss and independent assessment, observed selected retraining versus zero-filled-label contamination control, repair-induced outcomes separated from untreated potential outcomes and label-version changes.

```bash
python scripts/run_notebook.py notebooks/223_Chapter_42_03_selective_labels_audit_propensities_and_repair_feedback.ipynb
```

## 42.4 · Retraining, updating and validation


Declared mechanisms: actual old frozen Platt recalibration full refit recent refit and incremental SGD after sensor-generation change, mature chronological update development and untouched final cohorts with rolling-origin checks, scheduled versus evidence-triggered update decisions with fixed development acceptance criteria, versioned candidate gate and actual retained-prior rollback visual.

```bash
python scripts/run_notebook.py notebooks/224_Chapter_42_04_recalibration_refit_incremental_update_and_fixed_release_gate.ipynb
```

## 42.5 · Versioning, incident response and retirement


Declared mechanisms: actual canonical raw snapshot data feature model and decision version binding, replay of historical unit-conversion defect and threshold decision with exact retained parameters, latest-version reconstruction counterexample and repaired-schema validation, fictional incident ownership suspension and task-based retirement with rejected future use.

```bash
python scripts/run_notebook.py notebooks/225_Chapter_42_05_versioned_incident_snapshot_replay_repair_and_retirement.ipynb
```

## Interpretation and boundaries

# Chapter 42 mechanisms, controls and interpretation

Five original laboratories retain all five scopes and both visual briefs: **20 fresh-kernel code cells and 10 embedded figures**. Imports, helpers and generated inputs are internal. Ordinary execution is offline and CPU-only, without files, credentials, a GPU or new dependencies/assets. Runtime: Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0 and threadpoolctl 3.7.0. Complete outcomes and potential outcomes are privileged simulator audit controls. Operational comparisons respect declared availability. Owners and approvals are fictional fixtures. Access/execution: 22 October 2026, Australia/Melbourne; literature cutoff: 18 October 2026.

- **221 — monitoring clocks.** A logistic model fits 1,000 source records; 6,000 requests span 120 days. Missingness increases from 2% to 18% at day 40; the response law reverses at day 65. There are 5,132 scored, 814 invalid and 54 deferred requests. Latencies are generated scenario values, not measured service timings. A seven-day outcome window precedes reporting delays of three additional days for positives and seven for negatives. At day 80, 3,079 scored labels are visible, but only 2,997 belong to the conservative fourteen-day mature cohort. Recent days 67–73 contain 287 scored requests and 82 visible labels, all positive, versus complete privileged positive frequency 0.529617. Visible Brier is 0.355795 versus privileged full-cohort 0.339970. Pending outcomes are never assigned zero. Original probabilities and IDs support as-of joins; the last partial mature cohort contains 164 cases with Brier 0.276617. Fictional owner/cadence/response specifications cover score coverage below 0.9, timeout fraction above 0.02 and mature Brier above 0.27. These thresholds are teaching choices. Visual A shows input, prediction, action, outcome, reporting and maturity clocks.
- **222 — drift and alert quality.** Reference and current years each have 52 weeks of 100 independent records. Seasonal temperature is irrelevant to the response; severity drives the logistic event. Actual pooled-temperature KS tests alert in all 52 weeks under nominal and fixed-family Bonferroni rules. Same-phase references produce two nominal and zero corrected alerts. Each route has 52 predeclared looks; their null populations differ. A known response-law reversal at week 32 leaves inputs stable but raises Brier from 0.170982 to 0.478830. Mean predictions remain 0.488548/0.497140. A three-week label delay makes the first fixed-threshold 0.30 quality alert available at week 35. In 2,000 explicit independent-uniform null years, any nominal alert occurs in 0.9405, versus analytic 0.930557; corrected simulation frequency is 0.056, a finite Monte Carlo observation rather than a theoretical failure. Fixed-family control requires valid individual p-values and does not establish indefinite sequential validity. No ADWIN implementation is claimed.
- **223 — selective labels and feedback.** The model fits 1,000 complete source labels, then scores 4,000 candidates with a new low-severity risk term. Deterministic p≥0.6 inspection observes 1,522 labels: observed Brier 0.169399 versus complete privileged 0.249661, with zero low-score support. A separate generated audit samples high scores with probability one and low scores with probability 0.15, observing 1,884 labels. Its unweighted Brier is 0.194977 and known-propensity Horvitz–Thompson estimate 0.246976. Positive known support is essential; weighting cannot recover arbitrary unknown selection or zero-support regions. On 2,000 independent final cases, frozen/selected/audit-weighted/wrong zero-filled update Brier is 0.246126/0.250162/0.223609/0.359562. Final results do not select a release. Repair is assigned to 1,035 selected cases with probability 0.7; untreated selected positive frequency 0.764783 becomes 0.254271 after the policy. Actions, observation and target versions are logged. Full potential outcomes are simulator controls, not identified field counterfactuals. No consequential real randomization, contraction method or performative-convergence implementation occurs.
- **224 — updates and gate.** Eight independent 200-row blocks provide source 0–2 (600 rows), mature update 3–4 (400), development 5 (200) and untouched final 6–7 (400). The new sensor negates feature zero and adds 0.8 from block three; latent response is unchanged. Actual alternatives are frozen logistic, unconstrained sigmoid old-logit remapping, full old-plus-new refit, recent-only refit and SGD partial updates with an old-source fixed scaler. Remapping learns a negative slope and reverses ordering; it is broader than increasing calibration or positive-temperature scaling. Historical rolling Brier is 0.179815 before the boundary and 0.454545 at it, using no future information. Development selects recent refit at 0.192206 versus frozen 0.409977, under a fixed improvement≥0.01/Brier<0.25 gate. Final Brier is frozen 0.413714, remapped 0.222103, full 0.260416, recent 0.193326 and incremental 0.232649. Scheduled investigations and old mature-loss>0.30 triggers both occur at blocks three/four; neither bypasses validation. Injected rollback exactly restores retained old predictions, which does not establish their scientific adequacy for the new sensor. Visual B shows roles, gate, release fixture and recoverable prior; no actual human approval occurs.
- **225 — incident and retirement.** A 1,200-row source model uses kN load and age in decades. An authored eight-kN/thirty-year finding fixture passes through defective feature-v1, which always divides load by 1,000. Historical probability is 0.087094 with no alarm at 0.5; corrected feature-v2 gives 0.932916. Canonical raw snapshot, digest, data/schema, feature, model and decision versions are retained. Exact replay succeeds; replacing history with the latest feature would conceal the miss. Corrected eight-kN/eight-thousand-N equivalence and unknown-unit rejection pass. Fictional owner transitions are active → suspended → repair_verified → retired. A requested immediate structural-clearance use exceeds annual finding-priority evidence and returns rejected with no probability. The original snapshot stays unchanged; its digest does not establish identity or tamperproof storage. No live approval or structural clearance is claimed.

Initial kernels pass. Notebook 224 was rerun after adding its remapping slope and arranging the gate vertically for the book; 225 was rerun after replacing an illustrative numerical lifecycle display with categorical state transitions. Notebook 221 was rerun to separate crowded timeline labels. Current outputs have no errors/stderr. Independent vector exports rerun every code cell and require exact scientific RESULTS. All book and embedded figures are inspected during delivery.

Primary sources inspected: Bifet/Gavaldà's expanded author preprint dated 17 October 2006 (17 pages, distinguished from the six-page SDM 2007 proceedings paper); Perdomo/Zrnic/Mendler-Dünner/Hardt's eleven-page ICML 2020 paper; and Lakkaraju/Kleinberg/Leskovec/Ludwig/Mullainathan's KDD 2017 primary author manuscript at PMC5958915. The Stanford selective-label PDF fetch failed; the primary PMC full text was successfully inspected instead. Chapter 43 and the whole-book editorial/technical audit remain required.
