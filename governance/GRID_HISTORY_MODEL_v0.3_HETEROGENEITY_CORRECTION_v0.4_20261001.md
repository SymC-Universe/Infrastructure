# GRID_HISTORY_MODEL_v0.3_HETEROGENEITY_CORRECTION_v0.4_20261001.md

**Status:** PROSPECTIVE IMPLEMENTATION CORRECTION — NO SYNTHETIC OR REAL HISTORY FIT YET  
**Date:** 2026-10-01

## Defect found

The v0.3 implementation freeze required detection of opposite history directions across grids but specified one global linear M2 history slope.

Without interactions, that learner cannot represent genuinely opposite grid-specific history directions.

## Correction

M2 retains the three primary burden features:

- log1p(prior_cum_amp_input)
- log1p(prior_cum_rate_input)
- log1p(prior_cum_outside_pre_return_s)

and additionally includes each burden feature interacted with grid identity.

M3 likewise includes grid interactions for its incomplete-recovery features.

All interactions use the same L2 regularization as the parent model.

No interaction is outcome-selected.

## Interpretation

The main M2 comparison still asks whether the burden block, including allowed grid heterogeneity, adds out-of-sample information beyond M0.

A program-wide direction label requires direction consistency.

If at least two grids show erosion-direction and at least two show adaptation-direction at the frozen >=0.01 probability-contrast magnitude, the result is MIXED_OR_DIRECTION_DEPENDENT even if M2 is predictively admitted.

## Robustness unchanged

Program-level M2 admission still requires:

- positive mean macro DeltaB;
- positive Fold A and Fold B deltas;
- positive all seven leave-one-grid-out aggregates;
- nonnegative macro delta in at least 5/7 grids;
- positive 95% hierarchical-bootstrap lower bound.

Therefore adding interactions does not permit one grid to generate a program-wide history result.

All other v0.3 rules remain unchanged.
