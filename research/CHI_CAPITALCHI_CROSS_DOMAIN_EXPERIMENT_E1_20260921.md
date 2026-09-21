# SymC χ <-> Χ cross-domain experimental expansion: E1 independent sketches

**Date:** 2026-09-21  
**Status:** P0-D / E1 INDEPENDENT EXPERIMENT SKETCHS, PRESERVED BEFORE TARGETED LITERATURE COLLISION  
**GOM basis:** v0.8.1 active baseline with v0.8.2 REVIEW joint-meaning and reader-first controls applied prospectively at user direction  
**Central hypothesis under test:** if adding broader system architecture `Χ_t` improves prediction of a local stability coordinate `χ_{t+1}` beyond the local history alone, then system organization conditions realized local stability. The converse direction, `χ_t -> Χ_{t+1}`, is equally open.

## Cross-domain design rule

The program will not count three versions of the same mechanism as three independent examples. The first three primary testbeds intentionally span:

1. a directly manipulable second-order mechanical network where scalar χ is natively licensed;
2. a biological adaptation system where scalar χ must earn admission rather than being imposed;
3. a large engineered infrastructure network where local modal damping is meaningful but embedded behavior is network-dependent.

A fourth neuro-perturbational candidate is retained as an expansion option if an open dataset can support the same question without forcing a scalar.

For every testbed, compare:

[
M_0: z_{i,t+1} = f(z_{i,le t}, u_t)
]

against

[
M_1: z_{i,t+1} = f(z_{i,le t}, Χ_t, u_t)
]

where `z_i` is the local native stability coordinate, equal to scalar χ only where χ is independently licensed. The reciprocal test compares prediction of `Χ_{t+1}` from `Χ_{le t}` alone versus `Χ_{le t}` plus local `z_{i,t}`.

A positive result requires prospective held-out improvement, not mere contemporaneous correlation.

---

## E1-A. Coupled mechanical network, direct benchtop intervention

**Direct testing:** APPLICABLE.

### Native question

Does changing the coupling architecture around an oscillator alter its realized local recovery even when its isolated scalar damping ratio χ is held approximately fixed?

### System

A 3-5 node coupled translational or pendular network built from masses, springs, bearings/shafts, rigid supports, and controllable damping. Magnetic/eddy-current damping may be used if it can be calibrated reproducibly without changing stiffness materially.

### Local observable

For each node or licensed local mode, estimate its isolated second-order factor and

[
χ_i = rac{gamma_i}{2omega_{0,i}}
]

or the equivalent ringdown form when the single-mode approximation is demonstrably valid.

### Broader Χ representation

Preserve rather than collapse:

- full coupled-system mode frequencies;
- modal damping/eigenvalues;
- mode shapes and participation of the focal node;
- coupling graph and coupling strengths;
- energy redistribution among nodes;
- recovery trajectory after focal and nonfocal perturbations;
- model residual / open-channel structure.

No master Χ scalar is required.

### Manipulations

1. **Architecture intervention:** keep focal mass, local spring and damper fixed while changing coupling topology/strength around it: isolated, chain, ring, star/asymmetric.
2. **Local intervention:** change focal damping while keeping coupling architecture fixed.
3. **Perturbation location:** identical impulse/displacement applied locally versus elsewhere in the network.
4. **Optional substrate test:** change support/base compliance while keeping local assembly fixed.

### Controls

- isolated focal oscillator before and after every network condition;
- matched mass/stiffness controls;
- repeated randomized perturbation order;
- sensor relocation / calibration control;
- decoupled sham network;
- topology labels hidden during analysis where practical.

### Decisive observation

Evidence that Χ conditions local stability requires that the broader architecture improves held-out prediction of focal recovery/ringdown or embedded modal behavior beyond the focal isolated χ, perturbation amplitude, and local history.

A stronger causal signature is:

[
χ_i^{isolated,A} approx χ_i^{isolated,B}
]

while

[
P(z_{i,t+1}mid z_{i,t},Χ_A) 
e P(z_{i,t+1}mid z_{i,t},Χ_B)
]

under experimentally changed topology.

### Falsifier

- adding Χ does not improve prediction beyond local variables;
- apparent improvement disappears when modal participation/local forcing are controlled;
- the focal isolated χ changes materially with each topology, showing the manipulation did not isolate embedding;
- any apparent Χ effect is explained completely by a simpler native modal model.

### Feasibility

HIGH. This can be fabricated with ordinary mechanical components and can be instrumented with phone video, optical tracking, accelerometers, or inexpensive encoders before specialized sensors are justified.

### Claim ceiling

Direct evidence that **embedded network organization conditions realized local dynamics in this mechanical system**. It would not establish universal SymC architecture.

---

## E1-B. SCC25 cetuximab-resistance multi-omics trajectory

**Direct new wet-lab testing:** NOT_CURRENTLY_REQUIRED for the first pass.  
**Existing controlled empirical data:** APPLICABLE.

### Native question

During acquired drug resistance, does broader multi-layer organization contain information about subsequent local/modal stability and phenotype that is absent from the local dynamical coordinate alone, and vice versa?

### System

Weekly SCC25 cetuximab and time-matched PBS trajectories with RNA, DNA methylation, and proliferation/phenotypic observations.

### Local observable

No biological scalar χ is assumed.

Candidate local objects must pass a scalar-admission gate. Possible branches:

- a licensed continuous-time second-order mode reconstructed from an identifiable complex-conjugate operator pair;
- a model-specific modal persistence/decay coordinate if a true χ is not licensed;
- explicit scalar refusal when branch/embedding/representation ambiguity prevents a unique local χ.

The joint experiment proceeds even if the scalar branch refuses.

### Partial Χ representation

[
Χ_{mathrm{SCC25}}(t) = {R(t),S(t),M(t),T(t),Q(t)}
]

where:

- R: RNA regulatory-state architecture;
- S: methylation/epigenetic-context architecture;
- M: modal/vector organization;
- T: ordered transition/operator information;
- Q: uncertainty, identifiability and refusal information.

Proliferation remains external to Χ as a validation phenotype.

### Manipulations / contrasts

The empirical perturbation is cetuximab exposure versus time-matched PBS. The analysis must preserve time ordering and compare:

1. local-only prediction of next-week local/modal behavior;
2. local + Χ prediction;
3. Χ-only prediction of next-week broader organization or proliferation;
4. Χ + local prediction;
5. same-local / different-Χ trajectory segments;
6. different-local / similar-Χ trajectory segments, if naturally observed.

### Controls

- PBS time-matched arm;
- persistence and arm-specific mean-next-state baselines;
- source-native temporal-program comparator;
- same-task DMD/DMDc/state-space comparator for transition prediction;
- feature/null definitions fixed before outcome-bearing rerun;
- methylation and RNA construction non-circularity check.

### Decisive observation

One or more of the following:

- Χ_t improves held-out prediction of local/modal state at t+1 after local history is known;
- local state improves held-out prediction of Χ_{t+1};
- joint local+Χ model improves held-out proliferation/resistance prediction over either alone;
- same local coordinate appears under materially different broader organization with different future behavior;
- scalar branch refuses but modal+Χ relationship remains predictive.

### Falsifier

- local history fully subsumes broader architecture for the tested task;
- broader architecture fully subsumes the local coordinate;
- neither carries held-out information beyond standard temporal baselines;
- joint benefit disappears under source-native methods or composition/representation robustness;
- the local scalar is not identifiable.

### Feasibility

HIGH for computation using existing source data. New wet-lab replication becomes justified only after a residual question remains following literature and archival analysis.

### Claim ceiling

Evidence about local/system interaction during one cancer-resistance model, not clinical utility and not pan-cancer universality.

---

## E1-C. Power-grid disturbance recovery and network embedding

**Direct intervention on real grid:** NOT FEASIBLE / NOT ETHICALLY OR OPERATIONALLY APPROPRIATE.  
**Archival PMU/FNET + controlled simulation/hardware analog:** APPLICABLE.

### Native question

Does network-wide modal/coupling state improve prediction of local electromechanical recovery beyond the local mode's damping estimate and recent local history?

### System

Real disturbance windows from the existing PMU/FNET grid program, paired with prospective simulation of matched network perturbations in a standard power-system model. A later low-voltage benchtop RLC/inverter analog may be used if needed.

### Local observable

For a licensed local/inter-area electromechanical mode:

[
χ_i = -rac{Re(lambda_i)}{|lambda_i|}
]

for a complex-conjugate continuous-time mode, or the equivalent damping-ratio representation used by the native grid model.

### Broader Χ representation

Preserve:

- mode shapes;
- generator/bus participation;
- cross-site coherence;
- network coupling/topology;
- disturbance location;
- modal energy redistribution;
- load/generation context;
- uncertainty and mode-identification confidence.

Again, no master scalar is presumed.

### Manipulations

Real-grid topology cannot be manipulated experimentally for SymC. Therefore:

1. use archived real disturbances as observational tests;
2. use a frozen simulation model to intervene on line topology/coupling, inertia/damping distribution and disturbance location while holding focal local modal parameters as closely matched as possible;
3. if useful, reproduce a reduced analogue with coupled RLC/inverter nodes at safe voltage.

### Controls

- local-only autoregressive/modal predictor;
- standard Prony/matrix-pencil/system-identification baseline;
- network model without the candidate broader Χ features;
- matched disturbance magnitude/location where possible;
- topology intervention in simulation with exact known truth.

### Decisive observation

The key test is whether two states with similar local damping ratio but different network mode participation/topology have predictably different local disturbance recovery, and whether adding network architecture improves held-out recovery prediction.

### Falsifier

- network variables add no predictive information once local mode and forcing are known;
- gains arise only from data leakage or disturbance magnitude;
- a simpler standard network/modal model contains all apparent Χ information.

### Feasibility

HIGH computationally because an existing grid program and data pipeline exist; MEDIUM for safe benchtop analogue.

### Claim ceiling

Evidence about local-versus-embedded stability in a large engineered network. Because this shares second-order modal mathematics with the mechanical test, it is treated primarily as a **scale and natural-system transport test**, not a fully independent mechanism for cross-domain generality.

---

## E1-D. Optional neuro-perturbational expansion candidate

**Direct TMS/EEG experiment locally:** NOT_CURRENTLY_FEASIBLE.  
**Open perturbational data:** candidate, pending source qualification.

### Native question

Does whole-network brain state before a perturbation alter the subsequent local oscillatory recovery beyond a local pre-perturbation dynamical coordinate?

### Local observable

A scalar χ is admitted only if the post-perturbation local/source-resolved response contains a stable identifiable second-order oscillatory factor under representation checks. Otherwise retain the mode/pole pair without calling it χ.

### Broader Χ representation

Whole-brain mode/connectivity architecture, source participation, state/context, and uncertainty.

### Perturbation

TMS or other controlled perturbation with repeated trials/conditions.

### Decisive observation

Pre-perturbation Χ improves out-of-sample prediction of local post-stimulus recovery after local pre-state is known, or local dynamics predict subsequent network reorganization beyond prior network state.

### Disposition

Do not activate beyond source/literature qualification until a sufficiently open perturbational dataset and native comparator are identified.

---

## Cross-test prediction classes

Across every activated testbed, preserve all outcomes:

1. **LOCAL_SUFFICIENT:** χ/local mode predicts as well as χ+Χ.
2. **SYSTEM_CONDITIONS_LOCAL:** Χ adds held-out information about local future behavior.
3. **LOCAL_CONDITIONS_SYSTEM:** local χ adds held-out information about Χ evolution.
4. **BIDIRECTIONAL_COMPLEMENTARITY:** both directions add information.
5. **REDUNDANT_REPRESENTATIONS:** both encode the same predictive information.
6. **INTERACTION_ONLY:** neither alone is adequate but their interaction adds value.
7. **REPRESENTATION_DEPENDENT:** conclusion changes with justified representation.
8. **SCALAR_REFUSED_SYSTEM_USEFUL:** no defensible scalar χ, while modal/system architecture remains informative.
9. **BOTH_INADEQUATE:** neither representation predicts the target adequately.
10. **STANDARD_TOOLKIT_SUBSUMES:** a simpler/native method contains the predictive information without a distinct SymC contribution.

## Next step under GOM 50.2

This E1 file is intentionally preserved **before** targeted literature collision. E2 now searches prior experimental and methodological work for each testbed, credits existing answers, identifies known-truth testbeds, and isolates the residual question that remains worth executing.
