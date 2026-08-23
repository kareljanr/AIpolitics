# tick 1958 — IRE FUP parent YE2025 Medium CW+EN twin+KBO (rq_1958 after IRE ELiT)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T15:30:00Z"
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
        "source_id": "src_ire_fup_jr2025_cw",
        "title": "Companyweb IRE FUP YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0408449677/nationaal-instituut-voor-radio-elementen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1958; Laatste balansjaar 2025; omzet 73583681 DROP -16.56pct; "
            "pnl LOSS -2232791; equity 230520047; bruto 34261391; FTE 223; "
            "Groot; KBO 0408.449.677 SON/FUP"
        ),
    },
    {
        "source_id": "src_ire_fup_jr2025_cw_en",
        "title": "Companyweb EN twin IRE FUP YE2025 turnover equity",
        "url": "https://www.companyweb.be/en/0408449677/national-institute-for-radioelements",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1958; Last balance sheet year 2025; Turnover 73583681; "
            "Profit/Loss -2232791; Equity 230520047; Gross margin 34261391; FTE 223"
        ),
    },
    {
        "source_id": "src_ire_fup_kbo_1958",
        "title": "KBO IRE FUP 0408.449.677 Actief SON pointer",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408449677",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1958; Actief Stichting van openbaar nut sinds 27.12.2004; "
            "zetel Avenue de l'Esperance 1 Zoning 6220 Fleurus; NACE 24.460/38.320; "
            "aanbestedende overheid; NBB consult SPA for deposit PDF"
        ),
    },
    {
        "source_id": "src_ire_group_site_ca118m_1958",
        "title": "ire.eu group marketing turnover 118m 2025",
        "url": "https://www.ire.eu/en/",
        "publisher": "IRE / IRE ELiT (marketing)",
        "accessed_date": "2026-08-23",
        "source_class": "company_website",
        "notes": (
            "tick1958; site claims Turnover in 2025 EUR118m / ~300 employees; "
            "reconciles approx parent CW omzet 73.58m + ELiT 44.59m = 118.17m"
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
    "tick1958 YE2025 Medium CW NL+EN + Strong KBO 0408.449.677 Actief SON/FUP; "
    "omzet DROP 73.58m pnl LOSS 2.23m equity 230.52m bruto 34.26m FTE 223; "
    "assets/debt/cash Unknown (Upswitch lag YE2024-only; Pappers cash conflict); "
    "daughter nv_ire_elit YE2025 omzet 44.59m; group site CA 118m ~ parent+ELiT; "
    "FOI gap_ire_fup_nbb_pdf_assets_debt_elit_tp_l5; preferred AGB Bornem/FARO/AIESH/REW still YE2024"
)

update_csv_rows(
    DATA / "entities.csv",
    "entity_id",
    {
        "ire_radioelements": {
            "notes": ent_notes,
            "foi_email": "generalmail@ire.be",
            "foi_postal": "Avenue de l'Esperance 1 Zoning 6220 Fleurus",
            "website": "https://www.ire.eu",
        },
        "ire": {
            "notes": (
                "tick1958 parent FUP YE2025 Medium omzet DROP 73.58m pnl LOSS 2.23m; "
                "daughter nv_ire_elit YE2025 omzet 44.59m; group marketing CA 118m reconciled approx; "
                "Medical isotopes uranium; tick759 seed"
            )
        },
        "nv_ire_elit": {
            "notes": (
                "tick1957 YE2025 Medium CW+Upswitch+SBM KBO 0826.980.032; "
                "omzet JUMP 44.59m pnl JUMP 6.87m equity JUMP 14.18m; "
                "tick1958 note: parent IRE FUP YE2025 now mined Medium omzet DROP 73.58m"
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
        "budget_id": "bud_ire_fup_omzet_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "73583681",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet statutory",
        "source_id": "src_ire_fup_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 omzet 73583681 DROP -16.56pct vs 88188241",
    },
    {
        "budget_id": "bud_ire_fup_pnl_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "-2232791",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived Winst/Verlies",
        "source_id": "src_ire_fup_jr2025_cw",
        "confidence": "medium",
        "notes": (
            "tick1958; YE2025 pnl LOSS -2232791 vs profit 8498292 YE2024; "
            "Pappers claims distinct net -1.26m — FOI NBB PDF to resolve line labels"
        ),
    },
    {
        "budget_id": "bud_ire_fup_bruto_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "34261391",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived bruto/gross margin",
        "source_id": "src_ire_fup_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 bruto 34261391 DROP -20.3pct vs 42985817",
    },
    {
        "budget_id": "bud_ire_fup_equity_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "230520047",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived equity",
        "source_id": "src_ire_fup_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 equity 230520047 flat -0.33pct vs 231282955",
    },
    {
        "budget_id": "bud_ire_fup_fte_jr2025_statutory",
        "entity_id": "ire_radioelements",
        "year": "2025",
        "amount_eur": "223",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": "src_ire_fup_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1958; YE2025 FTE 223 flat vs 223 YE2024; group site ~300 with ELiT",
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
    "commitment_id": "comm_ire_fup_jr2025_statutory_omzet",
    "title": "IRE FUP YE2025 leftover nuclear parent dual statutory (omzet DROP 73.58m / pnl LOSS 2.23m)",
    "entity_id": "ire_radioelements",
    "beneficiary": "Nuclear medicine Mo-99/Tc-99m supply / IRE ELiT daughter / federal Energy tutelle",
    "legal_basis": "Stichting van openbaar nut / FUP; NBB neerlegging; wet openbaarheid bestuur",
    "decision_date": "2026-05-21",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "230520047",
    "cash_by_year": (
        "2025:omzet=73583681;bruto=34261391;pnl=-2232791;"
        "equity=230520047;fte=223;assets=Unknown;debt=Unknown"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0408449677/nationaal-instituut-voor-radio-elementen",
    "stated_goal": "Radioisotope production purification for nuclear medicine and environment",
    "cut_option": "FOI NBB PDF + assets/debt/cash + ELiT TP/dividend + group CA recon",
    "source_id": "src_ire_fup_jr2025_cw",
    "confidence": "medium",
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>FUP>JR2025_statutory_L5",
    "notes": (
        "tick1958; Medium CW NL+EN after IRE ELiT; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo ELiT/FANC/SCK CEN/"
        "EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_ire_fup_omzet_drop_73_58m_pnl_loss_2_23m_jr2025",
    "name": "IRE FUP omzet DROP 73.58m / pnl LOSS 2.23m / equity 230.52m (statutory YE2025)",
    "level": "L5",
    "type": "nuclear_radioisotope_parent_dual",
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>FUP>JR2025_statutory_L5",
    "annual_cost_eur": "73583681",
    "total_cost_eur": "230520047",
    "tco_notes": (
        "statutory omzet 73583681 DROP bruto 34261391 pnl LOSS -2232791 "
        "equity 230520047 fte 223; assets/debt Unknown; daughter ELiT omzet 44.59m; "
        "group marketing CA 118m ~ parent+ELiT"
    ),
    "confidence": "medium",
    "source_id": "src_ire_fup_jr2025_cw",
    "beneficiaries": "Nuclear medicine patients / IRE ELiT / federal Energy tutelle",
    "stated_goal": "Radioisotope production for diagnosis/therapy",
    "measured_outcome": (
        "CW NL+EN YE2025 live after ELiT daughter; turnover DROP and LOSS turnaround; "
        "primary NBB PDF + BS opacity unresolved"
    ),
    "absurdity_score": "4.5",
    "cost_score": "7.0",
    "difficulty": "3.5",
    "priority_index": "6.0",
    "cut_proposal": "Publish NBB PDF + BS (assets/debt/cash) + ELiT transfer-pricing/dividend matrix",
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1958; Medium CW; leftover nuclear parent dual after IRE ELiT; "
        "not TE-additive pure-waste top10; public FUP with commercial daughter"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_ire_fup_nbb_pdf_assets_debt_elit_tp_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Belgie>Federaal>Nucleair>IRE>FUP>nbb_pdf_assets_debt_tp_L5",
    "entity_id": "ire_radioelements",
    "what_is_missing": (
        "NBB deposit PDF body YE2025 (Pappers lists Comptes sociaux 2025 dated 21.05.2026); "
        "assets / debt LT-ST / cash exact; reconcile CW Winst/Verlies -2.23m vs Pappers net -1.26m; "
        "transfer-pricing / recharge / dividend matrix with daughter IRE ELiT; "
        "federal Energy tutelle / BA passive-waste dual reconciliation"
    ),
    "why_it_matters": (
        "Public-utility nuclear radioisotope FUP: omzet DROP to 73.58m and LOSS 2.23m under "
        "Energy tutelle while commercial daughter ELiT JUMP 44.59m — BS and intra-group flows opaque"
    ),
    "priority": "8",
    "recipient_body": "IRE FUP / Institut National des Radioelements (cc IRE ELiT)",
    "recipient_email": "generalmail@ire.be",
    "recipient_postal": "Avenue de l'Esperance 1 Zoning 6220 Fleurus",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_ire_fup_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_ire_fup_omzet_drop_73_58m_pnl_loss_2_23m_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1958; human-send only; Medium CW; next every-10 1960",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — IRE FUP (NBB PDF / assets-debt-cash / ELiT TP)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** Nationaal Instituut voor Radio-elementen (IRE FUP) — KBO **0408.449.677**  
**recipient:** generalmail@ire.be / Avenue de l'Espérance 1 Zoning 6220 Fleurus / cc IRE ELiT  
**sources:** [Companyweb NL](https://www.companyweb.be/nl/0408449677/nationaal-instituut-voor-radio-elementen) · [Companyweb EN](https://www.companyweb.be/en/0408449677/national-institute-for-radioelements) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0408449677) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0408449677) · [ire.eu](https://www.ire.eu/en/)  
**tick:** 1958 (NOT every-10; next every-10 is **1960**)  
**confidence on table euros:** Medium (NBB-derived CW NL+EN; primary deposit PDF unresolved; assets/debt/cash Unknown)

## Context

- Sourced YE **01.01.2025–31.12.2025**: omzet **EUR73,583,681** (**DROP −16.56%**); bruto **EUR34,261,391**; pnl **LOSS EUR−2,232,791**; equity **EUR230,520,047**; FTE **223**.
- Daughter IRE ELiT YE2025 omzet **EUR44,587,904** (tick1957). Group website claims combined CA **EUR118m** ≈ 73.58+44.59.
- Preferred leftover paths stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo ELiT / FANC / SCK CEN / EURIDICE / Bel V / NIRAS / Belgoprocess / Vivaqua / Hydria / BRUGEL.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: Institut National des Radioéléments (IRE FUP)
t.a.v. openbaarheid / information officer
Avenue de l'Espérance 1
Zoning
6220 Fleurus

cc: IRE ELiT NV
Avenue de l'Espérance 1
6220 Fleurus

Betreft: Verzoek om openbaarmaking — NBB-jaarrekening 2025,
balansposten en moeder-dochter facturatie (KBO 0408.449.677)

Geachte,

Op grond van toepasselijke openbaarheid vraag ik:

1. Digitaal afschrift van de bij de NBB neergelegde jaarrekening 2025
   (deposit-/referentienummer + PDF; Pappers noemt neerlegging 21.05.2026).
2. Balanstotaal / schulden LT-ST / cash reconcilieerbaar met publieke
   aggregators (CW Winst/Verlies EUR−2.232.791; equity EUR230.520.047).
3. Transfer-pricing / recharge / dividendmatrix met dochter IRE ELiT 2025.
4. Reconciliatie groepscommunicatie CA EUR118m vs statutaire moeder
   EUR73.583.681 + ELiT EUR44.587.904.
5. Koppeling federale BA passief afval / uranium-partnership (Energy tutelle).

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (IRE FUP + cc ELiT)
- [x] Concrete documenten (NBB PDF + BS + TP)
- [x] Periode en bedragen gevraagd
- [x] Moeder-dochter dual expliciet
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
            "title": "leftover dual hole-fill after IRE ELiT — IRE FUP YE2025 Medium",
            "status": "done",
            "hierarchy_target": "Belgie>Federaal>Nucleair>IRE>FUP>JR2025_L5",
            "entity_id": "ire_radioelements",
            "updated_utc": TS,
            "instructions": (
                "Completed: IRE FUP leftover nuclear parent dual after IRE ELiT; KBO 0408.449.677; "
                "YE2025 Medium CW NL+EN; sourced euros omzet DROP 73583681 pnl LOSS -2232791 "
                "equity 230520047 bruto 34261391 FTE 223; assets/debt Unknown; FOI ready not sent"
            ),
            "notes": (
                "tick1958 IRE FUP after ELiT; Medium CW omzet DROP 73.58m pnl LOSS 2.23m; "
                "FOI ready not sent; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1959; next every-10 1960"
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
        "title": "leftover dual hole-fill after IRE FUP",
        "sprint": "hole_fill",
        "priority": "8",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "",
        "instructions": (
            "Tick 1959 after 1958 IRE FUP. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE "
            "NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/nuclear "
            "(Pidpa/De Watergroep/Aquafin-if-unused). Do NOT redo IRE FUP, IRE ELiT, FANC, SCK CEN, "
            "EURIDICE, BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
            "Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE."
        ),
        "blocked_gap_id": "",
        "created_utc": TS,
        "updated_utc": TS,
        "notes": "spawned after tick1958; next every-10 1960",
    }
    append_csv(DATA / "research_queue.csv", [{k: rq_1959.get(k, "") for k in rq_fields}])

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
                "tick1958 leftover IRE FUP 0408.449.677 Medium CW NL+EN "
                "(omzet DROP 73.58m pnl LOSS 2.23m equity 230.52m bruto 34.26m FTE 223); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1959; next every-10 1960; "
                "continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""
## Tick 1958 - {TS} - rq_1958 IRE FUP (omzet DROP 73.58m / pnl LOSS 2.23m / Medium)

- Unit: **rq_1958** leftover dual after **rq_1957 IRE ELiT**. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took leftover **IRE FUP parent** now YE2025 on CW (KBO **0408.449.677**; Avenue de l'Espérance 1 Fleurus; SON/FUP radioisotope parent of ELiT). Do not redo IRE ELiT/FANC/SCK CEN/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/Synatom.
- Found: Companyweb NL+EN YE2025 — omzet **EUR73,583,681** DROP −16.56%; bruto **EUR34,261,391**; pnl **LOSS EUR−2,232,791**; equity **EUR230,520,047**; FTE **223**. Assets/debt/cash Unknown (Upswitch still YE2024-only). Group site CA **EUR118m** ≈ parent 73.58 + ELiT 44.59. Medium confidence.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (updated ire_radioelements/ire/nv_ire_elit); foi + draft gap_ire_fup_nbb_pdf_assets_debt_elit_tp_l5; rq_1958=done + rq_1959 open; loop_state ticks=1958.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1960**). Next: rq_1959 (AGB/FARO-if-YE2025 / AIESH-REW / unused water-DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1958 write OK: IRE FUP YE2025 Medium")
