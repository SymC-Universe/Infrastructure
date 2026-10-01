# GRID_CLEAN_SHEET_PRIOR_ART_ATLAS_v0.1_20261001.md

**Status:** P0-N ACTIVE PRIOR-ART CONGLOMERATION  
**Branch:** grid-revalidation-2026-10-01  
**Parent:** WORKING_INVESTIGATION.md  
**Scope:** clean-sheet power-grid stability investigation; historical SymC grid paper has no privileged scientific status.

## 1. Current prior-art result

The modern literature does not support treating power-system stability as one universal scalar. The active field already distinguishes multiple stability classes, modal families, operating-state dependencies, converter-driven interactions, transient amplification, recovery/resilience behavior, and frequency-dependent network-control effects.

Therefore the new investigation should not ask whether one scalar replaces power-system stability. The stronger residual question is whether a joint architecture of local/modal damping, spatial/modal structure, participation/observability, network coupling, non-normal transient amplification, operating state, and cross-timescale organization provides reproducible information that conventional summaries miss.

## 2. Major occupied territories

### A. Stability taxonomy and native state space
Foundational and modern references include Kundur et al. 2004, DOI 10.1109/TPWRS.2004.825981, and Hatziargyriou et al. 2021, DOI 10.1109/TPWRS.2020.3041774.

Implication: stability is already explicitly multi-category and system/trajectory dependent. Any proposed architecture must sit on top of this taxonomy, not overwrite it.

### B. Modal identification and oscillation monitoring
Established methods include eigenanalysis, Prony, matrix pencil, ERA, stochastic-subspace/ambient identification, multichannel mode estimation, mode meters, forced-oscillation detection, and source-location methods.

Key references include:
- Hauer, Demeure, Scharf 1990, DOI 10.1109/59.49090.
- Pierre, Trudnowski, Donnelly 1997, DOI 10.1109/59.630467.
- Trudnowski et al. 2008, DOI 10.1109/TPWRS.2008.919415.
- Almunif, Fan, Miao 2020, DOI 10.1002/2050-7038.12283.
- Agrawal et al. 2019, DOI 10.1109/TPWRS.2018.2876128.
- Trudnowski et al. 2025, DOI 10.1109/ACCESS.2025.3543457.

Implication: a new χ_i notation by itself is not novel. Any contribution must show incremental scientific value beyond native damping-ratio/modal representations.

### C. Participation, mode shapes and coupling
Participation factors, mode shapes, selective modal analysis, coherency, and dynamic equivalents already retain information discarded by scalar damping.

Implication: any capital Χ/modal-vector construct must be compared directly with native left/right-eigenvector participation, observability, coherency, residues, sensitivities and related modal objects.

### D. Early warning and critical-transition literature
Relevant literature includes:
- Sanchez, Hines, Danforth 2012, DOI 10.1109/TSG.2012.2213848.
- Ghanavati, Hines, Lakoba 2014/2015, DOI 10.1109/TPWRS.2015.2412115.
- Follum, Holzer, Etingov 2021, DOI 10.1016/j.ijepes.2020.106685.
- Xie, Chen, Kumar 2014, DOI 10.1109/TPWRS.2014.2316476.
- Ren, Watts 2015, DOI 10.1016/j.epsr.2015.03.009.

Current literature picture: event detection and oscillation alarming have field/control-room implementations, but broad prospective warning of instability remains far less mature than retrospective/simulation studies.

Implication: any new warning claim must use frozen thresholds, untouched events, explicit base rates/false alarms, and direct comparison with native detectors.

### E. Recovery and resilience
The literature treats resilience, reliability, robustness, outage/restore curves, nadir, duration, restoration rates and area-under-curve metrics as related but distinct.

Implication: the GOM separation of resistance, response, first reclaim, sustained recovery, reorganization, basin robustness and repeated events is scientifically compatible with a genuine open gap: these distinctions are not yet standardized in modal state space.

### F. IBR, low-inertia and grid-forming systems
Key references include:
- Gu, Green 2023, DOI 10.1109/JPROC.2022.3179826.
- Markovic et al. 2021, DOI 10.1109/TPWRS.2021.3061434.
- Milano et al. 2018, DOI 10.23919/PSCC.2018.8450880.
- Tayyebi et al. 2020, DOI 10.1109/JESTPE.2020.2966524.
- Li, Gu, Green 2021/2022, DOI 10.1109/TPWRS.2022.3151851.
- Zhang et al. 2023, DOI 10.1109/OAJPE.2022.3230007.
- Henderson et al. 2024, DOI 10.1109/TPWRD.2022.3233455.
- Kouki, Marinescu, Xavier 2020, DOI 10.1109/TPWRS.2020.2969641.
- Fan 2022, DOI 10.1109/TPWRS.2021.3124667.
- Zhu et al. 2021, DOI 10.1109/TPWRS.2021.3088345.

Current literature picture: IBR-rich stability is not adequately described by penetration percentage, inertia, SCR, or damping alone. Control type, placement, current limits, network impedance, frequency band, topology, and modal coupling matter.

Implication: this domain is a strong testbed for a multivariate stability architecture, provided native impedance/modal methods remain the comparator floor.

### G. Non-normality, transient growth and pseudospectral structure
A major prior-art finding is that asymptotically stable eigenvalues can coexist with large finite-time transient amplification.

Relevant work includes Maldonado et al. 2023, arXiv:2302.10388, and Murillo-Aguirre & Roman-Messina 2024, DOI 10.1109/ACCESS.2024.3471495.

The latter explicitly studies modal coalescence, repeated-eigenvalue proximity, matrix nearness, pseudospectra, modal coupling and transient-energy growth in power systems.

Implication: any future EP/coalescence claim must be framed against this occupied power-system literature. A novel contribution cannot simply be "eigenvalues approach/coalesce near a boundary." The residual question is whether SymC's scalar/modal/system hierarchy adds a measurable relation or predictive object beyond pseudospectral distance, eigenvalue conditioning and transient-growth measures.

## 3. Strong residual questions after first pass

### RQ1 — Scalar sufficiency/refusal
When is a mode-specific damping coordinate sufficient for the scientific task, and when does it fail because different mode shapes, coupling, observability, non-normality or operating states produce materially different outcomes at similar damping values?

### RQ2 — Joint modal architecture
Can a structured Χ containing eigenvalues, mode shapes/participation, uncertainty, coupling and excitation identify reproducible state changes that native one-number damping summaries miss?

### RQ3 — Transient amplification
For stable spectra, does adding pseudospectral/non-normal transient-growth structure improve prediction of realized disturbance amplification relative to damping ratio alone?

### RQ4 — Recovery path
After a disturbance, does the trajectory through modal/vector state space distinguish first reclaim, sustained recovery and reorganization better than scalar damping or standard frequency metrics?

### RQ5 — IBR organization shift
As IBR/control composition changes, are there reproducible reorganizations of modal families, participation and coupling that are better represented by Χ or Χ_arc than by inertia/SCR/damping alone?

### RQ6 — Early warning incremental value
Does a prospectively frozen cross-timescale architecture statistic improve prediction over native event detectors, oscillation metrics, frequency/ROCOF, change-point statistics and dynamic-security measures on untouched events?

### RQ7 — Failure/refusal map
Can the study identify principled regimes in which no coherent scalar χ exists, and does that refusal correspond to known multi-mode, forced, non-normal or converter-coupled conditions?

## 4. Data-evidence implications

The Popstop data root contains approximately 12.17 GB across 79 files, including the KIT/OSF frequency dataset, 100-ms archives, quality metadata and multiple historical derived products.

The KIT source columns are frequency deviations from nominal in mHz. Historical window-builder code multiplied their time derivative by 1000 while retaining an mHz/s label, contaminating historical forcing/event derivative scales by 10^3.

This defect does not automatically invalidate historical modal χ outputs because a separate modal estimator was used. However, the saved historical products are not internally unique: the same 30-s EE01 window carries different mode counts and χ values in two historical derived datasets. Therefore all old modal products are provenance objects only until the estimator code path is reconstructed or the modes are freshly re-estimated from raw data.

## 5. Evidence capability boundary of current raw corpus

Frequency-only streams can support:
- frequency-deviation statistics,
- change points,
- spectral content,
- single-/multi-station frequency coherence where synchronized channels exist,
- data-driven modal/ringdown estimation where excitation and sampling support it,
- cross-timescale trajectory analysis,
- recovery and disturbance-response studies.

Frequency-only streams do not by themselves establish:
- bus-voltage/current phasor mode shapes,
- native state participation factors,
- topology-conditioned eigenvectors,
- impedance-based stability,
- microscopic electron-scale mechanisms,
- whole-network causal coupling.

Those questions require richer PMU/network/model datasets. The 2023 open-source PMU library and other public PMU/oscillation datasets should be evaluated as external complementary data sources.

## 6. Current novelty posture

No novelty claim is promoted yet.

The strongest provisional gap is not "power systems need modal analysis" and not "critical damping matters." Those are occupied.

The potentially defensible new space is a rigorously tested relationship among:
- local/modal damping coordinates,
- modal/vector organization,
- non-normal/transient-growth geometry,
- network/system organization,
- and disturbance/recovery trajectory,

with explicit refusal when scalar compression fails and with direct native-method comparison.

That is the target to sharpen through the next literature passes and data-capability audit.
