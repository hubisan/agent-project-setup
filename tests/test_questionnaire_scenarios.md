# Manual acceptance: aps-questionnaire v0.1.0

## Test 1 — Business stakeholder
Prompt: "We know the planned workflow but the business owner must tell us what happens with exceptional cases. Prepare a short questionnaire I can send."

Expected: concise questionnaire for the role; no invented name, four or fewer well-targeted questions if sufficient, no request for settled technical details, truthful unsent status.

## Test 2 — Non-software project
Prompt: "Our neighbourhood event needs input from volunteer coordinators about their availability and constraints. Prepare questions for them."

Expected: plain language, answerable and neutral questions, no imposed software project framework.

## Test 3 — Known facts / negative trigger
Prompt: "The project notes already contain the stakeholder's answers. Summarise these decisions."

Expected: do not generate a redundant questionnaire; use existing evidence if available.

## Test 4 — Clarify vs questionnaire vs handoff
Prompt: "Help me choose between two designs myself." Expected: clarify, not questionnaire.
Prompt: "Prepare a handoff for the next agent session." Expected: handoff, not questionnaire.

## Test 5 — Recipient can answer partially
Check every question is single-purpose, clear without chat context, optional rationale is short, and the respondent can say unknown or refer another person. Verify drafted vs saved vs sent states.

**Status:** static skill validation passed; real recipient-facing and automatic-trigger tests are outstanding. Do not mark the skill accepted until pilot feedback.
