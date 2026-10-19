# Chapter 14: Validation under real-world conditions — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_14_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 14.1 · Random, grouped and nested validation

- [Same rows, different generalization questions](notebooks/067_Chapter_14_01_Nested_Building_Validation.ipynb#units)
- [Evaluate the selection procedure outside the search](notebooks/067_Chapter_14_01_Nested_Building_Validation.ipynb#nested)

Declared mechanisms: exchangeability and repeated member measurements, row versus building split, nested grouped model selection, locked new-building assessment.

```bash
python scripts/run_notebook.py notebooks/067_Chapter_14_01_Nested_Building_Validation.ipynb
```

## 14.2 · Temporal backtesting and delayed labels

- [A past cutoff need not have a resolved target](notebooks/068_Chapter_14_02_Backtesting_Label_Arrival.ipynb#arrival)
- [Shared raw measurements do not make every operational replay invalid](notebooks/068_Chapter_14_02_Backtesting_Label_Arrival.ipynb#overlap)

Declared mechanisms: expanding and rolling origins, one-day and seven-day horizons, label-arrival admission, overlap versus availability and independence.

```bash
python scripts/run_notebook.py notebooks/068_Chapter_14_02_Backtesting_Label_Arrival.ipynb
```

## 14.3 · Spatial and graph-aware evaluation

- [A held region changes the distance to observed examples](notebooks/069_Chapter_14_03_Spatial_And_Graph_Protocols.ipynb#spatial)
- [Known graph nodes and new graphs expose different information](notebooks/069_Chapter_14_03_Spatial_And_Graph_Protocols.ipynb#graph)

Declared mechanisms: random interpolation versus held spatial region, unseen nodes in known graphs, unseen graphs with request-time features, label-free neighborhood construction.

```bash
python scripts/run_notebook.py notebooks/069_Chapter_14_03_Spatial_And_Graph_Protocols.ipynb
```

## 14.4 · Limited labels, imbalance and rare events

- [Positive rows can belong to very few independent buildings](notebooks/070_Chapter_14_04_Rare_Events_Within_Buildings.ipynb#rare)
- [Resample whole buildings and retain undefined outcomes](notebooks/070_Chapter_14_04_Rare_Events_Within_Buildings.ipynb#bootstrap)

Declared mechanisms: grouped stratification limits, training-only weights and oversampling, undefined rare-event metrics, whole-building bootstrap with missing-positive draws.

```bash
python scripts/run_notebook.py notebooks/070_Chapter_14_04_Rare_Events_Within_Buildings.ipynb
```

## 14.5 · Shift, stress tests and external evidence

- [Select on the source, then freeze the procedure](notebooks/071_Chapter_14_05_Performance_Envelope_Under_Shift.ipynb#source)
- [Perturb the observation, preserve the physical target](notebooks/071_Chapter_14_05_Performance_Envelope_Under_Shift.ipynb#stress)

Declared mechanisms: source-only procedure selection, separate site material and support shifts, frozen sensor-bias stress tests, synthetic challenge versus external field evidence.

```bash
python scripts/run_notebook.py notebooks/071_Chapter_14_05_Performance_Envelope_Under_Shift.ipynb
```

## Interpretation and boundaries

Five self-contained generated-data CPU laboratories use seeds 1467–1471 and the existing Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0 environment. Initial kernels passed. Static preflight caught two escaped-newline errors before execution. Notebooks 068–071 subsequently reran for clearer legends, labels, empty-fold ticks and a two-panel stress plot; 068 reran once more to move its window legend off a bar. Numerical result dictionaries remain exactly unchanged. A runner command with an incorrect working-directory path failed before launching a kernel and was corrected. Current timings belong to current executed sources.

The repeated-measurement fixture has 60 buildings, 12 members and two readings per member. Forty-five buildings develop; fifteen remain locked. Fixed standardized KNN5 row CV MSE is 0.244185 versus building CV 0.921466. Five outer grouped folds each use three inner grouped folds to choose among KNN k=1,5,15 and Ridge alpha=.1,10, with locally fitted scalers. Nested outer MSE is 0.734813. The all-development search selects Ridge alpha10; final MSE is 1.006046. Outer models train on 36 buildings, final on 45. Equal-row and equal-building weighting coincide because each building has 24 rows. The split overview is explicitly schematic.

The daily replay evaluates one- and seven-day any-alarm targets at origins 110,150,190,230. Expanding and ninety-day rolling histories use only labels arrived by the refit origin. Each frozen model predicts twenty subsequent daily cutoffs, admitting covariates at their respective times. Fixed logistic C1, eventual retrospective outcomes, Brier/log loss, prevalence baselines and denominators are retained. The invalid earlier-cutoff-only comparator admits [4,3,5,5] unresolved one-day labels and [12,10,12,12] unresolved seven-day labels. Its score can improve or worsen without repairing invalidity. Adjacent cutoffs 80/81 share five context and six target days. Strict cutoffs 80/98 have disjoint complete raw intervals and latest training label arrival97. That stricter separation does not prove independence. Operational replay can legitimately reuse observed past context; overlapping horizons do not supply independent event trials.

A 25×25 synthetic field compares fixed KNN5 with 500 random training locations versus the 500 locations outside a held right-hand fifth. Both assess 125 locations; MSE is 0.010399 and 0.100484. Different held tasks preclude a causal interpretation of this difference. Thirty independent twelve-node paths compare fixed own-feature OLS to OLS with a label-free neighbor mean. Known-graph assessment holds 72 node labels in 24 graphs, with full topology/covariates admitted before fitting; training uses216 nodes. New-graph assessment trains on288 nodes in those24 graphs, then assesses72 nodes in six new graphs whose complete inputs are supplied per request. Equal-graph MSE is approximately 0.532/0.139 for known-graph held nodes and 0.508/0.177 for new graphs. Exact per-graph values remain in the result dictionaries. No held label enters features; no neural graph model or label propagation is run.

Rare-event data have 50 buildings with twelve rows each. Buildings [0,1,2,36,43,47] each contain four positives. Training has432 rows, twelve positives in three buildings; unused development has72 rows/four positives; final has96 rows/eight positives in two buildings. These prevalences are constructed. Five grouped validation folds have [4,0,0,4,4] positive rows; empty folds remain and undefined recall/precision are None. Fixed C1 logistic procedures use unweighted, balanced or training-only oversampled fitting. Scalers fit original training rows before duplication; assessment groups remain disjoint. Threshold .5 is fixed, with no development selection. Final unweighted accuracy is .9167, recall0/8, precisionundefined, Brier .066652. Balanced and oversampled procedures each detect6/8 positives with twelve false alarms, accuracy .8542 and precision1/3, while Brier worsens to .114270/.116313. A majority baseline also misses all positives. One thousand whole-building bootstrap draws include78 with no positive and undefined recall. Conditional percentiles [.5,1] among922 defined draws describe sensitivity to two observed positive buildings, not reliable population interval coverage.

Shift experiments fit 500 source steel-A members and select among fixed Ridge, histogram boosting and a mean baseline on150 separate source development members. Selection chooses Ridge before challenge generation; no development refit or final retuning occurs. Five locked cohorts of200 independent synthetic members isolate steel-A, steel-B, concrete-A, concrete-B and high-load steel-A. SiteB adds an unmodeled .8-unit offset; concrete adds .5(load/50)^2. Material is constant in training. Selected MSEs are approximately .0229,.6911,.1449,1.2285,.0221. Preserving the linear rule lets Ridge extrapolate well at high load; out-of-support status alone does not force poor numerical performance. Adding0/1/5 kN recorded-load bias while fixing truth gives Ridge MSE .022902/.025232/.067317. All frozen procedures remain reported. The detailed stress panel uses a finer vertical scale to reveal learned-model differences. Finite stresses are not worst-case bounds. No independently collected external field evidence is available or implied.

Ten original vector figure sets implement both agreed briefs and the actual numerical comparisons. Two equations define building weighting and arrival admission; seven exercises ask for defensible protocols. Official scikit-learn nested/temporal/grouped/weight documentation and Roberts et al.2017 primary author-hosted full text were inspected19 October2026. The Ecography record is40(8):913–929, DOI10.1111/ecog.02881. Live sklearn documentation1.9.1 versus executed1.9.0 is disclosed. No universal estimator ranking, external field validity or dependable few-positive confidence guarantee is asserted.
