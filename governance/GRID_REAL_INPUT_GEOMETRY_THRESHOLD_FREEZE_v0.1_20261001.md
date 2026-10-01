# GRID_REAL_INPUT_GEOMETRY_THRESHOLD_FREEZE_v0.1_20261001.md

**Status:** FROZEN BEFORE DEVELOPMENT INPUT EXPOSURE  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_PERTURBATION_GEOMETRY_SYNTHETIC_v0.1A_RESULT_20261001.md  
**Recovery outcomes opened:** NO

## 1. Development-only exposure

Only the DEVELOPMENT portion of each primary development campaign may be used in this stage.

Internal validation, temporal holdout, same-grid replication holdouts, whole-grid holdouts and quality-limited auxiliary data remain closed.

## 2. Real baseline and scale construction

For each development grid independently:

- K1 baseline = causal 101-s rolling median using the previous 101 consecutive QI=0 seconds;
- current sample is excluded from the baseline;
- no baseline value is emitted until all previous 101 seconds are valid and contiguous;
- residual r(t)=f(t)-B(t);
- one-second increment df(t)=f(t)-f(t-1), only when both samples are QI=0 and contiguous.

Within DEVELOPMENT:
- first 70% of QI=0 development seconds = INPUT_CALIBRATION;
- final 30% = INPUT_GEOMETRY_CHECK.

Since DEVELOPMENT is the first 60% of primary-campaign QI=0 time, the calibration/check boundary is at 42% of total primary-campaign QI=0 seconds.

Robust scales s_f and s_df are estimated from INPUT_CALIBRATION only and frozen for the grid.

## 3. Selected event coordinate

D3(t)=sqrt[(r(t)/s_f)^2+(df(t)/s_df)^2].

No future recovery information enters D3.

## 4. Candidate entry quantiles

For each grid, candidate thresholds are the INPUT_CALIBRATION quantiles:

- q=0.995;
- q=0.999;
- q=0.9995.

Thresholds are grid-calibrated because the first frequency-only lane tests a common method under heterogeneous synchronous-area frequency statistics, not a universal raw-mHz threshold.

## 5. Geometry-check quantities

On INPUT_GEOMETRY_CHECK only, and without calculating post-entry recovery:

For each q:
- pointwise exceedance rate;
- ratio of check exceedance rate to nominal 1-q;
- number of contiguous exceedance runs;
- median run length;
- 95th-percentile run length;
- fraction of candidate runs touching any invalid/gap state, required to be zero by construction.

No time-to-return, sustained return, burden, or residual recovery endpoint is calculated in this stage.

## 6. Entry-quantile eligibility

A candidate q is eligible only if, in every development grid:

1. at least 25 contiguous exceedance runs occur in INPUT_GEOMETRY_CHECK;
2. no invalid/QI!=0 point enters a run;
3. check exceedance-rate ratio lies within [0.25, 4.0] of nominal 1-q.

Additional cross-grid criterion:
- median exceedance-rate ratio across the seven grids must lie within [0.5, 2.0].

If multiple q values qualify:
- select the **highest q** to reduce event overlap and preserve clearer perturbation episodes.

If no q qualifies:
- return REAL_ENTRY_THRESHOLD_REFUSED and issue a plan delta before any recovery outcome is opened.

## 7. Why the highest eligible q is selected

The scientific goal is not to maximize the number of labeled events.

The first confirmatory lane requires sufficiently separated, clearly identifiable perturbations with enough observations for recovery modeling.

A lower threshold remains a later sensitivity analysis after the primary threshold is frozen.

## 8. Development-data computation limits

This stage may calculate only:
- baseline;
- fixed robust scales;
- D3;
- candidate threshold values;
- exceedance/run geometry.

It may not calculate:
- T_first;
- T_sustain;
- recovery burden;
- history effects;
- abnormal-recovery labels;
- chi/Χ/Χ_arc recovery quantities.

## 9. Next gate

After a real entry quantile is selected:
- freeze episode entry/exit representation;
- freeze return set;
- freeze sustain rule;
- freeze maximum recovery horizon;
- freeze partition embargo.

Only then may real DEVELOPMENT recovery trajectories be opened.
