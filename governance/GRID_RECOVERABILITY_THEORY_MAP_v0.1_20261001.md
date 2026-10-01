# GRID_RECOVERABILITY_THEORY_MAP_v0.1_20261001.md

**Status:** CENTRAL THEORY MAP — P0-N / P0-D  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** governance/GRID_RECOVERABILITY_CENTRAL_HYPOTHESIS_v0.1_20261001.md

## 1. Core interpretation

A disturbance spike is an **input** to the grid.

Recoverability is a property of the **state-conditioned response dynamics** that govern what happens after that input.

Therefore:

[
	ext{perturbation magnitude} 
eq 	ext{recovery ability}.
]

Two disturbances of comparable magnitude may have different scientific meaning if the grid's response law differs.

Conversely, a large transient may be ordinary if the grid exhibits the expected response-and-recovery trajectory for its current state.

## 2. Native dynamical form

Let (x(t)) denote the admitted native grid state and (b(t)) a causal operating-point / baseline trajectory.

Define local deviation:

[
y(t)=x(t)-b(t).
]

In a locally linear regime around time (t_0),

[
dot y(t)=A(t_0)y(t)+B(t_0)u(t)+eta(t),
]

where:
- (A(t_0)) is the local dynamic state operator;
- (u(t)) is the disturbance/input;
- (eta(t)) represents unresolved/stochastic forcing.

The finite-time response is governed by the propagator

[
Phi(	au;t_0).
]

For locally time-invariant dynamics,

[
Phi(	au;t_0)=e^{A(t_0)	au}.
]

The spike itself is represented by (u) and the resulting initial displacement.

The ability to recover is represented by the properties of (A), (Phi), the nonlinear basin around the state, controls, and stochastic forcing.

## 3. Why spike amplitude alone is insufficient

Three cases must be separable:

### Case A — large ordinary perturbation
Large input, but the conditional response operator is normal.

Possible observation:
- large displacement;
- large ROCOF;
- expected transient;
- ordinary restoring dynamics;
- sustained reclaim;
- no abnormal residual or reorganization.

Disposition: **large but normally recoverable**.

### Case B — small perturbation with impaired recovery
Small input, but the response law is altered.

Possible observation:
- modest displacement;
- weaker restoring rate;
- prolonged reclaim;
- repeated failed reclaim;
- abnormal residual burden;
- altered modal/vector organization.

Disposition: **small but recovery-abnormal**.

### Case C — transient amplification without lost recoverability
The spectrum may remain asymptotically stable while non-normality produces substantial finite-time growth.

Disposition: **transiently amplified but recoverable**, unless later recovery measures also fail.

This is why transient amplification and recoverability must remain separate coordinates.

## 4. First native mathematical levels of recovery ability

### Level R-A — local restoring tendency

For a one-dimensional local stochastic approximation:

[
d y = h(y,t),dt + g(y,t),dW_t.
]

Near an operating point,

[
h(y,t)approx zeta(t)y.
]

For stable local restoring dynamics:

[
zeta(t)<0.
]

The magnitude of the negative slope represents a local restoring rate.

A move of (zeta) toward zero corresponds to weaker local restoring tendency.

This connects directly to modern Bayesian-Langevin power-grid work, but only within the scale and observable for which that reduction is valid.

### Level R-B — modal/vector response

For multidimensional linearized dynamics, eigenvalues alone do not completely determine finite-time response.

Relevant objects include:
- eigenvalues;
- damping ratios;
- eigenvectors / mode shapes;
- participation / observability;
- condition numbers;
- singular values of (Phi(	au));
- pseudospectral / non-normal growth.

Mode-specific (chi_i), if independently licensed, belongs here as one local damping coordinate.

It does not by itself equal recovery ability.

### Level R-C — nonlinear recoverability / basin

For sufficiently large perturbations, local linear response may not determine whether the state returns.

A nonlinear system may have:
- a recovery region;
- basin boundary;
- multiple stable operating states;
- protection/control discontinuities;
- saturation/current limits;
- topology change;
- state-dependent switching.

This level determines whether a perturbation is recoverable at all for the present parameter/state configuration.

### Level R-D — empirical conditional recovery law

For field data where (A), (Phi), and the nonlinear basin are incompletely observed, define an empirical conditional law:

[
mathcal{P}
left(
R_j
mid
Z_j^{-},
P_j,
C_j,
H_j^{-}
ight),
]

where:
- (R_j) = finite-time recovery vector;
- (Z_j^{-}) = pre-event native state;
- (P_j) = perturbation class/magnitude/direction;
- (C_j) = operating context/noise/forcing/measurement state;
- (H_j^{-}) = prior perturbation/recovery history.

The central hypothesis is that (H_j^{-}) may change this law even after conditioning on current state and perturbation.

## 5. "Normal recovery" definition

Normal recovery is **not** defined as "frequency returns quickly" and not as "small spike."

A provisional scientific definition is:

> The observed response trajectory belongs to the frozen conditional response-and-recovery family expected for the present grid state and perturbation class.

This family may contain:
- underdamped recovery;
- overdamped recovery;
- transient amplification;
- shifted but stable operating points;
- different event magnitudes;
- different recovery times across grids.

Normality is conditional, not universal.

## 6. Recovery-law change

A candidate recovery-law change exists when, after controlling for current state and perturbation:

- local restoring rate changes;
- state-transition / propagator behavior changes;
- recovery-time distribution shifts;
- sustained-reclaim probability changes;
- transient-growth distribution changes;
- residual burden changes;
- mode/participation organization changes;
- history becomes predictive.

A recovery-law change is not automatically deterioration.

Allowed directional outcomes:

[
	ext{erosion},quad
	ext{no material change},quad
	ext{adaptation/strengthening}.
]

## 7. Baseline migration versus recovery-law change

Let (b(t)) move while the local response law remains unchanged.

Then the grid can move to a new operating point without losing recovery capability.

Scientific requirement:

[
Delta b 
eq 0

otRightarrow
Delta mathcal{R} 
eq 0.
]

Conversely:

[
Delta b approx 0

otRightarrow
Delta mathcal{R} = 0.
]

The operating point can remain similar while the local restoring or modal response changes.

This is one of the central discriminations of the program.

## 8. Literature collision map

### Fisher & Hiskens — recovery regions
Fisher and Hiskens define parameter-space recovery regions: for a specified disturbance, combinations of system parameters are separated into trouble-free recovery versus undesirable non-recovery, with distance to the boundary forming a recovery safety margin.

This occupies the model-based nonlinear "can the system recover?" question.

Our field-data question is different:
does the inferred recovery law change across matched observed perturbations and histories?

### Heßler & Kamps — restoring rate plus noise
Recent Western Interconnection analysis estimates local restoring-rate changes and noise intensity from frequency time series.

This occupies part of Level R-A and establishes that restoring tendency and stochastic forcing can be separately estimated.

It is a direct native comparator for any frequency-only recovery-law inference.

### Maldonado et al. — transient linear growth
Power-system non-normality work demonstrates that asymptotically stable eigenvalues can coexist with substantial finite-time amplification.

This occupies part of Level R-B.

Therefore spike amplification is not equivalent to impaired asymptotic recoverability.

### Liu, Zhu & Kekatos — recovered impulse response
Ambient synchrophasor work reconstructs impulse/dynamic responses from cross-correlations.

This is highly relevant to estimating (Phi)-like response information from measurements.

Their term "dynamic response recovery" refers to reconstructing a response, not testing whether post-disturbance recovery ability has degraded.

### Danziger et al. — elastic versus nonlinear service recovery
Large-scale outage observations show a strong normal elastic/linear repair-response regime for most ordinary service outages, with large disruptions departing systematically from that regime.

This is a service-restoration timescale, not electromechanical recovery.

However, it provides a strong conceptual precedent for the exact statistical structure we want to test:
**learn the ordinary response law first, then test departures from it rather than classifying by shock size alone.**

### Outage/restoration resilience literature
Established work quantifies outage magnitude, restoration time, service-loss curves and recovery coupling.

These are adjacent but operate mostly on minutes-to-days service restoration, not subsecond-to-minute electromechanical recoverability.

## 9. Central test reformulated

The first decisive test should not be:

> Does chi fall after a spike?

It should be:

> After conditioning on the present state and perturbation, is the response-and-recovery law invariant?

Operationally:

[
H_0:
mathcal{P}(R_j mid Z_j^{-},P_j,C_j,H_j^{-})
=
mathcal{P}(R_j mid Z_j^{-},P_j,C_j).
]

versus:

[
H_1:
H_j^{-}
	ext{ adds reproducible out-of-sample information.}
]

If (H_1) survives, ask what changed physically:
- local restoring rate;
- noise;
- mode damping;
- participation/coupling;
- non-normality;
- operating-point basin;
- control/topology state;
- broader (Chi) / (Chi_{mathrm{arc}}) structure if licensed.

## 10. Tool implication

A successful tool should not first answer:

**"Was the spike large?"**

It should answer, in order:

1. What was the pre-event state?
2. What kind/magnitude of perturbation occurred?
3. What recovery family is expected for that state/input?
4. Is the observed trajectory inside that family?
5. If not, is the departure explained by baseline motion, forcing, noise, interruption, or measurement quality?
6. If unexplained, which recovery component changed?
7. Is the change isolated, persistent, history-dependent, or reorganized?

Only after those steps can a scientifically defensible warning state exist.

## 11. Current strongest conceptual outcome

The investigation is now centered on a **response-law invariance hypothesis**:

> Healthy/ordinary perturbations may vary greatly in size, but after conditioning on grid state and disturbance class they should belong to a reproducible family of recovery dynamics. A meaningful loss or change of recoverability is a reproducible departure in the response law, not merely a large excursion.

This hypothesis can be supported, narrowed, or falsified without requiring SymC.

If supported, the relationship of (chi_i), (Chi), and (Chi_{mathrm{arc}}) to that recovery law becomes a second-stage mechanistic/representation question.
