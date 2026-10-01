# GRID_RETURN_AND_SUSTAIN_QUALIFICATION_v0.2_RESULT_20261001.md

**Status:** QUALIFIED FOR RECOVERY_MODEL_DEVELOPMENT  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Recovery outcomes opened during qualification:** NO

## 1. Qualified recovery-state geometry

Perturbation entry remains:

[
E(t)=
[D_A(t)>T_A^{entry}]
lor
[D_R(t)>T_R^{entry}],
]

with q_entry=0.999 and 1-s source-unit-correct rate.

Recovery settling uses a distinct rate-energy object:

[
V_5(t)
=
sqrt{
rac{1}{5}
sum_{k=0}^{4} v_1(t-k)^2
}.
]

This is a 5-s causal rolling RMS of the 1-s derivative.

The distinction is intentional:

- 1-s rate is retained for abrupt perturbation entry;
- 5-s rate energy is used to ask whether short-timescale motion has actually settled.

## 2. Fresh confirmation result

The revised rule was confirmed on the untouched 20–25% QI-valid slice of each primary development campaign.

Eligible (W,q_return) pairs included:
- W=5, q=0.975;
- W=5, q=0.99;
- W=10, q=0.975;
- W=10, q=0.99;
- W=20, q=0.975;
- W=20, q=0.99.

The frozen hierarchy selected:
1. smallest eligible W;
2. lowest eligible q.

Therefore:

[
oxed{W=5 mathrm{s}}
]

and

[
oxed{q_{mathrm{return}}=0.975}.
]

## 3. Cross-grid input-state dwell at the selected return set

| Grid | Return-set occupancy | Median dwell | 75th percentile | 95th percentile |
|---|---:|---:|---:|---:|
| BALTIC | 0.9278 | 26 s | 70 s | 184.9 s |
| CONTINENTAL_EUROPE | 0.9378 | 48 s | 119.8 s | 310.4 s |
| GREAT_BRITAIN | 0.9494 | 105 s | 259 s | 801.6 s |
| ICELAND | 0.8317 | 13 s | 49 s | 262 s |
| MALLORCA | 0.8903 | 20 s | 50 s | 137 s |
| NORDIC | 0.9769 | 176.5 s | 440.8 s | 1211.1 s |
| WESTERN_INTERCONNECTION | 0.8656 | 18 s | 52 s | 152 s |

Thus the selected return set is neither nearly always true nor pathologically rare in any development grid.

## 4. Sustain qualification

Candidate sustain durations:

- 10 s
- 20 s
- 30 s
- 60 s

Input-only dwell adequacy:
- 10 s: PASS
- 20 s: PASS
- 30 s: FAIL
- 60 s: FAIL

Synthetic damped-oscillation safeguard:
- 10 s: false sustained-return rate 0.03333 -> FAIL
- 20 s: false sustained-return rate 0.00000 -> PASS
- 30 s: false sustained-return rate 0.00000 -> PASS
- 60 s: false sustained-return rate 0.00000 -> PASS

The frozen rule selects the shortest duration passing both gates.

Therefore:

[
oxed{L_{mathrm{sustain}}=20 mathrm{s}}.
]

## 5. Qualified state definitions

### FIRST_RECLAIM_PRE
First entry into the q_return=0.975 pre-event return set.

### SUSTAINED_RETURN_PRE
First time the pre-event return condition remains true for 20 continuous seconds.

### FIRST_RECLAIM_LOCAL
First entry into the q_return=0.975 local moving-baseline return set.

### SUSTAINED_RETURN_LOCAL
First time the local return condition remains true for 20 continuous seconds.

### REPERTURBATION_OR_REEXCITATION
A new q_entry=0.999 D_OR run begins before SUSTAINED_RETURN_PRE.

This state makes no claim that the second excursion is statistically independent of the first.

## 6. Time-to-event reporting

Primary development inference:
competing-event time to sustained pre-event return versus re-perturbation/re-excitation.

Frozen reporting horizons:

- 60 s
- 300 s
- 900 s.

No one horizon defines recovery by itself.

## 7. Partition update

Final development firewall before opening real recovery outcomes:

- 0–10%: input-geometry calibration;
- 10–15%: event-geometry confirmation;
- 15–20%: return v0.1 qualification / failure investigation;
- 20–25%: return v0.2 fresh confirmation;
- 25–60%: RECOVERY_MODEL_DEVELOPMENT;
- 60–80%: INTERNAL_VALIDATION;
- 80–100%: TEMPORAL_HOLDOUT.

External grid holdouts remain:
- ERCOT;
- GRAN_CANARIA;
- RUSSIA.

Within-grid replication holdouts remain sealed.

## 8. Exact embargo

The recovery development table must not use events whose analysis window crosses a partition boundary.

Use:
- baseline lookback: 101 s;
- maximum reporting horizon: 900 s.

Freeze a conservative partition embargo of:

[
oxed{1001 mathrm{s}}
]

from each recovery-development boundary for event-entry eligibility.

## 9. What this licenses

Real recovery outcomes may now be opened **only in the 25–60% RECOVERY_MODEL_DEVELOPMENT segment**.

Allowed first output:
an event-level raw recovery table containing native entry state and prespecified recovery outcomes.

Still prohibited:
- normal/abnormal labels;
- history-effect claims;
- validation-set access;
- holdout access;
- chi/Χ/Χ_arc interpretation;
- early-warning claims;
- operational intervention.
