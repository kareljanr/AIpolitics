# tick 1958 — IRE Fleurus parent YE2025 Medium CW+Rovalta (rq_1958 after IRE ELiT)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T15:20:00Z"
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
        "source_id": "src_ire_jr2025_cw",
        "title": "Companyweb IRE parent YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0408449677/nationaal-instituut-voor-radio-elementen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1958; Laatste balansjaar 2025; omzet DROP 73583681; "
            "pnl LOSS -2232791; equity 230520047; bruto DROP 34261391; FTE 223"
        ),
    },
    {
        "source_id": "src_ire_jr2025_rovalta",
        "title": "Rovalta NBB-derived IRE parent YE2025 assets EBITDA debt cash FTE",
        "url": "https://www.rovalta.com/nl/onderneming/0408449677/institut-national-des-radioelements",
        "publisher": "Rovalta (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1958; YE2025 assets 311968419 equity 230520047 liabilities 63962093 "
            "ST debt 63519706 cash 7477505 revenue 73583681 operating LOSS -4752011 "
            "pnl LOSS -2232791 EBITDA DROP 2778810 staff 31014078 FTE 223; "
            "YE2024 assets 332011760 equity 231282955 liabilities 83743899 "
            "revenue 88188241 pnl 8498292; neerlegging listed 21.05.2026 on Pappers"
        ),
    },
    {
        "source_id": "src_ire_kbo_1958",
        "title": "KBO IRE 0408.449.677 Actief SON pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408449677",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1958; Actief Stichting van openbaar nut sinds 20.08.1971; "
            "zetel Avenue de l'Espérance 1 6220 Fleurus; NACE 24.460; "
            "web ire.eu; dual daughter IRE ELiT 0826.980.032 already mined tick1957"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1958 YE2025 statutory Medium CW+Rovalta KBO 0408.449.677 Actief SON; "
    "omzet DROP 73.58m pnl LOSS 2.23m equity 230.52m bruto DROP 34.26m "
    "assets DROP 311.97m EBITDA DROP 2.78m schulden 63.96m cash 7.48m "
    "FTE 223 staff 31.01m; medical radioisotopes Fleurus; ELiT dual mined 1957; "
    "federal BA dual already mapped; FOI gap_ire_nbb_pdf_debt_cash_elit_federal_ba_l5"
)

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "ire_radioelements": {
            "foi_email": "info@ire.eu",
            "foi_postal": "Avenue de l'Espérance 1 6220 Fleurus",
            "website": "https://www.ire.eu",
            "notes": ent_notes,
        },
        "ire": {
            "foi_email": "info@ire.eu",
            "foi_postal": "Avenue de l'Espérance 1 6220 Fleurus",
            "website": "https://www.ire.eu",
            "notes": ent_notes + "; alias of ire_radioelements",
        },
    },
)

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_ire_omzet_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "73583681",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Rovalta NBB-derived omzet statutory",
        "source_id": "src_ire_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 omzet 73583681 DROP -16.56pct vs 88188241; not additive to ELiT/federal BA",
    },
    {
        "budget_id": "bud_ire_pnl_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "-2232791",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Rovalta NBB-derived net PnL",
        "source_id": "src_ire_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 pnl LOSS -2232791 vs +8498292 YE2024; operating LOSS -4752011 distinct",
    },
    {
        "budget_id": "bud_ire_bruto_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "34261391",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto",
        "source_id": "src_ire_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 bruto 34261391 DROP -20.3pct vs 42985817",
    },
    {
        "budget_id": "bud_ire_equity_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "230520047",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Rovalta NBB-derived equity",
        "source_id": "src_ire_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 equity 230520047 DROP -0.33pct vs 231282955; ~73.9pct of assets",
    },
    {
        "budget_id": "bud_ire_assets_jr2025_rovalta",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "311968419",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Rovalta NBB-derived assets",
        "source_id": "src_ire_jr2025_rovalta",
        "confidence": "medium",
        "notes": "tick1958; YE2025 assets 311968419 DROP vs 332011760 YE2024; current assets 178799450",
    },
    {
        "budget_id": "bud_ire_ebitda_jr2025_rovalta",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "2778810",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Rovalta NBB-derived EBITDA",
        "source_id": "src_ire_jr2025_rovalta",
        "confidence": "medium",
        "notes": "tick1958; YE2025 EBITDA 2778810 DROP vs ~10.88m YE2024 Upswitch; ~3.8pct of omzet",
    },
    {
        "budget_id": "bud_ire_schulden_jr2025_rovalta",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "63962093",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Rovalta NBB-derived total liabilities",
        "source_id": "src_ire_jr2025_rovalta",
        "confidence": "medium",
        "notes": "tick1958; YE2025 schulden 63962093 vs 83743899 YE2024; ST ~63519706 LT Unknown pending NBB PDF",
    },
    {
        "budget_id": "bud_ire_cash_jr2025_rovalta",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "7477505",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Rovalta NBB-derived cash and equivalents",
        "source_id": "src_ire_jr2025_rovalta",
        "confidence": "medium",
        "notes": "tick1958; YE2025 cash 7477505 DROP vs 32546491 YE2024",
    },
    {
        "budget_id": "bud_ire_fte_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "223",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW+Rovalta social-balance FTE",
        "source_id": "src_ire_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 FTE 223 flat vs YE2024; staff costs 31014078; ELiT dual separate (tick1957)",
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
    "commitment_id": "comm_ire_jr2025_statutory_omzet",
    "title": "IRE Fleurus parent YE2025 leftover nuclear radioisotopes dual statutory (omzet DROP 73.58m / pnl LOSS 2.23m / assets 311.97m)",
    "entity_id": "ire_radioelements",
    "beneficiary": "Nuclear medicine / radioisotope customers / IRE ELiT dual / federal BA path",
    "legal_basis": "Stichting van openbaar nut IRE; KBO 0408.449.677; NBB neerlegging; federal BA dual already mapped",
    "decision_date": "2026-05-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "311968419",
    "cash_by_year": (
        "2025:omzet=73583681;bruto=34261391;pnl=-2232791;operating=-4752011;"
        "assets=311968419;equity=230520047;ebitda=2778810;schulden=63962093;"
        "cash=7477505;staff=31014078;fte=223"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0408449677/nationaal-instituut-voor-radio-elementen",
    "stated_goal": "Produce radioisotopes for nuclear medicine / public health",
    "cut_option": "FOI NBB PDF + debt/cash split + ELiT consol recon + federal BA recon",
    "source_id": "src_ire_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>JR2025_statutory_L5",
    "notes": (
        "tick1958; Medium CW+Rovalta YE2025 statutory after IRE ELiT; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo IRE ELiT/FANC/SCK CEN/EURIDICE/"
        "BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_ire_omzet_drop_73_58m_pnl_loss_2_23m_assets_311_97m_jr2025",
    "name": "IRE Fleurus parent omzet DROP 73.58m / pnl LOSS 2.23m / assets 311.97m (statutory YE2025)",
    "level": "L5",
    "type": "nuclear_radioisotopes_dual",
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>JR2025_statutory_L5",
    "annual_cost_eur": "73583681",
    "total_cost_eur": "311968419",
    "tco_notes": (
        "statutory omzet DROP 73583681 bruto DROP 34261391 pnl LOSS -2232791 "
        "operating LOSS -4752011 assets DROP 311968419 equity 230520047 "
        "EBITDA DROP 2778810 schulden 63962093 cash DROP 7477505 fte 223; "
        "SON medical isotopes; ELiT dual mined 1957; federal BA dual separate; NBB PDF unresolved"
    ),
    "confidence": "medium",
    "source_id": "src_ire_jr2025_cw",
    "beneficiaries": "Nuclear medicine / hospitals / IRE ELiT dual",
    "stated_goal": "Medical radioisotope production public-interest foundation",
    "measured_outcome": (
        "CW+Rovalta YE2025 live; omzet -16.6pct turn to LOSS; cash DROP; "
        "primary NBB PDF + ELiT consol recon + federal BA recon still FOI"
    ),
    "absurdity_score": "5.0",
    "cost_score": "7.0",
    "difficulty": "3.5",
    "priority_index": "6.0",
    "cut_proposal": "Publish NBB PDF + debt/cash detail + ELiT consolidation recon + federal BA outturn recon",
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1958; Medium CW+Rovalta; leftover nuclear radioisotopes parent after IRE ELiT; "
        "not TE-additive pure-waste top10; prior passive/partnership lbs remain"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_ire_nbb_pdf_debt_cash_elit_federal_ba_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>nbb_pdf_elit_ba_L5",
    "entity_id": "ire_radioelements",
    "what_is_missing": (
        "NBB deposit PDF body for YE2025; LT/ST debt and cash-flow detail recon to "
        "schulden 63962093 / cash 7477505; IRE ELiT consolidation perimeter recon; "
        "federal BA partnership/passive/invest outturn vs statutory PnL"
    ),
    "why_it_matters": (
        "SON medical radioisotopes with 73.58m omzet / 311.97m assets / LOSS turn — "
        "absolute statutory now Medium but primary PDF + daughter ELiT recon + federal BA dual still opaque"
    ),
    "priority": "8",
    "recipient_body": "IRE / Institut national des Radioéléments (cc FOD Economie AD Energie / IRE ELiT)",
    "recipient_email": "info@ire.eu",
    "recipient_postal": "Avenue de l'Espérance 1 6220 Fleurus",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ire_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_ire_omzet_drop_73_58m_pnl_loss_2_23m_assets_311_97m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1958; human-send only; Medium CW+Rovalta; next every-10 1960",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — IRE Fleurus parent (NBB PDF / debt-cash / ELiT / federal BA)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** IRE / Nationaal Instituut voor Radio-elementen — KBO **0408.449.677** (SON)  
**recipient:** info@ire.eu / Avenue de l'Espérance 1 6220 Fleurus / cc FOD Economie AD Energie · IRE ELiT  
**sources:** [Companyweb](https://www.companyweb.be/nl/0408449677/nationaal-instituut-voor-radio-elementen) · [Rovalta NBB-derived](https://www.rovalta.com/nl/onderneming/0408449677/institut-national-des-radioelements) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408449677) · [ire.eu](https://www.ire.eu)  
**tick:** 1958 (NOT every-10; next every-10 is **1960**)  
**confidence on table euros:** Medium (NBB-derived CW + Rovalta; primary deposit PDF unresolved)

## Context

- Sourced YE **01.01.2025–31.12.2025**: omzet **EUR73,583,681** (**DROP -16.56%**); bruto **EUR34,261,391**; pnl **LOSS EUR-2,232,791**; operating **LOSS EUR-4,752,011**; assets **EUR311,968,419** (**DROP**); equity **EUR230,520,047**; EBITDA **EUR2,778,810** (**DROP**); schulden **EUR63,962,093**; cash **EUR7,477,505** (**DROP**); staff **EUR31,014,078**; FTE **223**.
- Stichting van openbaar nut; medical radioisotopes Fleurus; dual daughter **IRE ELiT** (KBO 0826.980.032) already mined tick1957; federal BA partnership/passive/invest already mapped earlier ticks.
- Preferred leftover paths stalled: AGB Bornem **JR2024-only**; FARO NBB YE2025 unpublished; AIESH/REW **YE2024**. Do not redo IRE ELiT / FANC / SCK CEN / EURIDICE / BRUGEL / Hydria / Vivaqua / Belgoprocess / Laborelec / CILE / NIRAS / Bel V.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Institut national des Radioéléments (IRE)
t.a.v. openbaarheid / informatieambtenaar
Avenue de l'Espérance 1
6220 Fleurus

cc: FOD Economie — AD Energie
cc: IRE ELiT NV

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
schulden-/cashdetail, ELiT-consolidatie en federale BA-reconciliatie
(KBO 0408.449.677)

Geachte,

Op grond van toepasselijke openbaarheid vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF).
2. Schuldenrooster LT/ST reconcilieerbaar met schulden EUR63.962.093
   en cashflow vs cash EUR7.477.505 (vs YE2024).
3. Consolidatie-/deelnemingsperimeter IRE ELiT (KBO 0826.980.032)
   t.o.v. statutaire IRE-cijfers 2025.
4. Reconciliatie federale BA-paden (partnership / passive / invest)
   vs statutaire omzet/PnL 2024-2025.
5. Toelichting omzet DROP en turnaround naar verlies 2025.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (IRE SON Fleurus)
- [x] Concrete documenten (NBB PDF + debt/cash + ELiT + federal BA)
- [x] Periode en bedragen gevraagd
- [x] Meerjarigheid / ELiT dual expliciet
- [ ] Contactgegevens verzoeker (human)
- [x] foi_queue.csv ready — **NOT sent**
""",
        encoding="utf-8",
    )

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1958": {
            "title": "leftover dual hole-fill after IRE ELiT — IRE Fleurus parent YE2025 Medium",
            "status": "done",
            "hierarchy_target": "Belgie>Federaal>Nucleair>IRE>JR2025_L5",
            "entity_id": "ire_radioelements",
            "updated_utc": TS,
            "instructions": (
                "Completed: IRE Fleurus parent leftover nuclear radioisotopes dual after IRE ELiT; "
                "KBO 0408.449.677; YE2025 Medium CW+Rovalta; sourced euros omzet DROP 73583681 "
                "pnl LOSS -2232791 equity 230520047 bruto DROP 34261391 assets DROP 311968419 "
                "EBITDA DROP 2778810 schulden 63962093 cash DROP 7477505 FTE 223; "
                "FOI ready not sent"
            ),
            "notes": (
                "tick1958 IRE parent after ELiT; Medium CW+Rovalta omzet DROP 73.58m pnl LOSS 2.23m "
                "assets DROP 311.97m equity 230.52m; FOI ready not sent; AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_1959; next every-10 1960"
            ),
        }
    },
)

with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    rq_rows = list(csv.DictReader(f))
    rq_fields = list(rq_rows[0].keys()) if rq_rows else []
    existing_rq = {r["task_id"] for r in rq_rows}

if "rq_1959" not in existing_rq:
    rq_1959 = {
        "task_id": "rq_1959",
        "title": "leftover dual hole-fill after IRE Fleurus parent",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 1959 after 1958 IRE Fleurus parent statutory. Prefer leftover AGB/APB if JR2025 PDF live, "
            "else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/"
            "energy. Do NOT redo IRE parent, IRE ELiT, FANC, SCK CEN, EURIDICE, BRUGEL, Hydria, "
            "Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synatom, Atrias, AIEG, "
            "Synergrid, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": "spawned after tick1958; next every-10 1960",
    }
    row = {k: rq_1959.get(k, "") for k in rq_fields}
    append_csv(DATA / "research_queue.csv", [row])

update_csv_rows(
    DATA / "loop_state.csv",
    "state_id",
    {
        "main": {
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": TS,
            "last_unit_id": "rq_1958",
            "ticks_completed": "1958",
            "paused": "no",
            "notes": (
                "tick1958 leftover IRE Fleurus parent 0408.449.677 Medium CW+Rovalta "
                "(omzet DROP 73.58m pnl LOSS 2.23m assets DROP 311.97m equity 230.52m "
                "schulden 63.96m cash DROP 7.48m FTE 223); AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_1959; next every-10 1960; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""
## Tick 1958 - {TS} - rq_1958 IRE Fleurus parent (omzet DROP 73.58m / pnl LOSS 2.23m / assets 311.97m / Medium)

- Unit: **rq_1958** leftover dual after concurrent **rq_1957 IRE ELiT** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024** (narrative JV2025 only; NBB YE2025 unpublished); AIESH still **YE2024**; REW still **YE2024**. Took leftover **IRE Fleurus parent** statutory YE2025 (KBO **0408.449.677**; Avenue de l'Espérance 1 Fleurus; SON medical radioisotopes; **IRE ELiT dual** already mined 1957). Do not redo IRE ELiT/FANC/SCK CEN/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92.
- Found: Companyweb+Rovalta YE2025 — omzet **EUR73,583,681** DROP -16.56%; bruto **EUR34,261,391**; pnl **LOSS EUR-2,232,791**; operating **LOSS EUR-4,752,011**; assets **EUR311,968,419** DROP; equity **EUR230,520,047**; EBITDA **EUR2,778,810** DROP; schulden **EUR63,962,093**; cash **EUR7,477,505** DROP; staff **EUR31,014,078**; FTE **223**. Medium confidence (NBB-derived aggregators; primary deposit PDF unresolved). Upswitch still YE2024-only for parent.
- Wrote: sources (+3); budgets (+9 statutory); commitments (+1); leaderboard (+1); entities (updated ire_radioelements + ire); foi + draft gap_ire_nbb_pdf_debt_cash_elit_federal_ba_l5; rq_1958=done + rq_1959 open; loop_state ticks=1958.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1960**). Next: rq_1959 (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / unused water-DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1958 write OK: IRE Fleurus parent YE2025 Medium")
