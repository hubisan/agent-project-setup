# Question presentation

Shared presentation rules for APS questioning workflows, including a future `aps-brainstorm`. Reuse this guidance rather than redefining question formatting in every skill; it does not require invoking a separate form skill.

## Choose the presentation

- Do not repeat a long introduction both before and inside a question. Keep setup proportional to the decision, and ensure options are genuinely distinct rather than overlapping directions.
- Use a simple conversational question when choices are not helpful. Use a single question when its answer blocks meaningful follow-ups; otherwise group related or independent questions when the host makes that easier.
- **Layout (required):** render each answer as a single *vertical* block: radio button with option title, then its short explanation **directly below that title** inside the same option. Never use a label/description two-column layout, aligned table cells or side-by-side boxes; these squeeze titles and cause awkward line breaks. Keep explanations short and omit obvious ones. If the interactive form cannot reliably render this layout at narrow and wide widths, use clean Markdown/plain text instead of an awkward form.
- Respect natural-language requests such as "one at a time", "briefly" or "several together". Use interactive controls when supported, and preserve the same content and choices in plain Markdown or text.
- Show a multi-question round's general-comments field. When supported, include **two actions**: **Copy answers** (copy formatted selections and free-text remarks to the clipboard without submitting) and **Submit answers** (send them). Copy lets users paste the answers into the normal chat composer and attach images/files before sending. Do not promise to place text directly in the composer unless the host supports that action. Keep navigation and progress indicators meaningful; never invent a fixed total.

## Write each question

1. **Number and title.** Use stable identifiers `Q1`, `Q2`, `Q3`, etc. Start at Q1 for a new clarification topic; continue sequentially across rounds or when resuming the same topic. Do not renumber existing questions.
2. **Optional context.** Under the question title, add a brief explanation of the situation, scope or consequence **only when the title alone would leave the user unsure what is being decided**.
3. **Options.** When offering choices, place the **recommended option first as A**, with a concise explanation of why and its most relevant trade-off. Put genuinely distinct alternatives after it as B and C (as applicable), and offer **D - Other / own solution** with free text. If there is no defensible recommendation yet, disclose that instead of inventing one.
4. **Optional option descriptions.** Add short explanations below individual choices **only if their titles leave meaning or consequences unclear**.
5. **Human choice and defaults.** In supported interactive single-choice controls, **preselect recommended A** so users can quickly accept the recommendation or choose another option. Keep the selection editable and require an explicit user submission; a preselection alone is **never consent**. Do not invent a selection in plain text or when there is no justified recommendation. Support qualified replies such as "B, but..." and preserve general comments.

## Visual example (structure, not fixed content)

For an interactive single-choice question, use this semantic order for **each** option:

```text
(●) A — Recommended option
    One brief explanation directly underneath.
( ) B — Alternative option
    One brief explanation directly underneath.
( ) C — Another genuinely distinct option
    One brief explanation directly underneath.
( ) D — Other / combination
```

Radio title and explanation must be in the *same selectable block*; do not make a separate label column and description column. The recommendation must be preselected **only if defensible** and remain editable. Provide a compact comment field and adjacent copy/submit actions when interactive controls genuinely help. Check readability at both narrow and wide viewport widths; if it wraps awkwardly, fall back to plain text.

## After each round

Update the active question frontier. Reuse established answers, research factual unknowns, decide safe defaults, consolidate overlapping questions, and defer non-blockers before asking again. Summarise only at consequential milestones or when an answer materially changes other choices, rather than after every round. Stop questioning when meaningful work can continue.
