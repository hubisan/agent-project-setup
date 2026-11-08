# Architecture and rollout

## Ownership

- `agent-project-setup`: provider-neutral instructions, phase guidance, skill acceptance, safe adoption and handoff.
- Target repository: authoritative project facts, decisions, tasks, privacy rules, and Org/Markdown structure.
- `memento` (optional): personal project index, capture and journal; corresponding extensions use `mem-*`.
- GTD-specific reusable methods (optional): `gtd-*`; Memento-specific integrations remain `mem-*`.
- `coding-agent-setup` (optional): specialised engineering workflows when software development is chosen.

## Sources of truth and next work

- [`AGENTS.md`](../AGENTS.md) explains how any agent takes over and works.
- [Phase navigation](phases.md) defines the six-phase process, without mandatory waterfall gates.
- [Skill catalog](skills.md) defines current proposed names and boundaries.
- [Roadmap issue #11](https://github.com/hubisan/agent-project-setup/issues/11) gives priority and candidate/release status. Each skill's own issue specifies acceptance criteria; verify its actual linked PR and files.
- [Approved v2 specification](spec-v2/README.md) preserves historical decisions. It is not a live implementation dashboard.

## Delivery approach

1. Resolve and validate the existing `aps-clarify` prototype (#14 / PR #21) and shared UI issue #23; acceptance requires user approval.
2. Resolve and validate `aps-handoff` (#20 / PR #22), including the canonical `handoff` label and a real cross-agent trial.
3. Then work through ready, individually scoped skills from #11, starting with adoption (#12); re-evaluate order after pilot evidence.
4. Test the incremental menu-planner pilot without presuming a custom application.
5. Build optional Memento/GTD or coding integrations only when explicitly needed; avoid duplicate ownership.

This is a proposed working sequence, not permission to merge existing drafts or install any skill.

## Agent compatibility and adapters

Keep accepted canonical skill sources under `.agents/skills/`. Derived Claude Code / other-host adapters must not become independent sources of truth. `AGENTS.md` is the shared entrypoint; `CLAUDE.md` is a short Claude adapter. Native skill auto-discovery and installed capabilities differ by host and must be tested rather than assumed.

Project-owned instructions, formats and skills take precedence during adoption. Preview potential collisions and keep updates reproducible. Report file writes, commits and pushes distinctly; never claim an exported capture or a draft is a durable verified result.
