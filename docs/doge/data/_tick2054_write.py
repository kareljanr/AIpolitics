# ephemeral tick2054 — Seniorenzorg St-Vincentius Lendelede YE2025 Medium
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T18:35:00Z"
ENTITY = "vzw_seniorenzorg_st_vincentius_lendelede"
GAP = "gap_lendelede_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_lendelede_jr2025_cw"
SRC_EN = "src_lendelede_jr2025_cw_en"
SRC_FR = "src_lendelede_jr2025_cw_fr"
SRC_KBO = "src_lendelede_kbo_2054"
SRC_SITE = "src_lendelede_site_2054"
SRC_EMAIL = "src_lendelede_zorg_repertorium_email_2054"

OMZET = "6678491"
PNL = "410246"
EQUITY = "8894294"
BRUTO = "6864614"
FTE = "83.5"
OMZET24 = "6317326"
PNL24 = "228837"
EQUITY24 = "8703474"
BRUTO24 = "6431980"
# pi = 0.55*4.6 + 0.35*4.5 + 0.10*(10-4) = 2.53 + 1.575 + 0.6 = 4.705 → 4.7
PI = "4.7"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2054")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Seniorenzorg St-Vincentius Lendelede YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0461511449/seniorenzorg-st-vincentius-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2054; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 01.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2054/lendelede_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Seniorenzorg St-Vincentius Lendelede YE2025 statutory",
        "url": "https://www.companyweb.be/en/0461511449/seniorenzorg-st-vincentius-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2054; EN mirror YE2025 Medium; filed 01-07-2026; Last balance sheet year 2025; FTE 83.5; raw docs/doge/data/raw/tick2054/lendelede_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Seniorenzorg St-Vincentius Lendelede YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0461511449/seniorenzorg-st-vincentius-vzw",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2054; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2054/lendelede_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Seniorenzorg St-Vincentius Lendelede 0461.511.449 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461511449",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2054; Actief VZW; Izegemsestraat 14 8860 Lendelede; 1 VE; NACE 87.101; KBO email empty; aanbestedende overheid flag not present in KBO extract",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Seniorenzorg Lendelede website",
        "url": "https://www.seniorenzorglendelede.be/",
        "publisher": "Seniorenzorg St-Vincentius Lendelede",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2054; site HTTP 200; email not in HTML; raw docs/doge/data/raw/tick2054/lendelede_site.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EMAIL,
        "title": "Departement Zorg WZC repertorium — Lendelede directie@seniorenzorglendelede.be",
        "url": "https://www.zorg-en-gezondheid.be/sites/default/files/external/Repertorium_burst_def_-_ADRESSEN_WZC-_PROVINCIE_West-Vlaanderen.pdf",
        "publisher": "Departement Zorg Vlaanderen",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2054; repertorium lists directie@seniorenzorglendelede.be / Izegemsestraat 14 Lendelede / Aksent WZC",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_lendelede_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2054; omzet JUMP {OMZET} +5.72pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_lendelede_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2054; pnl JUMP {PNL} +79.27pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_lendelede_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2054; equity JUMP {EQUITY} +2.19pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_lendelede_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2054; bruto JUMP {BRUTO} +6.73pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_lendelede_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2054; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_lendelede_jr2025_statutory_wzc",
    "title": "Seniorenzorg Lendelede YE2025 leftover dual (omzet JUMP 6.68m / pnl JUMP 0.41m)",
    "entity_id": ENTITY,
    "beneficiary": "West-Vlaanderen elderly-care residents (Aksent / Seniorenzorg Lendelede)",
    "legal_basis": "VZW WZC operator (KBO 0461.511.449)",
    "decision_date": "2026-07-01",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0461511449/seniorenzorg-st-vincentius-vzw",
    "stated_goal": "WZC Seniorenzorg St-Vincentius Lendelede (Aksent)",
    "cut_option": "Publish NBB PDF assets/debt + subsidy vs dagprijs split FOI",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Lendelede>SeniorenzorgStVincentius>JR2025_statutory_L5",
    "notes": "tick2054; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Ganspoel/Westerhauwe deferred if still live; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_lendelede_omzet_jump_6_68m_pnl_jump_jr2025",
    "name": "Seniorenzorg Lendelede omzet JUMP 6.68m / pnl JUMP 0.41m (YE2025)",
    "level": "L5",
    "type": "vzw_wzc_dual",
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Lendelede>SeniorenzorgStVincentius>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown; VZW WZC dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "West-Vlaanderen elderly-care residents via Seniorenzorg Lendelede",
    "stated_goal": "WZC Seniorenzorg St-Vincentius Lendelede",
    "measured_outcome": "Medium CW YE2025; 6.68m omzet JUMP +5.72pct with pnl JUMP +79.27pct; NBB PDF residual",
    "absurdity_score": "4.5",
    "cost_score": "4.6",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; map subsidy vs dagprijs stack",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2054 leftover dual; Medium CW; TE-adjacent care flow not pure-waste top10; next every-10 2060",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Seniorenzorg St-Vincentius Lendelede / Aksent (VZW)",
    "name_fr": "Soins aux seniors St-Vincentius Lendelede / Aksent (ASBL)",
    "name_en": "Seniorenzorg St-Vincentius Lendelede (VZW nursing home)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.seniorenzorglendelede.be/",
    "foi_email": "directie@seniorenzorglendelede.be",
    "foi_postal": "Izegemsestraat 14, 8860 Lendelede",
    "notes": (
        "tick2054 YE2025 Medium CW NL+EN+FR + Strong KBO 0461.511.449 Actief VZW 1 VE; omzet JUMP 6.68m pnl JUMP 0.41m equity JUMP 8.89m bruto JUMP 6.86m FTE 83.5; "
        "assets/debt Unknown; neerlegging 01.07.2026; FOI "
        + GAP
        + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/Lourdes/St Vincentius Antwerpen/Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have"
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
    "hierarchy_path": "Vlaanderen>WestVlaanderen>Lendelede>SeniorenzorgStVincentius>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); public subsidy vs dagprijs split; corroboration of pnl JUMP +79pct",
    "why_it_matters": "Medium CW shows 6.68m omzet VL WZC VZW without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "Seniorenzorg St-Vincentius Lendelede vzw",
    "recipient_email": "directie@seniorenzorglendelede.be",
    "recipient_postal": "Izegemsestraat 14, 8860 Lendelede",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_lendelede_jr2025_statutory_wzc",
    "linked_leaderboard_id": "lb_lendelede_omzet_jump_6_68m_pnl_jump_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2054; human-send only; Medium CW; next every-10 2060",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Seniorenzorg Lendelede (NBB PDF / assets-debt / pnl-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Seniorenzorg St-Vincentius Lendelede VZW — KBO **0461.511.449**  
**recipient:** directie@seniorenzorglendelede.be · Izegemsestraat 14, 8860 Lendelede  
**sources:** [CW NL](https://www.companyweb.be/nl/0461511449/seniorenzorg-st-vincentius-vzw) · [CW EN](https://www.companyweb.be/en/0461511449/seniorenzorg-st-vincentius-vzw) · [CW FR](https://www.companyweb.be/fr/0461511449/seniorenzorg-st-vincentius-vzw) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0461511449) · [site](https://www.seniorenzorglendelede.be/) · [Zorg repertorium](https://www.zorg-en-gezondheid.be/sites/default/files/external/Repertorium_burst_def_-_ADRESSEN_WZC-_PROVINCIE_West-Vlaanderen.pdf)  
**tick:** 2054  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **01.07.2026**): omzet **EUR6,678,491** JUMP +5.72%; pnl **EUR410,246** JUMP +79.27% vs YE2024 EUR228,837; equity **EUR8,894,294** JUMP +2.19%; bruto **EUR6,864,614** JUMP +6.73%; FTE **83.5**; assets/debt **Unknown**.
- KBO: Actief VZW; **1 VE**; zetel Izegemsestraat 14 Lendelede; NACE 87.101.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Seniorenzorg St-Vincentius Lendelede vzw — Izegemsestraat 14, 8860 Lendelede
directie@seniorenzorglendelede.be
cc: Departement Zorg / Agentschap Zorg en Gezondheid indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Seniorenzorg Lendelede + subsidiematrix (KBO 0461.511.449)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde WZC-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 01.07.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split publieke subsidies (IFIC, Alivia, Vlaio, andere code73/74) vs dagprijzen/supplementen 2025.
4. Toelichting pnl JUMP (van EUR228.837 YE2024 naar EUR410.246 YE2025).
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo Seniorenzorg Lendelede, Walfergem, Ter Berk/Seniorenzorg Sint-Vincentius Anzegem, Van Lierde, Hof ter Waarbeek, "
    "Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, Zorggroep Zusters van Berlaar, "
    "Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, C.W.Z.C. Zonhoven, Orelia Zorg, "
    "WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, Cassiers WZC, "
    "WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, WZC De Foyer Gent, "
    "Sint-Jozef Rumst, Veilige Have, Witte Meren, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, "
    "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
    "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, Armonea. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2054":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Walfergem — Seniorenzorg Lendelede YE2025 Medium"
        x["notes"] = (
            "tick2054 Lendelede Medium omzet JUMP 6.68m pnl JUMP 0.41m equity JUMP 8.89m bruto JUMP 6.86m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Ganspoel/Westerhauwe deferred if still live; next rq_2055; next every-10 2060"
        )
        x["instructions"] = (
            "Completed leftover Seniorenzorg St-Vincentius Lendelede YE2025 Medium CW; KBO 0461.511.449; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity JUMP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_2055" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2055",
            "title": "leftover dual hole-fill after Seniorenzorg Lendelede",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2054 after Seniorenzorg Lendelede YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych "
                "(Centrum Ganspoel YE2025 if still deferred / Huize Westerhauwe YE2025 if unmined / other unused YE2025 if live with omzet). "
                + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2054 Lendelede; next every-10 2060; Ganspoel/Westerhauwe if still live deferred",
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
        "last_unit_id": "rq_2054",
        "ticks_completed": "2054",
        "paused": "no",
        "notes": (
            "tick2054 leftover Seniorenzorg Lendelede 0461.511.449 Medium CW (omzet JUMP 6.68m pnl JUMP 0.41m equity JUMP 8.89m bruto JUMP 6.86m FTE 83.5; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Ganspoel/Westerhauwe deferred if still live; next rq_2055; next every-10 2060; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2054 - {UTC} - rq_2054 Seniorenzorg Lendelede (omzet JUMP 6.68m / pnl JUMP 0.41m / Medium)

- Unit: **rq_2054** leftover dual after **rq_2053 Walfergem**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took deferred leftover **Seniorenzorg St-Vincentius Lendelede** YE2025 (KBO **0461.511.449**; Izegemsestraat 14 Lendelede; West-Vlaanderen **VZW** WZC / **1 VE**). Centrum Ganspoel / Huize Westerhauwe YE2025 may still be live — deferred. Do not redo Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/De Verlosser/Zorggroep Zusters van Berlaar/Psychogeriatrisch/De Linde/Samen Ouder/C.W.Z.C. Zonhoven/Orelia/Kanunnik Triest/OLVA/Roosdaal/Bernardus Assenede/Cassiers/OLV Lourdes/St Vincentius Antwerpen/Sint-Jozef Rillaar/Karus/De Foyer/Sint-Jozef Rumst/Veilige Have/Witte Meren.
- Found: Companyweb NL+EN+FR YE2025 — omzet **EUR6,678,491** JUMP +5.72%; pnl **EUR410,246** JUMP +79.27%; equity **EUR8,894,294** JUMP +2.19%; bruto **EUR6,864,614** JUMP +6.73%; FTE **83.5**; neerlegging **01.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email directie@seniorenzorglendelede.be (Departement Zorg repertorium).
- Wrote: sources (+6); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2054=done + rq_2055 open; loop_state ticks=2054; raw under docs/doge/data/raw/tick2054/.
- FOI: **ready not sent** (human-gated; directie@seniorenzorglendelede.be).
- NOT every-10 (**next every-10 is 2060**). Next: rq_2055 (AGB/FARO-if-YE2025 / AIESH-REW / Ganspoel-Westerhauwe if live / unused DSO-IGS-HVZ-WZC-psych).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
print("DONE tick2054 Lendelede", OMZET, "pi", PI)
