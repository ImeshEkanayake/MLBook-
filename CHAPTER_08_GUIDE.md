# Chapter 8: concept-to-code guide

Permanent IDs code_037–code_041 correspond to sections 8.1–8.5. All generators, imports and helpers are internal; restart and run all cells. Ordinary execution needs no files, downloads, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [execution evidence](CHAPTER_08_EXECUTION.md).

These are construction laboratories with explicit task/data controls rather than model-constructor tutorials. The sampling example fits only two predeclared probability constants; it has no tuning candidates. No trained graph model, survival estimator, weak-label aggregator or PDE solver is claimed.

## 8.1 · Units of observation and target design

- [contract](notebooks/037_Chapter_08_01_Units_And_Targets.ipynb#contract): Example key, horizon endpoint convention, follow-up and explicit unknown labels.
- [clocks](notebooks/037_Chapter_08_01_Units_And_Targets.ipynb#clocks): Event/report timeline and overlapping targets.
- [maturity](notebooks/037_Chapter_08_01_Units_And_Targets.ipynb#maturity): Extraction sensitivity, censored versus pending states and unsupported zero filling.
- [exercises](notebooks/037_Chapter_08_01_Units_And_Targets.ipynb#exercises): First-event eligibility, changed horizons and grouped/time-aware assessment.

```bash
python scripts/run_notebook.py notebooks/037_Chapter_08_01_Units_And_Targets.ipynb
```

## 8.2 · Joins, keys and relational structure

- [relations](notebooks/038_Chapter_08_02_Joins_Keys_And_Relations.ipynb#relations): Primary, foreign and composite keys; complete source relations.
- [amplification](notebooks/038_Chapter_08_02_Joins_Keys_And_Relations.ipynb#amplification): A rejected cardinality assumption and 96 unsafe combinations.
- [repair](notebooks/038_Chapter_08_02_Joins_Keys_And_Relations.ipynb#repair): Separate aggregation and one-member views retaining missing sensors.
- [exercises](notebooks/038_Chapter_08_02_Joins_Keys_And_Relations.ipynb#exercises): Unequal sampling rates, null keys and graph relations lost by flattening.

```bash
python scripts/run_notebook.py notebooks/038_Chapter_08_02_Joins_Keys_And_Relations.ipynb
```

## 8.3 · Time-aware information availability

- [versions](notebooks/039_Chapter_08_03_Time_Aware_Availability.ipynb#versions): Available version resolution before backward as-of event matching.
- [timeline](notebooks/039_Chapter_08_03_Time_Aware_Availability.ipynb#timeline): Parallel event, arrival, cutoff and target/report clocks.
- [invariance](notebooks/039_Chapter_08_03_Time_Aware_Availability.ipynb#invariance): Current-revision violation and a future append that cannot change past features.
- [exercises](notebooks/039_Chapter_08_03_Time_Aware_Availability.ipynb#exercises): Late records, tolerance, revision ties and historical label resolution.

```bash
python scripts/run_notebook.py notebooks/039_Chapter_08_03_Time_Aware_Availability.ipynb
```

## 8.4 · Sampling, labels and dataset documentation

- [frame](notebooks/040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb#frame): Known inspection selection and two fixed constant probability estimators.
- [labels](notebooks/040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb#labels): Reference, weak proxy, abstention and two imperfect annotators.
- [final](notebooks/040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb#final): Independent final population, actual Brier errors and validated teaching dataset card.
- [exercises](notebooks/040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb#exercises): Zero support, within-stratum selection, shared annotation bias and real documentation.

```bash
python scripts/run_notebook.py notebooks/040_Chapter_08_04_Sampling_Labels_And_Documentation.ipynb
```

## 8.5 · Representations and storage contracts

- [views](notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb#views): Source readings to ordered wide/sequence values with missingness masks.
- [graph](notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb#graph): Stable ID mapping and a substantive graph permutation invariant.
- [storage](notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb#storage): Numeric archive round trip, explicit schema and unit conversion.
- [mesh](notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb#mesh): Connectivity-dependent interpolation, topology and boundary metadata.
- [exercises](notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb#exercises): Identity misalignment, schema migration and task-specific storage choice.

```bash
python scripts/run_notebook.py notebooks/041_Chapter_08_05_Representations_And_Storage.ipynb
```

## Controls and interpretation

| Laboratory | Declared controls | Prediction before changing them |
| --- | --- | --- |
| Units/targets | 14-day horizon; 7-day cadence; reporting lag 3–10 days; extract 45/60/80 | Which targets overlap, and which unknowns can waiting resolve? |
| Relations | Reading/member/inspection key scopes; inner versus left joins; separate aggregation | Which distinct units disappear or receive extra weight? |
| Availability | Available-version resolution; backward event match; tolerance 5 days | Can a future upload alter an earlier snapshot? |
| Sampling/labels | Source old/new shares .2/.8; inspected counts 240/160; known probabilities .6/.1 | Which population and label source does a reported fraction describe? |
| Storage | Stable IDs; axis order; m/mm units; boolean observation mask; schema 1.0 | Which invariant fails after an inconsistent reorder or unit change? |

A negative needs outcome evidence; an absent record or abstention is not zero. Known-design weights require positive sampling support and do not repair arbitrary selection. Label agreement is not correctness. Graph/mesh/sequence representations retain different relationships, and round-trip byte/value checks do not establish measurement validity. Preserve the source log, lineage and a fresh assessment population when redesigning fitted procedures.
