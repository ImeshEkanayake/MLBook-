# Chapter 25: Physics-informed and hybrid learning — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_25_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 25.1 · Forward, inverse and hybrid scientific tasks

- [Given mechanics, observed sensors, inferred parameters](notebooks/127_Chapter_25_01_forward_inverse_and_identifiability.ipynb#beam-task-contract)
- [A parameter estimate requires the declared observation model](notebooks/127_Chapter_25_01_forward_inverse_and_identifiability.ipynb#reference-and-inverse-audit)

Declared mechanisms: native beam boundary-value solver, sparse observation operator, known-load stiffness recovery, joint load-stiffness nonidentifiability, reference refinement and sensitivity rank.

```bash
python scripts/run_notebook.py notebooks/127_Chapter_25_01_forward_inverse_and_identifiability.ipynb
```

## 25.2 · Physics-informed neural network objectives

- [Every loss term has a separate origin and scale](notebooks/128_Chapter_25_02_pinn_objectives_and_derivatives.ipynb#beam-pinn-loss)
- [Differentiate the represented function, then check what it solves](notebooks/128_Chapter_25_02_pinn_objectives_and_derivatives.ipynb#off-grid-physics-check)

Declared mechanisms: actual fourth-order autograd beam residual, separate data equation and boundary terms, dimensionless residual scaling, fixed weight candidates and independent development grid, dense off-collocation validation.

```bash
python scripts/run_notebook.py notebooks/128_Chapter_25_02_pinn_objectives_and_derivatives.ipynb
```

## 25.3 · Constraints, conservation and architecture

- [Exact endpoint values are a narrower claim than an exact solution](notebooks/129_Chapter_25_03_hard_constraints_and_conservation.ipynb#constraint-contracts)
- [Cancellation follows from shared edge fluxes](notebooks/129_Chapter_25_03_hard_constraints_and_conservation.ipynb#conservation-versus-accuracy)

Declared mechanisms: actual soft versus hard displacement boundary fits, independent differential residual checks, learned positive edge conductances, differentiable conservative finite-volume solve, boundary flux and interior balance identities.

```bash
python scripts/run_notebook.py notebooks/129_Chapter_25_03_hard_constraints_and_conservation.ipynb
```

## 25.4 · Neural differential equations and structured dynamics

- [Learned continuous laws still require a numerical solver](notebooks/130_Chapter_25_04_neural_dynamics_and_solver_contracts.ipynb#learned-dynamics-contract)
- [Numerical paths are part of the model contract](notebooks/130_Chapter_25_04_neural_dynamics_and_solver_contracts.ipynb#control-noise-and-gradient)

Declared mechanisms: actual learned neural ODE vector field, positive mechanical stiffness and damping, differentiable RK4 and finite-difference gradient, controlled input-path integration, neural drift SDE with shared Brownian refinement.

```bash
python scripts/run_notebook.py notebooks/130_Chapter_25_04_neural_dynamics_and_solver_contracts.ipynb
```

## 25.5 · Mechanistic hybrids and multifidelity learning

- [Mechanics and learned corrections have distinct responsibilities](notebooks/131_Chapter_25_05_hybrid_and_multifidelity_learning.ipynb#multifidelity-contract)
- [A corrected response and a corrected operator enforce different things](notebooks/131_Chapter_25_05_hybrid_and_multifidelity_learning.ipynb#hybrid-limits)

Declared mechanisms: native coarse and fine mechanical solves, actual residual-correction Ridge, data-only comparison with matched case selection, differentiable positive-conductance closure, whole-case and changed-support assessment.

```bash
python scripts/run_notebook.py notebooks/131_Chapter_25_05_hybrid_and_multifidelity_learning.ipynb
```

## 25.6 · PINN failures, validation and model choice

- [Small source residual can leave the solution wrong](notebooks/132_Chapter_25_06_pinn_failure_and_validation_audits.ipynb#failure-audit-contract)
- [Retain a failed fit and diagnose its claim](notebooks/132_Chapter_25_06_pinn_failure_and_validation_audits.ipynb#frequency-and-reference)

Declared mechanisms: actual low and high frequency PINN fits, matched-budget data-only references, off-collocation adversarial witness, missing-boundary nonuniqueness, native refined numerical reference.

```bash
python scripts/run_notebook.py notebooks/132_Chapter_25_06_pinn_failure_and_validation_audits.ipynb
```

## Interpretation and boundaries

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
