# Chapter 40: Fairness, privacy, and security — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_40_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 40.1 · Group performance and fairness objectives


Declared mechanisms: actual subgroup TPR FPR precision calibration and allocation assessment, Wilson frequency intervals and minority-group denominators, independent development group-threshold comparison, unequal outcome coverage contrasted with privileged simulator full audit.

```bash
python scripts/run_notebook.py notebooks/211_Chapter_40_01_group_performance_uncertainty_and_allocation.ipynb
```

## 40.2 · Sensitive data and minimization


Declared mechanisms: actual household-level pseudonymous grouping with explicit non-anonymity limits, purpose and role based field export and retention fixtures, auxiliary location-linkage diagnostic before and after coarsening, preserved household temporal split rather than random-row mixing.

```bash
python scripts/run_notebook.py notebooks/212_Chapter_40_02_sensitive_fields_pseudonyms_and_data_minimization.ipynb
```

## 40.3 · Privacy-preserving learning and release


Declared mechanisms: bounded household-mean Laplace utility simulation with replacement sensitivity and composition, actual federated local-gradient model averaging and centralized comparator, single-client update disclosure and arithmetic mask cancellation illustration, synthetic copying and rare-record nearest-neighbour disclosure fixtures.

```bash
python scripts/run_notebook.py notebooks/213_Chapter_40_03_privacy_noise_federated_updates_and_disclosure_audit.ipynb
```

## 40.4 · Model and data security


Declared mechanisms: generated poisoning and trigger backdoor fits assessed independently, bounded measurement evasion and own-model query extraction fixture, strict numeric inference interface treats external-note instructions only as data, artifact digest change detection and query-volume control with explicit limits.

```bash
python scripts/run_notebook.py notebooks/214_Chapter_40_04_security_threat_access_and_structured_data_boundaries.ipynb
```

## 40.5 · Governance, misuse and evidence records


Declared mechanisms: actual fitted model metrics bound to an executable evidence/use record, simulated role intended-use and lifecycle state gates, canonical hash-chain audit log with change detection and authenticity limits, incident suspension and retirement preserve evidence without autonomous structural clearance.

```bash
python scripts/run_notebook.py notebooks/215_Chapter_40_05_use_records_audit_trails_and_incident_states.ipynb
```

## Interpretation and boundaries

# Chapter 40 mechanisms, controls and interpretation

Five original laboratories preserve all five scopes and both visual briefs. They execute22 code cells and embed12 figures. Every import, helper and input is internal. Ordinary execution is offline and CPU-only, without credentials or new files/dependencies/assets. All household identities, contacts, locations, role assignments and inspection candidates are fictional generated controls. Runtime remains CPython3.14.3, NumPy2.4.4, SciPy1.17.1, pandas3.0.3, Matplotlib3.11.0, scikit-learn1.9.0 and threadpoolctl3.7.0. Access/execution date22 October2026, Australia/Melbourne; literature cutoff18 October2026. No jurisdiction-specific legal conclusion is asserted.

- **211 / group assessment:** Generated source2,400 candidates, outcome observation depends on group and outcome,1,460 observed source labels. Logistic model omits group but that is not a fairness guarantee. Independent600-case development audit is completely labelled, assumed separately acquired; group thresholds are development-positive20th percentiles0.218083/0.183565, not a complete equalized-odds optimizer. No shared inspection capacity is imposed. Complete final simulator audit1,200 has groups1,052/148 and positives319/84. Common0.5 TPR0.388715/0.404762, FPR0.088677/0.0625, precision0.656085/0.894737, allocation0.179658/0.256757. Development group thresholds yield final TPR0.777429/0.821429, FPR0.306958/0.453125, precision0.524313/0.704082, allocation0.449620/0.662162. Wilson intervals retain true denominators and conditional frequency interpretation. Observed final label coverage0.697719/0.243243; observed group1 has only36 labelled candidates/19 positives, TPR0.315789 with interval[0.153642,0.539900], FPR0/precision1. Those apparently favourable rates do not characterize unobserved outcomes. Full truth is a privileged simulator audit. Four predeclared probability bins per group retain counts/empty bins and Wilson intervals, not simultaneous/refitting uncertainty. Visual A separates support, TPR uncertainty and workload.
- **212 / minimization:**100 fictional households×eight weekly records. HMAC tokens preserve household trajectories; public teaching key is explicitly not a production secret, and pseudonyms are not anonymity. Actual analyst export keeps token/week/temperature/response, removes identity/contact/exact coordinates/equipment serial; unsupported role rejected by an in-memory policy fixture, not production IAM. Raw retention week>=4 removes400/retains400 rows; model/log/backup retention is separate. Exact coordinate auxiliary join uniquely links100 households. Four-by-four coarsening gives zero unique households in this run, candidate-set minimum3/median6, without general linkage or anonymity guarantee. Household holdout tokens overlap0, random-row partitions overlap97 households. Minimize unnecessary disclosure while retaining restricted valid grouping.
- **213 / privacy mechanisms:**100 fictional households×eight bounded readings, mean of household means. Fixed-public-n replacement adjacency protects one whole trajectory; sensitivity0.01 versus row sensitivity0.00125. Worst-case neighbouring all-zero/one-all-one household verifies the bound.2,000 seeded Laplace utility draws for epsilon0.1/0.5/1/4 give MAE0.100269/0.019877/0.009858/0.002513, matching scale0.1/0.02/0.01/0.0025. One private release at each parameter would compose to epsilon5.6. Public seeded simulation on public generated data is explicitly NOT a protected release; real secret entropy/accounting/numerics require separate implementation. No DP training claim. Actual decentralized linear model averaging: ten sites×100 records, nonidentical input means,40 rounds×five local gradient steps, learning rate0.05; centralized200-gradient-step comparator. Independent500-case final RMSE0.321457 federated/0.321418 centralized. First zero-initialized intercept update reveals exact local mean target0.281382. Opposite pairwise float masks cancel arithmetically; no cryptographic secure-aggregation protocol, real key management, dropout or collusion protection is claimed. Source-resampling synthetic candidate copies100/100 rows and deliberately exposes canary[10,10,10], distance0; independent generator copies0, canary distance15.033015. Lack of exact copies is not membership or linkage privacy proof.
- **214 / access-specific threats:** Only own-model/generated-data sandbox exercises; no network/external target. Actual logistic fit1,200 source/500 final,80 high-logit label flips and separate120 appended negative records with trigger1/target1. Ordinary final error clean0.212/label-poison0.242/backdoor0.212. Triggered true-negative positive rates clean0.210526/backdoor0.995951. Rejecting the whole untrusted appended batch recovers clean decisions, but does not detect trusted-source poisoning. Bounded measured-feature evasion L-infinity0.25 flips0.190955 of199 originally detected true positives. Fifty own-model probability queries/log-odds least squares recover the known linear family with agreement1.0; query-volume limit50 is enforced but does not establish extraction resistance. Twenty misleading external-note strings leave the separate strict numeric interface exactly unchanged; unexpected control field rejected. No LLM is invoked and no general prompt-injection defense is claimed. Canonical own-parameter JSON digest detects one-byte alteration relative to a trusted-in-fixture expected digest; not publisher authentication or validation of a real dependency chain. Visual B labels record access, training writes, artifacts and serving interfaces.
- **215 / use and responsibility:** Actual logistic model1,000 source/500 final, Brier0.185435/error0.284. Fifteen-field record binds actual metrics/model digest, provenance, purpose, excluded clearance use, limitations and fictional decision-owner/incident roles. Missing owner fails; completeness does not establish adequacy. Fictional state/role sequence draft→verified→review_ready→suspended→retired; no actual human approval or production release. Only review-prioritization requests are allowed in review_ready; wrong role, excluded structural-clearance use, suspended review and retired reopening are rejected. Unit-metadata incident and dispositions persist in nine-event canonical SHA256 chain. Modified historical payload fails verification, while unkeyed-chain rewrite with a replaced trusted head remains possible. No automatic structural-safe judgment or legal compliance certificate.

All initial fresh kernels pass with assertions and no notebook errors/stderr. Numerical RESULTS rerun in isolated vector-export processes agree exactly. Plot-only book label wrapping repairs retain scientific results.12 original SVG/vector-PDF/PNG sets and actual inline versions are reviewed during delivery. Full primary PDFs inspected for Hardt/Price/Srebro2016 fairness, Dwork/Roth2014 DP definition/Laplace/composition, McMahan et al.2017 federated averaging, NIST AI100-2e2025 taxonomy/prompt-injection interfaces and Mitchell et al.2019 model cards. The original generated mechanisms are not benchmark reproductions, actual privacy releases, real IAM/cryptographic protocols, live dependency audits, LLM injection tests or real human approvals. Chapters41–43 and the whole-book audit remain required.
