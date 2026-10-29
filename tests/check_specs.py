#!/usr/bin/env python3
"""Check presence and traceability of the approved specification."""
from pathlib import Path
import re

spec = Path(__file__).resolve().parents[1] / "docs" / "spec-v2"

for stem in ("spezifikation", "entscheidungsregister", "akzeptanz-und-umsetzung"):
    for suffix in (".org", ".md"):
        file = spec / (stem + suffix)
        assert file.is_file(), f"missing: {file}"
        assert file.stat().st_size > 10_000, f"unexpectedly short: {file}"

docs = {name: (spec / (name + ".md")).read_text(encoding="utf-8")
        for name in ("spezifikation", "entscheidungsregister", "akzeptanz-und-umsetzung")}

for name, prefix, count, width in (
    ("spezifikation", "R", 40, 2),
    ("entscheidungsregister", "Q", 121, 3),
    ("akzeptanz-und-umsetzung", "AK", 52, 2),
):
    for i in range(1, count + 1):
        identifier = f"{prefix}{i:0{width}}"
        assert re.search(r"\b" + identifier + r"\b", docs[name]), f"missing {identifier}"

for file in spec.glob("*.md"):
    for url in re.findall(r"\]\(([^)]+)\)", file.read_text(encoding="utf-8")):
        if url.startswith(("http:", "https:", "mailto:", "#")):
            continue
        assert (file.parent / url.split("#", 1)[0]).is_file(), f"bad link: {file}: {url}"

for file in spec.glob("*.org"):
    for url in re.findall(r"\[\[file:([^\]]+)", file.read_text(encoding="utf-8")):
        target = url.split("::", 1)[0]
        if target:
            assert (file.parent / target).is_file(), f"bad link: {file}: {url}"

print("OK: six source documents, 40 requirements, 121 decisions, 52 acceptance scenarios, and links")
