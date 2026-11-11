# aps-clarify v0.3.5 — ChatGPT native-form regression (manual)

Status: **not yet executed against a freshly installed 0.3.5 skill**.

The user successfully tested the underlying native-form pattern in a normal ChatGPT conversation on 2026-11-11: Q1=A native ChatGPT form; Q2=A native Claude presentation preferred; Q3=A numbered terminal text fallback; submitted answers and remarks ("hat geklappt") arrived in the chat. This proves that single in-chat prototype submitted successfully, **not** that installing a new skill follows the pattern every time or that the Copy action was tested.

## Test procedure

Install a single-skill ZIP containing SKILL.md, agents/openai.yaml, assets/search-check.svg, assets/chatgpt-form-template.md, references/question-presentation.md, and any other referenced assets. Start a **fresh** ChatGPT conversation.

- [ ] Three independent questions appear in one round with correct Q1/Q2/Q3.
- [ ] Visible radio labels begin A, B, C (internal values alone do not count).
- [ ] First visible option is recommended and A is preselected, where justified.
- [ ] Other is last and labelled with the next letter for the actual option count.
- [ ] Selecting Other shows a distinct editable text field, required for Submit.
- [ ] Remarks are optional, independent of Other, and retained.
- [ ] Copy answers includes the selected letters, choice titles, custom answers and remarks; does not submit.
- [ ] Submit sends the **same** formatted content back into the chat.
- [ ] Narrow-screen layout keeps each option in one flowing radio, not split columns.
- [ ] A resumed round continues stable question numbering.
- [ ] An unsupported native UI uses full-featured plain-text fallback.
- [ ] Skill does not claim HTML is executable in ChatGPT or that a default means consent.

Record screenshots, skill ZIP version, observed results and failures in issue #14. Keep PR unmerged until manual acceptance.
