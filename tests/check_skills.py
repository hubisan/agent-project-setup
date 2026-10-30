#!/usr/bin/env python3
"""Check the planned APS skill catalog and phase navigation."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
catalog = (root / "docs/skills.md").read_text()
phases = (root / "docs/phases.md").read_text()
names = ("frame", "analyze", "design", "plan", "validate", "clarify",
         "brainstorm", "research", "review", "improve", "handoff", "adopt")
for name in names:
    assert "aps-" + name in catalog
    assert "aps-" + name in phases
for phase in ("Clarify", "Understand", "Design", "Plan", "Execute", "Review"):
    assert phase in phases
skills = sorted((root / ".agents/skills").glob("*/SKILL.md"))
for path in skills:
    data = path.read_text()
    assert data.startswith("---\n"), path
    name = re.search(r"(?m)^name: ([a-z][a-z0-9-]+)$", data)
    assert name and name.group(1) == path.parent.name, path
    assert name.group(1) in {"aps-" + n for n in names}, path
    assert re.search(r"(?m)^description: .{30,}$", data), path
print(f"OK: {len(names)} planned APS skills, {len(skills)} installed")
