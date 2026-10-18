# Chapter 1: concept-to-code traceability

These five independent notebooks accompany the first manuscript chapter. Their permanent IDs live in [CODE_EXAMPLES.md](CODE_EXAMPLES.md); chapter/file names can change without reassigning the IDs. Each notebook contains its own imports, generated data, definitions, interpretive text, controls and exercises. The model-specific decision-tree lab [code_001](CODE_EXAMPLES.md#code_001) remains unchanged.

| Manuscript concepts | Code and precise notebook section | Executable evidence or exercise |
| --- | --- | --- |
| Stakeholder output, population, observation/action unit and consequences | [code_002: task contract](notebooks/002_Chapter_01_01_Task_Framing.ipynb#task-contract) | A required-field task-specification dictionary with meaningful units, target, horizon, use and capacity. Semantic usefulness remains a human judgement. |
| Event time, availability time and future information | [code_002: availability](notebooks/002_Chapter_01_01_Task_Framing.ipynb#availability) | Deliberately invalid event-only filter versus the two-clock mask; a plotted cutoff and assertions. |
| Horizon endpoints, follow-up, repeated entities and negative labels | [code_002: labels and units](notebooks/002_Chapter_01_01_Task_Framing.ipynb#labels-units) | Open-left/closed-right event labels at 3/7 days; boundary and identity checks; incomplete-follow-up example and worksheet. |
| Regression/classification targets, baseline, APIs and probability limitations | [code_003: prediction](notebooks/003_Chapter_01_02_Prediction_And_Discovery.ipynb#prediction) | Fixed linear/prior/logistic models; disjoint training, validation and sealed final sets; numeric and probability metrics. |
| Ranking, precision/recall at capacity and decision limits | [code_003: ranking](notebooks/003_Chapter_01_02_Prediction_And_Discovery.ipynb#ranking) | Fixed top-20 probability ordering on the sealed cohort; separate denominators and interpretation prompts. |
| Clustering objectives, arbitrary IDs, scale sensitivity and descriptive limits | [code_003: discovery](notebooks/003_Chapter_01_02_Prediction_And_Discovery.ipynb#discovery) | Two/three-centroid comparison without fitting known regime labels; channel-scale experiment; cluster-permutation and causal-reasoning exercises. |
| Anomaly reference, rarity versus faults and evaluation scope | [code_003: discovery](notebooks/003_Chapter_01_02_Prediction_And_Discovery.ipynb#discovery) | Reference-only isolation fit with new normal/injected cases; score diagnostic and harder-reference exercise. |
| Generative scenarios, marginal versus joint validity and support | [code_004: generation](notebooks/004_Chapter_01_03_Generation_Simulation_And_Inversion.ipynb#generation) | Paired versus independent-column resampling; dependence and support checks, range-extension exercise. |
| Signed spring law, units, simulator and surrogate | [code_004: forward](notebooks/004_Chapter_01_03_Generation_Simulation_And_Inversion.ipynb#forward) | Declared static SI model; exact unit/value checks; noisy calibration with a zero-intercept compliance fit and held-out loads. |
| Inverse ambiguity, noise, assumptions and added information | [code_004: inverse](notebooks/004_Chapter_01_03_Generation_Simulation_And_Inversion.ipynb#inverse) | Different stiffness pairs with identical endpoint curves and different internal measurements; regularization and additional-sensor exercises. |
| Probability versus action, expected utility, capacity and causal prevention | [code_005: static decisions](notebooks/005_Chapter_01_04_Decisions_And_Sequential_Interaction.ipynb#static-decision) | Risk-only versus assumed-benefit choices; cost calculations; prevention-sensitivity and selective-observation worksheets. |
| State, action, transition, policy, boundary fairness and planning | [code_005: sequential system](notebooks/005_Chapter_01_04_Decisions_And_Sequential_Interaction.ipynb#sequential) | Complete battery rollouts, feasibility checks and equal initial/terminal state; idle/myopic/planned policies. Efficiency and uncertain-future exercises mark model limits. |
| Tables, relational keys, join cardinality and distinct data units | [code_006: linked tables](notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb#linked-tables) | Four members/eight sensors/48 readings with valid key/cardinality checks. |
| Graph adjacency, physical edges, spatial coordinates and row order | [code_006: graph](notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb#graph) | Coordinate plot, adjacency, neighbour aggregation and consistent permutation assertion; explicitly not a GNN or equilibrium solution. |
| Temporal information loss, task/architecture/objective/adaptation axes | [code_006: time and resources](notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb#time-and-resources) | Same summaries/opposite sequence order; reading-map dataframe and representation exercises. |
| Preprocessing versus pretraining, frozen context versus fine-tuning | [code_006: time and resources](notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb#time-and-resources) | Validated operation-role worksheet. No pretend foundation-model training is necessary to teach this conceptual distinction. |
| Baseline-first choices, budget and domain-validity boundaries | [code_006: worksheet and exercises](notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb#time-and-resources) | Starting-method map, actual tiny-array storage diagnostic and bounded first-project specification. Future family names are roadmap items rather than algorithms claimed implemented here. |

## Scope of controls and next experiments

Task horizon, information availability and observation unit are task/data controls. Scenario distributions, simulated noise and domain ranges are data-generating assumptions. Cluster count and estimator settings are model controls. Inspection capacity, costs, prevention assumptions and battery limits are decision/system controls. Each notebook identifies which kind is being changed. They are not collectively called hyperparameters.

These opening examples explain task mechanisms. They do not claim to exhaust the constructors of linear regression, logistic regression, clustering or isolation models. Their later model chapters provide that depth; code_001 already demonstrates the full model-lab pattern for a tree. Exercises distinguish exploratory changes from a fresh final assessment. Generation and physical demonstrations are checked against stated toy rules, not represented as field evidence. Causal claims and physical validity cannot be established by a successful assertion alone.

## Run and inspect

From the activated pinned environment, for example:

```bash
python scripts/run_notebook.py notebooks/002_Chapter_01_01_Task_Framing.ipynb
python scripts/run_notebook.py notebooks/003_Chapter_01_02_Prediction_And_Discovery.ipynb
python scripts/run_notebook.py notebooks/004_Chapter_01_03_Generation_Simulation_And_Inversion.ipynb
python scripts/run_notebook.py notebooks/005_Chapter_01_04_Decisions_And_Sequential_Interaction.ipynb
python scripts/run_notebook.py notebooks/006_Chapter_01_05_Representations_And_Reading_Map.ipynb
```

The runner writes independent executed copies to ignored `build/` by default, preserving the committed reference. The [execution report](CHAPTER_01_EXECUTION.md) records actual runtime, versions, figures and checks. Read the notebook's prompts before observing output, then explain what changed and what the result cannot establish.
