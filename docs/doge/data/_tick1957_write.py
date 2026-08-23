# tick 1957 — IRE ELiT YE2025 Medium CW+Upswitch+SBM (rq_1957 after FANC)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T15:00:00Z"
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
        "source_id": "src_ire_elit_jr2025_cw",
        "title": "Companyweb IRE ELiT YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0826980032/ire-elit",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1957; Laatste balansjaar 2025; neerlegging 16.06.2026; "
            "omzet 44587904 JUMP +17.36pct; pnl JUMP 6872467; equity JUMP 14178731; "
            "bruto 14727315; FTE 54"
        ),
    },
    {
        "source_id": "src_ire_elit_jr2025_upswitch",
        "title": "Upswitch NBB/CBSO IRE ELiT YE2025 assets operating EBITDA",
        "url": "https://www.upswitch.app/en/companies/be/ire-elit-0826980032",
        "publisher": "Upswitch (NBB/CBSO-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1957; YE2025 revenue 44587904 / assets 19493610 / operating 7555995 / "
            "EBITDA 8504126 / equity 14178731 / depr 948131; YE2024 revenue 37992619 / "
            "assets 19471529 / operating 5753835 / EBITDA 6667102; archive 2026-06-30"
        ),
    },
    {
        "source_id": "src_ire_elit_jr2025_sbm",
        "title": "Staatsbladmonitor IRE ELiT YE2025 statutory table",
        "url": "https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0826980032",
        "publisher": "Staatsbladmonitor (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1957; YE2025 assets 19493610 omzet 44587904 bedrijfswinst 7555995 "
            "taxes 176057 equity 14178731 schulden 4450641; neerlegging 2026-06-16"
        ),
    },
    {
        "source_id": "src_ire_elit_kbo_1957",
        "title": "KBO IRE ELiT 0826.980.032 Actief NV pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0826980032",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1957; Actief NV sinds 28.06.2010; zetel Avenue de l'Esperance 1 6220 Fleurus; "
            "IRE FUP daughter radiopharma; NACE 21.20; dual parent IRE 0408.449.677 YE2024-only"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    ent_fields = None
    for row in csv.DictReader(f):
        if ent_fields is None:
            ent_fields = list(row.keys())
        existing_ent.add(row.get("entity_id") or "")

ent_notes = (
    "tick1957 YE2025 Medium CW+Upswitch+SBM KBO 0826.980.032 Actief NV; "
    "omzet JUMP 44.59m pnl JUMP 6.87m equity JUMP 14.18m bruto 14.73m assets 19.49m "
    "operating 7.56m EBITDA JUMP 8.50m schulden 4.45m FTE 54; "
    "IRE FUP radiopharma daughter; FOI gap_ire_elit_nbb_pdf_parent_tp_dividend_l5; "
    "parent IRE 0408.449.677 still YE2024; group marketing CA 118m distinct"
)

if "nv_ire_elit" not in existing_ent:
    ent_row = {
        "entity_id": "nv_ire_elit",
        "name_nl": "IRE ELiT NV",
        "name_fr": "IRE ELiT SA",
        "name_en": "IRE ELiT (IRE radiopharma daughter)",
        "level": "company",
        "parent_id": "ire_radioelements",
        "community_language": "fr",
        "website": "https://www.ire.eu",
        "foi_email": "info@ire.eu",
        "foi_postal": "Avenue de l'Esperance 1 6220 Fleurus",
        "notes": ent_notes,
    }
    append_csv(DATA / "entities.csv", [{k: ent_row.get(k, "") for k in ent_fields}])
else:
    update_csv_rows(DATA / "entities.csv", "entity_id", {"nv_ire_elit": {"notes": ent_notes, "foi_email": "info@ire.eu", "foi_postal": "Avenue de l'Esperance 1 6220 Fleurus", "website": "https://www.ire.eu"}})

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "ire_radioelements": {
            "notes": (
                "tick1957 note: daughter IRE ELiT NV YE2025 mined Medium; parent FUP 0408.449.677 "
                "still YE2024 on NBB (data.be last YE2024 filed 28.05.2025); group site claims CA 118m 2025"
            )
        },
        "ire": {
            "notes": (
                "tick1957: operational daughter nv_ire_elit YE2025 omzet 44.59m; parent statutory YE2025 unpublished; "
                "Medical isotopes uranium; tick759 seed"
            )
        },
    },
)

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_ire_elit_omzet_jr2025_statutory",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "44587904",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_ire_elit_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1957; YE2025 omzet 44587904 JUMP +17.36pct vs 37992619",
    },
    {
        "budget_id": "bud_ire_elit_pnl_jr2025_statutory",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "6872467",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived net PnL",
        "source_id": "src_ire_elit_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1957; YE2025 pnl JUMP 6872467 +27.73pct vs 5380255; operating Upswitch 7555995 distinct",
    },
    {
        "budget_id": "bud_ire_elit_bruto_jr2025_statutory",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "14727315",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto",
        "source_id": "src_ire_elit_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1957; YE2025 bruto 14727315 JUMP +16.68pct vs 12621690",
    },
    {
        "budget_id": "bud_ire_elit_equity_jr2025_statutory",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "14178731",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Upswitch NBB-derived equity",
        "source_id": "src_ire_elit_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1957; YE2025 equity JUMP 14178731 +94.06pct vs 7306265; ~73pct of assets",
    },
    {
        "budget_id": "bud_ire_elit_assets_jr2025_upswitch",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "19493610",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch+SBM NBB-derived assets",
        "source_id": "src_ire_elit_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1957; YE2025 assets 19493610 vs 19471529 YE2024; flat BS / equity thickening",
    },
    {
        "budget_id": "bud_ire_elit_operating_jr2025_upswitch",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "7555995",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived operating / SBM bedrijfswinst",
        "source_id": "src_ire_elit_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1957; YE2025 operating 7555995 vs 5753835 YE2024",
    },
    {
        "budget_id": "bud_ire_elit_ebitda_jr2025_upswitch",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "8504126",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Upswitch NBB-derived EBITDA",
        "source_id": "src_ire_elit_jr2025_upswitch",
        "confidence": "medium",
        "notes": "tick1957; YE2025 EBITDA 8504126 JUMP vs 6667102; ~19.1pct of omzet",
    },
    {
        "budget_id": "bud_ire_elit_schulden_jr2025_sbm",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "4450641",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "SBM NBB-derived schulden 17/49",
        "source_id": "src_ire_elit_jr2025_sbm",
        "confidence": "medium",
        "notes": "tick1957; YE2025 schulden 4450641 DROP vs 11384841 YE2024; LT/ST Unknown pending NBB PDF",
    },
    {
        "budget_id": "bud_ire_elit_fte_jr2025_statutory",
        "entity_id": "nv_ire_elit",
        "year": "2025",
        "amount_eur": "54",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_ire_elit_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1957; YE2025 FTE 54 vs 49 YE2024; group site claims ~300 IRE+ELiT combined",
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
    "commitment_id": "comm_ire_elit_jr2025_statutory_omzet",
    "title": "IRE ELiT YE2025 leftover nuclear radiopharma dual statutory (omzet JUMP 44.59m / equity JUMP 14.18m)",
    "entity_id": "nv_ire_elit",
    "beneficiary": "Nuclear medicine / IRE FUP parent / Ge-68 Ga-68 radiopharma markets",
    "legal_basis": "NV daughter of IRE FUP 0408.449.677; NBB neerlegging; wet openbaarheid bestuur",
    "decision_date": "2026-06-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "19493610",
    "cash_by_year": (
        "2025:omzet=44587904;bruto=14727315;pnl=6872467;operating=7555995;"
        "assets=19493610;equity=14178731;ebitda=8504126;schulden=4450641;fte=54"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0826980032/ire-elit",
    "stated_goal": "Radiopharmaceutical innovation / cancer imaging therapy supply",
    "cut_option": "FOI NBB PDF + parent TP/dividend + group CA 118m recon + IRE passive dual",
    "source_id": "src_ire_elit_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>ELiT>JR2025_statutory_L5",
    "notes": (
        "tick1957; Medium CW+Upswitch+SBM YE2025 after FANC; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo FANC/SCK CEN/EURIDICE/BRUGEL/"
        "Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synatom"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_ire_elit_omzet_jump_44_59m_equity_jump_14_18m_jr2025",
    "name": "IRE ELiT omzet JUMP 44.59m / equity JUMP 14.18m / assets 19.49m (statutory YE2025)",
    "level": "L5",
    "type": "nuclear_radiopharma_dual",
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>ELiT>JR2025_statutory_L5",
    "annual_cost_eur": "44587904",
    "total_cost_eur": "19493610",
    "tco_notes": (
        "statutory omzet 44587904 JUMP bruto 14727315 pnl JUMP 6872467 operating 7555995 "
        "assets 19493610 equity JUMP 14178731 EBITDA JUMP 8504126 schulden DROP 4450641 fte 54; "
        "parent IRE YE2025 unpublished; group marketing CA 118m conflict class"
    ),
    "confidence": "medium",
    "source_id": "src_ire_elit_jr2025_cw",
    "beneficiaries": "Nuclear medicine patients / IRE FUP / radiopharma markets",
    "stated_goal": "Radiopharmaceutical products Ge-68/Ga-68 and related",
    "measured_outcome": (
        "CW+Upswitch+SBM YE2025 live; equity nearly doubled; debt DROP; "
        "primary NBB PDF + parent TP unresolved"
    ),
    "absurdity_score": "4.0",
    "cost_score": "6.5",
    "difficulty": "3.5",
    "priority_index": "5.5",
    "cut_proposal": "Publish NBB PDF + parent transfer-pricing/dividend + reconcile group CA 118m",
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1957; Medium CW+Upswitch+SBM; leftover nuclear radiopharma dual after FANC; "
        "not TE-additive pure-waste top10; commercial NV under public FUP parent"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_ire_elit_nbb_pdf_parent_tp_dividend_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>ELiT>nbb_pdf_parent_tp_L5",
    "entity_id": "nv_ire_elit",
    "what_is_missing": (
        "NBB deposit PDF body YE2025; parent IRE FUP transfer-pricing / recharge / dividend matrix; "
        "reconcile group marketing CA EUR118m vs ELiT statutory 44.59m + parent; LT/ST debt split; "
        "IRE parent YE2025 filing status"
    ),
    "why_it_matters": (
        "Public-utility nuclear radioisotope stack: commercial NV daughter with 44.59m omzet / "
        "equity JUMP to 14.18m under IRE FUP — parent YE2025 and intra-group flows opaque"
    ),
    "priority": "8",
    "recipient_body": "IRE ELiT NV (cc IRE FUP)",
    "recipient_email": "info@ire.eu",
    "recipient_postal": "Avenue de l'Esperance 1 6220 Fleurus",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ire_elit_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_ire_elit_omzet_jump_44_59m_equity_jump_14_18m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1957; human-send only; Medium CW+Upswitch+SBM; next every-10 1960",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — IRE ELiT (NBB PDF / parent TP / dividend / group CA)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** IRE ELiT NV — KBO **0826.980.032** (daughter of IRE FUP **0408.449.677**)  
**recipient:** info@ire.eu / Avenue de l'Espérance 1 6220 Fleurus / cc IRE FUP  
**sources:** [Companyweb](https://www.companyweb.be/nl/0826980032/ire-elit) · [Upswitch](https://www.upswitch.app/en/companies/be/ire-elit-0826980032) · [Staatsbladmonitor](https://www.staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0826980032) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0826980032) · [ire.eu](https://www.ire.eu)  
**tick:** 1957 (NOT every-10; next every-10 is **1960**)  
**confidence on table euros:** Medium (NBB-derived CW + Upswitch + SBM; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025**: omzet **EUR44,587,904** (**JUMP +17.36%**); bruto **EUR14,727,315**; pnl **EUR6,872,467**; operating **EUR7,555,995**; assets **EUR19,493,610**; equity **EUR14,178,731** (**JUMP +94%**); EBITDA **EUR8,504,126**; schulden **EUR4,450,641** (**DROP**); FTE **54**.
- Parent IRE FUP still **YE2024** on public NBB listings; group website claims combined CA **EUR118m** 2025 (marketing class — not statutory ELiT).
- Preferred leftover paths stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo FANC / SCK CEN / EURIDICE / Bel V / NIRAS / Belgoprocess.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: IRE ELiT NV
t.a.v. openbaarheid / information officer
Avenue de l'Espérance 1
6220 Fleurus

cc: Institut National des Radioéléments (IRE FUP)
Avenue de l'Espérance 1
6220 Fleurus

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
moeder-dochter facturatie/dividend en groeps-CA (KBO 0826.980.032)

Geachte,

Op grond van toepasselijke openbaarheid vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF).
2. Transfer-pricing / recharge / dividendmatrix met moeder IRE FUP 2025.
3. Schuldenrooster LT/ST reconcilieerbaar met schulden EUR4.450.641.
4. Reconciliatie groepscommunicatie CA EUR118m vs statutaire ELiT
   EUR44.587.904 (+ moeder indien YE2025).
5. Status neerlegging jaarrekening 2025 van IRE FUP (0408.449.677).

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (IRE ELiT + cc parent)
- [x] Concrete documenten (NBB PDF + TP/dividend + group recon)
- [x] Periode en bedragen gevraagd
- [x] Meerjarigheid / parent dual expliciet
- [ ] Contactgegevens verzoeker (human)
- [x] foi_queue.csv ready — **NOT sent**
""",
        encoding="utf-8",
    )

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1957": {
            "title": "leftover dual hole-fill after FANC — IRE ELiT YE2025 Medium",
            "status": "done",
            "hierarchy_target": "Belgie>Federaal>Nucleair>IRE>ELiT>JR2025_L5",
            "entity_id": "nv_ire_elit",
            "updated_utc": TS,
            "instructions": (
                "Completed: IRE ELiT leftover nuclear radiopharma dual after FANC; KBO 0826.980.032; "
                "YE2025 Medium CW+Upswitch+SBM; sourced euros omzet JUMP 44587904 pnl JUMP 6872467 "
                "equity JUMP 14178731 assets 19493610 EBITDA JUMP 8504126 schulden DROP 4450641 FTE 54; "
                "FOI ready not sent"
            ),
            "notes": (
                "tick1957 IRE ELiT after FANC; Medium CW+Upswitch+SBM omzet JUMP 44.59m equity JUMP 14.18m; "
                "FOI ready not sent; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1958; next every-10 1960"
            ),
        }
    },
)

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []
    existing_rq = {r["task_id"] for r in rq_rows}

if "rq_1958" not in existing_rq:
    rq_1958 = {
        "task_id": "rq_1958",
        "title": "leftover dual hole-fill after IRE ELiT",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 1958 after 1957 IRE ELiT. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
            "NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/nuclear "
            "(IRE parent FUP if YE2025 appears). Do NOT redo IRE ELiT, FANC, SCK CEN, EURIDICE, BRUGEL, "
            "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synatom, Atrias, AIEG, "
            "Synergrid, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": "spawned after tick1957; next every-10 1960",
    }
    append_csv(DATA / "research_queue.csv", [{k: rq_1958.get(k, "") for k in rq_fields}])

update_csv_rows(
    DATA / "loop_state.csv",
    "state_id",
    {
        "main": {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1957",
            "ticks_completed": "1957",
            "paused": "no",
            "notes": (
                "tick1957 leftover IRE ELiT 0826.980.032 Medium CW+Upswitch+SBM "
                "(omzet JUMP 44.59m pnl JUMP 6.87m equity JUMP 14.18m assets 19.49m "
                "schulden DROP 4.45m FTE 54); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                "next rq_1958; next every-10 1960; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""
## Tick 1957 - {TS} - rq_1957 IRE ELiT (omzet JUMP 44.59m / equity JUMP 14.18m / Medium)

- Unit: **rq_1957** leftover dual after concurrent **rq_1956 FANC** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024**. Took leftover **IRE ELiT NV** (KBO **0826.980.032**; Avenue de l'Espérance 1 Fleurus; IRE FUP radiopharma daughter; YE2025 live CW). Do not redo FANC/SCK CEN/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synatom.
- Found: Companyweb+Upswitch+SBM YE2025 — omzet **EUR44,587,904** JUMP +17.36%; bruto **EUR14,727,315**; pnl **EUR6,872,467**; operating **EUR7,555,995**; assets **EUR19,493,610**; equity **EUR14,178,731** JUMP +94%; EBITDA **EUR8,504,126**; schulden **EUR4,450,641** DROP; FTE **54**. Parent IRE FUP still YE2024. Medium confidence.
- Wrote: sources (+4); budgets (+9); commitments (+1); leaderboard (+1); entities (+1 nv_ire_elit + parent notes); foi + draft gap_ire_elit_nbb_pdf_parent_tp_dividend_l5; rq_1957=done + rq_1958 open; loop_state ticks=1957.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1960**). Next: rq_1958 (AGB/FARO-if-YE2025 / AIESH-REW / IRE-parent-if-YE2025 / unused water-DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1957 write OK: IRE ELiT YE2025 Medium")
