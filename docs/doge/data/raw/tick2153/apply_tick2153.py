# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T21:00:00Z"
TICK = 2153
RQ = "rq_2153"
NEXT_RQ = "rq_2154"
ENTITY = "zs_brabant_wallon"
GAP = "gap_brabant_wallon_budget_jr2025_dotation_commune_fed_matrix_l5"
COMM = "comm_brabant_wallon_jr2025_budget_opacity_hvz"
LB = "lb_brabant_wallon_hvz_budget_opacity_fte200_jr2025"
SRC_EN = "src_bw_cw_en_2153"
KBO = "0500.915.423"
KBO_DIGITS = "0500915423"
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
                "leftover dual — Zone de secours Brabant wallon HVZ Medium "
                "(FTE 200 / budget Unknown FOI)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} Brabant wallon Medium Strong KBO {KBO} Actief HVZ 7 VE Wavre; "
                f"CW FTE {FTE}; omzet/bruto/pnl/equity Unknown (no CW kerncijfers); "
                f"FOI ready; Hainaut-Est 0500.915.819 deferred; AGB Bornem JR2024; "
                f"FARO/AIESH/REW YE2024; next {NEXT_RQ}; next every-10 2160"
            )
            r["instructions"] = (
                f"Completed leftover ZS Brabant wallon after Vesdre; "
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
                    "leftover dual hole-fill after Brabant wallon — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Zone de secours du Brabant wallon HVZ Medium (budget FOI). "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused Hainaut-Est 0500.915.819 (FTE 200 probed) / water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS. "
                    "Do NOT redo Zone de secours Brabant wallon, Zone de secours Vesdre, WZC Annuntiaten Heverlee, "
                    "Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, "
                    "Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, "
                    "Zonnelied Roosdaal, Seniors Care-Ion, Groep Sint-Franciscus Brakel, Brandweerzone Antwerpen, "
                    "Flemish HVZ stack, AGB Bornem, Armonea/emeis/Korian holdings, IPFBW, Aquiris, SPGE, IRE*, "
                    "FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, "
                    "Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Brabant wallon HVZ FOI; Hainaut-Est deferred; "
                    "FARO/AIESH/REW still YE2024; next every-10 2160"
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
        "title": "Companyweb EN Zone de secours du Brabant wallon (no YE kerncijfers)",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; ZDS public-law entity; FTE {FTE}; Last balance sheet year N/A / "
            f"no omzet-bruto-pnl-equity on free CW; raw docs/doge/data/raw/tick2153/bw_en.html"
        ),
    },
    {
        "source_id": "src_bw_cw_nl_2153",
        "title": "Companyweb NL Zone de secours du Brabant wallon",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; NL mirror; FTE {FTE}; Brandweer; no YE kerncijfers; raw tick2153/bw_nl.html",
    },
    {
        "source_id": "src_bw_cw_fr_2153",
        "title": "Companyweb FR Zone de secours du Brabant wallon",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror; raw tick2153/bw_fr.html",
    },
    {
        "source_id": f"src_bw_kbo_{TICK}",
        "title": f"KBO Zone de secours Brabant wallon {KBO} Actief HVZ Wavre",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Rechtsvorm Hulpverleningszone sinds 01.04.2015; "
            "LA ZONE DE SECOURS DU BRABANT WALLON; Chaussée des Collines 52 bus 5 1300 Wavre; 7 VE; "
            "NACE RSZ 84.250 brandweer; aanbestedende overheid sinds 05.10.2012; start 05.10.2012"
        ),
    },
    {
        "source_id": f"src_bw_site_{TICK}",
        "title": "Brabant wallon FOI contact zonedesecours@incendiebw.be (27 communes)",
        "url": "https://brabant-wallon.secourspompiers.be/",
        "publisher": "Zone de secours du Brabant wallon",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Siège/Parc des Collines Wavre; FOI zonedesecours@incendiebw.be; "
            "27 communes province BW; 5 postes + Villers-la-Ville; tel 010/39.55.00"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Zone de secours Brabant Wallon (HVZ provincie BW)",
        "name_fr": "Zone de secours du Brabant wallon",
        "name_en": "Brabant wallon emergency rescue zone",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://brabant-wallon.secourspompiers.be/",
        "foi_email": "zonedesecours@incendiebw.be",
        "foi_postal": "Chaussée des Collines 52 bte 5, 1300 Wavre",
        "notes": (
            f"tick{TICK} Medium Strong KBO {KBO} Actief Hulpverleningszone + Medium CW FTE {FTE}; "
            f"7 VE; NACE 84.250; omzet/bruto/pnl/equity/budget Unknown (no CW/NBB kerncijfers); "
            f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT Vesdre / Val de Sambre / HEMECO / WAPI / Hesbaye / Dinaphi / Hainaut-Centre / Brandweerzone Antwerpen / Flemish HVZ; 27 communes; Hainaut-Est deferred"
        ),
    },
)

append_csv(
    DATA / "budgets.csv",
    {
        "budget_id": "bud_bw_fte_cw_2153",
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
        "title": "Zone de secours Brabant wallon leftover HVZ (FTE 200 / budget opacity FOI)",
        "entity_id": ENTITY,
        "beneficiary": "27 communes Brabant wallon province",
        "legal_basis": f"Hulpverleningszone / zone de secours (KBO {KBO}; Actief; 7 VE; NACE 84.250)",
        "decision_date": "2026-08-25",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "",
        "cash_by_year": (
            f'{{"2025_fte":{FTE},"2025_omzet":"Unknown","2025_budget":"Unknown","ve":7,"communes":27}}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "stated_goal": "Fire / ambulance / rescue services for 27 Brabant wallon municipalities",
        "cut_option": (
            "Publish comptes 2025 + budget 2026 PDF; disclose communal+federal dotation matrix; "
            "FTE professional vs volunteer split"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>BrabantWallon>ZS_BW>HVZ_budget_opacity_L5",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; budget Unknown; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT Vesdre / VDS / HEMECO / WAPI / Flemish HVZ"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Zone de secours Brabant wallon HVZ budget opacity / FTE 200 / no public YE kerncijfers",
        "level": "L5",
        "type": "hvz_zone",
        "hierarchy_path": "Wallonie>BrabantWallon>ZS_BW>HVZ_opacity",
        "annual_cost_eur": "",
        "total_cost_eur": "",
        "tco_notes": (
            f"Strong KBO Actief HVZ {KBO}; CW FTE {FTE}; 7 VE; NACE 84.250; 27 communes (province-wide); "
            "omzet/bruto/pnl/equity/budget Unknown — no free CW/NBB kerncijfers "
            "(contrast Flemish HVZ with public BBC PDFs)"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "27 Brabant wallon communes",
        "stated_goal": "Fire / ambulance / rescue zone",
        "measured_outcome": f"FTE {FTE} sourced; budget euros Unknown pending FOI",
        "absurdity_score": "7.3",
        "cost_score": "3.0",
        "difficulty": "3.5",
        "priority_index": "5.7",
        "cut_proposal": "FOI comptes 2025 + budget 2026 + communal/federal dotation matrix",
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT Vesdre / Val de Sambre / HEMECO / Wallonie Picarde / Hesbaye / Dinaphi / Hainaut-Centre / Brandweerzone Antwerpen / Flemish HVZ; Hainaut-Est deferred"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>BrabantWallon>ZS_BW>budget_JR2025_dotation_commune_fed",
        "entity_id": ENTITY,
        "what_is_missing": (
            "Comptes/jaarrekening 2025 PDF; budget 2026; communal dotations per 27 communes; "
            "federal dotation; personnel vs functioning vs invest split; FTE professional vs volunteer"
        ),
        "why_it_matters": (
            "Walloon ZDS Brabant wallon has Strong KBO identity and CW FTE 200 but no public YE kerncijfers — "
            "province-wide public-safety spend opacity vs Flemish HVZ with published BBC PDFs"
        ),
        "priority": "8",
        "recipient_body": "Zone de secours du Brabant wallon",
        "recipient_email": "zonedesecours@incendiebw.be",
        "recipient_postal": "Chaussée des Collines 52 bte 5, 1300 Wavre",
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
        "notes": f"tick{TICK}; human-send only; Medium; no invented euros; next every-10 2160",
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
                f"tick{TICK} leftover ZS Brabant wallon {KBO} Medium (FTE {FTE}; budget/omzet Unknown FOI; "
                f"Actief HVZ 7 VE Wavre; 27 communes); AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"Hainaut-Est deferred; next {NEXT_RQ}; next every-10 2160; continuous hole_fill"
            ),
        }
    )

update_rq()

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} Zone de secours du Brabant wallon (FTE 200 / budget Unknown FOI / Medium)

- Unit: **{RQ}** leftover dual after **rq_2152 Vesdre**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took unused leftover **Zone de secours du Brabant wallon** (KBO **{KBO}**; Chaussée des Collines 52/5 Wavre; **Hulpverleningszone** / **7 VE**; NACE **84.250**; province-wide **27 communes**). Deferred Hainaut-Est 0500.915.819 (FTE 200 probed). Do not redo Vesdre/Annuntiaten/Val de Sambre/HEMECO/WAPI/Hesbaye/ZHC/Dinaphi/Flemish HVZ stack.
- Found: Strong KBO Actief + Medium CW FTE **{FTE}**; **no** CW/NBB YE kerncijfers (Laatste balansjaar N/A; omzet/bruto/pnl/equity/budget **Unknown**). FOI via zonedesecours@incendiebw.be. No invented euros.
- Wrote: sources (+5); budgets (+1 FTE-only); commitments (+1); leaderboard (+1 pi 5.7 opacity); entities (+1 {ENTITY}); foi + draft {GAP}; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2153/.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**last every-10 was 2150**; next **2160**). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Hainaut-Est / unused).
"""
    )

print("OK tick", TICK, ENTITY, "FTE", FTE, "budget Unknown FOI")
