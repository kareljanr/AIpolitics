# tick 2082 — rq_2082 WZC De Wijshage Rumst YE2025 Medium CW
# (Wijshage CSV rows already appended during aborted 2081 race; retarget to 2082)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW2081 = DATA / "raw" / "tick2081"
RAW = DATA / "raw" / "tick2082"
RAW.mkdir(parents=True, exist_ok=True)

csv.field_size_limit(10**7)
UTC = "2026-08-25T01:35:00Z"
TICK = 2082
ENTITY = "vzw_wzc_de_wijshage_rumst"
GAP = "gap_wijshage_nbb_pdf_assets_debt_pnl_drop_fte_jump_matrix_l5"
LB = "lb_wijshage_omzet_drop_8_00m_pnl_drop_fte_jump_jr2025"
COMM = "comm_wijshage_jr2025_statutory_wzc"

OMZET = 7995385
PNL = 543894
EQUITY = 13934288
BRUTO = 8323447
FTE = 100.9
OMZET24 = 8007098
PNL24 = 749719
EQUITY24 = 13562501
BRUTO24 = 8165947
FTE24 = 96.1
OMZET_YOY = "-0.15%"
PNL_YOY = "DROP -27.45%"
EQUITY_YOY = "+2.74%"
BRUTO_YOY = "+1.93%"
FTE_YOY = "+4.99%"
FILED = "03.07.2026"
KBO = "0449.425.546"
EMAIL = "onthaal@dewijtshage.be"
ADDR = "'s Herenbaan 170, 2840 Rumst"
SITE = "https://woonzorgcollectief.be/de-wijtshage2/wzc-de-wijtshage/"
CW_NL = "https://www.companyweb.be/nl/0449425546/rust-en-verzorgingstehuis-de-wijtshage"
CW_EN = "https://www.companyweb.be/en/0449425546/rust-en-verzorgingstehuis-de-wijtshage"
CW_FR = "https://www.companyweb.be/fr/0449425546/rust-en-verzorgingstehuis-de-wijtshage"
KBO_URL = "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0449425546"
PI = "5.2"

DO_NOT_REDO = (
    "Do NOT redo WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
    "WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, Zorg en Welzijn Kuurne, "
    "Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, WZC Maria's Rustoord Moorslede, "
    "VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, "
    "Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, "
    "WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, "
    "Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, "
    "Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, "
    "WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, "
    "WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, "
    "WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, "
    "Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, "
    "Always Home, Armonea, WZC Sint-Barbara Herselt, Molenheide, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, "
    "SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, "
    "Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)


def copy_raw():
    for name in [
        "wijshage_nl.html",
        "wijshage_en.html",
        "wijshage_fr.html",
        "kbo_wij.html",
        "wij_collectief.html",
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
        "bornem_jr.html",
    ]:
        src = RAW2081 / name
        if src.exists():
            shutil.copy2(src, RAW / name)


def retarget_csv_notes():
    # Fix source_id tick tags 2081->2082 for wijshage rows already present
    path = DATA / "sources.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        sid = row.get("source_id") or ""
        if "wijshage" in sid:
            row["source_id"] = sid.replace("_2081", "_2082")
            row["notes"] = (row.get("notes") or "").replace("tick2081", f"tick{TICK}")
            if "src_wijshage_kbo_" in row["source_id"]:
                row["source_id"] = f"src_wijshage_kbo_{TICK}"
            if "src_wijshage_site_" in row["source_id"]:
                row["source_id"] = f"src_wijshage_site_{TICK}"
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
            if "wijsh" in blob.lower() or "wijtsh" in blob.lower() or ENTITY in blob:
                for k, v in list(row.items()):
                    if v and "tick2081" in v:
                        row[k] = v.replace("tick2081", f"tick{TICK}")
                if fname == "foi_queue.csv":
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
        if r["task_id"] == "rq_2082":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2082 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — WZC De Wijshage Rumst YE2025 Medium"
            r["instructions"] = (
                "Completed leftover WZC De Wijshage Rumst YE2025 Medium CW; "
                f"KBO {KBO}; omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            )
            r["notes"] = (
                f"tick{TICK} Wijshage Medium omzet DROP {OMZET/1e6:.2f}m "
                f"pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE JUMP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2083; next every-10 2090"
            )
    if not any(r["task_id"] == "rq_2083" for r in rows):
        rows.append(
            {
                "task_id": "rq_2083",
                "title": "leftover dual hole-fill after Wijshage — prefer AGB/FARO-YE2025/AIESH-REW/unused-WZC",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2082 after WZC De Wijshage Rumst YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2082 Wijshage; next every-10 2090",
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
                "last_unit_id": "rq_2082",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover WZC De Wijshage Rumst {KBO} Medium CW "
                    f"(omzet DROP {OMZET/1e6:.2f}m pnl DROP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2083; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def ensure_foi_draft():
    FOI.mkdir(parents=True, exist_ok=True)
    path = FOI / f"{GAP}.md"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if f"**tick:** {TICK}" not in text:
        path.write_text(
            f"""# FOI draft — WZC De Wijshage Rumst (NBB PDF / assets-debt / pnl-drop / FTE-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum De Wijtshage / De Wijshage VZW — KBO **{KBO}**  
**recipient:** {EMAIL} · {ADDR}  
**sources:** [CW NL]({CW_NL}) · [CW EN]({CW_EN}) · [CW FR]({CW_FR}) · [KBO]({KBO_URL}) · [site]({SITE})  
**tick:** {TICK}  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **{FILED}**): omzet **EUR{OMZET}** DROP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel 's Herenbaan 170 Rumst; NACE 87.101; email {EMAIL}.
- Site: Woonzorgcollectief De Wijtshage (DISTINCT from Sint-Jozef Rumst 0448.190.181 and Mater Dei Heikruis).
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Sint-Barbara Herselt already mined — skipped.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum De Wijtshage vzw — 's Herenbaan 170, 2840 Rumst
{EMAIL}
cc: Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 De Wijtshage + subsidiematrix (KBO {KBO})
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging {FILED}).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting van de winstdaling van EUR{PNL24} (YE2024) naar EUR{PNL} (YE2025; -27.45%) bij vrijwel vlakke omzet ({OMZET_YOY}) en FTE-stijging van {FTE24} naar {FTE} ({FTE_YOY}).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
            encoding="utf-8",
        )


def main():
    # Verify Wijshage entity row exists (from aborted 2081 apply)
    with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
        ids = {r.get("entity_id") for r in csv.DictReader(fh)}
    if ENTITY not in ids:
        raise SystemExit("missing Wijshage entity row — re-run full append")

    copy_raw()
    retarget_csv_notes()
    ensure_foi_draft()
    update_research_queue()
    write_loop_state()

    # copy apply helper into raw
    shutil.copy2(Path(__file__), RAW / "apply_tick2082.py")

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2082 WZC De Wijshage Rumst (omzet DROP 8.00m / pnl DROP 0.54m / Medium)

- Unit: **rq_2082** leftover dual after **rq_2081 Mater Dei** (concurrent race took Mater Dei on 2081; this fire continues with unused Wijshage). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Sint-Barbara Herselt YE2025 live but **already mined rq_2019** — skipped. Took unused leftover **WZC De Wijshage / De Wijtshage** YE2025 (KBO **{KBO}**; 's Herenbaan 170 Rumst; Antwerpen **VZW** WZC / **1 VE**; Woonzorgcollectief; **DISTINCT from Sint-Jozef Rumst and Mater Dei Heikruis**). Do not redo Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara Herselt/Molenheide.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** DROP {OMZET_YOY}; pnl **PROFIT EUR{PNL}** DROP vs YE2024 PROFIT EUR{PNL24}; equity **EUR{EQUITY}** JUMP {EQUITY_YOY}; bruto **EUR{BRUTO}** JUMP {BRUTO_YOY}; FTE **{FTE}** JUMP {FTE_YOY} vs YE2024 {FTE24}; neerlegging **{FILED}**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email {EMAIL}.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2082=done + rq_2083 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2082/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2083 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL, "SHA pending")


if __name__ == "__main__":
    main()
