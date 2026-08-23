# tick 1962 — Gabrielle Passelecq YE2025 Medium CW+Upswitch (rq_1962 after IPFBW/IGRETEC)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T17:45:00Z"
csv.field_size_limit(10**7)


def append_csv(path, rows):
    with path.open("a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        for r in rows:
            w.writerow(r)


def update_csv_rows(path, key, updates_by_key):
    with path.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        rows = list(r)
    for row in rows:
        k = row[key]
        if k in updates_by_key:
            row.update(updates_by_key[k])
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


existing_src = set()
with (DATA / "sources.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_src.add(row.get("source_id") or "")

sources_new = [
    {
        "source_id": "src_passelecq_jr2025_cw",
        "title": "Companyweb Gabrielle Passelecq YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0440868364/intercommunale-gabrielle-passelecq",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1962; Laatste balansjaar 2025; neergelegd 07-07-2026; "
            "omzet 77724985 +3.11pct; pnl JUMP 3265483 +36.82pct; "
            "equity 61314893 +8.24pct; bruto 120260142; FTE 1297; Groot; "
            "KBO 0440.868.364"
        ),
    },
    {
        "source_id": "src_passelecq_jr2025_cw_en",
        "title": "Companyweb EN twin Gabrielle Passelecq YE2025 turnover equity",
        "url": "https://www.companyweb.be/en/0440868364/intercommunale-gabrielle-passelecq",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1962; Last balance sheet year 2025; Turnover 77724985; "
            "Profit/Loss 3265483; Equity 61314893; Gross margin 120260142; "
            "FTE 1297; filed 07-07-2026"
        ),
    },
    {
        "source_id": "src_passelecq_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO Gabrielle Passelecq YE2025 assets EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/intercommunale-gabrielle-passelecq-0440868364",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1962; YE2025 assets 139220560; equity 61314893; revenue 77724985; "
            "EBITDA 7547480; operating 3490688; DA 4056792; equity~44pct BS; "
            "archive 2026-06-30"
        ),
    },
    {
        "source_id": "src_passelecq_kbo_1962",
        "title": "KBO Gabrielle Passelecq 0440.868.364 Actief SC Mons",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0440868364",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1962; Actief SC sinds 31.01.1990; zetel Chemin du Chene aux Haies 24 "
            "7000 Mons; email officiel.ic-chupmb@chupmb.be; aanbestedende overheid; "
            "NACE 86.101 ziekenhuis; NBB consult https://consult.cbso.nbb.be/consult-enterprise/0440868364; "
            "dual HELORA / ex CHU Ambroise Pare path"
        ),
    },
    {
        "source_id": "src_passelecq_mons_ag_jr2025",
        "title": "Mons AG publiable comptes BNB 2025 Gabrielle Passelecq",
        "url": "https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/gabrielle-passelecq/gabrielle-passelecq-1/ag-du-25-juin-2026/publiable-ago-2026-06-comptes-bnb-2025.pdf",
        "publisher": "Ville de Mons / Intercommunale Gabrielle Passelecq",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": (
            "tick1962; AG 25.06.2026 publiable; bilan 139220560.29; equity 61314892; "
            "consolidated net 3265482.77; sectors A +2.24m B +4.26m C -3.24m D 0; "
            "matches CW/Upswitch assets+pnl"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1962 YE2025 Medium CW NL+EN + Upswitch + Strong KBO 0440.868.364 Actief SC; "
    "omzet JUMP 77.72m pnl JUMP 3.27m equity JUMP 61.31m bruto 120.26m assets 139.22m "
    "EBITDA 7.55m FTE 1297; debt Unknown (provisions not invented); neerlegging 07.07.2026; "
    "Mons hospital IGS dual HELORA / mental-health / non-hospital sectors; "
    "FOI gap_passelecq_nbb_pdf_debt_helora_sector_matrix_l5; "
    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
    "do not redo IPFBW/IGRETEC/Aquiris/SPGE/Hydria/Vivaqua/CILE/IRE*/FANC/SCK/"
    "EURIDICE/BRUGEL/Belgoprocess/Laborelec/NIRAS/Bel V/Dijk92/AIEG/Synergrid"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if "igs_passelecq" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "igs_passelecq",
                "name_nl": "Intercommunale Gabrielle Passelecq (Mons ziekenhuis-IGS / HELORA dual)",
                "name_fr": "Intercommunale Gabrielle Passelecq (hopital Mons / dual HELORA)",
                "name_en": "Gabrielle Passelecq intercommunale (Mons hospital IGS / HELORA dual)",
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.helora.be/",
                "foi_email": "officiel.ic-chupmb@chupmb.be",
                "foi_postal": "Chemin du Chene aux Haies 24 7000 Mons",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "igs_passelecq": {
                "notes": ent_notes,
                "foi_email": "officiel.ic-chupmb@chupmb.be",
                "foi_postal": "Chemin du Chene aux Haies 24 7000 Mons",
                "website": "https://www.helora.be/",
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_passelecq_omzet_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "77724985",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Upswitch NBB-derived omzet statutory",
        "source_id": "src_passelecq_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1962; YE2025 omzet 77724985 JUMP +3.11pct vs 75379321",
    },
    {
        "budget_id": "bud_passelecq_pnl_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "3265483",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived Winst/Verlies (+ Mons AG PDF match)",
        "source_id": "src_passelecq_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1962; YE2025 pnl JUMP 3265483 +36.82pct vs 2386772; Mons AG 3265482.77",
    },
    {
        "budget_id": "bud_passelecq_bruto_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "120260142",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto/gross margin",
        "source_id": "src_passelecq_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1962; YE2025 bruto 120260142 +3.21pct vs 116521604",
    },
    {
        "budget_id": "bud_passelecq_equity_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "61314893",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Upswitch+Mons AG equity",
        "source_id": "src_passelecq_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1962; YE2025 equity 61314893 JUMP +8.24pct; Mons AG 61314892",
    },
    {
        "budget_id": "bud_passelecq_assets_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "139220560",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB/CBSO + Mons AG bilan total",
        "source_id": "src_passelecq_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1962; YE2025 assets 139220560; Mons AG 139220560.29; YE2024 138832142",
    },
    {
        "budget_id": "bud_passelecq_ebitda_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "7547480",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived EBITDA",
        "source_id": "src_passelecq_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1962; YE2025 EBITDA 7547480 vs 6581402 YE2024; operating 3490688",
    },
    {
        "budget_id": "bud_passelecq_fte_jr2025_statutory",
        "entity_id": "igs_passelecq",
        "year": "2025",
        "amount_eur": "1297",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_passelecq_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1962; YE2025 FTE 1297 vs 1285 YE2024 (down from 2466 YE2022 HELORA path)",
    },
]
budgets_new = [b for b in budgets_new if b["budget_id"] not in existing_bud]
if budgets_new:
    append_csv(DATA / "budgets.csv", budgets_new)

existing_comm = set()
with (DATA / "commitments.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_comm.add(row.get("commitment_id") or "")

comm_row = {
    "commitment_id": "comm_passelecq_jr2025_statutory_omzet",
    "title": (
        "Gabrielle Passelecq YE2025 leftover Mons hospital IGS dual statutory "
        "(omzet JUMP 77.72m / pnl JUMP 3.27m / assets 139.22m)"
    ),
    "entity_id": "igs_passelecq",
    "beneficiary": "Mons/HELORA hospital patients + mental-health / non-hospital sectors",
    "legal_basis": (
        "SC association de communes CDLD; NBB neerlegging; "
        "decret wallon openbaarheid / Code de la democratie locale"
    ),
    "decision_date": "2026-07-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "77724985",
    "cash_by_year": (
        "2025:omzet=77724985;bruto=120260142;pnl=3265483;equity=61314893;"
        "assets=139220560;ebitda=7547480;fte=1297;debt=Unknown"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0440868364/intercommunale-gabrielle-passelecq",
    "stated_goal": (
        "Hospital intercommunale Mons: general hospital + mental health + "
        "non-hospital / patrimoniale sectors (HELORA dual path)"
    ),
    "cut_option": (
        "FOI NBB PDF + debt LT-ST/cash + HELORA sector A/B/C/D recon + "
        "staffing path vs YE2022 2466 FTE"
    ),
    "source_id": "src_passelecq_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>Mons>Gabrielle_Passelecq>JR2025_statutory_L5",
    "notes": (
        "tick1962; Medium CW+Upswitch+Mons AG after IPFBW/IGRETEC; preferred AGB Bornem "
        "JR2024 / FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo IPFBW/IGRETEC/"
        "Aquiris/SPGE/nuclear stack; not TE-additive of 348bn"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_passelecq_omzet_jump_77_72m_pnl_jump_3_27m_jr2025",
    "name": (
        "Gabrielle Passelecq omzet JUMP 77.72m / pnl JUMP 3.27m / assets 139.22m "
        "(Mons hospital IGS YE2025)"
    ),
    "level": "L5",
    "type": "walloon_hospital_igs_dual",
    "hierarchy_path": "Wallonie>Hainaut>Mons>Gabrielle_Passelecq>JR2025_statutory_L5",
    "annual_cost_eur": "77724985",
    "total_cost_eur": "139220560",
    "tco_notes": (
        "statutory omzet 77724985 JUMP bruto 120260142 pnl JUMP 3265483 "
        "equity 61314893 assets 139220560 ebitda 7547480 fte 1297; debt Unknown; "
        "HELORA dual sectors A/B/C"
    ),
    "confidence": "medium",
    "source_id": "src_passelecq_jr2025_cw",
    "beneficiaries": "Mons region patients / HELORA network / communes associees",
    "stated_goal": "Hospital + mental-health intercommunale Mons",
    "measured_outcome": (
        "CW+Upswitch+Mons AG YE2025 live unused after preferred AGB/FARO/AIESH/REW stall; "
        "pnl JUMP +37pct on flat-ish omzet; primary NBB PDF + debt/HELORA fee matrix unresolved"
    ),
    "absurdity_score": "4.0",
    "cost_score": "6.5",
    "difficulty": "3.5",
    "priority_index": "5.4",
    "cut_proposal": (
        "Publish NBB PDF + debt/cash + HELORA sector A/B/C/D P&L recon; "
        "explain FTE path 2466→1297 and sector C LOSS 3.24m"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1962; Medium CW+Upswitch; leftover unused hospital IGS after IPFBW; "
        "not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_passelecq_nbb_pdf_debt_helora_sector_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Wallonie>Hainaut>Mons>Gabrielle_Passelecq>nbb_pdf_debt_helora_L5",
    "entity_id": "igs_passelecq",
    "what_is_missing": (
        "NBB deposit PDF body YE2025 (CW neerlegging 07.07.2026); "
        "schulden LT-ST / cash / provisions exact (debt not invented from assets-equity); "
        "HELORA dual fee / staff transfer recon vs FTE path 2466→1297; "
        "sector A/B/C/D P&L matrix detail beyond Mons AG summary "
        "(A +2.24m B +4.26m C LOSS 3.24m D 0)"
    ),
    "why_it_matters": (
        "Large Mons hospital intercommunale: 77.72m omzet / 139.22m assets / 1297 FTE "
        "with opaque debt + HELORA dual sector stack — public euro opacity without NBB PDF"
    ),
    "priority": "8",
    "recipient_body": "Intercommunale Gabrielle Passelecq SC (cc Ville de Mons / HELORA)",
    "recipient_email": "officiel.ic-chupmb@chupmb.be",
    "recipient_postal": "Chemin du Chene aux Haies 24 7000 Mons",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_passelecq_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_passelecq_omzet_jump_77_72m_pnl_jump_3_27m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1962; human-send only; Medium CW+Upswitch; next every-10 1970",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — Gabrielle Passelecq (NBB PDF / debt / HELORA sector matrix)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** Intercommunale Gabrielle Passelecq SC — KBO **0440.868.364** (Mons hospital IGS / HELORA dual)  
**recipient:** officiel.ic-chupmb@chupmb.be / cc Ville de Mons / HELORA  
**sources:** [Companyweb NL](https://www.companyweb.be/nl/0440868364/intercommunale-gabrielle-passelecq) · [Companyweb EN](https://www.companyweb.be/en/0440868364/intercommunale-gabrielle-passelecq) · [Upswitch](https://www.upswitch.app/en/companies/be/intercommunale-gabrielle-passelecq-0440868364) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0440868364) · [Mons AG PDF](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/gabrielle-passelecq/gabrielle-passelecq-1/ag-du-25-juin-2026/publiable-ago-2026-06-comptes-bnb-2025.pdf) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0440868364)  
**tick:** 1962  
**confidence on table euros:** Medium (NBB-derived CW NL+EN + Upswitch; Mons AG confirms assets/pnl/equity; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **07.07.2026**): omzet **EUR77,724,985** (**JUMP +3.11%**); bruto **EUR120,260,142**; pnl **EUR3,265,483** (**JUMP +36.82%**); equity **EUR61,314,893**; assets **EUR139,220,560**; EBITDA **EUR7,547,480**; FTE **1297**.
- Debt / cash / provisions **Unknown** (not invented from assets−equity).
- Mons AG summary sectors: A **+EUR2.24m**; B mental health **+EUR4.26m**; C non-hospital **LOSS EUR3.24m**; D patrimoniale **0**.
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo IPFBW / IGRETEC / Aquiris / SPGE / nuclear stack / AIEG / Synergrid.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Intercommunale Gabrielle Passelecq SC
t.a.v. openbaarheid / information officer
Chemin du Chene aux Haies 24
7000 Mons

cc: Ville de Mons — College / HELORA network

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025 Gabrielle Passelecq,
schulden/cash en HELORA sector-P&L-matrix (KBO 0440.868.364)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / CDLD)
vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   van Intercommunale Gabrielle Passelecq SC (deposit-/referentienummer + PDF;
   Companyweb noemt neerlegging 07.07.2026).
2. Schulden LT-ST / cash / provisions reconcilieerbaar met publieke
   aggregators (CW/Upswitch omzet EUR77.724.985; assets EUR139.220.560;
   equity EUR61.314.893; debt YE2025 Unknown).
3. HELORA dual fee / staff-transfer recon vs FTE-pad 2466 (2022) → 1297 (2025).
4. Detail sector A/B/C/D P&L 2025 voorbij Mons AG-samenvatting
   (A +2.24m; B +4.26m; C LOSS 3.24m; D 0) + eventuele related-party flows.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (Gabrielle Passelecq SC + Mons/HELORA cc)
- [x] Concrete documenten (NBB PDF / debt-cash / HELORA sector matrix)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; took unused leftover **Gabrielle Passelecq** hospital IGS YE2025 live.
""",
        encoding="utf-8",
    )

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1962": {
            "status": "done",
            "entity_id": "igs_passelecq",
            "updated_utc": TS,
            "notes": (
                "tick1962; Completed: Gabrielle Passelecq leftover Mons hospital IGS "
                "YE2025 Medium CW+Upswitch (omzet JUMP 77.72m / pnl JUMP 3.27m / "
                "assets 139.22m); preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                "FOI gap_passelecq_nbb_pdf_debt_helora_sector_matrix_l5 ready; "
                "next every-10 1970"
            ),
        }
    },
)

# ensure next open unit exists
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    rq_rows = list(csv.DictReader(f))
    rq_ids = {r.get("task_id") for r in rq_rows}

if "rq_1963" not in rq_ids:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1963",
                "title": "leftover dual hole-fill after Gabrielle Passelecq",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/nuclear. "
                    "Do NOT redo Gabrielle Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, "
                    "SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, "
                    "Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, "
                    "ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "tick1962; next after Passelecq; next every-10 1970",
            }
        ],
    )

update_csv_rows(
    DATA / "loop_state.csv",
    "state_id",
    {
        "main": {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1962",
            "ticks_completed": "1962",
            "paused": "no",
            "notes": (
                "tick1962 leftover Gabrielle Passelecq 0440.868.364 Medium CW+Upswitch "
                "(omzet JUMP 77.72m pnl JUMP 3.27m assets 139.22m equity 61.31m bruto 120.26m "
                "EBITDA 7.55m FTE 1297); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1963; next every-10 1970; continuous hole_fill"
            ),
        }
    },
)

print("tick1962 write OK")
