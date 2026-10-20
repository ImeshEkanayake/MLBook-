# Chapter 26: Neural operators and learned simulation — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_26_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 26.1 · From finite-dimensional maps to operators

- [A case is a complete physical input function pair](notebooks/133_Chapter_26_01_operator_datasets_and_discretization.ipynb#operator-case-contract)
- [More output queries do not add missing input information](notebooks/133_Chapter_26_01_operator_datasets_and_discretization.ipynb#sampling-and-transfer)

Declared mechanisms: actual variable-coefficient solution family, whole-problem fitting and assessment, finite-grid Ridge operator reference, independent mesh refinement, input-sensor alias nonidentifiability.

```bash
python scripts/run_notebook.py notebooks/133_Chapter_26_01_operator_datasets_and_discretization.ipynb
```

## 26.2 · DeepONet and branch--trunk representations

- [The branch encodes one function; the trunk encodes one query](notebooks/134_Chapter_26_02_deeponet_and_operator_objectives.ipynb#branch-trunk-contract)
- [The training evidence differs even when the serving computation agrees](notebooks/134_Chapter_26_02_deeponet_and_operator_objectives.ipynb#operator-objective-limits)

Declared mechanisms: actual native branch-trunk inner-product network, fixed input sensors and variable output queries, supervised versus discrete physics operator objectives, whole-function development selection, higher-frequency input-support assessment.

```bash
python scripts/run_notebook.py notebooks/134_Chapter_26_02_deeponet_and_operator_objectives.ipynb
```

## 26.3 · Fourier and spectral neural operators

- [Fourier parameters have a declared physical grid and frequency meaning](notebooks/135_Chapter_26_03_fourier_operator_and_resolution_checks.ipynb#fourier-operator-contract)
- [A reusable spectral matrix does not guarantee reusable accuracy](notebooks/135_Chapter_26_03_fourier_operator_and_resolution_checks.ipynb#fourier-transfer-limits)

Declared mechanisms: actual native complex spectral convolution, lifting local paths and projection, same-function grid transfer without refitting, retained-mode and FFT identity checks, nonlinear aliasing and changed spectral support.

```bash
python scripts/run_notebook.py notebooks/135_Chapter_26_03_fourier_operator_and_resolution_checks.ipynb
```

## 26.4 · Graph and geometry-aware operators

- [Geometry, measures and boundary semantics travel with the field](notebooks/136_Chapter_26_04_geometry_graph_operator_and_mesh_transfer.ipynb#geometry-operator-contract)
- [Weighted graph access does not establish geometry generalization](notebooks/136_Chapter_26_04_geometry_graph_operator_and_mesh_transfer.ipynb#geometry-transfer-limits)

Declared mechanisms: native triangular finite-element problem family, actual quadrature-weighted learned graph kernel, whole-mesh geometry assessment, node-permutation identity, new mesh resolution and notched domain.

```bash
python scripts/run_notebook.py notebooks/136_Chapter_26_04_geometry_graph_operator_and_mesh_transfer.ipynb
```

## 26.5 · Surrogates, rollouts and inverse design

- [Two small tasks separate surrogate reuse from physical verification](notebooks/137_Chapter_26_05_surrogate_rollouts_and_inverse_design.ipynb#rollout-and-design-contract)
- [Optimize the surrogate, then ask the physical solver a new question](notebooks/137_Chapter_26_05_surrogate_rollouts_and_inverse_design.ipynb#verification-and-amortization)

Declared mechanisms: actual repeated learned heat-step rollout, mass-preserving projection audit, surrogate design optimization with analytic gradients, independent refined solver verification, bootstrap disagreement and actual solve counts.

```bash
python scripts/run_notebook.py notebooks/137_Chapter_26_05_surrogate_rollouts_and_inverse_design.ipynb
```

## Interpretation and boundaries

## Operator evidence and boundaries

Five independent generated-data laboratories (code_133–code_137; seeds3133–3137) expose function sampling, actual operator computation, geometry and repeated-use contracts. Current fresh kernels pass twenty code cells and ten inline figures with no error or stderr warnings. Ordinary execution is offline and CPU-only; all inputs/helpers/imports are internal. No dependency is added. Existing Torch2.14.1, NumPy2.4.4, SciPy1.17.1, pandas3.0.3, Matplotlib3.11.0 and scikit-learn1.9.0 pins remain unchanged. Printed versions, hardware, deterministic Torch float64 settings and thread limits are retained in every notebook.

### Cases and finite representations — code_133

A variable-coefficient Dirichlet bar family has64 source,16 development,32 final and32 changed-frequency cases. Three material/four load coefficients define smooth positive conductance and forcing. Inputs contain32 samples of each field, outputs65 fixed positions from a63-interior-position finite-volume solve. Source-only preprocessing and development alpha choices0.001/0.1/10 select0.001 for a finite-grid multioutput Ridge. Final fixed-grid MSE0.000629058; changed-frequency MSE0.000435147; interpolated129-query final MSE0.000633721. Different target spectra/scales prevent treating the smaller changed-frequency absolute error as a universal easier/harder ordering.

Native reference65→129 refinement gives RMS0.0000137553 on final cases. Output interpolation is explicit, not claimed sampling-invariant operator learning. A separate exact constant-coefficient witness adds sin(31*pi*x): its thirty-two endpoint-inclusive input sensors differ by at most1.42109e-14, but exact solutions differ by up to0.000105433. More output queries cannot identify missing input components. VisualA shows several source input/output functions behind one complete final case.

### Actual branch–trunk models — code_134

The Dirichlet Poisson family has128 source/32 development/64 final functions using four sine modes, plus64 final frequency5–8 functions. A32-sensor branch and coordinate trunk produce16 features each, their inner product/bias multiplied by x(1−x) and source-only scale. Both2177-parameter supervised and discrete-physics recipes receive rates0.003/0.01 and1,200 updates, with development checkpoints every40updates. Supervised source fields have33 queries (4,224 scalar labels); discrete physics instead uses31 interior finite-difference equations per source case (3,968 constraints). Both use2,080 development solution values at65 queries for selection. Final129-point assessment remains separate. Hard endpoint values are exactlyzero; a nonboundary inner-product trace checks actual output composition.

Both select rate0.01, supervised update1200/physics1160. Final source-frequency MSE1.43620e-5 versus7.73824e-6; higher-frequency MSE0.000132623 versus0.000204412. Explicitly interpolated fixed-grid Ridge has source-frequency final error5.89002e-9, retaining the strong linear reference rather than manufacturing a neural win. Source output scale0.0681025. The discrete-physics recipe is not a continuous-residual or zero-validation-label guarantee.

During authoring, code review caught solution targets accidentally constructed with the forcing helper's default rather than its solution branch. That unpublished run was invalid for the intended task; its snapshot is retained locally as134-before-target-correction.json. All target, development, assessment and scaling calls were corrected to analytic displacement, then the identical candidate budgets were rerun. A unit-mode analytic target assertion and coefficient-equation check (max2.22045e-16) were added. No candidate settings were chosen from those mistaken results. A later three-panel layout repair reran the current valid experiment; full deterministic RESULTS are reproduced into the book figures.

### Native Fourier operator — code_135

A periodic unit-domain heat step uses diffusivity0.003 and elapsed time0.1, with exact Fourier-generated truth. Source128/development32/final64 functions have modes1–6 plus a constant;64 additional final functions have modes10–14 plus a constant. A three-block native Torch spectral/local/GELU model lifts to width8, retains rFFT modes0–7 and projects one output channel. Its3,465 stored real scalar parameters include real/imaginary coefficients, including nonidentifiable imaginary parts at real-only frequencies. Rates0.003/0.01 each receive800 full-batch updates and40-step development checkpoints; rate0.01/update800 is selected.

Frozen32-grid weights evaluate the same analytic final functions on32/64/128 grids. Familiar-frequency field MSEs0.000133781/0.000130202/0.000130010, relative L2errors0.008405/0.008291/0.008285. High-frequency errors0.00880750/0.00871830/0.00872657, relative L2around0.402. Mean mass is not exactly preserved: reported absolute mean errors remain separate. Resolution-compatible parameter shapes do not repair unseen spectral support.

Independent retained-sine identity tests at all three resolutions and constant/Nyquist FFT round trips check the actual normalization. Squaring mode12 produces a mode24 component that aliases to mode8 at32 points (amplitude0.5) but not128 points (mode8 amplitude3.68050e-16). One-sided figure amplitudes were corrected to avoid doubling DC/Nyquist values; actual model/alias RESULTS remained exactly unchanged in a fresh kernel. The nonlinear alias is an independent calculation, not an attribution of a specific trained-model error. Periodic boundaries are explicit; no full neuraloperator package or published speedup is claimed.

### Geometry and quadrature — code_136

Own P1 triangular finite-element assembly uses SciPy Delaunay and NumPy linear solves, constant positive material per case, lumped load weights and extracted Dirichlet boundary edges. Source32/development8/final8 rectangles have known dimensions/material/load parameters and25-node meshes with interior jitter. The481-parameter dense pair-kernel integrates source forcing with actual nodal areas. Every query accesses every source node, with quadratic pair cost, rather than a fixed-hop local message network. Boundary-node masks impose exact zeros only at supplied boundary queries.

Rates0.003/0.01 each receive400 updates and20-step whole-development checkpoints;0.01/update400 is selected. Final rectangle mean-case/all-node MSE9.54723e-6 and interior2.65201e-5. The same eight cases remeshed at regular81-node grids have2.17515e-5/3.59565e-5. Remeshing changes both placement and density. Two native coarse/finer-reference RMS differences0.00142161/0.00178523 disclose nonnegligible reference discretization error; continuum accuracy is not asserted.

Twelve unseen notched domains have21 nodes each. Their geometry, topology and boundary proportion differ, with no selection labels used. All-node/interior error4.16888e-5/0.000175093, boundary outputs exactlyzero. During source review, nominal notch-boundary coordinates were exempted from interior jitter so the experiment represents the intended retained L-domain; an unpublished earlier geometry snapshot is saved locally as136-before-notch-boundary-correction.json. Rectangle fitting/candidates/results remain unchanged. Node permutation changes predictions1.38778e-17 when every aligned input moves together. Replacing area quadrature with uniform weights changes one output RMS0.00497101, demonstrating an adapter contract. VisualB aligns actual branch/trunk, spectral and weighted irregular-domain computations; reference triangulation is distinguished from dense learned access. This small kernel is not full GINO.

### Reuse and inverse design — code_137

Two separate tasks remain explicitly separated. A sixteen-grid heat-step Ridge fits128 source functions with declared response-label offset0.002 and Gaussian SD0.003;32 clean development functions select alpha0.001 from1e-5/0.001/0.1;64 independent clean final functions assess forty rollouts. Raw one-step/final40 MSE4.48781e-6/0.00628513; final mean error0.0787278. Known-initial-mean projection leaves40-step MSE0.0000515799 and mean error1.55041e-17. The fitted affine step map's linear spectral radius1.000620798 is a stability diagnostic, not a nonlinear error theorem.

A scalar center-displacement bar surrogate uses64 source/16 development designs within[−0.6,0.6]² and32 independently refined final cases. Degree-two Ridge alpha0.1 is selected; final MSE1.97419e-8. Its analytic design gradient agrees with finite differences to1.10886e-12. Optimization over broader[−1.5,1.5]² asks for displacement0.22 and produces[-0.00169951,0.94191000], outside source support. Surrogate prediction0.219906308;257-position independent solve0.220436600, accepted at predeclared absolute tolerance0.0005. Four bootstrap values have SD0.000257784; this is fit variability, not a calibrated predictive interval.

Separately counted solver-assisted refinement gives design[9.50161e-7,0.93665305] and independent257-position response0.219903969. Mechanical solve counts are80 at63 interior positions,68 at127 (32 final assessments plus36 refinement calls), and two at257. The surrogate optimizer uses nine objective calls. Data generation, fitting, serving and verification costs are discussed symbolically; no invented measured speedup is claimed. The design plot's legend was moved to expose the out-of-support proposal, and response errors expanded relative to the target with tolerance lines. Fresh reruns preserve exact numerical RESULTS.

## Primary sources and visual QA

Read primary records/documentation20October2026, with literature bounded by18October2026: original three-author DeepONet preprint1910.03193 (8October2019; v3 15April2020), FNO2010.08895 (18October2020; v3 17May2021), GINO2309.00583 (1September2023), official NeuralOperator2.0.0 theory/implementation guidance and official DeepXDE operator demos. These are conceptual/algorithm attribution, not installed backends or reproduced benchmark claims. Later DeepONet publication author lists are not attached to the distinct earlier preprint.

All ten current inline and ten original grayscale vector-book figures are inspected, including final mapping title, corrected FFT endpoint amplitudes, branch/trunk layout, notched geometry and expanded inverse-design error. Original SVG/vector-PDF/PNG files share stems. Figure generation reruns every current notebook cell and asserts exact RESULTS agreement with successful fresh kernels. No resource/timing replay exception applies. Chapter26 contains2,696 conservative substantive words across five exact scopes, ten figures, five equations, one code map and fifteen exercises. Final composed-page, preservation and publication proofs are recorded separately after compilation.
