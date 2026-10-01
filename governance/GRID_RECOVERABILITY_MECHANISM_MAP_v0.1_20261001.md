# GRID_RECOVERABILITY_MECHANISM_MAP_v0.1_20261001.md

**Status:** ACTIVE THEORY / COMPARATOR MAP  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_RECOVERABILITY_THEORY_MAP_v0.1_20261001.md

## 1. Purpose

A slow or incomplete return after a disturbance is not one mechanism.

The central recoverability program must distinguish at least six physically different causes before interpreting any event as deterioration.

## 2. Mechanism classes

### M1 — weakened local restoring tendency

Local frequency or voltage dynamics may exhibit a reduced restoring rate.

A local stochastic approximation may be written:

[
dy = h(y,t),dt + g(y,t),dW_t,
]

with local slope

[
zeta(t)=partial h/partial y.
]

For a stable local fixed point, (zeta<0).

A movement of (zeta) toward zero implies slower local return, but does not identify the cause by itself.

Native comparator:
Heßler & Kamps, Nature Communications 2025, DOI 10.1038/s41467-025-60877-0.

Required separation:
restoring-rate change versus increased noise intensity.

### M2 — stochastic forcing/noise increase

Observed excursions can become larger or more frequent even if the deterministic restoring law is unchanged.

Therefore:

[
	ext{more volatility}

otRightarrow
	ext{weaker recoverability}.
]

A valid method must estimate or condition on the noise/forcing state separately from the recovery law.

Native comparator:
Bayesian Langevin estimation of drift and diffusion/noise.

### M3 — non-normal transient amplification

A stable system matrix can have all eigenvalues in the stable half-plane while finite-time perturbations grow substantially before decaying.

For linear dynamics:

[
y(	au)=Phi(	au)y(0),qquad Phi(	au)=e^{A	au}.
]

If (A) is non-normal, the largest singular value of (Phi) can exceed one even when all eigenmodes are asymptotically damped.

Therefore:

[
A_{mathrm{transient}}>1

otRightarrow
	ext{loss of asymptotic recoverability}.
]

Native comparator:
Maldonado et al., maximum transient linear growth in power systems.

Required separation:
large short-term amplification versus impaired sustained recovery.

### M4 — nonlinear basin / recovery-region change

For large disturbances, local eigenvalues may be insufficient.

The relevant object can be the set of state/parameter combinations that return to an acceptable operating state after a specified disturbance.

This includes:
- basin boundaries;
- unstable equilibria;
- protection switching;
- topology changes;
- controller mode changes;
- saturation/current limits.

Native comparator:
Fisher & Hiskens, "Determining Disturbance Recovery Conditions by Inverse Sensitivity Minimization," DOI 10.1109/TPWRS.2025.3600275.

The recovery boundary is a strong native comparator for any claim about "how far the grid can be pushed and still recover."

### M5 — controller saturation / converter-mode recovery

In inverter-rich systems the post-fault dynamics may change because the controller has entered a different operating mode.

Current limiting can:
- remove outer-loop voltage control temporarily;
- change post-fault phase/power-angle dynamics;
- cause integrator windup;
- trap the device in current-limited operation;
- lengthen recovery;
- produce oscillation between control modes.

Relevant literature includes:
- overcurrent/current-limiting reviews for grid-forming inverters;
- post-fault current-saturation recovery studies;
- model-predictive post-fault recovery control.

Implication:
a changed recovery trajectory can be caused by a **control-regime switch**, not by a generic loss of grid damping.

### M6 — operating-point / topology / composition migration

Load, generation mix, tie-line flow, topology, control settings, and IBR composition move over time.

These can alter:
- eigenvalues;
- mode shapes;
- participation;
- local restoring rates;
- inertia-like response;
- transient growth;
- recovery basin.

The first question is therefore not "did recovery change?"

It is:

> did recovery change more than expected from the changed operating point?

This mechanism is central to separating benign baseline migration from degraded recoverability.

## 3. History dependence is a separate hypothesis

None of M1-M6 by itself establishes memory.

The history hypothesis requires:

[
mathcal{P}(R_j mid Z_j^{-},P_j,C_j,H_j^{-})

eq
mathcal{P}(R_j mid Z_j^{-},P_j,C_j)
]

out of sample.

If history adds no information after the current state is properly measured, then the grid may be effectively Markovian at the admitted state resolution.

That is a scientifically valuable negative result.

If history does add information, at least three interpretations must be separated:

1. **hidden state** — current observables are incomplete;
2. **physical memory** — equipment/control state carries path dependence;
3. **structural reorganization** — the effective response architecture has changed.

Do not call all three "damage."

## 4. Recoverability decomposition

A useful conceptual decomposition is:

[
mathcal{R}
=
mathcal{R}
left(
	ext{restoring tendency},
	ext{noise/forcing},
	ext{transient amplification},
	ext{basin/recovery region},
	ext{control mode},
	ext{operating point},
	ext{history}
ight).
]

This is a scientific decomposition, not a proposed scalar score.

No universal aggregation is assumed.

## 5. Normal perturbation test

For a candidate event:

### Step 1 — input
How large and how fast was the disturbance relative to the current baseline/noise state?

### Step 2 — immediate response
Was transient amplification ordinary for this state/input?

### Step 3 — restoring dynamics
Did the local restoring tendency remain within the matched normal envelope?

### Step 4 — sustained recovery
Did the system first reclaim and then remain reclaimed?

### Step 5 — state migration
Did the system settle to:
- the prior state;
- a new but stable operating point;
- a different control regime;
- or an unresolved/unstable state?

### Step 6 — history
After controlling the above, does prior perturbation/recovery history still predict the result?

A spike is "ordinary recoverable" only relative to this conditional chain.

## 6. Tool architecture implication

The eventual tool should report a **structured recovery diagnosis**, not one alarm number.

Possible internal outputs:

- INPUT_SEVERITY
- TRANSIENT_AMPLIFICATION
- RESTORING_RATE_STATE
- NOISE_FORCING_STATE
- FIRST_RECLAIM
- SUSTAINED_RECLAIM
- BASELINE_MIGRATION
- CONTROL_MODE_CHANGE
- HISTORY_EFFECT
- DATA_QUALITY
- IDENTIFIABILITY

A later user-facing simplification may be built only after these components are validated.

## 7. Relationship to SymC notation

If earned:

- (chi_i) may summarize one modal damping coordinate;
- (Chi) may represent modal/vector response organization;
- (Chi_{mathrm{arc}}) may represent broader recovery/stability architecture.

But recoverability is not defined by those symbols.

The correct causal order remains:

[
	ext{native recovery physics}
ightarrow
	ext{validated representation}
ightarrow
	ext{possible SymC interpretation}.
]

## 8. Immediate consequence for the empirical program

The first real-frequency study should test only what the frequency corpus can identify:

- moving baseline;
- displacement;
- ROCOF;
- local restoring tendency;
- noise/forcing scale;
- first/sustained return;
- residual burden;
- repeated-event history.

It should **not** claim:
- full-system modal participation;
- converter control-state diagnosis;
- topology-specific basin boundaries;
- impedance-based stability;
- (Chi_{mathrm{arc}}) reconstruction.

Those require richer PMU/model data.

## 9. Current strongest hypothesis

The central hypothesis is now sharper:

> After conditioning on operating state and perturbation, ordinary disturbances share a reproducible response law. A meaningful change in recoverability is a reproducible change in one or more recovery mechanisms, not simply a larger spike.

The program must determine whether that statement is true, false, or only valid within restricted grid classes and timescales.
