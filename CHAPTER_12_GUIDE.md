# Chapter 12: Engineering and selecting features — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_12_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 12.1 · Domain features and interactions

- [Encode a declared bending hypothesis](notebooks/057_Chapter_12_01_Physical_Features_And_Sample_Efficiency.ipynb#hypothesis)
- [A useful feature is a falsifiable assumption](notebooks/057_Chapter_12_01_Physical_Features_And_Sample_Efficiency.ipynb#limits)

Declared mechanisms: beam-inspired feature and domain assumptions, dimensionless group and unit invariance, interaction basis versus raw main effects, predeclared learning-size comparisons.

```bash
python scripts/run_notebook.py notebooks/057_Chapter_12_01_Physical_Features_And_Sample_Efficiency.ipynb
```

## 12.2 · Aggregates and history summaries

- [Build features only from completed, arrived history](notebooks/058_Chapter_12_02_Cutoff_Safe_History_And_Relations.ipynb#clock)
- [Show unavailable proxies alongside lawful summaries](notebooks/058_Chapter_12_02_Cutoff_Safe_History_And_Relations.ipynb#availability)

Declared mechanisms: event and arrival clocks in trailing windows, RMS and spectral energy summaries, prior inspection counts and recency, relational aggregates and future-append invariance.

```bash
python scripts/run_notebook.py notebooks/058_Chapter_12_02_Cutoff_Safe_History_And_Relations.ipynb
```

## 12.3 · Feature selection and stability

- [Correlated channels can share predictive information](notebooks/059_Chapter_12_03_Correlated_Channels_And_Selection.ipynb#design)
- [Report variation across resamples](notebooks/059_Chapter_12_03_Correlated_Channels_And_Selection.ipynb#resampling)
- [Nest selection inside each fit boundary](notebooks/059_Chapter_12_03_Correlated_Channels_And_Selection.ipynb#diagram)

Declared mechanisms: filter wrapper and embedded selectors, selection inside validation pipelines, correlated proxies and resample variation, frequency diagnostics without error-control claims.

```bash
python scripts/run_notebook.py notebooks/059_Chapter_12_03_Correlated_Channels_And_Selection.ipynb
```

## 12.4 · Compact representations and learned features

- [Compare representations of the same signal windows](notebooks/060_Chapter_12_04_Spectra_PCA_And_Autoencoder.ipynb#signals)
- [Train an explicit nonlinear bottleneck](notebooks/060_Chapter_12_04_Spectra_PCA_And_Autoencoder.ipynb#encoder)
- [Assess the downstream objective independently of reconstruction](notebooks/060_Chapter_12_04_Spectra_PCA_And_Autoencoder.ipynb#downstream)

Declared mechanisms: hand-built spectral and low-rank features, self-contained nonlinear autoencoder, training-only representation fitting, reconstruction versus downstream performance.

```bash
python scripts/run_notebook.py notebooks/060_Chapter_12_04_Spectra_PCA_And_Autoencoder.ipynb
```

## 12.5 · Leakage, cost and feature availability

- [Compare operational feature packages, not isolated scores](notebooks/061_Chapter_12_05_Operational_Feature_Packages.ipynb#packages)
- [Reject unavailable columns and schema reorderings](notebooks/061_Chapter_12_05_Operational_Feature_Packages.ipynb#audit)

Declared mechanisms: feature acquisition cost and latency, future target proxies and apparent error, development-only package choice, train-serving column contract.

```bash
python scripts/run_notebook.py notebooks/061_Chapter_12_05_Operational_Feature_Packages.ipynb
```

## Interpretation and boundaries

All five self-contained generated-data laboratories execute in fresh kernels with no failed reference runs. Construction audits and fitted prediction roles are explicitly distinguished. All numerical inputs are generated internally, without downloads, credentials or GPU; no dependency was added. The custom autoencoder's gradient is checked numerically and its fixed optimization budget is disclosed rather than claimed converged or globally optimal.

The physical-feature comparison uses 600 independent idealized central-load beam records with positive load/span/rigidity, an explicitly favorable affine beam mechanism, 300/100/200 roles and nested training sizes 40/80/160/300. Units and a dimensionless identity pass numerical checks. Raw main effects, quadratic expansion and the beam feature have 300-member final MSE 44.890505566/7.484463859/.009738991 mm². The physical slope is 1.079878951 against declared 1.08, and its 40-member MSE is .010481687. Different hypothesis classes and correct domain information are intentional. The outcomes do not validate field mechanics, uncertain stiffness or other supports/loading/material regimes; no final curve selects a representation.

The history construction fixes six members, ten daily 64-sample windows at 64 Hz, cutoff 7.5 and trailing interval (4.5,7.5]. Both end and arrival clocks apply. Member-0 day-6 payload arrives day 9 and is excluded, leaving two windows rather than three. Only day-1 inspections arrive before cutoff; each member has one known prior inspection and recency 6.5 days. One-sided Fourier weighting passes Parseval against time-domain mean square. RMS has acceleration units, while band contributions/mean square are squared acceleration, not physical mechanical energy. Ring-neighbor means use only individually eligible histories; appending huge future windows leaves all historical features exactly unchanged. These are construction audits, not predictive scores or causal graph claims.

The selection comparison generates 440 independent members with two proxies of u (training correlation .995017927), one v channel and five noise channels; 240/80/120 roles. Scaling/selection are refitted inside each of four training CV folds. Fixed two-column filter and RFE both retain the redundant u pair and omit v, with final MSE 1.048943984 mm². Lasso alpha .08 retains all three useful channels and gives .282530643. Forty training half-samples produce filter/RFE/Lasso mean Jaccard 1/.966666667/.819102564. The filter is perfectly stable yet predictively inadequate; the important u proxies do not exchange places in this run. Lasso's variation includes occasional noise columns. A predeclared .7-frequency threshold retains u_A/u_B/v_C; refitted ridge gives .250449342 final MSE. Frequencies are descriptive diagnostics, not posterior inclusion, causal relevance or the original stability-selection paper's false-discovery guarantees. An attempted author-hosted PDF was unavailable, so the primary arXiv record and publisher article were inspected for the framework; no unverified theorem conditions are asserted.

The representation experiment uses 550 independent 64-sample acceleration windows, random phases/amplitudes and 300/100/150 roles. Its target deliberately depends on squared amplitudes, privileging known two-bin spectral features with phase invariance. Raw-64/PCA-8/autoencoder-8/spectral-2 plus the same fixed linear ridge readout have final response-index MSE 2.086286224/1.895526944/1.965539342/.009810793. PCA/autoencoder final standardized reconstruction MSE is .002370630/.040967383. The eight-unit tanh/linear-output autoencoder uses full-batch gradients, rate .1, 2,000 fixed updates and weight penalty 1e-4; objective falls 1.069936954 to .037966299 and the central-difference encoder-gradient check passes. Reconstruction and downstream objectives differ. No best-encoder ranking, convergence certificate, end-to-end supervised training, foundation embedding or transfer to other acquisition conditions is claimed.

The feature-package experiment uses 700 independent members and 400/150/150 roles with a declared static latent condition. Acquisition costs/delays are teaching fixtures: base 0/0, vibration 5/.1 day, preplanned prior inspection 20/0 at decision time, combination 25/.1, new precise inspection 50/2, outcome proxy 0/7.1. Only the four available packages meet budget 25 and deadline .5. Lowest development error chooses the combination; final MSE is .495234390 mm² versus vibration .574102248, prior .861263602 and base 1.759124835. The new inspection/proxy apparent errors .088835502/.000103986 are invalid for the original decision. Their scores are retained as leakage findings, not deployable performance. The prior inspection requires advance scheduling; a later decision needs a different task and is not evaluated here. Reordered selected-request columns are explicitly rejected. Prediction MSE is not operational utility or a field cost-effectiveness estimate.

Seven original vector figure sets implement both planned visual briefs: cutoff-safe trailing and relational summaries, plus nested selection and resample frequencies. Four equations specify the physical combination, RMS, selection frequency and autoencoder. Primary/official references support the mechanics convention, spectral units, selector/PCA interfaces and formal-versus-diagnostic stability distinction. The underlying generated experiments and fixed-budget autoencoder are specified independently. All controls and limitations remain in the companion guide and execution evidence.

Visual review prompted fresh-kernel reruns of code_060 and code_061 after separating neighboring tick labels and shortening a clipped axis label. Both pass with unchanged result dictionaries; current timings are recorded. The first PDF integrity pass also caught an overlong mechanics URL; its local reference typography was repaired. Closing practice was kept together after page review.
