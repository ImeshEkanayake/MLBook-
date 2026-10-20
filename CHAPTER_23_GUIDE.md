# Chapter 23: Graph neural networks and relational learning — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_23_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 23.1 · Graph tasks and relational baselines

- [One topology, distinct targets](notebooks/115_Chapter_23_01_prediction_units_and_relational_baselines.ipynb#graph-task-contract)
- [Aggregation already supplies relational information](notebooks/115_Chapter_23_01_prediction_units_and_relational_baselines.ipynb#prediction-unit-limits)

Declared mechanisms: node versus existing-edge targets, non-neural aggregated baseline, actual shared graph encoder and task heads, whole-building holdout, whole-graph mean readout.

```bash
python scripts/run_notebook.py notebooks/115_Chapter_23_01_prediction_units_and_relational_baselines.ipynb
```

## 23.2 · Message passing and graph convolutions

- [A message has a source, destination and edge meaning](notebooks/116_Chapter_23_02_messages_aggregation_and_graph_convolutions.ipynb#message-contract)
- [Sharing, aggregation and readout make different promises](notebooks/116_Chapter_23_02_messages_aggregation_and_graph_convolutions.ipynb#operator-limits)

Declared mechanisms: edge-feature message trace, GCN SAGE and GIN-style learned operators, two-hop derivative support, permutation and pooling identities, disconnected mini-batch contract.

```bash
python scripts/run_notebook.py notebooks/116_Chapter_23_02_messages_aggregation_and_graph_convolutions.ipynb
```

## 23.3 · Graph attention and graph transformers

- [Can the query receive the required load?](notebooks/117_Chapter_23_03_local_attention_and_distant_information.ipynb#graph-attention-contract)
- [Access, mixing and compression are distinct](notebooks/117_Chapter_23_03_local_attention_and_distant_information.ipynb#graph-bottleneck-limits)

Declared mechanisms: actual masked graph attention, global graph attention with distance bias, distant-source derivative audit, permutation of structural encodings, oversmoothing and bottleneck fixtures.

```bash
python scripts/run_notebook.py notebooks/117_Chapter_23_03_local_attention_and_distant_information.ipynb
```

## 23.4 · Heterogeneous, temporal and knowledge graphs

- [Relation meaning and availability precede aggregation](notebooks/118_Chapter_23_04_typed_relations_and_time_bounded_links.ipynb#typed-history-contract)
- [Current absence is a time-indexed claim](notebooks/118_Chapter_23_04_typed_relations_and_time_bounded_links.ipynb#typed-negative-limits)

Declared mechanisms: actual relation-specific graph update, node and edge availability clocks, historical-only typed snapshot, trained typed link decoder, future-positive negative audit.

```bash
python scripts/run_notebook.py notebooks/118_Chapter_23_04_typed_relations_and_time_bounded_links.ipynb
```

## 23.5 · Geometric and physical graph learning

- [Rotate the loads and geometry under the same convention](notebooks/119_Chapter_23_05_coordinate_transformations_and_graph_solver.ipynb#geometric-physics-contract)
- [Equivariance is a transformation identity, not an accuracy certificate](notebooks/119_Chapter_23_05_coordinate_transformations_and_graph_solver.ipynb#geometric-limits)

Declared mechanisms: actual vector-valued graph propagation, learned relaxation with a known physical operator, fixed numerical and coordinate-MLP baselines, joint rotation reflection translation audits, ground-reaction equilibrium.

```bash
python scripts/run_notebook.py notebooks/119_Chapter_23_05_coordinate_transformations_and_graph_solver.ipynb
```

## 23.6 · Scaling, failure analysis and graph explanations

- [Fixed fanout can miss a consequential connection](notebooks/120_Chapter_23_06_graph_size_sampling_and_explanation_checks.ipynb#graph-scaling-contract)
- [Graph dependence affects sampling and explanations](notebooks/120_Chapter_23_06_graph_size_sampling_and_explanation_checks.ipynb#graph-failure-limits)

Declared mechanisms: actual graph-size holdout, mean versus sum aggregation transfer, uniform neighbor sampling with known degree correction, heterophily counterexample, edge-attribution fidelity and stability.

```bash
python scripts/run_notebook.py notebooks/120_Chapter_23_06_graph_size_sampling_and_explanation_checks.ipynb
```

## Interpretation and boundaries

# Chapter 23 mechanisms, evidence and boundaries

Six original self-contained CPU Torch laboratories implement actual graph calculations. No dependency was added. They do not claim execution of PyTorch Geometric, full GraphGPS/EGNN systems, complete paper benchmarks or field-valid engineering models. Core pins remain Python 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0, scikit-learn 1.9.0, threadpoolctl 3.7.0 and Torch 2.14.1. Explicit CPU thread count one, float64, deterministic Torch algorithms and seeds 2515–2520. Ordinary runs require no files, downloads, credentials, GPU or private modules.

## Actual mechanisms and results

- **115 — prediction units:** sixty graphs, 10–16 members each, ring plus random chords; 40/10/10 whole buildings. Observed loads/material/capacity and known topology precede separate Bernoulli node-damage/existing-edge-failure targets. Training-only feature scaling. Own logistic versus relational-aggregate logistic, endpoint-symmetric edge logistic, and actual two-layer mean-aggregation encoder with node/symmetric edge heads. Shared neural fit has unit-weighted node/edge BCE, two rates × 250 updates, own joint-development checkpoint; selected rate 0.01/update 50, 722 parameters. Final node Brier own 0.214864132, relational 0.162630380, GNN 0.151053770. Final edge Brier endpoint logistic 0.168729007, GNN 0.185988129. Final 124 nodes/194 connections in ten independent buildings. Graph readout is mean marginal node probability, not a separately fitted graph classifier or a damage-count interval: fraction MSE own 0.048037003, relational 0.023010149, GNN 0.020210577. Known topology/features within final buildings are admitted, labels never enter messages; inductive whole-graph assessment, not a transductive node split. Neither existing-edge failure model predicts absent-link existence.
- **116 — message/operator contracts:** manual five-member chain, explicit stiffness/length edge factors, transformed messages and own-state ReLU update. Edge M1→M0 message [0.344, 0.232], first M0 state [0.564, 0.572], second [0.5914400000000001, 0.59752]. Dense versus indexed accumulation, node permutation equivariance, mean/sum pooling invariance and disconnected block batching pass. Two-layer M0 derivative at M3/M4 is exactly zero, while the reachable M2 derivative is nonzero. Separate sixty twelve-node graphs, 40/10/10, target generated from own/neighbor-mean/two-hop components plus noise 0.03; training-only scale. Actual GCN self-loop symmetric normalization, mean-SAGE separate own/neighbor maps, and GIN-style sum/learned epsilon/MLP. Two rates × 300 updates each, own development selection. Final MSE GCN 0.060759427, SAGE 0.002513548, GIN-style 0.058828733, parameters 353/657/899. Mechanism favors own/mean structure; no universal ranking. Multiset mean collision {1,3}/{2}, scalar-sum collision {1,3}/{0,4}, nonlinear summed squares distinguish latter. Finite learned references do not claim theorem-level injectivity.
- **117 — local/global graph attention:** 260 independent sixteen-node chains, 120/40/100 split. Admitted random loads plus root/terminal markers; root target equals terminal load fifteen hops away. Own two-layer local GAT-style attention (145 parameters) versus own global two-head width-eight graph transformer with shortest-path biases (673), two rates × 400 updates/own development checkpoint. Final root MSE 0.734211620 versus 2.252851e-5. Known marker selector is exact zero by constructed rule and remains visible. Same-weights root derivative outside two local hops zero; global derivative to terminal load 0.985839431. Joint feature/adjacency/distance permutation max errors 0 and 4.44e-16. Attention weights are not physical/causal explanations, and nonedge attention does not create physical adjacency. Separate fixed mean-diffusion fixture measures representation variance across depths, with original-feature reinjection; not a fitted-network comparison. Binary mean-aggregation tree verifies leaf derivatives 2^-depth for depths 1–8 as an explicit compression example, not a universal trained-GNN theorem.
- **118 — typed/time/link:** sixty buildings, each with four members/four sensors/three inspections, 40/10/10 split. Separate typed encoders and building→member, sensor→member, inspection→member and member-connectivity transformations, one actual heterogeneous update and member head; each type's scaler fits training buildings only. Day-ten sensor event/receipt clocks [4,7,9,8]/[4,7,11,9] exclude S2 despite its pre-cutoff event. Inspection creation [1,6,9], assignment [3,8,12], report receipt [5,9,13]; future creation-known entity retains known priority but no future edge/report. Historical assignment edges total 120. Changing unavailable readings leaves admitted values exactly unchanged. Future damage-report surrogate Brier zero is explicitly forbidden, never an admitted candidate. Typed aggregate logistic final Brier 0.189573088 beats relation-specific graph 0.216906630; graph 457 parameters, two rates × 300 update limits, selected 0.005/update 50. Separate inductive ten-parameter typed distance link decoder uses known member load/inspection priority, no identity embeddings; fixed rate 0.02/500 limits and historical-development checkpoint update 300. Enumerated same-building eligible pairs; future candidate set excludes historical positives. Forty historical training nonedges become positive later and are deliberately not removed using future knowledge. An inspection can add a second target member later. Final day10→12 candidates 70 with 20 additions on ten unseen buildings; Brier 0.167455384, AP 0.567720413, MRR 0.916666667. Complete synthetic candidate universe is explicit; real unobserved/censored nonedges require different observation assumptions. Decoder is a scoped relation model, not exhaustive knowledge-graph coverage.
- **119 — geometric/physical graph:** sixty eight-node ring/chord graphs, 40/10/10 split. Positive distance-dependent scalar stiffness, isotropic ground tethers; known dimensionless A=L_k+diag(g), exact U=solve(A,F) targets. This is an ideal isotropic vector network, not bar-direction mechanics, frame bending or structural assessment. Compare a 242-parameter coordinate MLP on seven local features; eight fixed Jacobi steps/eta=1/zero parameters; and eight graph residual steps with learned sigmoid eta/eight parameters. Learned graph explicitly receives the known physical operator, a strong prior absent from the MLP's local features; it is unrolling, not full EGNN execution or a data-only fair-capacity contest. Learned families two rates × 300 updates/own development checkpoint, MLP selected0.005/update240, learned steps0.1/update300; eight independent coefficients remain equal under symmetric initialization at 0.987092391. Final vector MSE MLP 0.090978829, fixed 0.004630261, learned 0.004928872. Residual MSE 0.218250967/0.001308652/0.001291034, so response and force-residual rankings differ slightly. Fixed method's better displacement result retained. Joint rotation0.7rad, reflection and position-translation audits pass for graph methods to rounding: rotation RMS fixed1.5588e-16/learned1.6763e-16 versus MLP0.117997553; reflection0/0 versus0.150239325; translation1.15e-16/1.44e-16 versus0.158647177. Exact equilibrium max error8.88e-16, ground-reaction balance2.66e-15; internal forces sum zero. Ground tethers are isotropic scalar supports, not untransformed fixed-axis restraints. The three-panel typed/time/geometric figure uses declared small semantic/time fixtures plus actual final rotated graph, not a secretly combined trained system.
- **120 — size/sampling/explanation:** eighty star-plus-leaf-ring graphs; forty train/ten dev/ten final at8–12 nodes, twenty additional final at24–40. One observed hub connection weight20 carries load near±2; other weights1. Response .4own+.6weighted-neighbor-mean+noise.02. Own actual weighted indexed aggregate, verified against dense reference; all disconnected edges stay within their building. Mean/sum graph networks use training-only aggregate centers/scales, two rates ×300updates/development selection; relational Ridge1e-6 baseline on own/mean. Final all-node MSE source Ridge0.000315433/mean0.000406300/sum0.024632003; large0.000391314/0.000452390/0.021338846. Hub MSE source0.000245458/0.000523411/0.006503516, large0.000804150/0.001145446/0.214793569. Keeping hub loss exposes sum size failure hidden by ordinary leaf count. Disconnected-batch separate/joined max error1.11e-16. Uniform sampling without replacement atfanouts1/2/4 uses known full weighted degree and degree/fanout correction; an exact single-neighbor expectation check passes. Linear conditional unbiasedness does not transfer through the nonlinear prediction. Frozen mean model, 100repeats per graph/every hub query retained. Source sampled MSE2.991508/1.538728/0.659295; larger5.043918/2.091489/1.005175. Observed important-edge miss fractions source0.890/0.769/0.532, larger0.967/0.9405/0.8785; analytic averages also recorded, finite empirical aggregate deviations retained. Repeats are not new independent buildings, and no measured inference-speed claim is made. Separate four-node opposite-sign fixture: own-sign Brier0/accuracy1; neighbor smoothingBrier1/accuracy0; signed contrastBrier0.0142093/accuracy1. One frozen final larger graph explanation differentiates shared physical edge weights with normalization recomputed, then removes incident connections explicitly. Top-gradient critical-edge removal changes prediction0.461690375 versus uniform incident mean0.020990854; gradient-times-weight estimate0.420683837. Top-two set Jaccard1 across20input-noise perturbationsSD.02. This observed stability and finite-change sensitivity are computational checks, not causal physical-intervention evidence.

## Execution, figures and repairs

All six initial fresh kernels passed without error or stderr warnings. Source/plot review then added the actually used member-connectivity edges to 118's typed diagram and expanded 119's coordinate limits to include complete load arrows. Both current notebook sources reran in fresh kernels and preserved exact deterministic RESULTS. The book-sized 117 plot uses more legible context ticks and shorter equivalent global-attention labeling. All twelve initial notebook images and twelve vector figures were visually inspected; repaired images are rechecked during the composed-page review. Figure generation reruns every current code cell and asserts exact equality with the fresh-kernel summary; no resource replay exception is needed in this chapter. Current notebooks contain 24 executed code cells and twelve inline images. Original plots are SVG/vector-PDF/PNG sets.

Primary papers and versioned official operator/type documentation were accessed20October2026. Version2.5.0 PyG documentation is a conceptual snapshot, not an installed or newest-version claim. All numerical evidence is generated teaching data with explicit task and knowledge boundaries; literature completeness, universal rankings and field validity are not asserted.
