# GRID_RECOVERY_EPISODE_DEFINITION_AND_DEVELOPMENT_FINDINGS_v0.1_20261001.md

**Status:** P0-D DEVELOPMENT EVIDENCE — VALIDATION/HOLDOUTS SEALED  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01

## 1. Scientific unit correction

The q_entry detector produced 27,520 qualifying trigger runs in the 25–60% development segments.

Run-level re-excitation frequently occurred before sustained return. Therefore trigger runs are not treated as independent perturbation trials.

Define a **recovery episode** as:
- one initiating D_OR perturbation run;
- plus every subsequent D_OR run occurring before sustained pre-event return;
- ending at sustained pre-event return, 900-s horizon, or data-quality censor.

This collapses 27,520 trigger runs to **17,455 recovery episodes**.

The central history hypothesis will be tested between recovery episodes, while within-episode re-excitation remains part of the current episode's response.

## 2. Episode counts and internal repetition

| Grid | Episodes | Median runs/episode | Mean runs | Max runs | >1 run | >=3 runs |
|---|---:|---:|---:|---:|---:|---:|
| BALTIC | 1,221 | 1 | 1.189 | 7 | 14.0% | 2.9% |
| CONTINENTAL_EUROPE | 1,566 | 1 | 1.279 | 7 | 18.5% | 5.7% |
| GREAT_BRITAIN | 502 | 1 | 1.468 | 9 | 31.5% | 9.0% |
| ICELAND | 159 | 2 | 2.855 | 21 | 57.2% | 36.5% |
| MALLORCA | 13,617 | 1 | 1.638 | 25 | 34.5% | 13.6% |
| NORDIC | 80 | 1 | 1.162 | 4 | 12.5% | 2.5% |
| WESTERN_INTERCONNECTION | 310 | 1 | 1.542 | 7 | 31.3% | 14.5% |

Iceland demonstrates why trigger-run count cannot be interpreted as repeated independent failure: median episode contains two detector runs, but 98.7% of episode chains ultimately reach sustained pre-event return.

## 3. Episode-level finite-time outcome

Final sustained pre-event return fractions in development:

- BALTIC: 99.92%
- CONTINENTAL_EUROPE: 99.74%
- GREAT_BRITAIN: 91.04%
- ICELAND: 98.74%
- MALLORCA: 99.29%
- NORDIC: 98.75%
- WESTERN_INTERCONNECTION: 99.68%

Median episode duration:
- BALTIC 25 s
- CONTINENTAL_EUROPE 29 s
- GREAT_BRITAIN 83 s
- ICELAND 67 s
- MALLORCA 42 s
- NORDIC 42 s
- WESTERN_INTERCONNECTION 40 s

These are development descriptions only. They are not normal/abnormal thresholds.

## 4. Local stabilization without pre-event return

At least one local sustained-return state without pre-event sustained return occurred in:

- BALTIC 2.62% of episodes
- CONTINENTAL_EUROPE 4.28%
- GREAT_BRITAIN 18.73%
- ICELAND 2.52%
- MALLORCA 7.51%
- NORDIC 0%
- WESTERN_INTERCONNECTION 3.87%

This is direct evidence that "locally settled" and "returned to the previous baseline" are not equivalent empirical outcomes.

No physical interpretation is promoted from this observation alone.

## 5. Great Britain forcing investigation

Great Britain contains 44 horizon-censored development episodes.

All 44 achieved sustained local stabilization while failing to regain sustained pre-event return within the episode/horizon framework.

For these episodes:
- median local stabilization time is about 70.5 s;
- median absolute endpoint baseline migration is about 6.88 frozen residual-scale units;
- endpoint migration is about 120 mHz at the GB development scale.

The episodes are enriched near half-hour clock boundaries.

Relative to all other GB development episodes:

### Within 10 s of a half-hour boundary
- horizon episodes: 12/44 = 27.3%
- other episodes: 28/458 = 6.1%
- Fisher odds ratio ~5.76
- two-sided Fisher p ~4.25e-5

### Within 30 s
- horizon episodes: 15/44 = 34.1%
- other episodes: 59/458 = 12.9%
- odds ratio ~3.50
- two-sided Fisher p ~5.91e-4

This is development evidence for a scheduled/exogenous forcing confound.

It does **not** imply all GB baseline-migration episodes are market-caused and does not convert clock time into a causal mechanism by itself.

## 6. Consequence for the recoverability hypothesis

Scheduled-time forcing enters the native current-state comparator rather than being excluded from the primary sample.

For GB, preserve at least:
- distance to nearest half-hour boundary;
- indicators within 10 s and 30 s of that boundary;
- UTC time-of-day.

This mirrors the program rule that identifiable forcing is a modeled covariate, not "noise."

Stable local return with pre-event baseline failure remains provisionally LOCAL_STABILIZATION_WITH_BASELINE_MIGRATION_P0D.

It is **not yet** promoted to stable reorganization, damage, hysteresis, or recovery failure.

## 7. Canonical development episode table

Local Popstop artifact:
GRID_RECOVERY_DEVELOPMENT_EPISODES_v01.csv

SHA-256:
0b32b5f5bbbd7a7fa0ea233c58ffee2e7ee5af9ab73e058284c5ef7cd842224c

It contains only 25–60% recovery-development evidence.

Internal validation, temporal holdout, within-grid replication holdouts, ERCOT, Gran Canaria, and Russia remain unopened.

## 8. Next scientific gate

Freeze and synthetically qualify the episode-level current-state versus history model before fitting real development outcomes:

- M0: current native state + current perturbation + operating-time/forcing + clustering context;
- M2: M0 + prior perturbation/recovery burden.

History earns support only if M2 improves frozen out-of-sample recovery scoring beyond M0 and survives the prespecified alternative explanations.
