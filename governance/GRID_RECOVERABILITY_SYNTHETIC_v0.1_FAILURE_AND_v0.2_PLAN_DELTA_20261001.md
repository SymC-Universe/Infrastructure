# GRID_RECOVERABILITY_SYNTHETIC_v0.1_FAILURE_AND_v0.2_PLAN_DELTA_20261001.md

**Status:** v0.1 SYNTHETIC QUALIFICATION INCOMPLETE / IMPLEMENTATION-PLAN MISMATCH PRESERVED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent plan:** governance/GRID_RECOVERABILITY_METHOD_QUALIFICATION_PLAN_v0.1_20261001.md

## 1. Failure found

The first synthetic implementation is not promotable.

Two defects were found during immediate self-audit:

1. **S10 overlapping/re-perturbation was omitted from the executable scenario list** even though it was required by the frozen v0.1 plan.
2. The executable eligibility rule used an **>=80% replicate pass fraction** for null/signal criteria, while the v0.1 plan text stated that an operator falsely labeling specified null scenarios as recovery deterioration was ineligible. The code therefore did not exactly implement the frozen plan.

No real recovery outcomes were opened. The v0.1 result is retained as development evidence only.

## 2. What v0.1 nevertheless showed

Across 40 fresh synthetic replications per scenario:

K1:
- null replicate-level pass fraction: 0.9286;
- true slowing detection: 1.000;
- true strengthening detection: 1.000;
- history-erosion monotonicity: 1.000;
- history-strengthening monotonicity: 1.000;
- median normalized baseline error: 0.5843.

K2:
- null replicate-level pass fraction: 0.9107;
- true slowing detection: 0.975;
- true strengthening detection: 1.000;
- history-erosion monotonicity: 1.000;
- history-strengthening monotonicity: 1.000;
- median normalized baseline error: 0.9590.

The null-scenario mean estimated late-minus-early recovery coefficient changes were near zero for both operators; stochastic replicate tails, especially under changing noise, crossed the hard per-replicate tolerance.

The non-normal known truth also behaved correctly: spectral radius 0.92, transient norm amplification from 1.0 to about 1.61, followed by decay to about 0.0058. This confirms why transient amplification must remain separate from asymptotic recovery failure.

## 3. v0.2 correction principles

v0.2 will use completely new random seeds and will not reuse v0.1 seeds.

Qualification is changed from an unrealistic "no noisy replicate may ever cross a tolerance" concept to a prespecified **known-truth ensemble criterion**.

For each operator and each null scenario:
- compute the mean late-minus-early recovery-coefficient change across replications;
- compute a 95% interval across replications;
- require absolute mean <= 0.02;
- require the full 95% interval to lie within [-0.05, +0.05].

For true slowing S05:
- mean change >= +0.05;
- lower 95% bound > +0.03.

For true strengthening S06:
- mean change <= -0.05;
- upper 95% bound < -0.03.

For history erosion S08:
- median event-index/recovery-coefficient Spearman rho >= +0.8;
- at least 90% of replications rho > 0.

For history strengthening S09:
- median rho <= -0.8;
- at least 90% of replications rho < 0.

For S10:
- at least 95% of known overlapping events must be classified as INTERRUPTED_BY_NEW_PERTURBATION rather than completed sustained recovery.

For S11:
- the baseline-shift scenario must satisfy the null recovery-law criterion while showing nonzero baseline migration.

For S12:
- stable spectrum + transient amplification + eventual decay must remain distinguishable.

For S13:
- injected missing/zero-fill artifact must trigger refusal/artifact detection before scientific recovery classification.

## 4. v0.2 operator selection

1. Both K1 and K2 must pass numerical/causal checks.
2. An operator failing any mandatory scenario-level criterion is ineligible.
3. If exactly one operator remains, select it as the candidate synthetic-qualified baseline.
4. If both remain, select lower median normalized baseline-location error.
5. If neither remains, return BASELINE_OPERATOR_REFUSED.
6. The selected operator is only synthetic-qualified; real-data transport remains a separate gate.

## 5. Independence rule

v0.2 uses new seeds not inspected in v0.1.

The v0.2 criteria above are frozen before those seeds are executed.

No real grid recovery/event outcomes may enter this revision.
