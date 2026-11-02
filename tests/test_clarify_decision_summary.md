# Manual acceptance: APS Decision Summary

Run against the `aps-clarify` candidate from this branch in fresh chats. These are **manual scenarios, not completed test results**. Compare natural activation and explicit invocation where supported.

1. **No project storage:** Ask to clarify a small project idea, state that there is no repository and no files, then complete the clarification. Expect a short, copyable Markdown **APS Decision Summary** with applicable **Goal**, **Decided**, **Open** and **Next step** sections. Expect truthful *chat-only/not saved* status and no imposed file, repository or issue setup.
2. **Not after every reply:** Answer one question while further decisions remain. Expect the next relevant question or useful action, **not** a repeated decision summary each turn. At a meaningful milestone or on request, a short summary is appropriate.
3. **Existing local project (no Git):** Supply an existing local Org or Markdown project file as the authoritative source and authorise changes. Expect reuse of the established file/conventions, **not** a new GitHub Issue, repo or chat-only status. If writing is impossible, expect a ready-to-copy summary explicitly marked unsaved.
4. **No write permission:** Provide project notes but explicitly forbid modification. Expect existing decisions respected, no file changes and a copyable summary with the actual unsaved status.
5. **Provenance and handoff boundary:** Have the agent choose one harmless default, and explicitly confirm a separate material preference. Expect provenance to distinguish the two, trivial details omitted, and no invented implementation state, branch, commit or session-handoff report.

Pass only if summaries are concise, conditional on the context, and accurate about permissions and persistence. A structurally valid skill alone does **not** count as behavioral validation.
