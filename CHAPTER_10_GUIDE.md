# Chapter 10: Cleaning imperfect data — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_10_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 10.1 · Missingness and observation processes

- [One NaN can hide different evidence](notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb#states)
- [Diagram generator inputs, not an inferred causal graph](notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb#mechanisms)
- [Fit the repair inside training, then select only on development](notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb#fit)
- [Assess frozen repairs on independent final members](notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb#final)
- [Exercises and hints](notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb#exercises)

Declared mechanisms: absent censored structural and failed measurements, MCAR MAR and MNAR as generator assumptions, training-only imputation and missingness indicators, development-only policy selection, protected final comparison without identifying missingness from data.

```bash
python scripts/run_notebook.py notebooks/047_Chapter_10_01_Missingness_And_Observation_Processes.ipynb
```

## 10.2 · Duplicates, identities and inconsistent records

- [An identical value is not an event identity](notebooks/048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb#identity)
- [Reject conflicting payloads before picking a survivor](notebooks/048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb#conflicts)
- [Prevent copies of one event from crossing roles](notebooks/048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb#leakage)
- [Exercises and hints](notebooks/048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb#exercises)

Declared mechanisms: reimported records versus legitimate repeat events, composite entity identity, version conflicts and known-at-cutoff resolution, provenance retention during deduplication, duplicate event leakage across role assignments.

```bash
python scripts/run_notebook.py notebooks/048_Chapter_10_02_Duplicates_Identities_And_Updates.ipynb
```

## 10.3 · Measurement units, timestamps and validity

- [Convert quantities, not just column names](notebooks/049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb#units)
- [The same local clock reading can denote two instants](notebooks/049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb#clocks)
- [Calibration uses independent reference evidence](notebooks/049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb#calibration)
- [Exercises and hints](notebooks/049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb#exercises)

Declared mechanisms: quantity-aware unit conversion, offset-aware timestamp ordering and repeated local clocks, event-arrival validity checks, independent reference calibration, schema checks precede statistical scaling.

```bash
python scripts/run_notebook.py notebooks/049_Chapter_10_03_Units_Timestamps_And_Validity.ipynb
```

## 10.4 · Noisy and uncertain labels

- [The target definition and the label measurement are separate](notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb#measurement)
- [Spend new reference evidence only on training disputes](notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb#adjudication)
- [Fit disclosed objectives without a hidden candidate search](notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb#objectives)
- [Compare against the same independent reference target](notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb#final)
- [Exercises and hints](notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb#exercises)

Declared mechanisms: continuous severity and threshold ambiguity, annotator disagreement and exclusion, explicit measurement-model soft targets, training-only adjudication and extra evidence budget, fixed logistic objectives and independent reference assessment.

```bash
python scripts/run_notebook.py notebooks/050_Chapter_10_04_Noisy_And_Uncertain_Labels.ipynb
```

## 10.5 · Outliers, corruption and rare events

- [Investigate a spike before calling it an outlier](notebooks/051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb#trail)
- [Bound one residual's influence without declaring all extremes invalid](notebooks/051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb#fit)
- [Assess the fixed procedures on ordinary and rare cases separately](notebooks/051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb#final)
- [Exercises and hints](notebooks/051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb#exercises)

Declared mechanisms: provenance-led investigation of extreme strain, known loading event versus isolated source-unit fault, blind outlier deletion erases valid rare cases, fixed-threshold Huber response robustness, verified repair and independent final assessment.

```bash
python scripts/run_notebook.py notebooks/051_Chapter_10_05_Outliers_Corruption_And_Rare_Events.ipynb
```

## Interpretation and boundaries

All five laboratories pass fresh-kernel execution. The missingness experiment retains absent, structural, failed and censored states separately. Its three stipulated MCAR/MAR/MNAR generators use 600 independent members and train/development/final roles 300/150/150. Training medians exclude assessment inputs. Development selects the indicator in all three mechanisms, but it slightly loses on final MAR and MNAR cases (.048239224 versus .047677427 and .051192369 versus .050690067 mm²). The MCAR final errors are .037406610/.037558362. These outcomes do not identify missingness or establish valid inference under MNAR.

The identity audit preserves seven import rows, five event versions, four events and three composite-key members. It retains three e1 import IDs in lineage, keeps legitimate same-grade inspections and rejects a fabricated conflicting payload. Event e4 has grade one at cutoff 10 and grade three at cutoff 15. An invalid row split overlaps e1/e4; event separation repairs only that boundary, not building/time independence.

Quantity-aware conversion retains signed displacements [1.2,1.4,1.5,-.8] mm and flags a separate invalid negative length. Offset-aware repeated local clocks differ by 3,600 seconds in UTC and have verified timezone folds 0/1. An arrival-before-event record is flagged rather than guessed. Ten reference standards fit offset .199682692 mm and gain 1.050049495; five independent checks give raw/calibrated MAE .277852384/.003511267 mm. This is a simulated calibration check, not accreditation or operational target fitting.

The uncertain-label experiment uses a declared uniform severity prior and independent Gaussian annotation errors; the annotation-only posterior does not condition on all predictive information. Training annotators disagree on 54/400 cases; agreement-only training retains 346. Twenty new training-only adjudications change eleven labels and incur extra evidence. All four logistic policies are frozen, with disclosed normalization, slope penalty and gradient budget. On 150 final reference cases, hard/consensus/soft/adjudicated log losses are .394242010/.387891956/.391291221/.391860090 versus frequency .692359484. Soft targets have the lowest Brier error of the four, while consensus has the lowest log loss; no universal label-policy ranking follows.

The strain audit distinguishes a verified day-80 source-unit fault from a valid shared day-120 response to 65 kN loading. It preserves raw lineage and checks times, neighbors, units/calibration and load evidence; no single contextual clue proves physical validity. A separate fixed-delta (.15 mm) Huber IRLS response-corruption experiment converges in six iterations and passes a stationarity check. Raw OLS/Huber/verified-repair OLS final MAE is 3.381644184/.043884739/.043959975 mm. All five valid high-load training members remain; a blind three-standard-deviation rule flags all five even after unit correction. Residual robustness does not handle arbitrary input leverage or decide whether a rare case is task-relevant.

Eight original vector figure sets support the two agreed visual briefs and the numerical comparisons. The Bayesian label, calibration, missingness and robust-objective assumptions remain explicit. No dependency was added; ordinary execution is offline and CPU-only. There were no failed reference notebook runs or hidden final-set tuning. The original robust-loss article was not available through the retrieved DOI landing page, so the chapter cites the primary SciPy mathematical convention and distinguishes its custom fixed-threshold solver from scikit-learn's fitted-scale implementation.

Visual review prompted fresh-kernel reruns of code_048 and code_049 to give timeline labels opaque backgrounds and separate neighboring subplot titles. Both reruns pass with unchanged result dictionaries; the recorded runtimes refer to the current sources.
