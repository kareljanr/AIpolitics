# tick 2093 — rq_2093 Lidwina Mol YE2025 Medium CW
# (CSV/FOI already written in raced 2092 commit vs SED Zoutleeuw; close as 2093)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW2092 = DATA / "raw" / "tick2092"
RAW = DATA / "raw" / "tick2093"
RAW.mkdir(parents=True, exist_ok=True)

csv.field_size_limit(10**7)
UTC = "2026-08-25T04:20:00Z"
TICK = 2093
ENTITY = "vzw_lidwina_mol"
GAP = "gap_lidwina_nbb_pdf_assets_debt_bruto_vs_omzet_pnl_jump_matrix_l5"
OMZET = 10939532
PNL = 999268
EQUITY = 24353329
BRUTO = 21595069
FTE = 515.1
KBO = "0407.601.720"
EMAIL = "info@lidwina.be"
PI = "5.2"

DO_NOT_REDO = (
    "Do NOT redo Lidwina Mol, Sint-Elisabeth's Dal Zoutleeuw, CZD Zilvervogel Lo-Reninge, Familiezorg West-Vlaanderen, "
    "De Lovie Poperinge, Ocura Beringen, WZC Lindelo Lille, De Medemens Antwerpen, WZC Sint-Augustinus Halle, "
    "Ben Woonzorgnetwerk Roeselare, Home Stuyvenberg Herzele, WZC De Wijshage Rumst, WZC Mater Dei Heikruis Pepingen, "
    "WZC DEN AKKER Sint-Truiden, WZC H. Vander Stokken Pepingen, Ten Anker Nieuwpoort, De Zwaluw Pajottegem, "
    "Zorg en Welzijn Kuurne, Sint-Jozef Brugge Sint-Michiels, Heilig Hart Grimbergen, Mater Amabilis Wervik, "
    "WZC Maria's Rustoord Moorslede, VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, "
    "Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, Huize Sint-Jozef Ieper, WZC Sint-Antonius, "
    "OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, Groep Zorg H. Familie, "
    "Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, "
    "Werken Glorieux, Woonhaven Antwerpen, Maria Rustoord Ingelmunster, Always Home, Armonea, "
    "WZC Sint-Barbara Herselt, Molenheide, De Vaeren, WoonZorgGroep Arendonk, Solidum, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, "
    "CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Prefer deferred Sint-Lucia if unused live."
)


def copy_raw():
    for name in [
        "lidwina_nl.html",
        "lidwina_en.html",
        "lidwina_fr.html",
        "kbo_lidwina.html",
        "lidwina_site.html",
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
    ]:
        src = RAW2092 / name
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
        if "lidwina" in sid:
            row["source_id"] = sid.replace("_2092", f"_{TICK}")
            row["notes"] = (row.get("notes") or "").replace("tick2092", f"tick{TICK}")
            if "src_lidwina_kbo_" in row["source_id"]:
                row["source_id"] = f"src_lidwina_kbo_{TICK}"
            if "src_lidwina_site_" in row["source_id"]:
                row["source_id"] = f"src_lidwina_site_{TICK}"
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
            if "lidwina" in blob.lower() or ENTITY in blob or GAP in blob:
                for k, v in list(row.items()):
                    if v and "tick2092" in v:
                        row[k] = v.replace("tick2092", f"tick{TICK}")
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
        text = text.replace("**tick:** 2092", f"**tick:** {TICK}")
        draft.write_text(text, encoding="utf-8")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2093":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2093 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — Lidwina Mol YE2025 Medium"
            r["instructions"] = (
                "Completed leftover Lidwina Mol YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; NACE 88.993 maatwerk 5 VE"
            )
            r["notes"] = (
                f"tick{TICK} Lidwina Medium omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; FOI ready; "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2094; next every-10 2100"
            )
    if not any(r["task_id"] == "rq_2094" for r in rows):
        rows.append(
            {
                "task_id": "rq_2094",
                "title": "leftover dual hole-fill after Lidwina — prefer AGB/FARO-YE2025/AIESH-REW/Sint-Lucia/unused",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2093 after Lidwina Mol YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred Sint-Lucia if unused live, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2093 Lidwina; next every-10 2100; prefer Sint-Lucia deferred",
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
                "last_unit_id": "rq_2093",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover Lidwina Mol {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m "
                    f"equity JUMP {EQUITY/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown; NACE 88.993 5 VE); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                    "next rq_2094; next every-10 2100; continuous hole_fill"
                ),
            }
        )


def main():
    with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
        ids = {r.get("entity_id") for r in csv.DictReader(fh)}
    if ENTITY not in ids:
        raise SystemExit("missing Lidwina entity")

    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        if row["task_id"] == "rq_2093":
            st = (row.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE claim status={row.get('status')}")
            row["status"] = "in_progress"
            row["updated_utc"] = UTC
            row["notes"] = "CLAIM tick2093 Lidwina (CSV already filled in raced 2092 commit)"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    copy_raw()
    retarget_notes()
    update_research_queue()
    write_loop_state()

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2093 Lidwina Mol (bruto JUMP 21.60m / omzet JUMP 10.94m / pnl JUMP 1.00m / Medium)

- Unit: **rq_2093** leftover dual after **rq_2092 SED Zoutleeuw** (concurrent race took SED on 2092; Lidwina CSV/FOI already written in raced commit — closing as 2093). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took preferred deferred leftover **Lidwina** YE2025 (KBO **{KBO}**; Postelarenweg 213 Mol; Antwerpen **VZW** maatwerk NACE **88.993** / **5 VE**). Sint-Lucia deferred if still live. Do not redo SED Zoutleeuw/Zilvervogel/Familiezorg/Lovie/Ocura/Lindelo/Medemens/Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +12.92%; bruto **EUR{BRUTO}** JUMP +7.73%; pnl **PROFIT EUR{PNL}** JUMP +37.58% vs YE2024 PROFIT EUR726326; equity **EUR{EQUITY}** JUMP +4.85%; FTE **{FTE}** JUMP +1.64% vs YE2024 506.8; neerlegging **26.05.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE NACE 88.993; email {EMAIL}.
- Wrote: sources (+5 already); budgets (+5 already); commitments (+1 already); leaderboard (+1 pi {PI} already); entities (+1 already); foi + draft {GAP} already; rq_2093=done + rq_2094 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2093/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2100**). Next: rq_2094 (AGB/FARO-if-YE2025 / AIESH-REW / Sint-Lucia deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "bruto", BRUTO, "pnl", PNL)


if __name__ == "__main__":
    main()
