# GRID_PERTURBATION_INPUT_GEOMETRY_PLAN_v0.1_20261001.md

**Status:** FROZEN INPUT-ONLY QUALIFICATION PLAN  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_REAL_DATA_INTAKE_AND_HOLDOUT_FREEZE_v0.1_20261001.md  
**Recovery outcomes opened:** NO

## 1. Purpose

Qualify a native, outcome-blind perturbation-entry geometry for the frequency-only recovery lane.

This stage does **not** define whether an event recovered normally.

It only asks how to represent an input disturbance without:
- confusing baseline drift with a disturbance;
- confusing invalid/gapped data with a disturbance;
- reintroducing the historical mHz/s scaling error;
- forcing amplitude and rate into one unexamined scalar.

## 2. Geometry calibration firewall

For each primary development campaign:

- first 10% of QI=0 valid time = INPUT_GEOMETRY_CALIBRATION;
- next 50% = RECOVERY_MODEL_DEVELOPMENT;
- next 20% = INTERNAL_VALIDATION;
- final 20% = TEMPORAL_HOLDOUT.

Within INPUT_GEOMETRY_CALIBRATION only:

- first 20% of eligible geometry rows = METRIC_TRAIN;
- remaining 80% = METRIC_EVAL.

No real recovery outcome may be computed in either segment.

## 3. Native components

For frequency deviation (f(t)) in source mHz:

### Baseline residual
[
r_f(t)=f(t)-B(t)
]

where (B(t)) is the synthetic-qualified K1 causal trailing robust location.

K1 implementation for the 1-Hz source stream:
- rolling median of the preceding 101 contiguous QI=0 seconds;
- current sample excluded;
- reset after any timestamp gap or QI!=0 state;
- require full 101-second causal warmup after reset.

### Correct ROCOF-like component
[
v_f(t)=f(t)-f(t-1)
]

in **mHz/s** because source frequency deviation is already in mHz and nominal sampling is one second.

No extra factor of 1000 is allowed.

Derivative is refused across timestamp gaps or non-QI0 samples.

## 4. Training-only robust scaling

On METRIC_TRAIN only, separately estimate:

[
s_r = 1.4826,mathrm{MAD}(r_f),
qquad
s_v = 1.4826,mathrm{MAD}(v_f).
]

If either scale is nonfinite or effectively zero, the campaign returns INPUT_GEOMETRY_REFUSED.

Define component coordinates:

[
z_r=r_f/s_r,
qquad
z_v=v_f/s_v.
]

These are event-input coordinates, not chi.

## 5. Candidate event coordinates

Preserve (z_r) and (z_v) separately in all outputs.

Candidate scalar entry coordinates:

- D_A = abs(z_r): displacement-only;
- D_R = abs(z_v): rate-only;
- D_MAX = max(abs(z_r), abs(z_v)): union/max coordinate;
- D_E = sqrt(z_r^2 + z_v^2): Euclidean joint coordinate;
- D_M = shrinkage-Mahalanobis distance in [z_r,z_v], only if covariance conditioning is acceptable.

No coordinate may be renamed chi.

## 6. Mahalanobis refusal

D_M is eligible only if:
- finite covariance exists;
- effective rank is 2;
- condition number <= 100;
- shrinkage estimator is numerically stable.

Otherwise return MAHALANOBIS_REFUSED and continue with native/simple coordinates.

## 7. Tail-threshold candidate grid

Within each campaign and candidate coordinate, derive thresholds from METRIC_TRAIN only at:

- q = 0.995
- q = 0.999
- q = 0.9995
- q = 0.9999

Evaluate those frozen thresholds on METRIC_EVAL.

An exceedance run is a maximal contiguous 1-Hz sequence above threshold. No recovery horizon or post-event merge rule is used at this stage.

## 8. Input-only adequacy metrics

For every grid × coordinate × q report:

- training threshold;
- METRIC_EVAL exceedance fraction;
- number of exceedance runs;
- median and 95th-percentile run duration;
- four-block temporal exceedance fractions;
- temporal coefficient of variation;
- proportion of D_MAX entries attributable to displacement-only, rate-only, or both;
- fraction of candidate entries adjacent to a source gap/QI reset after the mandatory 101-second warmup.

Any nonzero post-warmup gap-adjacency artifact rate is investigated before promotion.

## 9. Threshold selection rule

Choose the **highest q** satisfying across all seven development grids:

1. at least 10 exceedance runs per grid in METRIC_EVAL;
2. median at least 30 exceedance runs per grid;
3. finite threshold and finite temporal-stability statistics in every grid.

If no q satisfies these rules for a coordinate, that coordinate is not eligible as the primary event-entry coordinate.

This criterion is about event-sample adequacy only and does not inspect recovery.

## 10. Coordinate selection rule

Primary scientific preference is to preserve the native 2D severity vector ((z_r,z_v)).

A scalar entry coordinate is selected only for episode entry bookkeeping.

Selection order:

1. D_MAX is preferred if it passes the threshold-adequacy rule because it transparently means "unusual displacement OR unusual rate."
2. If D_MAX fails, D_E is eligible if it passes.
3. D_M may replace D_E only if it passes conditioning and reduces median temporal exceedance-rate CV by at least 20% relative to D_E.
4. D_A or D_R alone may be selected only if joint coordinates fail and the retained component passes across all grids.
5. If no coordinate passes, return EVENT_GEOMETRY_REFUSED.

This hierarchy is frozen before looking at the geometry results.

## 11. Scientific interpretation

Passing this stage licenses only:
- a candidate perturbation-entry coordinate;
- a frozen input-only threshold construction rule;
- event severity components (z_r,z_v).

It does not license:
- normal versus abnormal recovery;
- a recovery horizon;
- a sustained-return rule;
- history dependence;
- chi/Χ/Χ_arc interpretation;
- early warning;
- operational intervention.

## 12. Next gate after qualification

After event geometry is qualified:

1. apply it to RECOVERY_MODEL_DEVELOPMENT only;
2. construct episode entries without opening holdout outcomes;
3. qualify return-set, sustain, interruption and horizon rules using synthetic truths plus development-only input geometry;
4. freeze those rules;
5. then open development recovery trajectories.
