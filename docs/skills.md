# Project skill catalog

**Status:** proposed / not yet accepted. This is the source of truth for the **order and maturity** of skills, not an instruction to install them all.

**Parent tracker:** [Skill roadmap #11](https://github.com/hubisan/agent-project-setup/issues/11). These are **linked GitHub issues**, not native GitHub sub-issues (current connector cannot create those).

## Skill candidates

| Order | Skill | When it helps | Main result | Status | Issue |
| --- | --- | --- | --- | --- | --- |
| 1 | `adopt-project-setup` | New or existing project wants the setup | Safe, verified adoption | Planned | [#12](https://github.com/hubisan/agent-project-setup/issues/12) |
| 2 | `project-retro` | After a session, a project milestone, or a workflow friction | Evidence-based KVP improvement proposal | Planned | [#13](https://github.com/hubisan/agent-project-setup/issues/13) |
| 3 | `clarify-project` | An important decision requires structured questioning | Answered decision tree and next open frontier | Planned | [#14](https://github.com/hubisan/agent-project-setup/issues/14) |
| 4 | `discover-project` | Goals, context or purpose are unclear | Outcome and next learning action | Planned | [#15](https://github.com/hubisan/agent-project-setup/issues/15) |
| 5 | `research-project` | External evidence is required | Source-linked findings and uncertainty | Planned | [#16](https://github.com/hubisan/agent-project-setup/issues/16) |
| 6 | `shape-project` | Compare AI workflow, existing tools or custom solution | Choice or testable experiment | Planned | [#17](https://github.com/hubisan/agent-project-setup/issues/17) |
| 7 | `plan-project` | Turn purpose and ideas into executable next actions | Flexible Natural Planning | Planned | [#18](https://github.com/hubisan/agent-project-setup/issues/18) |
| 8 | `review-project` | Check progress and priorities | Few NEXT actions and relevant blockers | Planned | [#19](https://github.com/hubisan/agent-project-setup/issues/19) |
| 9 | `handoff-project` | Resume work in a new session or extract a wiki project | Portable, verified continuation package | Planned | [#20](https://github.com/hubisan/agent-project-setup/issues/20) |

**Phase guidance is not a linear lifecycle.** These skills can be used in any order as the project evolves. The order above is a *development priority*, not an order users must follow. A project can remain research/planning forever without a coding setup.

## Skill acceptance contract

Develop **one skill at a time**, in its own issue and review. An author must show:

1. **Trigger:** clear phrases/contexts that require this skill and when it should not fire.
2. **Inputs:** exactly which existing files, user decisions and tools it needs. Reuse existing sources before asking again.
3. **Output:** observable user result, source-of-truth destination, and explicit proposed/saved/committed/pushed status.
4. **Procedure:** concise repeatable actions, only necessary branching and a checkable stopping condition.
5. **Quality:** at least three meaningful scenarios (normal, ambiguous, failure/missing permission). Review the behaviour before calling it ready.
6. **Portability:** useful in a plain Markdown/Org and CLI context; optional host-specific visual controls must not be required.
7. **Security and improvement:** preserve project privacy, avoid hidden cross-repo writes, and feed verified general workflow lessons to `project-retro` only with authorisation.

An installed `SKILL.md` is **not evidence of acceptance**. The six early draft skill bodies from PR #1 remain in Git history as ideas, and are intentionally withdrawn from active discovery pending individual review.

## KVP / retrospective — `project-retro`

Three scopes with distinct owners:

- **Session/chat:** concise, evidence-based reflection on what went well, what caused friction and one or two adjustments for the next interaction. No assumption of repository write access.
- **Project:** record project-specific process lessons in that project's established docs/rules (only when authorised).
- **Reusable setup:** abstract a proven general improvement into a proposed update for `agent-project-setup`. Remove project identifiers, personal details and confidential content. Show diff and request the appropriate permission before writing.

Prefer a small actionable outcome to a ritual. Do not produce a retro automatically after every message. Distinguish project work review (`review-project`: **what next?**) from KVP (`project-retro`: **how should the process improve?**). Evaluate whether a proposed improvement worked on a later use, and retire ineffective rules.

## Structured questioning — `clarify-project`

This project needs a **presentation contract** as well as a reasoning process:

- Each question has a stable number, short title, enough context, options A/B/C where appropriate and **D — Other solution** with free text.
- Clearly distinguish the recommended answer and the user's actual selection.
- End each round with **general remarks** and a single clear submission path.
- Where supported, use compact interactive controls, preselect the recommended answer, and reveal custom text only for D. Else render the same content in readable plain text.
- Preserve corrections and comments on any option, including an answer like “B, with this change.”
- Ask only independent frontier questions; don't repeatedly ask settled decisions; finish when the tree is resolved and the user confirms shared understanding.

A general skill should not hard-code a particular ChatGPT component or assume all models can render a form.

## Later optional integration skills

`capture`, `inbox-review`, `gtd-review`, `activity-journal`, `calendar-sync` and update/maintenance support are **not part of this initial nine-skill development queue**. Their broader functionality is already covered by the relevant future memento and update tickets (#7–#10) or explicitly deferred. Introduce separate skill issues only when a real repeatable workflow calls for one.

**AIHero boundary:** borrow practical ideas (focused research, questions, progressive project guidance, retrospectives), not upstream skill bodies, naming obligations, installations or version-coupled dependencies.
