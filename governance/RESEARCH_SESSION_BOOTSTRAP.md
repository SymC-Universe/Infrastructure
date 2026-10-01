# SymC Research Session Bootstrap

Purpose: eliminate avoidable startup delay and prevent new research chats from proceeding under stale manual or stale repository state.

## Required startup sequence

1. At the first substantive turn of a new SymC research chat, load the current authoritative SymC General Operations Manual (GOM) before substantial analysis or execution whenever it is accessible through the conversation, project files, File Library, or a connected repository source.
2. Read Section 0.4.0 first, then the Core Card. Load the Operating Quick Reference only when the task can trigger those controls, then read the GOM sections material to the immediate task. Do not require a full reread of the entire manual for every question unless a full governance audit is itself the task.
3. If the current GOM cannot be loaded and GitHub access is not available to the conversation, surface the option to connect or enable GitHub at the beginning of the conversation, before a long research response. Authorization delay should not consume several minutes of reading before the user learns that repository access is needed.
4. If GitHub is already connected and authorized, use it when repository state is material. Do not ask for redundant per-conversation permission.
5. Before inheriting active work, verify current source-of-record state: active branch/workflow/run, relevant commit, watchdog/recovery state, and whether the work has already completed, failed, been superseded, or fallen off.
6. Do not launch duplicate work merely because the new chat lacks prior conversational context.
7. If the authoritative GOM still cannot be directly loaded, proceed only with the best available context and state that the current GOM was not directly verified. Never silently substitute an older version when a newer one may exist.

## Current authoritative baseline

SymC General Operations Manual **v1.1**, dated **1 October 2026**, is the definitive active baseline and supersedes v1.0.

Directly verified authoritative Library artifact: `SymC_General_Operations_Manual_v1.1.md`.

Canonical companion working-record template: `WORKING_INVESTIGATION_TEMPLATE_v1.1.md`.

v1.1 locks the program notation to:
- lowercase `chi` / \(\chi\): licensed scalar/local coordinate;
- capital `Chi` / \(\Chi\): modal/vector representation;
- `Chi_arc` / \(\Chi_{\mathrm{arc}}\): overall reconstructed stability architecture.

Conglomerate/system organization is a contributing starting component and is not automatically identical to \(\Chi_{\mathrm{arc}}\). Admission at one level does not imply admission at another.

Legacy artifacts are migrated semantically, not by blind replacement. Historical, archived, submitted, accepted, and published artifacts retain their original notation. At the next substantive touch, active artifacts map a legacy capital `Chi` meaning the full architecture to `Chi_arc`, while preserving any use of capital `Chi` that genuinely denotes modal/vector structure.

A numbered GOM version is canonical immediately when issued and remains authoritative until superseded by a later numbered version. Unnumbered working drafts may exist during editing; there is no separate REVIEW/promotion state for an issued numbered version.

This bootstrap is a pointer, not an independent authority. If a later numbered GOM exists, that later numbered version supersedes this pointer and the pointer must be updated as a mechanical governance repair.

## Internal-use transfer principle

The GOM stores program-wide transferable rules. Project-specific equations, datasets, atlas targets, paper-specific claims, and implementation details remain in the relevant project protocol unless they are necessary to understand or execute a general rule safely. When a project lesson generalizes, promote the transferable rule into the GOM in domain-neutral form rather than importing the full project machinery.

When consolidation removes a project-specific safeguard from the GOM, verify that its project-local destination exists or create one before treating the safeguard as safely relocated.

## Reader-first communication default

Use smooth, accurate prose as the default. Paragraphs commonly fall around 3-5 sentences when that fits naturally, but this is not a hard limit. Multiple paragraphs per section are expected when needed. Headings should mark real changes in subject, and bullets, tables, equations, code, diagrams, or callouts should be used when they materially improve comprehension rather than as decorative scaffolding.

Default adaptable flow: Status; What happened; Why it matters; What happens next; What you need to do.

Governing presentation principle: scrolling should correspond primarily to new information, not formatting.


## Current cross-program representation obligations

Every active project must determine, where scientifically applicable:

1. what licensed scalar \(\chi\) means, if any, and its carrier, boundary, or scope;
2. what modal/vector \(\Chi\) means in the native mathematics, if that level is admitted;
3. what conglomerate/system organization exists independently of those lower representations;
4. what overall reconstructed \(\Chi_{\mathrm{arc}}\) is supported, if any, and which admitted components and relations contribute to it;
5. what the admitted levels mean together, including coupling, hierarchy, inheritance, recovery, transformation, emergence, and information loss;
6. whether perturbation/recovery is an informative probe for the claim actually being made.

The program does not require every domain to instantiate every layer. `NOT_APPLICABLE`, `REFUSED`, `NON_IDENTIFIABLE`, `UNRESOLVED`, and no-coherent-scalar outcomes remain scientifically valid.

The program must not identify stability with recovery universally. Recovery evidence is required only when the promoted claim depends on return, resilience, adaptation, or post-perturbation organization.
