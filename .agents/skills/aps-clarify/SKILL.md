---
name: aps-clarify
description: Clarify a project goal, requirement, assumption, stakeholder concern, or individual decision with the fewest high-value questions. Use when a user asks to clarify, sharpen, decide, or resolve project uncertainty, including natural-language requests for quick or deep clarification. Reuse documented decisions, verify facts, choose safe reversible defaults transparently, and ask the user only about consequential choices. Work for knowledge, research, personal planning, and software projects without presuming an app is needed.
---

# APS Clarify

Resolve the **current decision frontier**, not every possible future detail. Follow *Decide -> Try -> Adjust*: finish with a workable next action when possible.

## Workflow

1. **Bound the request.** Identify the particular goal or decision. Respect natural-language guidance such as "quick", "deep", "one question at a time", or "three questions per round"; do not require formal parameters. Use the user's language for conversation and the target project's language for documents.
2. **Read selectively.** Inspect the project's relevant existing decisions, requirements, notes, permissions, and evidence. Never reopen a settled decision without new consequential evidence; do not require an entire project history for a narrow question.
3. **Route each uncertainty:**
   - **Known:** reuse the recorded fact or decision.
   - **Verifiable:** research or test it when tools and permissions permit.
   - **Reversible default:** decide, state why and what would cause revision, and persist when meaningful.
   - **User-owned:** ask about priorities, goals, personal preferences, domain policy, substantial trade-offs, privacy boundaries, or consequential actions.
   - **Later:** defer optional details with the condition that would make them relevant.
   - **Duplicate:** consolidate related questions into one decision with preserved nuances.
4. **Ask the minimum independent user-owned questions** that affect the immediate next step. Default to one to three per round, adjusted to the user's preference and complexity. Offer specific alternatives and a reasoned recommendation when there is a real trade-off. Include **Other / own solution** and accept qualified answers such as "B, except...". A recommended or preselected option is **not** consent.
5. **Use shared question presentation.** Apply [question-presentation.md](references/question-presentation.md) for questions requiring structured choices. Prefer conversational prose for a single simple open question. Use interactive controls only when supported; equivalent plain text must work everywhere. Do not claim a separate form skill or cross-skill invocation exists.
6. **Persist consequential decisions in the target project's established authoritative file**, with selection, reason, origin (agent-selected vs user-confirmed), and revisit condition when useful. Retain existing Org/Markdown conventions. Avoid creating a new file merely to log trivial choices. Respect repository policies and write permissions; never equate choosing a default with permission to publish, merge, delete or transmit data.
7. **Stop when sufficient.** State the decisions, assumptions and any meaningful open blocker; say accurately what was proposed, saved, committed or pushed. Suggest or perform the smallest useful next step according to available permissions. If no persistence was possible, give ready-to-save wording and explicitly mark it unsaved.

## Completion check

- The current goal or decision can progress, **or** precisely one blocking user choice or missing piece of evidence remains visible.
- No question repeats an available source or seeks approval of an obvious reversible implementation default.
- Every meaningful autonomous choice is disclosed, with saved status accurately reported.
- The next action is actionable; optional later branches remain deferred.

## Scenario checks

- A broad meal-planner idea -> clarify the actual desired outcome, avoid assuming software, propose a small real trial.
- Existing decision says Org files are grouped by topic -> reuse it rather than requesting a new file-size policy.
- A routine filename convention -> choose a safe default, record it only if its effects matter later.
- Compatibility or tool support unknown -> inspect or test before asking the user for technical guesses.
- Privacy boundary or destructive action -> obtain user authority before acting.
- No project write access -> give a clear proposed decision and **not saved** status.

The historical 121-topic audit is a *retrospective routing hypothesis*, not evidence that this skill has reduced real interviews by a measured percentage. Use it as background, not as a list of questions to ask.
