# tick 2084 — rq_2084 Ben Woonzorgnetwerk Roeselare YE2025 Medium CW
# (Ben CSV rows appended during aborted 2083 race vs Stuyvenberg; retarget to 2084)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW2083 = DATA / "raw" / "tick2083"
RAW = DATA / "raw" / "tick2084"
RAW.mkdir(parents=True, exist_ok=True)

csv.field_size_limit(10**7)
UTC = "2026-08-25T02:05:00Z"
TICK = 2084
ENTITY = "vzw_ben_woonzorgnetwerk_roeselare"
GAP = "gap_ben_nbb_pdf_assets_debt_pnl_flip_loss_fte_jump_matrix_l5"
OMZET = 16591480
PNL = -114901
EQUITY = 4017165
BRUTO = 15700026
FTE = 241.2
OMZET24 = 16194264
PNL24 = 646070
EQUITY24 = 4132067
BRUTO24 = 16066582
FTE24 = 232.7
OMZET_YOY = "+2.45%"
PNL_YOY = "FLIP LOSS"
EQUITY_YOY = "-2.78%"
BRUTO_YOY = "-2.28%"
FTE_YOY = "+3.65%"
FILED = "26.06.2026"
KBO = "0416.493.254"
EMAIL = "info@benwzn.be"
ADDR = "Dokter Delbekestraat 27, 8800 Roeselare"
SITE = "https://www.ben-woonzorgnetwerk.be/"
CW_NL = "https://www.companyweb.be/nl/0416493254/ben-woonzorgnetwerk"
CW_EN = "https://www.companyweb.be/en/0416493254/ben-woonzorgnetwerk"
CW_FR = "https://www.companyweb.be/fr/0416493254/ben-woonzorgnetwerk"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416493254"
PI = "5.4"

DO_NOT_REDO = (
    "Do NOT redo Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, WZC De Wijshage Rumst, "
    "WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, "
    "Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, "
    "Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, "
    "Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, "
    "'t Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, "
    "WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren (CW YE2016-only/Stopgezet), IPFBW, IGRETEC, Aquiris, SPGE, "
    "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
    "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)


def copy_raw():
    for name in [
        "ben_nl.html",
        "ben_en.html",
        "ben_fr.html",
        "kbo_ben.html",
        "ben_site2.html",
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
        "bornem_jr.html",
    ]:
        src = RAW2083 / name
        if src.exists():
            shutil.copy2(src, RAW / name)


def retarget_csv_notes():
    path = DATA / "sources.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        sid = row.get("source_id") or ""
        if sid.startswith("src_ben_"):
            row["source_id"] = sid.replace("_2083", f"_{TICK}")
            row["notes"] = (row.get("notes") or "").replace("tick2083", f"tick{TICK}")
            if "src_ben_kbo_" in row["source_id"]:
                row["source_id"] = f"src_ben_kbo_{TICK}"
            if "src_ben_site_" in row["source_id"]:
                row["source_id"] = f"src_ben_site_{TICK}"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    for fname in ["budgets.csv", "commitments.csv", "leaderboard.csv", "entities.csv", "foi_queue.csv"]:
        path = DATA / fname
        with path.open(encoding="utf-8-sig", newline="") as fh:
            r = csv.DictReader(fh)
            fields = r.fieldnames
            rows = list(r)
        for row in rows:
            blob = " ".join((row.get(k) or "") for k in row)
            if ENTITY in blob or "src_ben_" in blob or "lb_ben_omzet" in blob or "gap_ben_nbb" in blob or "comm_ben_jr2025" in blob or "bud_ben_" in blob:
                for k, v in list(row.items()):
                    if v and "tick2083" in v:
                        row[k] = v.replace("tick2083", f"tick{TICK}")
                if fname == "foi_queue.csv" and row.get("gap_id") == GAP:
                    row["updated_utc"] = UTC
                    row["notes"] = f"tick{TICK}; human-send only; Medium CW; next every-10 2090"
        with path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2084":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2084 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Ben Woonzorgnetwerk Roeselare YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Ben Woonzorgnetwerk Roeselare YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} "
                f"bruto DROP {BRUTO} FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Ben Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m bruto DROP {BRUTO/1e6:.2f}m "
                f"FTE JUMP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2085; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2085" for r in rows):
        rows.append(
            {
                "task_id": "rq_2085",
                "title": "leftover dual hole-fill after Ben — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2084 after Ben Woonzorgnetwerk Roeselare YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2084 Ben; next every-10 2090",
            }
        )
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def write_loop_state():
    path = DATA / "loop_state.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
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
                "last_unit_id": "rq_2084",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Ben Woonzorgnetwerk Roeselare {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl FLIP LOSS {PNL/1e6:.2f}m equity DROP {EQUITY/1e6:.2f}m "
                    f"bruto DROP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2085; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def ensure_foi_draft():
    FOI.mkdir(parents=True, exist_ok=True)
    (FOI / f"{GAP}.md").write_text(
        f"""# FOI draft — Ben Woonzorgnetwerk Roeselare (NBB PDF / assets-debt / pnl-flip-loss / FTE-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Ben Woonzorgnetwerk VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW aanbestedende overheid; **2 VE**; zetel Dokter Delbekestraat 27 Roeselare; NACE 87.301; email {EMAIL}.
- Site: multi-site WZC netwerk West-Vlaanderen.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Concurrent 2083 took Home Stuyvenberg; De Vaeren skipped.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Ben Woonzorgnetwerk vzw — Dokter Delbekestraat 27, 8800 Roeselare
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Ben Woonzorgnetwerk + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit / aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de resultaatsomslag van winst EUR{PNL24} (YE2024) naar verlies EUR{PNL} (YE2025) bij omzetgroei {OMZET_YOY} en FTE-stijging van {FTE24} naar {FTE} ({FTE_YOY}).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
        encoding="utf-8",
    )


def main():
    with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
        ids = {r.get("entity_id") for r in csv.DictReader(fh)}
    if ENTITY not in ids:
        raise SystemExit("missing Ben entity row")

    copy_raw()
    retarget_csv_notes()
    ensure_foi_draft()
    update_research_queue()
    write_loop_state()

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2084 Ben Woonzorgnetwerk (omzet JUMP 16.59m / pnl FLIP LOSS 0.11m / Medium)

- Unit: **rq_2084** leftover dual after **rq_2083 Home Stuyvenberg** (concurrent race took Stuyvenberg on 2083; this fire continues with unused Ben). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. De Vaeren skipped (CW YE2016-only / Stopgezet). Took unused leftover **Ben Woonzorgnetwerk** YE2025 (KBO **{KBO}**; Dokter Delbekestraat 27 Roeselare; West-Vlaanderen **aanbestedende-overheid VZW** WZC netwerk / **2 VE**). Do not redo Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP {OMZET_YOY}; pnl **LOSS EUR{PNL}** FLIP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** DROP {EQUITY_YOY}; bruto **EUR{BRUTO}** DROP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 2 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2084=done + rq_2085 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2084/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2085 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL)


if __name__ == "__main__":
    main()
