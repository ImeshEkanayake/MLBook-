# Chapter 7: concept-to-code guide

Permanent IDs code_032–code_036 map one-to-one to sections 7.1–7.5. Read the prediction prompt, run all cells from a fresh kernel, then interpret before changing controls. All imports, helpers and generated data are internal. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_07_EXECUTION.md). No ordinary-run files, downloads, credentials or GPU are required.

## 7.1 · Baselines and experimental questions

- [claim](notebooks/032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb#claim): Falsifiable population/metric/comparator question; constant, heuristic, beam and learned references; units.
- [development](notebooks/032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb#development): Same three candidates, training-only scaling and development-only selection for both learned rules.
- [final](notebooks/032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb#final): All predeclared rules, paired per-case losses, actual gain and the limited practical threshold.
- [exercises](notebooks/032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb#exercises): Wrong physical boundary, absent constructed correction, fair nonlinear alternative and subgroup consequences.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/032_Chapter_07_01_Baselines_And_Experimental_Questions.ipynb
```

## 7.2 · Leakage and information boundaries

- [join](notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb#join): Both timestamp cutoffs, chronological group periods, cardinality rejection and rebuilt one-to-one features.
- [audit](notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb#audit): Group overlap, target-derived aggregate sensitivity and preprocessing boundaries.
- [development](notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb#development): Repaired versus unavailable future information; invalid method remains a counterexample.
- [final](notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb#final): Only the repaired rule on six new buildings, with no final redesign.
- [exercises](notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb#exercises): Late arrivals, relational multiplicity, cross-fit encodings and alternate known-building contracts.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/033_Chapter_07_02_Leakage_And_Information_Boundaries.ipynb
```

## 7.3 · Reproducibility and provenance

- [snapshot](notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb#snapshot): Canonical schema/payload, full recoverable bytes, hash and deliberate mutation rejection.
- [program](notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb#program): Actually executed critical-function hash, configuration, dependency/CPU state and exact replay.
- [variation](notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb#variation): Predeclared seed variability and a new independently generated sensor dataset.
- [final](notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb#final): Rolling one-step forecast, persistence baseline and actual final/replication results.
- [exercises](notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb#exercises): Source revision, true fixed-origin forecast, field replication and numerical tolerance contracts.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/034_Chapter_07_03_Reproducibility_And_Provenance.ipynb
```

## 7.4 · Fair comparisons and ablation

- [contract](notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb#contract): Actual graph task, split, same feature/topology access and matched budgets.
- [matched](notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb#matched): Separate graph/table forward-backward paths, corresponding states and candidate checkpoint evidence.
- [attempts](notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb#attempts): Rejected oversized-rate attempt explicitly outside the eligible comparison.
- [final](notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb#final): All seeds, equal-graph errors, graph/table numerical agreement and information ablations.
- [exercises](notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb#exercises): Two-hop access, total search/time budgets, graph weighting and unavailable future topology.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/035_Chapter_07_04_Fair_Comparisons_And_Ablation.ipynb
```

## 7.5 · Prediction, explanation and causal claims

- [mechanisms](notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb#mechanisms): Exact observationally identical tables with different author-known intervention effects.
- [prediction](notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb#prediction): Actual available-input logistic fit and associational coefficient/probability explanation.
- [final](notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb#final): Protected predictive log-loss assessment, with no causal interpretation of its advantage.
- [intervention](notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb#intervention): Separate randomized simulator sample and known identical potential outcomes.
- [exercises](notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb#exercises): Assumed graphs, observed confounders, prediction timing, intervention versions and explanation limits.

Run from the repository root:

```bash
python scripts/run_notebook.py notebooks/036_Chapter_07_05_Prediction_Explanation_And_Causal_Claims.ipynb
```

## What the evidence supports

The beam correction is deliberately matched to its synthetic residual representation. The leakage lab repairs full feature paths and time/group boundaries, not merely a final column list. The provenance lab preserves actual bytes and a narrow critical-code hash while identifying the full notebook revision separately. The graph/table methods are actual equivalent one-hop computations with the same information and update/search budgets; information ablations do not prove general architecture superiority. Two observationally equal causal mechanisms expose an identification limit, not merely sample uncertainty.

Preserve fresh final cases for redesign. A good score, a model explanation, exact computational replay and an intervention effect require different claims. All examples are scoped concept laboratories with fixed disclosed controls, not exhaustive estimator-constructor studies, observed engineering validation or causal maintenance advice.
