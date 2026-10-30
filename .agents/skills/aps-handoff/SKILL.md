---
name: aps-handoff
description: Create or resume a session handoff between chats, agents, or users. Use when pausing work for another session, handing work to Claude Code, Codex, or ChatGPT, or continuing from a specific handoff Issue. Prefer labelled GitHub Issues in the working repository; fall back to portable Markdown when Issue access is unavailable.
---

# APS Session Handoff

Treat a handoff as a **temporary context pointer**, not as a work ticket or a replacement for committed files. The target repository's tickets, specs, ADRs and established decisions remain authoritative. Each handoff has its **own GitHub Issue number**; never reuse a shared `HANDOFF.md` or guess the latest Issue belongs to this session.

## Create a handoff

1. **Find the work's home.** Identify `owner/repo`, the active work ticket(s), relevant authoritative artifacts and the current branch. Follow the repository's `AGENTS.md` and permission rules; do not move the work to another repository.
2. **Verify actual state.** Inspect the worktree or GitHub branch, HEAD commit, uncommitted/unpushed changes, open PRs, checks and remaining blockers. Preserve the current work branch. If required changes exist only locally, arrange an authorised commit/push before promising transfer; otherwise flag them as **not transferred**. Create a temporary branch only for a concrete need, never as the default handoff transport.
3. **Redact.** Keep credentials, personal information, private chat context, internal details and sensitive URLs out of Issue titles and bodies. Check whether the target repository is public. Reference safe, durable sources rather than copying specs, ADRs, ticket bodies or lengthy discussions.
4. **Ensure Issue capability and label.** Verify permission to create/read Issues and that `session-handoff` exists. Create this label through the available GitHub API/UI when authorised. In a Linux terminal, if needed: `gh label create session-handoff --repo owner/repo --color 8250df --description "Temporary session continuation record"`. Never create an unlabelled substitute for a work ticket. If GitHub/label access is unavailable, use the Markdown fallback below.
5. **Create one new labelled Issue per handoff.** Title: `[session-handoff] <safe short workstream>`; apply `session-handoff` at creation. Use the compact content contract below. With GitHub CLI: `gh issue create --repo owner/repo --title "[session-handoff] <workstream>" --label session-handoff --body-file <local-temporary-file>`. Other agents use their native GitHub connector/API with equivalent fields. A temporary file may be used only as command input, not as the canonical handoff.
6. **Verify before reporting success.** Read the returned Issue ID and fetch that exact Issue again. Confirm repository, title, `session-handoff` label, Issue body and open state. On an ambiguous creation failure, check whether an Issue was already created **before retrying**, to avoid duplicates. If verification fails, report the partial result and retain the Markdown fallback; do not invent an Issue ID.
7. **Return a short continuation prompt**, for example: `Continue in owner/repo from session-handoff Issue #47. Verify the current repository state before taking over.` Give the actual Issue URL when available, but no long copy-paste handoff.

## Compact Issue content contract

Include these headings, with concise, factual content and links (or `none` / `not checked` when relevant):

- `## Goal and current state` - purpose, completed work and what's in progress.
- `## Repository snapshot` - `owner/repo`, active branch, verified commit SHA, unpublished changes, PR and actual checks (passed/failed/not run).
- `## Sources of truth` - relevant work Issue(s), specs, ADRs, decisions and file paths/links; point, do not copy.
- `## Next action and blockers` - one concrete first action, remaining work, unresolved questions, risks and blockers.
- `## Suggested skills` - relevant skills to load if available; no invented installation claims.

Issue number is the transfer ID **within that repository**. It does not replace the work-ticket number. Never store code or unsaved changes only in an Issue.

## Resume a handoff

1. **Read the exact Issue** identified by the user as `owner/repo#number`; confirm its repository, `session-handoff` label, and open state. Do not select an Issue by recency or overwrite another handoff. A closed Issue is historical; ask for an explicit reason before reopening.
2. **Read and reconcile:** inspect its linked work tickets, specs, ADRs and decisions selectively; verify the actual repository branch and current commit, available working files, PRs and checks. The present verified repository state wins over a stale snapshot. Note any changes made since the handoff, missing/unpushed work or incompatible state. Do not silently reset or force-push.
3. **Establish usable continuation:** identify the specific next action, access and any blocker. If critical references are missing, the branch cannot be accessed, or the state diverged in a way that prevents safe continuation, **leave the Issue open**, report the blocker and avoid claiming takeover.
4. **Acknowledge successful takeover** in a new comment on that Issue, naming the verified branch/commit, inspected sources and the immediate next action (and meaningful differences from the snapshot). Only then, after the comment is successfully posted and the Issue remains the correct open labelled handoff, **close this Issue**. Do not close any other Issue or the underlying work ticket. If posting or closing fails, report the actual state; it stays open until closure is verified.
5. **Continue working** using the existing branch and authoritative artifacts. Acknowledgement means context has been taken over, **not** that the underlying task is finished.

## Fallback and compatibility

If GitHub Issues or write access are unavailable, produce the same concise content as Markdown in an accessible user-visible artifact (or the operating system's temporary directory when supported); state **not published to GitHub** and give the user a realistic way to carry it forward. Do not claim that a local path is accessible to another agent.

The existing AI-Hero `handoff` skill can help draft a compact, redacted, source-linked summary and suggest skills. **Do not fork it.** Its OS-temp-file destination is optional scratch in this workflow; a verified GitHub Issue is the preferred finished handoff when the project supports it. This APS rule concerns **session continuity**, not wiki-to-project extraction or handoffs requiring human-only operations.

## Completion check

- **Create:** a verified open, correctly labelled Issue and usable short prompt, or an explicitly unpublished Markdown fallback; work state and permissions reported accurately.
- **Resume:** sources and current branch/commit verified, next action actionable, acknowledgement successfully posted **before** closing the exact handoff Issue; otherwise the Issue stays open.
- Parallel agents each use separate Issues. Neither creates a global pointer nor closes unrelated Issues.
