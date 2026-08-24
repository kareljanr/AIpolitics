# -*- coding: utf-8 -*-
"""Merge Travie race dual into EVERY-10 files; keep Kiemkracht as primary."""
from __future__ import annotations

import csv
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)


def git_show(path: str) -> str:
    raw = subprocess.check_output(
        ["git", "-C", str(ROOT), "show", f"HEAD:{path}"],
    )
    return raw.decode("utf-8")


prog = git_show("docs/doge/data/progress_every_10_ticks.md")
prog = prog.replace(
    "· **Kiemkracht** omzet **13.26m** / bruto≫omzet **~1.41x** / pnl DROP **-75%** (EVERY-10 primary) Medium",
    "· **Kiemkracht** omzet **13.26m** / bruto≫omzet **~1.41x** / pnl DROP **-75%** (EVERY-10 primary) · race **Travie** bruto **11.39m** / ~**2.84×** / pnl DROP **-89%** · post **De Vleugels** bruto **35.11m** / ~**7.37×** Medium",
)
prog = prog.replace(
    "· **Kiemkracht** · prior 2211-2220 stack retained)",
    "· **Kiemkracht** · race **Travie** · post **De Vleugels** · prior 2211-2220 stack retained)",
)
prog = prog.replace(
    "· **Kiemkracht** (EVERY-10 primary — omzet JUMP **13.26m** **+9%**; bruto≫omzet **~1.41x**; pnl DROP **-75%**; equity JUMP; FTE JUMP **404.4**; Medium CW; FOI ready).",
    "· **Kiemkracht** (EVERY-10 primary — omzet JUMP **13.26m** **+9%**; bruto≫omzet **~1.41x**; pnl DROP **-75%**; equity JUMP; FTE JUMP **404.4**; Medium CW; FOI ready) · race **Travie** (bruto **11.39m** / omzet **4.01m** ~**2.84×**; pnl DROP **-89%**; FTE **496**; Medium CW; FOI ready) · post-2230 **De Vleugels** (bruto **35.11m** ~**7.37×** omzet; equity **35.35m**; FTE **442.8**; Medium CW; FOI ready).",
)
prog = prog.replace("| FOI ready | ~1876 |", "| FOI ready | ~1878 |")
prog = prog.replace("| FOI total rows | ~1928 |", "| FOI total rows | ~1930 |")
prog = prog.replace("**~1876** drafts ready", "**~1878** drafts ready")
prog = prog.replace("total FOI rows **~1928**", "total FOI rows **~1930**")
prog = prog.replace(
    "research_queue open | rq_2231 after progress",
    "research_queue open | rq_2232 after Travie race + De Vleugels",
)
(DATA / "progress_every_10_ticks.md").write_text(prog, encoding="utf-8")

top = git_show("docs/doge/data/doge_waste_top10_current.md")
top = top.replace(
    "**Kiemkracht omzet 13.26m / pnl DROP -75%** (EVERY-10@2230 primary)",
    "**Kiemkracht omzet 13.26m / pnl DROP -75%** (EVERY-10@2230 primary) · **Travie bruto 11.39m / ~2.84× / pnl DROP −89%** (race@2230) · **De Vleugels bruto 35.11m / ~7.37×** (@2231)",
)
top = top.replace(
    "· **Kiemkracht omzet JUMP 13.26m / bruto≫omzet ~1.41x / pnl DROP -75% / FTE JUMP 404.4** (EVERY-10@2230 primary). Count NEW since 2220: ~13 residual dual fills.",
    "· **Kiemkracht omzet JUMP 13.26m / bruto≫omzet ~1.41x / pnl DROP -75% / FTE JUMP 404.4** (EVERY-10@2230 primary) · race **Travie bruto 11.39m / ~2.84× / pnl DROP −89%** · **De Vleugels bruto 35.11m / ~7.37×** (@2231). Count NEW since 2220: ~15 residual dual fills.",
)
top = top.replace(
    "- **Kiemkracht** EVERY-10 primary omzet JUMP **EUR13.26m (+9%)** / bruto≫omzet **~1.41x** / pnl DROP **-75%** / FTE JUMP **404.4** — Hamme maatwerk+Kringwinkel subsidy opacity.\n- **De Oever**",
    "- **Kiemkracht** EVERY-10 primary omzet JUMP **EUR13.26m (+9%)** / bruto≫omzet **~1.41x** / pnl DROP **-75%** / FTE JUMP **404.4** — Hamme maatwerk+Kringwinkel subsidy opacity.\n"
    "- **De Vleugels** bruto **EUR35.11m** / omzet **EUR4.77m** (~**7.37×**) / equity JUMP **EUR35.35m** / FTE **442.8** — VAPH disability dual.\n"
    "- **Travie** race dual bruto **EUR11.39m** / omzet **EUR4.01m** (~**2.84×**) / pnl DROP **−89%** / FTE **496** — Brussels ETA maatwerk.\n"
    "- **De Oever**",
)
top = top.replace("· **8047+** leaderboard rows", "· **8049+** leaderboard rows")
(DATA / "doge_waste_top10_current.md").write_text(top, encoding="utf-8")


def read_csv(name: str):
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(name: str, fields, rows):
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


rf, rq = read_csv("research_queue.csv")
for row in rq:
    if row.get("task_id") == "rq_2230":
        row["title"] = (
            "EVERY-10 + leftover dual — Kiemkracht YE2025 Medium (EVERY-10 primary) + "
            "race Travie YE2025 Medium (bruto 11.39m / ~2.84x / pnl DROP -89%)"
        )
        row["entity_id"] = "vzw_kiemkracht_hamme"
        row["notes"] = (
            "tick2230 EVERY-10 race: Kiemkracht 0454.343.743 primary (omzet JUMP 13.26m / "
            "pnl DROP -75%) + Travie 0420.015.938 race dual (bruto 11.39m ~2.84x / pnl DROP "
            "-89% / FTE 496); FOI both ready not sent; next every-10 2240"
        )
        row["instructions"] = (
            "Completed EVERY-10@2230 (Kiemkracht primary) + race Travie dual; preferred AGB "
            "Bornem JR2024 / FARO/AIESH/REW YE2024 / Heropbeuring CW opaque; Medium CW + "
            "Strong KBO; FOI ready not sent"
        )
        row["blocked_gap_id"] = (
            "gap_kiemkracht_nbb_pdf_assets_debt_bruto_gt_omzet_pnl_drop_75pct_matrix_l5"
        )
    if row.get("task_id") == "rq_2232":
        instr = row.get("instructions") or ""
        instr = instr.replace(
            "SDB/Travie/Rucher", "SDB/Le Rucher (Travie TAKEN race@2230)"
        )
        if "Do NOT redo Travie" not in instr:
            instr = instr.replace("Do NOT redo", "Do NOT redo Travie, ")
        row["instructions"] = instr
        notes = row.get("notes") or ""
        notes = notes.replace(
            "named FREE SDB/Travie/Rucher YE2025",
            "named FREE SDB/Le Rucher YE2025; Travie TAKEN race@2230",
        )
        row["notes"] = notes
        row["title"] = (row.get("title") or "").replace("SDB-Travie-Rucher", "SDB-Rucher")
write_csv("research_queue.csv", rf, rq)

txt = LOG.read_text(encoding="utf-8")
if "Travie race merge" not in txt:
    LOG.write_text(
        txt
        + """

## Tick 2230 race merge - 2026-08-26T22:50:00Z - Travie dual absorbed + EVERY-10 merge

- Race: concurrent agents — **Kiemkracht** committed as official EVERY-10@2230; this agent filled **Travie** YE2025 Medium (bruto 11.39m / ~2.84x / pnl DROP -89% / FTE 496) with FOI ready; De Vleugels closed rq_2231.
- Merged Travie + De Vleugels into `progress_every_10_ticks.md` + `doge_waste_top10_current.md` (Kiemkracht remains EVERY-10 primary). FOI draft `gap_travie_...` ready not sent.
- Next: rq_2232 (AGB/FARO-if-YE2025 / AIESH-REW / SDB-Rucher-or-unused). Next every-10 **2240**.
""",
        encoding="utf-8",
    )

print("merged OK")
