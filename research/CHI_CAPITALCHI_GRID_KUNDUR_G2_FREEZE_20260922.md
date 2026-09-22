# SymC chi <-> capital-Chi grid Kundur G2 freeze

Date: 2026-09-22
Status: P0-D PRE-RESULT CONTROLLED-NETWORK FREEZE
Promotion effect: NONE
Authority: GOM v0.8.3
Parent: CHI_CAPITALCHI_GRID_TRANSPORT_G1_POSTRESULT_20260922.md

## Question
With local machine/controller parameters held fixed, does changing only native cross-area network organization condition (a) low-frequency electromechanical modal chi and (b) realized two-area perturbation/recovery response?

G1 remains preserved: external synchronized measurements worsened five-minute focal prediction at all four empirical sites. G2 is a different controlled topology question, not a rescue/tuning of G1.

## Native engine and band
Use ANDES 2.0.0 case kundur/kundur_full.xlsx. The topology-only preflight ran no PFlow/EIG/TDS outcomes and passed in workflow 35756577977, artifact digest sha256:5b74d3b768704580a854cdac10ba73ae3f17eebf7f3bc8325a8e2b86ccc57de8.

Retain every positive-imaginary eigenvalue with 0.15 <= f <= 1.00 Hz. This band is frozen from NERC's electromechanical inter-area/local-plant band, not from the outcomes.

For lambda=a+ib:
chi_mode = -a/sqrt(a^2+b^2)
f_hz = b/(2*pi)

This is modal scalar chi, not a whole-grid scalar. No chi=1 optimum is asserted.

## Preflight-bound topology
AREA1: GENROU 1,2. AREA2: GENROU 3,4.
Cross-area corridor: three parallel bus 7 <-> 8 branches Line_4, Line_5, Line_6.
Source default disturbance Line_8 is internal to AREA2 (bus 8 <-> 9).
All source machine/controller parameters remain unchanged.

## Frozen static landscape
Disable source Toggle events. Fresh system per state:
1 INTACT
2 N1_LINE4
3 N1_LINE5
4 N1_LINE6
5 N2_LINE4_LINE5
6 N2_LINE4_LINE6
7 N2_LINE5_LINE6
8 LINE8_INTERNAL_OUT

Every state must be reported, including PFlow/EIG failure, instability, connectivity failure, or changed band-mode count.

## Mode matching and numerical floor
Run INTACT twice on fresh instances. Match retained modes one-to-one by Hungarian assignment minimizing abs(lambda_test-lambda_ref)/max(abs(lambda_ref),1e-12).

eps_chi = max(1e-8, 100*max_abs_repeat_delta_chi).

For each N1 tie state, material_modal_change is true if band-mode count changes or max matched abs(delta_chi)>eps_chi.

N1 disposition:
- >=2/3 material: TOPOLOGY_CONDITIONS_MODAL_CHI
- <=1/3 material: LOCAL_MODAL_INVARIANCE_IN_TESTED_N1_CORRIDOR
- repeat/matching/numerical failure: STATIC_TOPOLOGY_RESULT_UNRESOLVED

N2 and Line_8 are frozen extensions and cannot alter this N1 rule.

## Participation/mode-shape record
Where ANDES exposes them, preserve normalized GENROU speed-state participation and right-eigenvector speed amplitude/phase. Use them descriptively to inspect area participation. Do not use them to drop primary modes.

## Frozen TDS perturbations
Fresh intact systems; source Toggle disabled; tf=10 s.

Permanent trips at t=2 s:
Line_4, Line_5, Line_6, Line_8.

Temporary topology perturbations:
for each Line_4/5/6, trip t=2 s and reconnect same line t=4 s.

Primary observable:
omega_A1 = inertia-weighted mean speed of GENROU 1,2
omega_A2 = inertia-weighted mean speed of GENROU 3,4
gap = omega_A1-omega_A2

A no-event intact run defines:
eps_rms=max(1e-10,100*RMS(gap_intact,0..10s)).

Permanent metrics: peak_abs_gap_2_10, rms_gap_2_5, rms_gap_7_10.
Temporary metrics: peak_abs_gap_2_4, post_reclose_peak_abs_gap_4_10, rms_gap_4_6, rms_gap_8_10, first_reclaim.

First reclaim after t=4 is the first time abs(gap)<=0.10*peak_abs_gap_2_4 continuously for >=1.0 s. It is observable reclaim only, not full architectural restoration.

For each tie line, reclosure improvement is resolved only when permanent_rms_8_10-temporary_rms_8_10>eps_rms.

Recovery disposition:
- 3/3: TOPOLOGY_RESTORATION_CHANGES_REALIZED_RESPONSE
- 1-2/3: LINE_DEPENDENT_RECOVERY
- 0/3: NO_RESOLVED_RECLAIM_INCREMENT_FROM_RECLOSURE
- failed simulations: RECOVERY_RESULT_UNRESOLVED

## Joint adjudication
Static modal dependence and realized recovery are separate gates. Preserve disagreement.
Positive topology dependence means broader network organization conditions the realized modal scalar in this benchmark while local parameters are fixed.
Positive reclosure response means that relationship also survives a realized perturbation/recovery probe.
Neither result licenses a whole-grid scalar chi, a universal mechanism, or causal claims outside the controlled benchmark.

Native-method ceiling: STANDARD_TOOLKIT_SUBSUMES_MECHANISM unless a later frozen comparator establishes added SymC value.

## Stop rules
No outcome-informed topology selection, mode deletion, band change, threshold tuning, controller retuning, or event-timing changes.
Failures and unstable states are results.
After execution, independently verify arithmetic/rule application before interpretation.
