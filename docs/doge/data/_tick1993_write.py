# ephemeral tick1993 — Cliniques universitaires Saint-Luc YE2025 Medium (leftover dual after GHdC)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T01:50:00Z"
ENTITY = "vzw_saint_luc"
GAP = "gap_saint_luc_nbb_pdf_assets_debt_pnl_loss_equity_drop_matrix_l5"
SRC = "src_saint_luc_jr2025_cw"
SRC_EN = "src_saint_luc_jr2025_cw_en"
SRC_FR = "src_saint_luc_jr2025_cw_fr"
SRC_KBO = "src_saint_luc_kbo_1993"
SRC_SITE = "src_saint_luc_site_1993"

# YE2025 (CW NL+EN+FR; neerlegging 28.07.2026)
OMZET = "857935946"
PNL = "-36647075"
EQUITY = "157496575"
BRUTO = "518871830"
FTE = "4931.8"
# YE2024 comps
OMZET24 = "813400060"
PNL24 = "1413271"
EQUITY24 = "195429781"
BRUTO24 = "498634634"
FTE24 = "4870.2"


def load(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows, list(rows[0].keys()) if rows else []


def save(path, rows, fields):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_1993")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Cliniques universitaires Saint-Luc YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0416885016/cliniques-universitaires-saint-luc",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1993; YE2025 omzet JUMP 857935946 pnl LOSS -36647075 equity DROP 157496575 bruto JUMP 518871830 FTE 4931.8; neerlegging 28.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1993/saintluc_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Cliniques universitaires Saint-Luc YE2025 statutory",
        "url": "https://www.companyweb.be/en/0416885016/cliniques-universitaires-saint-luc",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1993; EN mirror YE2025 Medium; filed 28-07-2026; raw docs/doge/data/raw/tick1993/saintluc_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Cliniques universitaires Saint-Luc YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0416885016/cliniques-universitaires-saint-luc",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick1993; FR mirror YE2025 Medium; déposés le 28-07-2026; raw docs/doge/data/raw/tick1993/saintluc_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO Cliniques universitaires Saint-Luc 0416.885.016 Actief VZW Woluwe",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416885016",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick1993; Actief VZW since 13.10.1976; Cliniques universitaires Saint-Luc; Hippokrateslaan 10 1200 Sint-Lambrechts-Woluwe; 5 VE; Aanbestedende overheid; no KBO email",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "saintluc.be Cliniques universitaires Saint-Luc UCL",
        "url": "https://www.saintluc.be/",
        "publisher": "Cliniques universitaires Saint-Luc",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick1993; Avenue Hippocrate 10 1200 Bruxelles; +32 2 764 11 11; UCL university hospital",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_saint_luc_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1993; omzet JUMP {OMZET} +5.48pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_saint_luc_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1993; pnl LOSS {PNL} vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_saint_luc_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1993; equity DROP {EQUITY} -19.41pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_saint_luc_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1993; bruto JUMP {BRUTO} +4.06pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_saint_luc_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick1993; YE2025 FTE {FTE} vs YE2024 {FTE24} (+61.6)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_saint_luc_jr2025_statutory_hospital",
    "title": "Saint-Luc YE2025 leftover hospital dual (omzet JUMP 857.94m / pnl LOSS 36.65m / equity DROP 157.50m)",
    "entity_id": ENTITY,
    "beneficiary": "Brussels/UCL university hospital patients / Cliniques universitaires Saint-Luc",
    "legal_basis": "ASBL/VZW university hospital (UCL)",
    "decision_date": "2026-07-28",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0416885016/cliniques-universitaires-saint-luc",
    "stated_goal": "UCL university hospital care (Woluwe)",
    "cut_option": "Publish NBB PDF assets/debt + pnl LOSS / equity DROP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Bruxelles>SaintLuc_UCL>JR2025_statutory_L5",
    "notes": "tick1993; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; GHdC already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*8.0 + 0.35*7.0 + 0.10*4.0 = 7.25
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_saint_luc_omzet_jump_857_94m_pnl_loss_36_65m_equity_drop_jr2025",
    "name": "Saint-Luc omzet JUMP 857.94m / pnl LOSS 36.65m / equity DROP 157.50m (YE2025)",
    "level": "L5",
    "type": "brussels_university_hospital_asbl_dual",
    "hierarchy_path": "Bruxelles>SaintLuc_UCL>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "UCL university hospital patients via Saint-Luc VZW",
    "stated_goal": "University hospital care",
    "measured_outcome": "Medium CW YE2025; 858m omzet with pnl LOSS turnaround from YE2024 profit and equity DROP -19pct; NBB PDF residual",
    "absurdity_score": "7.0",
    "cost_score": "8.0",
    "difficulty": "4.0",
    "priority_index": "7.25",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl LOSS + equity DROP path vs Humani/GHdC/CHIREC",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1993 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2000",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "Cliniques universitaires Saint-Luc (UCL)",
    "name_fr": "Cliniques universitaires Saint-Luc (UCL)",
    "name_en": "Cliniques universitaires Saint-Luc (UCL university hospital)",
    "level": "asbl",
    "parent_id": "brussels_gov",
    "community_language": "fr",
    "website": "https://www.saintluc.be/",
    "foi_email": "",
    "foi_postal": "Avenue Hippocrate 10, 1200 Bruxelles",
    "notes": "tick1993 YE2025 Medium CW NL+EN+FR + Strong KBO 0416.885.016 Actief VZW; omzet JUMP 857.94m pnl LOSS 36.65m equity DROP 157.50m bruto JUMP 518.87m FTE 4931.8; assets/debt Unknown; neerlegging 28.07.2026; 5 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
else:
    for x in erows:
        if x.get("entity_id") == ENTITY:
            x.update({k: v for k, v in ne.items() if v})
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Bruxelles>SaintLuc_UCL>NBB_PDF_assets_debt_pnl_loss_equity_drop",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS recon vs YE2024 profit; equity DROP -19pct recon",
    "why_it_matters": "Medium CW shows 858m omzet UCL university hospital with pnl LOSS turnaround and equity DROP -19pct without balance sheet",
    "priority": "8",
    "recipient_body": "Cliniques universitaires Saint-Luc ASBL",
    "recipient_email": "",
    "recipient_postal": "Avenue Hippocrate 10, 1200 Bruxelles",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_saint_luc_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_saint_luc_omzet_jump_857_94m_pnl_loss_36_65m_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1993; human-send only; Medium CW; route via saintluc.be (no KBO email); next every-10 2000",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Cliniques universitaires Saint-Luc (NBB PDF / assets-debt / pnl LOSS / equity DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Cliniques universitaires Saint-Luc VZW — KBO **0416.885.016**  
**recipient:** route via saintluc.be (no KBO email) · Avenue Hippocrate 10, 1200 Bruxelles  
**sources:** [CW NL](https://www.companyweb.be/nl/0416885016/cliniques-universitaires-saint-luc) · [CW EN](https://www.companyweb.be/en/0416885016/cliniques-universitaires-saint-luc) · [CW FR](https://www.companyweb.be/fr/0416885016/cliniques-universitaires-saint-luc) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416885016) · [site](https://www.saintluc.be/)  
**tick:** 1993  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **28.07.2026**): omzet **EUR857,935,946** JUMP +5.48%; pnl **LOSS EUR-36,647,075** (vs YE2024 profit EUR1,413,271); equity **EUR157,496,575** DROP -19.41%; bruto **EUR518,871,830** JUMP +4.06%; FTE **4931.8** (+61.6 vs 4870.2); assets/debt **Unknown**.
- UCL university hospital ASBL/VZW (Woluwe). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. GHdC/Humani/CHIREC already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Cliniques universitaires Saint-Luc — Avenue Hippocrate 10, 1200 Bruxelles
via saintluc.be openbaarheid / info
cc: Cocof / Brussels transparence indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Cliniques universitaires Saint-Luc + balans (KBO 0416.885.016)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 28.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl LOSS (EUR-36.647.075 vs YE2024 winst EUR1.413.271) en equity DROP (-19,41pct).
4. Dual vs Humani / GHdC / CHIREC indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_1993":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after GHdC — Saint-Luc YE2025 Medium"
        x["notes"] = (
            "tick1993 Saint-Luc Medium omzet JUMP 857.94m pnl LOSS 36.65m equity DROP 157.50m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1994; next every-10 2000"
        )
        x["instructions"] = (
            "Completed leftover Cliniques universitaires Saint-Luc YE2025 Medium CW; KBO 0416.885.016; "
            f"omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_1994" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1994",
            "title": "leftover dual hole-fill after Saint-Luc",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 1993 after Saint-Luc YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (CHBA Seraing 0203.980.409 / Haute Senne / CNDG / CHR Verviers if YE2025). "
                "Do NOT redo Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1993 Saint-Luc; next every-10 2000; CHBA Seraing YE2025 deferred",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1993",
        "ticks_completed": "1993",
        "paused": "no",
        "notes": (
            "tick1993 leftover Saint-Luc 0416.885.016 Medium CW (omzet JUMP 857.94m pnl LOSS 36.65m equity DROP 157.50m bruto JUMP 518.87m FTE 4931.8; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHBA Seraing deferred; next rq_1994; next every-10 2000; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1993 - 2026-08-24T01:50:00Z - rq_1993 Saint-Luc (omzet JUMP 857.94m / pnl LOSS 36.65m / Medium)

- Unit: **rq_1993** leftover dual after **rq_1992 GHdC**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **Cliniques universitaires Saint-Luc** YE2025 (KBO **0416.885.016**; Avenue Hippocrate 10 Woluwe; Brussels/UCL **university hospital VZW**). CHBA Seraing YE2025 deferred. Do not redo GHdC/Humani/CHIREC/Tivoli/Citadelle/ISoSL/Epicura/CHwapi/CHU UCL Namur/Vivalia/HELORA/IDETA/SPI.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR857,935,946** JUMP +5.48%; pnl **LOSS EUR-36,647,075** (vs YE2024 profit 1.41m); equity **EUR157,496,575** DROP **-19.41%**; bruto **EUR518,871,830** JUMP +4.06%; FTE **4931.8** (+61.6 vs 4870.2); neerlegging **28.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 5 VE; no KBO email (route via saintluc.be).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_saint_luc); foi + draft gap_saint_luc_nbb_pdf_assets_debt_pnl_loss_equity_drop_matrix_l5; rq_1993=done + rq_1994 open; loop_state ticks=1993; raw under docs/doge/data/raw/tick1993/.
- FOI: **ready not sent** (human-gated; route via saintluc.be).
- NOT every-10 (**next every-10 is 2000**). Next: rq_1994 (AGB/FARO-if-YE2025 / AIESH-REW / CHBA Seraing-CNDG-Haute Senne / unused DSO-IGS-HVZ-hospital).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1993" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1993")
