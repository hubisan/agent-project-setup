# Architecture and rollout

## Ownership

- `agent-project-setup`: portable instructions, phase guidance, skill quality gates, safe adoption and handoff.
- Target repository: authoritative facts, decisions, tasks, privacy rules, and Org/Markdown structure.
- `memento` (optional personal wiki): project index, capture inbox, personal GTD and activity journal. Other repositories do not depend on it.
- `coding-agent-setup` (optional): engineering workflow and implementation agents. Avoid shared AGENTS/skill collisions.

## Incremental delivery

1. **Design baseline and skill catalog**: 121 decisions, phase navigation, nine separately scoped skill issues. No installed skills yet.
2. **Adopt skill then safe installer**: test an individual `adopt-project-setup` skill (#12) and safe project adoption (#3), with dry-run and idempotency.
3. **KVP and questioning**: develop `project-retro` (#13) and `clarify-project` (#14) one by one using user-observed friction.
4. **General project workflows**: develop and verify each discovery, research, shaping, planning, review and handoff skill separately (#15–#20).
5. **User-led menu-planner pilot**: improve the skills as the project is actually used, without assuming an application.
6. **Optional extensions**: memento with orgfdb and GTD, setup upgrades, independent coding setup, and other later workflows.

## Session handoff architecture decision

**Decision:** use one temporary, `session-handoff`-labelled Issue per session in the **working repository**, rather than a shared mutable handoff file or a new temporary branch. GitHub's Issue number provides a unique transfer ID for concurrent users and agents. The Issue is a short pointer to authoritative work tickets, specs, ADRs and committed files, not an additional source of truth.

**Reason:** direct issue lookup avoids chat copy/paste and write collisions. The next agent must check the live repository state and acknowledge the takeover before closing the Issue; failures leave it open. Reuse the existing branch and work ticket. When GitHub Issues are unavailable, disclose and provide a Markdown fallback. Keep sensitive information out of Issue titles and bodies.

**Compatibility:** add the original `aps-handoff` procedure without editing/forking the installed AI-Hero `handoff` skill. Its OS-temporary-file output remains useful as scratch or fallback; the APS transport differs. No new issue-tracker implementation or document directory is needed. Source: [APS #20](https://github.com/hubisan/agent-project-setup/issues/20), based on [coding-agent-setup #32](https://github.com/hubisan/coding-agent-setup/issues/32). Detailed rules: [`aps-handoff`](../.agents/skills/aps-handoff/SKILL.md).

## Rules for future adapters

Canonical accepted skills live in `.agents/skills/`; provider-specific adapters or copies are derived, never independently maintained. Project-owned `AGENTS.md` remains the main shared entrypoint, with narrow pointers and collision-safe updates.

On failure, disclose which files were actually modified. An exported capture is not the same as a saved capture; committing or pushing is not implied by a local write.
