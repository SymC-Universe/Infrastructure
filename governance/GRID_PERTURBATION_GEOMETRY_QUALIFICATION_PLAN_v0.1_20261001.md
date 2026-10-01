# GRID_PERTURBATION_GEOMETRY_QUALIFICATION_PLAN_v0.1_20261001.md

**Status:** P0-Q SYNTHETIC INPUT-GEOMETRY QUALIFICATION / REAL RECOVERY SEALED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_REAL_DATA_PARTITION_MANIFEST_v0.1_20261001.md

## 1. Purpose

Qualify an outcome-blind frequency-only perturbation coordinate before looking at real recovery trajectories.

The coordinate must detect genuine input/state excursions while refusing or remaining stable under:
- moving baselines;
- changing noise scale;
- ordinary ambient fluctuations;
- invalid/zero-filled data;
- timestamp gaps.

It is not allowed to encode future recovery.

## 2. Frozen baseline

Use synthetic-qualified K1 causal trailing robust location as the candidate baseline operator.

On real data, K1 parameters remain subject to input-only transport checks, but recovery outcomes may not alter them.

## 3. Fixed-scale principle

The event metric must not normalize away a changing variance state.

For every training fold:
- baseline location is causal;
- residual scale is estimated from training data only and frozen;
- increment scale is estimated from training data only and frozen;
- changing local variance/noise remains a separate covariate.

## 4. Candidate coordinates

For residual:
r(t) = f(t) - B(t).

Let:
- s_f = robust training scale of r(t);
- s_df = robust training scale of one-second increments df(t)=f(t)-f(t-1).

### D1 — displacement
D1(t) = abs(r(t))/s_f.

### D2 — increment / correctly scaled ROCOF
D2(t) = abs(df(t))/s_df.

Because source frequency is already mHz at one-second resolution, df is numerically mHz/s when adjacent timestamps differ by exactly one second.

### D3 — joint diagonal robust distance
D3(t) = sqrt[(r(t)/s_f)^2 + (df(t)/s_df)^2].

No full covariance metric is admitted in the first frequency-only lane.

## 5. Synthetic threshold calibration

Each candidate is calibrated to the same nominal entry rate using synthetic stationary-null training data only.

Primary nominal pointwise exceedance rate:
0.001.

Threshold is the empirical 0.999 training-null quantile for that coordinate.

This equalizes nominal false-entry opportunity across D1-D3 before known-truth evaluation.

## 6. Fresh synthetic evaluation scenarios

N01 stationary colored ambient noise, no perturbation.  
N02 linearly moving baseline, unchanged local dynamics.  
N03 slowly increasing variance, unchanged recovery law.  
N04 combined moving baseline + heteroskedastic noise.  
P01 impulsive frequency displacement.  
P02 abrupt but persistent set-point shift.  
P03 damped oscillatory disturbance.  
P04 ramp-like disturbance.  
P05 small sharp impulse.  
P06 large smooth displacement.  
A01 zero-fill invalid segment.  
A02 missing-data gap.  
A03 timestamp discontinuity.

Recovery speed is varied independently of perturbation amplitude in P01/P03/P05/P06 so event detection cannot earn points from future recovery behavior.

## 7. Qualification metrics

For each candidate:
- pointwise false exceedance rate on N01-N04;
- episode-level detection probability for P01-P06 within a fixed short entry window;
- median entry latency;
- false episode count under drift/noise;
- artifact refusal rate for A01-A03.

No recovery time, sustained return, or post-entry outcome is used.

## 8. Selection rule

A candidate is eligible only if:
1. artifact refusal >= 0.99;
2. mean pointwise null exceedance <= 0.002 across N01-N04;
3. every perturbation family P01-P06 has detection probability >= 0.90;
4. median entry latency <= 5 s for sharp events P01/P03/P05;
5. no single null family has pointwise exceedance > 0.005.

If exactly one candidate is eligible, select it.

If multiple are eligible:
1. maximize the minimum P01-P06 detection probability;
2. then minimize worst-case N01-N04 false exceedance;
3. then minimize median sharp-event latency;
4. exact tie chooses lower-dimensional D1, then D2, then D3.

If none qualify: PERTURBATION_COORDINATE_REFUSED.

## 9. Real-development gate after synthetic qualification

Only DEVELOPMENT portions of the seven primary campaigns may be opened.

On development only:
- estimate training scales;
- compute the synthetic-qualified coordinate;
- inspect pointwise and clustered input geometry;
- evaluate candidate real entry quantiles 0.995, 0.999, 0.9995 for event density and data-quality contamination only.

No recovery trajectory may choose among real entry quantiles.

A separate freeze is required before event outcomes are constructed.

## 10. Native comparator preservation

D1, D2 and D3 remain interpretable in native frequency units.

Raw peak frequency displacement and correctly scaled ROCOF are retained for every future event even if a normalized coordinate is selected.

No chi/Χ/Χ_arc quantity participates in this qualification.
