#!/usr/bin/env python3
from pathlib import Path
ROOT = Path("/workspace/AIpolitics")
p = ROOT / "docs/doge/loop_log.md"
raw = p.read_bytes()
if raw and not raw.endswith(b"\n"):
    raw += b"\n"
block = (ROOT / "docs/doge/data/_tick1562_logblock.md").read_text(encoding="utf-8")
block = block.replace("2026-08-20TPLACEHOLDERZ", "2026-08-20T08:07:13Z", 1)
if not block.endswith("\n"):
    block += "\n"
p.write_bytes(raw + block.encode("utf-8"))
print("loop_log appended", len(block))
