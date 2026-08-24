# tick2232 — SDB YE2025 Medium leftover dual (named FREE after De Vleugels)
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DATA = ROOT / "docs" / "doge" / "data"
FOI_DRAFTS = ROOT / "docs" / "doge" / "foi" / "drafts"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
csv.field_size_limit(10_000_000)

ENTITY = "vzw_sdb_sint_truiden"
TICK = "2232"
UTC = "2026-08-26T23:05:00Z"
GAP = "gap_sdb_nbb_pdf_assets_debt_pnl_profit_flip_equity_jump_dienstencheque_matrix_l5"
COMM = "comm_sdb_jr2025_statutory_dienstencheque_omzet_jump_pnl_profit_flip"
LB = "lb_sdb_omzet_9_36m_pnl_profit_flip_equity_jump_57pct_jr2025"

OM25, OM24 = 9359256, 8133636
BR25, BR24 = 9589392, 7790296
PN25, PN24 = 310590, -115565
EQ25, EQ24 = 1684585, 1070506
FTE25, FTE24 = 241.9, 214.9


def read_csv(name: str) -> tuple[list[str], list[dict]]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames or []), list(r)


def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (DATA / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in fields})


def upsert(rows: list[dict], key: str, kid: str, new: dict) -> None:
    for i, r in enumerate(rows):
        if r.get(key) == kid:
            rows[i] = {**r, **new}
            return
    rows.append(new)


s_fields, sources = read_csv("sources.csv")
for sid, title, url, publisher, sclass, notes in [
    (
        "src_sdb_jr2025_cw_nl",
        "Companyweb NL SDB YE2025 statutory",
        "https://www.companyweb.be/nl/0665861844/sdb",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; YE2025 omzet JUMP {OM25} (+15.07%) bruto JUMP {BR25} (+23.09%) "
            f"pnl PROFIT FLIP {PN25} vs YE2024 {PN24} equity JUMP {EQ25} (+57.36%) "
            f"FTE {FTE25}; filed 28-04-2026"
        ),
    ),
    (
        "src_sdb_jr2025_cw_en",
        "Companyweb EN SDB YE2025 statutory",
        "https://www.companyweb.be/en/0665861844/sdb",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        (
            f"tick{TICK}; EN mirror; Turnover {OM25}; Gross margin {BR25}; Profit/Loss {PN25}; "
            f"Equity {EQ25}; Employees {FTE25}; filed 28-04-2026"
        ),
    ),
    (
        "src_sdb_jr2025_cw_fr",
        "Companyweb FR SDB YE2025 statutory",
        "https://www.companyweb.be/fr/0665861844/sdb",
        "Companyweb (NBB-derived)",
        "secondary_aggregator",
        f"tick{TICK}; FR mirror; CA {OM25}; Marge brute {BR25}; Benefice {PN25}",
    ),
    (
        "src_sdb_kbo_2232",
        "KBO SDB 0665.861.844 Actief Sint-Truiden 8 VE",
        "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0665861844",
        "KBO FOD Economie",
        "official_register",
        (
            "tick2232; Actief VZW Sociaal Dienstenchequebedrijf; zetel Diesterstraat 27/11 "
            "3800 Sint-Truiden; 8 VE Actief; NACE RSZ 88.999; info@vzw-sdbe.be; www.vzw-sdb.be; "
            "tel 011 711 270"
        ),
    ),
    (
        "src_sdb_site_contact_2232",
        "SDB FOI channel info@vzw-sdbe.be",
        "http://www.vzw-sdb.be",
        "SDB VZW",
        "foi_contact",
        "tick2232; info@vzw-sdbe.be; 011 711 270; Diesterstraat 27/11 3800 Sint-Truiden",
    ),
]:
    upsert(
        sources,
        "source_id",
        sid,
        {
            "source_id": sid,
            "title": title,
            "url": url,
            "publisher": publisher,
            "accessed_date": "2026-08-26",
            "source_class": sclass,
            "notes": notes,
        },
    )
write_csv("sources.csv", s_fields, sources)

e_fields, entities = read_csv("entities.csv")
upsert(
    entities,
    "entity_id",
    ENTITY,
    {
        "entity_id": ENTITY,
        "name_nl": "SDB VZW / Sociaal Dienstenchequebedrijf (Sint-Truiden)",
        "name_fr": "SDB ASBL / Entreprise sociale titres-services (Sint-Truiden)",
        "name_en": "SDB VZW / Social service-voucher company (Sint-Truiden)",
        "level": "parastatal",
        "parent_id": "sec_flanders",
        "community_language": "nl",
        "website": "http://www.vzw-sdb.be",
        "foi_email": "info@vzw-sdbe.be",
        "foi_postal": "Diesterstraat 27/11, 3800 Sint-Truiden",
        "notes": (
            f"tick{TICK} YE2025 Medium CW NL+EN+FR + Strong KBO 0665.861.844 Actief 8 VE "
            f"NACE 88.999; omzet JUMP {OM25} bruto JUMP {BR25} pnl PROFIT FLIP {PN25} equity "
            f"JUMP {EQ25} (+57.36%) FTE JUMP {FTE25}; neerlegging 28.04.2026; assets/debt "
            f"Unknown; FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "Heropbeuring CW opaque; deferred FREE Travie/Rucher YE2025; not TE-additive of 348bn"
        ),
    },
)
write_csv("entities.csv", e_fields, entities)

b_fields, budgets = read_csv("budgets.csv")
for bid, year, amt, basis, notes in [
    (
        "bud_sdb_omzet_jr2025_statutory",
        "2025",
        OM25,
        "CW statutory omzet YE2025",
        f"tick{TICK}; Medium CW; omzet JUMP +15.07% vs YE2024 {OM24}; primary envelope",
    ),
    (
        "bud_sdb_bruto_jr2025_statutory",
        "2025",
        BR25,
        "CW statutory bruto_marge YE2025",
        f"tick{TICK}; Medium CW; bruto JUMP +23.09% vs YE2024 {BR24}",
    ),
    (
        "bud_sdb_pnl_jr2025_statutory",
        "2025",
        PN25,
        "CW statutory winst/verlies YE2025",
        f"tick{TICK}; Medium CW; pnl PROFIT FLIP vs YE2024 LOSS {PN24}",
    ),
    (
        "bud_sdb_equity_jr2025_statutory",
        "2025",
        EQ25,
        "CW statutory eigen_vermogen YE2025",
        f"tick{TICK}; Medium CW; equity JUMP +57.36% vs YE2024 {EQ24}",
    ),
    (
        "bud_sdb_fte_jr2025_statutory",
        "2025",
        FTE25,
        "CW social-balance FTE 241.9",
        f"tick{TICK}; Medium CW; FTE JUMP {FTE25} vs YE2024 {FTE24}; assets/debt Unknown",
    ),
    (
        "bud_sdb_pnl_jr2024_statutory_cmp",
        "2024",
        PN24,
        "CW statutory winst/verlies YE2024 comparative (LOSS)",
        f"tick{TICK}; YE2024 pnl LOSS {PN24} comparative (pre PROFIT FLIP)",
    ),
]:
    upsert(
        budgets,
        "budget_id",
        bid,
        {
            "budget_id": bid,
            "entity_id": ENTITY,
            "year": year,
            "amount_eur": str(amt),
            "amount_min_eur": str(amt),
            "amount_max_eur": str(amt),
            "basis": basis,
            "source_id": "src_sdb_jr2025_cw_en",
            "confidence": "medium",
            "notes": notes,
        },
    )
write_csv("budgets.csv", b_fields, budgets)

c_fields, commitments = read_csv("commitments.csv")
cash = (
    f'{{"2025_omzet":{OM25},"2025_bruto":{BR25},"2025_pnl":{PN25},"2025_equity":{EQ25},'
    f'"2025_fte":{FTE25},"2024_omzet":{OM24},"2024_bruto":{BR24},"2024_pnl":{PN24},'
    f'"2024_equity":{EQ24},"2024_fte":{FTE24}}}'
)
upsert(
    commitments,
    "commitment_id",
    COMM,
    {
        "commitment_id": COMM,
        "title": (
            "SDB YE2025 leftover dual (omzet JUMP 9.36m / pnl PROFIT FLIP +311k / "
            "equity JUMP +57% / Medium)"
        ),
        "entity_id": ENTITY,
        "beneficiary": (
            "dienstencheque household clients Limburg (Sint-Truiden) / public service-voucher path"
        ),
        "legal_basis": (
            "VZW Sociaal Dienstenchequebedrijf (KBO 0665.861.844; Actief; 8 VE; NACE 88.999)"
        ),
        "decision_date": "2026-04-28",
        "start_year": "2025",
        "end_year": "2025",
        "total_envelope_eur": str(OM25),
        "cash_by_year": cash,
        "remaining_eur": "0",
        "status": "active",
        "evaluation_url": "https://www.companyweb.be/en/0665861844/sdb",
        "stated_goal": "Social service-voucher / huishoudhulp employment",
        "cut_option": (
            "Publish NBB PDF assets/debt FOI; reconcile pnl PROFIT FLIP (LOSS -116k -> +311k) "
            "with omzet JUMP +15% and FTE JUMP; federal/regional dienstencheque subsidy matrix; "
            "8-VE cost allocation; equity JUMP +57% drivers"
        ),
        "source_id": "src_sdb_jr2025_cw_en",
        "confidence": "medium",
        "hierarchy_path": "Vlaanderen>Limburg>SintTruiden>SDB>JR2025_statutory_L5",
        "notes": (
            f"tick{TICK}; Medium CW; omzet primary envelope {OM25}; pnl PROFIT FLIP; equity "
            f"JUMP +57.36%; FTE JUMP {FTE25}; 8 VE; named prefer in rq_2232 after De Vleugels; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque; deferred "
            "Travie/Rucher; not TE-additive"
        ),
    },
)
write_csv("commitments.csv", c_fields, commitments)

l_fields, leaderboard = read_csv("leaderboard.csv")
upsert(
    leaderboard,
    "item_id",
    LB,
    {
        "item_id": LB,
        "name": (
            "SDB omzet JUMP 9.36m / pnl PROFIT FLIP +311k / equity JUMP +57% "
            "(YE2025 dienstencheque)"
        ),
        "level": "L5",
        "type": "dienstencheque_vzw_statutory",
        "hierarchy_path": "Vlaanderen>Limburg>SintTruiden>SDB>JR2025",
        "annual_cost_eur": str(OM25),
        "total_cost_eur": str(OM25),
        "tco_notes": (
            f"CW omzet JUMP {OM25} / bruto {BR25} / pnl PROFIT FLIP {PN25} (from LOSS {PN24}) / "
            f"equity JUMP {EQ25} (+57.36%) / FTE JUMP {FTE25} / 8 VE Sint-Truiden dienstencheque"
        ),
        "confidence": "medium",
        "source_id": "src_sdb_jr2025_cw_en",
        "beneficiaries": "dienstencheque households Limburg / public service-voucher path",
        "stated_goal": "Social service-voucher employment",
        "measured_outcome": (
            f"omzet JUMP +15.07%; bruto JUMP +23.09%; pnl PROFIT FLIP (-116k->+311k); equity "
            f"JUMP +57.36%; FTE JUMP {FTE25} vs {FTE24}; 8 VE; filed 28.04.2026"
        ),
        "absurdity_score": "7.0",
        "cost_score": "5.5",
        "difficulty": "3.0",
        "priority_index": "6.20",
        "cut_proposal": (
            "Publish NBB PDF assets/debt/cash FOI; disclose dienstencheque federal/regional "
            "subsidy matrix behind omzet 9.36m; reconcile PROFIT FLIP + equity JUMP +57% with "
            "FTE JUMP; 8-VE cost allocation"
        ),
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium CW; FOI {GAP}; stall Heropbeuring CW opaque / FARO YE2024 / "
            "AIESH YE2024 / REW YE2024; AGB Bornem JR2024; after De Vleugels@2231; deferred "
            "FREE Travie/Rucher; next every-10 2240"
        ),
    },
)
write_csv("leaderboard.csv", l_fields, leaderboard)

f_fields, foi = read_csv("foi_queue.csv")
upsert(
    foi,
    "gap_id",
    GAP,
    {
        "gap_id": GAP,
        "hierarchy_path": (
            "Vlaanderen>Limburg>SintTruiden>SDB>NBB_PDF_assets_debt_pnl_profit_flip_dienstencheque"
        ),
        "entity_id": ENTITY,
        "what_is_missing": (
            f"NBB PDF jaarrekening YE2025 full (assets/debt LT-ST/cash); pnl PROFIT FLIP "
            f"EUR{PN25} vs YE2024 LOSS EUR{PN24}; equity JUMP EUR{EQ25} (+57.36%) drivers; "
            f"federal/regional dienstencheque subsidy matrix behind omzet EUR{OM25}; "
            f"8 VE cost allocation; FTE JUMP {FTE25} vs {FTE24} recon"
        ),
        "why_it_matters": (
            f"Medium CW shows Limburg social dienstencheque VZW (omzet 9.36m / {FTE25} FTE / "
            "8 VE) with pnl PROFIT FLIP and equity JUMP +57% under public service-voucher path; "
            "assets/debt unpublished"
        ),
        "priority": "8",
        "recipient_body": "SDB VZW / Sociaal Dienstenchequebedrijf",
        "recipient_email": "info@vzw-sdbe.be",
        "recipient_postal": "Diesterstraat 27/11, 3800 Sint-Truiden",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-26",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; ready NOT sent; Medium CW + Strong KBO; preferred stall FARO/AIESH/"
            "REW YE2024; AGB Bornem JR2024; Heropbeuring CW opaque; deferred Travie/Rucher; "
            "next every-10 2240"
        ),
    },
)
write_csv("foi_queue.csv", f_fields, foi)

FOI_DRAFTS.mkdir(parents=True, exist_ok=True)
(FOI_DRAFTS / f"{GAP}.md").write_text(
    f"""# FOI draft — SDB (NBB PDF / pnl PROFIT FLIP / equity JUMP +57% / dienstencheque)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** SDB VZW / Sociaal Dienstenchequebedrijf — KBO **0665.861.844** (Actief; Diesterstraat 27/11, 3800 Sint-Truiden; **8 VE**; FTE {FTE25} CW; NACE **88.999**)  
**recipient:** info@vzw-sdbe.be · Diesterstraat 27/11, 3800 Sint-Truiden  
**sources:** [CW EN](https://www.companyweb.be/en/0665861844/sdb) · [CW NL](https://www.companyweb.be/nl/0665861844/sdb) · [CW FR](https://www.companyweb.be/fr/0665861844/sdb) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0665861844) · [site](http://www.vzw-sdb.be)  
**tick:** {TICK}  
**confidence:** Medium (Strong KBO + Medium CW YE2025; assets/debt Unknown)

## Context
- KBO Strong: Actief VZW; **8 VE**; zetel Diesterstraat 27/11 Sint-Truiden; NACE **88.999**; info@vzw-sdbe.be; www.vzw-sdb.be.
- CW YE2025: omzet **EUR{OM25:,}** JUMP +15.07% vs YE2024 EUR{OM24:,}; bruto **EUR{BR25:,}** JUMP +23.09%; pnl **EUR{PN25:,}** PROFIT FLIP vs YE2024 LOSS EUR{PN24:,}; equity **EUR{EQ25:,}** JUMP +57.36%; FTE **{FTE25}**; filed **28.04.2026**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW opaque. Deferred FREE: Travie / Le Rucher YE2025.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: SDB VZW / Sociaal Dienstenchequebedrijf
via info@vzw-sdbe.be
Diesterstraat 27/11, 3800 Sint-Truiden
Betreft: Openbaarmaking jaarrekening 2025 SDB (KBO 0665.861.844)

Geachte,

Op grond van het Bestuursdecreet / openbaarheid van bestuur vraag ik openbaarmaking van:

1. NBB/CBSO jaarrekening YE2025 PDF (balans + resultaten + toelichting; assets/debt/cash).
2. PnL PROFIT FLIP EUR{PN25} vs YE2024 verlies EUR{PN24} — reconciliatie met omzet JUMP +15% en FTE JUMP naar {FTE25}.
3. Eigen vermogen JUMP EUR{EQ25} (+57,36%) — drivers.
4. Federale/regionale dienstencheque-subsidiematrix achter omzet EUR{OM25}.
5. Per-VE cost allocation (8 VE).

Periode YE2025 (+ YE2024 comparative). Ref: {GAP}

Met vriendelijke groeten,
[Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

r_fields, rq = read_csv("research_queue.csv")
upsert(
    rq,
    "task_id",
    "rq_2232",
    {
        "task_id": "rq_2232",
        "title": (
            "leftover dual — SDB YE2025 Medium (omzet JUMP 9.36m / pnl PROFIT FLIP / "
            "equity JUMP +57%)"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "done",
        "hierarchy_target": "L5",
        "entity_id": ENTITY,
        "instructions": (
            "leftover dual after De Vleugels; prefer AGB/FARO/AIESH/REW else named FREE SDB"
        ),
        "blocked_gap_id": GAP,
        "created_utc": "2026-08-26T22:45:00Z",
        "updated_utc": UTC,
        "notes": (
            f"tick{TICK}; SDB 0665.861.844 YE2025 Medium CW; omzet JUMP {OM25} bruto JUMP "
            f"{BR25} pnl PROFIT FLIP {PN25} equity JUMP {EQ25} (+57.36%) FTE JUMP {FTE25}; "
            "8 VE Sint-Truiden; AGB Bornem JR2024; FARO/AIESH/REW YE2024; Heropbeuring CW "
            "opaque; deferred FREE Travie/Rucher; next rq_2233; every-10 next 2240"
        ),
    },
)
upsert(
    rq,
    "task_id",
    "rq_2233",
    {
        "task_id": "rq_2233",
        "title": (
            "leftover dual hole-fill after SDB — prefer AGB/FARO-YE2025/AIESH-REW/"
            "Heropbeuring-or-Travie-Rucher-unused"
        ),
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "leftover dual after SDB Sint-Truiden YE2025 Medium (omzet JUMP 9.36m / pnl "
            "PROFIT FLIP / equity JUMP +57%). Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else Heropbeuring if "
            "NBB/CW euros live, else named FREE Travie (0420.015.938 YE2025 pnl DROP -89% / "
            "bruto≫omzet ~2.84x) / Le Rucher (0860.345.458 YE2025 LOSS FLIP) / unused "
            "maatwerk/kringloop/WZC/IGS/HVZ. Do NOT redo SDB, De Vleugels, Kiemkracht, "
            "De Oever, ViTeS BE, Kringwinkel Midwest, ViTeS, Reset, Den Azalee, Kringwinkel "
            "West, Manus BXL, Manus VZW groep, Manus Antwerpen, Kringwinkel Maasland, "
            "Kringwinkel ZOV, NBSW, Opnieuw & Co, Veerkracht 4, Werkmmaat, Constructief, "
            "Kringloopwinkel Deltagroep, Groep Maatwerk, OptimaT, Huize Tordale, Odas, Ecoso, "
            "Werkhuizen Min, ACG, Noordheuvel, Arcor, Kemphaan, Entiris, Oesterbank, "
            "Werkplus, Trianval, Ijsedal, De Kromme Boom, Aarova, Kaliber, MWP Pajottenland, "
            "De Winning, Atelier Groot Eiland, Groep Talent, BosKat, De Schakel, BWZ, Bewel, "
            "Forena, Kunnig, A-kwadraat, SW-WEB, Mivas, Demival, De Wroeter, Kringwinkel "
            "Antwerpen, Blankedale, Mirto, Mariasteen, De Brug, Weerwerk, InterWest, "
            "Westlandia, BWB, Wase, Groep INTRO, MAAAT, WAAK SW, Waak, Stijn, Stroom, "
            "Springplank, Creat CV, Farys Solar, Senes, Orpimmo, Langerheide, Cur@-Z, "
            "Het Dorp, De Vlietoever, NLZ, Mobiel, Vlotter (YE2024), Aralea (YE2024), IPFBW, "
            "Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
            "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, "
            "Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. Next EVERY-10: 2240."
        ),
        "blocked_gap_id": "",
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": (
            "spawned after tick2232 SDB; FARO/AIESH/REW YE2024; AGB Bornem JR2024; "
            "Heropbeuring CW opaque; named FREE Travie/Rucher YE2025"
        ),
    },
)
write_csv("research_queue.csv", r_fields, rq)

ls_fields, ls = read_csv("loop_state.csv")
ls[0] = {
    "state_id": "main",
    "mode": "continuous",
    "current_sprint": "hole_fill",
    "last_tick_utc": UTC,
    "last_unit_id": "rq_2232",
    "ticks_completed": "2232",
    "paused": "no",
    "notes": (
        f"tick2232 leftover SDB 0665.861.844 Medium (omzet JUMP {OM25}; bruto JUMP {BR25}; "
        f"pnl PROFIT FLIP {PN25}; equity JUMP {EQ25} +57.36%; FTE JUMP {FTE25}; 8 VE "
        "Sint-Truiden); after De Vleugels@2231; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
        "Heropbeuring CW opaque; deferred Travie/Rucher; next rq_2233; next every-10 2240; "
        "continuous hole_fill"
    ),
}
write_csv("loop_state.csv", ls_fields, ls)

log_block = f"""

## Tick 2232 - 2026-08-26T23:05:00Z - rq_2232 SDB Sint-Truiden (omzet JUMP 9.36m / pnl PROFIT FLIP / equity JUMP +57% / Medium)

- Unit: **rq_2232** leftover dual after **rq_2231 De Vleugels**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**; Heropbeuring still **CW opaque**. Took named FREE leftover **SDB VZW / Sociaal Dienstenchequebedrijf** YE2025 (KBO **0665.861.844**; Diesterstraat 27/11 Sint-Truiden; **Actief** **8 VE**; NACE **88.999**) — named prefer in rq_2232. Deferred FREE **Travie** / **Le Rucher** YE2025. Do not redo De Vleugels/Kiemkracht/De Oever/ViTeS stack.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OM25}** JUMP +15.07% vs YE2024 EUR{OM24}; bruto **EUR{BR25}** JUMP +23.09%; pnl **EUR{PN25}** PROFIT FLIP vs YE2024 LOSS EUR{PN24}; equity **EUR{EQ25}** JUMP +57.36%; FTE **{FTE25}** JUMP vs {FTE24}; neerlegging **28.04.2026**. Strong KBO Actief 8 VE; info@vzw-sdbe.be. Assets/debt Unknown. Medium. FOI via info@vzw-sdbe.be.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1 pi 6.20); entities (+1 vzw_sdb_sint_truiden); foi + draft {GAP}; rq_2232=done + rq_2233 open; loop_state ticks=2232; raw docs/doge/raw/tick2232/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2230**; next **2240**). Next: rq_2233 (AGB/FARO-if-YE2025 / AIESH-REW / Travie-Rucher-or-unused).
"""
with LOG.open("a", encoding="utf-8") as f:
    f.write(log_block)

print(
    f"OK tick2232 SDB omzet={OM25} bruto={BR25} pnl={PN25} equity={EQ25} FTE={FTE25}"
)
