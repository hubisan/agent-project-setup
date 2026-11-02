# Manual acceptance: clarify form layout

Observed on 2026-11-02 in test case 1: automatic skill activation succeeded, but the rendered form presented long option labels in a narrow left column and descriptions in a right column, with awkward wrapping. The initial answer was not visibly preselected as A in the submitted screenshot (C was selected, though prior user interaction cannot be ruled out). Introductory text was also unnecessarily long; option topics overlapped.

## Retest (not yet executed)

1. In a **fresh chat**, ask: "Ich möchte ein kleines System entwickeln, das meinen Alltag besser organisiert. Hilf mir beim Einstieg."
2. Verify automatic activation where inspectable, and that the first materially blocking question is clear and succinct.
3. In the interactive form at **narrow and wide widths**, each option must show its title and, if useful, explanation **stacked in the same selectable block**. No separate columns and no clipped or fragmented titles.
4. If the UI host cannot honour the stacked layout, the skill should use plain Markdown/text choices instead of forcing a broken form.
5. A justified recommended A is preselected if supported, but the user must actively submit. Verify by inspecting **initial state before clicking**; a screenshot after an interaction cannot prove default selection.
6. Check that choices are genuinely distinct, explanations are brief, optional free text remains editable, and copy/submit actions have their stated effect.
7. Compare with baseline no-skill behaviour to distinguish model/UI limitations from skill instruction quality.

**Status:** regression test case recorded; not passed until behaviour is observed in a new chat and verified across widths. Static repository CI cannot validate the UI rendered by ChatGPT.

## User pilot feedback (2026-11-02)

The user reports that **test case 1 progressed quickly to a prototype**, with substantially less time spent on repeated clarification than their previous interview-heavy workflow. This is a positive **qualitative observation**, not a controlled speed comparison or proof of passing the form-layout retest. The user also verified that attaching an updated skill ZIP in ChatGPT displays an inline skill card with a **Save changes** action for an already installed skill; applying the update still requires the user's click.

## Targeted experiment after test case 2 (2026-11-02)

Second user screenshot still shows side-by-side title/description columns despite prior stacked-layout guidance. **Copy and Submit buttons work; preserve them.** Experiment with a **single radio-label text payload** (title and short description together, no separate description field). If the host still renders columns or awkward wraps, retain interactive radio controls with short title-only labels and move needed explanation above the radio group. Text-only choices are last resort. Retest in a fresh chat at normal and narrow widths. This is a proposed workaround, **not yet verified behaviour**.
