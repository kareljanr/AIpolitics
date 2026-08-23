# Close rq_2097 as Familiezorg Gent (race: 2096 already emeis; CSVs already filled)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
csv.field_size_limit(10**7)

UTC = "2026-08-25T05:10:00Z"
TICK = 2097
ENTITY = "vzw_familiezorg_gent"
GAP = "gap_familiezorg_gent_nbb_pdf_assets_debt_bruto_vs_omzet_pnl_drop_matrix_l5"
OMZET = 14782023
PNL = 639579
EQUITY = 24209880
BRUTO = 70038917
FTE = 1237.4
KBO = "0412.914.845"
EMAIL = "info@familiezorg.be"
PI = "5.8"

DO_NOT_REDO = (
    "Do NOT redo Familiezorg Gent, emeis Belgium, Begralim / Grauwzusters Limburg, "
    "Sint-Lucia Turnhout, Lidwina Mol, Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel, "
    "Familiezorg West-Vlaanderen, De Lovie, Ocura, Lindelo, Medemens, Augustinus Halle, "
    "Ben, Stuyvenberg, Wijshage, Mater Dei, Den Akker, Vander Stokken, Ten Anker, "
    "De Zwaluw, Kuurne, SJ Brugge, HH Grimbergen, Mater Amabilis, Maria Moorslede, "
    "MSW NZVL, Welvaart, Vulpia, Compostela, Leiehome, Deinze, OLV Bornem, Huize SJ Ieper, "
    "Sint-Antonius, Wezembeek, Ter Burg, Christine, Vrijzicht, Pandje, H.Familie, "
    "Westerhauwe, Ganspoel, Lendelede, Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, "
    "Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, De Verlosser, Zusters Berlaar, "
    "Psychogeriatrisch Centrum, De Linde, Samen Ouder, CWZC Zonhoven, Orelia, Kanunnik Triest, "
    "OLVA, OLV Roosdaal, Sint-Bernardus, Cassiers, OLV Lourdes Kortenberg, St Vincentius Antwerpen, "
    "Sint-Jozef Rillaar, Karus, De Foyer, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Always Home, Armonea, SLG Operaties, Sint-Barbara, Molenheide, Arendonk, Solidum."
)


def main():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)

    found = False
    for r in rows:
        if r["task_id"] == "rq_2097":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2097 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Familiezorg Gent YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Familiezorg Gent YE2025 Medium CW after emeis race on 2096; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} equity JUMP {EQUITY} "
                f"FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "NACE 88.101 thuiszorg 2 VE aanbestedende; distinct Familiezorg WV"
            )
            r["notes"] = (
                f"tick{TICK} Familiezorg Gent Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2098; next every-10 2100"
            )
            found = True
    if not found:
        raise SystemExit("rq_2097 missing")

    if not any(r["task_id"] == "rq_2098" for r in rows):
        rows.append(
            {
                "task_id": "rq_2098",
                "title": (
                    "leftover dual hole-fill after Familiezorg Gent — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused WZC-zorg"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2098 after Familiezorg Gent YE2025 Medium. Prefer leftover "
                    "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    "spawned after tick2097 Familiezorg Gent; next every-10 2100; "
                    "prefer FARO/AIESH/REW if YE2025 else unused WZC-zorg"
                ),
            }
        )

    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

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
                "last_unit_id": "rq_2097",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Familiezorg Gent {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown; NACE 88.101 2 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2098; next every-10 2100; continuous hole_fill"
                ),
            }
        )

    # touch entity notes with tick2097
    epath = DATA / "entities.csv"
    with epath.open(encoding="utf-8-sig", newline="") as fh:
        er = csv.DictReader(fh)
        efields = er.fieldnames
        erows = list(er)
    for r in erows:
        if r.get("entity_id") == ENTITY and "tick2097" not in (r.get("notes") or ""):
            r["notes"] = (r.get("notes") or "").replace("tick2096", "tick2097")
    with epath.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=efields, lineterminator="\n")
        w.writeheader()
        w.writerows(erows)

    entry = f"""

## Tick {TICK} - {UTC} - rq_2097 Familiezorg Gent (bruto JUMP 70.04m / omzet JUMP 14.78m / pnl DROP 0.64m / Medium)

- Unit: **rq_2097** leftover dual after **rq_2096 emeis** (concurrent race took emeis on 2096; Familiezorg Gent CSV/FOI written this tick). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Familiezorg Gent** YE2025 (KBO **{KBO}**; Vogelenzang 29 Gent; Oost-Vlaanderen **aanbestedende-overheid VZW** thuiszorg NACE **88.101** / **2 VE**). Distinct from Familiezorg WV. Do not redo emeis/Begralim/Sint-Lucia/Lidwina/SED Zoutleeuw/Zilvervogel/Familiezorg WV/De Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/AGB Bornem/Armonea/Always Home/SLG/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +5.26%; bruto **EUR{BRUTO}** JUMP +2.53%; pnl **PROFIT EUR{PNL}** DROP -61.10% vs YE2024 PROFIT EUR1644314; equity **EUR{EQUITY}** JUMP +2.69%; FTE **{FTE}** DROP -0.26% vs YE2024 1240.6; neerlegging **14.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 2 VE NACE 88.101; email {EMAIL}; site https://www.familiezorg.be/. Bruto used as primary envelope (thuiszorg VZW omzet<<bruto).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI} bruto proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2097=done + rq_2098 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2096/ (Familiezorg fetch; closed as 2097).
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2098 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(entry)
    print("OK tick", TICK, "bruto", BRUTO, "omzet", OMZET, "pnl", PNL)


if __name__ == "__main__":
    main()
