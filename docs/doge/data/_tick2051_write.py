# ephemeral tick2051 — WZC Van Lierde YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T17:55:00Z"
ENTITY = "vzw_wzc_van_lierde"
GAP = "gap_van_lierde_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_van_lierde_jr2025_cw"
SRC_EN = "src_van_lierde_jr2025_cw_en"
SRC_FR = "src_van_lierde_jr2025_cw_fr"
SRC_KBO = "src_van_lierde_kbo_2051"
SRC_SITE = "src_van_lierde_site_2051"

OMZET = "7532068"
PNL = "461544"
EQUITY = "5687790"
BRUTO = "6890078"
FTE = "75.4"
OMZET24 = "7599325"
PNL24 = "529480"
EQUITY24 = "5559594"
BRUTO24 = "6697399"
# pi = 0.55*4.7 + 0.35*4.8 + 0.10*(10-4) = 2.585 + 1.68 + 0.6 = 4.865 → 4.9
PI = "4.9"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
        fields = [f.lstrip("\ufeff") for f in fields]
        for row in rows:
            if any(k.startswith("\ufeff") for k in row):
                for k in list(row):
                    if k.startswith("\ufeff"):
                        row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    fields = [f.lstrip("\ufeff") for f in fields]
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2051")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL WZC Van Lierde YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0633854022/woonzorgcentrum-van-lierde",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2051; YE2025 omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 02.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2051/van_lierde_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN WZC Van Lierde YE2025 statutory",
        "url": "https://www.companyweb.be/en/0633854022/woonzorgcentrum-van-lierde",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2051; EN mirror YE2025 Medium; filed 02-07-2026; Last balance sheet year 2025; FTE 75.4; raw docs/doge/data/raw/tick2051/van_lierde_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR WZC Van Lierde YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0633854022/woonzorgcentrum-van-lierde",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2051; FR mirror YE2025 Medium; depose le 02-07-2026; raw docs/doge/data/raw/tick2051/van_lierde_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO WZC Van Lierde 0633.854.022 Actief VZW Affligem",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0633854022",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2051; Actief VZW; Bellestraat 3 1790 Affligem; 1 VE; NACE 87.301; KBO email empty; aanbestedende overheid flag not present in KBO extract",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "WZC Van Lierde site onthaal@wzcvanlierde.be",
        "url": "https://www.vanlierde-wzc.be/",
        "publisher": "WZC Van Lierde",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2051; site lists onthaal@wzcvanlierde.be; raw docs/doge/data/raw/tick2051/van_lierde_site.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_van_lierde_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2051; omzet DROP {OMZET} -0.89pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_van_lierde_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2051; pnl DROP {PNL} -12.83pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_van_lierde_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2051; equity JUMP {EQUITY} +2.31pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_van_lierde_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2051; bruto JUMP {BRUTO} +2.88pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_van_lierde_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2051; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_van_lierde_jr2025_statutory_wzc",
    "title": "WZC Van Lierde YE2025 leftover dual (omzet DROP 7.53m / pnl DROP 0.46m)",
    "entity_id": ENTITY,
    "beneficiary": "Vlaams-Brabant elderly-care residents (WZC Van Lierde Affligem)",
    "legal_basis": "VZW WZC operator (KBO 0633.854.022)",
    "decision_date": "2026-07-02",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0633854022/woonzorgcentrum-van-lierde",
    "stated_goal": "WZC Van Lierde Affligem",
    "cut_option": "Publish NBB PDF assets/debt + explain pnl DROP vs omzet DROP FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Affligem>VanLierde>JR2025_statutory_L5",
    "notes": "tick2051; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_van_lierde_omzet_drop_7_53m_pnl_drop_jr2025",
    "name": "Van Lierde omzet DROP 7.53m / pnl DROP 0.46m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Affligem>VanLierde>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; VZW WZC dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "Vlaams-Brabant elderly-care residents via Van Lierde Affligem",
    "stated_goal": "WZC Van Lierde",
    "measured_outcome": "Medium CW YE2025; 7.53m omzet DROP -0.89pct with pnl DROP -12.83pct; NBB PDF residual",
    "absurdity_score": "4.8",
    "cost_score": "4.7",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP; map subsidy stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2051 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Woonzorgcentrum Van Lierde (Affligem)",
    "name_fr": "Maison de repos et de soins Van Lierde (Affligem)",
    "name_en": "Van Lierde nursing home (Affligem)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.vanlierde-wzc.be/",
    "foi_email": "onthaal@wzcvanlierde.be",
    "foi_postal": "Bellestraat 3, 1790 Affligem",
    "notes": (
        "tick2051 YE2025 Medium CW NL+EN+FR + Strong KBO 0633.854.022 Actief VZW 1 VE; omzet DROP 7.53m pnl DROP 0.46m equity JUMP 5.69m bruto JUMP 6.89m FTE 75.4; "
        "assets/debt Unknown; neerlegging 02.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer"
    ),
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Vlaanderen>VlaamsBrabant>Affligem>VanLierde>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; explanation of pnl DROP -12.83pct vs mild omzet DROP",
    "why_it_matters": "Medium CW shows 7.53m omzet VL WZC VZW with pnl DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Woonzorgcentrum Van Lierde vzw",
    "recipient_email": "onthaal@wzcvanlierde.be",
    "recipient_postal": "Bellestraat 3, 1790 Affligem",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_van_lierde_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_van_lierde_omzet_drop_7_53m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2051; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — WZC Van Lierde (NBB PDF / assets-debt / pnl-drop matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Woonzorgcentrum Van Lierde VZW — KBO **0633.854.022**  
**recipient:** onthaal@wzcvanlierde.be · Bellestraat 3, 1790 Affligem  
**sources:** [CW NL](https://www.companyweb.be/nl/0633854022/woonzorgcentrum-van-lierde) · [CW EN](https://www.companyweb.be/en/0633854022/woonzorgcentrum-van-lierde) · [CW FR](https://www.companyweb.be/fr/0633854022/woonzorgcentrum-van-lierde) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0633854022) · [site](https://www.vanlierde-wzc.be/)  
**tick:** 2051  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **02.07.2026**): omzet **EUR7,532,068** DROP −0.89%; pnl **EUR461,544** DROP −12.83% vs YE2024 EUR529,480; equity **EUR5,687,790** JUMP +2.31%; bruto **EUR6,890,078** JUMP +2.88%; FTE **75.4**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Bellestraat 3 Affligem; NACE 87.301.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Woonzorgcentrum Van Lierde vzw — Bellestraat 3, 1790 Affligem
onthaal@wzcvanlierde.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Van Lierde + subsidiematrix (KBO 0633.854.022)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 02.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting pnl DROP (van EUR529.480 YE2024 naar EUR461.544 YE2025) bij milde omzet DROP.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, "
    "Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, "
    "Molenheide WZC, Veilige Have, Witte Meren, Sint-Jozef Rumst, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2051":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Hof ter Waarbeek — WZC Van Lierde YE2025 Medium"
        x["notes"] = (
            "tick2051 Van Lierde Medium omzet DROP 7.53m pnl DROP 0.46m equity JUMP 5.69m bruto JUMP 6.89m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2052; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover WZC Van Lierde YE2025 Medium CW; KBO 0633.854.022; "
            f"omzet DROP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2052" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2052",
            "title": "leftover dual hole-fill after Van Lierde",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2051 after Van Lierde YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2051 Van Lierde; next every-10 2060",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2051",
        "ticks_completed": "2051",
        "paused": "no",
        "notes": (
            "tick2051 leftover Van Lierde 0633.854.022 Medium CW (omzet DROP 7.53m pnl DROP 0.46m equity JUMP 5.69m bruto JUMP 6.89m FTE 75.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2052; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2051 - {UTC} - rq_2051 WZC Van Lierde (omzet DROP 7.53m / pnl DROP 0.46m / Medium)

- Unit: **rq_2051** leftover dual after **rq_2050 Hof ter Waarbeek**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **WZC Van Lierde** YE2025 (KBO **0633.854.022**; Bellestraat 3 Affligem; Vlaams-Brabant **VZW** WZC / **1 VE**). Do not redo Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Ternat/Zilverbos/Mayerhof/Evara/Multiversum/Maria Rustoord/PPC Pittem/WZC Sint-Vincentius Avelgem/PC Sint-Hieronymus/WZC Sint-Barbara/PC Gent-Sleidinge/Molenheide/Veilige Have/Witte Meren/Sint-Jozef Rumst.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR7,532,068** DROP −0.89%; pnl **EUR461,544** DROP −12.83%; equity **EUR5,687,790** JUMP +2.31%; bruto **EUR6,890,078** JUMP +2.88%; FTE **75.4**; neerlegging **02.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email onthaal@wzcvanlierde.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2051=done + rq_2052 open; loop_state ticks=2051; raw under docs/doge/data/raw/tick2051/.
- FOI: **ready not sent** (human-gated; onthaal@wzcvanlierde.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2052 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2051 Van Lierde", OMZET, "pi", PI)
