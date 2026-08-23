# tick 2086 — rq_2086 De Medemens Antwerpen YE2025 Medium CW
# (CSV/FOI already written in raced 2085 commit; close as 2086 after Augustinus took 2085)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"
FOI = ROOT / "foi" / "drafts"
LOG = ROOT / "loop_log.md"
RAW2085 = DATA / "raw" / "tick2085"
RAW = DATA / "raw" / "tick2086"
RAW.mkdir(parents=True, exist_ok=True)

csv.field_size_limit(10**7)
UTC = "2026-08-25T02:35:00Z"
TICK = 2086
ENTITY = "vzw_de_medemens_antwerpen"
GAP = "gap_medemens_nbb_pdf_assets_debt_growth_matrix_l5"
OMZET = 117128722
PNL = 3746216
EQUITY = 105051203
BRUTO = 113208879
FTE = 1362.0
KBO = "0428.692.191"
EMAIL = "communicatie@demedemens.be"
PI = "6.3"

DO_NOT_REDO = (
    "Do NOT redo De Medemens Antwerpen, WZC Sint-Augustinus Halle, Ben Woonzorgnetwerk Roeselare, "
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
    "Prefer deferred Lindelo 0418.352.387 / Ocura 0443.072.838 / De Lovie 0410.853.396 if unused."
)


def copy_raw():
    for name in [
        "medemens_nl.html",
        "medemens_en.html",
        "medemens_fr.html",
        "kbo_med.html",
        "med_site.html",
        "med_contact.html",
        "faro_nl.html",
        "aiesh_nl.html",
        "rew_nl.html",
        "bornem_jr.html",
    ]:
        src = RAW2085 / name
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
        if "medemens" in sid:
            row["source_id"] = sid.replace("_2085", f"_{TICK}")
            row["notes"] = (row.get("notes") or "").replace("tick2085", f"tick{TICK}")
            if "src_medemens_kbo_" in row["source_id"]:
                row["source_id"] = f"src_medemens_kbo_{TICK}"
            if "src_medemens_site_" in row["source_id"]:
                row["source_id"] = f"src_medemens_site_{TICK}"
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
            if "medemens" in blob.lower() or ENTITY in blob or GAP in blob:
                for k, v in list(row.items()):
                    if v and "tick2085" in v:
                        row[k] = v.replace("tick2085", f"tick{TICK}")
                if fname == "foi_queue.csv" and row.get("gap_id") == GAP:
                    row["updated_utc"] = UTC
                    row["notes"] = f"tick{TICK}; human-send only; Medium CW; next every-10 2090"
        with path.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
            w.writeheader()
            w.writerows(rows)

    # FOI draft tick number
    draft = FOI / f"{GAP}.md"
    if draft.exists():
        text = draft.read_text(encoding="utf-8")
        text = text.replace("**tick:** 2085", f"**tick:** {TICK}")
        draft.write_text(text, encoding="utf-8")


def update_research_queue():
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames
        rows = list(reader)
    for r in rows:
        if r["task_id"] == "rq_2086":
            st = (r.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE: rq_2086 status={r.get('status')}")
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["title"] = "leftover dual — De Medemens Antwerpen YE2025 Medium"
            r["instructions"] = (
                "Completed leftover De Medemens Antwerpen YE2025 Medium CW; "
                f"KBO {KBO}; omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} "
                f"bruto JUMP {BRUTO} FTE JUMP {FTE}; FOI {GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "deferred Lindelo/Ocura/De Lovie"
            )
            r["notes"] = (
                f"tick{TICK} Medemens Medium omzet JUMP {OMZET/1e6:.2f}m "
                f"pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m bruto JUMP {BRUTO/1e6:.2f}m "
                f"FTE JUMP {FTE}; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_2087; next every-10 2090; deferred Lindelo/Ocura/De Lovie"
            )
    if not any(r["task_id"] == "rq_2087" for r in rows):
        rows.append(
            {
                "task_id": "rq_2087",
                "title": "leftover dual hole-fill after Medemens — prefer AGB/FARO-YE2025/AIESH-REW/Lindelo-Ocura-Lovie",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Tick 2086 after De Medemens Antwerpen YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, "
                    "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else deferred Lindelo 0418.352.387 / "
                    "Ocura 0443.072.838 / De Lovie 0410.853.396 if unused, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. "
                    + DO_NOT_REDO
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": "spawned after tick2086 Medemens; next every-10 2090; prefer Lindelo/Ocura/De Lovie",
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
                "last_unit_id": "rq_2086",
                "ticks_completed": str(TICK),
                "paused": "no",
                "notes": (
                    f"tick{TICK} leftover De Medemens Antwerpen {KBO} Medium CW "
                    f"(omzet JUMP {OMZET/1e6:.2f}m pnl JUMP {PNL/1e6:.2f}m equity JUMP {EQUITY/1e6:.2f}m "
                    f"bruto JUMP {BRUTO/1e6:.2f}m FTE JUMP {FTE}; assets/debt Unknown); "
                    "AGB Bornem JR2024; FARO/AIESH/REW YE2024; deferred Lindelo/Ocura/De Lovie; "
                    "next rq_2087; next every-10 2090; continuous hole_fill"
                ),
            }
        )


def main():
    with (DATA / "entities.csv").open(encoding="utf-8-sig", newline="") as fh:
        ids = {r.get("entity_id") for r in csv.DictReader(fh)}
    if ENTITY not in ids:
        raise SystemExit("missing Medemens entity")

    # claim
    path = DATA / "research_queue.csv"
    with path.open(encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        if row["task_id"] == "rq_2086":
            st = (row.get("status") or "").lower()
            if st not in ("open", "in_progress"):
                raise SystemExit(f"RACE claim status={row.get('status')}")
            row["status"] = "in_progress"
            row["updated_utc"] = UTC
            row["notes"] = "CLAIM tick2086 De Medemens (CSV already filled in raced 2085 commit)"
    with path.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    copy_raw()
    retarget_notes()
    update_research_queue()
    write_loop_state()

    log_entry = f"""

## Tick {TICK} - {UTC} - rq_2086 De Medemens (omzet JUMP 117.13m / pnl JUMP 3.75m / Medium)

- Unit: **rq_2086** leftover dual after **rq_2085 Augustinus Halle** (concurrent race took Augustinus on 2085; Medemens CSV/FOI already written in raced commit — closing as 2086). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **De Medemens** YE2025 (KBO **{KBO}**; Lokkaardstraat 10 Antwerpen; Antwerpen **aanbestedende-overheid VZW** multi-site WZC/kinderopvang / **22 VE**). Deferred live unused: Lindelo / Ocura / De Lovie. Do not redo Augustinus Halle/Ben/Stuyvenberg/Wijshage/Mater Dei/Den Akker/Vander Stokken/Ten Anker/De Zwaluw/Kuurne/SJ Brugge/HH Grimbergen/Mater Amabilis/Maria Moorslede/MSW NZVL/Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home/Maria Ingelmunster/SJ Rumst/Rillaar/Sint-Barbara/Molenheide/Veilige Have/De Foyer/De Verlosser/Kanunnik/Zusterhof/Arendonk/Solidum.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +10.61%; pnl **PROFIT EUR{PNL}** JUMP +13.37% vs YE2024 PROFIT EUR3304311; equity **EUR{EQUITY}** JUMP +10.10%; bruto **EUR{BRUTO}** JUMP +10.35%; FTE **{FTE}** JUMP +8.23% vs YE2024 1258.4; neerlegging **27.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende 22 VE; email {EMAIL}.
- Wrote: sources (+5 already); budgets (+5 already); commitments (+1 already); leaderboard (+1 pi {PI} already); entities (+1 already); foi + draft {GAP} already; rq_2086=done + rq_2087 open; loop_state ticks={TICK}; raw under docs/doge/data/raw/tick2086/.
- FOI: **ready not sent** (human-gated; {EMAIL}).
- NOT every-10 (**next every-10 is 2090**). Next: rq_2087 (AGB/FARO-if-YE2025 / AIESH-REW / Lindelo-Ocura-Lovie deferred / unused DSO-IGS-HVZ-WZC-psych).
"""
    with LOG.open("a", encoding="utf-8") as fh:
        fh.write(log_entry)
    print("OK tick", TICK, "omzet", OMZET, "pnl", PNL)


if __name__ == "__main__":
    main()
