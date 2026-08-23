# tick 1965 — CENEO YE2025 Strong AG+CW (rq_1965 after CHU HELORA)
import csv
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T18:30:00Z"
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
        "source_id": "src_ceneo_jr2025_ag_mons",
        "title": "CENEO AG 29.06.2026 Rapport financier YE2025 (Mons publiable PDF)",
        "url": (
            "https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/ceneo-1/ceneo/"
            "ag-du-29-juin-2026/publiable-ceneo_rapport-financier_2025.pdf/@@download/file/"
            "Publiable%20-%20CENEO_Rapport-financier_2025.pdf"
        ),
        "publisher": "CENEO SC / Ville de Mons AG publiable",
        "accessed_date": "2026-08-23",
        "source_class": "primary_official",
        "notes": (
            "tick1965; Strong AG financial report + NBB schema section; "
            "pnl 41353730.07; assets 1171706286.70; debt 212067606.08 "
            "(LT 154505775.05 + ST 57123285.57); dividends received 45469560.23; "
            "ORES Assets VNC 792362510.24 (70.21pct); SOCOFE 309568103 (27.42pct); "
            "apport 327216388.22; reval 386496381.62; reserves 245918253.10; "
            "dividend to associates 24775000; local raw "
            "docs/doge/data/raw/ceneo_rapport_financier_2025.pdf"
        ),
    },
    {
        "source_id": "src_ceneo_jr2025_cw",
        "title": "Companyweb CENEO / IPFH YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0201645281/ceneo",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1965; Laatste balansjaar 2025; neergelegd 21-07-2026; "
            "pnl 41353730 DROP -2.9pct; omzet JUMP 954029 +90.64pct; "
            "equity 959638681 +1.76pct; bruto NEG -734655; FTE empty"
        ),
    },
    {
        "source_id": "src_ceneo_jr2025_cw_en",
        "title": "Companyweb EN twin CENEO YE2025 equity turnover",
        "url": "https://www.companyweb.be/en/0201645281/ceneo",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1965; Last balance sheet year 2025; Profit/Loss 41353730; "
            "Turnover 954029; Equity 959638681; Gross margin -734655; filed 21-07-2026"
        ),
    },
    {
        "source_id": "src_ceneo_kbo_1965",
        "title": "KBO CENEO / IPFH 0201.645.281 Actief SC Charleroi",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
            "ondernemingsnummer=0201645281"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1965; Actief SC sinds 01.01.1968; naam CENEO / afkorting IPFH; "
            "zetel Boulevard Pierre Mayence 1 bus 1 6000 Charleroi; "
            "email info@ceneo.be; tel 071 20 28 81; aanbestedende overheid; "
            "dagelijks bestuur IGRETEC 0201.741.786 / Raphael Durant; "
            "NBB consult https://consult.cbso.nbb.be/consult-enterprise/0201645281"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1965 YE2025 Strong AG Mons Rapport financier + CW NL+EN + Strong KBO "
    "0201.645.281 Actief SC (CENEO / IPFH); pnl DROP 41.354m assets 1.172bn "
    "equity JUMP 959.64m debt 212.07m omzet JUMP 0.954m bruto NEG; "
    "dividends received 45.470m (ORES Assets 32.436m / SOCOFE 11.149m); "
    "ORES Assets VNC 792.36m (70.21pct) SOCOFE 309.57m (27.42pct); "
    "dividend to associates 24.775m; neerlegging 21.07.2026; "
    "Walloon municipal energy holding dual ORES/Socofe/VEH + IGRETEC seat; "
    "FOI gap_ceneo_nbb_pdf_commune_dividend_matrix_l5; preferred AGB Bornem JR2024; "
    "FARO/AIESH/REW YE2024; do not redo HELORA/iMio/Passelecq/IGRETEC/IPFBW/"
    "Aquiris/SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/CILE"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if "ceneo" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "ceneo",
                "name_nl": "CENEO (Intercommunale energieholding Hainaut / ex-IPFH)",
                "name_fr": "CENEO (ex-IPFH Intercommunale de Participation et de Financement Hennuyere)",
                "name_en": "CENEO (Walloon Hainaut municipal energy holding IGS)",
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.ceneo.be",
                "foi_email": "info@ceneo.be",
                "foi_postal": "Boulevard Pierre Mayence 1/1 6000 Charleroi",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "ceneo": {
                "notes": ent_notes,
                "foi_email": "info@ceneo.be",
                "foi_postal": "Boulevard Pierre Mayence 1/1 6000 Charleroi",
                "website": "https://www.ceneo.be",
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_ceneo_pnl_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "41353730.07",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG Rapport financier + CW Winst/Verlies",
        "source_id": "src_ceneo_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1965; YE2025 pnl 41353730.07 DROP -2.9pct vs 42588575.32",
    },
    {
        "budget_id": "bud_ceneo_assets_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "1171706286.70",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG bilan total actif",
        "source_id": "src_ceneo_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1965; YE2025 assets 1171706286.70 vs 1168722606.42 YE2024",
    },
    {
        "budget_id": "bud_ceneo_equity_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "959638681",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW equity + AG apport/reval/reserves recon",
        "source_id": "src_ceneo_jr2025_cw",
        "confidence": "strong",
        "notes": "tick1965; YE2025 equity 959638681 JUMP +1.76pct; AG apport 327.2m reval 386.5m reserves 245.9m",
    },
    {
        "budget_id": "bud_ceneo_debt_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "212067606.08",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG dettes LT+ST",
        "source_id": "src_ceneo_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1965; YE2025 debt 212067606.08 (LT 154505775.05 + ST 57123285.57)",
    },
    {
        "budget_id": "bud_ceneo_dividends_recv_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "45469560.23",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG produits participations / dividends received",
        "source_id": "src_ceneo_jr2025_ag_mons",
        "confidence": "strong",
        "notes": (
            "tick1965; YE2025 dividends received 45469560.23 DROP -2.73pct "
            "(ORES Assets 32436437.49 / SOCOFE 11149407 / Engie 1860510.96)"
        ),
    },
    {
        "budget_id": "bud_ceneo_omzet_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "954029.31",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW omzet (holding CA; dividends off CA line)",
        "source_id": "src_ceneo_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1965; YE2025 omzet JUMP 954029.31 +90.64pct; not primary economic flow vs dividends 45.5m",
    },
    {
        "budget_id": "bud_ceneo_dividend_out_jr2025_statutory",
        "entity_id": "ceneo",
        "year": "2025",
        "amount_eur": "24775000",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG attribution aux associes",
        "source_id": "src_ceneo_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1965; YE2025 dividend to commune associates 24775000 per strategic plan",
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
    "commitment_id": "comm_ceneo_jr2025_statutory_assets",
    "title": (
        "CENEO YE2025 leftover Walloon energy-holding dual "
        "(assets 1.172bn / pnl DROP 41.35m / ORES+SOCOFE stake)"
    ),
    "entity_id": "ceneo",
    "beneficiary": "Hainaut communes / ORES Assets / SOCOFE / renewable SPVs",
    "legal_basis": (
        "SC association de communes CDLD; NBB neerlegging 21.07.2026; "
        "decret wallon openbaarheid / Code de la democratie locale"
    ),
    "decision_date": "2026-07-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1171706286.70",
    "cash_by_year": (
        "2025:assets=1171706286.70;pnl=41353730.07;equity=959638681;"
        "debt=212067606.08;div_recv=45469560.23;omzet=954029.31;"
        "div_out=24775000;ores_vnc=792362510.24;socofe_vnc=309568103;"
        "bruto=-734655"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.ceneo.be",
    "stated_goal": (
        "Municipal energy holding: ORES/SOCOFE stakes, renewables, "
        "energy-purchase centrale for Hainaut communes"
    ),
    "cut_option": (
        "FOI NBB deposit + commune dividend matrix + dual unit-cost vs "
        "ORES/Socofe/VEH; publish Engie RDV policy"
    ),
    "source_id": "src_ceneo_jr2025_ag_mons",
    "confidence": "strong",
    "hierarchy_path": "Wallonie>Hainaut>CENEO>JR2025_statutory_L5",
    "notes": (
        "tick1965; Strong AG+CW after HELORA; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo HELORA/iMio/"
        "Passelecq/IGRETEC/IPFBW/Aquiris/SPGE/nuclear/water stack; not TE-additive"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_ceneo_assets_1_17bn_pnl_41m_ores_socofe_jr2025",
    "name": (
        "CENEO assets 1.172bn / pnl DROP 41.35m / ORES+SOCOFE stake "
        "(Walloon energy holding YE2025)"
    ),
    "level": "L5",
    "type": "walloon_igs_energy_holding_dual",
    "hierarchy_path": "Wallonie>Hainaut>CENEO>JR2025_statutory_L5",
    "annual_cost_eur": "41353730.07",
    "total_cost_eur": "1171706286.70",
    "tco_notes": (
        "statutory assets 1.172bn pnl DROP 41.35m equity 959.6m debt 212.1m; "
        "div_recv 45.47m (ORES 32.4 / SOCOFE 11.1); div_out 24.78m; "
        "ORES Assets VNC 792.4m 70pct / SOCOFE 309.6m 27pct; dual VEH/Socofe path"
    ),
    "confidence": "strong",
    "source_id": "src_ceneo_jr2025_ag_mons",
    "beneficiaries": "Hainaut communes / ORES-SOCOFE dividend chain",
    "stated_goal": "Public municipal energy holding and renewables co-investment",
    "measured_outcome": (
        "Strong AG Mons YE2025 PDF live unused after preferred AGB/FARO/AIESH/REW stall; "
        "pnl DROP -2.9pct with ORES dividend covenant; commune dividend matrix unresolved"
    ),
    "absurdity_score": "4.0",
    "cost_score": "7.5",
    "difficulty": "3.0",
    "priority_index": "5.8",
    "cut_proposal": (
        "Publish NBB deposit + per-commune dividend/attribution matrix + "
        "ORES covenant impact + Engie RDV policy; dual unit-cost vs Socofe/VEH"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1965; Strong AG+CW; leftover unused energy-holding IGS after HELORA; "
        "not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_ceneo_nbb_pdf_commune_dividend_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Wallonie>Hainaut>CENEO>nbb_pdf_commune_dividend_matrix_L5",
    "entity_id": "ceneo",
    "what_is_missing": (
        "NBB deposit reference number / official CDN PDF body YE2025 "
        "(CW neerlegging 21.07.2026; AG pack Strong but deposit id unpublished); "
        "per-commune dividend / attribution matrix reconcilable with 24.775m out "
        "and 45.470m dividends received; ORES Assets covenant dual vs Socofe/VEH "
        "unit-cost; Engie RDV policy detail; cash/placements split"
    ),
    "why_it_matters": (
        "1.172bn municipal energy holding with 792m ORES + 310m SOCOFE stakes: "
        "opacity on which communes capture 24.8m dividends and how ORES covenant "
        "shifts timing without matrix"
    ),
    "priority": "8",
    "recipient_body": "CENEO SC (cc SPW / communes membres / IGRETEC management)",
    "recipient_email": "info@ceneo.be",
    "recipient_postal": "Boulevard Pierre Mayence 1/1 6000 Charleroi",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ceneo_jr2025_statutory_assets",
    "linked_leaderboard_id": "lb_ceneo_assets_1_17bn_pnl_41m_ores_socofe_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1965; human-send only; Strong AG; next every-10 1970",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — CENEO (NBB deposit ref / commune dividend matrix / ORES-SOCOFE dual)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** CENEO SC (ex-IPFH) — KBO **0201.645.281** (Walloon Hainaut energy holding)  
**recipient:** info@ceneo.be / cc SPW / communes membres / IGRETEC management  
**sources:** [AG Mons Rapport financier 2025](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/ceneo-1/ceneo/ag-du-29-juin-2026/publiable-ceneo_rapport-financier_2025.pdf/@@download/file/Publiable%20-%20CENEO_Rapport-financier_2025.pdf) · [Companyweb NL](https://www.companyweb.be/nl/0201645281/ceneo) · [Companyweb EN](https://www.companyweb.be/en/0201645281/ceneo) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0201645281) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0201645281)  
**tick:** 1965  
**confidence on table euros:** Strong (official AG financial report + CW NL+EN confirm)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **21.07.2026**): assets **EUR1,171,706,286.70**; pnl **EUR41,353,730.07** (**DROP −2.9%**); equity **EUR959,638,681**; debt **EUR212,067,606.08**; dividends received **EUR45,469,560.23**; omzet **EUR954,029.31**; dividend to associates **EUR24,775,000**; ORES Assets VNC **EUR792,362,510.24** (70.21%); SOCOFE **EUR309,568,103** (27.42%).
- Same Charleroi seat / management path as IGRETEC (already mined tick1961).
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo HELORA / iMio / Passelecq / IGRETEC / IPFBW / Aquiris / SPGE / water-nuclear stack.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: CENEO SC
t.a.v. openbaarheid / information officer
Boulevard Pierre Mayence 1/1
6000 Charleroi

cc: SPW — transparence / communes membres CENEO / IGRETEC (management)

Betreft: Verzoek om openbaarmaking — NBB-deposit YE2025 CENEO,
gemeentelijke dividend-matrix en ORES/SOCOFE-dual (KBO 0201.645.281)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / CDLD)
vraag ik:

1. Digitaal afschrift / deposit-referentienummer van de bij de NBB
   neergelegde jaarrekening 2025 van CENEO SC (Companyweb noemt
   neerlegging 21.07.2026; AG-publieke pack bevestigt totalen).
2. Per-commune dividend- / attributiematrix 2025 reconcilieerbaar
   met EUR24.775.000 uitkering aan vennoten.
3. Dual unit-cost / stake recon vs ORES Assets (VNC EUR792.362.510,24)
   en SOCOFE (EUR309.568.103) + impact ORES dividend-covenant.
4. Toelichting Engie RDV-beleid en cash/placements-split YE2025.
5. Sector I–VII P&L matrix (energiecentrale / renewables) indien
   niet al in AG-pack.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (CENEO SC + SPW/communes/IGRETEC cc)
- [x] Concrete documenten (NBB deposit ref / commune dividend matrix / ORES dual)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; IDEA already mined Strong RA; HYGEA CW still YE2024; took unused leftover **CENEO** YE2025 Strong AG.
""",
        encoding="utf-8",
    )

# research_queue: close rq_1965, spawn rq_1966
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

have_1966 = False
for row in rq_rows:
    if row.get("task_id") == "rq_1965":
        row["status"] = "done"
        row["entity_id"] = "ceneo"
        row["title"] = (
            "leftover dual hole-fill after CHU HELORA — CENEO YE2025 Strong"
        )
        row["updated_utc"] = TS
        row["blocked_gap_id"] = gap_id
        row["notes"] = (
            "tick1965 CENEO YE2025 Strong assets 1.172bn pnl DROP 41.35m "
            "equity 959.64m debt 212.07m; FOI ready; next rq_1966; next every-10 1970"
        )
        row["instructions"] = (
            "Completed: CENEO leftover Walloon Hainaut energy-holding IGS dual after "
            "CHU HELORA; KBO 0201.645.281; YE2025 Strong AG Mons PDF + CW NL+EN "
            "(assets 1.172bn pnl DROP 41.35m equity 959.64m debt 212.07m "
            "div_recv 45.47m ORES VNC 792.36m); FOI "
            f"{gap_id} ready"
        )
        row["hierarchy_target"] = "Wallonie>Hainaut>CENEO>JR2025_L5"
    if row.get("task_id") == "rq_1966":
        have_1966 = True

if not have_1966:
    rq_rows.append(
        {
            "task_id": "rq_1966",
            "title": "leftover dual hole-fill after CENEO",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1966 after 1965 CENEO YE2025 Strong. Prefer leftover AGB/APB if "
                "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/nuclear. Do NOT redo CENEO, CHU HELORA, "
                "iMio, Gabrielle Passelecq, IGRETEC, IPFBW, Aquiris, SPGE, IRE parent, IRE ELiT, "
                "FANC, SCK CEN, EURIDICE, BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
                "NIRAS, Bel V, Dijk92, Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, SOWAER, INASEP, inBW, AIDE, ORES, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1965 CENEO; next every-10 1970",
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
            "last_unit_id": "rq_1965",
            "ticks_completed": "1965",
            "paused": "no",
            "notes": (
                "tick1965 CENEO YE2025 Strong AG+CW (assets 1.172bn pnl DROP 41.35m "
                "equity 959.64m debt 212.07m div_recv 45.47m ORES VNC 792.36m); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1966; next every-10 1970"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""

## Tick 1965 - {TS} - rq_1965 CENEO (assets 1.172bn / pnl DROP 41.35m / Strong)

- Unit: **rq_1965** leftover dual after **rq_1964 CHU HELORA**. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. IDEA already Strong RA-mined. HYGEA CW still YE2024. Took unused leftover **CENEO** YE2025 (KBO **0201.645.281**; Boulevard Pierre Mayence 1/1 Charleroi; Walloon Hainaut energy holding / ex-IPFH; **ORES Assets + SOCOFE dual**; same seat/management as IGRETEC). Do not redo HELORA/iMio/Passelecq/IGRETEC/IPFBW/Aquiris/SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/INASEP/inBW/AIDE/ORES/IDEA.
- Found: Strong [Mons AG 29.06.2026 Rapport financier PDF](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/ceneo-1/ceneo/ag-du-29-juin-2026/publiable-ceneo_rapport-financier_2025.pdf/@@download/file/Publiable%20-%20CENEO_Rapport-financier_2025.pdf) + Medium [Companyweb NL](https://www.companyweb.be/nl/0201645281/ceneo)/[EN](https://www.companyweb.be/en/0201645281/ceneo) + Strong KBO: assets **EUR1,171,706,286.70**; pnl **EUR41,353,730.07** (**DROP −2.9%**); equity **EUR959,638,681**; debt **EUR212,067,606.08**; dividends received **EUR45,469,560.23**; omzet **EUR954,029.31**; dividend out **EUR24,775,000**; ORES Assets VNC **EUR792,362,510.24** (70.21%); SOCOFE **EUR309,568,103** (27.42%); neerlegging **21.07.2026**.
- Wrote: sources (+4); budgets (+7); commitments (+1); leaderboard (+1); entities (+1 ceneo); foi + draft {gap_id}; rq_1965=done + rq_1966 open; loop_state ticks=1965; raw PDF saved.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1970**). Next: rq_1966 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1965 write complete: CENEO Strong YE2025")
