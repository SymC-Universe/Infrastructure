# GRID_HISTORY_MODEL_v0.1_PLAN_CORRECTION_v0.2_20261001.md

**Status:** PROSPECTIVE PLAN CORRECTION — NO REAL HISTORY MODEL FIT YET  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01

## Correction

The v0.1 history plan placed prior_incomplete_episode_count in M2 while also defining M3 as the incomplete-recovery alternative.

That overlap makes the M3 adjudication partially redundant.

No synthetic-history qualification and no real M0/M2 history fit had been run when this defect was found.

## Revised primary M2 block

M2 = M0 plus:

- log1p(prior_cum_amp_input);
- log1p(prior_cum_rate_input);
- log1p(prior_cum_outside_pre_return_s).

M2 does **not** include prior_incomplete_episode_count.

This tests cumulative perturbation/recovery burden without directly encoding whether a previous episode was formally incomplete.

## Revised M3 incomplete-recovery alternative

M3 = M0 plus:

- log1p(prior_incomplete_episode_count);
- previous episode final-cause indicators;
- prior mean outside-return burden per completed episode.

M3 is an alternative explanation, not an additional success route.

If M2 improves but M3 matches or exceeds that improvement and M2 adds no information when M3 terms are present, the development disposition is:

INCOMPLETE_RECOVERY_EXPLAINS_APPARENT_HISTORY_P0D.

## M0 exposure controls remain unchanged

M0 retains:
- prior episode count as exposure/ordinal nuisance;
- elapsed development time;
- time since previous episode end;
- recent 900-s episode count;
- current event/state/forcing variables.

Therefore the primary M2 comparison remains conservative against simple accumulation with time or event count.

All other v0.1 evaluation, macro-weighting, forward-fold, bootstrap, synthetic-gate, and holdout rules remain unchanged.
