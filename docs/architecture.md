# Architecture and rollout

## Separation of concerns

- `agent-project-setup`: reusable instructions, phase guidance, safe adoption, context and handoff.
- Target repo: authoritative project data, decisions, task source and format preferences.
- `memento` (optional personal installation): personal project index, capture inbox, GTD and activity journal. No other project depends on access to it.
- `coding-agent-setup` (optional): engineering workflow, tests and coding agents. Integration must respect common `AGENTS.md` and skills ownership without overwriting either source.

## V1 delivery slices

1. Phase guidance and reusable skill entrypoints (this slice).
2. Safe adoption and update tooling with dry-run, conflict detection and idempotency tests.
3. End-to-end meal planner pilot: discover, shape, plan, handoff; no coding assumption.
4. memento profile: `orgfdb` queries and watch/rebuild, Capture, journal and personal GTD, independently tested.
5. Optional co-installation with coding-agent-setup and later extensions.

## Rules for future adapters

Canonical skills live in `.agents/skills/`; adapters for specific hosts must be derived without changing canonical files. Use project-owned `AGENTS.md` as the shared entrypoint. Never overwrite unknown existing sections. An upgrade must compare provenance/version and local changes before writing.

On failure, disclose which files were modified and which operations were not completed; never claim that exported captures were stored in the intended repository.
