# SymC χ <-> Χ cross-domain experimental expansion: E2 literature collision

**Date:** 2026-09-21  
**Status:** P0-D / E2 LITERATURE COLLISION  
**E1 source:** `research/CHI_CAPITALCHI_CROSS_DOMAIN_EXPERIMENT_E1_20260921.md`  
**Rule:** prior work is credited even where the experiment was independently sketched. The residual question, not the original idea, is what proceeds.

## Status

The broad statement "system context can change the realized response of a local component" is **not novel as a generic principle**. Strong versions are already established in mechanics, neuroscience, and power systems. That is useful: those domains can serve as known-truth calibration testbeds for the χ<->Χ analysis rather than being used to manufacture novelty.

The residual cross-program question is narrower and more demanding:

> Can a common, non-circular joint-meaning protocol determine when a licensed local χ is sufficient, when broader Χ adds held-out information, when local χ adds information about future system organization, when interaction is required, and when either representation must be refused?

The oncology question remains materially open under that formulation.

---

## E2-A. Mechanical networks

### Prior work collision

Experimental structural/metamaterial literature already demonstrates that local resonators, damping distribution, coupling, and host/modal architecture jointly determine realized vibration attenuation and modal dissipation.

**Van Belle et al. 2017, Journal of Sound and Vibration**  
DOI: `10.1016/j.jsv.2017.07.045`  
A damped locally resonant metamaterial model was experimentally validated. Damping changed dispersion/attenuation behavior of the coupled structure.

**Zhao et al. 2024, Mechanical Systems and Signal Processing**  
DOI: `10.1016/j.ymssp.2023.111079`  
Experimental nonlinear locally resonant metamaterial. The paper directly discusses interaction between local resonators and host mode shapes and reports modal frequency dissipation and broadened attenuation.

**Mode-localization coupled-resonator literature** also experimentally shows that coupling strength, perturbation location, and damping distribution alter the response of individual resonators within a coupled system.

### Classification

`KNOWN_TRUTH_TESTBED + METHOD_AVAILABLE + GENERIC_PHENOMENON_ALREADY_ANSWERED`

### Residual question

Do not claim discovery that coupling matters. Use the benchtop network to validate the SymC joint-meaning machinery under a system where the governing equations are known:

- can the procedure recover that identical isolated χ does not imply identical embedded response?
- does the local-only model lose exactly the information carried by coupling/mode participation?
- does the method refuse a scalar when overlapping modes destroy a defensible local second-order factor?
- can Function and Limit maps identify when local χ is sufficient versus insufficient?

This becomes a **calibration experiment**, not a novelty experiment.

---

## E2-B. SCC25 cetuximab resistance

### Prior work collision

**Stein-O'Brien et al. 2018, Genome Medicine**  
PMID: `29792227`  
The exact SCC25 experiment collected RNA-seq and DNA methylation weekly during cetuximab resistance development and analyzed temporal molecular programs with CoGAPS. The source therefore already establishes that transcriptional and methylation organization evolve across treatment/resistance.

**Velten et al. 2022, Nature Methods, MEFISTO**  
DOI: `10.1038/s41592-021-01343-9`  
MEFISTO provides an established time-aware multi-view latent-factor method for multimodal temporal data, including shared/smooth temporal variation across views/groups.

### Classification

`PARTIALLY_ANSWERED + NATIVE_METHOD_AVAILABLE + RESIDUAL_QUESTION_IDENTIFIED`

### What is already answered

- SCC25 resistance is temporally structured.
- RNA and methylation do not remain static.
- multi-view temporal latent-factor methods already exist.
- CoGAPS is source-native prior art for evolving molecular-program description.

### Residual question

The source literature does **not** answer the specific joint-information question:

> conditional on the best defensible local/modal dynamical information, does broader RNA+methylation+modal/system organization improve held-out prediction of the next local state or external phenotype, and does local dynamics reciprocally improve prediction of broader architecture?

Nor does prior work establish a scalar biological χ. The scalar branch must earn or refuse admission.

This remains a live GRI/SymC investigation.

---

## E2-C. Brain perturbation / state-dependent stimulation

### Prior work collision

This domain contains an unusually direct empirical analogue of the proposed Χ -> local-response hypothesis.

**Bai, Xuan, Jia & Ziemann 2023, Brain Stimulation**  
DOI: `10.1016/j.brs.2023.10.008`  
In 24 healthy subjects, transient large-scale EEG network states before TMS changed the induced local/natural oscillatory response. State-locked stimulation increased alpha/beta response properties relative to state-unlocked trials.

**Rabuffo et al. 2026, Brain Stimulation**  
DOI: `10.1016/j.brs.2026.103118`, PMID `42144100`  
Across 36 epilepsy patients, about 320 sessions and >10,000 single-pulse stimulations, pre-stimulus brain dynamics predicted post-stimulation response. The published abstract reports that whole-brain measures outperformed local measures and that prospective closed-loop conditioning on favorable states reduced response variability.

The authors' public repository `grabuffo/State_Dependent_Brain_Stimulation` includes reproducibility notebooks, derived metrics, out-of-sample prediction analyses, radius-dependence analyses, network-dependence analyses, and prospective closed-loop analyses. The underlying data are reported as available through EBRAINS/OSF.

### Classification

`GENERIC_HYPOTHESIS_STRONGLY_ANSWERED + OPEN_KNOWN_TRUTH_DATASET + RESIDUAL_REPRESENTATION_QUESTION`

### Consequence

The statement

> broader system state can improve prediction/control of local response

already has direct neuroscientific empirical support and cannot be claimed as uniquely SymC.

This is valuable because the public dataset can test whether the χ<->Χ protocol recognizes the effect without being told the authors' preferred interpretation.

### Residual question

- can a licensed local oscillatory χ be extracted at all from the local post/pre-stimulus dynamics?
- does a χ-based local representation retain information beyond the source paper's conventional local metrics?
- does broader Χ add information beyond that local χ under the same train/test split?
- does the SymC joint protocol add anything over the source-native state metrics and standard predictive methods?

If not, outcome is `STANDARD_TOOLKIT_SUBSUMES`, which is scientifically useful.

---

## E2-D. Power-grid network embedding

### Prior work collision

**Chen et al. 2011, IEEE PES / CERTS**  
DOI: `10.1109/PES.2011.6039904`  
WECC studies showed that topology changes can alter inter-area oscillation modes, mode shapes, damping, and small-signal stability. The source explicitly argues that topological information can improve control accuracy/effectiveness.

**SSI/PMU and wide-area-control literature** demonstrates that inter-area mode frequency, damping, mode shape, observability, and participation are network-distributed objects rather than properties of a single local measurement.

### Classification

`GENERIC_PHENOMENON_ALREADY_ANSWERED + SCALE_TRANSPORT_TESTBED`

### Residual question

The grid should not be used to claim that embedding matters. That is established.

Use it instead to test:

- whether a local damping-ratio representation is sufficient in some operating regimes and not others;
- whether mode shape/participation/topology adds held-out information about local disturbance recovery;
- whether the joint protocol finds the same Function/Limit boundary as native power-system methods;
- whether standard PMU/modal methods fully subsume the proposed capital-Χ representation.

Because the grid and mechanical network share second-order modal structure, grid evidence counts primarily as **scale/natural-network transport**, not a wholly independent mechanism.

---

## Cross-domain adjudication after literature collision

### Broad proposition

`SYSTEM_CONTEXT_CAN_CONDITION_LOCAL_RESPONSE = PRIOR_ART_SUPPORTED_ACROSS_MULTIPLE_DOMAINS`

This is not yet a universal law. The evidence spans materially different systems, but each source uses its own native variables and boundary conditions.

### SymC residual proposition

`JOINT_CHI_CAPITALCHI_INFORMATION_STRUCTURE = ACTIVE_P0_D_QUESTION`

The residual proposition is not that context matters. It is whether the SymC architecture provides a useful and falsifiable way to determine:

1. what local χ/local modal dynamics contain;
2. what broader Χ contains beyond them;
3. how much predictive information flows conditionally in each direction;
4. whether their interaction is synergistic, redundant, representation-dependent, or absent;
5. when scalar χ stops being a defensible or sufficient reduction;
6. whether the same protocol transports across domains without overriding native methods.

## Immediate experiment ordering

1. **Mechanical known-truth simulation -> benchtop.** Cheapest causal calibration with known equations.
2. **Brain open-data reproduction.** Strongest published direct analogue of Χ conditioning local response; test against source-native metrics before inventing a SymC advantage.
3. **SCC25 joint-analysis freeze and pilot.** Primary biological discovery target because the exact conditional χ<->Χ question remains open.
4. **Grid transport check.** Test scale and operational-system transport after the joint protocol is stable.

This ordering minimizes the chance that oncology teaches the analysis what answer to find.
