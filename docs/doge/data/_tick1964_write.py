# tick 1964 — CHU HELORA YE2025 Medium CW (rq_1964 after iMio)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T18:15:00Z"
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
        "source_id": "src_helora_jr2025_cw",
        "title": "Companyweb CHU HELORA YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0801643533/chu-helora",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1964; Laatste balansjaar 2025; neergelegd 27-06-2026; "
            "omzet 900540159 JUMP +4.8pct; pnl JUMP turnaround 7860643 vs LOSS 3370003; "
            "equity 135310273 +3.95pct; bruto 391037739; FTE 4026.3; Groot; "
            "KBO 0801.643.533"
        ),
    },
    {
        "source_id": "src_helora_jr2025_cw_en",
        "title": "Companyweb EN twin CHU HELORA YE2025 turnover equity",
        "url": "https://www.companyweb.be/en/0801643533/chu-helora",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1964; Last balance sheet year 2025; Turnover 900540159; "
            "Profit/Loss 7860643; Equity 135310273; Gross margin 391037739; "
            "FTE 4026.3; filed 27-06-2026"
        ),
    },
    {
        "source_id": "src_helora_jr2024_upswitch",
        "title": "Upswitch NBB/CBSO CHU HELORA YE2024 assets (YE2025 lag)",
        "url": "https://www.upswitch.app/en/companies/be/chu-helora-0801643533",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1964; Upswitch still YE2024-only this tick: assets 633265402 equity "
            "130173997 revenue 859315064 EBITDA 46307967; YE2025 assets Unknown"
        ),
    },
    {
        "source_id": "src_helora_kbo_1964",
        "title": "KBO CHU HELORA 0801.643.533 Actief VZW Mons",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0801643533",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1964; Actief VZW sinds 10.05.2023; zetel Boulevard Fulgence Masson 5 "
            "7000 Mons; aanbestedende overheid; NACE 86.101/86.109; absorbed Jolimont "
            "pole + HELORA ASBL 30.06.2023; NBB consult "
            "https://consult.cbso.nbb.be/consult-enterprise/0801643533; "
            "dual Gabrielle Passelecq / CHU Mons network"
        ),
    },
    {
        "source_id": "src_helora_site_1964",
        "title": "HELORA.be contact / largest Walloon hospital group",
        "url": "https://www.helora.be/hopitaux/contactez-nous",
        "publisher": "CHU HELORA ASBL",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": (
            "tick1964; sites Jolimont/Lobbes/Nivelles/Tubize/Mons/Warquignies; "
            "no public FOI mailbox on contact page this tick; postal HQ Mons"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1964 YE2025 Medium CW NL+EN + Strong KBO 0801.643.533 Actief VZW; "
    "omzet JUMP 900.54m pnl JUMP turnaround 7.86m equity JUMP 135.31m bruto 391.04m "
    "FTE 4026.3; assets/debt Unknown (Upswitch still YE2024 assets 633.27m); "
    "neerlegging 27.06.2026; Walloon hospital mega-group dual Gabrielle Passelecq; "
    "FOI gap_helora_nbb_pdf_assets_debt_passelecq_matrix_l5; "
    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
    "do not redo iMio/Passelecq/IPFBW/IGRETEC/Aquiris/SPGE/Hydria/Vivaqua/CILE/IRE*/"
    "FANC/SCK/EURIDICE/BRUGEL/Belgoprocess/Laborelec/NIRAS/Bel V/Dijk92/AIEG/Synergrid"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if "vzw_chu_helora" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "vzw_chu_helora",
                "name_nl": "CHU HELORA (Walloons grootste ziekenhuisgroep / Mons-Jolimont)",
                "name_fr": "CHU HELORA (plus grand groupe hospitalier wallon / Mons-Jolimont)",
                "name_en": "CHU HELORA (largest Walloon hospital group / Mons-Jolimont)",
                "level": "intercommunale_adjacent",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.helora.be/",
                "foi_email": "",
                "foi_postal": "Boulevard Fulgence Masson 5 7000 Mons",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "vzw_chu_helora": {
                "notes": ent_notes,
                "foi_postal": "Boulevard Fulgence Masson 5 7000 Mons",
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
        "budget_id": "bud_helora_omzet_jr2025_statutory",
        "entity_id": "vzw_chu_helora",
        "year": "2025",
        "amount_eur": "900540159",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_helora_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1964; YE2025 omzet 900540159 JUMP +4.8pct vs 859315064",
    },
    {
        "budget_id": "bud_helora_pnl_jr2025_statutory",
        "entity_id": "vzw_chu_helora",
        "year": "2025",
        "amount_eur": "7860643",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived Winst/Verlies (turnaround)",
        "source_id": "src_helora_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1964; YE2025 pnl JUMP turnaround 7860643 vs LOSS 3370003 YE2024 (+333pct)",
    },
    {
        "budget_id": "bud_helora_bruto_jr2025_statutory",
        "entity_id": "vzw_chu_helora",
        "year": "2025",
        "amount_eur": "391037739",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto/gross margin",
        "source_id": "src_helora_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1964; YE2025 bruto 391037739 +6.69pct vs 366528999",
    },
    {
        "budget_id": "bud_helora_equity_jr2025_statutory",
        "entity_id": "vzw_chu_helora",
        "year": "2025",
        "amount_eur": "135310273",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived equity",
        "source_id": "src_helora_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1964; YE2025 equity 135310273 JUMP +3.95pct vs 130173997",
    },
    {
        "budget_id": "bud_helora_fte_jr2025_statutory",
        "entity_id": "vzw_chu_helora",
        "year": "2025",
        "amount_eur": "4026.3",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_helora_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1964; YE2025 FTE 4026.3 DROP vs 4176.9 YE2024 / 4566.1 YE2023",
    },
    {
        "budget_id": "bud_helora_assets_jr2024_upswitch_lag",
        "entity_id": "vzw_chu_helora",
        "year": "2024",
        "amount_eur": "633265402",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB YE2024 assets (YE2025 Unknown)",
        "source_id": "src_helora_jr2024_upswitch",
        "confidence": "medium",
        "notes": "tick1964; YE2024 assets 633265402 for context; YE2025 assets Unknown this tick",
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
    "commitment_id": "comm_helora_jr2025_statutory_omzet",
    "title": (
        "CHU HELORA YE2025 leftover Walloon hospital mega-group dual statutory "
        "(omzet JUMP 900.54m / pnl JUMP turnaround 7.86m / equity 135.31m)"
    ),
    "entity_id": "vzw_chu_helora",
    "beneficiary": "Wallonie Hainaut/BW hospital patients / Gabrielle Passelecq dual path",
    "legal_basis": (
        "VZW / aanbestedende overheid; NBB neerlegging; "
        "decret wallon openbaarheid / Code de la democratie locale"
    ),
    "decision_date": "2026-06-27",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "900540159",
    "cash_by_year": (
        "2025:omzet=900540159;bruto=391037739;pnl=7860643;equity=135310273;"
        "fte=4026.3;assets=Unknown;debt=Unknown;YE2024_assets_upswitch=633265402"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0801643533/chu-helora",
    "stated_goal": (
        "Largest Walloon hospital group: Mons-Jolimont-Lobbes-Nivelles-Tubize-"
        "Warquignies network (absorbed Jolimont/HELORA 2023)"
    ),
    "cut_option": (
        "FOI NBB PDF + assets/debt YE2025 + Passelecq dual fee/staff matrix + "
        "reconcile FTE DROP 4566→4026 with omzet JUMP"
    ),
    "source_id": "src_helora_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>Mons>CHU_HELORA>JR2025_statutory_L5",
    "notes": (
        "tick1964; Medium CW after iMio; preferred AGB Bornem JR2024 / FARO YE2024 / "
        "AIESH YE2024 / REW YE2024; do not redo iMio/Passelecq/IPFBW/IGRETEC/Aquiris/"
        "SPGE/nuclear stack; not TE-additive of 348bn"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_helora_omzet_jump_900_54m_pnl_turnaround_7_86m_jr2025",
    "name": (
        "CHU HELORA omzet JUMP 900.54m / pnl JUMP turnaround 7.86m / equity 135.31m "
        "(Walloon hospital mega-group YE2025)"
    ),
    "level": "L5",
    "type": "walloon_hospital_megagroup_dual",
    "hierarchy_path": "Wallonie>Hainaut>Mons>CHU_HELORA>JR2025_statutory_L5",
    "annual_cost_eur": "900540159",
    "total_cost_eur": "135310273",
    "tco_notes": (
        "statutory omzet 900540159 JUMP bruto 391037739 pnl JUMP turnaround 7860643 "
        "equity 135310273 fte 4026.3; assets/debt YE2025 Unknown (Upswitch YE2024 633m); "
        "dual Gabrielle Passelecq"
    ),
    "confidence": "medium",
    "source_id": "src_helora_jr2025_cw",
    "beneficiaries": "Wallonie picarde/BW patients / HELORA network / Passelecq dual",
    "stated_goal": "Largest Walloon multi-site hospital ASBL group",
    "measured_outcome": (
        "CW NL+EN YE2025 live unused after preferred AGB/FARO/AIESH/REW stall + after "
        "iMio; pnl turnaround vs LOSS 2024; primary NBB PDF + YE2025 BS unresolved"
    ),
    "absurdity_score": "4.5",
    "cost_score": "9.0",
    "difficulty": "4.0",
    "priority_index": "6.5",
    "cut_proposal": (
        "Publish NBB PDF + YE2025 assets/debt + Passelecq dual fee/staff recon; "
        "explain FTE DROP with omzet JUMP and LOSS→profit turnaround"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1964; Medium CW; leftover unused hospital mega-group IGS-adjacent after "
        "iMio; not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_helora_nbb_pdf_assets_debt_passelecq_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Wallonie>Hainaut>Mons>CHU_HELORA>nbb_pdf_assets_debt_passelecq_L5",
    "entity_id": "vzw_chu_helora",
    "what_is_missing": (
        "NBB deposit PDF body YE2025 (CW neerlegging 27.06.2026); "
        "assets / schulden LT-ST / cash YE2025 (Upswitch still YE2024 assets 633.27m only); "
        "Gabrielle Passelecq dual fee/staff/transfer matrix vs HELORA omzet 900.54m; "
        "reconcile FTE DROP 4566→4026 with omzet JUMP + pnl LOSS→profit turnaround"
    ),
    "why_it_matters": (
        "Largest Walloon hospital group: 900.54m omzet / 4026 FTE with opaque YE2025 BS "
        "and Passelecq dual stack — material public-euro opacity without NBB PDF"
    ),
    "priority": "8",
    "recipient_body": "CHU HELORA ASBL (cc Intercommunale Gabrielle Passelecq / Ville de Mons)",
    "recipient_email": "officiel.ic-chupmb@chupmb.be",
    "recipient_postal": "Boulevard Fulgence Masson 5 7000 Mons",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_helora_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_helora_omzet_jump_900_54m_pnl_turnaround_7_86m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": (
        "tick1964; human-send only; Medium CW; HELORA has no KBO FOI mailbox — "
        "cc Passelecq officiel + postal HELORA HQ; next every-10 1970"
    ),
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — CHU HELORA (NBB PDF / assets-debt / Passelecq dual matrix)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** CHU HELORA ASBL — KBO **0801.643.533** (largest Walloon hospital group / Mons-Jolimont)  
**recipient:** postal HELORA HQ + cc officiel.ic-chupmb@chupmb.be (Passelecq dual; HELORA has no KBO FOI mailbox this tick)  
**sources:** [Companyweb NL](https://www.companyweb.be/nl/0801643533/chu-helora) · [Companyweb EN](https://www.companyweb.be/en/0801643533/chu-helora) · [Upswitch YE2024 lag](https://www.upswitch.app/en/companies/be/chu-helora-0801643533) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0801643533) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0801643533) · [helora.be contact](https://www.helora.be/hopitaux/contactez-nous)  
**tick:** 1964  
**confidence on table euros:** Medium (NBB-derived CW NL+EN; Upswitch YE2025 assets lag; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **27.06.2026**): omzet **EUR900,540,159** (**JUMP +4.8%**); bruto **EUR391,037,739**; pnl **EUR7,860,643** (**JUMP turnaround** vs LOSS EUR3,370,003); equity **EUR135,310,273**; FTE **4026.3**.
- Assets / debt / cash YE2025 **Unknown** (Upswitch still YE2024 assets **EUR633,265,402** only — not invented).
- Dual: Gabrielle Passelecq already mined tick1962 (omzet 77.72m / assets 139.22m). Absorbed Jolimont pole + HELORA 30.06.2023.
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo iMio / Passelecq / IPFBW / IGRETEC / Aquiris / SPGE / nuclear stack.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: CHU HELORA ASBL
t.a.v. openbaarheid / direction generale
Boulevard Fulgence Masson 5
7000 Mons

cc: Intercommunale Gabrielle Passelecq SC
    officiel.ic-chupmb@chupmb.be
    Chemin du Chene aux Haies 24, 7000 Mons
    Ville de Mons — College

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025 CHU HELORA,
balansposten en dual-matrix Gabrielle Passelecq (KBO 0801.643.533)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / CDLD)
vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   van CHU HELORA ASBL (deposit-/referentienummer + PDF; Companyweb noemt
   neerlegging 27.06.2026).
2. Balanstotaal / schulden LT-ST / cash YE2025 (Upswitch nog YE2024 assets
   EUR633.265.402; CW omzet EUR900.540.159; equity EUR135.310.273).
3. Dual fee/staff/transfer matrix vs Intercommunale Gabrielle Passelecq
   (tick1962: omzet EUR77.72m / assets EUR139.22m).
4. Uitleg FTE DROP 4566 (2023) → 4026 (2025) bij omzet JUMP + pnl
   LOSS→winst turnaround.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (CHU HELORA + Passelecq/Mons cc)
- [x] Concrete documenten (NBB PDF / BS / dual matrix)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated; confirm HELORA FOI mailbox)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; took unused leftover **CHU HELORA** YE2025 live after iMio.
""",
        encoding="utf-8",
    )

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1964": {
            "status": "done",
            "entity_id": "vzw_chu_helora",
            "updated_utc": TS,
            "notes": (
                "tick1964; Completed: CHU HELORA leftover Walloon hospital mega-group "
                "YE2025 Medium CW (omzet JUMP 900.54m / pnl JUMP turnaround 7.86m / "
                "equity 135.31m); preferred AGB Bornem JR2024 / FARO/AIESH/REW YE2024; "
                "FOI gap_helora_nbb_pdf_assets_debt_passelecq_matrix_l5 ready; "
                "next every-10 1970"
            ),
        }
    },
)

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    rq_ids = {r.get("task_id") for r in csv.DictReader(f)}

if "rq_1965" not in rq_ids:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1965",
                "title": "leftover dual hole-fill after CHU HELORA",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/nuclear. "
                    "Do NOT redo CHU HELORA, iMio, Gabrielle Passelecq, IPFBW, IGRETEC, Aquiris, "
                    "SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
                    "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, "
                    "RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "tick1964; next after HELORA; next every-10 1970",
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
            "last_unit_id": "rq_1964",
            "ticks_completed": "1964",
            "paused": "no",
            "notes": (
                "tick1964 leftover CHU HELORA 0801.643.533 Medium CW "
                "(omzet JUMP 900.54m pnl JUMP turnaround 7.86m equity 135.31m bruto 391.04m "
                "FTE 4026.3; assets YE2025 Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1965; next every-10 1970; continuous hole_fill"
            ),
        }
    },
)

print("tick1964 HELORA write OK")
