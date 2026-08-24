# -*- coding: utf-8 -*-
"""Tick 2210 EVERY-10 progress + waste top10 (no new entity; ACG deferred)."""
import csv
from pathlib import Path

csv.field_size_limit(10**7)
ROOT = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\data")
LOG = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
TS = "2026-08-26T16:00:00Z"
TICK = 2210


def update_csv_rows(path, key, updates):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = list(r)
    n = 0
    for row in rows:
        if row.get(key) in updates:
            row.update(updates[row[key]])
            n += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("update", path.name, n)


def append_csv(path, rows):
    path = Path(path)
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        existing = list(r)
        cols = r.fieldnames
    idkey = cols[0]
    have = {row[idkey] for row in existing}
    added = 0
    for row in rows:
        if row.get(idkey) in have:
            print("SKIP", path.name, row.get(idkey))
            continue
        existing.append({c: row.get(c, "") for c in cols})
        added += 1
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
        w.writeheader()
        w.writerows(existing)
    print("append", path.name, "+", added, "total", len(existing))


update_csv_rows(
    ROOT / "research_queue.csv",
    "task_id",
    {
        "rq_2210": {
            "status": "done",
            "entity_id": "progress_every_10",
            "blocked_gap_id": "",
            "updated_utc": TS,
            "title": "EVERY-10 progress coverage % + waste top10 @2210 (after Noordheuvel)",
            "instructions": "Completed EVERY-10 refresh after Noordheuvel; preferred AGB Bornem JR2024 / FARO/AIESH/REW still YE2024; ACG unnamed FREE deferred; no new entity euros this tick",
            "notes": "tick2210 EVERY-10; refreshed progress_every_10_ticks.md + doge_waste_top10_current.md; top10 stable GIP/fossil/cars/cheque/reporté; residual dual 2201-2209 noted; next rq_2211; next every-10 2220",
        }
    },
)

append_csv(
    ROOT / "research_queue.csv",
    [
        dict(
            task_id="rq_2211",
            title="leftover dual hole-fill after EVERY-10@2210 — prefer AGB/FARO-YE2025/AIESH-REW/unused maatwerk-WZC-IGS",
            sprint="hole_fill",
            priority="8",
            status="open",
            hierarchy_target="L5",
            entity_id="",
            instructions=(
                "Tick 2211 after EVERY-10@2210 (progress + waste top10; no new entity). "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused maatwerk/WZC/IGS/DSO "
                "(FREE: ACG if identifiable YE2025 KBO; Odas still YE2024). "
                "Do NOT redo Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, De Winning, "
                "Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, "
                "Kringwinkel Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, Westlandia, BWB, Wase, Groep INTRO, MAAAT, "
                "WAAK SW, Waak, Stijn, Stroom, Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, Het Dorp, De Vlietoever, "
                "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10 at 2220."
            ),
            blocked_gap_id="",
            created_utc=TS,
            updated_utc=TS,
            notes="spawned after tick2210 EVERY-10; FARO/AIESH/REW still YE2024; AGB Bornem JR2024; ACG FREE unnamed; next EVERY-10 2220",
        )
    ],
)

with (ROOT / "loop_state.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    cols = r.fieldnames
    rows = list(r)
for row in rows:
    if row.get("state_id") == "main":
        row["mode"] = "continuous"
        row["current_sprint"] = "hole_fill"
        row["last_tick_utc"] = TS
        row["last_unit_id"] = "rq_2210"
        row["ticks_completed"] = "2210"
        row["paused"] = "no"
        row["notes"] = (
            "tick2210 EVERY-10 progress + waste top10 (top10 stable; residual dual 2201-2209 "
            "MWP/Aarova/Ijsedal/Werkplus/Oesterbank/Entiris/Kemphaan/Arcor/Noordheuvel); "
            "AGB Bornem JR2024; FARO/REW YE2024; ACG deferred; next rq_2211; next every-10 2220; continuous hole_fill"
        )
with (ROOT / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print("loop_state -> 2210")

log_block = f"""
## Tick 2210 - {TS} - rq_2210 EVERY-10 progress coverage % + waste top10

- Unit: **rq_2210 EVERY-10** after **rq_2209 Noordheuvel**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW stalled. **No new entity** this tick (ACG still unnamed FREE / Odas YE2024). Do not redo Noordheuvel/Arcor/Kemphaan/Entiris/Oesterbank/Werkplus/Ijsedal/Aarova/MWP/AGE stack.
- Found: inventory budgets **53182** / commitments **5901** / leaderboard **8022** / entities **1932** / sources **6066** / FOI ready **~1851** / answered **11** / partial **28** / FOI total **~1903**. Pure annual waste **top10 stable** (GIP 8.7 · fossil direct 8.55 · cars/cheque/reporté band 8.4–8.5). Residual dual **2201-2209** off pure top10: Entiris 18.93m · Oesterbank 7.31m · Aarova 5.62m · Arcor bruto 4.06m empty-omzet · Ijsedal 3.20m LOSS FLIP · Kemphaan 2.79m · Werkplus 2.69m · MWP 2.65m · Noordheuvel 2.57m LOSS FLIP.
- Wrote: progress_every_10_ticks.md (layers A–E @2210); doge_waste_top10_current.md; rq_2210=done + rq_2211 open; loop_state ticks=2210.
- FOI: none new this tick (prior Noordheuvel/Arcor/Kemphaan… ready not sent).
- **EVERY-10 done.** Next every-10 **2220**. Next: rq_2211 (AGB/FARO-if-YE2025 / AIESH-REW / ACG-or-unused).

"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)
print("loop_log appended")
print("DONE tick2210 EVERY-10")
