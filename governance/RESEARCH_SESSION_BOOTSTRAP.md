# SymC Research Session Bootstrap

Purpose: eliminate avoidable startup delay and prevent new research chats from proceeding under stale manual or stale repository state.

## Required startup sequence

1. At the first substantive turn of a new SymC research chat, load the current authoritative SymC General Operations Manual (GOM) before substantial analysis or execution whenever it is accessible through the conversation, project files, File Library, or a connected repository source.
2. Read the Core Card first. Load the Operating Quick Reference only when the task can trigger those controls, then read the GOM sections material to the immediate task. Do not require a full reread of the entire manual for every question.
3. If the current GOM cannot be loaded and GitHub access is not available to the conversation, surface the option to connect or enable GitHub at the beginning of the conversation, before a long research response. Authorization delay should not consume several minutes of reading before the user learns that repository access is needed.
4. If GitHub is already connected and authorized, use it when repository state is material. Do not ask for redundant per-conversation permission.
5. Before inheriting active work, verify current source-of-record state: active branch/workflow/run, relevant commit, watchdog/recovery state, and whether the work has already completed, failed, been superseded, or fallen off.
6. Do not launch duplicate work merely because the new chat lacks prior conversational context.
7. If the authoritative GOM still cannot be directly loaded, proceed only with the best available context and state that the current GOM was not directly verified. Never silently substitute an older version when a newer one may exist.

## Current authoritative baseline

SymC General Operations Manual v0.8.1, dated 19 September 2026.

Expected authoritative Markdown filename: `SymC_General_Operations_Manual_v0.8.1.md`

Authoritative Markdown SHA-256: `ca0c4bcf178b194dd01337e82bdde61332ee76682208a22352ce5e828a984ea0`

v0.8.2 REVIEW and any later review candidate are non-authoritative until explicit user promotion. They may be used as review/mediation inputs but do not supersede v0.8.1 by existence alone.

This is a pointer, not a permanent claim of currency. A later explicitly adopted active version supersedes it. Numbered releases are promoted only by explicit user authorization; review builds do not become active releases, and version numbers are not skipped unless the user explicitly authorizes the skip.

## Internal-use transfer principle

The GOM stores program-wide transferable rules. Project-specific equations, datasets, atlas targets, paper-specific claims, and implementation details remain in the relevant project protocol unless they are necessary to understand or execute a general rule safely. When a project lesson generalizes, promote the transferable rule into the GOM in domain-neutral form rather than importing the full project machinery.

When consolidation removes a project-specific safeguard from the GOM, verify that its project-local destination exists or create one before treating the safeguard as safely relocated.

## Reader-first communication default

Use smooth, accurate prose as the default. Paragraphs commonly fall around 3-5 sentences when that fits naturally, but this is not a hard limit. Multiple paragraphs per section are expected when needed. Headings should mark real changes in subject, and bullets, tables, equations, code, diagrams, or callouts should be used when they materially improve comprehension rather than as decorative scaffolding.

Default adaptable flow: Status; What happened; Why it matters; What happens next; What you need to do.

Governing presentation principle: scrolling should correspond primarily to new information, not formatting.
