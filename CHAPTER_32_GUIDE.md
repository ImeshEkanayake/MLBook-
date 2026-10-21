# Chapter 32: Reinforcement learning and control — concept-to-code guide

Permanent IDs map to the numbered sections below. Restart and run all cells; imports/helpers and generated inputs are internal. Ordinary execution needs no files, network, credentials or GPU. Use the [quickstart](README.md), [pinned environment](requirements-lock.txt), [registry](CODE_EXAMPLES.md) and [actual execution evidence](CHAPTER_32_EXECUTION.md). The notebook orientations disclose task/fitting controls and role boundaries; these scoped laboratories do not claim exhaustive estimator API coverage or field validity.

## 32.1 · Bandits, states, actions and rewards

- [Learn from the inspection actually purchased](notebooks/167_Chapter_32_01_bandits_states_actions_and_rewards.ipynb#contextual-inspection)
- [A battery changes tomorrow's feasible decision](notebooks/167_Chapter_32_01_bandits_states_actions_and_rewards.ipynb#sequential-feedback-and-aliasing)

Declared mechanisms: actual contextual linear upper-confidence acquisition with chosen-action feedback, independent fixed-policy evaluation against contextual expected-reward oracle, exact two-step battery dynamic program versus myopic reward, aliased observations under partial observability, agent environment feedback with policy and model distinguished.

```bash
python scripts/run_notebook.py notebooks/167_Chapter_32_01_bandits_states_actions_and_rewards.ipynb
```

## 32.2 · Value functions and temporal-difference learning

- [Solve a declared three-state process first](notebooks/168_Chapter_32_02_bellman_td_q_learning_and_function_approximation.ipynb#exact-and-sampled-values)
- [A tiny approximation can amplify an unsupported value](notebooks/168_Chapter_32_02_bellman_td_q_learning_and_function_approximation.ipynb#unsupported-bootstrap-instability)

Declared mechanisms: exact continuing maintenance MDP Bellman solution, actual tabular Q-learning from exploratory trajectories, actual target-network neural fitted Q iteration from off-policy samples, Bellman residual and greedy policy checked against known model, explicit unsupported-feature bootstrapping instability.

```bash
python scripts/run_notebook.py notebooks/168_Chapter_32_02_bellman_td_q_learning_and_function_approximation.ipynb
```

## 32.3 · Policy gradients and actor–critic methods

- [Train a discrete maintenance actor from fresh trajectories](notebooks/169_Chapter_32_03_ppo_and_soft_actor_critic_mechanisms.ipynb#ppo-maintenance-policy)
- [Train a continuous stochastic actor with a real replay buffer](notebooks/169_Chapter_32_03_ppo_and_soft_actor_critic_mechanisms.ipynb#sac-continuous-actuator)

Declared mechanisms: actual stochastic on-policy PPO with frozen behavior probabilities and clipped surrogate, finite-horizon observed clock and Monte Carlo advantage critic, actual continuous tanh-Gaussian SAC with corrected log density twin critics replay and target updates, separate independent simulator evaluation and simple controls, training budgets and distinct-task interpretation limits.

```bash
python scripts/run_notebook.py notebooks/169_Chapter_32_03_ppo_and_soft_actor_critic_mechanisms.ipynb
```

## 32.4 · Model-based learning, planning and MPC

- [Separate a learned disturbance model from known storage equations](notebooks/170_Chapter_32_04_learned_dynamics_planning_and_mpc.ipynb#learned-demand-and-shooting-plans)
- [Inspect a planned sequence before executing its first action](notebooks/170_Chapter_32_04_learned_dynamics_planning_and_mpc.ipynb#receding-horizon-and-model-assumptions)

Declared mechanisms: source-only fitted autoregressive demand residual model, known battery dynamics with efficiency and feasible-action projection, actual exhaustive finite action-sequence MPC and reactive control, independent multi-step forecast and closed-loop cost assessment, changed-demand regime and terminal-value assumptions retained.

```bash
python scripts/run_notebook.py notebooks/170_Chapter_32_04_learned_dynamics_planning_and_mpc.ipynb
```

## 32.5 · Offline learning and policy evaluation

- [Fit only from historical actions and preserve the missing column](notebooks/171_Chapter_32_05_offline_learning_and_doubly_robust_evaluation.ipynb#support-constrained-offline-learning)
- [Evaluate a supported policy; refuse an unsupported one](notebooks/171_Chapter_32_05_offline_learning_and_doubly_robust_evaluation.ipynb#dr-and-nonidentification)

Declared mechanisms: real fixed logged behavior trajectories with structural action noncoverage, unrestricted versus support-constrained fitted Q iteration, independent ordinary trajectory importance sampling and sequential doubly robust evaluation, whole-episode bootstrap and trajectory effective sample size, two observationally compatible worlds proving unsupported value nonidentification.

```bash
python scripts/run_notebook.py notebooks/171_Chapter_32_05_offline_learning_and_doubly_robust_evaluation.ipynb
```

## 32.6 · Constrained control and deployment tests

- [Stress a controller without hiding physical failures behind clipping](notebooks/172_Chapter_32_06_constrained_control_stress_and_termination.ipynb#bounded-storage-stress-tests)
- [Stop interaction on either flag; bootstrap only through truncation](notebooks/172_Chapter_32_06_constrained_control_stress_and_termination.ipynb#termination-and-truncation-tests)

Declared mechanisms: original five-tuple Gymnasium-style environment with explicit observed clock, actual feasible-action shields using trusted independent storage measurement, normal dropout demand-shift and efficiency-mismatch stress scenarios, nominal versus bounded-uncertainty robust projection and fallback, termination versus external truncation bootstrap tests and early-failure accounting.

```bash
python scripts/run_notebook.py notebooks/172_Chapter_32_06_constrained_control_stress_and_termination.ipynb
```

## Interpretation and boundaries

### Chapter 32 evidence and runtime

Chapter 32 is added only to `main_2.tex` / `output/pdf/main_2.pdf`. The separate first preview through Chapter 30 remains byte-identical. Chapter 31's source, notebooks and second-preview body pages are preserved. The second preview retains How to use this preview, contents and its own references; the two PDFs remain separate for later human assembly.

All six laboratories use the unchanged main CPython 3.14.3, NumPy 2.4.4 and Torch 2.14.1 CPU environment. Torch uses float64, one thread and deterministic operations. No package, downloaded asset, network request, credential or GPU is required by ordinary execution. The five-tuple control environment is an original Gymnasium-style implementation, not an imported native Gymnasium Env or checker-compliance claim. Each notebook has four executed code cells and two inline figures. Full code is rerun for vector exports and numeric RESULTS must agree exactly with fresh-kernel summaries.

### Mechanisms, controls and actual results

167: real disjoint linear LinUCB with ridge identity initialization and confidence coefficient 0.55, 600 training contexts and one observed chosen-action reward each. Counts 260/229/111. Only selected feedback updates statistics; full potential means remain simulator-only. A separate 400-context assessment freezes the ridge policy and compares conditional expected rewards, without noisy outcomes or final fitting: contextual 0.674175, random 0.253399, fixed first inspection 0.321158, oracle 0.674586. Training expected pseudo-regret is 3.759655. The exact two-step battery chooses wait then discharge for return 1 versus myopic 0.2. A hidden low-future-price regime reverses the first optimal action under the same present observation. The initial NumPy batched solve was repaired to use an explicit singleton right-hand-side dimension, then rerun; no score-selected parameter change was made.

168: explicit three-condition/two-action continuing maintenance MDP, discount 0.9. Value iteration takes 258 iterations and residual below 1e-12. Exact policy wait/repair/repair; exact healthy-wait Q 6.366972 and repair Q 4.348624. Real exploratory Q-learning uses 60,000 transitions, epsilon 0.3 and visit-count power −0.6 steps; all pairs are visited, with highly uneven counts [[41006,7261],[1665,9490],[77,501]]. The initial unjustified assertion that every pair must receive over 100 visits was replaced by the actual coverage assertion and the smaller count is disclosed. No trajectory or fitting setting changed. Tabular maximum Q error 0.038463 / Bellman residual 0.029491. A distinct generative simulator service supplies 6,000 uniformly sampled transitions to a one-hidden-layer 16-unit tanh Q network: 1,600 Adam 0.005 updates, batch 64, target copy every 50; error 0.264276 / residual 0.095868. Both greedy policies match the reference. Separate zero-reward two-state shared-feature counterexample updates only A→B records, gamma 0.95/step 0.1, amplifying weight by 1.09 to 30,987.01575 after 120 updates. It isolates an unsupported bootstrap rather than predicting universal divergence.

169: actual original PPO and SAC mechanisms, explicitly different tasks. PPO uses 30 on-policy batches ×48 episodes ×12 decisions =17,280 interactions, four epochs per batch, 16-unit tanh actor and critic, Monte Carlo returns at gamma 0.95, frozen old probabilities, normalized advantages, clip 0.2, entropy 0.01, critic coefficient 0.5 and gradient norm cap 1. No replay or final selection. Final deterministic argmax assessed on 300 independent matched-noise episodes: undiscounted mean 8.15 versus threshold repair 7.208667 and wait −11.222667; discounted 6.339825/5.737297/−6.542151. The final batch's recorded clip fraction is zero; clipping is implemented but not claimed active on every batch. SAC uses a tanh-Gaussian actor with change-of-variables log density, independent twin 32-unit critics, minimum soft backup, replay and Polyak 0.005 target updates. Fixed temperature 0.1, gamma 0.95, 3,600 transitions/256 uniform warm-up/3,344 batch-64 updates, critic lr 0.003/actor lr 0.001. Actual successor values bootstrap at external 32-step resets. Sixty independent matched-noise trajectories compare deterministic tanh means: undiscounted SAC −0.652905/proportional −0.635059/zero −2.066426; discounted −0.535513/−0.519556/−1.542429. Simple proportional control wins narrowly. Episode SDs are descriptive, not mean confidence intervals; no multiple-seed algorithm ranking is claimed. Discounted results were added explicitly and the current source rerun before publication, without selecting new training settings.

170: 30 generated 24-hour source days yield 690 demand residual pairs, least-squares intercept 0.001898 and coefficient 0.721537. Ten development days are diagnostic only (one-step MAE 0.065137); no selection or final refit. Unit battery/rate 0.25/efficiency 0.92 are known; only demand is learned and actions do not affect demand. Costs explicitly combine price purchases, peak-grid penalty coefficient 2 above 1.1, wear 0.02 and terminal storage coefficient 0.5 toward 0.5. Exhaustive 81 four-action sequences, first action only, state-dependent feasible projection; short-horizon terminal penalty is a declared heuristic. Ten familiar final days: no storage/reactive/persistence MPC/learned MPC costs 4.266641/4.287027/4.138903/4.126396. Ten changed-peak/different-persistence days: 5.800496/5.382552/5.290188/5.284075. Familiar learned one-/three-step MAE 0.060205/0.084425 versus persistence 0.078165/0.165852; changed learned 0.115604/0.181855. Fixed hour-16 rollout differs from future observed demand. No clairvoyant controller or field cost-saving claim. Legend clearance was repaired and both inline and vector figures rerun.

171: 200 fitting and 800 independent evaluation eight-step episodes, behavior wait/repair/overhaul probabilities [0.8,0.2,0] at every state. Training support counts [[824,240,0],[290,72,0],[143,31,0]]. Actual tabular FQI 100 iterations/gamma 0.9 with untouched optimistic unknown Q 5 chooses [wait,overhaul,overhaul]; simple support mask (at least ten state-action records) chooses [wait,repair,repair]. Simulator eight-step returns 0.833331 versus 5.163636. Mask is explicitly not CQL or a theoretical lower-bound implementation. A different fixed supported stochastic policy is evaluated at gamma 1 with model/finite-horizon Q,V fitted only on the 200 training episodes. Exact return 1.678812; trajectory IS 1.431109/episode SD 6.791695 and sequential DR 1.673035/SD 4.333482. Whole-episode 300-resample percentile intervals [1.025387,1.928264] and [1.368150,1.956431]. Weight sum 783.990012/max 4.561395/trajectory ESS 434.392284 out of 800. Evaluation outcomes never fit a nuisance model or select policy. An all-overhaul policy is refused by the support guard; identical logged worlds with overhaul reward −5/+5 give exact values −40/+40. The ambiguity is structural, not an interval-width problem.

172: original reset→(observation,info), step→(observation,reward,terminated,truncated,info). Unit storage evolves without clipping, max action 0.3. Trusted independent storage measurement supplies the shield; separately dropped policy sensor can trigger zero-action fallback. Natural day-24 horizon has observed clock, physical failure terminates, external limit truncates. Forty episodes per controller per scenario (normal/dropout 0.25/demand +0.6/efficiency 0.75). Unshielded fixed price rule fails in all 40 under every scenario, completing only 2–3 physical steps; low observed costs are not success. Nominal 0.92 projection survives familiar operation but fails all 40 at eta 0.75, serving 19/24 steps. Robust projection assumes eta∈[0.7,1.0], completes all tested episodes and passes 612 additional grid cases. Under shifted demand the nominal/robust controllers still exceed the 1.25 grid target on 0.889583/0.890625 of observed steps; storage feasibility does not imply service satisfaction. Dropout robust fallback triggers 222 times. Bootstrap tests retain actual successor state: r=1/gamma=0.9/Vnext=5 produces 5.5 after external truncation and 1 at true termination. The nominal failure trace ends rather than inventing later states. Figure labels and legends were repaired without metric changes and rerun.

### Interpretation and source boundaries

Nine primary records support contextual upper-confidence methods, tabular Q-learning, policy-gradient context, PPO, SAC, learned-model MPC, CQL context, sequential DR and the versioned Gymnasium interface. No author's benchmark gains are assigned to these original generated tasks. The publisher's Q-learning abstract supports the general tabular convergence boundary; no inaccessible full-text result is claimed inspected. PPO's clipped objective, SAC's log-density correction and target updates, and DR's independent-model backward recursion were checked against primary method text. Sources predate the 18 October 2026 cutoff and were accessed on 21 October 2026. Failed author-book fetches are not cited as inspected sources.

All assessment and fitting controls are fixed before final reporting. Final simulator truth diagnoses value error or identifies constructed ambiguity; it is never treated as available historical operational evidence. Controls, rewards, state observability, source support, generative sampling access, independent episodes and actual failures remain explicit. Small single-seed learned-policy comparisons and descriptive episode variability do not establish general algorithm superiority, field safety, a causal claim under arbitrary logs or hardware readiness. Kernel-manager transport notices appear in runner process logs rather than notebook stderr; they are not suppressed or described as learning failures.
