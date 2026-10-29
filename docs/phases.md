# Phase-aware project guidance

**This is a navigation aid, not a linear state machine.** A project can move back and forth, skip steps, and mix wiki, research and planning. Ask only the question that blocks the next useful action.

| Current need | Suggested skill | Result | Stop when |
| --- | --- | --- | --- |
| Start with an existing or new repo | `adopt-project-setup` | Minimal safe adoption proposal | Existing conventions and file ownership are understood |
| Identify direction and value | `discover-project` | Purpose, desired outcome, known constraints | Next useful experiment or decision is clear |
| Compare possible solutions | `shape-project` | Options, risks, evidence, choice or open decision | A path can be tested, not necessarily coded |
| Organize work | `plan-project` | Flexible Natural Planning, next actions | There is at least one executable next action |
| Resume or review progress | `review-project` | Concise status, blockers, neglected decisions | Priority and next action are current |
| Transfer between agents or repositories | `handoff-project` | Portable verified handoff | New reader can continue without chat history |

## Routing rules

1. Determine the user's **immediate need**, not an assumed phase based on folder names.
2. Load one fitting skill; combine with another only when a distinct need arises.
3. Reuse existing documents and verified decisions. Search narrowly; avoid full-repository context loading.
4. Distinguish **facts**, **ideas**, **decisions**, **tasks** and **unresolved questions**.
5. A project can be solved by a workflow, existing tools, or AI—software development is only one option.
6. Suggest optional coding-agent-setup only after the user chooses software implementation.
7. Do not create a GitHub issue, PR, scheduled task or extra directory unless it benefits the actual step.
8. Respect the repository's own permissions, writing rules and source-of-truth conventions.

## Suggested interaction

Respond with a brief orientation: where the project stands, why this skill fits, and the one or two outcomes of the next step. Guide the user through those decisions, but do not demand a fixed questionnaire or interview when sufficient context exists.

## Pilot scenario

The meal planner starts with recipes and planning ideas, may work using AI plus files or existing tools, and only later might need an application. Apply discovery and option-shaping before any coding workflow. Preserve original notes and cite their source.
