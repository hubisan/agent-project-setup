# Repository instructions

This public repository develops provider-neutral project guidance. It is not a target user project.

- Start with `README.md`, then `docs/phases.md` when routing, or `docs/skills.md` when planning/reviewing a skill.
- All custom project skills use the `aps-` prefix; keep names consistent across folder, frontmatter and references. Current catalog entries are proposals until accepted.
- **Develop one skill at a time.** Its GitHub issue defines cases, contracts and acceptance tests. A candidate in the catalog is not an installed skill.
- Store accepted canonical skills under `.agents/skills/`; adapter/mirror output must remain derived. Preserve project-owned `AGENTS.md` and existing installed skills.
- A project may remain research, planning or wiki work. Choose an application only if the user wants that direction.
- **Autonomous decisions:** tell the user about meaningful agent-made choices and persist the choice/rationale in the target project's established decision source; trivial details need no log. If unsaved, report that explicitly. See `docs/skills.md` for the rule.
- **Decide -> Try -> Adjust:** move forward with safe, reversible defaults, test a small real result, and revise using evidence. Ask the user only for material preferences, trade-offs or required approvals; follow `docs/phases.md` for boundaries.
- Keep existing Org/Markdown source of truth and decisions. Load relevant sections rather than entire repositories.
- AIHero is conceptual inspiration only; write original general-project instructions and do not copy or install upstream skills.
- KVP findings are scoped to session, project or setup. Apply generalised changes to this repo only after permission and sensitive-data scrubbing.
- Keep private and business data outside this public repository. Report proposed, saved, committed and pushed states separately.
- Changes to instructions, skills and docs require focused review.

## Language

Write agent instructions, skill definitions, setup docs and tests in English. Speak to the user in their preferred language. Preserve the existing language, terminology and style of each project's content. Never translate project content without an explicit request. Keep the original German v2 specification and decision register unchanged as historical source documents.

## Agent takeover and task execution

1. Read this file and `README.md`. Use `docs/phases.md` for phase routing, `docs/skills.md` for skill scope, and GitHub issue #11 for the current delivery order.
2. Treat the current catalog and issue-specific accepted decisions as authoritative over historical `docs/spec-v2/` snapshots. Existing implementation issues can have inherited names: follow the explicit scope-alignment notes, not the old heading.
3. Select **one ready issue** from #11, inspect its full body and linked PR/branch, and verify actual file/PR state before claiming work is done. Never infer completion from an issue's description or unchecked acceptance criteria.
4. Make a scoped branch/PR with tests appropriate to the change; do not merge unfinished skills or mark a candidate accepted without the issue's pilot, review and user-acceptance gates.
5. Report what was actually changed, tested, committed, pushed and still blocked. On agent/session transfer use a specific handoff issue when that workflow is available; otherwise supply an explicitly unpublished summary and exact refs.

`AGENTS.md` is the shared rule source. Provider adapters such as `CLAUDE.md` should point here rather than duplicate these rules.
