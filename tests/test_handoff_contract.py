#!/usr/bin/env python3
"""Structural regression tests for the APS session handoff contract.

These tests verify the documented protocol, not a live GitHub takeover.
The real cross-agent pilot remains a separate acceptance gate in Issue #20.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/aps-handoff/SKILL.md"
AGENTS = ROOT / "AGENTS.md"
CATALOG = ROOT / "docs/skills.md"
ARCH = ROOT / "docs/architecture.md"
README = ROOT / "README.md"


class HandoffContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.agents = AGENTS.read_text(encoding="utf-8")
        cls.catalog = CATALOG.read_text(encoding="utf-8")
        cls.arch = ARCH.read_text(encoding="utf-8")
        cls.readme = README.read_text(encoding="utf-8")

    def test_entrypoints_have_one_canonical_procedure(self):
        self.assertIn("name: aps-handoff", self.skill)
        self.assertIn(".agents/skills/aps-handoff/SKILL.md", self.agents)
        self.assertIn("](../.agents/skills/aps-handoff/SKILL.md)", self.catalog)
        self.assertIn("](../.agents/skills/aps-handoff/SKILL.md)", self.arch)
        self.assertIn("](.agents/skills/aps-handoff/SKILL.md)", self.readme)
        self.assertNotIn("## Create a handoff", self.agents)

    def test_content_is_compact_and_source_linked(self):
        for section in (
            "## Goal and current state", "## Repository snapshot",
            "## Sources of truth", "## Next action and blockers",
            "## Suggested skills",
        ):
            self.assertIn(section, self.skill)
        for field in ("commit SHA", "branch", "uncommitted", "checks", "ADRs"):
            self.assertIn(field, self.skill)
        self.assertIn("not as a work ticket", self.skill)
        self.assertIn("Redact", self.skill)

    def test_parallel_sessions_use_separate_issue_ids(self):
        self.assertIn("one new labelled Issue per handoff", self.skill)
        self.assertIn("own GitHub Issue number", self.skill)
        self.assertIn("never reuse a shared", self.skill)
        self.assertIn("Do not select an Issue by recency", self.skill)
        self.assertIn("Parallel agents each use separate Issues", self.skill)

    def test_cross_agent_takeover_has_acknowledgement_gate(self):
        for agent in ("Claude Code", "Codex", "ChatGPT"):
            self.assertIn(agent, self.skill)
        self.assertIn("Read the exact Issue", self.skill)
        self.assertIn("Read and reconcile", self.skill)
        self.assertIn("Acknowledge successful takeover", self.skill)
        self.assertIn("Only then, after the comment is successfully posted", self.skill)
        self.assertIn("close this Issue", self.skill)
        self.assertIn("work ticket", self.skill)

    def test_failures_leave_handoff_open(self):
        self.assertIn("leave the Issue open", self.skill)
        self.assertIn("not transferred", self.skill)
        self.assertIn("not published to GitHub", self.skill)
        self.assertIn("check whether an Issue was already created", self.skill)
        self.assertIn("Do not silently reset or force-push", self.skill)

    def test_issue_label_and_upstream_skill_compatibility(self):
        self.assertIn("session-handoff", self.skill)
        self.assertIn("gh label create", self.skill)
        self.assertIn("--label session-handoff", self.skill)
        self.assertIn("Do not fork it", self.skill)
        self.assertIn("temporary directory", self.skill)
        self.assertIn("coding-agent-setup/issues/32", self.arch)


if __name__ == "__main__":
    unittest.main()
