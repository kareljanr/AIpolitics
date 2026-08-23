# tick 2091 — rq_2091 CZD Zilvervogel Lo-Reninge YE2025 Medium CW
# (CSV/FOI already written in raced 2090 commit vs Familiezorg; close as 2091)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW2090 = DATA / "raw" / "tick2090"
RAW = DATA / "raw" / "tick2091"
RAW.mkdir(parents=True, exist_ok=True)

csv.field_size_limit(10**7)
UTC = "2026-08-25T03:50:00Z"
TICK = 2091
ENTITY = "vzw_czd_zilvervogel_lo_reninge"
GAP = "gap_zilvervogel_nbb_pdf_assets_debt_pnl_jump_fte_drop_matrix_l5"
OMZET = 20960560
PNL = 1149659
EQUITY = 34907378
BRUTO = 21115222
FTE = 278.3
KBO = "0471.475.527"
EMAIL = "info@zilvervogel.be"
PI = "5.4"

DO_NOT_REDO = (
    "Do NOT redo CZD Zilvervogel Lo-Reninge, Familiezorg West-Vlaanderen, De Lovie Poperinge, Ocura Beringen, "
    "WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, "
    "Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, WZC DEN AKKER Sint-Truiden, "
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
    "Always Home, Armonea, WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Prefer deferred Lidwina 0407.601.720 if unused."
)


def copy_raw():
    for name in [
        "czd_nl.html",
        "czd_en.html",
        "czd_fr.html",
        "kbo_czd.html",
        "czd_site.html",
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
        "bornem_jr.html",
    ]:
        src = RAW2090 / name
        if src.exists():
            shutil.copy2(src, RAW / name)


def retarget_notes():
    path = DATA / "sources.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        sid = row.get("source_id") or ""
        if "zilvervogel" in sid:
            row["source_id"] = sid.replace("_2090", f"_{TICK}")
            row["notes"] = (row.get("notes") or "").replace("tick2090", f"tick{TICK}")
            if "src_zilvervogel_kbo_" in row["source_id"]:
                row["source_id"] = f"src_zilvervogel_kbo_{TICK}"
            if "src_zilvervogel_site_" in row["source_id"]:
                row["source_id"] = f"src_zilvervogel_site_{TICK}"
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
            if "zilvervogel" in blob.lower() or ENTITY in blob or GAP in blob:
                for k, v in list(row.items()):
                    if v and "tick2090" in v:
                        row[k] = v.replace("tick2090", f"tick{TICK}")
                if fname == "foi_queue.csv" and row.get("gap_id") == GAP:
                    row["updated_utc"] = UTC
                    row["notes"] = f"tick{TICK}; human-send only; Medium CW; next every-10 2100"
        with path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)

    draft = FOI / f"{GAP}.md"
    if draft.exists():
        text = draft.read_text(encoding="utf-8")
        text = text.replace("**tick:** 2090", f"**tick:** {TICK}")
        draft.write_text(text, encoding="utf-8")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2091":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2091 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — CZD Zilvervogel Lo-Reninge YE2025 Medium"
            r["instructions"] = (
                "Completed leftover CZD Zilvervogel Lo-Reninge YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE DROP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "Lidwina YE2025 deferred"
            )
            r["notes"] = (
                f"tick{TICK} Zilvervogel Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE DROP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2092; next every-10 2100; Lidwina deferred"
            )
    if not any(r["task_id"] == "rq_2092" for r in rows):
        rows.append(
            {
                "task_id": "rq_2092",
                "title": "leftover dual hole-fill after Zilvervogel — prefer AGB/FARO-YE2025/AIESH-REW/Lidwina",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2091 after CZD Zilvervogel YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred Lidwina 0407.601.720 if unused, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2091 Zilvervogel; next every-10 2100; prefer Lidwina deferred",
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
                "last_unit_id": "rq_2091",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover CZD Zilvervogel Lo-Reninge {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE DROP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Lidwina deferred; "
                    "next rq_2092; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
        ids = {r.get("entity_id") for r in csv.DictReader(fh)}
    if ENTITY not in ids:
        raise SystemExit("missing Zilvervogel entity")

    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        if row["task_id"] == "rq_2091":
            st = (row.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE claim status={row.get('status')}")
            row["status"] = "in_progress"
            row["updated_utc"] = UTC
            row["notes"] = "CLAIM tick2091 CZD Zilvervogel (CSV already filled in raced 2090 commit)"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    copy_raw()
    retarget_notes()
    update_research_queue()
    write_loop_state()

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2091 CZD Zilvervogel (omzet JUMP 20.96m / pnl JUMP 1.15m / Medium)

- Unit: **rq_2091** leftover dual after **rq_2090 Familiezorg WV** (concurrent race took Familiezorg + EVERY-10 on 2090; Zilvervogel CSV/FOI already written in raced commit — closing as 2091). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **CZD / Zilvervogel** YE2025 (KBO **{KBO}**; Dorpplaats 14 Lo-Reninge; West-Vlaanderen **VZW** WZC / **3 VE**). Lidwina YE2025 deferred. Do not redo Familiezorg/Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +4.71%; pnl **PROFIT EUR{PNL}** JUMP +12.80% vs YE2024 PROFIT EUR1019213; equity **EUR{EQUITY}** JUMP +2.69%; bruto **EUR{BRUTO}** JUMP +6.42%; FTE **{FTE}** DROP -0.68% vs YE2024 280.2; neerlegging **03.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 3 VE; email {EMAIL}.
- Wrote: sources (+5 already); budgets (+5 already); commitments (+1 already); leaderboard (+1 pi {PI} already); entities (+1 already); foi + draft {GAP} already; rq_2091=done + rq_2092 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2091/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**; EVERY-10 already done at 2090 with Familiezorg). Next: rq_2092 (AGB/FARO-if-YE2025 / AIESH-REW / Lidwina deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL)


if __name__ == "__main__":
    main()
