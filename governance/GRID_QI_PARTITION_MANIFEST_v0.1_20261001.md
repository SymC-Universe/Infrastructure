# GRID_QI_PARTITION_MANIFEST_v0.1_20261001.md

**Status:** COMPLETE — OUTCOME-BLIND PARTITION MANIFEST FROZEN  
**Date:** 2026-10-01  
**Branch:** grid-revalidation-2026-10-01  
**Recovery outcomes opened:** NO

## Corpus partition summary

The Popstop raw-source scan completed successfully before the remote session ended.

- raw campaigns scanned: **22**
- primary development campaigns: **7**
- within-grid replication holdouts: **8**
- external-grid holdout campaigns: **5**
- quality-limited campaigns: **2**

Development grids:
BALTIC, CONTINENTAL_EUROPE, GREAT_BRITAIN, ICELAND, MALLORCA, NORDIC, WESTERN_INTERCONNECTION.

External whole-grid holdouts:
ERCOT, GRAN_CANARIA, RUSSIA.

Quality-limited auxiliary grids:
FAROE_ISLANDS, SOUTH_AFRICA.

## Frozen temporal cuts

| Grid | Primary campaign | QI=0 valid rows | Development end (60%) | Internal validation end (80%) | Temporal holdout end |
|---|---|---:|---|---|---|
| BALTIC | EE01 | 1,974,144 | 2019-04-08 04:11:20 UTC | 2019-04-12 17:52:06 UTC | 2019-04-17 07:32:47 UTC |
| CONTINENTAL_EUROPE | sync01 / DE_KA primary channel | 3,542,400 | 2019-08-02 14:23:59 UTC | 2019-08-10 19:11:59 UTC | 2019-08-18 23:59:59 UTC |
| GREAT_BRITAIN | GB02 | 4,422,918 | 2019-12-11 12:11:47 UTC | 2019-12-21 18:16:30 UTC | 2019-12-31 23:59:59 UTC |
| ICELAND | IS01 | 367,803 | 2017-10-18 14:43:42 UTC | 2017-10-19 11:10:18 UTC | 2017-10-20 07:54:06 UTC |
| MALLORCA | ES_PM02 | 26,468,589 | 2020-07-05 12:59:23 UTC | 2020-10-31 17:15:32 UTC | 2020-12-31 23:59:59 UTC |
| NORDIC | SE01 | 565,853 | 2019-05-10 14:34:51 UTC | 2019-05-11 22:34:29 UTC | 2019-05-13 06:54:20 UTC |
| WESTERN_INTERCONNECTION | US_UT | 548,793 | 2019-05-22 22:59:38 UTC | 2019-05-24 05:28:58 UTC | 2019-05-25 11:58:16 UTC |

## Cryptographic identity

Local Popstop manifest:
`GRID_QI_CAMPAIGN_MANIFEST_v01.csv`

SHA-256:
`41733f9498090a173c61f61b4003ae0b0fa4dc306aa592af99271e6ba29c18bb`

Temporal-cut manifest:
`GRID_TEMPORAL_PARTITION_CUTS_v01.csv`

SHA-256:
`d71e9e751e2744b58d2f75ecd821262b96be685b4ea537e791fe05e1948e18fc`

## Scientific meaning

This manifest was generated from source identity, QI state and time only.

No perturbation threshold, recovery duration, abnormal-recovery label, chi/Χ/Χ_arc value, or event outcome contributed to campaign selection or partition boundaries.

Accordingly:
- temporal holdouts remain untouched;
- within-grid replication campaigns remain untouched;
- ERCOT, GRAN_CANARIA and RUSSIA remain external-grid transport holdouts;
- any later change to these partitions requires a documented governance failure, not scientific convenience.

## Next authorized step

Use DEVELOPMENT portions only to qualify input geometry and event-candidate construction. Recovery outcomes remain sealed until event entry, return-set, sustained-return, interruption and horizon rules are frozen.
