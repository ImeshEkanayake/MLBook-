# Chapter 25 execution evidence

**Date:** 20 October 2026 (Australia/Melbourne). **Status:** published and executed; remote content verified.

All current sources ran in fresh kernels using the unchanged runner. Every import/helper and input is internal; ordinary execution is offline and CPU-only. Actual versions and hardware are printed by every kernel and retained below. No dependency was added. Wall times include kernel lifecycle and are observations, not comparative throughput promises. Check the chapter notes for individual reruns or repairs; independent initial jobs may have run concurrently.

| ID | Section | Code cells | Inline figures | Wall seconds |
| --- | --- | ---: | ---: | ---: |
| code_127 | 25.1 | 4 | 2 | 2.199 |
| code_128 | 25.2 | 4 | 2 | 5.655 |
| code_129 | 25.3 | 4 | 2 | 2.996 |
| code_130 | 25.4 | 4 | 2 | 2.560 |
| code_131 | 25.5 | 4 | 2 | 3.286 |
| code_132 | 25.6 | 4 | 2 | 4.054 |

Total: **24 executed code cells and 12 inline figures**. Current outputs contain no errors and all assertions pass. All twelve inline images and twelve original grayscale vector figures have been visually reviewed, including repaired forward/inverse and loss-assembly diagrams.

## Actual mechanisms and boundaries

## Scientific evidence and role boundaries

Six independent generated-data laboratories (code_127–code_132, seeds2927–2932) separate equation consistency, identification, numerical accuracy and physical validity. Each currently executes four code cells and produces two inline figures, without errors or stderr warnings. All transformations and inputs are defined inside each notebook; ordinary execution is offline, CPU-only and needs no credentials or private helper. No dependency is added. Existing Torch2.14.1 and numerical-library pins remain unchanged, with explicit CPU threads, float64, seeds and deterministic Torch settings.

### Forward and inverse beam — code_127

A unit-length simply supported Euler–Bernoulli beam has EI*w fourth derivative=q and zero endpoint displacements/moments. The exact polynomial independently checks native SciPy solve_bvp. Mesh/tolerance refinement from eight starting nodes/tolerance1e-5 to sixteen/tolerance1e-8 gives final meshes15/181 and maximum displacement errors1.01683e-7/3.72109e-12. Solver success and boundary residuals are checked separately.

Three interior sensors at0.2/0.5/0.8 have Gaussian generating noise SD0.00015. With known load3 and true EI2, fitted positive compliance recovers EI2.002769445. Dense field truth is assessment only. If load and stiffness are jointly unknown, equal ratios give identical entire fields; the whitened two-column sensitivity has singular values102.18397 and2.11688e-15, rankone. This is an explicit unidentifiable task, not a failed optimizer. Noise bars show the generating observation SD, not posterior/confidence intervals. VisualB connects forward known inputs and inverse sensor evidence beside the actual objective ridge.

### Actual beam PINN — code_128

Normalize v=24*EI*w/q, with fourth derivative24, endpoint v0 and second derivative0. Native Torch autograd first matches the exact polynomial's fourth derivative. Data loss uses six noisy interior v observations; equation loss uses32 fixed collocation points, scaled fourth derivative/24−1; boundary loss combines endpoint displacement and second derivative/12. Three321-parameter tanh models share initialization and1,200 Adam updates at0.005. Recipes are data-only, physics with boundary weight0.1 and physics with weight10. The independent63-point equation grid plus boundary defects selects between physics recipes; a separate401-point analytic/differential assessment does not select anything.

Data-only final field/residual MSE is7.07995e-6/1.540212. Physics weight0.1 has5.26427e-5/0.000188974 and max endpoint defect0.0230813. Weight10 is selected, with1.07619e-8/0.0000864809 and endpoint defect0.000293158. All fixed candidates remain. Initial unweighted parameter-gradient norms are0.329584/0.266531/0.409302 for data/equation/boundary; training histories keep their separate magnitudes. VisualA assembles the three evidence-derived losses before weighting. Smooth fourth-order differentiation does not certify the physical model or boundary assumptions.

### Boundary and conservation constructions — code_129

For −u second derivative=pi²sin(pi*x), both321-parameter tanh fits get32 source points and1,000 fixed Adam updates at0.005. The soft boundary penalty is10; the hard model multiplies its output by x(1−x). Independent401-point field errors are1.37270e-7 versus6.17350e-9, scaled residual errors5.59926e-5 versus6.55564e-6, and max endpoint defects2.27670e-5 versus exactlyzero. The hard construction fixes only displacement endpoints, not the full differential problem.

A separate twelve-interior-node chain learns thirteen positive conductances from eight source load/response cases, with two development and two final cases. Conductance MSE0.000358478 coexists with final response MSE2.83117e-10. Shared signed edge fluxes and the differentiable solve enforce interior balance to8.88178e-15 and global boundary-flux/load balance to5.55112e-16. Positivity ensures the declared connected Dirichlet operator is SPD; cancellation follows from incidence assembly, not positivity alone. Full noiseless source response labels and a known domain are strong teaching assumptions, not sparse field material recovery.

### Learned dynamics — code_130

Generated unit-mass oscillator dynamics use stiffness1.7 and damping0.25. Twenty initial conditions supply exact observed states/derivatives over0–4; five development and five final initial conditions remain whole-case holdouts. Final RK4 trajectories extend0–12. Derivative-supervised identification observes velocity and derivative labels, rather than hiding them inside a trajectory-only inverse claim. Both a354-parameter neural field and a two-parameter positive mechanical field fit1,200 Adam updates at0.01. The mechanical field is deliberately matched to the generating family.

Final rollout MSEs are4.41229e-5 and5.23308e-13. Step halving0.05→0.025 changes paths RMS2.52638e-7/2.51624e-7; mechanical continuous energy identity defect2.08167e-17. Learned stiffness/damping1.700000285/0.250001192. Direct RK4 parameter gradient0.0513850423095 agrees with finite difference0.0513850423142 (difference4.70880e-12). Native DOP853 reference refinement1e-7→1e-10 gives max analytic errors6.86869e-8/4.71827e-11 with332/767 field evaluations. No comparative timing or continuous-adjoint implementation is claimed.

A frozen neural drift with a prescribed observed control increment path has prefix perturbation differencezero; the entire displayed control segment is observed, not secretly forecast. This is a small controlled-input mechanism, not full neural CDE training. An Itô Euler–Maruyama neural-drift SDE uses known constant velocity diffusion0.2 and512 paths to time2. Coarse0.02 and fine0.01 paths share aggregated Brownian increments; refinement RMS0.001933107. Empirical learned-drift covariance[[0.0201926,0.00313266],[0.00313266,0.0243813]] is compared with exact generating linear covariance[[0.0208132,0.00194145],[0.00194145,0.0270873]]. Finite sampling and drift error remain; diffusion is neither learned nor calibrated. Hamiltonian/Lagrangian and stiff-solver discussions are conceptual, not extra unexecuted implementation claims.

### Hybrids and fidelity — code_131

Known-domain axial mechanics uses varying slope/material/load-amplitude/load-shape inputs, source32/development8/final16 cases in source support and sixteen shifted material cases. Fine63-interior-position and coarse12-position solves differ in grid and omitted spatial stiffness modulation. High-fidelity source fields are labels. Each data-only/residual Ridge independently selects alpha0.001 from0.001/0.1/10 on development cases. Residual Ridge includes the available coarse field at inference; data-only Ridge receives parameters. A two-parameter exponential positive-conductance closure fits1,000 updates, deliberately matching the generating modulation form while absorbing coarse discretization error. It is parametric, not a general neural material law.

Final mean field MSEs: coarse1.35610e-5, data-only2.92428e-8, residual8.66815e-9, closure8.11060e-8. Changed-support errors:1.31845e-5,2.19188e-5,6.07147e-8,1.12460e-7. The residual method wins these bounded cases; closure conservation does not guarantee lowest field error. Fitted coefficients0.3574468/0.1365405 versus generating0.35/0.14. Closure solve-gradient finite difference differs3.88144e-15; equilibrium defect8.21565e-15. Three native reference refinements63→127 have RMS9.32264e-6/1.11923e-5/8.02262e-6. They disclose finite reference error rather than declare continuum truth. Data-generation counts distinguish32 fit labels, eight development labels,32 final/shifted assessments and three extra refinement solves. No simulated industrial cost or speedup is reported.

### Failure audits — code_132

An analytic added oscillation0.2sin(16*pi*x) preserves displacement endpoints and has nearly zero scaled equation residual at fifteen interior j/16 sites, yet is wrong between them. Source scaled residual MSE1.18444e-26 contrasts dense residual1307.45137 and field0.0199501. This is an analytic counterexample, separate from trained comparisons. The second-derivative equation also leaves an affine ambiguity without endpoint information; displayed affine endpoint defects0.2/0.5 make the missing conditions explicit.

Actual321-parameter tanh fits at frequenciesone/eight each receive32 source locations and1,200 updates. Physics-only sees equations/endpoints; data-only instead observes exact source displacements/endpoints, so evidence budgets differ. No final tuning or winner selection occurs. At frequencyone, final field errors1.55878e-8 versus3.62027e-6. At frequencyeight, both fail near zero:0.498789 versus0.497569. Independent residual error stays near0.499 as well. Native solve_bvp references succeed, with473/4513 adaptive nodes and max analytic errors3.84177e-11/1.84011e-11. Spectral bias is discussed as a possible optimization tendency, not uniquely identified from this one failed recipe. Missing constraints, point coverage, scale, capacity and numerical reference are separate diagnostic questions.

## Sources and visual verification

Primary author/paper records and official SciPy APIs were read20October2026 with literature bounded by18October2026. They include Raissi/Perdikaris/Karniadakis original2017 two-part PINNs; Wang/Teng/Perdikaris gradient pathologies; Krishnapriyan etal failure modes; original neural ODE, HNN, LNN, neural CDE and SDE-gradient papers; and Rackauckas etal UDE framework. Live SciPy docs1.18.0 differ from executed1.17.1 and are explicitly distinguished. DeepXDE is a read landscape starting point, not an installed/executed dependency. Own small references do not claim full named-system implementations or reproduce paper benchmark gains.

All twelve inline and twelve vector figures have been inspected. Diagram repairs clarified127's forward/inverse arrows and128's loss collection; they reran fresh kernels and retained deterministic results. Book line series use grayscale and distinct styles. Figure generation reruns every current cell and asserts exact RESULTS equality with successful fresh-kernel summaries; no resource replay exception applies. Page layout, preservation and final companion tree/raw verification are recorded in the delivery review after compilation.

## Successful result dictionaries

### code_127

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2927.

```json
{
  "equal_ratio_max_difference": 0.0,
  "known_load": 3.0,
  "recovered_stiffness": 2.00276944524686,
  "sensitivity_rank": 1,
  "sensitivity_singular_values": [
    102.18396896153271,
    2.1168814513605073e-15
  ],
  "sensor_noise_sd": 0.00015,
  "sensor_positions": [
    0.2,
    0.5,
    0.8
  ],
  "solver_refinement": [
    {
      "final_nodes": 15,
      "initial_nodes": 8,
      "max_boundary_residual": 4.496003963831032e-22,
      "max_displacement_error": 1.0168289254694485e-07,
      "tolerance": 1e-05
    },
    {
      "final_nodes": 181,
      "initial_nodes": 16,
      "max_boundary_residual": 1.6772539622690948e-26,
      "max_displacement_error": 3.721092878272714e-12,
      "tolerance": 1e-08
    }
  ],
  "true_stiffness": 2.0
}
```

### code_128

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2928.

```json
{
  "comparisons": [
    {
      "boundary_loss": 0.0013079959647814038,
      "development_physics_score": 1.5342083632478019,
      "final_field_MSE": 7.079952083180492e-06,
      "final_residual_MSE": 1.5402122396837004,
      "max_endpoint_displacement": 0.010055870921343982,
      "model": "Data only",
      "parameters": 321,
      "source_data_MSE": 1.0354372617205227e-06,
      "source_residual_MSE": 1.5367555367758068
    },
    {
      "boundary_loss": 0.002253369773889315,
      "development_physics_score": 0.0024181760822685346,
      "final_field_MSE": 5.264272284195708e-05,
      "final_residual_MSE": 0.00018897398197830658,
      "max_endpoint_displacement": 0.023081315594603323,
      "model": "PINN bc0.1",
      "parameters": 321,
      "source_data_MSE": 3.0739400214540814e-05,
      "source_residual_MSE": 0.0001424381908396445
    },
    {
      "boundary_loss": 8.03271447510896e-08,
      "development_physics_score": 6.94643317692529e-05,
      "final_field_MSE": 1.076188376454719e-08,
      "final_residual_MSE": 8.648088169277626e-05,
      "max_endpoint_displacement": 0.00029315784703828895,
      "model": "PINN bc10",
      "parameters": 321,
      "source_data_MSE": 2.424988087736063e-06,
      "source_residual_MSE": 5.205683062233765e-05
    }
  ],
  "development_points": 63,
  "final_points": 401,
  "initial_unweighted_gradient_norms": {
    "Data only": [
      0.32958437778366934,
      0.266530642473542,
      0.4093015110701389
    ],
    "PINN bc0.1": [
      0.32958437778366934,
      0.266530642473542,
      0.4093015110701389
    ],
    "PINN bc10": [
      0.32958437778366934,
      0.266530642473542,
      0.4093015110701389
    ]
  },
  "learning_rate": 0.005,
  "selected_physics_candidate": "PINN bc10",
  "source_collocation": 32,
  "source_sensors": 6,
  "updates_per_candidate": 1200
}
```

### code_129

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2929.

```json
{
  "boundary_comparisons": [
    {
      "final_field_MSE": 1.3727039236951646e-07,
      "final_scaled_residual_MSE": 5.5992621323308926e-05,
      "max_endpoint_displacement": 2.2766975778856172e-05,
      "model": "Soft endpoint penalty",
      "trainable_parameters": 321
    },
    {
      "final_field_MSE": 6.1734954877277475e-09,
      "final_scaled_residual_MSE": 6.5556354391933775e-06,
      "max_endpoint_displacement": 0.0,
      "model": "Hard endpoint construction",
      "trainable_parameters": 321
    }
  ],
  "case_counts": [
    8,
    2,
    2
  ],
  "conductance_MSE": 0.0003584783326194274,
  "development_response_MSE": 9.49389811707473e-10,
  "edge_parameters": 13,
  "final_response_MSE": 2.831167492048755e-10,
  "max_global_flux_balance_error": 5.551115123125783e-16,
  "max_interior_equilibrium_error": 8.881784197001252e-15,
  "minimum_conductance": 0.7109369099888891,
  "source_response_MSE": 2.4737379936993086e-09
}
```

### code_130

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2930.

```json
{
  "comparisons": [
    {
      "development_derivative_MSE": 5.811806978362223e-06,
      "final_rollout_MSE": 4.4122916419599056e-05,
      "late_time_MSE": 6.212531863591613e-05,
      "model": "Unconstrained neural ODE",
      "parameters": 354,
      "source_derivative_MSE": 7.243995606376764e-06,
      "step_halving_RMS": 2.526381475816132e-07
    },
    {
      "development_derivative_MSE": 1.0090845582104403e-13,
      "final_rollout_MSE": 5.233078320985432e-13,
      "late_time_MSE": 6.666654485542623e-13,
      "model": "Dissipative mechanical field",
      "parameters": 2,
      "source_derivative_MSE": 2.2328691536917356e-13,
      "step_halving_RMS": 2.516244524078867e-07
    }
  ],
  "continuous_energy_identity_max_error": 2.0816681711721685e-17,
  "controlled_prefix_max_difference": 0.0,
  "discrete_gradient": {
    "absolute_difference": 4.70879585323658e-12,
    "autograd": 0.05138504230951378,
    "finite_difference": 0.05138504231422258
  },
  "final_time_range": [
    0,
    12
  ],
  "learned_damping": 0.25000119229678813,
  "learned_stiffness": 1.700000285298384,
  "neural_SDE": {
    "horizon": 2.0,
    "known_velocity_diffusion": 0.2,
    "learned_drift_covariance": [
      [
        0.02019261232912843,
        0.003132658348555201
      ],
      [
        0.003132658348555201,
        0.02438127964953417
      ]
    ],
    "learned_drift_mean": [
      -0.0017329213064611524,
      -0.005460746482286169
    ],
    "linear_truth_covariance": [
      [
        0.020813185951907853,
        0.001941447102553376
      ],
      [
        0.0019414471025533783,
        0.027087316552097493
      ]
    ],
    "paths": 512,
    "shared_Brownian_step_refinement_RMS": 0.0019331072054046211
  },
  "reference_refinement": [
    {
      "function_evaluations": 332,
      "max_state_error": 6.868693647188451e-08,
      "relative_tolerance": 1e-07
    },
    {
      "function_evaluations": 767,
      "max_state_error": 4.718270218972975e-11,
      "relative_tolerance": 1e-10
    }
  ],
  "source_development_final_initial_conditions": [
    20,
    5,
    5
  ],
  "source_time_range": [
    0,
    4
  ]
}
```

### code_131

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2931.

```json
{
  "case_counts": [
    32,
    8,
    16,
    16
  ],
  "closure_gradient_check": {
    "absolute_difference": 3.881443777498106e-15,
    "autograd": -0.001081243388793905,
    "finite_difference": -0.0010812433887900236
  },
  "coarse_interior_cells": 12,
  "comparisons": [
    {
      "changed_support_MSE": 1.3184459223268153e-05,
      "development_MSE": 1.2735702856030234e-05,
      "final_MSE": 1.3561000452297638e-05,
      "model": "Coarse solver",
      "source_MSE": 1.4167747638724017e-05
    },
    {
      "changed_support_MSE": 2.191876470997815e-05,
      "development_MSE": 2.1299866147397265e-08,
      "final_MSE": 2.924282303986949e-08,
      "model": "Data-only Ridge",
      "source_MSE": 2.2652271029950956e-09
    },
    {
      "changed_support_MSE": 6.071467733070152e-08,
      "development_MSE": 3.2820153806232338e-09,
      "final_MSE": 8.66815045914605e-09,
      "model": "Residual Ridge",
      "source_MSE": 5.855265887161824e-11
    },
    {
      "changed_support_MSE": 1.1245996618472486e-07,
      "development_MSE": 6.606444984779816e-08,
      "final_MSE": 8.110595901359957e-08,
      "model": "Learned mechanical closure",
      "source_MSE": 8.425598796155506e-08
    }
  ],
  "development_fine_solve_labels": 8,
  "final_and_shifted_assessment_fine_solves": 32,
  "fine_interior_cells": 63,
  "generating_closure_coefficients": [
    0.35,
    0.14
  ],
  "learned_closure_coefficients": [
    0.35744678851717,
    0.1365405082343037
  ],
  "max_coarse_equilibrium_error": 8.215650382226158e-15,
  "minimum_closure_conductance": 0.5337738007870533,
  "reference_refinement": [
    {
      "63_vs_127_grid_RMS": 9.322636310395326e-06,
      "case_index": 0
    },
    {
      "63_vs_127_grid_RMS": 1.1192327662749046e-05,
      "case_index": 40
    },
    {
      "63_vs_127_grid_RMS": 8.022624009489692e-06,
      "case_index": 56
    }
  ],
  "reference_refinement_extra_solves": 3,
  "ridge_candidates": [
    {
      "alpha": 0.001,
      "development_MSE": 2.1299866147397265e-08,
      "model": "Data-only Ridge"
    },
    {
      "alpha": 0.1,
      "development_MSE": 2.206761468029988e-07,
      "model": "Data-only Ridge"
    },
    {
      "alpha": 10.0,
      "development_MSE": 9.277393944122735e-06,
      "model": "Data-only Ridge"
    },
    {
      "alpha": 0.001,
      "development_MSE": 3.2820153806232338e-09,
      "model": "Residual Ridge"
    },
    {
      "alpha": 0.1,
      "development_MSE": 4.5635452981642846e-09,
      "model": "Residual Ridge"
    },
    {
      "alpha": 10.0,
      "development_MSE": 7.11362976611302e-09,
      "model": "Residual Ridge"
    }
  ],
  "source_fine_solve_labels": 32
}
```

### code_132

Versions: `{"matplotlib": "3.11.0", "numpy": "2.4.4", "pandas": "3.0.3", "python": "3.14.3", "scikit-learn": "1.9.0", "scipy": "1.17.1", "threadpoolctl": "3.7.0", "torch": "2.14.1"}`; Darwin arm64 CPU; seed 2932.

```json
{
  "collocation_witness": {
    "dense_field_MSE": 0.0199501246882793,
    "dense_scaled_residual_MSE": 1307.4513715710723,
    "max_boundary_defect": 0.0,
    "source_points": 15,
    "source_scaled_residual_MSE": 1.1844448033036694e-26
  },
  "comparisons": [
    {
      "development_residual_MSE": 2.340610229477588e-05,
      "final_field_MSE": 1.558777743912059e-08,
      "final_residual_MSE": 2.4737658641059085e-05,
      "frequency": 1,
      "max_boundary_defect": 6.274691423557854e-06,
      "model": "Physics only, m=1",
      "parameters": 321,
      "recipe": "Physics only",
      "source_residual_MSE": 1.4872286598627952e-05
    },
    {
      "development_residual_MSE": 0.0027640154351534292,
      "final_field_MSE": 3.6202663059367633e-06,
      "final_residual_MSE": 0.0027984929779036227,
      "frequency": 1,
      "max_boundary_defect": 8.820750555738055e-05,
      "model": "Data only, m=1",
      "parameters": 321,
      "recipe": "Data only",
      "source_residual_MSE": 0.0023446714973334995
    },
    {
      "development_residual_MSE": 0.49998980711826724,
      "final_field_MSE": 0.498788953232605,
      "final_residual_MSE": 0.49874302006764637,
      "frequency": 8,
      "max_boundary_defect": 1.041821207320437e-05,
      "model": "Physics only, m=8",
      "parameters": 321,
      "recipe": "Physics only",
      "source_residual_MSE": 0.5156150646898354
    },
    {
      "development_residual_MSE": 0.49999298126819003,
      "final_field_MSE": 0.4975689640600816,
      "final_residual_MSE": 0.4987461644291141,
      "frequency": 8,
      "max_boundary_defect": 0.007666581344835888,
      "model": "Data only, m=8",
      "parameters": 321,
      "recipe": "Data only",
      "source_residual_MSE": 0.5156181592233289
    }
  ],
  "development_points": 63,
  "final_points": 401,
  "learning_rate": 0.005,
  "missing_boundary_affine_endpoint_defects": [
    0.2,
    0.5
  ],
  "reference_solvers": [
    {
      "final_nodes": 473,
      "frequency": 1,
      "max_field_error": 3.841771345491907e-11,
      "max_relative_residual": 9.998324025661542e-09
    },
    {
      "final_nodes": 4513,
      "frequency": 8,
      "max_field_error": 1.840105845474227e-11,
      "max_relative_residual": 9.962492709752112e-09
    }
  ],
  "source_points_per_fit": 32,
  "updates_per_recipe": 1200
}
```


## Publication verification

At content verification, commit `22b1f5370151283a7f3a682133dd259d992ba761` matched remote main and all 215 file blobs with a clean working tree. Final metadata and all six notebooks are separately verified through commit-addressed raw files in local delivery evidence. Only companion artifacts are published.
