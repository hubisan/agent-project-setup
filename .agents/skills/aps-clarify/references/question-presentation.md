# Question presentation

Shared presentation rules for APS questioning workflows, including a future `aps-brainstorm`. Reuse this guidance rather than redefining question formatting in every skill; it does not require invoking a separate form skill.

For ChatGPT interactive forms, see [the ChatGPT native form template](../assets/chatgpt-form-template.md) for the tested rendering pattern and shared answer serialization. Do not mistake internal radio values for visible A/B/C labels. This reference remains host-neutral when native controls are unavailable.

## Choose the presentation

- Do not repeat a long introduction both before and inside a question. Keep setup proportional to the decision, and ensure options are genuinely distinct rather than overlapping directions.
- Use a simple conversational question when choices are not helpful. Use a single question when its answer blocks meaningful follow-ups; otherwise group related or independent questions when the host makes that easier.
- **Inline radio content (required):** within each single radio option, place the **bold title** followed immediately by an optional regular-weight description on the **same flowing line**. Example: `**A – Meal planning (recommended)** – Select recipes and prepare the shopping list.` The full option should naturally wrap across the available width. Do not author a separate description field, side column, grid, table or sibling layout. Omit descriptions when labels suffice. If the host still creates two columns, use short title-only radios and put essential explanation above the group. Preserve the working **Copy answers** and **Submit answers** controls.
- Respect natural-language requests such as "one at a time", "briefly" or "several together". Use interactive controls when supported, and preserve the same content and choices in plain Markdown or text.
- Show a multi-question round's general-comments field. When supported, include **two actions**: **Copy answers** (copy formatted selections and free-text remarks to the clipboard without submitting) and **Submit answers** (send them). Copy lets users paste the answers into the normal chat composer and attach images/files before sending. Do not promise to place text directly in the composer unless the host supports that action. Keep navigation and progress indicators meaningful; never invent a fixed total.

## Write each question

1. **Number and title.** Use stable identifiers `Q1`, `Q2`, `Q3`, etc. Start at Q1 for a new clarification topic; continue sequentially across rounds or when resuming the same topic. Do not renumber existing questions.
2. **Optional context.** Under the question title, add a brief explanation of the situation, scope or consequence **only when the title alone would leave the user unsure what is being decided**.
3. **Options.** When offering choices, place the **recommended option first as A**, with a concise explanation of why and its most relevant trade-off. Put genuinely distinct alternatives after it as B and C (as applicable), and offer **Other / own solution** as the final option, labelled with the next available letter (C, D, E, etc.), with free text. Do not pad the options to a fixed count. If there is no defensible recommendation yet, disclose that instead of inventing one.
4. **Optional option descriptions.** If needed, include short normal-weight explanations inline after the bold title inside the same radio option; never place them in a separate description area.
5. **Human choice and defaults.** In supported interactive single-choice controls, **preselect recommended A** so users can quickly accept the recommendation or choose another option. Keep the selection editable and require an explicit user submission; a preselection alone is **never consent**. For the final **Other / own solution** option, reveal a dedicated free-text field directly underneath when selected if conditional controls are supported. Otherwise include an always-visible, clearly labelled custom-answer field. Keep it separate from optional general remarks, including in single-question rounds. Do not invent a selection in plain text or when there is no justified recommendation. Support qualified replies such as "B, but..." and preserve general comments.

## Visual example (structure, not fixed content)

Use **one radio option with inline formatting** for its title and optional description:

```text
(●) **A — Recommended option** – Short explanation if needed.
( ) **B — Alternative option** – Short explanation if needed.
( ) **C — Distinct option** – Short explanation if needed.
( ) D — Other / combination
```

**If that still causes a two-column layout**, keep interactivity and put any necessary clarifications *before* the options:

```text
Brief context (only if needed): A means ..., B means ...
(●) A — Recommended option
( ) B — Alternative option
( ) C — Distinct option
( ) D — Other / combination
```

Keep title bold and description normal-weight, inline in the same radio option. Never create separate description fields for each radio option. The recommendation must be preselected only when defensible, remain editable, and require an explicit user submission. Preserve the dedicated custom-answer field, the separate compact optional-comment field and the **working copy/submit buttons**. Group 3–5 independent questions per round rather than asking them serially; reserve single-question rounds for real blockers or when only one user decision is necessary. Check narrow and wide views in the real host; use plain text only if even the label-only version is poor.

## After each round

Update the active question frontier. Reuse established answers, research factual unknowns, decide safe defaults, consolidate overlapping questions, and defer non-blockers before asking again. Summarise only at consequential milestones or when an answer materially changes other choices, rather than after every round. Stop questioning when meaningful work can continue.
