# GRID_RETURN_SET_v0.1_FAILURE_AND_v0.2_DELTA_20261001.md

**Status:** v0.1 RETURN SET REFUSED / v0.2 SETTLING-RATE DELTA FROZEN  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Recovery outcomes opened:** NO

## 1. v0.1 failure

No q_return candidate satisfied the frozen all-grid return-set criteria.

Input-only 15–20% qualification results:

- q=0.95: minimum occupancy 0.6876; minimum median dwell 5 s.
- q=0.975: minimum occupancy 0.7591; minimum median dwell 5 s.
- q=0.99: minimum occupancy 0.8331; minimum median dwell 5 s.

Therefore:
- RETURN_SET_REFUSED;
- SUSTAIN_RULE_REFUSED.

No real post-perturbation recovery trajectory was opened.

## 2. Root cause investigation

The limiting grid was ICELAND.

At q_return=0.99:

- amplitude-only return occupancy: ~0.9176;
- amplitude-only median dwell: 32 s;
- 1-s rate-only occupancy: ~0.9011;
- 1-s rate-only median dwell: 11 s;
- joint amplitude+1-s-rate occupancy: ~0.8331;
- joint median dwell: 5 s.

Thus the 1-second rate component fragments otherwise stable central-state dwell.

This is an input-state geometry problem, not evidence that Iceland cannot recover.

## 3. Rejected mechanical fix

Exploratory 5-s and 10-s lagged differences increased joint dwell.

They are **not adopted** because fixed-lag differencing has frequency-dependent cancellation/nulls:
a coherent oscillation whose period aligns with the lag can produce an artificially small lag-difference.

That is unacceptable in a power-system recovery metric.

## 4. v0.2 settling-rate family

Retain the entry-rate coordinate:

[
v_1(t)=f(t)-f(t-1)
]

for q_entry perturbation detection.

For recovery-state settling only, define a nonnegative recent-rate-energy coordinate:

[
V_W(t)
=
sqrt{
rac{1}{W}
sum_{k=0}^{W-1}
v_1(t-k)^2
}.
]

Candidate causal windows:

- W=5 s
- W=10 s
- W=20 s

The window resets/refuses across QI/timestamp gaps.

Unlike a fixed-lag difference, RMS derivative energy does not vanish merely because the window matches an oscillation period.

## 5. Fresh confirmation firewall

The 15–20% slice has already been inspected and may not confirm v0.2.

Create:

- 20–25% QI-valid time = RETURN_SET_v0.2_CONFIRMATION;
- 25–60% = RECOVERY_MODEL_DEVELOPMENT;
- 60–80% = INTERNAL_VALIDATION;
- 80–100% = TEMPORAL_HOLDOUT.

No event-specific recovery outcome may be computed in 20–25%.

## 6. Training-only thresholds

For each W and q_return in:

- 0.95
- 0.975
- 0.99

estimate on the original METRIC_TRAIN only:

[
T_A^{ret}(q)=Q_q[D_A]
]

and

[
T_{V,W}^{ret}(q)=Q_q[V_W/s_{V,W}]
]

where (s_{V,W}) is a robust scale estimated on METRIC_TRAIN only.

The amplitude threshold retains the same K1 residual geometry.

## 7. Fresh input qualification

On the 20–25% confirmation slice, a (W,q) return set is eligible if every development grid has:

1. joint occupancy >=0.80;
2. joint occupancy <=0.995;
3. median dwell >=10 s;
4. 75th-percentile dwell >=20 s.

Selection:
1. choose the smallest W with at least one eligible q;
2. within that W choose the lowest eligible q.

This prioritizes temporal resolution, then the stricter central-state definition.

If no pair passes, return RETURN_SET_REFUSED again.

## 8. Sustain duration

Candidate continuous sustain durations remain:

- 10 s
- 20 s
- 30 s
- 60 s.

Input adequacy:
- at least 25% of return-set dwell runs in every grid last >=L;
- median fraction across grids >=50%.

Synthetic damped-oscillation safeguard is repeated using (V_W), with periods 1, 2, 5 and 10 s.

A sustain candidate passes synthetic qualification only if false sustained-return rate <=1%.

Choose the shortest L passing both input and synthetic criteria.

## 9. Reference frames remain unchanged

Pre-event return:

[
A_{pre}(t)=|f(t)-B_0|/s_r.
]

Local stabilization:

[
A_{local}(t)=|f(t)-B(t)|/s_r.
]

The selected (V_W) is used with both.

A local stabilization without pre-event return remains a distinct outcome and is not automatically damage.

## 10. Consequence

The program explicitly permits the event-entry rate and recovery-settling rate to differ.

They answer different questions:

- entry v1: did an abrupt perturbation occur?
- settling V_W: has short-timescale frequency motion actually quieted?

No claim of universal optimal W is allowed beyond the qualified frequency-data lane.
