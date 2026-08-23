# tick 1961 — IGRETEC YE2025 Medium CW (rq_1961 after Aquiris EVERY-10)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T17:15:00Z"
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
        "source_id": "src_igretec_jr2025_cw",
        "title": "Companyweb IGRETEC YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0201741786/intercommunale-pour-la-gestion-et-la-realisation-d-etudes-techniques-et-economiques",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1961; Laatste balansjaar 2025; neergelegd 18-07-2026; "
            "omzet 105706740 JUMP +48.37pct; pnl DROP 7409365 -27.07pct; "
            "equity 267378265 -0.43pct; bruto 51746245; FTE 387.6; "
            "Groot; KBO 0201.741.786; assets/debt Unknown (Upswitch 404)"
        ),
    },
    {
        "source_id": "src_igretec_jr2025_cw_en",
        "title": "Companyweb EN twin IGRETEC YE2025 turnover equity",
        "url": "https://www.companyweb.be/en/0201741786/intercommunale-pour-la-gestion-et-la-realisation-d-etudes-techniques-et-economiques",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1961; Last balance sheet year 2025; Turnover 105706740; "
            "Profit/Loss 7409365; Equity 267378265; Gross margin 51746245; "
            "FTE 387.6; filed 18-07-2026"
        ),
    },
    {
        "source_id": "src_igretec_kbo_1961",
        "title": "KBO IGRETEC 0201.741.786 Actief SC Charleroi",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0201741786",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1961; Actief SC sinds 17.12.2020; zetel Boulevard Pierre Mayence 1 bus 1 "
            "6000 Charleroi; email officiel.ic-igretec@igretec.com; "
            "NBB consult https://consult.cbso.nbb.be/consult-enterprise/0201741786"
        ),
    },
    {
        "source_id": "src_igretec_site_1961",
        "title": "IGRETEC.com Walloon multi-sector intercommunale Charleroi",
        "url": "https://www.igretec.com/",
        "publisher": "IGRETEC SC",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": (
            "tick1961; bureau d'etudes + sanitation OAA + economic/airport real-estate "
            "sectors; dual SPGE/IDEA/BSCA; public site RF still 2024-only this tick"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1961 YE2025 Medium CW NL+EN + Strong KBO 0201.741.786 Actief SC; "
    "omzet JUMP 105.71m pnl DROP 7.41m equity 267.38m bruto 51.75m FTE 387.6; "
    "assets/debt Unknown (Upswitch 404); neerlegging 18.07.2026; "
    "multi-sector Charleroi-Sud Hainaut (etudes/assain/eco/airport dual BSCA); "
    "FOI gap_igretec_nbb_pdf_assets_debt_sector_matrix_l5; "
    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
    "do not redo Aquiris/SPGE/Hydria/Vivaqua/CILE/IRE*/FANC/SCK/EURIDICE/BRUGEL/"
    "Belgoprocess/Laborelec/NIRAS/Bel V/Dijk92/SOWAER"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if "igretec" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "igretec",
                "name_nl": "IGRETEC (Intercommunale studies/sanitatie/economie Charleroi)",
                "name_fr": "IGRETEC (Intercommunale etudes/assainissement/economie Charleroi)",
                "name_en": "IGRETEC (Charleroi multi-sector intercommunale)",
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.igretec.com",
                "foi_email": "officiel.ic-igretec@igretec.com",
                "foi_postal": "Boulevard Pierre Mayence 1 bus 1 6000 Charleroi",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "igretec": {
                "notes": ent_notes,
                "foi_email": "officiel.ic-igretec@igretec.com",
                "foi_postal": "Boulevard Pierre Mayence 1 bus 1 6000 Charleroi",
                "website": "https://www.igretec.com",
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_igretec_omzet_jr2025_statutory",
        "entity_id": "igretec",
        "year": "2025",
        "amount_eur": "105706740",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_igretec_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 omzet 105706740 JUMP +48.37pct vs 71245723",
    },
    {
        "budget_id": "bud_igretec_pnl_jr2025_statutory",
        "entity_id": "igretec",
        "year": "2025",
        "amount_eur": "7409365",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived Winst/Verlies",
        "source_id": "src_igretec_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 pnl DROP 7409365 -27.07pct vs 10160099",
    },
    {
        "budget_id": "bud_igretec_bruto_jr2025_statutory",
        "entity_id": "igretec",
        "year": "2025",
        "amount_eur": "51746245",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto/gross margin",
        "source_id": "src_igretec_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 bruto 51746245 +3.54pct vs 49977882",
    },
    {
        "budget_id": "bud_igretec_equity_jr2025_statutory",
        "entity_id": "igretec",
        "year": "2025",
        "amount_eur": "267378265",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived equity",
        "source_id": "src_igretec_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 equity 267378265 -0.43pct vs 268524099",
    },
    {
        "budget_id": "bud_igretec_fte_jr2025_statutory",
        "entity_id": "igretec",
        "year": "2025",
        "amount_eur": "387.6",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_igretec_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 FTE 387.6 vs 380.3 YE2024",
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
    "commitment_id": "comm_igretec_jr2025_statutory_omzet",
    "title": (
        "IGRETEC YE2025 leftover Walloon multi-sector dual statutory "
        "(omzet JUMP 105.71m / pnl DROP 7.41m / equity 267.38m)"
    ),
    "entity_id": "igretec",
    "beneficiary": "Charleroi-Sud Hainaut communes / SPGE OAA / BSCA airport dual path",
    "legal_basis": (
        "SC association de communes CDLD; NBB neerlegging; "
        "decret wallon openbaarheid / Code de la democratie locale"
    ),
    "decision_date": "2026-07-18",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "105706740",
    "cash_by_year": (
        "2025:omzet=105706740;bruto=51746245;pnl=7409365;"
        "equity=267378265;fte=387.6;assets=Unknown;debt=Unknown"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": (
        "https://www.companyweb.be/nl/0201741786/"
        "intercommunale-pour-la-gestion-et-la-realisation-d-etudes-techniques-et-economiques"
    ),
    "stated_goal": (
        "Multi-sector intercommunale: engineering bureau + sanitation OAA + "
        "economic/airport real-estate development"
    ),
    "cut_option": (
        "FOI NBB PDF + assets/debt + per-sector P&L matrix + dual unit-cost vs SPGE/IDEA"
    ),
    "source_id": "src_igretec_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>IGRETEC>JR2025_statutory_L5",
    "notes": (
        "tick1961; Medium CW NL+EN after Aquiris EVERY-10; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo Aquiris/SPGE/Hydria/Vivaqua/"
        "CILE/IRE/FANC/SCK/EURIDICE/BRUGEL/Belgoprocess/SOWAER; not TE-additive of 348bn"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_igretec_omzet_jump_105_71m_pnl_drop_7_41m_jr2025",
    "name": (
        "IGRETEC omzet JUMP 105.71m / pnl DROP 7.41m / equity 267.38m "
        "(multi-sector Charleroi YE2025)"
    ),
    "level": "L5",
    "type": "walloon_intercommunale_multi_sector_dual",
    "hierarchy_path": "Wallonie>Hainaut>IGRETEC>JR2025_statutory_L5",
    "annual_cost_eur": "105706740",
    "total_cost_eur": "267378265",
    "tco_notes": (
        "statutory omzet 105706740 JUMP bruto 51746245 pnl DROP 7409365 "
        "equity 267378265 fte 387.6; assets/debt Unknown; dual SPGE/IDEA/BSCA"
    ),
    "confidence": "medium",
    "source_id": "src_igretec_jr2025_cw",
    "beneficiaries": "Charleroi-Sud Hainaut communes / SPGE OAA / BSCA airport zone",
    "stated_goal": "Engineering + sanitation + economic/airport development intercommunale",
    "measured_outcome": (
        "CW NL+EN YE2025 live unused after preferred AGB/FARO/AIESH/REW stall; "
        "omzet JUMP +48pct with pnl DROP -27pct; primary NBB PDF + BS + sector matrix unresolved"
    ),
    "absurdity_score": "4.5",
    "cost_score": "7.0",
    "difficulty": "3.5",
    "priority_index": "5.8",
    "cut_proposal": (
        "Publish NBB PDF + assets/debt + per-sector P&L/dividend matrix; "
        "reconcile turnover JUMP vs declining profit"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1961; Medium CW; leftover unused IGS/water dual after Aquiris; "
        "not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_igretec_nbb_pdf_assets_debt_sector_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Wallonie>Hainaut>IGRETEC>nbb_pdf_assets_debt_sector_L5",
    "entity_id": "igretec",
    "what_is_missing": (
        "NBB deposit PDF body YE2025 (CW neerlegging 18.07.2026); "
        "assets / debt LT-ST / cash exact (Upswitch 404); "
        "per-sector P&L / dividend / SPGE works matrix 2025 vs omzet JUMP 105.71m; "
        "reconcile pnl DROP -27pct with turnover JUMP +48pct; "
        "BSCA airport real-estate sector flows"
    ),
    "why_it_matters": (
        "Large Walloon multi-sector intercommunale: 105.71m omzet JUMP / 267m equity "
        "with opaque BS and multi-sector fee stack (SPGE OAA + airport dual) — "
        "public euro opacity without NBB PDF"
    ),
    "priority": "8",
    "recipient_body": "IGRETEC SC (cc SPW / SPGE / communes associees)",
    "recipient_email": "officiel.ic-igretec@igretec.com",
    "recipient_postal": "Boulevard Pierre Mayence 1 bus 1 6000 Charleroi",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_igretec_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_igretec_omzet_jump_105_71m_pnl_drop_7_41m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1961; human-send only; Medium CW; next every-10 1970",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — IGRETEC (NBB PDF / assets-debt / sector matrix)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** IGRETEC SC — KBO **0201.741.786** (Charleroi multi-sector intercommunale)  
**recipient:** officiel.ic-igretec@igretec.com / cc SPW / SPGE / communes associees  
**sources:** [Companyweb NL](https://www.companyweb.be/nl/0201741786/intercommunale-pour-la-gestion-et-la-realisation-d-etudes-techniques-et-economiques) · [Companyweb EN](https://www.companyweb.be/en/0201741786/intercommunale-pour-la-gestion-et-la-realisation-d-etudes-techniques-et-economiques) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0201741786) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0201741786) · [igretec.com](https://www.igretec.com/)  
**tick:** 1961  
**confidence on table euros:** Medium (NBB-derived CW NL+EN; primary deposit PDF unresolved; Upswitch 404 for assets)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **18.07.2026**): omzet **EUR105,706,740** (**JUMP +48.37%**); bruto **EUR51,746,245**; pnl **EUR7,409,365** (**DROP -27.07%**); equity **EUR267,378,265**; FTE **387.6**.
- Assets / debt / cash **Unknown** (Upswitch SPA empty this tick — not invented).
- Multi-sector dual: engineering bureau + sanitation OAA (SPGE path) + economic/airport real-estate (BSCA dual). Official RF site still **2024-only**.
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo Aquiris / SPGE / Hydria / Vivaqua / CILE / IRE cluster / BRUGEL / SOWAER.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: IGRETEC SC
t.a.v. openbaarheid / information officer
Boulevard Pierre Mayence 1 bus 1
6000 Charleroi

cc: SPW / SPGE — Rue des Ecoles 17-19, 4800 Verviers
    Communes associees IGRETEC Secteurs 1-4

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025 IGRETEC,
balansposten en sector-P&L/dividend-matrix (KBO 0201.741.786)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / CDLD)
vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   van IGRETEC SC (deposit-/referentienummer + PDF; Companyweb noemt
   neerlegging 18.07.2026).
2. Balanstotaal / schulden LT-ST / cash reconcilieerbaar met publieke
   aggregators (CW omzet EUR105.706.740; equity EUR267.378.265;
   assets YE2025 Unknown).
3. Per-sector P&L / dividend / SPGE-werken matrix 2025 (Secteurs 1-4)
   vs statutaire omzet JUMP +48%.
4. Uitleg pnl DROP -27% bij omzet JUMP +48% + eventuele dividend-
   / related-party flows (incl. BSCA airport real-estate sector).
5. Dual unit-cost vs SPGE / IDEA OAA-pad indien beschikbaar.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (IGRETEC SC + SPGE/SPW cc)
- [x] Concrete documenten (NBB PDF / BS / sector matrix)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; took unused leftover **IGRETEC** YE2025 live.
""",
        encoding="utf-8",
    )

# research_queue: close rq_1961, spawn rq_1962
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

have_1962 = False
for row in rq_rows:
    if row.get("task_id") == "rq_1961":
        row["status"] = "done"
        row["entity_id"] = "igretec"
        row["title"] = (
            "leftover dual hole-fill after Aquiris EVERY-10 — IGRETEC YE2025 Medium"
        )
        row["updated_utc"] = TS
        row["notes"] = (
            "tick1961 IGRETEC YE2025 Medium omzet JUMP 105.71m pnl DROP 7.41m "
            "equity 267.38m; FOI ready; next rq_1962; next every-10 1970"
        )
        row["instructions"] = (
            "Completed: IGRETEC leftover Walloon multi-sector dual after Aquiris EVERY-10; "
            "KBO 0201.741.786; YE2025 Medium CW NL+EN (omzet JUMP 105.71m pnl DROP 7.41m "
            "equity 267.38m bruto 51.75m FTE 387.6); FOI "
            "gap_igretec_nbb_pdf_assets_debt_sector_matrix_l5 ready"
        )
    if row.get("task_id") == "rq_1962":
        have_1962 = True

if not have_1962:
    rq_rows.append(
        {
            "task_id": "rq_1962",
            "title": "leftover dual hole-fill after IGRETEC",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1962 after 1961 IGRETEC YE2025 statutory. Prefer leftover AGB/APB "
                "if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/nuclear. Do NOT redo IGRETEC, Aquiris, "
                "SPGE, IRE parent, IRE ELiT, FANC, SCK CEN, EURIDICE, BRUGEL, Hydria, Vivaqua, "
                "Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synatom, Atrias, AIEG, "
                "Synergrid, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, SOWAER."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1961; next every-10 1970",
        }
    )

with (DATA / "research_queue.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rq_rows)

update_csv_rows(
    DATA / "loop_state.csv",
    "state_id",
    {
        "main": {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1961",
            "ticks_completed": "1961",
            "paused": "no",
            "notes": (
                "tick1961 IGRETEC 0201.741.786 Medium CW NL+EN (omzet JUMP 105.71m "
                "pnl DROP 7.41m equity 267.38m bruto 51.75m FTE 387.6); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1962; "
                "next every-10 1970; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = """
## Tick 1961 - 2026-08-23T17:15:00Z - rq_1961 IGRETEC (omzet JUMP 105.71m / pnl DROP 7.41m / Medium)

- Unit: **rq_1961** leftover dual after **rq_1960 EVERY-10 + Aquiris**. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **IGRETEC** YE2025 (KBO **0201.741.786**; Boulevard Pierre Mayence 1 Charleroi; Walloon multi-sector intercommunale etudes/assain/eco/airport; **SPGE/IDEA/BSCA dual**). Do not redo Aquiris/SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/SOWAER.
- Found: Companyweb NL+EN YE2025 - omzet **EUR105,706,740** JUMP +48.37%; bruto **EUR51,746,245**; pnl **EUR7,409,365** DROP -27.07%; equity **EUR267,378,265**; FTE **387.6**; neerlegging **18.07.2026**. Assets/debt Unknown (Upswitch 404). Official RF site still 2024-only. Medium confidence.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igretec); foi + draft gap_igretec_nbb_pdf_assets_debt_sector_matrix_l5; rq_1961=done + rq_1962 open; loop_state ticks=1961.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1970**). Next: rq_1962 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1961 write OK: IGRETEC omzet", 105706740, "pnl", 7409365)
