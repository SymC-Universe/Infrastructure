# GRID_PERTURBATION_GEOMETRY_SYNTHETIC_v0.1A_RESULT_20261001.md

**Status:** SYNTHETIC INPUT-GEOMETRY QUALIFICATION PASSED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Plan:** governance/GRID_PERTURBATION_GEOMETRY_QUALIFICATION_PLAN_v0.1_20261001.md  
**Spec:** governance/GRID_PERTURBATION_GEOMETRY_SYNTHETIC_SPEC_v0.1A_20261001.md  
**Real grid recovery outcomes opened:** NO

## 1. Selected coordinate

**D3 joint diagonal robust distance** is the only candidate that passed every frozen eligibility criterion.

Definition:

D3(t) = sqrt[(r(t)/s_f)^2 + (df(t)/s_df)^2],

where:
- r(t) is causal frequency displacement from K1 baseline;
- df(t) is the one-second native frequency increment;
- s_f and s_df are fixed robust training scales.

This remains a native frequency-space event coordinate. It is not chi, Χ, or Χ_arc.

## 2. Synthetic calibration

Stationary-null robust scales:
- s_f = 0.378015 synthetic units;
- s_df = 0.207573 synthetic units.

0.999 null thresholds:
- D1 = 3.402883;
- D2 = 3.293280;
- D3 = 3.902306.

These numerical synthetic thresholds are **not** real-grid thresholds.

## 3. D1 result

D1 displacement was stable on nulls and detected large/smooth events, but detected the small sharp impulse in only **30.4%** of replications.

Disposition: INELIGIBLE.

## 4. D2 result

D2 increment/ROCOF detected sharp impulses well but failed gradual/smooth perturbations:
- ramp detection: **3.6%**;
- smooth pulse detection: **30.8%**.

Disposition: INELIGIBLE.

## 5. D3 result

Null pointwise exceedance rates:
- stationary: 0.001074;
- moving baseline: 0.001069;
- changing variance: 0.001592;
- drift + changing variance: 0.001501.

All satisfy the frozen null limits.

Perturbation detection:
- impulse: 1.000;
- set-point shift: 1.000;
- damped oscillation: 1.000;
- ramp: 0.988;
- small sharp impulse: 0.936;
- large smooth pulse: 1.000.

Sharp-event median entry latency:
- impulse: 0 s;
- oscillation: 1 s;
- small impulse: 0 s.

Artifact refusal:
- 1.000 for QI-invalid zero fill, missing segment and timestamp discontinuity controls.

Disposition: ELIGIBLE / SELECTED.

## 6. Scientific interpretation

The result demonstrates a structural point relevant to the grid program:

- frequency displacement alone misses some sharp low-amplitude perturbations;
- increment/ROCOF alone misses gradual but large state excursions;
- their joint native geometry can retain both types without using future recovery.

This does not show that D3 predicts abnormal recovery. It only qualifies D3 as an event-entry candidate.

## 7. Next gate

D3 may now be exposed to DEVELOPMENT input geometry only.

Recovery outcomes remain sealed.

Real-grid threshold values must be derived from development input distributions under a separately frozen rule.
