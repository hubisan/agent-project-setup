# APS skill catalog

**Status: design candidates, not installed or accepted skills.** Every original skill uses the `aps-` prefix (from `agent-project-setup`), including its directory, frontmatter name, invocation and references. The catalog describes **responsibilities**; it is not an instruction to build every candidate.

See [six project phases](phases.md) and [roadmap issue #11](https://github.com/hubisan/agent-project-setup/issues/11). The existing implementation issues #12–#20 predate this revised taxonomy and **will need review before their titles/scopes are changed**. Additional skills get separate issues only if real use warrants them. These links are ordinary issue references, not native GitHub sub-issues.

## Org-mode document granularity

Prefer **cohesive, topic-based Org files** rather than either a monolithic repository-wide file or a Zettelkasten-style collection of atomic notes. **Medium-sized and fairly large Org files are welcome.** Use headings and subheadings to organise related content within the same file.

Split a file **only when there is a concrete benefit**: clearly independent domains, separate lifecycles or maintainers, distinctly different retrieval/work contexts, or an actual navigation/maintenance problem. File size alone is not a reason to split. Avoid one-file-per-thought, one-file-per-term and arbitrary line-count/heading-count thresholds.

**Directories are first-class organisation tools.** Group coherent Org/Markdown files in a small number of descriptively named, domain-based directories once a flat directory becomes hard to navigate. Avoid both an unstructured root crowded with unrelated files and unnecessary deep or single-file folder trees. The right split depends on meaningful subject boundaries and the way people and agents retrieve information, not numeric file-count limits.

**Navigation and context efficiency:** a clear hierarchy and a short index/README (only where it provides useful orientation) let agents inspect directory names and read relevant files selectively instead of scanning everything. This can reduce file discovery effort and unnecessary context/token use **when the agent actually follows that selective retrieval workflow**; folder nesting itself does not guarantee token savings. Maintain obvious paths and links; prefer a few coherent directories with cohesive medium-to-large Org files.

Retain existing project conventions and meaningful cross-links. When splitting is warranted, use a small number of well-named, coherent files and keep their relationships discoverable. **Do not automatically reorganise an existing user's notes.** Ask permission before any consequential migration and explain the proposed split.

## Phase-specific candidates

| Phase | Skill candidate | Responsibility | Expected outcome | Existing issue |
| --- | --- | --- | --- | --- |
| 1. Clarify | `aps-frame` | Clarify purpose, desired outcome, success indicators and boundaries without a heavyweight vision ceremony | Small project brief | [#15](https://github.com/hubisan/agent-project-setup/issues/15) (re-scope candidate) |
| 2. Understand | `aps-analyze` | Inspect the current situation, stakeholders, environment, constraints, needs and requirements at an appropriate depth | Situation and actionable requirements | Not yet assigned |
| 3. Design | `aps-design` | Explore, compare and refine options, including AI + files, existing tools, process changes or custom software | Justified testable solution | [#17](https://github.com/hubisan/agent-project-setup/issues/17) (re-scope candidate) |
| 4. Plan | `aps-plan` | Organise the selected work, dependencies, priorities and next actions | Executable plan appropriate to project size | [#18](https://github.com/hubisan/agent-project-setup/issues/18) |
| 5. Execute | **No generic skill** | Perform real work or experiments with the relevant available tools and domain-specific methods | Actual results, not only planned NEXT actions | Not applicable |
| 6. Review | `aps-validate` | Test the outcome against requirements, success indicators and agreed acceptance | Findings, gaps and acceptance decision | Not yet assigned |

Do not automatically split stakeholder mapping, risk assessment, requirements or prototyping into additional skills. These are methods the phase skill can select as needed. Introduce a specialised skill only when actual work demonstrates a repeated, substantial workflow.

### Domain modeling as a method, not an IT-only phase

Within **`aps-analyze` / Understand**, develop a lightweight **conceptual domain model** when the project's subject has ambiguous terms, interacting concepts, or important rules. This is useful for research, knowledge bases, organisational processes and personal projects as well as software.

**Progressive depth: map first, zoom deliberately.** Keep the scope of the analysis visible; do not automatically follow interesting edge cases into deep modeling.

1. **Level 1 – domain landscape:** identify the main domains, each with a one-sentence purpose, rough boundary and important interactions. Keep this overview deliberately coarse, and save it before moving deeper. Avoid data fields, implementation details and exhaustive exceptions.
2. **Level 2 – selected domain:** zoom into **one domain** when it matters to the current goal. Clarify its key concepts, terminology, stakeholders, principal processes, relationships and high-value rules. Retain links to the Level 1 landscape.
3. **Level 3 – targeted detail:** explore specific constraints, edge cases, examples or precise rules **only if a concrete open question, experiment, requirement or next action needs it**. Do not fully specify every domain in advance.

Before moving from one level to the next, state **which domain**, **what decision/work requires the detail**, and **the expected useful outcome**. If no such need exists, stop at the current level, note optional unknowns and recommend the next meaningful action. New evidence may justify zooming back out and revising the domain map.

Reuse and refine the existing project vocabulary and document only meaningful distinctions. Use concrete examples or counterexamples where they resolve ambiguities. Do not automatically turn a conceptual domain model into a database, class diagram, DDD bounded-context architecture or software design.
- Save useful agreed terminology and relationships in the **target project's established authoritative files** (existing glossary, notes, specification or model). Create a new file only when its value is clear; distinguish agent-proposed choices from user-confirmed definitions.
- **`aps-frame`** defines *why and what outcome*; **`aps-analyze`** sharpens *what the domain means*; **`aps-design`** uses the resulting understanding to propose *how to solve the problem*. Continue refining the model across phases if new evidence warrants it.

**Initial decision:** domain modeling is a callable analysis **method** within `aps-analyze`, not an additional mandatory skill. Consider a separately scoped `aps-model` only after real pilots demonstrate a repeatable, distinct workflow.

## Cross-cutting candidates

| Skill candidate | Purpose | Existing issue |
| --- | --- | --- |
| `aps-clarify` | Question any scope (project, stakeholder, assumption, single requirement), explain recommended choices and capture the decision | [#14](https://github.com/hubisan/agent-project-setup/issues/14) (re-scope candidate) |
| `aps-brainstorm` | Expand the idea space using prompts, divergent perspectives and combinations; organise afterwards without premature evaluation | Not yet assigned |
| `aps-research` | Seek and compare evidence, distinguish source claims from hypotheses and note uncertainty | [#16](https://github.com/hubisan/agent-project-setup/issues/16) |
| `aps-review` | Review actual work status, relevant blockers, commitments and next actions at any point | [#19](https://github.com/hubisan/agent-project-setup/issues/19) |
| `aps-improve` | Continuous improvement (KVP): identify and test better **content or methods** for a chat/session, a project or the reusable setup | [#13](https://github.com/hubisan/agent-project-setup/issues/13) (re-scope candidate) |
| `aps-handoff` | Hand over evidence, decisions, current state and actual save/commit status between sessions or repositories | [#20](https://github.com/hubisan/agent-project-setup/issues/20) |
| `aps-adopt` | Safely integrate the setup into a project with preview, conflict handling and preservation of existing ownership | [#12](https://github.com/hubisan/agent-project-setup/issues/12) (re-scope candidate) |

**Distinct review questions:** `aps-review` = *Where do we stand and what is next?*; `aps-validate` = *Does the outcome meet the requirements?*; `aps-improve` = *How can the work or our way of working improve?*

## Natural Planning and brainstorming

Natural Planning is an on-demand technique across phases: **Purpose -> Outcome -> Brainstorming -> Organising -> Next actions**. Brainstorming often starts after clarifying the outcome, but is also valuable during situation analysis, design or execution. Organisation may structure *requirements*, *solution concepts* or *work items*: these are different things and should not be conflated.

Execution is a **real project phase after planning**; do not imply that identifying a NEXT action means it was done.

## Skill quality gate: develop one at a time

For every candidate, design and verify:

1. **Triggers and boundaries:** useful when asked for this workflow, including relevant smaller scopes; specify when another skill fits better.
2. **Inputs and permissions:** use existing authoritative project information before asking again; no silent cross-repository or external action.
3. **Output contract:** concrete useful result, provenance and accurate proposed/saved/committed/pushed statuses.
4. **Procedure and stopping condition:** minimal, readable process with only necessary branching, checkable completion, and plain-text fallback.
5. **Practical scenarios:** test at least a normal, ambiguous and blocked/failure case; observe actual user friction.
6. **Portability:** host-agnostic Markdown/Org guidance; specific UI capabilities are optional.
7. **Revision:** incorporate evidence from the user-led meal-planner pilot, review the skill independently and only then mark it accepted.

A short `SKILL.md` is **not** acceptance evidence. No project skill is currently ready for installation.

## Clarification and questioning presentation contract

**Historical context:** The [Q001–Q121 retrospective](clarify-121-question-audit.md) classifies documented decision topics into user decisions, agent defaults, verification, deferral and consolidation. It is a routing hypothesis, not a measured reduction in actual interview questions.

**Single source for question layout:** Use the [question presentation reference](../.agents/skills/aps-clarify/references/question-presentation.md) in the candidate `aps-clarify` skill. It defines question numbering, optional clarification text, recommended-first answers and free-text comments. Future APS questioning skills should point to this common guidance rather than copy it. Interactive forms are optional and must have a plain-text equivalent.

### Decision autonomy and question discipline

**Goal: remove uncertainty with the fewest valuable questions, not conduct the longest interview.**

Before asking a question, check whether it is already answered in the project, can be verified by available evidence, or can be resolved through a safe and reasonable default. In those cases, **do the work** instead of presenting A/B/C options merely to obtain agreement with the agent's recommendation.

| Decision type | Behaviour |
| --- | --- |
| Established fact, documented choice, or verifiable information | Reuse or research it; do not ask the user to reproduce facts the agent can find. |
| Clear, low-risk and easily reversible implementation/detail choice | Decide autonomously and inform the user; persist the decision in the project when it matters to future work. |
| Several viable but low-stakes defaults | Choose, briefly explain the reason and record the choice in the project's existing decision documentation if it can affect later work; make it easy to correct. |
| Goal, user preference, domain policy, materially different trade-offs, or consequential/irreversible action | Ask a **focused** question, show meaningful options and explain the recommendation; obtain necessary permission before the action. |
| Missing evidence or uncertain assumptions | Research when possible; otherwise disclose the assumption and ask only if it materially affects the outcome. |

### Reporting and retaining autonomous decisions

A meaningful decision is **not complete** just because the agent made it. For every autonomous choice that may influence future work:

1. **Tell the user** the chosen default and the reason, briefly and clearly. Distinguish an agent-selected choice from an explicit user decision.
2. **Record it in the target project's authoritative source** (its existing decision log, specification, ADR or project notes), including the choice, rationale and assumption/revisit condition when relevant. Reuse the project's conventions; do not create paperwork for insignificant details.
3. **Report persistence accurately.** If file access or permission is missing, show a ready-to-save decision and say it remains unsaved. Never assume chat context is durable project documentation.
4. **Reuse and revise** existing decisions in later work when evidence warrants it; avoid reopening settled choices reflexively.

This is primarily an `aps-clarify` responsibility, but **all APS workflows** that make meaningful autonomous decisions must follow the same principle. Brainstorming *ideas* are not decisions until selected.

- **Ask only questions whose answers would materially change the outcome, priority, safety or direction.** Do not ask because an interview template has an empty field.
- Ask a small set of independent, high-impact questions in each round; drill into details only if they block progress or the user explicitly requests exhaustive questioning.
- After each answer, update the decision frontier: remove resolved questions, infer only defensible consequences and continue useful work. Never ask the same question again without relevant new evidence.
- If the user repeatedly accepts the recommendation, reassess whether similar routine questions should instead be decided by the agent; this is a signal of excessive questioning, **not** blanket authorisation to override user-owned decisions.
- Stop clarification once the current task has enough information to progress safely; do **not** require every conceivable branch to be explored. Record optional unresolved points as follow-up only when relevant.
- Do not confuse autonomous **reasoning or choosing a reversible default** with permission to write, publish, buy, delete or perform another consequential action. Respect the target repository's established permission policy.
- For actual user-owned questions, keep the structured question presentation and a justified recommendation. A preselected answer is **never** evidence of user consent.

**Validation scenarios:** automatic selection of an obvious file naming convention without asking; reusing a documented stakeholder fact rather than questioning the user; asking the user to decide whether the project needs an application; stopping a detailed interview after the current requirements are sufficiently clear; reporting instead of guessing when source facts cannot be verified.

## Continuous improvement contract

`aps-improve` supports:

- **Session/chat:** what helped or hindered this interaction and one or two adjustments.
- **Project:** project-specific improvements to the outcome, content, decisions or process, recorded in the project's own authoritative files if authorised.
- **Reusable setup:** generalise proven lessons without personal/confidential details; propose a reviewed update to `agent-project-setup`, without silently writing across project boundaries.

Improve during relevant work, at milestones or on request. A future scheduled check requires a separately enabled scheduling mechanism; the skill alone cannot autonomously operate between chats. Evaluate whether an adopted improvement worked rather than repeatedly generating the same suggestion.

## Language and provenance

Write setup instructions and skills in **English**. Respond to users in their chosen language and preserve the language and conventions of existing project content; do not translate unless requested. Approved historical German specification documents remain unchanged.

AIHero contributes **design inspiration only**, not copied skills, installation or vendor-dependent workflow. `coding-agent-setup` and `memento` remain independent optional integrations.
