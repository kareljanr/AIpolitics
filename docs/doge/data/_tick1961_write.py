# tick 1961 — IPFBW YE2025 Strong auditor + Medium CW (rq_1961 after Aquiris EVERY-10)
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
        "source_id": "src_ipfbw_jr2025_rsm",
        "title": "RSM commissaire report IPFBW comptes 31.12.2025",
        "url": "https://www.wavre.be/sites/wavre/files/media/file/IPFBW%20-%20Rapport%20du%20commissaire%20RSM%20-%2012-05-2026.pdf",
        "publisher": "RSM Belgium (commissaire IPFBW) via Wavre",
        "accessed_date": "2026-08-23",
        "source_class": "official_audit",
        "notes": (
            "tick1961; Strong; bilan total EUR341059081.57; benefice exercice EUR10912136.13; "
            "opinion sans reserve; AG nomination 10.06.2025"
        ),
    },
    {
        "source_id": "src_ipfbw_jr2025_cw",
        "title": "Companyweb IPFBW YE2025 NBB-derived summary",
        "url": "https://www.companyweb.be/nl/0206041757/intercommunale-pure-de-financement-du-brabant-wallon",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": (
            "tick1961; Laatste balansjaar 2025; neerlegging 04.07.2026; "
            "pnl 10912136 +6.4pct; equity 228950352 +2.19pct; bruto NEG -187231; "
            "omzet 10500; FTE 1"
        ),
    },
    {
        "source_id": "src_ipfbw_kbo_1961",
        "title": "KBO IPFBW 0206.041.757 Actief CV publiek recht",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0206041757",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": (
            "tick1961; Actief CV publiek recht; Avenue Jean Monnet 2 1348 OLLN; "
            "aanbestedende overheid; email officiel.ic-ipfbw@ipfbw.be; "
            "absorbed Energie Brabant Wallon 0882.039.509 since 12.12.2023"
        ),
    },
]
sources_new = [s for s in sources_new if s["source_id"] not in existing_src]
if sources_new:
    append_csv(DATA / "sources.csv", sources_new)

existing_ent = set()
with (DATA / "entities.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_ent.add(row.get("entity_id") or "")

ent_notes = (
    "tick1961 YE2025 Strong RSM+Medium CW KBO 0206.041.757 Actief CV publiek recht; "
    "assets 341.06m pnl JUMP 10.91m equity 228.95m bruto NEG -0.19m omzet 10.5k FTE 1; "
    "FOI gap_ipfbw_nbb_pdf_debt_commune_share_ebw_l5; absorbed EBW 2023; dual inBW"
)

if "igs_ipfbw" not in existing_ent:
    append_csv(
        DATA / "entities.csv",
        [
            {
                "entity_id": "igs_ipfbw",
                "name_nl": "IPFBW / Intercommunale pure de financement du Brabant Wallon",
                "name_fr": "IPFBW / Intercommunale pure de financement du Brabant Wallon",
                "name_en": "IPFBW — pure financing intercommunale Brabant wallon communes",
                "level": "igs",
                "parent_id": "prov_brabant_wallon",
                "community_language": "fr",
                "website": "https://www.ipfbw.be",
                "foi_email": "officiel.ic-ipfbw@ipfbw.be",
                "foi_postal": "Avenue Jean Monnet 2 1348 Ottignies-Louvain-la-Neuve",
                "notes": ent_notes,
            }
        ],
    )
else:
    update_csv_rows(
        DATA / "entities.csv",
        "entity_id",
        {
            "igs_ipfbw": {
                "foi_email": "officiel.ic-ipfbw@ipfbw.be",
                "foi_postal": "Avenue Jean Monnet 2 1348 Ottignies-Louvain-la-Neuve",
                "notes": ent_notes,
            }
        },
    )

existing_bud = set()
with (DATA / "budgets.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_bud.add(row.get("budget_id") or "")

budgets_new = [
    {
        "budget_id": "bud_ipfbw_assets_jr2025",
        "entity_id": "igs_ipfbw",
        "year": "2025",
        "amount_eur": "341059082",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "RSM commissaire bilan total 31.12.2025",
        "source_id": "src_ipfbw_jr2025_rsm",
        "confidence": "strong",
        "notes": "tick1961; YE2025 assets 341059081.57 rounded; YE2024 CW/Upswitch 332609340",
    },
    {
        "budget_id": "bud_ipfbw_pnl_jr2025",
        "entity_id": "igs_ipfbw",
        "year": "2025",
        "amount_eur": "10912136",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "RSM commissaire benefice + CW 9904",
        "source_id": "src_ipfbw_jr2025_rsm",
        "confidence": "strong",
        "notes": "tick1961; YE2025 pnl 10912136 +6.4pct vs CW YE2024 10255819",
    },
    {
        "budget_id": "bud_ipfbw_equity_jr2025",
        "entity_id": "igs_ipfbw",
        "year": "2025",
        "amount_eur": "228950352",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived equity",
        "source_id": "src_ipfbw_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 equity 228950352 +2.19pct vs 224037949",
    },
    {
        "budget_id": "bud_ipfbw_bruto_jr2025",
        "entity_id": "igs_ipfbw",
        "year": "2025",
        "amount_eur": "-187231",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived brutomarge NEG",
        "source_id": "src_ipfbw_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 bruto NEG -187231 IMPROVED vs -207313; financing shell",
    },
    {
        "budget_id": "bud_ipfbw_omzet_jr2025",
        "entity_id": "igs_ipfbw",
        "year": "2025",
        "amount_eur": "10500",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived omzet",
        "source_id": "src_ipfbw_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 omzet 10500 nominal; financing IGS not trading utility",
    },
    {
        "budget_id": "bud_ipfbw_fte_jr2025",
        "entity_id": "igs_ipfbw",
        "year": "2025",
        "amount_eur": "1",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW NBB-derived FTE",
        "source_id": "src_ipfbw_jr2025_cw",
        "confidence": "medium",
        "notes": "tick1961; YE2025 FTE 1; dagelijks bestuur Sarah Gillard KBO",
    },
]
budgets_new = [b for b in budgets_new if b["budget_id"] not in existing_bud]
if budgets_new:
    append_csv(DATA / "budgets.csv", budgets_new)

existing_comm = set()
with (DATA / "commitments.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_comm.add(row.get("commitment_id") or "")

if "comm_ipfbw_jr2025_assets" not in existing_comm:
    append_csv(
        DATA / "commitments.csv",
        [
            {
                "commitment_id": "comm_ipfbw_jr2025_assets",
                "title": "IPFBW YE2025 leftover BW financing IGS (assets 341.1m / pnl JUMP 10.91m / equity 229.0m)",
                "entity_id": "igs_ipfbw",
                "beneficiary": "Brabant wallon communes / provincial financing dual vs inBW",
                "legal_basis": "CV publiek recht; aanbestedende overheid; NBB neerlegging; CDLD",
                "decision_date": "2026-05-12",
                "start_year": "2025",
                "end_year": "2025",
                "total_envelope_eur": "341059082",
                "cash_by_year": (
                    "2025:assets=341059082;pnl=10912136;equity=228950352;"
                    "bruto=-187231;omzet=10500;fte=1;debt=Unknown"
                ),
                "remaining_eur": "",
                "status": "active",
                "evaluation_url": "https://www.wavre.be/sites/wavre/files/media/file/IPFBW%20-%20Rapport%20du%20commissaire%20RSM%20-%2012-05-2026.pdf",
                "stated_goal": "Pure financing intercommunale for Brabant wallon communes",
                "cut_option": "FOI NBB PDF + debt + commune share/dividend + EBW integration vs inBW",
                "source_id": "src_ipfbw_jr2025_rsm",
                "confidence": "strong",
                "hierarchy_path": "Belgie>Wallonie>Brabant_wallon>IPFBW>JR2025_L5",
                "notes": (
                    "tick1961; Strong RSM assets/pnl + Medium CW equity; preferred AGB Bornem JR2024 / "
                    "FARO/AIESH/REW YE2024; do not redo Aquiris/SPGE/SWDE/CILE/Hydria/Vivaqua/nuclear stack"
                ),
            }
        ],
    )

existing_lb = set()
with (DATA / "leaderboard.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_lb.add(row.get("item_id") or "")

# pi = 0.55*5.5 + 0.35*5.5 + 0.10*(10-3.0) = 3.025+1.925+0.7 = 5.65 -> 5.7
if "lb_ipfbw_assets_341_1m_pnl_jump_10_91m_jr2025" not in existing_lb:
    append_csv(
        DATA / "leaderboard.csv",
        [
            {
                "item_id": "lb_ipfbw_assets_341_1m_pnl_jump_10_91m_jr2025",
                "name": "IPFBW assets 341.1m / pnl JUMP 10.91m (BW pure financing IGS dual inBW)",
                "level": "L5",
                "type": "financing_igs_dual",
                "hierarchy_path": "Belgie>Wallonie>Brabant_wallon>IPFBW>JR2025_L5",
                "annual_cost_eur": "10912136",
                "total_cost_eur": "341059082",
                "tco_notes": (
                    "assets 341059082 pnl 10912136 equity 228950352 bruto NEG -187231 "
                    "omzet 10500 FTE 1; debt Unknown; absorbed EBW 2023"
                ),
                "confidence": "strong",
                "source_id": "src_ipfbw_jr2025_rsm",
                "beneficiaries": "BW communes / provincial financing path",
                "stated_goal": "Pure financing intercommunale Brabant wallon",
                "measured_outcome": "RSM Strong assets/pnl; CW equity; NBB PDF body unresolved",
                "absurdity_score": "5.5",
                "cost_score": "5.5",
                "difficulty": "3.0",
                "priority_index": "5.7",
                "cut_proposal": "Publish NBB PDF + debt + commune share matrix + EBW/inBW dual flows",
                "status": "active",
                "struck_reason": "",
                "notes": "tick1961; Strong RSM; leftover after Aquiris EVERY-10; not TE-additive pure-waste top10",
            }
        ],
    )

existing_foi = set()
with (DATA / "foi_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_foi.add(row.get("gap_id") or "")

if "gap_ipfbw_nbb_pdf_debt_commune_share_ebw_l5" not in existing_foi:
    append_csv(
        DATA / "foi_queue.csv",
        [
            {
                "gap_id": "gap_ipfbw_nbb_pdf_debt_commune_share_ebw_l5",
                "hierarchy_path": "Belgie>Wallonie>Brabant_wallon>IPFBW>nbb_pdf_debt_L5",
                "entity_id": "igs_ipfbw",
                "what_is_missing": (
                    "NBB deposit PDF body YE2025; LT/ST debt + cash + portfolio recon to assets "
                    "341059082; commune/provincial share register + 2025 dividend/restitution; "
                    "Energie Brabant Wallon integration + dual flows vs inBW"
                ),
                "why_it_matters": (
                    "BW pure financing IGS with 341m assets / 11m pnl / 1 FTE — debt and commune "
                    "ownership opaque; dual-count risk vs inBW operating shell + absorbed EBW"
                ),
                "priority": "8",
                "recipient_body": "IPFBW",
                "recipient_email": "officiel.ic-ipfbw@ipfbw.be",
                "recipient_postal": "Avenue Jean Monnet 2 1348 Ottignies-Louvain-la-Neuve (cc inBW)",
                "draft_letter_path": "docs/doge/foi/drafts/gap_ipfbw_nbb_pdf_debt_commune_share_ebw_l5.md",
                "status": "ready",
                "date_ready": "2026-08-23",
                "date_sent": "",
                "date_due": "",
                "date_answered": "",
                "response_summary": "",
                "linked_commitment_id": "comm_ipfbw_jr2025_assets",
                "linked_leaderboard_id": "lb_ipfbw_assets_341_1m_pnl_jump_10_91m_jr2025",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "tick1961; human-send only; Strong RSM + Medium CW",
            }
        ],
    )

update_csv_rows(
    DATA / "research_queue.csv",
    "task_id",
    {
        "rq_1961": {
            "status": "done",
            "entity_id": "igs_ipfbw",
            "updated_utc": TS,
            "title": "leftover dual hole-fill after Aquiris EVERY-10 — IPFBW YE2025 Strong",
            "blocked_gap_id": "gap_ipfbw_nbb_pdf_debt_commune_share_ebw_l5",
            "notes": (
                "tick1961 IPFBW YE2025 Strong RSM assets 341.1m pnl JUMP 10.91m; "
                "preferred AGB Bornem JR2024 / FARO YE2024 / AIESH YE2024"
            ),
        }
    },
)

existing_rq = set()
with (DATA / "research_queue.csv").open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        existing_rq.add(row.get("task_id") or "")

if "rq_1962" not in existing_rq:
    append_csv(
        DATA / "research_queue.csv",
        [
            {
                "task_id": "rq_1962",
                "title": "leftover dual hole-fill after IPFBW",
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                    "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/nuclear. "
                    "Do NOT redo IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, BRUGEL, "
                    "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                    "Synatom, Atrias, AIEG, Synergrid, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE."
                ),
                "blocked_gap_id": "",
                "created_utc": TS,
                "updated_utc": TS,
                "notes": "tick1961; next after IPFBW; next every-10 1970",
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
            "last_unit_id": "rq_1961",
            "ticks_completed": "1961",
            "paused": "no",
            "notes": (
                "tick1961 leftover IPFBW 0206.041.757 Strong RSM+Medium CW "
                "(assets 341.06m pnl JUMP 10.91m equity 228.95m bruto NEG -0.19m FTE 1); "
                "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1962; "
                "next every-10 1970; continuous hole_fill"
            ),
        }
    },
)

log_path = ROOT / "docs" / "doge" / "loop_log.md"
log_block = f"""

## Tick 1961 - {TS} - rq_1961 IPFBW (assets 341.1m / pnl JUMP 10.91m / Strong)

- Unit: **rq_1961** leftover dual after concurrent **rq_1960 EVERY-10 + Aquiris** (already on main). Prefer NON-Eneco live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024**. Took leftover **IPFBW** (KBO **0206.041.757**; Avenue Jean Monnet 2 OLLN; pure financing intercommunale BW; aanbestedende overheid; absorbed Energie Brabant Wallon 12.12.2023). Do not redo Aquiris/SPGE/SWDE/CILE/Hydria/Vivaqua/IRE*/FANC/SCK/EURIDICE/BRUGEL/nuclear stack.
- Primary: Strong [RSM commissaire YE2025 PDF](https://www.wavre.be/sites/wavre/files/media/file/IPFBW%20-%20Rapport%20du%20commissaire%20RSM%20-%2012-05-2026.pdf) (assets **EUR341,059,082**; PnL **EUR10,912,136**) + Medium [Companyweb](https://www.companyweb.be/nl/0206041757/intercommunale-pure-de-financement-du-brabant-wallon) + Strong KBO (neerlegging **04.07.2026**): equity **EUR228,950,352** (**JUMP +2.19%**); bruto **NEG EUR-187,231**; omzet **EUR10,500**; FTE **1**; debt **Unknown**.
- Wrote: sources (+3); budgets (+6); commitments (+1); leaderboard (+1); entities (+1 igs_ipfbw); foi + draft gap_ipfbw_nbb_pdf_debt_commune_share_ebw_l5; rq_1961=done + rq_1962 open; loop_state ticks=1961.
- FOI opened: NBB PDF + debt + commune share + EBW/inBW dual (**ready**, human-send only).
- NOT every-10 (**1960 EVERY-10 already done with Aquiris**; next every-10 is **1970**). Next: rq_1962 (AGB/FARO-if-YE2025 / AIESH-REW-if-YE2025 / otherHVZ-IGS).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log_block)

print("tick1961 write OK")
