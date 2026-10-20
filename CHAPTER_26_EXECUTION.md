# Chapter 26 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** executed; publication verification pending.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_133 | 26.1 | 4 | 2 | 2.261 |
| code_134 | 26.2 | 4 | 2 | 3.405 |
| code_135 | 26.3 | 4 | 2 | 8.784 |
| code_136 | 26.4 | 4 | 2 | 5.540 |
| code_137 | 26.5 | 4 | 2 | 2.300 |

Total: **20 executed code cells and 10 inline figures**. Current outputs contain no errors and all assertions pass. Figure review is completed during the book delivery review.

## Actual mechanisms and boundaries

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

## Successful result dictionaries

### code_133

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3133.

```json
{
  "candidates": [
    {
      "alpha": 0.001,
      "development_MSE": 0.00023755158521376416
    },
    {
      "alpha": 0.1,
      "development_MSE": 0.00024924421772019796
    },
    {
      "alpha": 10.0,
      "development_MSE": 0.0002693565497898392
    }
  ],
  "case_counts": [
    64,
    16,
    32,
    32
  ],
  "changed_frequency_MSE": 0.0004351470573704551,
  "final_fixed_grid_MSE": 0.0006290578449163966,
  "final_interpolated_fine_grid_MSE": 0.0006337214128244511,
  "finer_output_locations": 129,
  "fixed_output_locations": 65,
  "input_alias_max_difference": 1.4210854715202004e-14,
  "input_channels": [
    "positive coefficient",
    "forcing"
  ],
  "input_sensor_count_per_field": 32,
  "reference_65_vs_129_grid_RMS": 1.3755328684900674e-05,
  "selected_alpha": 0.001,
  "unidentifiable_solution_max_difference": 0.00010543307350919646
}
```

### code_134

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3134.

```json
{
  "analytic_target_check_max_error": 2.220446049250313e-16,
  "candidates": [
    {
      "best_update": 1200,
      "development_MSE": 9.790469115958765e-06,
      "learning_rate": 0.003,
      "recipe": "Supervised branch\u2013trunk"
    },
    {
      "best_update": 1200,
      "development_MSE": 4.545476368869042e-06,
      "learning_rate": 0.01,
      "recipe": "Supervised branch\u2013trunk"
    },
    {
      "best_update": 1040,
      "development_MSE": 2.353861439427188e-06,
      "learning_rate": 0.003,
      "recipe": "Discrete-physics branch\u2013trunk"
    },
    {
      "best_update": 1160,
      "development_MSE": 7.253720754607403e-07,
      "learning_rate": 0.01,
      "recipe": "Discrete-physics branch\u2013trunk"
    }
  ],
  "case_counts": [
    128,
    32,
    64,
    64
  ],
  "comparisons": [
    {
      "best_update": 1200,
      "development_MSE": 4.545476368869042e-06,
      "final_129_query_MSE": 1.4362019368912086e-05,
      "higher_frequency_MSE": 0.00013262334628054605,
      "max_boundary_defect": 0.0,
      "model": "Supervised branch\u2013trunk",
      "parameters": 2177,
      "selected_learning_rate": 0.01
    },
    {
      "best_update": 1160,
      "development_MSE": 7.253720754607403e-07,
      "final_129_query_MSE": 7.738244090634755e-06,
      "higher_frequency_MSE": 0.0002044121307162123,
      "max_boundary_defect": 0.0,
      "model": "Discrete-physics branch\u2013trunk",
      "parameters": 2177,
      "selected_learning_rate": 0.01
    }
  ],
  "development_field_labels_per_recipe": 2080,
  "development_queries": 65,
  "final_queries": 129,
  "input_sensors": 32,
  "interpolated_fixed_grid_Ridge_final_MSE": 5.890019567900834e-09,
  "physics_source_equation_constraints": 3968,
  "source_output_queries": 33,
  "source_output_scale": 0.06810250098711444,
  "source_supervised_scalar_labels": 4224
}
```

### code_135

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3135.

```json
{
  "FFT_normalization": "forward for transform and inverse",
  "best_update": 800,
  "candidates": [
    {
      "best_update": 800,
      "development_MSE": 0.0006177733106658945,
      "learning_rate": 0.003
    },
    {
      "best_update": 800,
      "development_MSE": 0.0003035280224026267,
      "learning_rate": 0.01
    }
  ],
  "case_counts": [
    128,
    32,
    64,
    64
  ],
  "comparisons": [
    {
      "cohort": "Source-frequency final",
      "field_MSE": 0.00013378117994685857,
      "mean_mass_absolute_error": 0.0028349612505254645,
      "points": 32,
      "relative_L2": 0.008404700256117814
    },
    {
      "cohort": "High-frequency final",
      "field_MSE": 0.008807498553916392,
      "mean_mass_absolute_error": 0.021277495145605674,
      "points": 32,
      "relative_L2": 0.40403480914529877
    },
    {
      "cohort": "Source-frequency final",
      "field_MSE": 0.000130201702931039,
      "mean_mass_absolute_error": 0.002779798602957426,
      "points": 64,
      "relative_L2": 0.008291498960662558
    },
    {
      "cohort": "High-frequency final",
      "field_MSE": 0.008718303592407398,
      "mean_mass_absolute_error": 0.0215759654438013,
      "points": 64,
      "relative_L2": 0.40198374014378113
    },
    {
      "cohort": "Source-frequency final",
      "field_MSE": 0.00013001014970402753,
      "mean_mass_absolute_error": 0.0027751241566662155,
      "points": 128,
      "relative_L2": 0.008285397473732055
    },
    {
      "cohort": "High-frequency final",
      "field_MSE": 0.008726571568130007,
      "mean_mass_absolute_error": 0.02156204027540621,
      "points": 128,
      "relative_L2": 0.4021743049803425
    }
  ],
  "diffusivity": 0.003,
  "evaluation_grids": [
    32,
    64,
    128
  ],
  "quadratic_alias_amplitude_at_mode8": {
    "128_point_grid": 3.680496651235158e-16,
    "32_point_grid": 0.5
  },
  "real_scalar_parameters": 3465,
  "retained_modes": [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7
  ],
  "selected_rate": 0.01,
  "step": 0.1,
  "training_grid": 32
}
```

### code_136

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3136.

```json
{
  "best_update": 400,
  "candidates": [
    {
      "best_update": 400,
      "development_MSE": 2.06033319319708e-05,
      "learning_rate": 0.003
    },
    {
      "best_update": 400,
      "development_MSE": 5.904736737648079e-06,
      "learning_rate": 0.01
    }
  ],
  "case_counts": [
    32,
    8,
    8,
    12
  ],
  "coarse_vs_finer_FEM_reference_RMS": [
    0.0014216127838767333,
    0.0017852307184760365
  ],
  "comparisons": [
    {
      "cases": 8,
      "cohort": "Rectangle final, irregular25",
      "max_boundary_defect": 0.0,
      "mean_case_field_MSE": 9.547232013623346e-06,
      "mean_interior_MSE": 2.652008892673151e-05,
      "node_counts": [
        25,
        25,
        25,
        25,
        25,
        25,
        25,
        25
      ]
    },
    {
      "cases": 8,
      "cohort": "Rectangle final, regular81",
      "max_boundary_defect": 0.0,
      "mean_case_field_MSE": 2.1751460314320944e-05,
      "mean_interior_MSE": 3.595649562163259e-05,
      "node_counts": [
        81,
        81,
        81,
        81,
        81,
        81,
        81,
        81
      ]
    },
    {
      "cases": 12,
      "cohort": "Notched final, unseen geometry",
      "max_boundary_defect": 0.0,
      "mean_case_field_MSE": 4.16887537772823e-05,
      "mean_interior_MSE": 0.0001750927658645857,
      "node_counts": [
        21,
        21,
        21,
        21,
        21,
        21,
        21,
        21,
        21,
        21,
        21,
        21
      ]
    }
  ],
  "parameters": 481,
  "permutation_max_difference": 1.3877787807814457e-17,
  "selected_rate": 0.01,
  "source_whole_graph_scale": 0.03188272216482574,
  "uniform_vs_area_quadrature_prediction_RMS": 0.004971010644879778
}
```

### code_137

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 3137.

```json
{
  "bootstrap_predictions": [
    0.2202959470071097,
    0.21995810373277505,
    0.21991041132749878,
    0.21967009998082093
  ],
  "bootstrap_standard_deviation": 0.000257783922530656,
  "design_case_counts": [
    64,
    16,
    32
  ],
  "design_selected_alpha": 0.1,
  "final_design_surrogate_MSE": 1.9741894514636468e-08,
  "fitted_one_step_spectral_radius": 1.0006207976582284,
  "heat_case_counts": [
    128,
    32,
    64
  ],
  "heat_selected_alpha": 0.001,
  "heat_source_label_offset": 0.002,
  "heat_source_noise_sd": 0.003,
  "native_solver_call_counts": {
    "127": 68,
    "257": 2,
    "63": 80
  },
  "proposal": [
    -0.0016995093465610074,
    0.9419100045018169
  ],
  "proposal_accepted_at_tolerance": true,
  "proposal_independent_solver": 0.22043659982336453,
  "proposal_surrogate_prediction": 0.21990630840029393,
  "refined_design": [
    9.501608443145284e-07,
    0.9366530528569532
  ],
  "refined_independent_solver": 0.21990396860850736,
  "requested_displacement": 0.22,
  "rollout": [
    {
      "projected_MSE": 7.748860810372975e-07,
      "projected_mean_absolute_error": 4.846383711010205e-17,
      "raw_MSE": 4.487809211656777e-06,
      "raw_mean_absolute_error": 0.0019178781580743089,
      "step": 1
    },
    {
      "projected_MSE": 1.5695861595442136e-06,
      "projected_mean_absolute_error": 4.705437428587089e-17,
      "raw_MSE": 1.648788892952326e-05,
      "raw_mean_absolute_error": 0.003844538309148724,
      "step": 2
    },
    {
      "projected_MSE": 2.6588960882648734e-06,
      "projected_mean_absolute_error": 4.662069341687669e-17,
      "raw_MSE": 3.631322383181138e-05,
      "raw_mean_absolute_error": 0.005775205651730654,
      "step": 3
    },
    {
      "projected_MSE": 3.910085195608149e-06,
      "projected_mean_absolute_error": 3.5236570605778894e-17,
      "raw_MSE": 6.386553680311707e-05,
      "raw_mean_absolute_error": 0.007709540491289412,
      "step": 4
    },
    {
      "projected_MSE": 5.245269822957327e-06,
      "projected_mean_absolute_error": 3.209238430557093e-17,
      "raw_MSE": 9.909889040045904e-05,
      "raw_mean_absolute_error": 0.00964725033201783,
      "step": 5
    },
    {
      "projected_MSE": 6.61971287306885e-06,
      "projected_mean_absolute_error": 2.8514517136368767e-17,
      "raw_MSE": 0.00014199828991162878,
      "raw_mean_absolute_error": 0.011588082770774093,
      "step": 6
    },
    {
      "projected_MSE": 8.00850949468708e-06,
      "projected_mean_absolute_error": 2.222614453595284e-17,
      "raw_MSE": 0.00019256664416661856,
      "raw_mean_absolute_error": 0.013531819518462693,
      "step": 7
    },
    {
      "projected_MSE": 9.398463298961753e-06,
      "projected_mean_absolute_error": 3.3285006695304986e-17,
      "raw_MSE": 0.00025081689170833223,
      "raw_mean_absolute_error": 0.01547827136396246,
      "step": 8
    },
    {
      "projected_MSE": 1.078316443763137e-05,
      "projected_mean_absolute_error": 2.970713952610282e-17,
      "raw_MSE": 0.00031676730197368783,
      "raw_mean_absolute_error": 0.017427273926660793,
      "step": 9
    },
    {
      "projected_MSE": 1.2160033198791202e-05,
      "projected_mean_absolute_error": 2.688821387764051e-17,
      "raw_MSE": 0.00039043871556928363,
      "raw_mean_absolute_error": 0.01937868406935624,
      "step": 10
    },
    {
      "projected_MSE": 1.3528563521836003e-05,
      "projected_mean_absolute_error": 2.3201926491189795e-17,
      "raw_MSE": 0.000471852959649449,
      "raw_mean_absolute_error": 0.021332376864646035,
      "step": 11
    },
    {
      "projected_MSE": 1.4889294381651335e-05,
      "projected_mean_absolute_error": 2.873135757086587e-17,
      "raw_MSE": 0.0005610319685388944,
      "raw_mean_absolute_error": 0.023288243025660064,
      "step": 12
    },
    {
      "projected_MSE": 1.62432193700511e-05,
      "projected_mean_absolute_error": 2.5045070184415152e-17,
      "raw_MSE": 0.0006579973223378381,
      "raw_mean_absolute_error": 0.025246186726755583,
      "step": 13
    },
    {
      "projected_MSE": 1.759145766062414e-05,
      "projected_mean_absolute_error": 2.168404344971009e-17,
      "raw_MSE": 0.0007627700291023172,
      "raw_mean_absolute_error": 0.027206123752055916,
      "step": 14
    },
    {
      "projected_MSE": 1.8935079079227535e-05,
      "projected_mean_absolute_error": 2.3527187142935446e-17,
      "raw_MSE": 0.0008753704455996772,
      "raw_mean_absolute_error": 0.029167979919924855,
      "step": 15
    },
    {
      "projected_MSE": 2.0275018642998967e-05,
      "projected_mean_absolute_error": 2.1738253558334364e-17,
      "raw_MSE": 0.0009958182740866922,
      "raw_mean_absolute_error": 0.03113168973996575,
      "step": 16
    },
    {
      "projected_MSE": 2.1612041941742033e-05,
      "projected_mean_absolute_error": 2.0925101928970236e-17,
      "raw_MSE": 0.0011241325983494153,
      "raw_mean_absolute_error": 0.03309719526621075,
      "step": 17
    },
    {
      "projected_MSE": 2.2946738509458163e-05,
      "projected_mean_absolute_error": 2.211772431870429e-17,
      "raw_MSE": 0.0012603319377954003,
      "raw_mean_absolute_error": 0.035064445116062805,
      "step": 18
    },
    {
      "projected_MSE": 2.4279529836112632e-05,
      "projected_mean_absolute_error": 1.8323016715005025e-17,
      "raw_MSE": 0.0014044343076790677,
      "raw_mean_absolute_error": 0.037033393629468656,
      "step": 19
    },
    {
      "projected_MSE": 2.561068435010003e-05,
      "projected_mean_absolute_error": 2.4069288229178198e-17,
      "raw_MSE": 0.001556457279026386,
      "raw_mean_absolute_error": 0.03900400014690274,
      "step": 20
    },
    {
      "projected_MSE": 2.694033506672252e-05,
      "projected_mean_absolute_error": 1.9244588561617704e-17,
      "raw_MSE": 0.0017164180350151487,
      "raw_mean_absolute_error": 0.040976228388165295,
      "step": 21
    },
    {
      "projected_MSE": 2.826849756920173e-05,
      "projected_mean_absolute_error": 1.9244588561617704e-17,
      "raw_MSE": 0.0018843334223843657,
      "raw_mean_absolute_error": 0.04295004591685775,
      "step": 22
    },
    {
      "projected_MSE": 2.959508712737805e-05,
      "projected_mean_absolute_error": 2.200930410145574e-17,
      "raw_MSE": 0.0020602199974510097,
      "raw_mean_absolute_error": 0.04492542367778925,
      "step": 23
    },
    {
      "projected_MSE": 3.09199344048249e-05,
      "projected_mean_absolute_error": 1.973247953923618e-17,
      "raw_MSE": 0.0022440940668424923,
      "raw_mean_absolute_error": 0.04690233559656877,
      "step": 24
    },
    {
      "projected_MSE": 3.2242799561635814e-05,
      "projected_mean_absolute_error": 1.5829351718288365e-17,
      "raw_MSE": 0.002435971723310916,
      "raw_mean_absolute_error": 0.04888075823231111,
      "step": 25
    },
    {
      "projected_MSE": 3.3563384749396856e-05,
      "projected_mean_absolute_error": 1.555830117516699e-17,
      "raw_MSE": 0.002635868877100208,
      "raw_mean_absolute_error": 0.050860670475789606,
      "step": 26
    },
    {
      "projected_MSE": 3.488134508878439e-05,
      "projected_mean_absolute_error": 1.5720931501039814e-17,
      "raw_MSE": 0.0028438012833596374,
      "raw_mean_absolute_error": 0.05284205328654515,
      "step": 27
    },
    {
      "projected_MSE": 3.619629826106131e-05,
      "projected_mean_absolute_error": 1.4907779871675686e-17,
      "raw_MSE": 0.0030597845660775003,
      "raw_mean_absolute_error": 0.054824889463449995,
      "step": 28
    },
    {
      "projected_MSE": 3.7507832856813265e-05,
      "projected_mean_absolute_error": 1.973247953923618e-17,
      "raw_MSE": 0.0032838342389696355,
      "raw_mean_absolute_error": 0.0568091634440559,
      "step": 29
    },
    {
      "projected_MSE": 3.881551562257159e-05,
      "projected_mean_absolute_error": 1.702197410802242e-17,
      "raw_MSE": 0.003515965723711434,
      "raw_mean_absolute_error": 0.05879486112875531,
      "step": 30
    },
    {
      "projected_MSE": 4.0118897736204444e-05,
      "projected_mean_absolute_error": 2.222614453595284e-17,
      "raw_MSE": 0.003756194365855707,
      "raw_mean_absolute_error": 0.060781969726373695,
      "step": 31
    },
    {
      "projected_MSE": 4.1417520229471426e-05,
      "projected_mean_absolute_error": 1.485356976305141e-17,
      "raw_MSE": 0.004004535448735411,
      "raw_mean_absolute_error": 0.062770477618308,
      "step": 32
    },
    {
      "projected_MSE": 4.271091866306601e-05,
      "projected_mean_absolute_error": 2.0383000842727483e-17,
      "raw_MSE": 0.004261004205611018,
      "raw_mean_absolute_error": 0.06476037423874588,
      "step": 33
    },
    {
      "projected_MSE": 4.399862714700496e-05,
      "projected_mean_absolute_error": 1.452830911130576e-17,
      "raw_MSE": 0.004525615830287813,
      "raw_mean_absolute_error": 0.06675164996885574,
      "step": 34
    },
    {
      "projected_MSE": 4.528018178777544e-05,
      "projected_mean_absolute_error": 1.1926223897340549e-17,
      "raw_MSE": 0.004798385486398118,
      "raw_mean_absolute_error": 0.06874429604313778,
      "step": 35
    },
    {
      "projected_MSE": 4.6555123633451517e-05,
      "projected_mean_absolute_error": 1.6425662913155392e-17,
      "raw_MSE": 0.005079328315517477,
      "raw_mean_absolute_error": 0.07073830446638171,
      "step": 36
    },
    {
      "projected_MSE": 4.782300117895679e-05,
      "projected_mean_absolute_error": 1.474514954580286e-17,
      "raw_MSE": 0.005368459444261156,
      "raw_mean_absolute_error": 0.07273366793989325,
      "step": 37
    },
    {
      "projected_MSE": 4.908337248579426e-05,
      "projected_mean_absolute_error": 1.6046192152785466e-17,
      "raw_MSE": 0.005665793990488059,
      "raw_mean_absolute_error": 0.07473037979583586,
      "step": 38
    },
    {
      "projected_MSE": 5.033580696366646e-05,
      "projected_mean_absolute_error": 1.4148838350935833e-17,
      "raw_MSE": 0.0059713470687223266,
      "raw_mean_absolute_error": 0.07672843393869103,
      "step": 39
    },
    {
      "projected_MSE": 5.157988685546539e-05,
      "projected_mean_absolute_error": 1.5504091066542713e-17,
      "raw_MSE": 0.006285133794888632,
      "raw_mean_absolute_error": 0.07872782479297505,
      "step": 40
    }
  ],
  "surrogate_gradient_max_difference": 1.1088630014199907e-12,
  "surrogate_optimization_calls": 9,
  "verification_tolerance": 0.0005
}
```

