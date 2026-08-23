# tick 1960 — EVERY-10 + Aquiris YE2025 Medium CW (rq_1960 after SPGE)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T16:45:00Z"
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
        "source_id": "src_aquiris_jr2025_cw",
        "title": "Companyweb Aquiris YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0475443124/aquiris",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1960; Laatste balansjaar 2025; neergelegd 28-07-2026; "
            "omzet 55272688 JUMP +1.95pct; pnl JUMP 4867234 +326.93pct; "
            "equity 7590000 flat; bruto 29126214 JUMP +16.04pct; FTE 62; "
            "Groot; KBO 0475.443.124; assets/debt Unknown (Upswitch still YE2024)"
        ),
    },
    {
        "source_id": "src_aquiris_jr2025_cw_en",
        "title": "Companyweb EN twin Aquiris YE2025 turnover equity",
        "url": "https://www.companyweb.be/en/0475443124/aquiris",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1960; Last balance sheet year 2025; Turnover 55272688; "
            "Profit/Loss 4867234; Equity 7590000; Gross margin 29126214; FTE 62; "
            "filed 28-07-2026"
        ),
    },
    {
        "source_id": "src_aquiris_kbo_1960",
        "title": "KBO Aquiris 0475.443.124 Actief NV STEP Bruxelles-Nord",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0475443124",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1960; Actief NV; zetel Vilvoordselaan 450 1130 Brussel; "
            "NACE 36.000 water; kapitaal 6900000; geen KBO email/web; "
            "NBB consult https://consult.cbso.nbb.be/consult-enterprise/0475443124"
        ),
    },
    {
        "source_id": "src_aquiris_site_1960",
        "title": "Aquiris.be Bruxelles-Nord STEP (Veolia BOOT)",
        "url": "https://www.aquiris.be/",
        "publisher": "Aquiris SA / Veolia",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": (
            "tick1960; largest BE wastewater plant; Veolia BOOT dual Hydria/Vivaqua BCR; "
            "no statutory euros on public site this tick"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1960 YE2025 Medium CW NL+EN + Strong KBO 0475.443.124 Actief NV; "
    "omzet JUMP 55.27m pnl JUMP 4.87m equity 7.59m flat bruto JUMP 29.13m FTE 62; "
    "kapitaal 6.90m; assets/debt Unknown (Upswitch still YE2024 assets 82.3m class); "
    "Veolia BOOT STEP Bruxelles-Nord dual Hydria/Vivaqua; "
    "FOI gap_aquiris_nbb_pdf_assets_debt_boot_fee_matrix_l5; "
    "preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
    "do not redo SPGE/Hydria/Vivaqua/CILE/SWDE/IRE*/FANC/SCK/EURIDICE/BRUGEL"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if "nv_aquiris" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "nv_aquiris",
                "name_nl": "Aquiris (STEP Brussel-Noord / Veolia BOOT)",
                "name_fr": "Aquiris (STEP Bruxelles-Nord / Veolia BOOT)",
                "name_en": "Aquiris (Brussels-North WWTP / Veolia BOOT)",
                "level": "company",
                "parent_id": "brussels_gov",
                "community_language": "bi",
                "website": "https://www.aquiris.be",
                "foi_email": "info@hydria.be",
                "foi_postal": "Vilvoordselaan 450 1130 Brussel (cc Hydria Keizerinlaan 17-19)",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "nv_aquiris": {
                "notes": ent_notes,
                "foi_email": "info@hydria.be",
                "foi_postal": "Vilvoordselaan 450 1130 Brussel (cc Hydria Keizerinlaan 17-19)",
                "website": "https://www.aquiris.be",
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_aquiris_omzet_jr2025_statutory",
        "entity_id": "nv_aquiris",
        "year": "2025",
        "amount_eur": "55272688",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_aquiris_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1960; YE2025 omzet 55272688 JUMP +1.95pct vs 54217274",
    },
    {
        "budget_id": "bud_aquiris_pnl_jr2025_statutory",
        "entity_id": "nv_aquiris",
        "year": "2025",
        "amount_eur": "4867234",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived Winst/Verlies",
        "source_id": "src_aquiris_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1960; YE2025 pnl JUMP 4867234 +326.93pct vs 1140054",
    },
    {
        "budget_id": "bud_aquiris_bruto_jr2025_statutory",
        "entity_id": "nv_aquiris",
        "year": "2025",
        "amount_eur": "29126214",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto/gross margin",
        "source_id": "src_aquiris_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1960; YE2025 bruto 29126214 JUMP +16.04pct vs 25099896",
    },
    {
        "budget_id": "bud_aquiris_equity_jr2025_statutory",
        "entity_id": "nv_aquiris",
        "year": "2025",
        "amount_eur": "7590000",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived equity",
        "source_id": "src_aquiris_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1960; YE2025 equity 7590000 flat vs YE2022-2024; KBO kapitaal 6900000",
    },
    {
        "budget_id": "bud_aquiris_fte_jr2025_statutory",
        "entity_id": "nv_aquiris",
        "year": "2025",
        "amount_eur": "62",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_aquiris_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1960; YE2025 FTE 62 vs 62.4 YE2024",
    },
    {
        "budget_id": "bud_aquiris_kapitaal_kbo_1960",
        "entity_id": "nv_aquiris",
        "year": "2025",
        "amount_eur": "6900000",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "KBO registered capital",
        "source_id": "src_aquiris_kbo_1960",
        "confidence": "strong",
        "notes": "tick1960; KBO kapitaal 6900000; equity CW 7590000",
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
    "commitment_id": "comm_aquiris_jr2025_statutory_omzet",
    "title": (
        "Aquiris YE2025 leftover BCR STEP-Nord Veolia BOOT dual statutory "
        "(omzet JUMP 55.27m / pnl JUMP 4.87m / equity 7.59m)"
    ),
    "entity_id": "nv_aquiris",
    "beneficiary": "BCR / Hydria / Vivaqua wastewater users / Woluwe basin dual",
    "legal_basis": (
        "NV CSA; BOOT/PPP with Hydria (ex-SBGE); NBB neerlegging; "
        "ordonnances bruxelloises openbaarheid analog for public-fee dual"
    ),
    "decision_date": "2026-07-28",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "55272688",
    "cash_by_year": (
        "2025:omzet=55272688;bruto=29126214;pnl=4867234;"
        "equity=7590000;fte=62;kapitaal=6900000;assets=Unknown;debt=Unknown"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0475443124/aquiris",
    "stated_goal": "Operate Brussels-North wastewater treatment plant (BOOT/Veolia)",
    "cut_option": "FOI NBB PDF + assets/debt + Hydria BOOT fee/redevance matrix + dual vs Hydria omzet",
    "source_id": "src_aquiris_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Bruxelles>Eau>Hydria>Aquiris_STEP_Nord>JR2025_statutory_L5",
    "notes": (
        "tick1960 EVERY-10 dual; Medium CW NL+EN after SPGE; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo SPGE/Hydria/Vivaqua/CILE/"
        "IRE/FANC/SCK/EURIDICE/BRUGEL/Belgoprocess; not TE-additive of 348bn"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_aquiris_omzet_jump_55_27m_pnl_jump_4_87m_jr2025",
    "name": (
        "Aquiris omzet JUMP 55.27m / pnl JUMP 4.87m / equity 7.59m flat "
        "(Veolia BOOT STEP Nord YE2025)"
    ),
    "level": "L5",
    "type": "bcr_wastewater_boot_ppp_dual",
    "hierarchy_path": "Bruxelles>Eau>Hydria>Aquiris_STEP_Nord>JR2025_statutory_L5",
    "annual_cost_eur": "55272688",
    "total_cost_eur": "7590000",
    "tco_notes": (
        "statutory omzet 55272688 JUMP bruto 29126214 pnl JUMP 4867234 "
        "equity 7590000 flat fte 62; assets/debt Unknown; dual Hydria/Vivaqua BCR"
    ),
    "confidence": "medium",
    "source_id": "src_aquiris_jr2025_cw",
    "beneficiaries": "BCR households / Hydria / Woluwe basin / Veolia BOOT path",
    "stated_goal": "Treat Brussels-North + Woluwe-basin wastewater under BOOT",
    "measured_outcome": (
        "CW NL+EN YE2025 live (deferred from earlier ticks); pnl JUMP +327pct with flat equity; "
        "primary NBB PDF + BS + BOOT fee matrix unresolved; Upswitch still YE2024-only"
    ),
    "absurdity_score": "5.0",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.4",
    "cut_proposal": (
        "Publish NBB PDF + assets/debt + Hydria BOOT fee/redevance matrix; "
        "scrutinise thin equity 7.59m vs 55m public-fee omzet"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1960 EVERY-10 dual; Medium CW; leftover water after SPGE; "
        "not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_aquiris_nbb_pdf_assets_debt_boot_fee_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Bruxelles>Eau>Hydria>Aquiris>nbb_pdf_boot_fee_L5",
    "entity_id": "nv_aquiris",
    "what_is_missing": (
        "NBB deposit PDF body YE2025 (CW neerlegging 28.07.2026); "
        "assets / debt LT-ST / cash exact (Upswitch still YE2024-only); "
        "Hydria BOOT / redevance / availability-fee matrix 2025 vs Aquiris omzet 55.27m; "
        "reconcile pnl JUMP +327pct with flat equity 7.59m; "
        "end-of-BOOT transfer terms and public TCO"
    ),
    "why_it_matters": (
        "Largest BE wastewater plant run as Veolia BOOT: 55.27m omzet / thin 7.59m equity "
        "and opaque assets — public sanitation fees via Hydria/Vivaqua dual without BS"
    ),
    "priority": "8",
    "recipient_body": "Hydria NV van publiek recht (cc Aquiris SA / Vivaqua / Brussel Leefmilieu)",
    "recipient_email": "info@hydria.be",
    "recipient_postal": (
        "Keizerinlaan 17-19 1000 Brussel; Aquiris: Vilvoordselaan 450 1130 Brussel"
    ),
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_aquiris_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_aquiris_omzet_jump_55_27m_pnl_jump_4_87m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1960 EVERY-10; human-send only; Medium CW; next every-10 1970",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — Aquiris (NBB PDF / assets-debt / BOOT fee matrix)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** Aquiris SA — KBO **0475.443.124** (Veolia BOOT STEP Bruxelles-Nord)  
**recipient:** info@hydria.be (Hydria public BOOT counterparty) / cc Aquiris Vilvoordselaan 450 1130 Brussel / Vivaqua / Brussel Leefmilieu  
**sources:** [Companyweb NL](https://www.companyweb.be/nl/0475443124/aquiris) · [Companyweb EN](https://www.companyweb.be/en/0475443124/aquiris) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0475443124) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0475443124) · [aquiris.be](https://www.aquiris.be/)  
**tick:** 1960 (**EVERY-10** progress coverage % + waste top10 + dual)  
**confidence on table euros:** Medium (NBB-derived CW NL+EN; primary deposit PDF unresolved; Upswitch still YE2024 for assets)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **28.07.2026**): omzet **EUR55,272,688** (**JUMP +1.95%**); bruto **EUR29,126,214**; pnl **EUR4,867,234** (**JUMP +326.93%**); equity **EUR7,590,000** (flat); FTE **62**; KBO kapitaal **EUR6,900,000**.
- Assets / debt / cash **Unknown** (Upswitch still YE2024 assets ~EUR82.3m class only — not used as YE2025).
- Public BOOT counterparty: **Hydria** (ex-SBGE). Dual already mined: Hydria omzet 45.0m / Vivaqua omzet 356.0m.
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo SPGE / Hydria / Vivaqua / CILE / IRE cluster / BRUGEL.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Hydria NV van publiek recht
t.a.v. openbaarheid / information officer
Keizerinlaan 17-19
1000 Brussel

cc: Aquiris SA — Vilvoordselaan 450, 1130 Brussel
    Vivaqua — Keizerinlaan 17-19, 1000 Brussel
    Brussel Leefmilieu / Bruxelles Environnement

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025 Aquiris,
balansposten en BOOT/redevance-matrix (KBO 0475.443.124)

Geachte,

Op grond van toepasselijke openbaarheid (ordonnances bruxelloises /
Bestuursdecreet-analoog voor publieke BOOT-tegenpartij)
vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   van Aquiris SA (deposit-/referentienummer + PDF; Companyweb noemt
   neerlegging 28.07.2026).
2. Balanstotaal / schulden LT-ST / cash reconcilieerbaar met publieke
   aggregators (CW omzet EUR55.272.688; equity EUR7.590.000;
   Upswitch YE2024 assets ~EUR82.3m — YE2025 assets Unknown).
3. BOOT / availability-fee / redevance-matrix 2025 Hydria↔Aquiris
   (bedragen; indexatie; performance deductions) vs statutaire omzet.
4. Uitleg pnl JUMP +327% bij flat equity 7.59m + eventuele dividend/
   related-party flows naar Veolia-groep.
5. End-of-BOOT transfervoorwaarden en publieke TCO-raming indien beschikbaar.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (Hydria public BOOT + Aquiris/Vivaqua cc)
- [x] Concrete documenten (NBB PDF / BS / BOOT fee matrix)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; took deferred leftover **Aquiris** YE2025 live + **EVERY-10**.
""",
        encoding="utf-8",
    )

# research_queue: close rq_1960, spawn rq_1961
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

have_1961 = False
for row in rq_rows:
    if row.get("task_id") == "rq_1960":
        row["status"] = "done"
        row["entity_id"] = "nv_aquiris"
        row["updated_utc"] = TS
        row["notes"] = (
            "tick1960 EVERY-10 + Aquiris YE2025 Medium omzet JUMP 55.27m pnl JUMP 4.87m "
            "equity 7.59m; FOI ready; next rq_1961; next every-10 1970"
        )
        row["title"] = (
            "EVERY-10 + leftover dual after SPGE — Aquiris YE2025 Medium"
        )
    if row.get("task_id") == "rq_1961":
        have_1961 = True

if not have_1961:
    rq_rows.append(
        {
            "task_id": "rq_1961",
            "title": "leftover dual hole-fill after Aquiris EVERY-10",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1961 after 1960 EVERY-10 + Aquiris YE2025 statutory. "
                "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/nuclear. "
                "Do NOT redo Aquiris, SPGE, IRE parent, IRE ELiT, FANC, SCK CEN, EURIDICE, "
                "BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
                "Dijk92, Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, Fluxys*, ETB, "
                "Elia, BNO, SWDE."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1960; next every-10 1970",
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
            "last_unit_id": "rq_1960",
            "ticks_completed": "1960",
            "paused": "no",
            "notes": (
                "tick1960 EVERY-10 + Aquiris 0475.443.124 Medium CW NL+EN "
                "(omzet JUMP 55.27m pnl JUMP 4.87m equity 7.59m bruto 29.13m FTE 62); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1961; next every-10 1970; "
                "continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = """

## Tick 1960 - 2026-08-23T16:45:00Z - rq_1960 EVERY-10 + Aquiris (omzet JUMP 55.27m / pnl JUMP 4.87m / Medium)

- Unit: **rq_1960** AFTER **rq_1959 SPGE**. **EVERY-10 REQUIRED** (progress A–E % of €347.956bn TE + waste top10 by priority_index). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024**. Took deferred leftover **Aquiris** YE2025 (KBO **0475.443.124**; Vilvoordselaan 450 Brussel; Veolia BOOT STEP Bruxelles-Nord; **Hydria/Vivaqua dual**). Do not redo SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/SWDE.
- Found: Companyweb NL+EN YE2025 — omzet **EUR55,272,688** JUMP +1.95%; bruto **EUR29,126,214**; pnl **EUR4,867,234** JUMP +326.93%; equity **EUR7,590,000** flat; FTE **62**; KBO kapitaal **EUR6,900,000**; neerlegging **28.07.2026**. Assets/debt Unknown (Upswitch still YE2024-only). Medium confidence.
- EVERY-10: refreshed `progress_every_10_ticks.md` (A 100% / B 100% / C ~99% / D ~74-88% generous / E ~1576 ready) + `doge_waste_top10_current.md` (pure annual top10 **stable** GIP→dual cars; OWV snowball/Metro3/corrupt AGB pi>10 filtered). Inventory ~budgets 51837 / commitments 5625 / leaderboard 7746 / entities 1663 / sources 4705 / FOI rows ~1628.
- Wrote: sources (+4); budgets (+6); commitments (+1); leaderboard (+1); entities (+1 nv_aquiris); foi + draft gap_aquiris_nbb_pdf_assets_debt_boot_fee_matrix_l5; progress+top10 md; rq_1960=done + rq_1961 open; loop_state ticks=1960.
- FOI: **ready not sent** (human-gated).
- EVERY-10 done this tick. Next every-10: **1970**. Next: rq_1961 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1960 write OK: EVERY-10 + Aquiris YE2025 Medium omzet 55272688")
