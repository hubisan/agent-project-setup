# ChatGPT native form template (pilot v0.3.5)

This is a **rendering contract and example**, not HTML to inject into a ChatGPT message. The original HTML reference is optional and is **not** executed by the host. Prefer the ChatGPT-native form controls demonstrated in the 2026-11-11 pilot. If those controls are unavailable, use the text fallback in `question-presentation.md`. Do not claim that custom HTML/JS inside a skill runs automatically.

## Input data and normalization

Provide an array of user-owned questions, each with:
- `id`: stable `Q1`, `Q2`, ...
- `title`: concise question, `context` optional
- `options`: meaningful choices **in recommended-first order**; each has `title` and optional `description`
- `recommendedIndex`: 0 when there is a justified recommendation; otherwise no preselected choice

Before rendering:
1. Put the justified recommendation at index 0. **A must be the recommended choice**; never merely assign an internal `value="A"` to a visually unlabelled option.
2. Add exactly one last option `Other / own solution` using the next letter (`C` after two choices, `D` after three).
3. Render each choice as **one radio** with an explicit **visible** prefix `A –`, `B –`, etc. Mark A `(recommended)`. Use a bold title, then a short optional normal-weight explanation inside the same radio.
4. The recommended A starts selected only when justified; a default **never counts as consent**.
5. Show one separate free-text field when Other is selected (or an always-visible labelled field if conditional controls fail); also show an independent optional remarks field.
6. Display 3–5 independent user-owned questions in the same round when relevant; no fabricated questions.

## Native ChatGPT component pattern

Use the host's supported hooks and controls, adapting only question data. The following is schematic, showing **visible labels** and state flows; it is not an executable HTML file:

```jsx
{@body const questions = [
  {id:"Q1", title:"Which approach?", choices:[
    {title:"Recommended approach", description:"Reason and trade-off"},
    {title:"Alternative", description:"Distinct choice"}
  ]}
]}
{@body const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
{@body const [selected,setSelected] = DIL.useState(["A"])}
{@body const [own,setOwn] = DIL.useState([""])}
{@body const [remarks,setRemarks] = DIL.useState("")}
{@body const [error,setError] = DIL.useState("")}
{@body const formatted = () => questions.map((q,i) => {
  const n = letters.indexOf(selected[i]);
  const isOther = n === q.choices.length;
  return q.id + ": " + selected[i] + " – " +
    (isOther ? "Other / own solution\n    Own answer: " + own[i].trim() : q.choices[n].title);
}).join("\n") + (remarks.trim() ? "\n\nRemarks:\n" + remarks.trim() : "")}
{@body const valid = () => questions.every((q,i) =>
  letters.indexOf(selected[i]) !== q.choices.length || own[i].trim().length > 0)}
{#each questions as q,i}
  <text weight="semibold">{q.id} – {q.title}</text>
  <radio-group direction="col" value={selected[i]} onChange={v=>setSelected(prev=>prev.map((x,j)=>j===i?v:x))}>
    {#each q.choices as c,j}
      <radio value={letters[j]}>
        **{letters[j]} – {c.title}{j===0?" (recommended)":""}**{c.description?" – "+c.description:""}
      </radio>
    {/each}
    <radio value={letters[q.choices.length]}>
      **{letters[q.choices.length]} – Other / own solution**
    </radio>
  </radio-group>
  {#if selected[i]===letters[q.choices.length]}
    <label>Own answer for {q.id}</label>
    <textarea value={own[i]} onChange={v=>setOwn(prev=>prev.map((x,j)=>j===i?v:x))}/>
  {/if}
{/each}
<label>Optional remarks</label>
<textarea value={remarks} onChange={setRemarks}/>
{#if error}<text color="danger">{error}</text>{/if}
<button onClick={()=>{if(!valid()){setError("Complete your own answer.");return}setError("");GenUI.copy(formatted())}}>
  Copy answers
</button>
<button onClick={()=>{if(!valid()){setError("Complete your own answer.");return}GenUI.issueNewTurn(formatted())}}>
  Submit answers
</button>
```

### Implementation safeguards

- The actual control syntax and actions must match the **current host's available components**. This template is an example to adapt, not a guarantee that every ChatGPT client supports identical rendering.
- Initial `selected` and `own` state arrays must match the number of questions. If no defensible recommendation exists, do not default to A; use a conversational question or genuinely unselected supported control.
- Both buttons must call **the same** `formatted()` serializer, including every selected answer, own-answer text and optional remarks. Copy must not submit; Submit must send a user turn via a supported action, not only display a preview.
- `Other` must require text (or expressly capture that it was intentionally left blank if the host cannot validate).
- Never split the label and its description into columns, or rely on a radio's `value` as visible lettering.
- Check 1-question, 3-question, Other, comments, both buttons, and narrow viewport in a freshly installed skill. A correct source is not proof that the UI renders correctly.

## Portability

For Claude and terminal sessions, preserve the **same semantics** (IDs, choices, recommendations, custom replies, remarks) using host-supported presentation. Do not force ChatGPT components on those hosts. Terminal fallback: numbered questions, explicit A/B/C labels, recommended A as a suggested default, then prompt for Other text and optional remarks.
