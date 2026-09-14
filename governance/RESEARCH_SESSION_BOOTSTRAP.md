# SymC Research Session Bootstrap

Purpose: eliminate avoidable startup delay and prevent new research chats from proceeding under stale protocol or stale repository state.

## Required startup sequence

1. At the first substantive turn of a new SymC research chat, load the current authoritative General Cross-Project Research Protocol before substantial analysis or execution whenever it is accessible through the conversation, project files, File Library, or a connected repository source.
2. Read the Core Card first. Load the Operating Quick Reference only when the task can trigger those controls, then read the protocol sections material to the immediate task. Do not require a full reread of the entire protocol for every question.
3. If the current protocol cannot be loaded and GitHub access is not available to the conversation, surface the option to connect or enable GitHub at the beginning of the conversation, before a long research response. Authorization delay should not consume several minutes of reading before the user learns that repository access is needed.
4. If GitHub is already connected and authorized, use it when repository state is material. Do not ask for redundant per-conversation permission.
5. Before inheriting active work, verify current source-of-record state: active branch/workflow/run, relevant commit, watchdog/recovery state, and whether the work has already completed, failed, been superseded, or fallen off.
6. Do not launch duplicate work merely because the new chat lacks prior conversational context.
7. If the authoritative protocol still cannot be directly loaded, proceed only with the best available context and state that the current GP was not directly verified. Never silently substitute an older protocol when a newer one may exist.

## Current protocol at bootstrap update

General Cross-Project Research Protocol v0.7.8, dated 14 September 2026. This line is a pointer, not a permanent claim of currency. The highest later active version supersedes it.

## Internal-use transfer principle

The GP stores program-wide transferable rules. Project-specific equations, datasets, atlas targets, paper-specific claims, and implementation details remain in the relevant project protocol unless they are necessary to understand or execute a general rule safely. When a project lesson generalizes, promote the transferable rule into the GP in domain-neutral form rather than importing the full project machinery.

## Reader-first communication default

Use smooth, accurate prose as the default. Paragraphs commonly fall around 3-5 sentences when that fits naturally, but this is not a hard limit. Multiple paragraphs per section are expected when needed. Headings should mark real changes in subject, and bullets, tables, equations, code, diagrams, or callouts should be used when they materially improve comprehension rather than as decorative scaffolding.

Default adaptable flow: Status; What happened; Why it matters; What happens next; What you need to do.

Governing presentation principle: scrolling should correspond primarily to new information, not formatting.
