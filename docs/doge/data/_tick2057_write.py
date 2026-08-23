# ephemeral tick2057 — Groep Zorg H. Familie YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T19:20:00Z"
ENTITY = "vzw_groep_zorg_h_familie"
GAP = "gap_groep_zorg_h_familie_nbb_pdf_assets_debt_pnl_drop_matrix_l5"
SRC = "src_h_familie_jr2025_cw"
SRC_EN = "src_h_familie_jr2025_cw_en"
SRC_FR = "src_h_familie_jr2025_cw_fr"
SRC_KBO = "src_h_familie_kbo_2057"
SRC_SITE = "src_h_familie_site_2057"

OMZET = "62090224"
PNL = "2799756"
EQUITY = "77102105"
BRUTO = "65849946"
FTE = "748.5"
OMZET24 = "60304985"
PNL24 = "4805062"
EQUITY24 = "72072016"
BRUTO24 = "61009339"
# pi = 0.55*6.3 + 0.35*5.5 + 0.10*(10-4) = 3.465 + 1.925 + 0.6 = 5.99 → 6.0
PI = "6.0"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2057")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Groep Zorg H. Familie YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0414693113/groep-zorg-h-familie",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2057; YE2025 omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 18.06.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2057/h_familie_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Groep Zorg H. Familie YE2025 statutory",
        "url": "https://www.companyweb.be/en/0414693113/groep-zorg-h-familie",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2057; EN mirror YE2025 Medium; filed 18-06-2026; Last balance sheet year 2025; FTE 748.5; raw docs/doge/data/raw/tick2057/h_familie_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Groep Zorg H. Familie YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0414693113/groep-zorg-h-familie",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2057; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2057/h_familie_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Groep Zorg H. Familie 0414.693.113 Actief VZW aanbestedende overheid Kortrijk",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414693113",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2057; Actief VZW; Plein 26 8500 Kortrijk (since 01.01.2026); 16 VE; aanbestedende overheid sinds 11.07.1974; NACE 87.101; KBO email empty",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Groep Zorg H. Familie site info@zorghf.be",
        "url": "https://zorghf.be/",
        "publisher": "Groep Zorg H. Familie vzw",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2057; West-Vlaanderen ouderenzorg + GGZ + VAPH; site/contact/bestuur list info@zorghf.be; phone 056 30 55 33; raw docs/doge/data/raw/tick2057/zorghf.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_h_familie_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2057; omzet JUMP {OMZET} +2.96pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_h_familie_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2057; pnl DROP {PNL} -41.73pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_h_familie_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2057; equity JUMP {EQUITY} +6.98pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_h_familie_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2057; bruto JUMP {BRUTO} +7.93pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_h_familie_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2057; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_h_familie_jr2025_statutory_zorggroep",
    "title": "Groep Zorg H. Familie YE2025 leftover dual (omzet JUMP 62.09m / pnl DROP 2.80m)",
    "entity_id": ENTITY,
    "beneficiary": "West-Vlaanderen elderly + GGZ + VAPH residents (Groep Zorg H. Familie multi-site)",
    "legal_basis": "VZW zorggroep / aanbestedende overheid (KBO 0414.693.113)",
    "decision_date": "2026-06-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0414693113/groep-zorg-h-familie",
    "stated_goal": "Multi-site West-Vlaanderen ouderenzorg / GGZ / VAPH (Zusters H. Familie)",
    "cut_option": "Publish NBB PDF assets/debt + explain pnl DROP -42pct vs omzet JUMP FOI; map campus subsidy matrix",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>GroepZorgHFamilie>JR2025_statutory_L5",
    "notes": "tick2057; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_h_familie_omzet_jump_62_09m_pnl_drop_jr2025",
    "name": "Groep Zorg H. Familie omzet JUMP 62.09m / pnl DROP 2.80m (YE2025)",
    "level": "L5",
    "type": "vzw_zorggroep_aanbestedende_overheid_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>GroepZorgHFamilie>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; aanbestedende overheid VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "West-Vlaanderen elderly/GGZ/VAPH residents via Groep Zorg H. Familie",
    "stated_goal": "Multi-site ouderenzorg / GGZ / VAPH",
    "measured_outcome": "Medium CW YE2025; 62.09m omzet JUMP +2.96pct with pnl DROP -41.73pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "6.3",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl DROP vs omzet JUMP; map campus subsidy matrix",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2057 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Groep Zorg H. Familie (VZW, Kortrijk multi-site)",
    "name_fr": "Groupe de soins Sainte-Famille (ASBL, Courtrai multi-sites)",
    "name_en": "Groep Zorg H. Familie (VZW multi-site care group Kortrijk)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://zorghf.be/",
    "foi_email": "info@zorghf.be",
    "foi_postal": "Plein 26, 8500 Kortrijk",
    "notes": (
        "tick2057 YE2025 Medium CW NL+EN+FR + Strong KBO 0414.693.113 Actief VZW aanbestedende overheid 16 VE; omzet JUMP 62.09m pnl DROP 2.80m equity JUMP 77.10m bruto JUMP 65.85m FTE 748.5; "
        "assets/debt Unknown; neerlegging 18.06.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Kortrijk>GroepZorgHFamilie>NBB_PDF_assets_debt_pnl_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs/GGZ/VAPH split; explanation of pnl DROP -42pct despite omzet JUMP; campus matrix across 16 VE",
    "why_it_matters": "Medium CW shows 62.09m omzet VL aanbestedende-overheid zorggroep VZW with sharp pnl DROP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Groep Zorg H. Familie vzw",
    "recipient_email": "info@zorghf.be",
    "recipient_postal": "Plein 26, 8500 Kortrijk",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_h_familie_jr2025_statutory_zorggroep",
    "linked_leaderboard_id": "lb_h_familie_omzet_jump_62_09m_pnl_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2057; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Groep Zorg H. Familie (NBB PDF / assets-debt / pnl-drop)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Groep Zorg H. Familie VZW — KBO **0414.693.113**  
**recipient:** info@zorghf.be · Plein 26, 8500 Kortrijk  
**sources:** [CW NL](https://www.companyweb.be/nl/0414693113/groep-zorg-h-familie) · [CW EN](https://www.companyweb.be/en/0414693113/groep-zorg-h-familie) · [CW FR](https://www.companyweb.be/fr/0414693113/groep-zorg-h-familie) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0414693113) · [site](https://zorghf.be/)  
**tick:** 2057  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **18.06.2026**): omzet **EUR62,090,224** JUMP +2.96%; pnl **EUR2,799,756** DROP −41.73% vs YE2024 EUR4,805,062; equity **EUR77,102,105** JUMP +6.98%; bruto **EUR65,849,946** JUMP +7.93%; FTE **748.5**; assets/debt **Unknown**.
- KBO: Actief VZW **aanbestedende overheid**; **16 VE**; zetel Plein 26 Kortrijk; NACE 87.101.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Groep Zorg H. Familie vzw — Plein 26, 8500 Kortrijk
info@zorghf.be
cc: Departement Zorg / VAPH indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Groep Zorg H. Familie + subsidiematrix (KBO 0414.693.113)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (VZW is aanbestedende overheid) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 18.06.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC/Alivia/Vlaio/VAPH/andere code73/74) vs dagprijzen/GGZ-inkomsten 2025.
4. Toelichting pnl DROP (van EUR4.805.062 YE2024 naar EUR2.799.756 YE2025) bij omzet JUMP.
5. Niet-confidentieel overzicht omzet/resultaat per campus of VE-groep (16 VE).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, "
    "Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, "
    "AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, "
    "Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, "
    "WZC Sint-Bernardus Assenede, Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, "
    "WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, "
    "IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
    "NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2057":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Huize Westerhauwe — Groep Zorg H. Familie YE2025 Medium"
        x["notes"] = (
            "tick2057 Groep Zorg H. Familie Medium omzet JUMP 62.09m pnl DROP 2.80m equity JUMP 77.10m bruto JUMP 65.85m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2058; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover Groep Zorg H. Familie YE2025 Medium CW; KBO 0414.693.113; "
            f"omzet JUMP {OMZET} pnl DROP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2058" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2058",
            "title": "leftover dual hole-fill after Groep Zorg H. Familie",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2057 after Groep Zorg H. Familie YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2057 Groep Zorg H. Familie; next every-10 2060",
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
        "last_unit_id": "rq_2057",
        "ticks_completed": "2057",
        "paused": "no",
        "notes": (
            "tick2057 leftover Groep Zorg H. Familie 0414.693.113 Medium CW (omzet JUMP 62.09m pnl DROP 2.80m equity JUMP 77.10m bruto JUMP 65.85m FTE 748.5; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2058; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2057 - {UTC} - rq_2057 Groep Zorg H. Familie (omzet JUMP 62.09m / pnl DROP 2.80m / Medium)

- Unit: **rq_2057** leftover dual after **rq_2056 Huize Westerhauwe**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took unused leftover **Groep Zorg H. Familie** YE2025 (KBO **0414.693.113**; Plein 26 Kortrijk; West-Vlaanderen **aanbestedende-overheid VZW** multi-site ouderenzorg/GGZ/VAPH / **16 VE**). Do not redo Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR62,090,224** JUMP +2.96%; pnl **EUR2,799,756** DROP −41.73%; equity **EUR77,102,105** JUMP +6.98%; bruto **EUR65,849,946** JUMP +7.93%; FTE **748.5**; neerlegging **18.06.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW aanbestedende overheid 16 VE; email info@zorghf.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2057=done + rq_2058 open; loop_state ticks=2057; raw under docs/doge/data/raw/tick2057/.
- FOI: **ready not sent** (human-gated; info@zorghf.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2058 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2057 Groep Zorg H. Familie", OMZET, "pi", PI)
