# tick 1963 — iMio YE2025 Strong AG+CW (rq_1963 after Gabrielle Passelecq / IGRETEC race)
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = Path(__file__).resolve().parent
TS = "2026-08-23T18:00:00Z"
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
        "source_id": "src_imio_jr2025_ag_mons",
        "title": "iMio AG 02.06.2026 comptes annuels YE2025 (Mons publiable PDF)",
        "url": (
            "https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/imio-1/imio/"
            "ag-du-2-juin-2026/publiable-point-4-intercommunale_de_mutualisation_en_matiere_"
            "informatique_et_organisationnell.pdf/@@download/file/"
            "Publiable%20-%20point-4-intercommunale_de_mutualisation_en_matiere_informatique_"
            "et_organisationnell.pdf"
        ),
        "publisher": "iMio SC / Ville de Mons AG publiable",
        "accessed_date": "2026-08-23",
        "source_class": "primary_official",
        "notes": (
            "tick1963; Strong statutory NBB schema in AG pack; assets 3148420.72; "
            "equity 913079.94; debt 2160340.78; LT 758385.44; cash 560966.88; "
            "omzet 7771293.6 JUMP +4.2pct; bruto 5688042.52; pnl DROP 182396.69; "
            "FTE 60.2; pers charges ~5024588; intangibles 723831.30; "
            "prod immobilisee 478506; members 445 / 251 communes; local raw "
            "docs/doge/data/raw/imio_ag2026_comptes2025.pdf"
        ),
    },
    {
        "source_id": "src_imio_jr2025_cw",
        "title": "Companyweb iMio YE2025 NBB-derived summary",
        "url": (
            "https://www.companyweb.be/nl/0841470248/"
            "intercommunale-de-mutualisation-en-matiere-informatique-et-organisationnelle"
        ),
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1963; Laatste balansjaar 2025; neergelegd 17-06-2026; "
            "pnl 182397 DROP -23.4pct; equity 913080 JUMP +24.98pct; "
            "bruto 5688043; FTE 60.2; omzet empty on free CW (AG Strong)"
        ),
    },
    {
        "source_id": "src_imio_jr2025_cw_en",
        "title": "Companyweb EN twin iMio YE2025 equity FTE",
        "url": (
            "https://www.companyweb.be/en/0841470248/"
            "intercommunale-de-mutualisation-en-matiere-informatique-et-organisationnelle"
        ),
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1963; Last balance sheet year 2025; Profit/Loss 182397; "
            "Equity 913080; Gross margin 5688043; FTE 60.2; filed 17-06-2026"
        ),
    },
    {
        "source_id": "src_imio_kbo_1963",
        "title": "KBO iMio 0841.470.248 Actief SC Isnes/Gembloux",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?"
            "ondernemingsnummer=0841470248"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1963; Actief SC/SCRL sinds 01.12.2011; zetel Rue Leon Morel Isnes 1 "
            "5032 Gembloux; email directeurgeneral@imio.be; contact@imio.be; "
            "aanbestedende overheid; NBB consult "
            "https://consult.cbso.nbb.be/consult-enterprise/0841470248"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

ent_notes = (
    "tick1963 YE2025 Strong AG Mons PDF (NBB schema) + CW NL+EN + Strong KBO "
    "0841.470.248 Actief SC; omzet JUMP 7.771m pnl DROP 0.182m equity JUMP 0.913m "
    "assets 3.148m debt 2.160m cash 0.561m bruto 5.688m FTE JUMP 60.2; "
    "intangibles JUMP 0.724m prod immobilisee 0.479m; 445 members / 251 communes; "
    "neerlegging 17.06.2026; Walloon IT mutualisation IGS dual Digipolis VL; "
    "FOI gap_imio_nbb_pdf_tariff_member_matrix_l5; preferred AGB Bornem JR2024; "
    "FARO/AIESH/REW YE2024; do not redo Gabrielle Passelecq/IGRETEC/IPFBW/Aquiris/"
    "SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE"
)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

if "imio" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "imio",
                "name_nl": "iMio (Intercommunale IT-mutualisatie Wallonie)",
                "name_fr": (
                    "iMio (Intercommunale de Mutualisation en matiere "
                    "Informatique et Organisationnelle)"
                ),
                "name_en": "iMio (Walloon local-government IT mutualisation IGS)",
                "level": "intercommunale",
                "parent_id": "wallonie_gov",
                "community_language": "fr",
                "website": "https://www.imio.be",
                "foi_email": "contact@imio.be",
                "foi_postal": "Rue Leon Morel 1 5032 Isnes (Gembloux)",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "imio": {
                "notes": ent_notes,
                "foi_email": "contact@imio.be",
                "foi_postal": "Rue Leon Morel 1 5032 Isnes (Gembloux)",
                "website": "https://www.imio.be",
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_imio_omzet_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "7771293.6",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG official CA YE2025 (NBB schema)",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 omzet 7771293.6 JUMP +4.2pct vs YE2024",
    },
    {
        "budget_id": "bud_imio_pnl_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "182396.69",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG + CW Winst/Verlies",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 pnl DROP 182396.69 -23.4pct vs 238114.77",
    },
    {
        "budget_id": "bud_imio_bruto_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "5688042.52",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG + CW bruto/gross margin",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 bruto 5688042.52 +10.65pct vs 5140629.15",
    },
    {
        "budget_id": "bud_imio_equity_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "913079.94",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG + CW equity",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 equity 913079.94 JUMP +24.98pct vs 730609.05",
    },
    {
        "budget_id": "bud_imio_assets_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "3148420.72",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG bilan TOTAL ACTIF 20/58",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 assets 3148420.72 vs 2982750.39 YE2024",
    },
    {
        "budget_id": "bud_imio_debt_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "2160340.78",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG DETTES 17/49",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": (
            "tick1963; YE2025 debt 2160340.78 (LT 758385.44 + ST 1394309.38) "
            "vs 2177141.34 YE2024"
        ),
    },
    {
        "budget_id": "bud_imio_cash_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "560966.88",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG valeurs disponibles 54/58",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 cash 560966.88 DROP vs 616818.14 YE2024",
    },
    {
        "budget_id": "bud_imio_fte_jr2025_statutory",
        "entity_id": "imio",
        "year": "2025",
        "amount_eur": "60.2",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "AG + CW social-balance FTE 9087",
        "source_id": "src_imio_jr2025_ag_mons",
        "confidence": "strong",
        "notes": "tick1963; YE2025 FTE 60.2 JUMP vs 52.9 YE2024; pers ~5.025m",
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
    "commitment_id": "comm_imio_jr2025_statutory_omzet",
    "title": (
        "iMio YE2025 leftover Walloon IT-mutualisation IGS dual Digipolis "
        "(omzet JUMP 7.771m / pnl DROP 0.182m / assets 3.148m)"
    ),
    "entity_id": "imio",
    "beneficiary": "Walloon communes / CPAS / local powers (~251 communes; 445 members)",
    "legal_basis": (
        "SC association de communes CDLD; NBB neerlegging 17.06.2026; "
        "decret wallon openbaarheid / Code de la democratie locale"
    ),
    "decision_date": "2026-06-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "7771293.6",
    "cash_by_year": (
        "2025:omzet=7771293.6;bruto=5688042.52;pnl=182396.69;equity=913079.94;"
        "assets=3148420.72;debt=2160340.78;cash=560966.88;fte=60.2;"
        "intangibles=723831.30;prod_immo=478506"
    ),
    "remaining_eur": "",
    "status": "active",
    "evaluation_url": "https://www.imio.be",
    "stated_goal": (
        "Mutualise FLOSS/IT solutions for Walloon local authorities "
        "(cybersecurity, digitalisation, shared apps)"
    ),
    "cut_option": (
        "FOI NBB deposit ref + member tariff matrix + Digipolis dual unit-cost; "
        "publish intangibles capitalisation policy"
    ),
    "source_id": "src_imio_jr2025_ag_mons",
    "confidence": "strong",
    "hierarchy_path": "Wallonie>IGS>iMio>JR2025_statutory_L5",
    "notes": (
        "tick1963; Strong AG+CW after Gabrielle Passelecq; preferred AGB Bornem JR2024 / "
        "FARO YE2024 / AIESH YE2024 / REW YE2024; do not redo Passelecq/IGRETEC/IPFBW/"
        "Aquiris/SPGE/Hydria/Vivaqua/CILE/IRE/FANC/SCK/EURIDICE/BRUGEL; not TE-additive"
    ),
}
if comm_row["commitment_id"] not in existing_comm:
    append_csv(DATA / "commitments.csv", [comm_row])

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

lb_row = {
    "item_id": "lb_imio_omzet_7_77m_equity_jump_fte_60_jr2025",
    "name": (
        "iMio omzet JUMP 7.771m / pnl DROP 0.182m / equity JUMP 0.913m / "
        "FTE 60.2 (Walloon IT IGS YE2025)"
    ),
    "level": "L5",
    "type": "walloon_igs_it_mutualisation_dual",
    "hierarchy_path": "Wallonie>IGS>iMio>JR2025_statutory_L5",
    "annual_cost_eur": "7771293.6",
    "total_cost_eur": "3148420.72",
    "tco_notes": (
        "statutory omzet 7771293.6 JUMP bruto 5688042 pnl DROP 182397 equity JUMP 913080 "
        "assets 3148421 debt 2160341 cash 560967 fte JUMP 60.2; intangibles JUMP 723831; "
        "dual Digipolis VL IT mutualisation"
    ),
    "confidence": "strong",
    "source_id": "src_imio_jr2025_ag_mons",
    "beneficiaries": "Walloon communes/CPAS (~251 communes; 445 members)",
    "stated_goal": "Public FLOSS/IT mutualisation for local authorities",
    "measured_outcome": (
        "Strong AG Mons YE2025 PDF live unused after preferred AGB/FARO/AIESH/REW stall; "
        "omzet +4.2pct with pnl DROP -23pct and FTE JUMP; member tariff matrix + Digipolis "
        "dual unit-cost unresolved"
    ),
    "absurdity_score": "3.5",
    "cost_score": "4.0",
    "difficulty": "2.5",
    "priority_index": "4.2",
    "cut_proposal": (
        "Publish NBB deposit ref + commune tariff/fee matrix + Digipolis dual unit-cost; "
        "reconcile FTE/personnel JUMP vs pnl DROP; intangibles capitalisation transparency"
    ),
    "status": "active",
    "struck_reason": "",
    "notes": (
        "tick1963; Strong AG+CW; leftover unused IGS dual after Gabrielle Passelecq; "
        "not TE-additive pure-waste top10"
    ),
}
if lb_row["item_id"] not in existing_lb:
    append_csv(DATA / "leaderboard.csv", [lb_row])

gap_id = "gap_imio_nbb_pdf_tariff_member_matrix_l5"
existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

foi_row = {
    "gap_id": gap_id,
    "hierarchy_path": "Wallonie>IGS>iMio>nbb_pdf_tariff_member_matrix_L5",
    "entity_id": "imio",
    "what_is_missing": (
        "NBB deposit reference number / official CDN PDF body YE2025 "
        "(CW neerlegging 17.06.2026; AG pack Strong but deposit id unpublished); "
        "member tariff / fee matrix by commune-CPAS category vs CA 7.771m; "
        "Digipolis / VL IT-mutualisation dual unit-cost; "
        "intangibles capitalisation policy detail (JUMP 0.724m / prod 0.479m); "
        "personnel +13pct vs pnl DROP -23pct recon"
    ),
    "why_it_matters": (
        "Near-universal Walloon commune IT mutualisation (251/261 communes): "
        "7.771m CA / 5.025m personnel / rising capitalised software — "
        "opacity on per-member fees and Digipolis dual without matrix"
    ),
    "priority": "8",
    "recipient_body": "iMio SC (cc SPW / communes membres)",
    "recipient_email": "contact@imio.be",
    "recipient_postal": "Rue Leon Morel 1 5032 Isnes (Gembloux)",
    "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_imio_jr2025_statutory_omzet",
    "linked_leaderboard_id": "lb_imio_omzet_7_77m_equity_jump_fte_60_jr2025",
    "created_utc": TS,
    "updated_utc": TS,
    "notes": "tick1963; human-send only; Strong AG; next every-10 1970",
}
if gap_id not in existing_foi:
    append_csv(DATA / "foi_queue.csv", [foi_row])

draft_path = ROOT / "docs" / "doge" / "foi" / "drafts" / f"{gap_id}.md"
if not draft_path.exists():
    draft_path.write_text(
        f"""# FOI draft — iMio (NBB deposit ref / tariff matrix / Digipolis dual)

**gap_id:** `{gap_id}`  
**status:** ready (NOT sent)  
**entity:** iMio SC — KBO **0841.470.248** (Walloon IT mutualisation IGS)  
**recipient:** contact@imio.be / cc SPW / communes membres  
**sources:** [AG Mons PDF](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/imio-1/imio/ag-du-2-juin-2026/publiable-point-4-intercommunale_de_mutualisation_en_matiere_informatique_et_organisationnell.pdf/@@download/file/Publiable%20-%20point-4-intercommunale_de_mutualisation_en_matiere_informatique_et_organisationnell.pdf) · [Companyweb NL](https://www.companyweb.be/nl/0841470248/intercommunale-de-mutualisation-en-matiere-informatique-et-organisationnelle) · [Companyweb EN](https://www.companyweb.be/en/0841470248/intercommunale-de-mutualisation-en-matiere-informatique-et-organisationnelle) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0841470248) · [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0841470248) · [imio.be](https://www.imio.be)  
**tick:** 1963  
**confidence on table euros:** Strong (official AG statutory NBB schema + CW NL+EN confirm)

## Context

- Sourced YE **01.01.2025–31.12.2025** (neerlegging **17.06.2026**): omzet **EUR7,771,293.60** (**JUMP +4.2%**); bruto **EUR5,688,042.52**; pnl **EUR182,396.69** (**DROP −23.4%**); equity **EUR913,079.94** (**JUMP +24.98%**); assets **EUR3,148,420.72**; debt **EUR2,160,340.78**; cash **EUR560,966.88**; FTE **60.2** (**JUMP**); intangibles **EUR723,831.30**; production immobilisée **EUR478,506**.
- Membership: **445** members incl. **251** communes (~96% Wallonie).
- Preferred leftover paths still stalled: AGB Bornem **JR2024**; FARO/AIESH/REW **YE2024**. Do not redo Gabrielle Passelecq / IGRETEC / IPFBW / Aquiris / SPGE / Hydria / Vivaqua / CILE / IRE cluster / BRUGEL.

## Brief

```text
[Naam verzoeker]
[Adres]
[E-mail]
[Datum]

Aan: iMio SC
t.a.v. openbaarheid / information officer
Rue Léon Morel 1
5032 Isnes (Gembloux)

cc: SPW — transparence / communes membres iMio

Betreft: Verzoek om openbaarmaking — NBB-deposit YE2025 iMio,
ledentarieven-matrix en Digipolis-dual unit-cost (KBO 0841.470.248)

Geachte,

Op grond van toepasselijke openbaarheid (decret wallon / CDLD)
vraag ik:

1. Digitaal afschrift / deposit-referentienummer van de bij de NBB
   neergelegde jaarrekening 2025 van iMio SC (Companyweb noemt
   neerlegging 17.06.2026; AG-publieke pack bevestigt totalen).
2. Ledentarief- / contributiematrix 2025 per categorie (commune /
   CPAS / andere) reconcilieerbaar met CA EUR7.771.293,60.
3. Dual unit-cost vs Digipolis / andere VL IT-mutualisatie (per
   lid / per oplossing) indien beschikbaar.
4. Toelichting kapitalisatie immateriële vaste activa JUMP
   (EUR723.831,30) + production immobilisée EUR478.506 vs
   personeelsstijging +13% en pnl DROP −23%.
5. Top producten/oplossingen omzet-split 2025 (11 solutions).

Periode: boekjaar 01.01.2025–31.12.2025.
Referentie: {gap_id}

Met vriendelijke groeten,
[Naam]
```

## Checklist

- [x] Juiste instelling (iMio SC + SPW/communes cc)
- [x] Concrete documenten (NBB deposit ref / tariff matrix / Digipolis dual)
- [x] Periode en bedragen
- [x] `foi_queue.csv` ready — **NOT sent** (human-gated)
- Hunt this tick: AGB Bornem official still JR2024-only; FARO NBB still YE2024; AIESH/REW still YE2024; Gabrielle Passelecq already taken tick1962; took unused leftover **iMio** YE2025 Strong AG.
""",
        encoding="utf-8",
    )

# research_queue: close rq_1963, spawn rq_1964
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)

have_1964 = False
for row in rq_rows:
    if row.get("task_id") == "rq_1963":
        row["status"] = "done"
        row["entity_id"] = "imio"
        row["title"] = (
            "leftover dual hole-fill after Gabrielle Passelecq — iMio YE2025 Strong"
        )
        row["updated_utc"] = TS
        row["blocked_gap_id"] = gap_id
        row["notes"] = (
            "tick1963 iMio YE2025 Strong omzet JUMP 7.771m pnl DROP 0.182m "
            "assets 3.148m equity JUMP 0.913m; FOI ready; next rq_1964; next every-10 1970"
        )
        row["instructions"] = (
            "Completed: iMio leftover Walloon IT-mutualisation IGS dual after "
            "Gabrielle Passelecq; KBO 0841.470.248; YE2025 Strong AG Mons PDF + CW NL+EN "
            "(omzet JUMP 7.771m pnl DROP 0.182m assets 3.148m equity JUMP 0.913m "
            "debt 2.160m cash 0.561m FTE 60.2); FOI "
            f"{gap_id} ready"
        )
        row["hierarchy_target"] = "Wallonie>IGS>iMio>JR2025_L5"
    if row.get("task_id") == "rq_1964":
        have_1964 = True

if not have_1964:
    rq_rows.append(
        {
            "task_id": "rq_1964",
            "title": "leftover dual hole-fill after iMio",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1964 after 1963 iMio YE2025 Strong. Prefer leftover AGB/APB if "
                "JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/nuclear. Do NOT redo iMio, Gabrielle "
                "Passelecq, IGRETEC, IPFBW, Aquiris, SPGE, IRE parent, IRE ELiT, FANC, "
                "SCK CEN, EURIDICE, BRUGEL, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, "
                "NIRAS, Bel V, Dijk92, Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, SOWAER, INASEP, inBW, AIDE, ORES."
            ),
            "blocked_gap_id": "",
            "created_utc": TS,
            "updated_utc": TS,
            "notes": "spawned after tick1963 iMio; next every-10 1970",
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
            "last_unit_id": "rq_1963",
            "ticks_completed": "1963",
            "paused": "no",
            "notes": (
                "tick1963 iMio YE2025 Strong AG+CW (omzet JUMP 7.771m pnl DROP 0.182m "
                "assets 3.148m equity JUMP 0.913m debt 2.160m FTE 60.2); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1964; next every-10 1970"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""

## Tick 1963 - {TS} - rq_1963 iMio (omzet JUMP 7.771m / pnl DROP 0.182m / assets 3.148m / Strong)

- Unit: **rq_1963** leftover dual after concurrent **rq_1962 Gabrielle Passelecq** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **iMio** YE2025 (KBO **0841.470.248**; Rue Léon Morel 1 Isnes/Gembloux; Walloon IT mutualisation IGS; **Digipolis VL dual**). Do not redo Gabrielle Passelecq/IGRETEC/IPFBW/Aquiris/SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL/Hydria/Vivaqua/Belgoprocess/Laborelec/CILE/NIRAS/Bel V/INASEP/inBW/AIDE/ORES.
- Found: Strong [Mons AG 02.06.2026 PDF](https://www.mons.be/fr/ma-commune/vie-politique/intercommunales/imio-1/imio/ag-du-2-juin-2026/publiable-point-4-intercommunale_de_mutualisation_en_matiere_informatique_et_organisationnell.pdf/@@download/file/Publiable%20-%20point-4-intercommunale_de_mutualisation_en_matiere_informatique_et_organisationnell.pdf) (NBB schema) + Medium [Companyweb NL](https://www.companyweb.be/nl/0841470248/intercommunale-de-mutualisation-en-matiere-informatique-et-organisationnelle)/[EN](https://www.companyweb.be/en/0841470248/intercommunale-de-mutualisation-en-matiere-informatique-et-organisationnelle) + Strong KBO: omzet **EUR7,771,293.60** (**JUMP +4.2%**); bruto **EUR5,688,042.52**; pnl **EUR182,396.69** (**DROP −23.4%**); equity **EUR913,079.94** (**JUMP +24.98%**); assets **EUR3,148,420.72**; debt **EUR2,160,340.78**; cash **EUR560,966.88**; FTE **60.2**; intangibles **EUR723,831.30**; neerlegging **17.06.2026**; members **445** / communes **251**.
- Wrote: sources (+4); budgets (+8); commitments (+1); leaderboard (+1); entities (+1 imio); foi + draft {gap_id}; rq_1963=done + rq_1964 open; loop_state ticks=1963; raw PDF saved.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1970**). Next: rq_1964 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1963 write complete: iMio Strong YE2025")
