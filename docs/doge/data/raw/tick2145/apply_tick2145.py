# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T18:20:00Z"
TICK = 2145
RQ = "rq_2145"
NEXT_RQ = "rq_2146"
ENTITY = "zs_hainaut_centre"
GAP = "gap_zhc_hainaut_centre_budget_jr2025_dotation_commune_fed_matrix_l5"
COMM = "comm_zhc_jr2025_budget_opacity_hvz"
LB = "lb_zhc_hvz_budget_opacity_fte200_jr2025"
SRC_EN = "src_zhc_cw_en_2145"
KBO = "0500.916.215"
KBO_DIGITS = "0500916215"
FTE = "200"
ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data"


def append_csv(path, row):
    with open(path, newline="", encoding="utf-8") as f:
        fields = csv.DictReader(f).fieldnames
    out = {k: row.get(k, "") for k in fields}
    with open(path, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields, lineterminator="\n").writerow(out)


def update_rq():
    path = DATA / "research_queue.csv"
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    found = False
    for r in rows:
        if r.get("task_id") == RQ and r.get("status") == "open":
            r["status"] = "done"
            r["entity_id"] = ENTITY
            r["title"] = (
                "leftover dual — Zone de secours Hainaut-Centre HVZ Medium "
                "(FTE 200 / budget Unknown FOI)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} ZHC Medium Strong KBO {KBO} Actief HVZ 11 VE Mons; "
                f"CW FTE {FTE}; omzet/bruto/pnl/equity Unknown (no CW kerncijfers); "
                f"FOI ready budget/dotations; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2150"
            )
            r["instructions"] = (
                f"Completed leftover ZS Hainaut-Centre after Dinaphi; "
                f"preferred AGB Bornem JR2024 / FARO YE2024 / AIESH/REW YE2024; "
                f"Strong KBO {KBO} + Medium CW FTE {FTE}; budget Unknown → FOI {GAP}"
            )
            found = True
            break
    if not found:
        raise SystemExit(f"{RQ} open not found")
    if not any(r.get("task_id") == NEXT_RQ for r in rows):
        rows.append(
            {
                "task_id": NEXT_RQ,
                "title": (
                    "leftover dual hole-fill after Hainaut-Centre — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/Hesbaye/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Zone de secours Hainaut-Centre HVZ Medium (budget FOI). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused ZS Hesbaye 0500.916.512 (FTE 20 probed), else unused water/DSO/IGS/HVZ/energy/"
                    "hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Seniors Care-Ion, "
                    "Groep Sint-Franciscus Brakel, Denderrust Dienstengroep, Zorgcampus Denderrust, "
                    "Maison De Repos En Famille, Residence Prestige, Les Corolles, l'Esplanade, Les Peupliers, "
                    "Comte d'Egmont, CIGB Menen, Ten Rozen, L'Orchidée, Care-Support, MPC Sint-Franciscus Roosdaal, "
                    "Brandweerzone Antwerpen, Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, "
                    "IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
                    "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                    "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} ZHC HVZ FOI; Hesbaye deferred YE-opaque; "
                    "FARO/AIESH/REW still YE2024; next every-10 2150"
                ),
            }
        )
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


for s in [
    {
        "source_id": SRC_EN,
        "title": "Companyweb EN Zone de secours Hainaut-Centre (no YE kerncijfers)",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; ZDS public-law entity; FTE {FTE}; Last balance sheet year empty / "
            f"no omzet-bruto-pnl-equity on free CW; raw docs/doge/data/raw/tick2145/zhc_en.html"
        ),
    },
    {
        "source_id": "src_zhc_cw_nl_2145",
        "title": "Companyweb NL Zone de secours Hainaut-Centre",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; NL mirror; FTE {FTE}; no YE kerncijfers; raw tick2145/zhc_nl.html",
    },
    {
        "source_id": "src_zhc_cw_fr_2145",
        "title": "Companyweb FR Zone de secours Hainaut-Centre",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror; raw tick2145/zhc_fr.html",
    },
    {
        "source_id": f"src_zhc_kbo_{TICK}",
        "title": f"KBO Zone de secours Hainaut-Centre {KBO} Actief HVZ Mons",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Rechtsvorm Hulpverleningszone sinds 01.01.2015; "
            "LA ZONE DE SECOURS HAINAUT-CENTRE; Rue des Sandrinettes 29 7033 Mons; 11 VE; "
            "NACE 84.250 brandweer; aanbestedende overheid sinds 05.10.2012; start 05.10.2012"
        ),
    },
    {
        "source_id": f"src_zhc_site_{TICK}",
        "title": "ZHC FOI contact info@zhc.be / commandant@zhc.be",
        "url": "https://www.zhc.be/",
        "publisher": "Zone de secours Hainaut-Centre",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Siège Rue des Sandrinettes 29 Mons; FOI info@zhc.be; "
            "commandant@zhc.be; tel 065 32 17 00"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Zone de secours Hainaut-Centre (HVZ Mons belt)",
        "name_fr": "Zone de secours Hainaut-Centre",
        "name_en": "Hainaut-Centre emergency rescue zone",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.zhc.be/",
        "foi_email": "info@zhc.be",
        "foi_postal": "Rue des Sandrinettes 29, 7033 Mons",
        "notes": (
            f"tick{TICK} Medium Strong KBO {KBO} Actief Hulpverleningszone + Medium CW FTE {FTE}; "
            f"11 VE; NACE 84.250; omzet/bruto/pnl/equity/budget Unknown (no CW/NBB kerncijfers); "
            f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Dinaphi / Brandweerzone Antwerpen / Flemish HVZ stack; Hesbaye deferred"
        ),
    },
)

append_csv(
    DATA / "budgets.csv",
    {
        "budget_id": "bud_zhc_fte_cw_2145",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": "CW social-balance FTE / Employees (budget euros Unknown)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE only sourced; omzet/spend Unknown pending FOI comptes/budget",
    },
)

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Zone de secours Hainaut-Centre leftover HVZ (FTE 200 / budget opacity FOI)",
        "entity_id": ENTITY,
        "beneficiary": "Communes Hainaut-Centre belt (Mons / La Louvière / …)",
        "legal_basis": f"Hulpverleningszone / zone de secours (KBO {KBO}; Actief; 11 VE; NACE 84.250)",
        "decision_date": "2026-08-25",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "",
        "cash_by_year": (
            f'{{"2025_fte":{FTE},"2025_omzet":"Unknown","2025_budget":"Unknown","ve":11}}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "stated_goal": "Fire / ambulance / rescue services for Hainaut-Centre municipalities",
        "cut_option": (
            "Publish comptes 2025 + budget 2026 PDF; disclose communal+federal dotation matrix; "
            "FTE professional vs volunteer split"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>HainautCentre>HVZ_budget_opacity_L5",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; budget Unknown; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Dinaphi / Flemish HVZ"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Zone de secours Hainaut-Centre HVZ budget opacity / FTE 200 / no public YE kerncijfers",
        "level": "L5",
        "type": "hvz_zone",
        "hierarchy_path": "Wallonie>Hainaut>HainautCentre>HVZ_opacity",
        "annual_cost_eur": "",
        "total_cost_eur": "",
        "tco_notes": (
            f"Strong KBO Actief HVZ {KBO}; CW FTE {FTE}; 11 VE; NACE 84.250; "
            "omzet/bruto/pnl/equity/budget Unknown — no free CW/NBB kerncijfers "
            "(contrast Flemish HVZ with public BBC PDFs)"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "Hainaut-Centre communes",
        "stated_goal": "Fire / ambulance / rescue zone",
        "measured_outcome": f"FTE {FTE} sourced; budget euros Unknown pending FOI",
        "absurdity_score": "7.2",
        "cost_score": "3.0",
        "difficulty": "3.5",
        "priority_index": "5.6",
        "cut_proposal": "FOI comptes 2025 + budget 2026 + communal/federal dotation matrix",
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Dinaphi / Brandweerzone Antwerpen / Flemish HVZ; Hesbaye deferred"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>HainautCentre>budget_JR2025_dotation_commune_fed",
        "entity_id": ENTITY,
        "what_is_missing": (
            "Comptes/jaarrekening 2025 PDF; budget 2026; communal dotations per member commune; "
            "federal dotation; personnel vs functioning vs invest split; FTE professional vs volunteer"
        ),
        "why_it_matters": (
            "Walloon ZDS Hainaut-Centre has Strong KBO identity and CW FTE 200 but no public YE kerncijfers — "
            "material public-safety spend opacity vs Flemish HVZ with published BBC PDFs"
        ),
        "priority": "8",
        "recipient_body": "Zone de secours Hainaut-Centre",
        "recipient_email": "info@zhc.be",
        "recipient_postal": "Rue des Sandrinettes 29, 7033 Mons",
        "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
        "status": "ready",
        "date_ready": "2026-08-25",
        "date_sent": "",
        "date_due": "",
        "date_answered": "",
        "response_summary": "",
        "linked_commitment_id": COMM,
        "linked_leaderboard_id": LB,
        "created_utc": UTC,
        "updated_utc": UTC,
        "notes": f"tick{TICK}; human-send only; Medium; no invented euros; next every-10 2150",
    },
)

with open(DATA / "loop_state.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ],
        lineterminator="\n",
    )
    w.writeheader()
    w.writerow(
        {
            "state_id": "main",
            "mode": "continuous",
            "current_sprint": "hole_fill",
            "last_tick_utc": UTC,
            "last_unit_id": RQ,
            "ticks_completed": str(TICK),
            "paused": "no",
            "notes": (
                f"tick{TICK} leftover ZS Hainaut-Centre {KBO} Medium (FTE {FTE}; budget/omzet Unknown FOI; "
                f"Actief HVZ 11 VE Mons); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Hesbaye deferred; "
                f"next {NEXT_RQ}; next every-10 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Zone de secours Hainaut-Centre (FTE 200 / budget Unknown FOI / Medium)

- Unit: **{RQ}** leftover dual after **rq_2144 ZS Dinaphi**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Zone de secours Hainaut-Centre** (KBO **{KBO}**; Rue des Sandrinettes 29 Mons; **Hulpverleningszone** / **11 VE**; NACE **84.250**; aanbestedende overheid). Deferred ZS Hesbaye 0500.916.512 (FTE 20, same opacity class). Do not redo Dinaphi/Care-Ion/Groep SF/Flemish HVZ stack/Brandweerzone Antwerpen.
- Found: Strong KBO Actief + Medium CW FTE **{FTE}**; **no** CW/NBB YE kerncijfers (omzet/bruto/pnl/equity/budget **Unknown**). FOI via info@zhc.be for comptes 2025 + budget 2026 + communal/federal dotations. No invented euros.
- Wrote: sources (+5); budgets (+1 FTE-only); commitments (+1); leaderboard (+1 pi 5.6 opacity); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2145/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2140**; next **2150**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Hesbaye / unused).
"""
    )

print("OK tick", TICK, ENTITY, "FTE", FTE, "budget Unknown FOI")
