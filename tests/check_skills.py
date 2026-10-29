#!/usr/bin/env python3
"""Validate skill catalog and accepted skill entrypoints."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
catalog = (ROOT / "docs/skills.md").read_text(encoding="utf-8")
phases = (ROOT / "docs/phases.md").read_text(encoding="utf-8")
planned = {
    "adopt-project-setup", "project-retro", "clarify-project",
    "discover-project", "research-project", "shape-project",
    "plan-project", "review-project", "handoff-project",
}
for name in planned:
    assert name in catalog, f"missing candidate: {name}"
    assert name in phases, f"phase map missing: {name}"
assert "not yet accepted" in catalog, "missing maturity statement"

skills = sorted((ROOT / ".agents/skills").glob("*/SKILL.md"))
for file in skills:
    data = file.read_text(encoding="utf-8")
    assert data.startswith("---\n"), file
    name = re.search(r"(?m)^name: ([a-z][a-z0-9-]+)$", data)
    assert name and name.group(1) == file.parent.name, file
    assert re.search(r"(?m)^description: .{30,}$", data), file
    assert file.parent.name in planned, file
print(f"OK: {len(planned)} candidates catalogued, {len(skills)} active skills checked")
