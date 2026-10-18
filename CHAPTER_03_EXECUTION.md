# Chapter 3 execution evidence

**Date:** 19 October 2026 (Australia/Melbourne). **Status:** all five executed; publication verification pending.

Every cell ran in order in a fresh kernel using the existing runner and unchanged pinned environment. The five runs were launched concurrently; timings include kernel lifecycle and are observations on this machine, not performance promises. Every notebook defines its own data and helpers, needs no ordinary-run network/data downloads or keys, and prints actual versions, seed, hardware and results. Versions: CPython 3.14.3, NumPy 2.4.4, SciPy 1.17.1, pandas 3.0.3, Matplotlib 3.11.0 and scikit-learn 1.9.0, Darwin arm64 CPU. `pip check` passes; no new dependency was added.

| Example | Section | Code cells | Inline figures | Wall seconds incl. kernel lifecycle |
| --- | --- | ---: | ---: | ---: |
| [code_012](CODE_EXAMPLES.md#code_012) | 3.1 | 6 | 2 | 1.620 |
| [code_013](CODE_EXAMPLES.md#code_013) | 3.2 | 6 | 2 | 1.659 |
| [code_014](CODE_EXAMPLES.md#code_014) | 3.3 | 7 | 2 | 1.650 |
| [code_015](CODE_EXAMPLES.md#code_015) | 3.4 | 6 | 2 | 1.664 |
| [code_016](CODE_EXAMPLES.md#code_016) | 3.5 | 7 | 2 | 1.650 |

Total: **32 new code cells and ten inline figures**. Ordinary runs use modest CPU arrays; repeated sampling and bootstrap budgets are numerical controls, not additional scientific observations.

## Actual outcomes and checks

- **code_012:** all eight joint-table probabilities sum to one. Overall rate is .096, high-load rate .26 and reversed conditional 52/96=.541667. The total-probability identity and dependence check pass. At 60% high-load mixture with conditional rates held fixed, the scenario rate is .178. Normal-density integration gives approximately one; probability over [0.9,1.1] mm is .382925 and invariant to consistent unit conversion. Bernoulli mean/variance simulation agrees with its declared distribution.
- **code_013:** equal 10,000-row designs have theoretical population-mean SEs .0655308 and .00717137, compared with empirical .0660914 and .00703554 across 3000 fresh samples. Design effects are 477.142857 and 5.714286. Known-model normal intervals for the 100-building design cover .95 of the replications on this run; nominal coverage is approximate and simulator variance is explicitly known. Selection enrichment gives .308032 versus exact selected-population probability .307692. Repeated readings estimate a biased measured mean of 1.149835 mm, not the latent 1 mm.
- **code_014:** MLE is .2; sequential posterior shapes are (6,34), then (14,106), matching a batch update. Posterior means are .15 and .116667. The first equal-tailed 95% credible interval is [.0586243,.2742994]. For ten future outcomes, beta-binomial variance is 1.554878 versus plug-in binomial 1.275. A separate zero/20 batch has Wilson interval [0,.161125] and uniform-prior credible interval [.00120488,.161098], with different meanings. Posterior quantiles, normalization, predictive mean/variance and predeclared prior-sensitivity calculations pass.
- **code_015:** observed equal-building paired difference is .0133910 mm, although the declared simulator population mean is .08 mm. The building-bootstrap interval is [-.0546124,.0802295] mm; the deliberately wrong row-bootstrap interval is [.00154081,.0258150] mm. Bootstrap SE ratio is 5.57603. This contrast is retained rather than selecting a seed with a more favorable effect. Pairing equivalence and independent-building SE agree. The symmetry-dependent Monte Carlo sign-flip p-value is .6998. In 2000 independent twenty-candidate normal-null searches, familywise rejection rates are .6365 unadjusted and .044 with Bonferroni; independent-test unadjusted theory is .641514.
- **code_016:** the Bernoulli predictive variance .1275 equals .12439024 expected conditional variance plus .003109756 parameter-mean variance. Repeated normal-model mean and new-outcome coverages are .94925 and .9512; misusing the mean band for a new outcome covers only .2976. A biased sensor's measured mean is 1.150450 mm with noise-only SE .00115470 mm. Material-A-only compliance estimate is .0019955553 mm/N. The fixed 600-outcome assessment sets have coverage .953333 in material A and .333333 in material B after compliance changes. No B outcome is used to fit or retune the A model or interval rule.

## Interpretation and verification

The Bernoulli event is a declared one-year inspection criterion, not structural collapse. Counts and distributions are invented. Hierarchical outcomes are conditionally independent within building only after fixing its latent rate; marginal dependence is retained. The design-effect formula assumes equal cluster sizes and a common within-building correlation. Known-model simulation intervals are not claimed estimated from one observed building.

Beta updates assume one common recorded-event probability, independent comparable outcomes and unchanged ascertainment. Priors are declared and compared, not chosen after viewing which conclusion they support. Credible intervals concern the parameter; predictive counts integrate its uncertainty. Confidence interpretation, density units, zero-event limits and prior sensitivity remain explicit.

The paired bootstrap concerns assessment-sample uncertainty for fixed predictors and an equal-building estimand. It omits retraining/selection uncertainty. Percentile intervals are pedagogically transparent, with no exact small-sample coverage claim. Sign flips require symmetry/appropriate randomization, not merely equal means. Null multiplicity experiments use valid normal-model t tests. Bonferroni relies on valid individual tests and a defined family. The support flag for a new material is not a calibrated error probability or guaranteed interval.

Notebook schemas, execution sequence, no error outputs, meaningful assertions, output-summary/manifest agreement, permanent anchors and local links are checked with `scripts/check_chapter03.py`. All ten figures are visually reviewed. Numerical plots use explicit units/reference populations and line styles/hatching for grayscale. The original eleven notebook files and their manifest entries remain unchanged. Manuscript and book-figure sources are maintained separately and excluded from this public repository.
