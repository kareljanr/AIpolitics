# tick 2101 — close rq_2101 as SLG Vlaanderen (CSV/FOI already filled; race with Always Home @2100)
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T06:05:00Z"
TICK = 2101
ENTITY = "vzw_slg_vlaanderen"
GAP = "gap_slg_vlaanderen_nbb_pdf_assets_debt_pnl_flip_loss_equity_thin_matrix_l5"
OMZET = 115872918
PNL = -332030
EQUITY = 397440
BRUTO = 83069045
FTE = 1190.2
KBO = "0410.958.712"
PI = "6.7"

DO_NOT_REDO = (
    "Do NOT redo SLG Vlaanderen, Always Home, SLG Operaties Vlaanderen, AREWAL, "
    "Familiezorg Gent, emeis Belgium, Begralim, Sint-Lucia, Lidwina, SED, Zilvervogel, "
    "Familiezorg WV, De Lovie, Ocura, Armonea, Colisée Belgium, AGB Bornem, AIEG, RESA, "
    "Enodia, Fluxys*, ETB, Elia, BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, "
    "Aquiris, Vivaqua, Hydria, CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, "
    "FANC, SCK CEN, EURIDICE, IRE*, BRUGEL."
)


def main():
    # verify rows exist
    with (DATA / "commitments.csv").open(encoding="utf-8-sig", newline="") as fh:
        ids = {r["commitment_id"] for r in csv.DictReader(fh)}
    if "comm_slg_vlaanderen_jr2025_statutory_wzc" not in ids:
        raise SystemExit("missing SLG Vlaanderen commitment — abort")
    with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
        eids = {r["entity_id"] for r in csv.DictReader(fh)}
    if ENTITY not in eids:
        raise SystemExit("missing entity — abort")
    draft = ROOT / "foi" / "drafts" / f"{GAP}.md"
    if not draft.exists():
        raise SystemExit("missing FOI draft — abort")

    # research queue
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == "rq_2101":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2101 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — SLG Vlaanderen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover SLG Vlaanderen YE2025 Medium CW (CSV/FOI filled during "
                f"2100 race); KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl FLIP LOSS "
                f"{PNL} equity DROP thin {EQUITY} FTE DROP {FTE}; FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.101 VZW 29 VE; "
                "dual SLG Operaties / Always Home / Korian"
            )
            r["notes"] = (
                f"tick{TICK} SLG Vlaanderen Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto JUMP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m "
                f"equity DROP thin {EQUITY/1e6:.2f}m FTE DROP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2102; next every-10 2110"
            )
            found = True
    if not found:
        raise SystemExit("rq_2101 missing")
    if not any(r["task_id"] == "rq_2102" for r in rows):
        rows.append(
            {
                "task_id": "rq_2102",
                "title": (
                    "leftover dual hole-fill after SLG Vlaanderen — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Korian-Belgium/unused WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2102 after SLG Vlaanderen YE2025 Medium. Prefer leftover AGB/APB "
                    "if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else Korian Belgium 0869.769.702 YE2025 live unused dual, else unused "
                    "water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2101 SLG Vlaanderen; next every-10 2110; "
                    "Korian Belgium YE2025 deferred live"
                ),
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    # loop state
    with (DATA / "loop_state.csv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
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
                "last_unit_id": "rq_2101",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover SLG Vlaanderen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                    f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP thin {EQUITY/1e6:.2f}m "
                    f"FTE DROP {FTE}; assets/debt Unknown; NACE 87.101 29 VE Korian dual); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2102; next every-10 2110; continuous hole_fill"
                ),
            }
        )

    # fix progress: Always Home was EVERY-10@2100; SLG Vlaanderen is 2101
    prog = (DATA / "progress_every_10_ticks.md").read_text(encoding="utf-8")
    prog = prog.replace(
        "**SLG Vlaanderen VZW** omzet JUMP **115.87m** / pnl FLIP LOSS / equity thin **0.40m** Medium (this tick EVERY-10 dual)",
        "**Always Home** omzet DROP **8.86m** / equity JUMP Medium (tick2100 EVERY-10 dual) · **SLG Vlaanderen VZW** omzet JUMP **115.87m** / pnl FLIP LOSS / equity thin **0.40m** Medium (tick2101)",
    )
    prog = prog.replace(
        "**SLG Vlaanderen** · prior 2081-2090",
        "**Always Home** · **SLG Vlaanderen** · prior 2081-2090",
    )
    prog = prog.replace(
        "· **SLG Vlaanderen / Senior Living Group Vlaanderen VZW** (this tick EVERY-10 dual — Kontich VZW RVT NACE 87.101 YE2025 Medium CW; omzet 115.87m; pnl FLIP LOSS; equity thin 0.40m vs omzet; FTE DROP; dual SLG Operaties / Korian Belgium).",
        "· **Always Home** (tick2100 EVERY-10 dual — Colisée-path NV) · **SLG Vlaanderen / Senior Living Group Vlaanderen VZW** (tick2101 — Kontich VZW RVT NACE 87.101 YE2025 Medium CW; omzet 115.87m; pnl FLIP LOSS; equity thin 0.40m vs omzet; FTE DROP; dual SLG Operaties / Korian Belgium).",
    )
    # research_queue open line
    prog = re.sub(
        r"research_queue open \| rq_\d+ after progress",
        "research_queue open | rq_2102 after progress",
        prog,
    )
    (DATA / "progress_every_10_ticks.md").write_text(prog, encoding="utf-8")

    waste = (DATA / "doge_waste_top10_current.md").read_text(encoding="utf-8")
    if "Always Home" not in waste:
        waste = waste.replace(
            "**NEW residual 2091-2100:** **SLG Vlaanderen omzet 115.87m**",
            "**NEW residual 2091-2101:** **SLG Vlaanderen omzet 115.87m** · **Always Home omzet 8.86m**",
        )
        waste = waste.replace(
            "· **SLG Vlaanderen** (EVERY-10 dual).",
            "· **Always Home** (EVERY-10@2100) · **SLG Vlaanderen** (tick2101).",
        )
    (DATA / "doge_waste_top10_current.md").write_text(waste, encoding="utf-8")

    # update entity notes tick label if still says tick2100
    epath = DATA / "entities.csv"
    with epath.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        efields = reader.fieldnames
        erows = list(reader)
    for r in erows:
        if r.get("entity_id") == ENTITY and "tick2100" in (r.get("notes") or ""):
            r["notes"] = (r.get("notes") or "").replace(
                "tick2100 EVERY-10", f"tick{TICK}"
            )
    with epath.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=efields, lineterminator="\n")
        w.writeheader()
        w.writerows(erows)

    entry = f"""

## Tick {TICK} - {UTC} - rq_2101 SLG Vlaanderen (omzet JUMP 115.87m / pnl FLIP LOSS / equity thin 0.40m / Medium)

- Unit: **rq_2101** leftover dual after **rq_2100 Always Home EVERY-10**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Closed preferred deferred dual **SLG Vlaanderen / Senior Living Group Vlaanderen** YE2025 (KBO **{KBO}**; Satenrozen 1 B Kontich; Antwerpen **VZW** RVT NACE **87.101** / **29 VE**; bestuurder Korian Belgium) — CSV/FOI already written during 2100 race; this tick closes queue + state. Korian Belgium NV YE2025 deferred. Do not redo Always Home/SLG Operaties/AREWAL/Familiezorg Gent/emeis/Begralim/Sint-Lucia/Lidwina/SED/Zilvervogel/Familiezorg WV/De Lovie/Ocura/Armonea/Colisée/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +2.17%; bruto **EUR{BRUTO}** JUMP +1.20%; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR176516; equity **EUR{EQUITY}** DROP -45.52% (thin vs omzet); FTE **{FTE}** DROP vs YE2024 1192.8; neerlegging **28.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 29 VE; email info@korian.be.
- Wrote: rq_2101=done + rq_2102 open; loop_state ticks={TICK}; progress/waste attribution fix (Always Home@2100 EVERY-10; SLG Vlaanderen@2101); entity notes tick label; FOI draft already ready.
- FOI: **ready not sent** (human-gated; info@korian.be).
- NOT every-10 (**last every-10 was 2100**; next **2110**). Next: rq_2102 (AGB/FARO-if-YE2025 / AIESH-REW / Korian Belgium deferred / unused WZC).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print(f"OK tick{TICK} closed {ENTITY} omzet={OMZET} pi={PI} gap={GAP}")


if __name__ == "__main__":
    main()
