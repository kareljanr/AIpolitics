# Complete orphaned SED write as tick 2092 (rq_2092 in_progress finish)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
LOG = ROOT / "loop_log.md"
FOI_DRAFT = ROOT / "foi" / "drafts" / "gap_sed_zoutleeuw_nbb_pdf_assets_debt_pnl_flip_loss_equity_drop_matrix_l5.md"

csv.field_size_limit(10**7)
UTC = "2026-08-25T04:15:00Z"
TICK = 2092
ENTITY = "vzw_sint_elisabeths_dal_zoutleeuw"
GAP = "gap_sed_zoutleeuw_nbb_pdf_assets_debt_pnl_flip_loss_equity_drop_matrix_l5"
KBO = "0413.653.827"
OMZET = 16361513
PNL = -238101
EQUITY = 8763808
BRUTO = 16337809
FTE = 212.1
EMAIL = "info.zl@vzwsed.be"

DO_NOT_REDO = (
    "Do NOT redo Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel Lo-Reninge, Familiezorg West-Vlaanderen, "
    "De Lovie Poperinge, Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, "
    "Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, "
    "WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, "
    "Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, "
    "WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, "
    "Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, Always Home, Armonea, "
    "Maria Rustoord Ingelmunster, Sint-Jozef Rumst, WZC Sint-Jozef Rillaar, WZC Sint-Barbara Herselt, "
    "Molenheide, Veilige Have, De Foyer, De Verlosser, Kanunnik Triest, Zusterhof, WoonZorgGroep Arendonk, Solidum."
)


def main():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)

    found = False
    for r in rows:
        if r["task_id"] == "rq_2092":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2092 status={r.get('status')}")
            found = True
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto DROP {BRUTO} pnl FLIP LOSS {PNL} equity DROP {EQUITY} "
                f"FTE {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 87.101 RVT 3 VE; "
                "Lidwina/Sint-Lucia deferred"
            )
            r["notes"] = (
                f"tick{TICK} SED Medium omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2093; next every-10 2100"
            )
    if not found:
        raise SystemExit("rq_2092 missing")

    if not any(r["task_id"] == "rq_2093" for r in rows):
        rows.append(
            {
                "task_id": "rq_2093",
                "title": "leftover dual hole-fill after SED Zoutleeuw — prefer AGB/FARO-YE2025/AIESH-REW/Lidwina",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2093 after Sint-Elisabeth's Dal Zoutleeuw YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred Lidwina Mol 0407.601.720 if unused, "
                    "else Sint-Lucia Turnhout 0410.151.137 if unused, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2092 SED Zoutleeuw; next every-10 2100; Lidwina/Sint-Lucia deferred live",
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
                "last_unit_id": "rq_2092",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Sint-Elisabeth's Dal Zoutleeuw {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m "
                    f"equity DROP {EQUITY/1e6:.2f}m FTE {FTE}; assets/debt Unknown; NACE 87.101 3 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Lidwina/Sint-Lucia deferred; "
                    "next rq_2093; next every-10 2100; continuous hole_fill"
                ),
            }
        )

    # retarget FOI draft tick label if still 2091
    if FOI_DRAFT.exists():
        text = FOI_DRAFT.read_text(encoding="utf-8")
        text = text.replace("**tick:** 2091", f"**tick:** {TICK}")
        FOI_DRAFT.write_text(text, encoding="utf-8")

    # patch foi_queue notes tick if needed
    foi_path = DATA / "foi_queue.csv"
    with foi_path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        ffields = reader.fieldnames
        frows = list(reader)
    for r in frows:
        if r.get("gap_id") == GAP:
            r["updated_utc"] = UTC
            r["notes"] = f"tick{TICK}; human-send only; Medium CW; next every-10 2100"
    with foi_path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=ffields, lineterminator="\n")
        w.writeheader()
        w.writerows(frows)

    log_entry = f"""

### {UTC} — tick {TICK}
- Unit: **rq_2092** leftover dual after **rq_2091 CZD Zilvervogel**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused WZC **Sint-Elisabeth's Dal** YE2025 (KBO **{KBO}**; Stationsstraat 36 Zoutleeuw; Vlaams-Brabant **aanbestedende-overheid VZW** NACE **87.101** / **3 VE**; campuses OLV Lourdes / Sint-Jozef Nieuwerkerken / Betze Rust). Deferred live unused **Lidwina Mol** / **Sint-Lucia Turnhout**. Do not redo Zilvervogel/Familiezorg WV/De Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/…/AGB Bornem/Armonea/Always Home/Solidum.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR{OMZET}** JUMP +2.65%; bruto **EUR{BRUTO}** DROP -1.05%; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR225456; equity **EUR{EQUITY}** DROP -6.63%; FTE **{FTE}** (YoY Unknown); neerlegging **23.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 3 VE NACE 87.101; email {EMAIL}; site https://st-elisabethsdal.be/.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.4 omzet proxy); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2092=done + rq_2093 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2091/ (+ tick2092 probe leftovers).
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2093 (AGB/FARO-if-YE2025 / AIESH-REW / Lidwina / Sint-Lucia / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK finish tick", TICK, "entity", ENTITY)


if __name__ == "__main__":
    main()
