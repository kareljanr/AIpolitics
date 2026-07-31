# -*- coding: utf-8 -*-
"""Tick 163: patch research_queue + foi_queue without encoding corruption."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # docs/doge/data

# --- research_queue ---
p = ROOT / "research_queue.csv"
text = p.read_text(encoding="utf-8")
old = None
for line in text.splitlines():
    if line.startswith("rq_158,"):
        old = line
        break
if not old:
    raise SystemExit("rq_158 not found")

new = (
    "rq_158,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"
    '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register univ per-institution '
    'VIPA Mons BI2026 bpost USO HR Rail) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    "gap_univ_per_institution,2026-07-28T04:05:00Z,2026-07-28T04:25:00Z,"
    '"tick163: CRC HO 2024 per-uni L5: results/invest/students/VTE all 5; 1st stream implied UGent 428m UA 207m '
    'VUB 166m UHasselt 94m medium + KUL strong; residual AHOVOKS exact+FWB FOI; spawn rq_159"'
)
text2 = text.replace(old, new, 1)
if not text2.endswith("\n"):
    text2 += "\n"
if "rq_159," not in text2:
    text2 += (
        "rq_159,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"
        '"Prefer public primary fills (De Lijn 2025-26 full perimeter Antwerp register VIPA Mons BI2026 '
        'bpost USO HR Rail FWB univ dots) if new PDFs appear; else next open rq; do not idle while public work remains.",'
        ",2026-07-28T04:25:00Z,,"
        '"Spawned tick163 after univ per-inst CRC; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
p.write_text(text2, encoding="utf-8", newline="\n")
print("research_queue: rq_158 done, rq_159 present=", "rq_159," in text2)

# --- foi_queue ---
fp = ROOT / "foi_queue.csv"
ft = fp.read_text(encoding="utf-8")
lines = ft.splitlines(keepends=True)
out = []
found = False
for line in lines:
    if line.startswith("gap_univ_per_institution,"):
        found = True
        out.append(
            "gap_univ_per_institution,BE>Universities>operating_grants_L5,sec_flanders,"
            "AHOVOKS exact cash-by-year werkingsuitkering matrix 2023-2026 (5 VL unis) + FWB university operating dots by institution; CRC 2024 implied matrix medium fill only,"
            "KUL strong JV + CRC results/students/VTE all 5; 1st stream UGent~428m UA~207m VUB~166m UHasselt~94m medium reverse-engineered; AHOVOKS exact + FWB still opaque,"
            "6,AHOVOKS / Team Openbaarheid + FWB Enseignement,openbaarheid@vlaanderen.be,Havenlaan 88 bus 20 1000 Brussel,"
            "docs/doge/foi/drafts/gap_univ_per_institution.md,ready,2026-07-27,,,,,"
            "cmt_vl_univ_per_inst_matrix_2024,lb_vl_univ_per_inst_matrix,"
            "2026-07-27T23:15:00Z,2026-07-28T04:25:00Z,"
            "tick149 partial |tick163: CRC per-uni results+implied 1st; residual AHOVOKS exact+FWB human send\n"
        )
    else:
        out.append(line)
if not found:
    raise SystemExit("gap_univ_per_institution not found")
fp.write_text("".join(out), encoding="utf-8", newline="\n")
print("foi_queue: gap_univ updated")
