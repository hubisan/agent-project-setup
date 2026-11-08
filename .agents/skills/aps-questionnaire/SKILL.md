---
name: aps-questionnaire
description: Prepare a concise, recipient-ready questionnaire to obtain missing facts, decisions or requirements from another stakeholder or subject-matter expert. Use when the current user needs to ask someone else for information asynchronously or in an interview. Do not use for ordinary clarification with the current user, stakeholder mapping alone or session handoffs.
---

# APS Questionnaire

**Pilot version: 0.1.0**. Candidate for real testing; not yet accepted.

Turn a specific knowledge gap into a questionnaire that the intended recipient can answer without access to the current chat. Work from **Decide -> Try -> Adjust**: create a useful small draft quickly; do not conduct a speculative interview about every detail.

## Workflow

1. **Identify the gap.** Use relevant project sources and established decisions if available. Separate known facts, unknown facts, conflicting claims and approvals needed. Do not ask again for documented answers. Avoid invented stakeholder identities or authority.
2. **Establish recipient and purpose.** Determine who has the missing knowledge, what they can reasonably answer, and what the user must be able to decide or do afterward. Reuse known roles and context. Ask the current user only for a *blocking* missing recipient or outcome, ideally one concise question. Otherwise choose a neutral, clearly marked assumption and proceed.
3. **Select only necessary questions.** Ask the recipient for concrete facts, constraints, workflows, examples or decisions that they own. Group related items; put the most consequential first. Make each question answerable independently, without compound or leading wording. Avoid questions that the agent should resolve from available evidence. Do not make a long survey by default.
4. **Draft the questionnaire.** Give a brief purpose, the intended recipient/role, how answers will be used, sufficient context, short thematic question groups, and an answer area below each question. Add a one-line 'why this matters' only where needed. Allow partial answers, 'unknown', and referral to another person. Use the recipient's language and vocabulary. A short closing invitation for missed considerations is optional.
5. **Handle delivery honestly.** Produce copyable Markdown in chat unless a destination and permission are established. If project sources use Org-mode or a designated document location, respect that convention. Do not send messages or create GitHub issues/files without authorization. Distinguish drafted, saved and sent states.
6. **Use replies constructively.** When answers are supplied, extract verified facts, stakeholder opinions, decisions and unresolved conflicts separately; clarify only material contradictions. Update the project's authoritative source when permitted, preserving provenance. Hand unresolved user decisions to `aps-clarify`; do not invent consent.

## Output shape

Use a compact document with an informative heading and, when relevant:
- **Purpose:** what decision or next step these answers enable.
- **For:** recipient role, not an invented person.
- **Context:** only what the recipient needs to answer.
- **Questions:** grouped by theme if useful, each with space for a response; optional examples or conditional follow-ups only when necessary.
- **Return:** suggested response method or deadline only if provided; do not fabricate commitments.

No fixed question count, survey platform or file is mandatory. A four-question Markdown note can be sufficient. Treat responses as evidence, not automatically binding approval.

## Boundaries and checks

- `aps-analyze` identifies stakeholder roles, relevant perspectives, needs and gaps. `aps-questionnaire` elicits information from another knowledge holder. `aps-clarify` resolves choices with the current user. `aps-handoff` transfers session state.
- Do not perform a full stakeholder analysis when just a short targeted questionnaire is needed; identify missing roles only when material to recipient selection.
- Do not repeat known information, solicit sensitive personal data without need, or represent a recipient's answer as the user's decision.
- Finish when the questionnaire is immediately usable and its persistence/delivery status is accurate; refine after actual feedback.

## Quick scenario checks

- Business process facts held by a subject-matter expert: ask about missing steps and exceptions, not settled technical design.
- Community project with volunteers: use clear non-technical language; identify affected groups without inventing names.
- All needed facts already in accessible sources: synthesize the answer instead of generating a redundant questionnaire.
- No writable project source: provide chat-only draft and clearly say it has not been saved or sent.
