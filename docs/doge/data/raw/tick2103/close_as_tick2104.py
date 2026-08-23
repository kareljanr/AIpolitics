# Remap partial Korian write (raced on 2103/Comnexio) to tick 2104 / rq_2104
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
DRAFT = ROOT / "foi" / "drafts" / (
    "gap_korian_belgium_nbb_pdf_assets_debt_pnl_drop_holding_dual_matrix_l5.md"
)

csv.field_size_limit(10**7)
UTC = "2026-08-25T06:40:00Z"
TICK = 2104
RQ = "rq_2104"
NEXT_RQ = "rq_2105"
ENTITY = "nv_korian_belgium"
GAP = "gap_korian_belgium_nbb_pdf_assets_debt_pnl_drop_holding_dual_matrix_l5"
KBO = "0869.769.702"
OMZET = 36661929
BRUTO = 23130494
PNL = 3410765
EQUITY = 194558071
FTE = 47.4
PI = "5.9"
EMAIL = "info@korian.be"

DO_NOT_REDO = (
    "Do NOT redo Korian Belgium, Comnexio, ORES SC, SLG Vlaanderen, Always Home, "
    "SLG Operaties Vlaanderen, AREWAL, Familiezorg Gent, emeis Belgium, Begralim, "
    "Sint-Lucia, Lidwina, SED, Zilvervogel, Familiezorg WV, De Lovie, Ocura, "
    "Armonea, Colisée Belgium, AGB Bornem, AIEG, RESA, Enodia, Fluxys*, ETB, Elia, "
    "BNO, Synergrid, Atrias, Synatom, IPFBW, IGRETEC, SPGE, Aquiris, Vivaqua, Hydria, "
    "CILE, SWDE, Belgoprocess, Laborelec, NIRAS, Bel V, Dijk92, FANC, SCK CEN, "
    "EURIDICE, IRE*, BRUGEL, ORES Assets."
)


def rewrite(path: Path, id_key: str, match_prefix: str, mut):
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    n = 0
    for r in rows:
        if (r.get(id_key) or "").startswith(match_prefix) or match_prefix in (
            r.get(id_key) or ""
        ):
            mut(r)
            n += 1
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(path.name, "updated", n)


def fix_notes(s: str) -> str:
    if not s:
        return s
    s = s.replace("tick2103", f"tick{TICK}")
    s = s.replace("_2103", f"_{TICK}")
    s = s.replace("rq_2103", RQ)
    s = s.replace("next rq_2104", f"next {NEXT_RQ}")
    return s


def main():
    # sources: rename kbo/contact ids 2103→2104 + notes
    def mut_src(r):
        if r["source_id"].endswith("_2103"):
            r["source_id"] = r["source_id"].replace("_2103", f"_{TICK}")
        r["notes"] = fix_notes(r.get("notes") or "")

    rewrite(DATA / "sources.csv", "source_id", "src_korian_belgium", mut_src)

    for fn, key, pref in [
        ("budgets.csv", "budget_id", "bud_korian_belgium"),
        ("commitments.csv", "commitment_id", "comm_korian_belgium"),
        ("leaderboard.csv", "item_id", "lb_korian_belgium"),
        ("entities.csv", "entity_id", "nv_korian_belgium"),
        ("foi_queue.csv", "gap_id", "gap_korian_belgium"),
    ]:

        def mut(r, _key=key):
            for k, v in list(r.items()):
                if isinstance(v, str) and ("tick2103" in v or "_2103" in v):
                    r[k] = fix_notes(v)
            if _key == "gap_id":
                r["created_utc"] = UTC
                r["updated_utc"] = UTC
                r["notes"] = (
                    f"tick{TICK}; human-send only; Medium CW; next every-10 2110; "
                    "race-remapped from concurrent 2103 Comnexio"
                )

        rewrite(DATA / fn, key, pref, mut)

    # FOI draft tick label
    if DRAFT.exists():
        text = DRAFT.read_text(encoding="utf-8")
        text = text.replace("**tick:** 2103", f"**tick:** {TICK}")
        text = text.replace(
            "tick 2103",
            f"tick {TICK} (race-remapped from concurrent 2103 Comnexio)",
        )
        DRAFT.write_text(text, encoding="utf-8")
        print("draft retitled")

    # research queue
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r["task_id"] == RQ:
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: {RQ} status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Korian Belgium YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Korian Belgium YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto DROP {BRUTO} pnl DROP {PNL} "
                f"equity JUMP {EQUITY} FTE {FTE}; FOI {GAP}; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.301 ROB + RSZ 64.210 "
                "holding; 1 VE NV; dual SLG Vlaanderen / SLG Operaties; "
                "DISTINCT Armonea/Always Home/emeis/ORES SC/Comnexio; "
                "race-remapped from concurrent 2103 Comnexio"
            )
            r["notes"] = (
                f"tick{TICK} Korian Belgium Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"bruto DROP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m "
                f"equity JUMP {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; "
                f"AGB Bornem JR2024; FARO/AIESH/REW YE2024; next {NEXT_RQ}; "
                "next every-10 2110"
            )
            found = True
    if not found:
        raise SystemExit(f"{RQ} missing")
    if not any(r["task_id"] == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Korian Belgium — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Korian Belgium YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else "
                    "AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/"
                    "WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Korian Belgium; next every-10 2110"
                ),
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print("research_queue closed", RQ, "spawned", NEXT_RQ)

    # loop_state
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
                "last_unit_id": RQ,
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Korian Belgium {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                    f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"FTE {FTE}; assets/debt Unknown; NACE 87.301+64.210 1 VE holding dual "
                    "SLG); race: 2103 was Comnexio; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    f"next {NEXT_RQ}; next every-10 2110; continuous hole_fill"
                ),
            }
        )
    print("loop_state", TICK)

    entry = f"""


## Tick {TICK} - {UTC} - rq_2104 Korian Belgium (omzet JUMP 36.66m / pnl DROP 3.41m / Medium)

- Unit: **rq_2104** leftover dual after **rq_2103 Comnexio** (concurrent race took Comnexio on 2103; this agent remapped preferred deferred **Korian Belgium**). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Korian Belgium** YE2025 (KBO **{KBO}**; Satenrozen 1B Kontich; Antwerpen **NV** holding/ROB NACE **87.301 + RSZ 64.210** / **1 VE**; HQ of SLG path). Do not redo Comnexio/ORES SC/SLG Vlaanderen/SLG Operaties/Always Home/AREWAL/Familiezorg Gent/emeis/Begralim/Armonea/Colisée/AGB Bornem.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +4.37%; bruto **EUR{BRUTO}** DROP -24.45%; pnl **PROFIT EUR{PNL}** DROP -49.77% vs YE2024 PROFIT EUR6790713; equity **EUR{EQUITY}** JUMP +1.78%; FTE **{FTE}** (YoY Unknown); neerlegging **15.08.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief NV 1 VE; email {EMAIL}. Omzet used as primary envelope (holding dual vs SLG ops daughters 115.87m + 58.28m).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2103/ (gather) + close_as_tick2104.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**last every-10 was 2100**; next **2110**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused WZC).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("log appended")
    print(f"OK tick{TICK} {ENTITY} omzet={OMZET} pi={PI}")


if __name__ == "__main__":
    main()
