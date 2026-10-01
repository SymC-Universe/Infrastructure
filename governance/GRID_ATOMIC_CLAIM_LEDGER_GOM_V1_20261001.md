# GRID_ATOMIC_CLAIM_LEDGER_GOM_V1_20261001.md

**Status:** ACTIVE P0-D / P0-N AUDIT  
**Parent record:** WORKING_INVESTIGATION.md  
**Branch:** grid-revalidation-2026-10-01  
**Historical source set:** SymC_GridCon.tex; SymC_GridConSupmats.tex

Historical wording is preserved as a claim inventory only. Dispositions are provisional until the linked evidence lane closes.

## Status vocabulary

NATIVE_ESTABLISHED; MODEL_IDENTITY_SCOPE_LIMITED; EMPIRICALLY_SUPPORTED_CURRENT_SCOPE; RETROSPECTIVE_UNVERIFIED; OVERSTATED; CONTRADICTED_OR_WRONG; HYPOTHESIS_TESTABLE; NON_IDENTIFIABLE_WITH_CURRENT_DATA; REFUSED; PENDING_SOURCE_AUDIT.

## A. Native mathematics and representation

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-M01 | A linearized electromechanical mode can be written in a second-order damped form. | NATIVE_ESTABLISHED | Valid for an appropriate local/modal reduction such as the linearized swing equation. It does not imply the entire grid is one oscillator. |
| G-M02 | Every transmission line, generator and load is governed by the same scalar second-order equation. | CONTRADICTED_OR_WRONG | Grid models are multi-state, network-coupled, controller-dependent and include algebraic constraints and multiple stability classes/timescales. |
| G-M03 | χ = D/(2√(MK)) is a damping ratio for a properly reduced second-order mode. | NATIVE_ESTABLISHED | Standard identity when M,D,K belong to the same licensed modal reduction. |
| G-M04 | For λ=-σ±jωd, χ=σ/abs(λ). | MODEL_IDENTITY_SCOPE_LIMITED | Correct if σ>0 denotes positive decay rate. If σ=Re(λ)<0, use -Re(λ)/abs(λ). Historical code convention must be recovered. |
| G-M05 | χ=1 gives a repeated real root in the ideal scalar second-order oscillator. | NATIVE_ESTABLISHED | Algebraic identity in that model. |
| G-M06 | The repeated-root point at χ=1 is automatically a physical power-grid exceptional point. | OVERSTATED | A companion matrix can be defective at critical damping, but a physical EP claim requires operator definition, eigenvector/eigenspace coalescence, continuation and perturbation evidence. |
| G-M07 | Eigenvalue sensitivity diverges as the scalar repeated-root point is approached. | MODEL_IDENTITY_SCOPE_LIMITED | True for the stated algebraic branch; it does not establish a network-level singular response. |
| G-M08 | p(i,k)=abs(phi(i,k))^2/sum(abs(phi(i,j))^2) is a standard modal participation factor. | CONTRADICTED_OR_WRONG | Standard small-signal participation factors use paired left/right eigenvector information. The historical formula is closer to normalized right-mode-shape magnitude absent special conditions. |
| G-M09 | A regional/grid χ can be formed by weighted averaging of modal χ_i. | HYPOTHESIS_TESTABLE | No preservation theorem has been established. Requires information-loss tests against the full modal/network object. |
| G-M10 | For two real poles forming one second-order factor, χ=-(λ1+λ2)/(2√(λ1λ2)). | MODEL_IDENTITY_SCOPE_LIMITED | Algebraically valid for a legitimate paired second-order factor, not an arbitrary real-pole pairing rule. |
| G-M11 | As synchronizing stiffness Ps approaches zero with finite damping in the scalar swing reduction, χ approaches infinity. | MODEL_IDENTITY_SCOPE_LIMITED | Follows from the scalar formula, but does not make large χ a universal whole-grid stiffness-collapse diagnostic. |
| G-M12 | Dvirt=2√(Jvirt Ps) is the universal correct GFM/VSM damping law. | OVERSTATED | It is a critical-damping condition for a simplified second-order control model, not a universal optimum for multi-loop converter/network dynamics. |
| G-M13 | Local modal damping alone is the whole-grid stability coordinate. | REFUSED | Refused absent system derivation and information-loss analysis. |
| G-M14 | Broader grid stability must preserve modes, mode shapes/participation, coupling, topology, operating state, uncertainty and refusal structure. | NATIVE_ESTABLISHED | This is the present representation requirement for Χ; the exact native object remains analysis-specific. |
| G-M15 | χ_i, modal/vector Χ and system/conglomerate Χ_arc are interchangeable. | CONTRADICTED_OR_WRONG | Current notation and GOM architecture explicitly prohibit this collapse. Their relationship is a research target. |

## B. Universal-boundary and substrate claims

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-U01 | The electrical grid operates near a universal χ≈1 boundary independent of topology, size and generation mix. | RETROSPECTIVE_UNVERIFIED | Historical numerical support lacks reconstructed raw provenance and a licensed whole-grid scalar. |
| G-U02 | Real grids universally occupy χ≈0.8–1.0. | RETROSPECTIVE_UNVERIFIED | Historical figures/statistics are not source-bound; mode and task dependence must be tested. |
| G-U03 | χ≈1 is not a design choice but physical necessity. | OVERSTATED | Critical damping is one regime of a second-order model, not a demonstrated universal necessity for stable grids. |
| G-U04 | Stable/adaptive systems converge toward critical damping because it optimizes information flow and reversibility. | HYPOTHESIS_TESTABLE | No native grid derivation or validated optimization functional recovered. |
| G-U05 | Grid behavior near χ≈1 is inherited from electromagnetic/electron physics through transmission, generation, controls and markets. | REFUSED | No carrier map or causal derivation recovered. Similar mathematical forms do not establish inheritance. |
| G-U06 | Stable higher layers require every lower layer to share χ≈1. | CONTRADICTED_OR_WRONG | Coupled/hierarchical stability does not generally require identical scalar damping ratios at all layers. |
| G-U07 | Electron identity invariance makes the electron scale the privileged substrate for grid stability. | OVERSTATED | Electron identity does not establish causal relevance to electromechanical modal stability. |
| G-U08 | Lattice defects/electron microvariations are the source of operational grid precursors. | NON_IDENTIFIABLE_WITH_CURRENT_DATA | PMU/FNET observables do not resolve the asserted microscopic carrier. |
| G-U09 | Markets inherit the same physical critical-damping constraint from the electromagnetic substrate. | REFUSED | No native causal bridge has been established. |

## C. Measurement, modal extraction and data claims

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-D01 | PMU/FNET/ringdown data can support electromechanical mode estimation. | NATIVE_ESTABLISHED | Established use case subject to observability, signal quality and estimator assumptions. |
| G-D02 | A 30 s Prony window with L=15 is generally appropriate. | RETROSPECTIVE_UNVERIFIED | Historical text says AIC validation, but code/output is not recovered. |
| G-D03 | abs(df/dt)>0.05 Hz/s is a validated universal event trigger. | RETROSPECTIVE_UNVERIFIED | Exact source, training set and transport evidence unresolved. |
| G-D04 | Residual error <0.05 and SNR>20 dB are universally valid QC thresholds. | RETROSPECTIVE_UNVERIFIED | Need method calibration and sensitivity analysis. |
| G-D05 | >80% PMU coverage of major nodes is required for accurate field construction. | RETROSPECTIVE_UNVERIFIED | No reconstructed derivation; major nodes is undefined. |
| G-D06 | PMUs measure the electron-scale substrate state through χ. | CONTRADICTED_OR_WRONG | PMUs measure synchronized electrical quantities; microscopic interpretation would be indirect and model-dependent. |
| G-D07 | FO/TX/UT 1500+ real points validate a universal χ attractor. | RETROSPECTIVE_UNVERIFIED | Raw identities, labels, extraction code and uncertainty are not located. |
| G-D08 | UK field data contain 2,847 snapshots and 47 independent validation events. | RETROSPECTIVE_UNVERIFIED | Exact dataset/event provenance and independence are unresolved. |
| G-D09 | Stable χ=0.82±0.11 vs event χ=0.43±0.18, t=8.7, p<0.001. | RETROSPECTIVE_UNVERIFIED | Printed statistic is not reproduced evidence; sampling unit/dependence/code unresolved. |
| G-D10 | Stable/event separation has Cohen d=2.3. | RETROSPECTIVE_UNVERIFIED | Same provenance issue and requires arithmetic/sample-definition check. |
| G-D11 | The lifecycle experiment was an 83-hour run with events through t=8900 min. | CONTRADICTED_OR_WRONG | Internal contradiction: 83 h=4,980 min; 8,900 min≈148.3 h. |
| G-D12 | Fifty 20–30 h simulation runs establish field behavior. | OVERSTATED | Simulation is synthetic evidence and cannot establish field prevalence. |

## D. Early-warning and prediction claims

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-P01 | Grid degradation is detectable 60–100+ minutes before cascade. | RETROSPECTIVE_UNVERIFIED | Needs frozen prospective rule, independent events, event-time definition, base-rate accounting and native comparator performance. |
| G-P02 | Cross-timescale Δχ divergence is a direct degradation signal. | HYPOTHESIS_TESTABLE | Could encode changing spectral/modal structure, but direct physical interpretation is unestablished. |
| G-P03 | abs(Δχ)>0.2 sustained >5 min is a validated precursor threshold. | RETROSPECTIVE_UNVERIFIED | Historical threshold was ROC-optimized and cannot be reused as untouched confirmation. |
| G-P04 | χ=0.60 is a validated early-warning crossing. | RETROSPECTIVE_UNVERIFIED | Same leakage/transport issue. |
| G-P05 | The method achieves 89% sensitivity, 98% specificity and 127 min lead time. | RETROSPECTIVE_UNVERIFIED | Confusion matrix, prevalence, tuning history and raw predictions not recovered. |
| G-P06 | Standard monitoring misses the precursor information detected by SymC. | CONTRADICTED_OR_WRONG | Native literature already contains modal monitoring, oscillation detection, dynamic-security and early-warning methods. Incremental value must be benchmarked. |
| G-P07 | Baseline decay is invisible to variance/native methods. | OVERSTATED | Trend, change-point and state-estimation methods can test baseline change. |
| G-P08 | Precursor clustering forms a descending wedge toward bifurcation. | HYPOTHESIS_TESTABLE | Needs a defined statistic, null and independent-event test. |
| G-P09 | Better instrumentation/faster control should cluster systems closer to χ=1; legacy/noisy systems lower. | HYPOTHESIS_TESTABLE | Clear prospective prediction but currently unvalidated and potentially confounded by estimator bias. |
| G-P10 | A 30-second SymC Advantage exists in the illustrated reaction protocol. | RETROSPECTIVE_UNVERIFIED | Exact simulation/comparator and data-generating process must be reconstructed. |

## E. Damage, hysteresis, recovery and resilience claims

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-R01 | Baseline χ decay demonstrates irreversible physical substrate damage. | OVERSTATED | Finite-time non-return does not establish irreversibility; separate slow recovery, dispatch/topology/control change, reorganization and measurement drift. |
| G-R02 | Permanent post-event shifts of 1–3% are validated. | RETROSPECTIVE_UNVERIFIED | Raw longitudinal evidence is not recovered. |
| G-R03 | Offset >0.01 persisting >1 h proves hysteresis/irreversible damage. | CONTRADICTED_OR_WRONG | One hour persistence can define finite-time non-recovery, not irreversibility. |
| G-R04 | Early Tier 1–2 intervention restores substrate elasticity. | RETROSPECTIVE_UNVERIFIED | Requires intervention-specific counterfactual/control evidence. |
| G-R05 | Late Tier 3 intervention prevents collapse but leaves permanent damage. | RETROSPECTIVE_UNVERIFIED | Requires controlled evidence and measurable damage endpoint. |
| G-R06 | No intervention leads to irreversible cascade. | OVERSTATED | Not every stressed state cascades; natural recovery/operator actions must be represented. |
| G-R07 | Recovery constants 8±3, 14±4 and 18±5 min are established by event size. | RETROSPECTIVE_UNVERIFIED | Source data/code and event independence not recovered. |
| G-R08 | Pristine baseline remains χ=1.00±0.02 after 15+ disturbances. | RETROSPECTIVE_UNVERIFIED | Appears simulation-derived and may be built into initial/control assumptions. |
| G-R09 | Stability and recovery are the same property. | REFUSED | GOM requires resistance, response, first reclaim, sustained recovery, reorganization, basin robustness and repeated-event behavior to be separated where relevant. |

## F. Inertia, IBR, strength and failure taxonomy

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-I01 | As IBR penetration approaches 100%, system inertia necessarily approaches zero. | OVERSTATED | Synchronous kinetic inertia can decrease, but converter controls/storage/GFM resources alter fast frequency response and the relevant state model. |
| G-I02 | As Hsys approaches zero, RoCoF necessarily tends to infinity. | OVERSTATED | Simplified balance predicts increasing initial RoCoF for fixed imbalance absent fast control, but real response depends on controls, limits, network and timescale. |
| G-I03 | H>3 s safe, 1–3 s yellow, <1 s red is universal. | REFUSED | System- and contingency-dependent historical bands are frozen from reuse. |
| G-I04 | SCR>3 safe, 2–3 yellow, <2 red is universal. | REFUSED | SCR definitions/thresholds are context-specific. |
| G-I05 | SCR<1.5 uniquely diagnoses stiffness collapse. | OVERSTATED | No universal collapse theorem follows from that scalar threshold. |
| G-I06 | Series compensation should be adjusted to increase SCR during Tier 2. | OVERSTATED | Not a generic real-time prescription; protection/SSR/network consequences require native study. |
| G-I07 | Negative total damping can create growing oscillatory modes and Hopf-type instability. | NATIVE_ESTABLISHED | General local-modal concept is valid; exact Hopf claim needs nonlinear-system/parameter-path evidence. |
| G-I08 | Subsynchronous electrical/mechanical resonance can reduce effective damping. | NATIVE_ESTABLISHED | Established native phenomenon, not unique to SymC. |
| G-I09 | Stiffness collapse, controller failure and impedance mismatch form a complete grid failure taxonomy. | CONTRADICTED_OR_WRONG | Native power-system stability/failure modes are broader. |

## G. Operational tiers and interventions

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-O01 | Tier 0–4 can be assigned directly from historical χ bands. | REFUSED | No operational use before prospective task-specific validation and transport testing. |
| G-O02 | χ≥0.8 is universally nominal/healthy. | REFUSED | Modal damping and security are mode/system/task dependent. |
| G-O03 | 0.70≤χ<0.80 universally means substrate softening. | REFUSED | Mechanistic label and threshold unsupported. |
| G-O04 | 0.60≤χ<0.70 universally means irreversible inheritance onset. | REFUSED | Unsupported threshold and mechanism. |
| G-O05 | χ<0.60 universally means imminent bifurcation. | REFUSED | No universal mapping from one damping coordinate to all grid bifurcations. |
| G-O06 | Activate PSS on all synchronous generators when Tier 1 triggers. | CONTRADICTED_OR_WRONG | PSS configuration/tuning is unit-specific; blanket activation is not a safe generic rule. |
| G-O07 | Increased damping/commitment actions may improve a mode under selected conditions. | HYPOTHESIS_TESTABLE | Plausible action class but trigger/action efficacy must be tested natively. |
| G-O08 | Tier 2 should trigger 3–5% demand response. | REFUSED | Fixed amount has no validated universal basis. |
| G-O09 | Tier 3 should trigger 5–10% load shedding. | REFUSED | Emergency shedding must be system/contingency specific and protection/security validated. |
| G-O10 | Monitoring should shift to 5–10 min or 2–3 min by tier. | OVERSTATED | PMUs operate much faster; aggregation and decision cadence are separate design problems. |
| G-O11 | Weak regions cannot borrow stability from strong regions. | CONTRADICTED_OR_WRONG | Interconnected regions exchange synchronizing/damping support through network coupling. |
| G-O12 | Damping resources must be allocated proportional to regional χ deficit. | HYPOTHESIS_TESTABLE | Requires control optimization and comparison with modal sensitivity/participation methods. |
| G-O13 | No single damping source should provide >50% of system damping. | RETROSPECTIVE_UNVERIFIED | Appears arbitrary absent reliability/control optimization evidence. |
| G-O14 | Control authority at every relevant timescale is useful design language. | MODEL_IDENTITY_SCOPE_LIMITED | Sensible framing, but it does not validate the old timescale bands or thresholds. |
| G-O15 | Real-time χ can replace native stability margins. | OVERSTATED | Incremental value must be demonstrated over accepted security/modal measures. |

## H. Redundancy and lifecycle claims

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-L01 | Multiple independent substrates with automated transfer maintain stability indefinitely. | CONTRADICTED_OR_WRONG | Indefinitely cannot be established by finite simulations and ignores common-mode failure, resource limits and maintenance. |
| G-L02 | Dynamic redundancy achieves what classical N-1 cannot. | OVERSTATED | N-1 is a contingency-security criterion, not a theorem of unlimited resilience or elastic recovery. |
| G-L03 | Redundancy can be framed as multiple independent routes to restore desired dynamic behavior rather than merely spare MW. | HYPOTHESIS_TESTABLE | Potentially useful if translated into native reliability/control metrics. |
| G-L04 | Spatial/timescale/damping diversity may improve robustness to single-controller failure. | HYPOTHESIS_TESTABLE | Likely overlaps established reliability/control concepts; novelty depends on prior-art conglomeration. |

## I. Bibliography/source claims

| ID | Historical claim | Provisional disposition | Audit finding |
|---|---|---|---|
| G-C01 | DOI 10.1016/j.ijepes.2017.12.012 supports the cited Phadke/Thorp PMU/WAMS article. | CONTRADICTED_OR_WRONG | DOI maps to a wind-power forecast-error/energy-storage sizing paper. |
| G-C02 | DOI 10.1109/TPWRS.2006.873125 supports the cited Zhou/Pierre/Hauer ambient-identification article. | CONTRADICTED_OR_WRONG | DOI maps to A maximum loading margin method for static voltage stability in power systems. A different Zhou/Pierre/Hauer 2006 identification paper has DOI 10.1109/TPWRS.2006.879292; intended source still requires exact matching. |
| G-C03 | DOI 10.1103/PhysRevE.87.042909 supports the cited Early warning signals for critical transitions in power systems by Weckesser/Rohden/Beck/Witthaut. | CONTRADICTED_OR_WRONG | Historical title/authors/DOI mapping is wrong. The verified power-system paper with that title is Hui Ren & David Watts, EPSR 124 (2015), DOI 10.1016/j.epsr.2015.03.009, and is simulation-based. |
| G-C04 | Hauer/Demeure/Scharf 1990 Prony citation DOI 10.1109/59.49090 is correctly identified. | NATIVE_ESTABLISHED | Bibliographic match verified. |
| G-C05 | Rohden/Sorge/Timme/Witthaut 2012 PRL DOI 10.1103/PhysRevLett.109.064101 is correctly identified. | NATIVE_ESTABLISHED | Bibliographic match verified; it concerns coarse oscillator-network synchronization, not universal χ≈1. |
| G-C06 | Dörfler/Bullo 2012 SIAM DOI 10.1137/110851584 is correctly identified. | NATIVE_ESTABLISHED | Bibliographic match verified; it concerns synchronization/transient-stability models, not substrate inheritance. |
| G-C07 | The historical bibliography can be used as-is. | REFUSED | Full title/author/year/venue/DOI/source-support matching is mandatory. |

## J. Residual questions that survive first triage

1. Does a licensed χ_i=-Re(λ_i)/abs(λ_i) add useful interpretability or cross-event comparability beyond native damping-ratio notation without losing essential information?
2. How do mode-specific χ_i values relate to modal/vector Χ and network/system Χ_arc, and when does scalar compression fail?
3. Can distribution/geometry changes in modal damping, participation and coupling distinguish operating-state change from genuine damping loss?
4. Does a preregistered cross-timescale architecture metric improve prediction beyond native modal damping, spectral/coherence features, frequency/ROCOF, change-point methods and dynamic-security measures on untouched events?
5. Do post-disturbance trajectories in modal/vector space reveal first reclaim, sustained recovery or reorganization that scalar damping alone misses?
6. As generation/control architecture changes, does the organization of damping/inertia/system-strength modes change reproducibly in ways Χ or Χ_arc capture beyond one scalar?
7. Under what operating conditions is no coherent scalar χ licensed, and is refusal itself informative?
8. Are any modal/vector patterns transportable across grids after controlling topology, estimator, event type and operating state, without asserting a universal optimum?

## Current ceiling

The historical work contains legitimate native pieces, especially local swing-mode damping mathematics and PMU/ringdown modal identification. The principal failures arise when those pieces are promoted into a universal whole-grid scalar, microscopic inheritance mechanism, retrospective predictor, irreversible-damage theory, fixed operational doctrine or indefinite-lifecycle claim without the required evidence chain.

Next gate: complete source/provenance reconstruction and the native prior-art/comparator map before selecting confirmatory targets.
