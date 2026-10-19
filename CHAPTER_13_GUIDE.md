# Chapter 13: Preparing graphs, sequences, and physical systems — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_13_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 13.1 · Graph construction and relational meaning

- [An edge is a claim about a relationship](notebooks/062_Chapter_13_01_Typed_Graphs_And_Construction_Boundaries.ipynb#relations)
- [Fit a similarity graph only on admitted history](notebooks/062_Chapter_13_01_Typed_Graphs_And_Construction_Boundaries.ipynb#similarity)

Declared mechanisms: physical member and sensor node types, directed typed relations and self-loops, training-only correlation graph, stable identifiers and permutation equivariance.

```bash
python scripts/run_notebook.py notebooks/062_Chapter_13_01_Typed_Graphs_And_Construction_Boundaries.ipynb
```

## 13.2 · Sequence windows and irregular observations

- [Context and forecast intervals have different roles](notebooks/063_Chapter_13_02_Irregular_Windows_And_Overlap.ipynb#windows)
- [Resampling cannot interpolate from an unavailable future endpoint](notebooks/063_Chapter_13_02_Irregular_Windows_And_Overlap.ipynb#resampling)

Declared mechanisms: context forecast stride and raw-record overlap, event and arrival aligned windows, bounded forward hold and masks, future-invariant construction and label maturity.

```bash
python scripts/run_notebook.py notebooks/063_Chapter_13_02_Irregular_Windows_And_Overlap.ipynb
```

## 13.3 · Spatial coordinates, geometry and meshes

- [Array rows do not define geometry](notebooks/064_Chapter_13_03_Mesh_Fields_And_Boundary_Tags.ipynb#mesh)
- [Transform the coordinate frame and vector quantities consistently](notebooks/064_Chapter_13_03_Mesh_Fields_And_Boundary_Tags.ipynb#frames)

Declared mechanisms: points cells edges and material fields, boundary tags and scalar vector units, consistent mesh renumbering, coordinate frames and field transformations.

```bash
python scripts/run_notebook.py notebooks/064_Chapter_13_03_Mesh_Fields_And_Boundary_Tags.ipynb
```

## 13.4 · Physical constraints and conditions

- [Specify the physical task before choosing a learner](notebooks/065_Chapter_13_04_Forward_Conditions_And_Inverse_Ambiguity.ipynb#forward)
- [A complete forward task need not identify an inverse task](notebooks/065_Chapter_13_04_Forward_Conditions_And_Inverse_Ambiguity.ipynb#inverse)

Declared mechanisms: constitutive assumptions and conservation balance, supports boundary loads and initial-state schema, forward input completeness, inverse load-stiffness non-identifiability.

```bash
python scripts/run_notebook.py notebooks/065_Chapter_13_04_Forward_Conditions_And_Inverse_Ambiguity.ipynb
```

## 13.5 · Batching and structure-preserving transformations

- [Concatenation must preserve entity boundaries](notebooks/066_Chapter_13_05_Disconnected_Batches_And_Equivariance.ipynb#batch)
- [Padding and graph membership are part of the input](notebooks/066_Chapter_13_05_Disconnected_Batches_And_Equivariance.ipynb#masks)
- [Rotate physical quantities together](notebooks/066_Chapter_13_05_Disconnected_Batches_And_Equivariance.ipynb#rotation)

Declared mechanisms: disconnected graph batching and offsets, mask-safe sequence aggregation, neighbor-sampling variability, covariant geometry loads stiffness and targets.

```bash
python scripts/run_notebook.py notebooks/066_Chapter_13_05_Disconnected_Batches_And_Equivariance.ipynb
```

## Interpretation and boundaries

All five laboratories are self-contained generated construction audits and execute successfully in fresh kernels. No advanced graph/sequence/scientific architecture is trained, and no benchmark or field validation is claimed. Ordinary execution requires no network, credentials, GPU or additional dependency. A static builder check caught derivative apostrophes prematurely closing a source string; derivative notation and an inadvertently rewritten dictionary key were corrected before kernel execution. There were no failed reference kernel runs. Diagram review prompted successful reruns of code_062/064/065/066 for a physical-to-typed-graph panel, relation legends, unobstructed mesh IDs, shorter field labels, explicit dynamic initial-state text and integer mask indices. Current sources retain the same result dictionaries.

The typed graph has four members/four sensors, four undirected mechanical connections (eight directed entries) and four sensor-to-member measurement links. A[target,source] is explicit; equal weights and empty-neighborhood placeholders are declared choices. The top member carries [0,-10] kN. Row normalization/self-loops differ; consistent node reordering preserves both relation-specific aggregations. Eighty admitted sensor observations give two .8-threshold absolute-correlation edges; invalid use of all 120 observations with a later shared component yields six. Future-input perturbation leaves the training-only graph unchanged. These associations are neither physical connectivity nor causal identification, and no learned graph is fitted.

Irregular sequence context (c-5,c] and future-record-mean target (c,c+2] use stride one and a c+3 label-resolution rule. Seventeen training cutoffs 8–24 and nineteen final cutoffs 32–50 have disjoint raw context/target IDs; alternating-window splitting shares forty-four IDs. Four training and three final windows remain unresolved under the reporting rule. At cutoff 15, grid times [11,12,13,14,15] have validity [true,false,true,false,false], with only two bounded-hold measurements available. A true observed zero remains valid; placeholders require masks. The conservative replay checks arrival at each grid time and maximum observation age 1.5 s; future-value perturbation leaves its inputs unchanged. This is a construction audit of a recorded-mean target, not an unobserved continuous-process estimate or independence guarantee.

The six-node/four-triangle mesh has nine unique edges, positive CCW areas totaling 2 m², stable noncontiguous IDs, nodal temperature and separate cell conductivities. Left boundary IDs [101,401] and right [310,612] retain their meanings through reindexing. Consistent coordinate/connectivity/field/tag permutation preserves areas and the exact linear-field temperature integral 652 K m²; a coordinates-only permutation fails. A 30-degree rotation and origin translation preserve edge lengths/areas/scalars while rotating gradient [25,2] to [20.650635095,14.232050808] K/m. Tag 0 means neither named side, not a claim that every such node is physically interior. No mesh file parser, Gmsh execution or finite-element solution is asserted.

The static cantilever contract declares L=3 m, EI=8 MN m², q=5 kN/m, a homogeneous small-deflection linear Euler–Bernoulli law, clamped displacement/slope and free-end zero curvature/third derivative. Analytic boundary/balance/tip checks pass and tip displacement is 6.328125 mm. A separate dynamic schema states initial rest and additional mass/forcing/time inputs, without computing a transient. Doubling q and EI leaves the full field identical, exposing inverse ratio ambiguity. With q known independently, twenty .02-mm-noise repeated tip measurements give mean EI 7.997917125 MN m², sample SD .022526972, range 7.947596971–8.032825961. This is repeated-reading sensitivity, not a posterior interval or inclusion of support/model uncertainty. MIT's primary formula-sheet text was retrieved and inspected; the complete reference and derivatives are checked independently in code.

The batching audit combines a three-node chain and a two-node graph into a five-node disconnected union with correct offsets and membership. Joint aggregation equals separate calls; pooled means are [2,15]. Two masked sequence means [1.5,5] survive replacing padding with 1e9 while preserving a real zero. Uniform pairs of [0,0,0,100] yield means [0,0,50,0,50,50], whose average is the full mean 25; a single sampled neighborhood varies, and no nonlinear-network unbiasedness claim follows. Rotating anisotropic stiffness, force, geometry and displacement consistently gives original u=[.714285714,-.857142857] mm and rotated [1.099450346,.190018146], preserving norm 1.115749954 mm and work. Leaving anisotropic stiffness unchanged fails covariance. Diagram arrow drawing scales are stated explicitly. Mesh coarsening and normalization/nondimensionalization are explained as contracts, not claimed as implemented solvers.

Nine original vector figures implement both agreed visual briefs: the physical-frame conversion to typed relations with loads/directions, and context/forecast windows paired with a supported physical domain and declared initial-state distinction. Five equations state relation aggregation, coordinate transformation, cantilever conditions/reference, and mechanical covariance. Primary/official Gmsh, PyTorch Geometric and MIT sources support concepts only where inspected; the NumPy audit mechanisms are independent and no unavailable dependency is hidden in the examples.

Book-page inspection caught an oversized tightly cropped vertical graph figure. Its export now retains the full declared canvas so print scaling preserves the intended height; node/legend positions were repaired and the current code_062 source reran successfully with unchanged results. The preview integrity checker now rejects the oversized-float warning as well as overflow/reference errors. The other completed cumulative builds were checked for this warning and contain none.
