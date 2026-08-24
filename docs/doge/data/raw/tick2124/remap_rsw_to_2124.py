# -*- coding: utf-8 -*-
"""Race recovery: concurrent tick took rq_2123 as Home Sebrechts; remap RSW to tick 2124."""
import csv
import os
import re
import shutil
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T11:25:00Z"
ENTITY = "sa_rsw_residence_seniors_westland"
GAP = "gap_rsw_nbb_pdf_assets_debt_pnl_flip_loss_equity_drop_matrix_l5"

src = Path("docs/doge/data/raw/tick2123")
dst = Path("docs/doge/data/raw/tick2124")
dst.mkdir(parents=True, exist_ok=True)
for f in src.glob("rsw_*"):
    shutil.copy2(f, dst / f.name)
os.system("git checkout HEAD -- docs/doge/data/raw/tick2123/apply_tick2123.py")

rq = "docs/doge/data/research_queue.csv"
with open(rq, newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)

seen = set()
out = []
for row in rows:
    tid = row.get("task_id")
    if tid in ("rq_2124", "rq_2125") and tid in seen:
        continue
    if tid:
        seen.add(tid)
    out.append(row)
rows = out
has_2125 = any(x.get("task_id") == "rq_2125" for x in rows)

for row in rows:
    if row.get("task_id") == "rq_2123":
        row["status"] = "done"
        row["entity_id"] = "nv_home_sebrechts"
        row["title"] = "leftover dual — Home Sebrechts Mechelen YE2025 Medium"
        row["notes"] = "tick2123 Home Sebrechts YE2025 Medium CW; FOI ready not sent; next rq_2124; next every-10 2130"
        row["blocked_gap_id"] = "gap_sebrechts_nbb_pdf_assets_debt_bruto_drop_fte_drop_matrix_l5"
    if row.get("task_id") == "rq_2124":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["title"] = "leftover dual — R.S.W. Residence Senior's Westland YE2025 Medium"
        row["instructions"] = (
            "Completed leftover dual R.S.W. after Home Sebrechts; "
            "preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; live YE2025 Medium CW NL+EN+FR + Strong KBO 0459.540.765; "
            "omzet JUMP 312k pnl FLIP LOSS -34.8k equity DROP 5.12m bruto JUMP 415k FTE Medium 0; FOI ready NBB PDF; "
            "DISTINCT 't Buurthuis same seat / emeis holding / Home Sebrechts / Unite Jolimont"
        )
        row["blocked_gap_id"] = GAP
        row["updated_utc"] = UTC
        row["notes"] = "tick2124 RSW YE2025 Medium CW; FOI ready not sent; next rq_2125; next every-10 2130"

if not has_2125:
    rows.append(
        {
            "task_id": "rq_2125",
            "title": "leftover dual hole-fill after RSW — prefer AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2125 after R.S.W. YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche. Do NOT redo R.S.W., "
                "Home Sebrechts, Unite Jolimont, 't Buurthuis Uccle, Le Bosquet, Strebo Services, Entraide Fraternelle Jolimont, "
                "La Charmille, Charmilles Sambreville, Les Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, XXe Aout, "
                "Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, Korian Belgium, Comnexio, ORES*, SLG*, Always Home, AREWAL, "
                "AGB Bornem, Armonea holding, emeis holding."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2124 RSW; FARO/AIESH/REW still YE2024; next every-10 2130",
        }
    )

with open(rq, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open("docs/doge/data/loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": "rq_2124",
            "ticks_completed": "2124",
            "paused": "no",
            "notes": (
                "tick2124 leftover R.S.W. 0459.540.765 Medium CW "
                "(omzet JUMP 312k pnl FLIP LOSS -34.8k equity DROP 5.12m bruto JUMP 415k FTE Medium 0; "
                "assets/debt Unknown; 1 VE NACE 68.201/87.301 same seat emptied 't Buurthuis); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Home Sebrechts/Unite Jolimont taken; next rq_2125; next every-10 2130; continuous hole_fill"
            ),
        }
    )

rsw_markers = (
    "rsw",
    "0459.540",
    ENTITY,
    GAP,
    "src_rsw",
    "bud_rsw",
    "lb_rsw",
    "comm_rsw",
    "sa_rsw",
)
for path in [
    "docs/doge/data/sources.csv",
    "docs/doge/data/entities.csv",
    "docs/doge/data/budgets.csv",
    "docs/doge/data/commitments.csv",
    "docs/doge/data/leaderboard.csv",
    "docs/doge/data/foi_queue.csv",
]:
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        blob = " ".join((row.get(k) or "") for k in row).lower()
        if not any(m.lower() in blob for m in rsw_markers):
            continue
        for k, v in list(row.items()):
            if not v:
                continue
            if "tick2123" in v:
                row[k] = v.replace("tick2123", "tick2124")
            if "tick 2123" in v:
                row[k] = v.replace("tick 2123", "tick 2124")
            if "raw/tick2123" in v and "rsw" in v.lower():
                row[k] = v.replace("raw/tick2123", "raw/tick2124")
        if row.get("gap_id") == GAP:
            row["created_utc"] = UTC
            row["updated_utc"] = UTC
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

p = Path(f"docs/doge/foi/drafts/{GAP}.md")
txt = p.read_text(encoding="utf-8")
txt = txt.replace("**tick:** 2123", "**tick:** 2124")
p.write_text(txt, encoding="utf-8")

logp = Path("docs/doge/loop_log.md")
log = logp.read_text(encoding="utf-8")
m = re.search(
    r"## Tick 2123 - 2026-08-25T11:10:00Z - rq_2123 R\.S\.W\..*?(?=\n## Tick |\Z)",
    log,
    re.S,
)
new = """## Tick 2124 - 2026-08-25T11:25:00Z - rq_2124 R.S.W. Residence Senior's Westland (omzet JUMP 312k / pnl FLIP LOSS -35k / equity DROP 5.12m / Medium)

- Unit: **rq_2124** leftover dual after **rq_2123 Home Sebrechts** (race: concurrent agent took rq_2123 as Sebrechts; this tick recovers deferred RSW). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took deferred unused leftover **R.S.W. / Residence Senior's Westland** YE2025 (KBO **0459.540.765**; Alsembergsesteenweg 1037 Uccle; **NV/SA** NACE **68.201/87.301** / **1 VE**; same seat as emptied **'t Buurthuis**; Van Houtte/Guichard path). Do not redo Home Sebrechts/Unite Jolimont/'t Buurthuis/Le Bosquet/Strebo/Entraide/La Charmille/Charmilles/Sittelles/Buissons/Residence 3/Elisabeth Aan Zee/XXe Aout/Ninove/emeis holding.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR312212** JUMP +2.97% vs YE2024 EUR303195; bruto **EUR414736** JUMP +2.03%; pnl **EUR-34826** FLIP from YE2024 PROFIT EUR83337 (−141.79%); equity **EUR5120098** DROP −15.37% vs YE2024 EUR6049814; FTE **Medium-sized 0**; neerlegging **08.07.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via senior.westland@emeis.com.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 6.0); entities (+1 sa_rsw_residence_seniors_westland); foi + draft gap_rsw_nbb_pdf_assets_debt_pnl_flip_loss_equity_drop_matrix_l5; rq_2124=done + rq_2125 open; loop_state ticks=2124; raw docs/doge/data/raw/tick2124/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2120**; next **2130**). Next: rq_2125 (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
if m:
    log = log[: m.start()] + new + log[m.end()]
    print("log replaced")
else:
    log = log.rstrip() + "\n\n" + new
    print("log appended")
logp.write_text(log, encoding="utf-8")
print("remap OK")
