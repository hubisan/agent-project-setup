# Retrospective: 121 decisions through the lens of aps-clarify

**Status:** a retrospective *design exercise*, not a review of a finished skill and not a change to any historic decision.

**Source:** [approved Q001-Q121 decision register](spec-v2/entscheidungsregister.md), version 2.0 (29 October 2026). The register notes that **the exact original question text and options are not available for every Q-number**. This audit therefore classifies the **underlying decision topics** into the best route for a future AI-assisted project, rather than claiming to know which actual historical questions were unnecessary. Results are provisional and depend on the context available at the time.

## Executive finding

| Route for a future aps-clarify | Topics | Share |
| --- | ---: | ---: |
| **User decision:** ask about personal priorities, scope, authority or material trade-offs | 31 | 25.6% |
| **Agent default:** choose a transparent, reversible standard and proceed | 65 | 53.7% |
| **Verify/test:** investigate facts or run a technical check | 5 | 4.1% |
| **Defer:** leave a conditional detail until it is actually relevant | 11 | 9.1% |
| **Consolidate:** avoid revisiting a closely related decision already being resolved | 9 | 7.4% |
| **Total** | **121** | **100%** |

**Interpretation:** The **90 non-user-decision topics (74.4%)** would plausibly be handled without an additional immediate user questionnaire in a streamlined workflow. This is a **routing hypothesis, not a measured 74.4% reduction** in original questions. Even the 31 user-owned topics do not all need asking: some are already resolved in existing project sources, while others arise only much later.

## Full Q001-Q121 routing inventory

Each Q-number appears **exactly once**. For the decision meaning, consult the canonical source above. The inventory is grouped by the proposed *handling method*, not by original interview order.

| Recommended route | Count | Percent | Q-numbers |
| --- | ---: | ---: | --- |
| User decision | 31 | 25.6% | Q001, Q004, Q006, Q008, Q012, Q021, Q022, Q023, Q027, Q035, Q036, Q049, Q050, Q052, Q055, Q057, Q058, Q061, Q065, Q067, Q074, Q076, Q079, Q085, Q090, Q093, Q095, Q099, Q110, Q119, Q120 |
| Agent default | 65 | 53.7% | Q002, Q003, Q005, Q007, Q010, Q011, Q013, Q014, Q015, Q016, Q017, Q018, Q019, Q020, Q024, Q025, Q026, Q028, Q029, Q031, Q032, Q033, Q034, Q037, Q038, Q039, Q040, Q041, Q042, Q043, Q044, Q045, Q046, Q047, Q048, Q054, Q060, Q062, Q063, Q064, Q068, Q069, Q070, Q071, Q072, Q073, Q075, Q077, Q078, Q080, Q081, Q082, Q084, Q086, Q087, Q088, Q089, Q092, Q096, Q098, Q102, Q112, Q114, Q116, Q117 |
| Verify/test | 5 | 4.1% | Q059, Q094, Q104, Q118, Q121 |
| Defer | 11 | 9.1% | Q009, Q030, Q051, Q053, Q056, Q066, Q083, Q091, Q105, Q107, Q113 |
| Consolidate | 9 | 7.4% | Q097, Q100, Q101, Q103, Q106, Q108, Q109, Q111, Q115 |

## Main patterns and concrete evidence

### 1. Ask only where the user's answer can change a meaningful choice

- **Q008**: Preferred document format is a user preference; reuse the established format rather than selecting a new one at every document.
- **Q036**: Natural Planning as the preferred lightweight workflow is a real project-governance preference.
- **Q049/Q050 and Q057/Q058**: Privacy classification, private/business separation and a new external data transfer depend on project/user permissions. Never infer consent.
- **Q065**: The actual pilot is a user priority.
- **Q110 and Q120**: Authoritative location of personal GTD and index/journal in memento required real user intent, **once**, and is now settled.
- **Q027, Q052, Q055, Q079**: Execute updates, conversions or ownership handoffs only within actual permission. The agent can propose a plan independently but cannot treat a recommendation as approval.

### 2. Defaults the agent could reasonably choose and report

- **Q002, Q005, Q007, Q010, Q011**: Minimal structure, minimal metadata and progressive loading are sensible reversible starting points.
- **Q015-Q018**: Avoid duplicated knowledge articles, maintain relevant links, cite external evidence and flag contradictions by default.
- **Q020, Q024-Q026, Q028**: Versioned updates, safe adoption, preserving file ownership and conflict visibility are default implementation practices.
- **Q037, Q043-Q048**: Ask adaptively; write concisely; report completed changes; group commits; avoid unnecessary issues; offer but do not force handoffs.
- **Q070, Q080, Q084, Q088, Q116**: Use focused structural checks, preserve project-owned agent instructions, handle adapter paths deliberately and use Git diffs.

A meaningful agent-selected default must be **disclosed to the user** and **recorded in the target project's existing decision source** when relevant to future work. Trivial details do not need separate decision records. If writing is unavailable, say the decision is not saved.

### 3. Verify facts instead of asking a user to guess

- **Q059**: Inspect the real sync script and device setup before claiming compatibility.
- **Q094 and Q104**: Test orgfdb, search/index and watch/rebuild behaviour.
- **Q118**: Verify CUSTOM_ID rendering and link resolution in the actual viewers.
- **Q121**: Verify access to the capture list and scheduling capability before promising reminders.

### 4. Defer premature branches

- **Q030/Q066**: Combining a coding setup belongs to a project that actually needs software work.
- **Q051**: Backup design depends on the concrete storage and recovery needs.
- **Q053/Q105/Q113**: Detailed conversion scope and original-file handling belong to an actual migration.
- **Q083/Q091**: Do not design a full new issue tracker while testing a minimal project workflow.

### 5. Consolidate repeated or superseded threads

- **Q100, Q101, Q108, Q115 -> Q120**: The index/journal location came up repeatedly before the definitive memento decision. Maintain **one tracked unresolved decision** and carry forward previously stated constraints.
- **Q106 -> Q110**: Personal GTD source-of-truth discussion was resolved later.
- **Q103/Q109 -> Q116**: Complicated diff/snapshot proposals were superseded by simple Git diffs.
- **Q111 -> Q117**: An ambiguous no-write fallback became a concrete capture fallback.
- **Q097 -> Q102**: Archiving and a 30-day active view are one related discussion; avoid separate questionnaires if a workable default is enough.

These chains can include legitimate refinement; **repetition is not automatically an error**. The mistake to prevent is losing prior context or asking a new user decision without a new consequential trade-off.

## Test cases for the future aps-clarify

1. **First-pass scope:** Given a broad project idea, identify the few consequential unknowns and a small runnable next action. Do not enumerate all eventual design branches.
2. **Autonomous defaults:** Pick a conventional low-risk structure, explain its rationale and persist it in the project when it matters.
3. **No duplicate decisions:** If Q120 or an equivalent source-of-truth decision is already saved, do not reopen Q100/Q101/Q108/Q115 without new evidence.
4. **Research before asking:** Inspect available repositories, app features or tools before requesting technical facts from the user.
5. **Stop when workable:** Begin a real trial with unresolved optional design details parked, not forgotten.
6. **Maintain user authority:** Personal priorities, privacy boundaries, irreversible actions and material trade-offs remain user-owned.
7. **Progressive domain modeling:** Keep the domain landscape broad; zoom into one domain only for a specific actual decision or experiment.
8. **Transparent status:** Clearly separate *agent-selected, user-approved, proposed, saved, committed and pushed* states.

## Practical conclusion

The next version of `aps-clarify` should optimize for **useful progress per interruption**, not question coverage. Apply **Decide -> Try -> Adjust**; adopt reversible defaults, preserve meaningful decisions, and return to the user only when their judgment is genuinely needed. Review the proposed categories against a new real pilot before treating the audit as an empirically validated result.

**No existing user decisions or historical files were changed. No APS skill has been implemented.**
