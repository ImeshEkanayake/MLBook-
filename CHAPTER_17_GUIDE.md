# Chapter 17: Similarity, kernels, and margins — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_17_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 17.1 · Distances, metrics and meaningful neighbourhoods

- [Stored numeric units are part of a naive distance](notebooks/082_Chapter_17_01_Units_Missingness_And_Metric_Geometry.ipynb#units)
- [A perfect match on one available field can be weak evidence](notebooks/082_Chapter_17_01_Units_Missingness_And_Metric_Geometry.ipynb#mixed)

Declared mechanisms: raw units versus dimensionless reference scales, unit-consistent Mahalanobis covariance, categorical and missing shared features, distance eligibility and neighborhood geometry.

```bash
python scripts/run_notebook.py notebooks/082_Chapter_17_01_Units_Missingness_And_Metric_Geometry.ipynb
```

## 17.2 · Nearest-neighbour prediction and retrieval

- [Fit neighborhoods on admitted historical cases](notebooks/083_Chapter_17_02_Neighbor_Support_And_Search.ipynb#prediction)
- [Search accuracy is separate from predictive quality](notebooks/083_Chapter_17_02_Neighbor_Support_And_Search.ipynb#search)

Declared mechanisms: development neighborhood and weighting selection, inside versus unusual query support, exact tree versus brute retrieval, candidate-subset approximation and zero-distance behavior.

```bash
python scripts/run_notebook.py notebooks/083_Chapter_17_02_Neighbor_Support_And_Search.ipynb
```

## 17.3 · Kernels and implicit feature spaces

- [A kernel is a specified geometry, not an arbitrary similarity score](notebooks/084_Chapter_17_03_Kernel_Assumptions_And_Seasonality.ipynb#kernels)
- [Check a finite feature map and reject an indefinite matrix](notebooks/084_Chapter_17_03_Kernel_Assumptions_And_Seasonality.ipynb#features)

Declared mechanisms: positive-semidefinite Gram matrices, explicit polynomial feature identity, common-objective kernel ridge, linear radial and periodic assumptions.

```bash
python scripts/run_notebook.py notebooks/084_Chapter_17_03_Kernel_Assumptions_And_Seasonality.ipynb
```

## 17.4 · Support vector machines and margins

- [A margin is a decision score](notebooks/085_Chapter_17_04_Margins_Calibration_And_Regression_Tubes.ipynb#margins)
- [Calibrated decisions have a separate evidence boundary](notebooks/085_Chapter_17_04_Margins_Calibration_And_Regression_Tubes.ipynb#calibration)

Declared mechanisms: soft margins and balanced penalties, kernel boundary versus schematic feature map, independent score calibration, epsilon-insensitive regression.

```bash
python scripts/run_notebook.py notebooks/085_Chapter_17_04_Margins_Calibration_And_Regression_Tubes.ipynb
```

## 17.5 · Scalability and learned similarity

- [Compare explicitly specified candidates](notebooks/086_Chapter_17_05_Learned_Retrieval_And_Kernel_Approximations.ipynb#retrieval)
- [Approximate a kernel under a defined array budget](notebooks/086_Chapter_17_05_Learned_Retrieval_And_Kernel_Approximations.ipynb#approximation)

Declared mechanisms: linear supervised NCA and tuned neighbors, fold-contained label-valued retrieval context, candidate-budget recall and array memory, random Fourier and Nystroem Gram approximations.

```bash
python scripts/run_notebook.py notebooks/086_Chapter_17_05_Learned_Retrieval_And_Kernel_Approximations.ipynb
```

## Interpretation and boundaries

Five self-contained CPU laboratories use seeds1782–1786 and the existing Python3.14.3/NumPy2.4.4/SciPy1.17.1/pandas3.0.3/Matplotlib3.11.0/scikit-learn1.9.0 environment. Already-pinned threadpoolctl3.7.0 explicitly limits loaded BLAS pools to one thread for reproducible kernel/figure arithmetic. All five initial experiments passed. Notebook085 initially emitted a FutureWarning because version1.9 deprecates the explicit probability argument even when false; it reran with the documented margin-only default and asserts that the public probability-prediction interface is unavailable. An intermediate rerun also exposed deprecated probability-array inspection; the final source checks public interface availability instead. No warning is suppressed. All five reran with shorter panel titles after visual review found collisions in the notebook outputs. Exact numerical result dictionaries are preserved across layout reruns. No dependency was added; ordinary execution is offline. Counts and geometry are synthetic or declared, with no field-validity or population-prevalence assertion.

082 fixes a query40000N/4m/steel with complete A/B/C/D. Raw stored N/m Euclidean selectsA; force conversion to kN alone selectsB. Reference scales50000N/2m selectB under consistent unit conversion. An80-record separately generated admitted training covariance with10%diagonal shrinkage gives Mahalanobis distances[6.223457,.227165,.733822,1.723058] and unit-conversion invariance. This is numerical geometry, not a validated mechanical similarity law. Custom mixed mean absolute normalized numeric/material mismatch gives E zero distance on two shared fields but excludes it under the declared three-field rule. F shares no fields and returnsNone, not zero. Pair-dependent missingness rules need not satisfy metric assumptions. A200-record origin-query diagnostic adds50independent nuisance dimensions to2D: distance coefficient of variation falls .498302→.098003 and top-five overlap is0. No prediction-accuracy claim follows from those geometric checks.

083 generates train300/development120 inside[0,1]^2, response sin5load+.6span+NormalSD.15. Training-only StandardScaler and six k/weight candidates select k9/distance by development MSE .0336259. Final source-like200 has MSE .0313019 and mean ninth-distance .345589; unusual40 in[1.5,2]^2 has MSE3.951934 and distance4.361285. Distances are support diagnostics, not intervals. Exact brute/KDtree top-five IDs/distances agree. A predeclared100-of300candidate subset has exact-top5recall .2975; fixed selected predictor source MSE worsens .0504737 while unusual MSE happens to improve3.003388. Retain both outcomes: retrieval recall is not monotone predictive quality, and subset search does not repair extrapolation.300vs100 distance candidates are not wall-time speedups or HNSW/FAISS results. A separate duplicate-zero fixture predicts2from co-located responses1and3, excluding response10atdistance1; it audits weighting, not duplicate evidence validity.

084 generates train120/development80/final200within seasonal months0–12 and future60within12–24. Response=.8load+sin(2pi*time/12)+NormalSD.15; known period12 and kernel shape controls are fixed. Training-only load scaling/time centering and fixed training-response offset .0145226 precede common KRR solves(K+n*lambda I). Linear/RBFgamma1/additive-load-plus-periodiclength.7 choose lambda .01/.001/.001 by development. Source-final MSE .215424/.168332/.0222264; future3.227959/1.324875/.0240803. An independent locked80-record load-zero slice gives1.855413/.597297/.0249532. Curves/observations share that slice. Periodic success reflects the constructed generator, not discovered future physics. Six-dimensional polynomial map exactly matches(1+u.v)^2; symmetric[[1,2],[2,1]]has eigenvalues[-1,3] and is rejected. No finite exact RBF-map or probability-output claim.

085 rare circular positives with .01flips have43/500training,25/200development,27/200calibration,45/400final positives. Stored[1000*x1,x2] uses training-only scaling. Balanced-penalty linear SVC grid3 and RBF grid9 select C.1linear and C1/gamma1RBF by development balanced accuracy. Final margin-zero balanced accuracy .664006/.939906, separately sigmoid-calibrated probability-half .5/.9. Calibration logistic C1 fits calibration margins at natural generated prevalence only; no final threshold/model tuning. Final Brier .100561/.0229856 and logloss .354071/.107403. Support counts496/127 and training hinge violations496/121 are observed, not set byC. Five final calibration groups each contain80records. Schematic radius-squared map is explicitly not the exact RBF feature map. Separate fixed SVR train100/final120,C5/epsilon.1/gamma4 has57support vectors,.49training fraction inside the tube with .002numerical tolerance and finalMSE .0190589. The epsilon band is a loss tolerance, not a probability interval.

086 generates train240/development120/final300,12independent normal descriptors, XOR signal in first2 plus.05label flips. Baseline scaled kNN and linear2D NCA kNN each select six k/weight candidates by development Brier. Both select15neighbors, baseline distance/NCAuniform. NCA PCA initialization/max_iter50/tol1e-5 and norm rescaling are fixed; public n_iter_ full/folds[28,33,36,46,46,51] is retained honestly, including the51counter, without a convergence certificate. The separately specified retrieval-context stack uses top15 soft NCA neighbors and26features(rawquery12,labelmean1,original-feature differences12,weighted sqdistance1). Entire scaler/NCA fit is contained within each of five OOFmemory folds; query labels never enter their own first-level encoder or neighbor values. Rotation-sensitive embedding-coordinate differences are avoided. Fixed C1 logistic meta-head plus training-only meta scaling fits OOFfeatures; development selects temperature1of[.05,.2,1]. Deployment encoder/memory uses alltraining only. This is not a neural TabR/ModernNCA execution or paper reproduction. Final baseline/NCA/stack Brier .235156/.214548/.226626, clipped1e-6logloss .662730/.772107/.652284, probability-half accuracy .61/.68/.67. NCA improvesBrier but worsenslogloss. Invalid1NNselftrainingaccuracy1is flagged and excluded. Fixed60-of240subset top15recall .249778; distance candidates240vs60 are not timings. Array ledger rawtraining23040B/keys3840B/labels1920B/NCAmap192B excludes process/Python/temporary overhead.

The isolated RBFgamma.2 approximation audit uses64Fourier features or64Nystroem landmarks on training-standardized inputs. Development Gram relative Frobenius error is1.184026/.807916; each training feature matrix122880B plus transform arrays6656/38912B versus dense training Gram460800B. Shared inputs/workspaces/Python/process overhead are excluded consistently. Manual cosine map matches RBFSampler; approximate Grams are PSD within arithmetic tolerance. No response-model comparison or claim that lower Gram error implies better prediction is attached.

Ten original vector figure sets implement both planned visual briefs, with four numbered equations and ten exercises. Official neighbor/SVC/NCA/kernel-approximation references and TabR primary preprintv2Section3.2 were inspected20October2026. TabR's retrieved features/labels and learned architecture are documentary context; its original neural implementation/benchmark and neural ModernNCA are not executed. Live sklearn1.9.1 versus executed1.9.0 is disclosed. Every cost, score, transformation and memory boundary remains explicitly scoped.
