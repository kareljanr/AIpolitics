# tick 2131 — L'Orchidée Ittre YE2025 Medium CW leftover dual MRS
import csv
from pathlib import Path

csv.field_size_limit(10**7)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "docs" / "doge" / "data"
LOG = ROOT / "docs" / "doge" / "loop_log.md"
FOI_DRAFT = ROOT / "docs" / "doge" / "foi" / "drafts"
UTC = "2026-08-25T13:45:00Z"
DATE = "2026-08-25"
ENTITY = "asbl_lorchidee_ittre"
GAP = "gap_lorchidee_ittre_nbb_pdf_assets_debt_thin_equity_omzet_jump_matrix_l5"
COMM = "comm_lorchidee_ittre_jr2025_statutory"
LB = "lb_lorchidee_ittre_omzet_jump_4_47m_thin_equity_jr2025"

OMZET = 4468744
PNL = 101039
EQUITY = 202028
BRUTO = 4201164
FTE = 66.5
OMZET_Yoy = 9.32
BRUTO_Yoy = 5.18
PNL_Yoy = -5.77
EQUITY_Yoy = 100.05


def append_csv(path: Path, rows: list[dict], id_key: str):
    with path.open(newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fieldnames = r.fieldnames
        existing = list(r)
    have = {row.get(id_key) for row in existing}
    new_rows = [row for row in rows if row.get(id_key) not in have]
    if not new_rows:
        print(f"skip {path.name}: already present")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(existing)
        for row in new_rows:
            w.writerow({k: row.get(k, "") for k in fieldnames})
    print(f"append {path.name}: +{len(new_rows)}")


sources = [
    {
        "source_id": "src_lorchidee_ittre_jr2025_cw_nl",
        "title": "L'Orchidée Ittre Companyweb NL YE2025",
        "url": "https://www.companyweb.be/nl/0458352318",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2131; YE2025 omzet/pnl/equity/bruto/FTE; neerlegging 01.08.2026; Medium",
    },
    {
        "source_id": "src_lorchidee_ittre_jr2025_cw_en",
        "title": "L'Orchidée Ittre Companyweb EN YE2025",
        "url": "https://www.companyweb.be/en/0458352318",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2131; EN mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_lorchidee_ittre_jr2025_cw_fr",
        "title": "L'Orchidée Ittre Companyweb FR YE2025",
        "url": "https://www.companyweb.be/fr/0458352318",
        "publisher": "Companyweb",
        "accessed_date": DATE,
        "source_class": "company_register_aggregator",
        "notes": "tick2131; FR mirror confirms same YE2025 euros; Medium",
    },
    {
        "source_id": "src_lorchidee_ittre_kbo_2131",
        "title": "KBO L'ORCHIDEE 0458.352.318",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?lang=nl&ondernemingsnummer=0458352318",
        "publisher": "KBO/BCE",
        "accessed_date": DATE,
        "source_class": "official_register",
        "notes": (
            "tick2131; Actief VZW/ASBL; 1 VE; NACE 87.301 ROB/MRPA; "
            "bestuurders Jeandel Christine + Remy Yves (Armonea path); Strong identity"
        ),
    },
    {
        "source_id": "src_lorchidee_ittre_site_2131",
        "title": "Armonea L'Orchidée Ittre contact",
        "url": "https://www.armonea.be/lorchidee",
        "publisher": "Armonea / Colisée",
        "accessed_date": DATE,
        "source_class": "entity_site",
        "notes": "tick2131; orchidee.admin@armonea.be / info@armonea.be; Rue des Rabots 27 Ittre",
    },
]
append_csv(DATA / "sources.csv", sources, "source_id")

budgets = [
    {
        "budget_id": "bud_lorchidee_ittre_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(OMZET),
        "amount_min_eur": str(OMZET),
        "amount_max_eur": str(OMZET),
        "basis": "CW turnover / Omzet YE2025 (primary envelope)",
        "source_id": "src_lorchidee_ittre_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick2131; omzet JUMP {OMZET} (+{OMZET_Yoy}%) vs YE2024 4087776",
    },
    {
        "budget_id": "bud_lorchidee_ittre_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(PNL),
        "amount_min_eur": str(PNL),
        "amount_max_eur": str(PNL),
        "basis": "CW Profit/Loss YE2025",
        "source_id": "src_lorchidee_ittre_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick2131; pnl DROP {PNL} ({PNL_Yoy}%) vs YE2024 107231",
    },
    {
        "budget_id": "bud_lorchidee_ittre_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(EQUITY),
        "amount_min_eur": str(EQUITY),
        "amount_max_eur": str(EQUITY),
        "basis": "CW Equity / Eigen vermogen YE2025",
        "source_id": "src_lorchidee_ittre_jr2025_cw_en",
        "confidence": "medium",
        "notes": (
            f"tick2131; equity JUMP {EQUITY} (+{EQUITY_Yoy}%) vs YE2024 100989; "
            "thin vs omzet; YE2023 was negative equity"
        ),
    },
    {
        "budget_id": "bud_lorchidee_ittre_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(BRUTO),
        "amount_min_eur": str(BRUTO),
        "amount_max_eur": str(BRUTO),
        "basis": "CW Gross margin / Brutomarge YE2025",
        "source_id": "src_lorchidee_ittre_jr2025_cw_en",
        "confidence": "medium",
        "notes": f"tick2131; bruto JUMP {BRUTO} (+{BRUTO_Yoy}%) vs YE2024 3994303",
    },
    {
        "budget_id": "bud_lorchidee_ittre_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": str(FTE),
        "amount_min_eur": str(FTE),
        "amount_max_eur": str(FTE),
        "basis": "CW social-balance FTE / Employees",
        "source_id": "src_lorchidee_ittre_jr2025_cw_en",
        "confidence": "medium",
        "notes": "tick2131; FTE 66.5 JUMP vs YE2024 64.8",
    },
]
append_csv(DATA / "budgets.csv", budgets, "budget_id")

append_csv(
    DATA / "entities.csv",
    [
        {
            "entity_id": ENTITY,
            "name_nl": "L'Orchidée (Ittre) — Armonea MRS",
            "name_fr": "L'Orchidée ASBL (Ittre) — MRS Armonea",
            "name_en": "L'Orchidée nursing home (Ittre)",
            "level": "other",
            "parent_id": "sec_wallonia",
            "community_language": "fr",
            "website": "https://www.armonea.be/lorchidee",
            "foi_email": "orchidee.admin@armonea.be",
            "foi_postal": "Rue des Rabots 27, 1460 Ittre",
            "notes": (
                "tick2131 YE2025 Medium CW NL+EN+FR + Strong KBO 0458.352.318 Actief VZW/ASBL "
                "1 VE; NACE 87.301 ROB/MRPA; Remy Yves Armonea/Colisée path; omzet JUMP 4.47m "
                "bruto JUMP 4.20m pnl DROP 0.10m equity JUMP thin 0.20m FTE 66.5; FOI "
                f"{GAP}; AGB Bornem JR2024; FARO/AIESH/REW YE2024"
            ),
        }
    ],
    "entity_id",
)

append_csv(
    DATA / "commitments.csv",
    [
        {
            "commitment_id": COMM,
            "title": (
                "L'Orchidée Ittre YE2025 leftover dual "
                "(omzet JUMP 4.47m / thin equity JUMP 0.20m)"
            ),
            "entity_id": ENTITY,
            "beneficiary": "Ittre/Brabant wallon elderly residents (MRPA/MRS)",
            "legal_basis": "ASBL/VZW MRS Armonea path (KBO 0458.352.318); AViQ/INAMI dual",
            "decision_date": "2026-08-01",
            "start_year": "2025",
            "end_year": "2025",
            "total_envelope_eur": str(OMZET),
            "cash_by_year": (
                f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},'
                f'"2025_bruto":{BRUTO},"2025_fte":{FTE}}}'
            ),
            "remaining_eur": "0",
            "status": "active",
            "evaluation_url": "https://www.companyweb.be/en/0458352318",
            "stated_goal": "Residential elderly care Ittre (MRPA/MRS)",
            "cut_option": (
                "Publish NBB PDF assets/debt FOI; map AViQ/INAMI vs resident fees; "
                "explain thin equity 0.20m after YE2022-23 negative equity vs 4.47m omzet"
            ),
            "source_id": "src_lorchidee_ittre_jr2025_cw_en",
            "confidence": "medium",
            "hierarchy_path": "Wallonie>BrabantWallon>Ittre>LOrchidee_Armonea>JR2025_statutory_L5",
            "notes": (
                "tick2131; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; "
                "FARO/AIESH/REW YE2024; not TE-additive of 348bn; omzet primary; "
                "do not redo Restel Flats/Famifamenne/Fakkel/Armonea holding"
            ),
        }
    ],
    "commitment_id",
)

append_csv(
    DATA / "leaderboard.csv",
    [
        {
            "item_id": LB,
            "name": "L'Orchidée Ittre omzet JUMP 4.47m / thin equity 0.20m (YE2025)",
            "level": "L5",
            "type": "mrs_asbl_statutory",
            "hierarchy_path": "Wallonie>BrabantWallon>Ittre>LOrchidee_Armonea>JR2025",
            "annual_cost_eur": str(OMZET),
            "total_cost_eur": str(OMZET),
            "tco_notes": (
                "CW omzet primary MRS envelope; bruto near omzet; "
                "thin equity 0.20m (~4.5pct of omzet) after YE2022-23 negative; "
                "assets/debt Unknown pending NBB PDF FOI"
            ),
            "confidence": "medium",
            "source_id": "src_lorchidee_ittre_jr2025_cw_en",
            "beneficiaries": "Ittre L'Orchidée MRS residents (1 VE; Armonea path)",
            "stated_goal": "MRPA/MRS elderly residential care",
            "measured_outcome": (
                f"omzet JUMP +{OMZET_Yoy}%; bruto JUMP +{BRUTO_Yoy}%; "
                f"pnl DROP {PNL_Yoy}%; equity JUMP +{EQUITY_Yoy}% to thin 0.20m; "
                f"FTE JUMP {FTE} from 64.8"
            ),
            "absurdity_score": "6.8",
            "cost_score": "4.0",
            "difficulty": "3.5",
            "priority_index": "5.8",
            "cut_proposal": (
                "Publish NBB PDF assets/debt FOI; map AViQ/INAMI vs fees; "
                "scrutinise thin equity recovery path vs Armonea group extraction"
            ),
            "status": "open",
            "struck_reason": "",
            "notes": (
                f"tick2131; Medium CW; FOI {GAP}; stall FARO/AIESH/REW YE2024; "
                "deferred leftover after Care-Support; Remy Yves path"
            ),
        }
    ],
    "item_id",
)

append_csv(
    DATA / "foi_queue.csv",
    [
        {
            "gap_id": GAP,
            "hierarchy_path": "Wallonie>BrabantWallon>Ittre>LOrchidee>NBB_PDF_assets_debt",
            "entity_id": ENTITY,
            "what_is_missing": (
                "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); AViQ/INAMI "
                "public subsidy vs resident-fee split; explanation of thin equity JUMP "
                "0.20m (+100%) after YE2022-23 negative equity vs omzet JUMP 4.47m"
            ),
            "why_it_matters": (
                "Medium CW shows 4.47m omzet Armonea-path MRS ASBL with thin equity "
                "0.20m (~4.5pct of omzet) after multi-year negative equity without "
                "balanstotaal/assets/debt; material L5 residual MRS"
            ),
            "priority": "8",
            "recipient_body": "L'Orchidée ASBL / Armonea",
            "recipient_email": "orchidee.admin@armonea.be",
            "recipient_postal": "Rue des Rabots 27, 1460 Ittre",
            "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
            "status": "ready",
            "date_ready": DATE,
            "date_sent": "",
            "date_due": "",
            "date_answered": "",
            "response_summary": "",
            "linked_commitment_id": COMM,
            "linked_leaderboard_id": LB,
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "tick2131; human-send only; Medium CW; next every-10 2140",
        }
    ],
    "gap_id",
)

rq_path = DATA / "research_queue.csv"
with rq_path.open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fieldnames = r.fieldnames
    rows = list(r)

found = False
for row in rows:
    if row["task_id"] == "rq_2131":
        found = True
        row["status"] = "done"
        row["title"] = "leftover dual — L'Orchidée Ittre YE2025 Medium"
        row["entity_id"] = ENTITY
        row["updated_utc"] = UTC
        row["hierarchy_target"] = "L5"
        row["instructions"] = (
            "Completed leftover L'Orchidée Ittre YE2025 Medium CW after Care-Support; "
            f"KBO 0458.352.318; omzet JUMP {OMZET} bruto JUMP {BRUTO} pnl DROP {PNL} "
            f"equity JUMP thin {EQUITY} FTE {FTE}; FOI {GAP}; 1 VE NACE 87.301 Armonea path; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024"
        )
        row["notes"] = (
            "tick2131 L'Orchidée Ittre Medium omzet JUMP 4.47m bruto JUMP 4.20m pnl DROP "
            "0.10m equity JUMP thin 0.20m FTE 66.5; FOI ready; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; next rq_2132; next every-10 2140"
        )
        row["blocked_gap_id"] = GAP

if not any(r.get("task_id") == "rq_2132" for r in rows):
    rows.append(
        {
            "task_id": "rq_2132",
            "title": (
                "leftover dual hole-fill after L'Orchidée — prefer "
                "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
            ),
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2132 after L'Orchidée Ittre YE2025 Medium. Prefer leftover AGB/APB "
                "if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/"
                "disability/thuiszorg. Do NOT redo L'Orchidée Ittre, Care-Support, "
                "MPC Sint-Franciscus, Zorghome De Fakkel, Restel Flats, Le Château Vert, "
                "SLG Wallonie, Famifamenne, Residence Le Castel, R.S.W., Home Sebrechts, "
                "Unite Jolimont, t Buurthuis, Le Bosquet, Strebo, Entraide, La Charmille, "
                "Charmilles, Sittelles, Les Buissons, Residence 3, Elisabeth Aan Zee, "
                "XXe Aout, Ninove, Zilverlinde, Sint-Camillus, IDELUX*, INTRADEL, Korian*, "
                "SLG Operaties VL, SLG Vlaanderen VZW, Always Home, AREWAL, AGB Bornem, "
                "Armonea holding, emeis holding."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": (
                "spawned after tick2131 L'Orchidée; FARO/AIESH/REW still YE2024; "
                "next every-10 2140"
            ),
        }
    )

with rq_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)
assert found, "rq_2131 not found"

with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            UTC,
            "rq_2131",
            "2131",
            "no",
            (
                "tick2131 leftover L'Orchidée Ittre 0458.352.318 Medium CW "
                "(omzet JUMP 4.47m bruto JUMP 4.20m pnl DROP 0.10m equity JUMP thin 0.20m "
                "FTE 66.5; assets/debt Unknown; 1 VE NACE 87.301 Armonea Remy Yves); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2132; next every-10 2140; "
                "continuous hole_fill"
            ),
        ]
    )

foi_text = f"""# FOI draft — L'Orchidée Ittre (NBB PDF / assets-debt / thin-equity / omzet-jump)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** L'Orchidée ASBL — KBO **0458.352.318**  
**recipient:** orchidee.admin@armonea.be · Rue des Rabots 27, 1460 Ittre · cc AViQ / INAMI · Remy Yves / Jeandel Christine  
**sources:** [CW NL](https://www.companyweb.be/nl/0458352318) · [CW EN](https://www.companyweb.be/en/0458352318) · [CW FR](https://www.companyweb.be/fr/0458352318) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0458352318) · [NBB](https://consult.cbso.nbb.be/consult-enterprise/0458352318)  
**tick:** 2131  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown; KBO Strong)

## Context
- YE **2025** (filed **01.08.2026**): omzet **EUR{OMZET}** JUMP +{OMZET_Yoy}%; bruto **EUR{BRUTO}** JUMP +{BRUTO_Yoy}%; pnl **EUR{PNL}** DROP {PNL_Yoy}%; equity **EUR{EQUITY}** JUMP +{EQUITY_Yoy}% (thin ~4.5pct of omzet; YE2023 negative); FTE **{FTE}** vs 64.8; assets/debt **Unknown**.
- KBO: Actief VZW/ASBL; **1 VE**; NACE **87.301** ROB/MRPA; Remy Yves + Jeandel Christine (Armonea/Colisée path).
- DISTINCT from Restel Flats / Famifamenne / Fakkel / Armonea holding. Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024.

## Brief
```text
[Nom] [Adresse] [E-mail] [Date]
À: L'Orchidée ASBL — Rue des Rabots 27, 1460 Ittre
via orchidee.admin@armonea.be / info@armonea.be
t.a.v. Remy Yves / Jeandel Christine (administrateurs)
cc: AViQ / INAMI
Objet: Publicité compte annuel NBB 2025 L'Orchidée Ittre + matrice bilan/résultat (BCE 0458.352.318)
Madame, Monsieur, sur base du décret wallon sur la publicité de l'administration / règles applicables (MRS), je demande:
1. PDF NBB comptes 2025 (dépôt 01.08.2026) + référence de dépôt.
2. Actifs / dettes LT-CT / trésorerie / total bilan.
3. Split AViQ/INAMI vs contributions résidents (omzet EUR{OMZET}; marge brute EUR{BRUTO}).
4. Explication equity JUMP EUR{EQUITY} (+{EQUITY_Yoy}%) après equity négatif YE2022-23 — apport / regroupement Armonea / extraction?
5. FTE 64.8→{FTE}.
Période 01.01.2025–31.12.2025. Réf: {GAP}
Cordialement, [Nom]
```
- [x] ready NOT sent (human-gated)
"""
FOI_DRAFT.mkdir(parents=True, exist_ok=True)
(FOI_DRAFT / f"{GAP}.md").write_text(foi_text, encoding="utf-8")
print(f"wrote FOI draft {GAP}.md")

log_block = f"""

## Tick 2131 - {UTC} - rq_2131 L'Orchidée Ittre (omzet JUMP 4.47m / thin equity 0.20m / Medium)

- Unit: **rq_2131** leftover dual after **rq_2130 Care-Support EVERY-10**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took deferred unused leftover **L'Orchidée ASBL Ittre** YE2025 (KBO **0458.352.318**; Rue des Rabots 27 Ittre; **VZW/ASBL** NACE **87.301** / **1 VE**; Armonea/Colisée Remy Yves path). Do not redo Care-Support/Restel Flats/De Fakkel/MPC Sint-Franciscus/Famifamenne/SLG Wallonie/Armonea holding.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR{OMZET}** JUMP +{OMZET_Yoy}% vs YE2024 EUR4087776; bruto **EUR{BRUTO}** JUMP +{BRUTO_Yoy}%; pnl **EUR{PNL}** DROP {PNL_Yoy}%; equity **EUR{EQUITY}** JUMP +{EQUITY_Yoy}% (thin ~4.5pct of omzet; YE2023 negative); FTE **{FTE}** vs 64.8; neerlegging **01.08.2026**. Assets/debt Unknown. Medium. Strong KBO. FOI via orchidee.admin@armonea.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi 5.8); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2131=done + rq_2132 open; loop_state ticks=2131; raw docs/doge/data/raw/tick2131/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2130**; next **2140**). Next: rq_2132 (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""

log_text = LOG.read_text(encoding="utf-8")
if "## Tick 2131 -" in log_text:
    print("skip loop_log: Tick 2131 already present")
else:
    LOG.write_text(log_text + log_block, encoding="utf-8")
    print("appended loop_log Tick 2131")

print("tick2131 write complete")
