# tick 1967 — CISCH YE2025 Strong Mons bilan+CW (rq_1967 after IEG)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T19:00:00Z"
csv.field_size_limit(10**7)

ENTITY = "cisch"
GAP = "gap_cisch_nbb_pdf_one_pension_commune_debt_matrix_l5"


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
        "source_id": "src_cisch_jr2025_bilan_mons",
        "title": "CISCH AG 18.06.2026 Bilan et comptes YE2025 (Mons PDF)",
        "url": (
            "https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/"
            "cisch-1/cisch/ag-du-18-juin-2026-1/cisch-bilan-comp-2025.pdf"
        ),
        "publisher": "CISCH SC / Ville de Mons AG",
        "accessed_date": "2026-08-23",
        "source_class": "primary_official",
        "notes": (
            "tick1967; Strong Horus bilan 01-12/2025; assets 1274482.74; "
            "equity 711448.89; debt 349281.03; provisions 213752.82; "
            "pnl 191870.13; bruto 1431781.28; omzet 7281; autres produits "
            "1521886.06 (ONE 720714.85 + commune cotisations); "
            "cotisation responsabilisation 342861.84; personnel 1137163.12; "
            "cash 817472.79; local docs/doge/data/raw/tick1967/"
        ),
    },
    {
        "source_id": "src_cisch_jr2025_note_synthese_mons",
        "title": "CISCH AG 18.06.2026 note de synthese comptes 2025",
        "url": (
            "https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/"
            "cisch-1/cisch/ag-du-18-juin-2026-1/"
            "note-de-synthese-ago-180626-comptes-2025-cisch.pdf"
        ),
        "publisher": "CISCH SC / Ville de Mons AG",
        "accessed_date": "2026-08-23",
        "source_class": "primary_official",
        "notes": (
            "tick1967; bilan 1.274483m; benefice 191870.13 affecte dette "
            "Quaregnon/Colfontaine + demenagement; cotisation "
            "responsabilisation 342861.84; commissaire opinion sans reserve; "
            "email dg@santemons.be"
        ),
    },
    {
        "source_id": "src_cisch_jr2025_cw",
        "title": "Companyweb CISCH YE2025 NBB-derived summary",
        "url": (
            "https://www.companyweb.be/nl/0214732561/"
            "centre-intercommunale-de-sante-du-coeur-du-hainaut"
        ),
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1967; Laatste balansjaar 2025; neergelegd 16-07-2026; "
            "pnl JUMP 191870 +194.73pct; equity JUMP 711449 +199.14pct; "
            "bruto JUMP 1431781 +20.35pct; FTE 10.2; omzet not published on CW"
        ),
    },
    {
        "source_id": "src_cisch_jr2025_cw_en",
        "title": "Companyweb EN twin CISCH YE2025 equity pnl bruto",
        "url": (
            "https://www.companyweb.be/en/0214732561/"
            "centre-intercommunale-de-sante-du-coeur-du-hainaut"
        ),
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1967; Last balance sheet year 2025; Profit/Loss 191870; "
            "Equity 711449; Gross margin 1431781; Employees 10.2; filed 16-07-2026"
        ),
    },
    {
        "source_id": "src_cisch_kbo_1967",
        "title": "KBO CISCH 0214.732.561 Actief SC Mons",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
            "ondernemingsnummer=0214732561"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1967; Actief SC sinds 15.10.1974; Rue des Arquebusiers 5 "
            "7000 Mons; aanbestedende overheid; absorbed CIS Arthur Naze "
            "0201.808.696 since 15.06.2020; NACE 94.993; "
            "NBB https://consult.cbso.nbb.be/consult-enterprise/0214732561"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1967 YE2025 Strong Mons bilan+note + CW NL+EN + Strong KBO "
    "0214.732.561 Actief SC; assets JUMP 1.274m equity JUMP 0.711m "
    "(reval terrains +0.282m) debt DROP 0.349m pnl JUMP 0.192m bruto JUMP "
    "1.432m omzet 7.3k autres produits 1.522m (ONE 0.721m + commune "
    "cotisations); cot. responsabilisation 0.343m; FTE 10.2; cash 0.817m; "
    "neerlegging 16.07.2026; Walloon health-promotion IGS dual ONE/communes; "
    f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
    "do not redo IEG/CENEO/HELORA/iMio/Passelecq/IGRETEC/IPFBW/Aquiris/SPGE/"
    "IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/CILE"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if ENTITY not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": ENTITY,
                "name_nl": (
                    "CISCH (Centre Intercommunale de Santé du Coeur du Hainaut)"
                ),
                "name_fr": (
                    "CISCH (Centre Intercommunale de Santé du Coeur du Hainaut)"
                ),
                "name_en": (
                    "CISCH (Walloon Hainaut heart-of-Hainaut health-promotion IGS)"
                ),
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": (
                    "https://www.mons.be/fr/ma-commune/vie-politique/"
                    "intercommunales/cisch-1/cisch"
                ),
                "foi_email": "dg@santemons.be",
                "foi_postal": "Rue des Arquebusiers 5 7000 Mons",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            ENTITY: {
                "notes": ent_notes,
                "foi_email": "dg@santemons.be",
                "foi_postal": "Rue des Arquebusiers 5 7000 Mons",
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_cisch_assets_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "1274482.74",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan TOTAL DE L'ACTIF 20/58",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": "tick1967; YE2025 assets 1274482.74 JUMP vs 1059295.44 YE2024",
    },
    {
        "budget_id": "bud_cisch_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "711448.89",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan CAPITAUX PROPRES 10/15 + CW",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": (
            "tick1967; YE2025 equity 711448.89 JUMP +199pct; includes "
            "reval terrains 281750 (not cash operating)"
        ),
    },
    {
        "budget_id": "bud_cisch_debt_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "349281.03",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan DETTES 17/49",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": (
            "tick1967; YE2025 debt 349281.03 DROP vs 563696.27; includes "
            "LT Quaregnon 52206.06 + Colfontaine 59199.61"
        ),
    },
    {
        "budget_id": "bud_cisch_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "191870.13",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan 9904 + CW Winst/Verlies",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": "tick1967; YE2025 pnl 191870.13 JUMP +194.73pct vs 65101.09",
    },
    {
        "budget_id": "bud_cisch_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "1431781.28",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan marge brute 9900 + CW",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": "tick1967; YE2025 bruto 1431781.28 JUMP +20.35pct vs 1189649.44",
    },
    {
        "budget_id": "bud_cisch_autres_produits_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "1521886.06",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan autres produits d exploitation 74",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": (
            "tick1967; YE2025 autres produits 1521886.06 (ONE promo sante "
            "720714.85 + commune AC + Province Hainaut 182925)"
        ),
    },
    {
        "budget_id": "bud_cisch_cot_resp_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "342861.84",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Mons bilan 621100 + note synthese",
        "source_id": "src_cisch_jr2025_bilan_mons",
        "confidence": "strong",
        "notes": (
            "tick1967; YE2025 cotisation responsabilisation 342861.84 "
            "JUMP vs 285847.68; largest single charge; FOI 2026-2030 path"
        ),
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
    "commitment_id": "comm_cisch_jr2025_statutory_assets",
    "title": (
        "CISCH YE2025 leftover Walloon health-promotion IGS dual "
        "(assets 1.274m / pnl JUMP 0.192m / ONE+commune)"
    ),
    "entity_id": ENTITY,
    "beneficiary": "Hainaut communes / ONE / CISCH patients-users",
    "legal_basis": (
        "SC association de communes CDLD; NBB neerlegging 16.07.2026; "
        "decret wallon openbaarheid / Code de la democratie locale"
    ),
    "decision_date": "2026-07-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "1274482.74",
    "cash_by_year": (
        "2025:assets=1274482.74;equity=711448.89;debt=349281.03;"
        "pnl=191870.13;bruto=1431781.28;autres_prod=1521886.06;"
        "one=720714.85;cot_resp=342861.84;omzet=7281;fte=10.2;"
        "cash=817472.79;prov_pension=213752.82"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": (
        "https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/"
        "cisch-1/cisch"
    ),
    "stated_goal": (
        "Intercommunal health-promotion centre (OMS-style prevention) "
        "financed by ONE + commune cotisations"
    ),
    "cut_option": (
        "FOI ONE contract + pension cot.responsabilisation 2026-2030 path + "
        "commune debt Quaregnon/Colfontaine repayment schedule; dual unit-cost "
        "vs other Walloon CIS"
    ),
    "source_id": "src_cisch_jr2025_bilan_mons",
    "confidence": "strong",
    "hierarchy_path": "Wallonie>Hainaut>CISCH>JR2025_statutory_L5",
    "notes": (
        "tick1967; Strong Mons bilan after IEG; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; HYGEA CW still YE2024; "
        "do not redo IEG/CENEO/HELORA/iMio/Passelecq/IGRETEC/IPFBW/"
        "Aquiris/SPGE/nuclear/water stack; not TE-additive"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_cisch_assets_1_27m_pnl_jump_0_19m_one_jr2025",
    "name": (
        "CISCH assets 1.274m / pnl JUMP 0.192m / ONE+commune health IGS YE2025"
    ),
    "level": "L5",
    "type": "walloon_igs_health_promotion_dual",
    "hierarchy_path": "Wallonie>Hainaut>CISCH>JR2025_statutory_L5",
    "annual_cost_eur": "1521886.06",
    "total_cost_eur": "1274482.74",
    "tco_notes": (
        "statutory assets 1.274m equity JUMP 0.711m (reval +0.282m) debt "
        "DROP 0.349m pnl JUMP 0.192m bruto 1.432m; autres produits 1.522m "
        "(ONE 0.721m); cot.responsabilisation 0.343m of 1.137m personnel; "
        "FTE 10.2; dual ONE/commune path"
    ),
    "confidence": "strong",
    "source_id": "src_cisch_jr2025_bilan_mons",
    "beneficiaries": "Hainaut communes / ONE / prevention users",
    "stated_goal": "Public intercommunal health-promotion centre",
    "measured_outcome": (
        "Strong Mons YE2025 bilan live unused after preferred AGB/FARO/AIESH/"
        "REW stall + after IEG; equity JUMP driven partly by land reval; "
        "pension cot.responsabilisation opaque 2026-2030"
    ),
    "absurdity_score": "3.5",
    "cost_score": "3.0",
    "difficulty": "2.5",
    "priority_index": "3.0",
    "cut_proposal": (
        "Publish ONE contract + pension cot.responsabilisation trajectory + "
        "Quaregnon/Colfontaine debt schedule; dual unit-cost vs other CIS"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1967; Strong Mons+CW; leftover unused health-promotion IGS after "
        "IEG; not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": GAP,
    "hierarchy_path": (
        "Wallonie>Hainaut>CISCH>nbb_pdf_one_pension_commune_debt_matrix_L5"
    ),
    "entity_id": ENTITY,
    "what_is_missing": (
        "NBB deposit reference number / official CDN PDF body YE2025 "
        "(CW neerlegging 16.07.2026; Mons bilan Strong but deposit id "
        "unpublished); ONE promo-sante contract reconcilable with 720714.85; "
        "cotisation responsabilisation 2026-2030 engagement path "
        "(commissaire annexe A-app 6.5); Quaregnon/Colfontaine debt "
        "repayment schedule to 2030; dual unit-cost vs other Walloon CIS"
    ),
    "why_it_matters": (
        "1.52m public autres-produits (ONE 0.72m + communes) with 0.34m "
        "pension cot.responsabilisation and commune-debt repayment plan "
        "opaque without contract/matrix"
    ),
    "priority": "7",
    "recipient_body": "CISCH SC (cc SPW / communes membres / ONE)",
    "recipient_email": "dg@santemons.be",
    "recipient_postal": "Rue des Arquebusiers 5 7000 Mons",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_cisch_jr2025_statutory_assets",
    "linked_leaderboard_id": "lb_cisch_assets_1_27m_pnl_jump_0_19m_one_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1967; human-send only; Strong Mons bilan; next every-10 1970",
}
if GAP not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{GAP}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — CISCH (NBB deposit / ONE / pension cot. / commune debt)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** CISCH SC — KBO **0214.732.561** (Centre Intercommunale de Santé du Coeur du Hainaut)  
**recipient:** dg@santemons.be / cc SPW / communes membres / ONE  
**sources:** [Mons bilan 2025](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/cisch-1/cisch/ag-du-18-juin-2026-1/cisch-bilan-comp-2025.pdf) · [note synthese](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/cisch-1/cisch/ag-du-18-juin-2026-1/note-de-synthese-ago-180626-comptes-2025-cisch.pdf) · [CW NL](https://www.companyweb.be/nl/0214732561/centre-intercommunale-de-sante-du-coeur-du-hainaut) · [CW EN](https://www.companyweb.be/en/0214732561/centre-intercommunale-de-sante-du-coeur-du-hainaut) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214732561) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0214732561)  
**tick:** 1967  
**confidence on table euros:** Strong (official Mons bilan + CW NL+EN confirm)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **16.07.2026**): assets **EUR1,274,482.74**; equity **EUR711,448.89** (**JUMP +199%**, includes land reval **EUR281,750**); debt **EUR349,281.03**; pnl **EUR191,870.13** (**JUMP +194.73%**); bruto **EUR1,431,781.28**; autres produits **EUR1,521,886.06** (ONE **EUR720,714.85**); cot. responsabilisation **EUR342,861.84**; FTE **10.2**.
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. HYGEA CW still YE2024. Do not redo IEG / CENEO / HELORA / iMio / Passelecq / IGRETEC / IPFBW / Aquiris / SPGE / nuclear-water stack.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: CISCH SC
t.a.v. openbaarheid / information officer
Rue des Arquebusiers 5
7000 Mons

cc: SPW — transparence / communes membres CISCH / ONE

Betreft: Verzoek om openbaarmaking — NBB-deposit YE2025 CISCH,
ONE-contract, cot.responsabilisation 2026-2030 en commune-schulden
(KBO 0214.732.561)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / CDLD)
vraag ik:

1. Digitaal afschrift / deposit-referentienummer van de bij de NBB
   neergelegde jaarrekening 2025 van CISCH SC (Companyweb noemt
   neerlegging 16.07.2026; Mons-publieke bilan bevestigt totalen).
2. ONE promo-sante contract / toelage reconcilieerbaar met
   EUR720.714,85 (code 740100).
3. Cotisation de responsabilisation traject 2026-2030 (commissaire
   annexe A-app 6.5) reconcilieerbaar met EUR342.861,84 in 2025.
4. Aflossingsschema schulden Quaregnon / Colfontaine tot 2030
   (LT+ST per bilan).
5. Dual unit-cost vs andere Walloon CIS / health-promotion IGS.

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {GAP}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (CISCH SC + SPW/communes/ONE cc)
- [x] Concrete documenten (NBB deposit / ONE / pension path / commune debt)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; HYGEA CW still YE2024; took unused leftover **CISCH** YE2025 Strong Mons bilan.
""",
        encoding="utf-8",
    )

# research_queue: close rq_1967, spawn rq_1968
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

have_1968 = False
for row in rq_rows:
    if row.get("task_id") == "rq_1967":
        row["status"] = "done"
        row["entity_id"] = ENTITY
        row["title"] = (
            "leftover dual hole-fill after IEG — CISCH YE2025 Strong"
        )
        row["updated_utc"] = TS
        row["blocked_gap_id"] = GAP
        row["notes"] = (
            "tick1967 CISCH YE2025 Strong assets 1.274m pnl JUMP 0.192m "
            "equity JUMP 0.711m debt DROP 0.349m bruto 1.432m; FOI ready; "
            "next rq_1968; next every-10 1970"
        )
        row["instructions"] = (
            "Completed: CISCH leftover Walloon Hainaut health-promotion IGS "
            "dual after IEG; KBO 0214.732.561; YE2025 Strong Mons bilan + "
            "CW NL+EN (assets 1.274m pnl JUMP 0.192m equity JUMP 0.711m "
            "debt DROP 0.349m bruto 1.432m autres_prod 1.522m ONE 0.721m); "
            f"FOI {GAP} ready"
        )
        row["hierarchy_target"] = "Wallonie>Hainaut>CISCH>JR2025_L5"
    if row.get("task_id") == "rq_1968":
        have_1968 = True

if not have_1968:
    rq_rows.append(
        {
            "task_id": "rq_1968",
            "title": "leftover dual hole-fill after CISCH",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1968 after 1967 CISCH YE2025 Strong. Prefer leftover "
                "AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/"
                "energy/nuclear. Do NOT redo CISCH, IEG, CENEO, CHU HELORA, "
                "iMio, Gabrielle Passelecq, IGRETEC, IPFBW, Aquiris, SPGE, "
                "IRE parent, IRE ELiT, FANC, SCK CEN, EURIDICE, BRUGEL, "
                "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
                "Dijk92, Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, SOWAER, INASEP, inBW, AIDE, "
                "ORES, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1967 CISCH; next every-10 1970",
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
            "last_unit_id": "rq_1967",
            "ticks_completed": "1967",
            "paused": "no",
            "notes": (
                "tick1967 CISCH YE2025 Strong Mons+CW (assets JUMP 1.274m "
                "pnl JUMP 0.192m equity JUMP 0.711m debt DROP 0.349m bruto "
                "1.432m autres_prod 1.522m ONE 0.721m); AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; next rq_1968; next every-10 1970"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""

## Tick 1967 - {TS} - rq_1967 CISCH (assets JUMP 1.274m / pnl JUMP 0.192m / Strong)

- Unit: **rq_1967** leftover dual after **rq_1966 IEG**. Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. HYGEA CW still YE2024. Took unused leftover **CISCH** YE2025 (KBO **0214.732.561**; Rue des Arquebusiers 5 Mons; Walloon Hainaut health-promotion IGS; **ONE + commune dual**; absorbed CIS Arthur Naze 2020). Do not redo IEG/CENEO/HELORA/iMio/Passelecq/IPFBW/IGRETEC/Aquiris/SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/Dijk92/AIEG/Synergrid.
- Found: Strong [Mons AG 18.06.2026 Bilan PDF](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/cisch-1/cisch/ag-du-18-juin-2026-1/cisch-bilan-comp-2025.pdf) + [note synthese](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/cisch-1/cisch/ag-du-18-juin-2026-1/note-de-synthese-ago-180626-comptes-2025-cisch.pdf) + Medium [Companyweb NL](https://www.companyweb.be/nl/0214732561/centre-intercommunale-de-sante-du-coeur-du-hainaut)/[EN](https://www.companyweb.be/en/0214732561/centre-intercommunale-de-sante-du-coeur-du-hainaut) + Strong KBO: assets **EUR1,274,482.74** JUMP; equity **EUR711,448.89** (**JUMP +199%**, reval terrains **EUR281,750**); debt **EUR349,281.03** DROP; pnl **EUR191,870.13** (**JUMP +194.73%**); bruto **EUR1,431,781.28**; autres produits **EUR1,521,886.06** (ONE **EUR720,714.85**); cot. responsabilisation **EUR342,861.84**; FTE **10.2**; neerlegging **16.07.2026**.
- Wrote: sources (+5); budgets (+7); commitments (+1); leaderboard (+1); entities (+1 cisch); foi + draft {GAP}; rq_1967=done + rq_1968 open; loop_state ticks=1967; raw PDFs saved.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1970**). Next: rq_1968 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1967 write complete: CISCH Strong YE2025")
