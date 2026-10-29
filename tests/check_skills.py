#!/usr/bin/env python3
"""Lightweight static checks for phase-skill metadata and references."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOC = (ROOT / "docs/phases.md").read_text()
skills = sorted((ROOT / ".agents/skills").glob("*/SKILL.md"))
required = {
    "adopt-project-setup", "discover-project", "shape-project",
    "plan-project", "review-project", "handoff-project",
}
found = {file.parent.name for file in skills}
assert required <= found, f"missing core skills: {sorted(required - found)}"
for file in skills:
    data = file.read_text()
    assert data.startswith("---\n"), file
    name = re.search(r"(?m)^name: ([a-z][a-z0-9-]+)$", data)
    assert name and name.group(1) == file.parent.name, file
    assert re.search(r"(?m)^description: .{30,}$", data), file
    assert re.search(r"(?m)^\*\*Done:\*\*", data), file
    assert file.parent.name in DOC, file
for keyword in ("no application", "no-code", "wiki", "handoff"):
    assert keyword.lower() in (
        DOC + "\n" + (ROOT / "docs/architecture.md").read_text()
        + "\n" + "".join(f.read_text() for f in skills)
    ).lower()
print(f"OK: {len(skills)} phase skills validated")
