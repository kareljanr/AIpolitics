# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T19:20:00Z"
TICK = 2148
RQ = "rq_2148"
NEXT_RQ = "rq_2149"
ENTITY = "zs_wallonie_picarde"
GAP = "gap_wapi_budget_jr2025_dotation_commune_fed_matrix_l5"
COMM = "comm_wapi_jr2025_budget_opacity_hvz"
LB = "lb_wapi_hvz_budget_opacity_fte200_jr2025"
SRC_EN = "src_wapi_cw_en_2148"
KBO = "0500.915.621"
KBO_DIGITS = "0500915621"
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
                "leftover dual — Zone de secours Wallonie Picarde HVZ Medium "
                "(FTE 200 / budget Unknown FOI)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} WAPI Medium Strong KBO {KBO} Actief HVZ 8 VE Tournai/Orcq; "
                f"CW FTE {FTE}; omzet/bruto/pnl/equity Unknown (no CW kerncijfers); "
                f"FOI ready budget/dotations; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2150"
            )
            r["instructions"] = (
                f"Completed leftover ZS Wallonie Picarde after Hesbaye; "
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
                    "leftover dual hole-fill after Wallonie Picarde — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Zone de secours Wallonie Picarde HVZ Medium (budget FOI). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Zone de secours Wallonie Picarde, Zone de secours Hesbaye, Zone de secours Hainaut-Centre, "
                    "Zone de secours Dinaphi, Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, "
                    "Denderrust Dienstengroep, Zorgcampus Denderrust, Maison De Repos En Famille, Residence Prestige, "
                    "Les Corolles, l'Esplanade, Les Peupliers, Comte d'Egmont, CIGB Menen, Ten Rozen, L'Orchidée, "
                    "Care-Support, MPC Sint-Franciscus Roosdaal, Brandweerzone Antwerpen, Flemish HVZ stack, "
                    "AGB Bornem, Armonea/emeis/Korian holdings, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, "
                    "EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, "
                    "AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} WAPI HVZ FOI; FARO/AIESH/REW still YE2024; next every-10 2150"
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
        "title": "Companyweb EN Zone de Secours Wallonie Picarde (no YE kerncijfers)",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; ZDS public-law entity; FTE {FTE}; Last balance sheet year empty / "
            f"no omzet-bruto-pnl-equity on free CW; raw docs/doge/data/raw/tick2148/wapi_en.html"
        ),
    },
    {
        "source_id": "src_wapi_cw_nl_2148",
        "title": "Companyweb NL Zone de Secours Wallonie Picarde",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; NL mirror; FTE {FTE}; no YE kerncijfers; raw tick2148/wapi_nl.html",
    },
    {
        "source_id": "src_wapi_cw_fr_2148",
        "title": "Companyweb FR Zone de Secours Wallonie Picarde",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror; raw tick2148/wapi_fr.html",
    },
    {
        "source_id": f"src_wapi_kbo_{TICK}",
        "title": f"KBO Zone de Secours Wallonie Picarde {KBO} Actief HVZ Tournai",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Rechtsvorm Hulpverleningszone sinds 01.01.2015; "
            "Zone de Secours Wallonie Picarde; Chaussée de Lille 422 7501 Tournai; 8 VE; "
            "NACE 84.250; aanbestedende overheid; tel 069 58 08 95; 19 communes Hainaut west"
        ),
    },
    {
        "source_id": f"src_wapi_site_{TICK}",
        "title": "Wallonie Picarde FOI contact info@zswapi.be",
        "url": "https://www.zswapi.be/",
        "publisher": "Zone de Secours Wallonie Picarde",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Siège Chaussée de Lille 422C Orcq; FOI info@zswapi.be; "
            "tel 069 58 08 95; finances 069 620 505; 19 communes"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Zone de secours Wallonie Picarde (HVZ Tournai/Mouscron belt)",
        "name_fr": "Zone de Secours Wallonie Picarde",
        "name_en": "Wallonie Picarde emergency rescue zone",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.zswapi.be/",
        "foi_email": "info@zswapi.be",
        "foi_postal": "Chaussée de Lille 422C, 7501 Orcq",
        "notes": (
            f"tick{TICK} Medium Strong KBO {KBO} Actief Hulpverleningszone + Medium CW FTE {FTE}; "
            f"8 VE; NACE 84.250; omzet/bruto/pnl/equity/budget Unknown (no CW/NBB kerncijfers); "
            f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Hesbaye / Hainaut-Centre / Dinaphi / Brandweerzone Antwerpen / Flemish HVZ; 19 communes"
        ),
    },
)

append_csv(
    DATA / "budgets.csv",
    {
        "budget_id": "bud_wapi_fte_cw_2148",
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
        "title": "Zone de secours Wallonie Picarde leftover HVZ (FTE 200 / budget opacity FOI)",
        "entity_id": ENTITY,
        "beneficiary": "19 communes Wallonie picarde (Tournai/Mouscron/Ath belt)",
        "legal_basis": f"Hulpverleningszone / zone de secours (KBO {KBO}; Actief; 8 VE)",
        "decision_date": "2026-08-25",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "",
        "cash_by_year": (
            f'{{"2025_fte":{FTE},"2025_omzet":"Unknown","2025_budget":"Unknown",'
            f'"ve":8,"communes":19}}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "stated_goal": "Fire / ambulance / rescue services for 19 Walloon municipalities",
        "cut_option": (
            "Publish comptes 2025 + budget 2026 PDF; disclose communal+federal dotation matrix; "
            "FTE professional vs volunteer split"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Hainaut>WalloniePicarde>HVZ_budget_opacity_L5",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; budget Unknown; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Hesbaye/Dinaphi/ZHC/Flemish HVZ"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Zone de secours Wallonie Picarde HVZ budget opacity / FTE 200 / no public YE kerncijfers",
        "level": "L5",
        "type": "hvz_zone",
        "hierarchy_path": "Wallonie>Hainaut>WalloniePicarde>HVZ_opacity",
        "annual_cost_eur": "",
        "total_cost_eur": "",
        "tco_notes": (
            f"Strong KBO Actief HVZ {KBO}; CW FTE {FTE}; 8 VE; 19 communes; "
            "omzet/bruto/pnl/equity/budget Unknown — no free CW/NBB kerncijfers "
            "(contrast Flemish HVZ with public BBC PDFs)"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "19 communes Wallonie picarde",
        "stated_goal": "Fire / ambulance / rescue zone",
        "measured_outcome": f"FTE {FTE} sourced; budget euros Unknown pending FOI",
        "absurdity_score": "7.0",
        "cost_score": "2.2",
        "difficulty": "3.5",
        "priority_index": "5.3",
        "cut_proposal": "FOI comptes 2025 + budget 2026 + communal/federal dotation matrix",
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Hesbaye / Hainaut-Centre / Dinaphi / Brandweerzone Antwerpen / Flemish HVZ"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Hainaut>WalloniePicarde>budget_JR2025_dotation_commune_fed",
        "entity_id": ENTITY,
        "what_is_missing": (
            "Comptes/jaarrekening 2025 PDF; budget 2026; communal dotations per 19 communes; "
            "federal dotation; personnel vs functioning vs invest split; FTE professional vs volunteer"
        ),
        "why_it_matters": (
            "Walloon ZDS Wallonie Picarde has Strong KBO identity and CW FTE 200 but no public YE kerncijfers — "
            "material public-safety spend opacity vs Flemish HVZ with published BBC PDFs"
        ),
        "priority": "8",
        "recipient_body": "Zone de Secours Wallonie Picarde",
        "recipient_email": "info@zswapi.be",
        "recipient_postal": "Chaussée de Lille 422C, 7501 Orcq",
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
                f"tick{TICK} leftover ZS Wallonie Picarde {KBO} Medium (FTE {FTE}; budget/omzet Unknown FOI; "
                f"Actief HVZ 8 VE Tournai/Orcq); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2150; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Zone de secours Wallonie Picarde (FTE 200 / budget Unknown FOI / Medium)

- Unit: **{RQ}** leftover dual after **rq_2147 Hesbaye** (race: concurrent closed 2147 as Hesbaye before this fire). Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW(0644.638.937) still **YE2024**. Took unused leftover **Zone de Secours Wallonie Picarde** (KBO **{KBO}**; Chaussée de Lille 422 Tournai/Orcq; **Hulpverleningszone** / **8 VE**; NACE **84.250**; 19 communes). Do not redo Hesbaye/Hainaut-Centre/Dinaphi/Zonnelied/Care-Ion/Groep SF/Flemish HVZ stack.
- Found: Strong KBO Actief + Medium CW FTE **{FTE}**; **no** CW/NBB YE kerncijfers (omzet/bruto/pnl/equity/budget **Unknown**). FOI via info@zswapi.be for comptes 2025 + budget 2026 + communal/federal dotations. No invented euros.
- Wrote: sources (+5); budgets (+1 FTE-only); commitments (+1); leaderboard (+1 pi 5.3 opacity); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2148/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2140**; next **2150**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "FTE", FTE, "budget Unknown FOI")
