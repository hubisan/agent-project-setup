# Phase-aware project workflow

These six phases **orient** a project; they are not a mandatory waterfall. Work can skip a phase, revisit an earlier one, or combine several in one session. A project may remain a wiki, research project or planning workflow indefinitely.

| Phase | Question | Typical result | Phase-specific candidate skill |
| --- | --- | --- | --- |
| **1. Clarify** | Why are we doing this, and what outcome matters? | Purpose, desired outcome, boundaries, success indicators | `aps-frame` |
| **2. Understand** | What is the actual situation and what do people need? | Relevant stakeholders, environment, problems, needs and requirements | `aps-analyze` |
| **3. Design** | Which approach could meet these requirements? | Alternative solutions, tradeoffs and testable concept | `aps-design` |
| **4. Plan** | How do we organise the work and what is next? | Dependencies, priorities, actionable next steps | `aps-plan` |
| **5. Execute** | Can we do or try the next meaningful piece of work? | Real work, experiments and usable results | Use the project's existing tools and appropriate task-specific skills; no generic execution skill |
| **6. Review** | Does the result meet the intended outcome? | Evaluated outcome, gaps and acceptance decision | `aps-validate` |

## What counts as a validated outcome?

APS covers the path from an initial idea to a **real outcome checked against its intended purpose**, not only to a written specification or a list of next actions. The outcome can be a useful knowledge base, an agreed process, a completed research artifact, an operational workflow, or a working software application. For a software project, **implementation, tests and integration can be part of Execute and Validate**; adopt the separately maintained `coding-agent-setup` and its engineering skills when appropriate rather than requiring APS to duplicate specialised programming workflows. Validation concerns the **actual result**; an approved specification is only a milestone unless the intended deliverable itself was a specification. This does not require every APS project to become software.

## Cross-cutting skills

See the [skill catalog](skills.md) for the scope of `aps-clarify`, `aps-brainstorm`, `aps-research`, `aps-review`, `aps-improve`, `aps-handoff` and `aps-adopt`. They may be useful in **any** phase. All names are design candidates, not installed/approved skills.

## Natural Planning, GTD and execution

Use Natural Planning as a **lightweight method**, not a separate compulsory stage: **Purpose -> Outcome -> Brainstorming -> Organising -> Next actions**. Brainstorm and reorganise again when useful. The project workflow then **executes** the next action and **checks** the result; a planned NEXT action is not completed work.

A simple project may need only a purpose, a possible outcome and a single next action. A complex project may need a stakeholder map, structured requirements, risk assumptions, prototypes or an acceptance plan. Do what the current need justifies.

## Core working principle: Decide -> Try -> Adjust

Move projects forward through short, reversible learning cycles rather than lengthy speculative interviews.

1. **Decide:** use existing decisions and verified information; make reasonable, low-risk, reversible choices independently. State assumptions when they matter. Ask the user only when their goals, values, priorities or a material trade-off determine the choice.
2. **Try:** do a small, useful piece of real work or run a proportionate experiment. A next-action list is not a trial or a completed result.
3. **Adjust:** compare what happened with the desired outcome; keep what works, revise decisions or approach when evidence warrants it, and continue.

Prefer changes that are cheap to reverse. The time spent asking many hypothetical questions may exceed the cost of revising a few good defaults after real feedback. For consequential, irreversible, costly or permission-requiring actions, obtain the appropriate explicit decision or authorisation before acting.

This principle applies **across all phases and skills**, particularly `aps-clarify`, `aps-guide`, `aps-next` and `aps-improve`. Reopen earlier choices only when new evidence or real use justifies doing so.

## Routing rules

1. Identify the **immediate need**, not an assumed phase from a folder name.
2. Consult existing project decisions and files before asking repeated questions; never invent project facts.
3. Recommend one focused action and only the relevant methods. A cross-cutting skill can apply to a single stakeholder, question or document.
4. Distinguish proposed, saved, committed and pushed states; respect access permissions and target-source ownership.
5. Recommend software development only if justified by the project's needs; `coding-agent-setup` stays optional.
6. If a candidate skill is not implemented and accepted, describe the intended method without claiming to invoke an installed skill.
7. Follow the language policy in [AGENTS.md](../AGENTS.md): English for setup instructions; user-facing conversation and project content in their existing or requested languages.

## Pilot

The user-led meal-planner pilot will test this workflow incrementally. Explore existing recipes, AI-assisted planning and available tools before assuming a new application is needed. Use `aps-improve` concepts to propose process improvements at session, project or reusable-setup level.

## Source and status

This working taxonomy refines the [approved historical specification](spec-v2/README.md) without changing its original source files. Skill scopes and issue mapping are proposals until each skill has its own reviewed implementation. Ideas from AIHero are inspiration only; no skills are copied or automatically installed.
