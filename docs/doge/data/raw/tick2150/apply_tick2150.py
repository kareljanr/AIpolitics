# -*- coding: utf-8 -*-
import csv
from pathlib import Path

csv.field_size_limit(10**7)
UTC = "2026-08-25T20:00:00Z"
TICK = 2150
RQ = "rq_2150"
NEXT_RQ = "rq_2151"
ENTITY = "zs_val_de_sambre"
GAP = "gap_val_de_sambre_budget_jr2025_dotation_commune_fed_matrix_l5"
COMM = "comm_val_de_sambre_jr2025_budget_opacity_hvz"
LB = "lb_val_de_sambre_hvz_budget_opacity_fte50_jr2025"
SRC_EN = "src_vds_cw_en_2150"
KBO = "0500.927.004"
KBO_DIGITS = "0500927004"
FTE = "50"
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
                "EVERY-10 leftover dual — Zone de secours Val de Sambre HVZ Medium "
                "(FTE 50 / budget Unknown FOI)"
            )
            r["blocked_gap_id"] = GAP
            r["updated_utc"] = UTC
            r["notes"] = (
                f"tick{TICK} EVERY-10 VDS Medium Strong KBO {KBO} Actief HVZ 3 VE Sambreville; "
                f"CW FTE {FTE}; Budget 2026 avis on-site only (no public euros); "
                f"omzet/bruto/pnl Unknown; FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2160"
            )
            r["instructions"] = (
                f"Completed EVERY-10 leftover ZS Val de Sambre after HEMECO; "
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
                    "leftover dual hole-fill after Val de Sambre — prefer "
                    "AGB/FARO-YE2025/AIESH-REW/unused IGS-DSO-WZC-MRS"
                ),
                "sprint": "hole_fill",
                "priority": "8",
                "status": "open",
                "hierarchy_target": "L5",
                "entity_id": "",
                "instructions": (
                    f"Tick {TICK + 1} after Zone de secours Val de Sambre HVZ Medium (budget FOI) + EVERY-10@{TICK}. "
                    "Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, "
                    "else unused Vesdre / water/DSO/IGS/HVZ/energy/hospital/WZC/psych/MRS/creche/disability/thuiszorg. "
                    "Do NOT redo Zone de secours Val de Sambre, Zone de secours HEMECO, Zone de secours Wallonie Picarde, "
                    "Zone de secours Hesbaye, Zone de secours Hainaut-Centre, Zone de secours Dinaphi, Zonnelied Roosdaal, "
                    "Seniors Care-Ion, Groep Sint-Franciscus Brakel, Denderrust Dienstengroep, Zorgcampus Denderrust, "
                    "Maison De Repos En Famille, Residence Prestige, Les Corolles, Brandweerzone Antwerpen, Flemish HVZ stack, "
                    "AGB Bornem, Armonea/emeis/Korian holdings, IPFBW, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, "
                    "Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, "
                    "Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL."
                ),
                "blocked_gap_id": "",
                "created_utc": UTC,
                "updated_utc": UTC,
                "notes": (
                    f"spawned after tick{TICK} Val de Sambre HVZ FOI + EVERY-10; "
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
        "title": "Companyweb EN Zone de secours Val de Sambre (no YE kerncijfers)",
        "url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": (
            f"tick{TICK}; ZDS public-law entity; FTE {FTE}; Last balance sheet year N/A / "
            f"no omzet-bruto-pnl-equity on free CW; raw docs/doge/data/raw/tick2150/vds_en.html"
        ),
    },
    {
        "source_id": "src_vds_cw_nl_2150",
        "title": "Companyweb NL Zone de secours Val de Sambre",
        "url": f"https://www.companyweb.be/nl/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; NL mirror; FTE {FTE}; Brandweer; no YE kerncijfers; raw tick2150/vds_nl.html",
    },
    {
        "source_id": "src_vds_cw_fr_2150",
        "title": "Companyweb FR Zone de secours Val de Sambre",
        "url": f"https://www.companyweb.be/fr/{KBO_DIGITS}",
        "publisher": "Companyweb",
        "accessed_date": "2026-08-25",
        "source_class": "secondary_aggregator",
        "notes": f"tick{TICK}; FR mirror; raw tick2150/vds_fr.html",
    },
    {
        "source_id": f"src_vds_kbo_{TICK}",
        "title": f"KBO Zone de secours Val de Sambre {KBO} Actief HVZ Sambreville",
        "url": (
            "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html"
            f"?lang=nl&ondernemingsnummer={KBO_DIGITS}"
        ),
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-25",
        "source_class": "official_register",
        "notes": (
            f"tick{TICK}; Status Actief; Rechtsvorm Hulpverleningszone sinds 01.01.2015; "
            "LA ZONE DE SECOURS VAL DE SAMBRE; Rue de la Vacherie 78 5060 Sambreville; 3 VE; "
            "NACE RSZ 84.250 brandweer; aanbestedende overheid sinds 05.10.2012; tel 071/12 14 29; start 05.10.2012"
        ),
    },
    {
        "source_id": f"src_vds_site_{TICK}",
        "title": "Val de Sambre FOI contact + Budget 2026 avis (on-site consultation)",
        "url": "https://www.zonevaldesambre.be/",
        "publisher": "Zone de secours Val de Sambre",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Siège Rue de la Vacherie 78 Sambreville; info@ / facturation@zonevaldesambre.be; "
            "6 communes; 3 postes; Budget 2026 avis PDF = consultation on-site only (no public euro figures)"
        ),
    },
    {
        "source_id": f"src_vds_budget_avis_pdf_{TICK}",
        "title": "Avis de publication Budget 2026 Val de Sambre (PDF)",
        "url": "https://www.zonevaldesambre.be/wp-content/uploads/2026/02/avis-de-publication-budget-2026.pdf",
        "publisher": "Zone de secours Val de Sambre",
        "accessed_date": "2026-08-25",
        "source_class": "official_org",
        "notes": (
            f"tick{TICK}; Budget 2026 adopté Conseil 27.01.2026; avis 03.02.2026; "
            "consultation siège + maisons communales 15 jours; NO euro totals in avis PDF; "
            "raw tick2150/vds_budget2026_avis.pdf"
        ),
    },
]:
    append_csv(DATA / "sources.csv", s)

append_csv(
    DATA / "entities.csv",
    {
        "entity_id": ENTITY,
        "name_nl": "Zone de secours Val de Sambre (HVZ Sambreville belt)",
        "name_fr": "Zone de secours Val de Sambre",
        "name_en": "Val de Sambre emergency rescue zone",
        "level": "parastatal",
        "parent_id": "sec_wallonia",
        "community_language": "fr",
        "website": "https://www.zonevaldesambre.be/",
        "foi_email": "info@zonevaldesambre.be",
        "foi_postal": "Rue de la Vacherie 78, 5060 Sambreville",
        "notes": (
            f"tick{TICK} EVERY-10 Medium Strong KBO {KBO} Actief Hulpverleningszone + Medium CW FTE {FTE}; "
            f"3 VE; NACE 84.250; omzet/bruto/pnl/equity/budget Unknown (no CW/NBB kerncijfers; Budget 2026 avis on-site only); "
            f"FOI {GAP}; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
            "DISTINCT HEMECO / WAPI / Hesbaye / Dinaphi / Hainaut-Centre / Brandweerzone Antwerpen / Flemish HVZ; 6 communes"
        ),
    },
)

append_csv(
    DATA / "budgets.csv",
    {
        "budget_id": "bud_vds_fte_cw_2150",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": FTE,
        "amount_max_eur": FTE,
        "basis": "CW social-balance FTE / Employees (budget euros Unknown; Budget 2026 avis on-site only)",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick{TICK}; FTE only sourced; omzet/spend Unknown pending FOI comptes/budget PDF",
    },
)

append_csv(
    DATA / "commitments.csv",
    {
        "commitment_id": COMM,
        "title": "Zone de secours Val de Sambre leftover HVZ (FTE 50 / budget opacity FOI)",
        "entity_id": ENTITY,
        "beneficiary": "6 communes Val de Sambre (Namur province)",
        "legal_basis": f"Hulpverleningszone / zone de secours (KBO {KBO}; Actief; 3 VE; NACE 84.250)",
        "decision_date": "2026-08-25",
        "start_year": "2025",
        "end_year": "2026",
        "total_envelope_eur": "",
        "cash_by_year": (
            f'{{"2025_fte":{FTE},"2025_omzet":"Unknown","2025_budget":"Unknown","2026_budget_avis":"on_site_only","ve":3,"communes":6}}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": f"https://www.companyweb.be/en/{KBO_DIGITS}",
        "stated_goal": "Fire / ambulance / rescue services for 6 Val de Sambre municipalities",
        "cut_option": (
            "Publish comptes 2025 + budget 2026 PDF (beyond on-site avis); disclose communal+federal "
            "dotation matrix; FTE professional vs volunteer split"
        ),
        "source_id": SRC_EN,
        "confidence": "medium",
        "hierarchy_path": "Wallonie>Namur>ValDeSambre>HVZ_budget_opacity_L5",
        "notes": (
            f"tick{TICK}; Medium; no invented euros; budget Unknown; AGB Bornem JR2024; "
            "FARO/AIESH/REW YE2024; not TE-additive of 348bn; DISTINCT HEMECO / WAPI / Hesbaye / Dinaphi / ZHC / Flemish HVZ"
        ),
    },
)

append_csv(
    DATA / "leaderboard.csv",
    {
        "item_id": LB,
        "name": "Zone de secours Val de Sambre HVZ budget opacity / FTE 50 / Budget 2026 on-site only",
        "level": "L5",
        "type": "hvz_zone",
        "hierarchy_path": "Wallonie>Namur>ValDeSambre>HVZ_opacity",
        "annual_cost_eur": "",
        "total_cost_eur": "",
        "tco_notes": (
            f"Strong KBO Actief HVZ {KBO}; CW FTE {FTE}; 3 VE; NACE 84.250; 6 communes; "
            "Budget 2026 adopted 27.01.2026 but avis = on-site consultation only; "
            "omzet/bruto/pnl/equity/budget Unknown — no free CW/NBB kerncijfers "
            "(contrast Flemish HVZ with public BBC PDFs)"
        ),
        "confidence": "medium",
        "source_id": SRC_EN,
        "beneficiaries": "6 Val de Sambre communes",
        "stated_goal": "Fire / ambulance / rescue zone",
        "measured_outcome": f"FTE {FTE} sourced; Budget 2026 avis without euros; spend Unknown pending FOI",
        "absurdity_score": "7.1",
        "cost_score": "2.0",
        "difficulty": "3.5",
        "priority_index": "5.25",
        "cut_proposal": "FOI comptes 2025 + budget 2026 PDF + communal/federal dotation matrix",
        "status": "open",
        "struck_reason": "",
        "notes": (
            f"tick{TICK}; EVERY-10; Medium; no invented euros; FOI {GAP}; FARO/AIESH/REW YE2024; "
            "DISTINCT HEMECO / Wallonie Picarde / Hesbaye / Dinaphi / Hainaut-Centre / Brandweerzone Antwerpen / Flemish HVZ"
        ),
    },
)

append_csv(
    DATA / "foi_queue.csv",
    {
        "gap_id": GAP,
        "hierarchy_path": "Wallonie>Namur>ValDeSambre>budget_JR2025_dotation_commune_fed",
        "entity_id": ENTITY,
        "what_is_missing": (
            "Comptes/jaarrekening 2025 PDF; budget 2026 PDF (beyond on-site avis); communal dotations per 6 communes; "
            "federal dotation; personnel vs functioning vs invest split; FTE professional vs volunteer"
        ),
        "why_it_matters": (
            "Walloon ZDS Val de Sambre has Strong KBO identity and CW FTE 50; Budget 2026 adopted but euros only "
            "on-site — material public-safety spend opacity vs Flemish HVZ with published BBC PDFs"
        ),
        "priority": "8",
        "recipient_body": "Zone de secours Val de Sambre",
        "recipient_email": "info@zonevaldesambre.be",
        "recipient_postal": "Rue de la Vacherie 78, 5060 Sambreville",
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
        "notes": f"tick{TICK}; EVERY-10; human-send only; Medium; no invented euros; next every-10 2160",
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
                f"tick{TICK} EVERY-10 leftover ZS Val de Sambre {KBO} Medium (FTE {FTE}; "
                f"Budget 2026 avis on-site only / omzet Unknown FOI; Actief HVZ 3 VE Sambreville) "
                f"+ progress/top10 refresh; AGB Bornem JR2024; FARO/AIESH/REW YE2024; "
                f"next {NEXT_RQ}; next every-10 2160; continuous hole_fill"
            ),
        }
    )

update_rq()

# inventory for every-10
counts = {}
for fn in [
    "budgets.csv",
    "commitments.csv",
    "leaderboard.csv",
    "entities.csv",
    "sources.csv",
    "foi_queue.csv",
]:
    with (DATA / fn).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    counts[fn] = len(rows)
    if fn == "foi_queue.csv":
        counts["foi_ready"] = sum(1 for r in rows if r.get("status") == "ready")
        counts["foi_answered"] = sum(1 for r in rows if r.get("status") == "answered")
        counts["foi_partial"] = sum(1 for r in rows if r.get("status") == "partial")

progress = f"""# DOGE progress — every 10 ticks

**Protocol:** At ticks **10, 20, 30, …** (and anytime human asks), refresh this file **and** append a short block to `loop_log.md`.  
**Anchor:** ESA S.13 total expenditure **€347.956 bn (2025)** = 100% of the “public spend pie” for flow coverage.  
**Rule:** no invented euros; **never** sum all `budgets.csv` rows (double-count debt, multi-year envelopes, subtotals).

---

## Snapshot at **tick 2150** (2026-08-25)

| Layer | Coverage of EUR 347.956 bn TE | Assessment |
|-------|---------------------------:|------------|
| **A. L0 total** | **100%** | Strong (NBB/ESA 2025 TE EUR 347.956bn) |
| **B. L1 subsectors** | **100%** of unconsol. map | Strong; fed/C&R/local/SS |
| **C. L2 entity totals** | **~99%** (order of magnitude) | **+** residual dual 2141-2150 WZC/MRS + Walloon HVZ opacity continuum after 2140 Denderrust |
| **D. L5 named / measure end-lines** | **~74-88%** of TE (generous) | **Gain 2141-2150 is residual dual L5 (not near-complete of 348bn):** **Denderrust Dienstengroep** omzet **0.63m** Stopgezet fusie · **Groep Sint-Franciscus Brakel** omzet JUMP **31.0m** / pnl FLIP PROFIT · **Seniors Care-Ion** omzet JUMP **86.0m** / equity DROP / pnl LOSS · **Zonnelied** bruto JUMP **24.0m** / pnl DROP · **Dinaphi** FTE **50** budget Unknown FOI · **Hainaut-Centre** FTE **200** FOI · **Hesbaye** FTE **20** FOI · **Wallonie Picarde** FTE **200** FOI · **HEMECO** FTE **50** FOI · **Val de Sambre** FTE **50** / Budget 2026 on-site avis only (this tick EVERY-10) Medium |
| **E. FOI-ready gaps** | **~{counts['foi_ready']}** drafts ready | Human send only; answered **~{counts['foi_answered']}**; partial **~{counts['foi_partial']}**; total FOI rows **~{counts['foi_queue.csv']}** |

**Off-TE (do not mix into 348 bn):** federal taxex **EUR 29.7bn+** · company cars/cheque/EIWT · lottery · Tax Shelter · private PPP · equity injections · reform savings paths · **gross financing / OLO** · **debt principal repay** · **SAFE loans EUR8.34bn BE** · **Entity II HermReg soldes EUR7.9bn** · **VL/WAL/FWB/BCR debt stocks** · **Hedera CAP EUR15bn** · **MOG II / PE Island multi-bn grid** · **Metro3 multi-bn** · **university/city balance sheets** · **AGB/zorg/APB/EVA/IGS/NV/cv dual + commercial WZC/HVZ/thuiszorg/property/renewable/energy/nuclear/water/forest/hospital/psych/creche/disability shells** (**NEW 2141-2150** Denderrust Dienstengroep · Groep Sint-Franciscus · Care-Ion · Dinaphi · Hainaut-Centre · Zonnelied · Hesbaye · Wallonie Picarde · HEMECO · **Val de Sambre** · prior 2131-2140 / 2121-2130 stacks retained) · **LUWA PPP EUR590m** · private gambling **EUR31.5bn** market. **Double-count vs hospital IGS/ASBL path possible; Medium aggregators pending NBB PDF.**

### Inventory (tick 2150)

| File | Rows (class) |
|------|-------------:|
| budgets.csv | {counts['budgets.csv']} |
| commitments.csv | {counts['commitments.csv']} |
| leaderboard.csv | {counts['leaderboard.csv']} |
| entities.csv | {counts['entities.csv']} |
| sources.csv | {counts['sources.csv']} |
| FOI ready | {counts['foi_ready']} |
| FOI answered | {counts['foi_answered']} |
| FOI partial | {counts['foi_partial']} |
| FOI total rows | {counts['foi_queue.csv']} |
| research_queue open | {NEXT_RQ} after progress |

### What improved since tick 2140

- **Residual dual (tick2141-2150):** **Denderrust Dienstengroep** (Stopgezet fusie into campus) · **Groep Sint-Franciscus Brakel** (omzet JUMP 31.0m / pnl FLIP PROFIT) · **Seniors Care-Ion Anderlecht** (omzet JUMP 86.0m / equity DROP / pnl LOSS) · **Zone de secours Dinaphi** (FTE 50 / budget FOI) · **Zone de secours Hainaut-Centre** (FTE 200 / budget FOI) · **Zonnelied Roosdaal** (bruto JUMP 24.0m / pnl DROP) · **Zone de secours Hesbaye** (FTE 20 / budget FOI) · **Zone de secours Wallonie Picarde** (FTE 200 / budget FOI) · **Zone de secours HEMECO** (FTE 50 / budget FOI) · **Zone de secours Val de Sambre** (this tick EVERY-10 — FTE 50; Budget 2026 adopté 27.01.2026 but avis = on-site consultation only; no CW YE kerncijfers; FOI ready).
- **Blocked still:** AGB Bornem JR2025 unpublished (JR2024 Strong mined) · FARO NBB YE2025 unpublished (YE2024 filing / CW last balance 2024) · AIESH / REW YE2024-only · prior Eneco deposit FOI stack · Walloon ZDS comptes/budget PDFs (Dinaphi/ZHC/Hesbaye/WAPI/HEMECO/VDS FOI-ready).
"""

(DATA / "progress_every_10_ticks.md").write_text(progress, encoding="utf-8")

top10 = f"""# DOGE waste ranking — current top 10

**As-of:** tick **{TICK}** (2026-08-25) · **{counts['leaderboard.csv']}** leaderboard rows  
**Sort:** `priority_index` desc (then annual €); **stocks / multi-decade finance with annual € = full stock filtered off pure top10**; **corrupt AGB / scoring anomalies with pi>10 excluded**  
**Formula:** `0.55·cost_score + 0.35·absurdity + 0.10·(10−difficulty)`  
**cost_score bands (from annual €):** <1m→1.5 · <10m→3.5 · <100m→5.5 · <1bn→7.5 · ≥1bn→9.5  

**This is a prioritisation for cuts/review**, not a claim that these euros are illegal.  
Large structural TE/FFS score high on **cost** even when “absurdity” is moderate.

---

## Top 10 (all-time current — annual flow / TE-adjacent)

| # | ID | Name | Annual € (class) | Abs | Cost | Diff | **Priority** | Why it ranks |
|---|-----|------|------------------:|----:|-----:|-----:|-------------:|--------------|
| 1 | `lb_vl_gip_monitor_fail_2_5bn` | GIP steers ~2.5bn without VEK encours public report | **2.50 bn** | 9.0 | 9.0 | 5 | **8.7** | Strong CoA ch6-8: no public exec report |
| 2 | `lb_fed_fossil_direct_13_3bn` | Federal fossil direct subsidies 13.3bn 2022 bench1 | **13.27 bn** | 8 | 9.5 | 7 | **8.55** | Strong climat.be 4e inv: direct 13.268bn |
| 3 | `lb_company_cars_fpb` | Company cars TE package FPB ~4.7-5.2bn | **4.70 bn** | 8.5 | 9.5 | 7 | **8.5** | FPB 2025 strong: 4.7bn rising to 5.2bn |
| 4 | `lb_fed_fossil_accises_10_5bn` | Fossil accise rate gaps+exemptions 10.5bn 2022 | **10.54 bn** | 8 | 9.5 | 6 | **8.5** | Strong: 10536m of 13268m direct; gas pro |
| 5 | `lb_exc_heatoil` | Excise preference: heating gas oil (low sulfur) | **1.84 bn** | 8 | 9.5 | 6 | **8.43** | FFS bench1 total 1836.4m 2024 (lowS) |
| 6 | `lb_cheque_economy` | Cheque economy meal vouchers (para)fiscal + restricted | **1.07 bn** | 8.5 | 9.5 | 8 | **8.4** | CoA 2024 private parafiscal 1.07bn strong |
| 7 | `lb_co2_vs_ordinary_ssc_gap_1bn` | Company car CO2 vs ordinary SSC gap >1bn by 2026 | **1.00 bn** | 8.5 | 9.5 | 6 | **8.4** | Strong CoA: gap CO2 receipts vs ordinary |
| 8 | `lb_dual_cars_ssc_taxex` | Dual company car CO2 SSC under-collection vs taxex | **278.52 m** | 8.5 | 9.5 | 6 | **8.4** | Strong dual: SSC CO2 278m + cum gap |
| 9 | `lb_oaa_consol_reporte_300_6m` | OAA+missions reporté solde shift +300.6m | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA: consol solde 34 to +300.6 |
| 10 | `lb_bcr_annexe2_reporte_wave` | BCR Annexe2 reporté wave systemic 2026 | **300.60 m** | 9.0 | 9.0 | 3 | **8.4** | Strong CoA wave: OAA consol reporté |

**GIP honesty:** #1 ranks high on **governance absurdity × volume steered**, not as a claim that €2.5bn is discretionary waste. Prefer FOI VEK/encours/public exec report.  
**Cheque honesty:** annual € tracks **layer B TE** (~€1.07bn CoA) for fiscal ranking. Face (~€3.55bn) is mostly wages. Pure waste (admin + restricted-spend DWL) is a **smaller band**.  
**Stock filter (off pure annual top10):** Metro3 overrun/gap · OWV snowball **€27bn** eoy2083 · Hedera CAP · VL/WAL/FWB/BCR debt stocks · federal unconsol debt · **Defence eng / SAFE loans €8.34bn** · **EU GNI / MFF** · **Entity II HermReg €7.9bn** · **illness €14.2bn / RIZIV €41.3bn** · **SS spend €140bn class** · **MOG II €7–8bn** CAPEX · **university/city balance sheets** · **AGB/zorg dual + IGS/HVZ/CAW/CGG/woonmaatschappij/thuiszorg shells** · **NEW residual 2141-2150:** **Care-Ion omzet 86.0m** · **Groep Sint-Franciscus omzet 31.0m** · **Zonnelied bruto 24.0m** · Walloon HVZ opacity stack (**Dinaphi / ZHC / Hesbaye / WAPI / HEMECO / Val de Sambre** FTE-only FOI) · prior 2131-2140 Denderrust/CIGB/Corolles stack retained · prior nuclear/Fluxys/Elia/Enodia/RESA · **LUWA PPP €590m** · private gambling **€31.5bn** market.

**Change vs tick 2140:** pure annual top10 **stable** (GIP #1; fossil/cars/cheque/reporté #2–10; Metro3/OWV filtered as stock). Re-verified from leaderboard (corrupt AGB/scoring pi>10 / Metro3 stock / OWV snowball stock filtered off; seed/open TE-FFS rows retained for pure annual ranking). **Major NEW residual 2141-2150 (off pure top10 / dual):** Denderrust Dienstengroep · Groep Sint-Franciscus · Care-Ion · Dinaphi · Hainaut-Centre · Zonnelied · Hesbaye · Wallonie Picarde · HEMECO · **Val de Sambre** (EVERY-10@2150). Count NEW since 2140: 10 residual dual ticks. **Prior 2131-2140 + 2121-2130 stacks retained.** Not TE-additive of ~348bn.
"""

(DATA / "doge_waste_top10_current.md").write_text(top10, encoding="utf-8")

with open(ROOT / "loop_log.md", "a", encoding="utf-8") as f:
    f.write(
        f"""
## Tick {TICK} - {UTC} - {RQ} EVERY-10 Zone de secours Val de Sambre (FTE 50 / Budget 2026 on-site FOI / Medium)

- Unit: **{RQ}** EVERY-10 + leftover dual after **rq_2149 HEMECO**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took named deferred unused leftover **Zone de secours Val de Sambre** (KBO **{KBO}**; Rue de la Vacherie 78 Sambreville; **Hulpverleningszone** / **3 VE**; NACE **84.250**; 6 communes). Do not redo HEMECO/WAPI/Hesbaye/ZHC/Dinaphi/Zonnelied/Care-Ion/Groep SF/Flemish HVZ stack.
- Found: Strong KBO Actief + Medium CW FTE **{FTE}**; **no** CW/NBB YE kerncijfers. Official **Avis Budget 2026** (adopté Conseil 27.01.2026) published — **on-site consultation only**, **no euro figures** in PDF. FOI via info@zonevaldesambre.be / facturation@ for comptes 2025 + budget 2026 PDF + communal/federal dotations. No invented euros.
- Wrote: sources (+6); budgets (+1 FTE-only); commitments (+1); leaderboard (+1 pi 5.25 opacity); entities (+1 {ENTITY}); foi + draft {GAP}; progress_every_10_ticks.md + doge_waste_top10_current.md refreshed; {RQ}=done + {NEXT_RQ} open; loop_state ticks={TICK}; raw docs/doge/data/raw/tick2150/.
- FOI: **ready not sent** (human-gated).
- **EVERY-10@{TICK}** (last was 2140; **next 2160**). Pure annual top10 stable (GIP/fossil/cars/cheque). Next: {NEXT_RQ} (AGB/FARO-if-YE2025 / AIESH-REW / Vesdre / unused IGS-DSO-WZC-MRS).
"""
    )

print("OK tick", TICK, ENTITY, "FTE", FTE, "budget Unknown FOI EVERY-10")
print("inventory", {k: counts[k] for k in counts})
