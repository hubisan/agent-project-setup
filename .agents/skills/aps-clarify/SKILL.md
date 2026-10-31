---
name: aps-clarify
description: Clarify open questions, goals, requirements, and decisions. Use when uncertainty needs to be resolved before meaningful progress can be made.
---

# APS Clarify

Resolve the **current decision frontier**: the choices that matter for the next useful step. Follow *Decide -> Try -> Adjust* rather than exploring every possible future detail.

## Workflow

1. **Bound the request.** Identify the goal, question, or decision to clarify. Adapt depth and question format to the user's request and the current context.
2. **Read selectively.** When project sources exist, follow their `AGENTS.md`, README or index pointers and inspect only relevant decisions, requirements, notes and permissions. Reuse established choices unless new consequential evidence warrants revisiting them.
3. **Route every uncertainty before asking anything:**
   - **Handle without asking the user:**
     - **Known:** reuse an established fact or decision.
     - **Verify:** research or test an ascertainable fact using available evidence and tools.
     - **Decide:** choose a safe, low-risk, reversible default; tell the user why and record it when it matters later.
     - **Consolidate:** combine overlapping questions into one decision while preserving earlier answers and nuances.
   - **Ask the user:** seek their judgement for goals, priorities, preferences, domain policy, material trade-offs, privacy boundaries or consequential permissions.
   - **Defer:** park a non-blocking question until a concrete decision or task requires it; retain a revisit condition if useful.
4. **Ask only the current independent user-owned questions.** Normally group **3–5 questions per round**, when that many are genuinely needed. Ask fewer when fewer matter, or ask a single **blocking question first** when its answer determines which further questions are relevant. Adapt to the user's stated preference. Offer alternatives and a justified recommendation for real trade-offs; never treat a suggestion or preselection as consent.
5. **Present questions consistently.** Follow [question-presentation.md](references/question-presentation.md) for numbering, context, option order and free-text responses. Use conversational questions when simpler; use interactive forms only where supported, with a usable plain-text fallback.
6. **Process answers and continue.** Preserve qualified choices and update the unresolved decision frontier after each round. Continue with the next relevant questions or useful work. Summarise decisions at meaningful milestones or when a response changes several other choices, not mechanically after every round.
7. **Record consequential decisions** in the existing authoritative source, if available and permitted. Capture the choice, reason, origin (agent-selected versus user-confirmed) and relevant assumptions or revisit conditions. Retain the project's established language and Org/Markdown conventions. Do not create a new log for trivial details or interpret a reversible default as permission to publish, merge, delete or share data.
8. **Stop when the current work can progress.** Report what is decided, assumed or genuinely blocked and distinguish proposed, saved, committed and pushed status. If writing is unavailable, provide ready-to-save wording and state explicitly that it is **not saved**. Perform or propose the smallest useful next action within the available permissions.

## Completion check

- The current goal can progress, or the remaining blocking user choice(s) or unavailable evidence are explicit.
- Every question is both user-owned and relevant now; already known, verifiable, reversible, overlapping and deferrable questions are handled without unnecessary interruption.
- Meaningful autonomous decisions are disclosed and their persistence status is accurate.
- The next action is practical rather than another speculative questionnaire.

## Scenario checks

- A broad meal-planner idea -> clarify the desired outcome without assuming an application is necessary; propose a small real trial.
- A previous decision sets topic-based Org files -> reuse it instead of asking about file-size limits again.
- Several independent user-owned choices -> ask 3–5 together; if one choice blocks the rest, ask it first.
- A routine filename convention -> select a safe default, not a user question.
- Unknown tool compatibility -> investigate or test before asking for a technical guess.
- Two overlapping storage questions -> consolidate while preserving prior constraints.
- Privacy boundaries or destructive actions -> seek explicit authority.
- No write access -> distinguish the drafted decision from a saved decision.

The historical 121-topic audit is a **routing hypothesis**, not evidence of measured interview reductions.
