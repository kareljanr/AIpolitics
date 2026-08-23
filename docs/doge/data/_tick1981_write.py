# ephemeral tick1981 — Vivalia YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T22:50:00Z"
ENTITY = "igs_vivalia"
GAP = "gap_vivalia_nbb_pdf_assets_debt_sector_matrix_l5_ye2025"
SRC = "src_vivalia_jr2025_cw"
SRC_EN = "src_vivalia_jr2025_cw_en"
SRC_KBO = "src_vivalia_kbo_1981"
SRC_GEST = "src_vivalia_gestion_2024_pdf"
SRC_AG = "src_vivalia_ag_2024_press"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys())


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_1981")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Vivalia YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0214567166",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1981; YE2025 omzet JUMP 473139578 +2.98pct; pnl DROP 7568119 -49.87pct; equity JUMP 205609886 +3.96pct; bruto JUMP 275658155 +4.69pct; FTE 3178.1; neerlegging 17.07.2026; raw docs/doge/data/raw/tick1981/vivalia_cw.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Vivalia YE2025 statutory",
        "url": "https://www.companyweb.be/en/0214567166",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1981; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1981/vivalia_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Vivalia 0214.567.166 Actief CV Bastogne",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214567166",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1981; Actief CV; Chaussee de Houffalize 1 6600 Bastogne; Luxembourg hospital IGS; no email/web in KBO",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_GEST,
        "title": "Vivalia Rapport de gestion 2024 consol (YE2024 Strong cross-check)",
        "url": "https://www.vivalia.be/sites/default/files/2025-09/v2_237387-01_bro_web.pdf",
        "publisher": "Vivalia",
        "accessed_date": "2026-08-23",
        "source_class": "primary_official",
        "notes": "tick1981; YE2024 Strong consol pnl 15097521.50 matches CW YE2024; assets consol class 494.8m path; sector hospital/PCPA/AMU/extra; YE2025 NBB PDF still FOI; raw docs/doge/data/raw/tick1981/vivalia_gestion_2024.pdf",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_AG,
        "title": "Vivalia AG 24.06.2025 YE2024 result press",
        "url": "https://www.vivalia.be/assemblee-generale-ordinaire-de-vivalia-062025",
        "publisher": "Vivalia",
        "accessed_date": "2026-08-23",
        "source_class": "primary_official",
        "notes": "tick1981; YE2024 net +15m / courant 3.3m; hospital sector +18m; exceptional 11.8m; invest path Houdemont/Vivalia 2030",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_vivalia_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "473139578",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1981; omzet JUMP 473139578 +2.98pct vs YE2024 459453322",
    },
    {
        "budget_id": "bud_vivalia_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "7568119",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1981; pnl DROP 7568119 -49.87pct vs YE2024 15097522 (Strong PDF YE2024 15097521.50)",
    },
    {
        "budget_id": "bud_vivalia_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "205609886",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1981; equity JUMP 205609886 +3.96pct vs YE2024 197786837",
    },
    {
        "budget_id": "bud_vivalia_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "275658155",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1981; bruto JUMP 275658155 +4.69pct vs YE2024 263319856",
    },
    {
        "budget_id": "bud_vivalia_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "3178.1",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1981; YE2025 FTE 3178.1 vs YE2024 3050",
    },
    {
        "budget_id": "bud_vivalia_pnl_jr2024_gestion_strong",
        "entity_id": ENTITY,
        "year": "2024",
        "amount_eur": "15097521.50",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "Official gestion 2024 resultat net consol",
        "source_id": SRC_GEST,
        "confidence": "strong",
        "notes": "tick1981; YE2024 Strong PDF cross-check; hospital sector +18.045m; matches CW YE2024",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_vivalia_jr2025_statutory_hospital",
    "title": "Vivalia YE2025 leftover Luxembourg hospital IGS dual (omzet JUMP 473.14m pnl DROP 7.57m)",
    "entity_id": ENTITY,
    "beneficiary": "Luxembourg (+partial Namur) hospital/MR/AMU patients + communes/provinces",
    "legal_basis": "Code democratie locale intercommunale CV hospitaliere; loi hopitaux",
    "decision_date": "2026-07-17",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "473139578",
    "cash_by_year": '{"2025_omzet":473139578,"2025_pnl":7568119,"2025_equity":205609886,"2025_bruto":275658155,"2025_fte":3178.1}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0214567166",
    "stated_goal": "Integrated hospital + elderly + AMU care for Luxembourg province",
    "cut_option": "Publish NBB PDF assets/debt + sector P&L matrix + Vivalia 2030 CAPEX path FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Luxembourg>Vivalia>JR2025_statutory_L5",
    "notes": "tick1981; Medium CW YE2025 + Strong YE2024 gestion; assets/debt Unknown; dual HELORA/Passelecq/LOGIPOLE; preferred AGB/FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_vivalia_omzet_jump_473_14m_pnl_drop_7_57m_jr2025",
    "name": "Vivalia omzet JUMP 473.14m / pnl DROP 7.57m / equity JUMP 205.61m (Luxembourg hospital IGS YE2025)",
    "level": "L5",
    "type": "walloon_igs_hospital_dual",
    "hierarchy_path": "Wallonie>Luxembourg>Vivalia>JR2025_statutory_L5",
    "annual_cost_eur": "473139578",
    "total_cost_eur": "205609886",
    "tco_notes": "statutory omzet JUMP 473139578 pnl DROP 7568119 equity JUMP 205609886 bruto JUMP 275658155 FTE 3178.1; assets/debt Unknown; YE2024 Strong net 15.10m",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Luxembourg hospital/MR/AMU users via communal/provincial IGS",
    "stated_goal": "Public hospital network + elderly + AMU (Vivalia 2030 Houdemont path)",
    "measured_outcome": "Medium CW YE2025; pnl halved vs YE2024 Strong 15.1m; FTE 3178; NBB PDF assets/debt residual; dual HELORA",
    "absurdity_score": "5.5",
    "cost_score": "7.5",
    "difficulty": "3.0",
    "priority_index": "6.75",
    "cut_proposal": "Publish NBB PDF + sector matrix + CAPEX/debt path FOI; scrutinise pnl DROP vs omzet JUMP",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1981 leftover hospital dual; Medium CW; unused Luxembourg IGS after HELORA/Passelecq; not TE-additive pure-waste top10",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Vivalia (Luxembourg ziekenhuis-IGS)",
    "name_fr": "Vivalia (intercommunale hospitaliere Luxembourg)",
    "name_en": "Vivalia (Luxembourg hospital intercommunale)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://www.vivalia.be/",
    "foi_email": "",
    "foi_postal": "Chaussee de Houffalize 1, 6600 Bastogne",
    "notes": "tick1981 YE2025 Medium CW NL+EN + Strong KBO 0214.567.166 Actief CV + Strong YE2024 gestion PDF; omzet JUMP 473.14m pnl DROP 7.57m equity JUMP 205.61m bruto JUMP 275.66m FTE 3178.1; assets/debt Unknown; neerlegging 17.07.2026; FOI gap_vivalia_nbb_pdf_assets_debt_sector_matrix_l5_ye2025; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo HELORA/Passelecq/LOGIPOLE/IBH/CISCH/HYGEA/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Luxembourg>Vivalia>NBB_PDF_assets_debt_sector_matrix",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); sector P&L matrix hospital/PCPA/AMU/extra; Vivalia 2030 CAPEX/debt path; dual recon vs HELORA",
    "why_it_matters": "Medium CW shows 473m omzet / 7.57m pnl hospital mega-IGS without balance sheet; pnl halved vs YE2024 Strong 15.1m while omzet JUMP; Houdemont multi-100m path opacity",
    "priority": "7",
    "recipient_body": "Vivalia / Province de Luxembourg",
    "recipient_email": "",
    "recipient_postal": "https://www.vivalia.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_vivalia_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_vivalia_omzet_jump_473_14m_pnl_drop_7_57m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1981; human-send only; Medium CW; no KBO email — postal Chaussee de Houffalize 1 Bastogne; next every-10 1990",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Vivalia (NBB PDF / assets-debt / sector matrix YE2025)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Vivalia CV — KBO **0214.567.166**  
**recipient:** Vivalia — Chaussée de Houffalize 1, 6600 Bastogne (no KBO email)  
**sources:** [CW NL](https://www.companyweb.be/nl/0214567166) · [CW EN](https://www.companyweb.be/en/0214567166) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0214567166) · [gestion 2024](https://www.vivalia.be/sites/default/files/2025-09/v2_237387-01_bro_web.pdf) · [AG 2025](https://www.vivalia.be/assemblee-generale-ordinaire-de-vivalia-062025)  
**tick:** 1981  
**confidence:** Medium (CW NL+EN YE2025; Strong YE2024 gestion; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **17.07.2026**): omzet **EUR473,139,578** JUMP +2.98%; pnl **EUR7,568,119** DROP -49.87%; equity **EUR205,609,886** JUMP +3.96%; bruto **EUR275,658,155** JUMP +4.69%; FTE **3,178.1**; assets/debt **Unknown**.
- YE **2024** Strong gestion: resultat net **EUR15,097,521.50** (hospital +18.05m); matches CW YE2024.
- Unused leftover Luxembourg hospital IGS dual of HELORA/Passelecq after IDELUX Finances EVERY-10. Preferred stall: AGB Bornem / FARO / AIESH / REW YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Vivalia — Chaussée de Houffalize 1, 6600 Bastogne
cc: Province de Luxembourg / SPW transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 Vivalia + balans + sectorale P&L (KBO 0214.567.166)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 17.07.2026).
2. Assets / schulden LT-ST / cash.
3. Sectorale P&L 2025: hospitalier / PCPA / AMU / extra-hospitalier.
4. Recon pnl DROP (7.57m vs YE2024 Strong 15.10m) bij omzet JUMP.
5. Vivalia 2030 / Houdemont CAPEX-schuld path indien publiek.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1981":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["title"] = "leftover dual hole-fill after IDELUX Finances — Vivalia YE2025 Medium"
        x["notes"] = "tick1981 Vivalia Medium omzet JUMP 473.14m pnl DROP 7.57m; FOI ready; next rq_1982; next every-10 1990"
        x["instructions"] = (
            "Completed leftover Vivalia Luxembourg hospital IGS YE2025 Medium CW; KBO 0214.567.166; "
            "omzet JUMP 473139578 pnl DROP 7568119 equity JUMP 205609886 bruto JUMP 275658155 FTE 3178.1; FOI " + GAP
        )
        x["entity_id"] = ENTITY
        x["blocked_gap_id"] = GAP
if not any(x.get("task_id") == "rq_1982" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1982",
            "title": "leftover dual hole-fill after Vivalia",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1981 after Vivalia YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/ADT (IDETA/SPI if YE2025). Do NOT redo Vivalia, "
                "IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, "
                "BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, "
                "Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, "
                "IPALLE, INTRADEL, Tibi, IDELUX Env."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1981 Vivalia; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1981",
        "ticks_completed": "1981",
        "paused": "no",
        "notes": "tick1981 leftover Vivalia 0214.567.166 Medium CW (omzet JUMP 473.14m pnl DROP 7.57m equity JUMP 205.61m bruto JUMP 275.66m FTE 3178.1; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1982; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1981 - 2026-08-23T22:50:00Z - rq_1981 Vivalia (omzet JUMP 473.14m / pnl DROP 7.57m / Medium)

- Unit: **rq_1981** leftover dual after **rq_1980 EVERY-10 + IDELUX Finances**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**; waste COPIDEC (IPALLE/INTRADEL/Tibi) + IDELUX Finances already mined. Took unused leftover **Vivalia** YE2025 (KBO **0214.567.166**; Chaussée de Houffalize 1 Bastogne; Luxembourg hospital IGS dual HELORA/Passelecq). Do not redo IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/HELORA/Passelecq/LOGIPOLE/IPALLE/INTRADEL/Tibi.
- Found: Companyweb NL+EN YE2025 - omzet **EUR473,139,578** JUMP +2.98%; pnl **EUR7,568,119** DROP -49.87%; equity **EUR205,609,886** JUMP +3.96%; bruto **EUR275,658,155** JUMP +4.69%; FTE **3,178.1**; neerlegging **17.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV; YE2024 Strong gestion PDF resultat net **EUR15,097,521.50** matches CW YE2024.
- Wrote: sources (+5); budgets (+6); commitments (+1); leaderboard (+1); entities (+1 igs_vivalia); foi + draft gap_vivalia_nbb_pdf_assets_debt_sector_matrix_l5_ye2025; rq_1981=done + rq_1982 open; loop_state ticks=1981; raw under docs/doge/data/raw/tick1981/.
- FOI: **ready not sent** (human-gated; no KBO email — postal Bastogne).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1982 (AGB/FARO-if-YE2025 / AIESH-REW / IDETA-SPI / unused DSO-IGS-HVZ).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1981" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log exists")
print("DONE tick1981")
