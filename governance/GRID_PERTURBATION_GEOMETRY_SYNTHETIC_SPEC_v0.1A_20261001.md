# GRID_PERTURBATION_GEOMETRY_SYNTHETIC_SPEC_v0.1A_20261001.md

**Status:** FROZEN NUMERICAL SPEC BEFORE EXECUTION  
**Date:** 2026-10-01  
**Parent:** governance/GRID_PERTURBATION_GEOMETRY_QUALIFICATION_PLAN_v0.1_20261001.md  
**Real grid outcomes opened:** NO

## 1. Calibration

Synthetic sampling interval: 1 s.

K1 baseline:
- causal rolling median;
- 101-sample window;
- minimum 60 past samples;
- current sample excluded.

Training null:
- 200,000 samples;
- stationary AR(1) ambient residual;
- AR coefficient 0.85;
- innovation SD 0.20 arbitrary frequency units;
- fixed random seed 771001.

Robust scale:
1.4826 × MAD.

D1-D3 thresholds:
empirical 0.999 quantile on the stationary training null after the first 500 samples.

## 2. Evaluation

Fresh replications: 250 per scenario.

Length: 3,000 s.

Perturbation nominal onset: t=1,200 s.

Detection window:
- first exceedance from t=1,200 through t=1,220 inclusive;
- detection probability is fraction of replications with at least one exceedance in that window;
- entry latency is first exceedance time minus 1,200 s.

Sharp-event latency rule applies to P01, P03 and P05.

## 3. Null scenarios

N01:
- AR coefficient 0.85;
- innovation SD 0.20;
- fixed zero baseline.

N02:
- same local dynamics;
- baseline linear drift +0.0003 units/s.

N03:
- same baseline/local dynamics;
- innovation SD increases linearly 0.18 -> 0.22.

N04:
- combines N02 drift and N03 variance change.

## 4. Perturbation scenarios

P01 impulse:
- instantaneous state kick +2.0 at t=1,200;
- recovery coefficient sampled by replication from {0.82, 0.88, 0.94, 0.97}.

P02 persistent set-point shift:
- baseline step +2.0 beginning at t=1,200;
- local recovery law unchanged.

P03 damped oscillation:
- additive amplitude 2.0;
- period 8 s;
- exponential decay time 30 s;
- begins t=1,200.

P04 ramp:
- additive displacement grows linearly 0 -> 2.0 over 15 s;
- then remains at 2.0 for the remainder of the 20-s detection window.

P05 small sharp impulse:
- instantaneous state kick +1.0;
- recovery coefficient sampled from the same P01 set.

P06 large smooth pulse:
- Gaussian-shaped additive pulse;
- amplitude 3.0;
- temporal SD 6 s;
- center t=1,210.

Perturbation sign alternates deterministically across replications so detection cannot rely on sign.

## 5. Artifact scenarios

A01:
- 120-s zero-filled segment flagged invalid by QI.

A02:
- 120-s missing-data segment.

A03:
- explicit 15-s timestamp discontinuity.

Required behavior:
all are refused by preprocessing before coordinate-based scientific event classification.

## 6. Qualification

The eligibility and tie-break rules remain exactly those frozen in the parent plan.

Synthetic recovery behavior is not scored except insofar as P01/P05 deliberately vary recovery coefficient to verify that event detection is not contingent on one recovery speed.

Execution seeds:
- calibration seed fixed above;
- evaluation seed family begins at 881001 and is deterministic by scenario/replication.

No parameter may be revised after reading v0.1A results without preserving this execution as evidence and issuing a new plan delta.
