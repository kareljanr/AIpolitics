# ephemeral tick2011 — Heilig Hart Lier YE2025 Medium (leftover dual after Vlaamse Zorgkas)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T07:10:00Z"
ENTITY = "vzw_heilig_hart_lier"
GAP = "gap_heilig_hart_lier_nbb_pdf_assets_debt_pnl_loss_matrix_l5"
SRC = "src_heilig_hart_lier_jr2025_cw"
SRC_EN = "src_heilig_hart_lier_jr2025_cw_en"
SRC_FR = "src_heilig_hart_lier_jr2025_cw_fr"
SRC_KBO = "src_heilig_hart_lier_kbo_2011"
SRC_SITE = "src_heilig_hart_lier_site_2011"

OMZET = "204492026"
PNL = "-2108644"
EQUITY = "78662672"
BRUTO = "92494807"
FTE = "1008.3"
OMZET24 = "194007634"
PNL24 = "-1225911"
EQUITY24 = "81047097"
BRUTO24 = "91400941"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2011")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL Heilig Hart Lier YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0412080645",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2011; YE2025 omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 09.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2011/lier_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN Heilig Hart Lier YE2025 statutory",
        "url": "https://www.companyweb.be/en/0412080645",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2011; EN mirror YE2025 Medium; filed 09-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2011/lier_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR Heilig Hart Lier YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0412080645",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2011; FR mirror YE2025 Medium; deposés le 09-07-2026; raw docs/doge/data/raw/tick2011/lier_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO HeiligHartziekenhuis Lier 0412.080.645 Actief VZW",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412080645",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2011; Actief VZW since 08.03.1972; Mechelsestraat 24 2500 Lier; no KBO email; 1 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "heilighartlier.be Heilig Hart Ziekenhuis Lier",
        "url": "https://www.heilighartlier.be/",
        "publisher": "Heilig Hart Lier",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2011; info@heilighartlier.be / ombudsdienst@heilighartlier.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_heilig_hart_lier_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2011; omzet JUMP {OMZET} +5.40pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_heilig_hart_lier_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2011; pnl LOSS {PNL} vs YE2024 LOSS {PNL24} (-72.01pct deeper)",
    },
    {
        "budget_id": "bud_heilig_hart_lier_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2011; equity DROP {EQUITY} -2.94pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_heilig_hart_lier_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2011; bruto JUMP {BRUTO} +1.20pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_heilig_hart_lier_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2011; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_heilig_hart_lier_jr2025_statutory_hospital",
    "title": "Heilig Hart Lier YE2025 leftover hospital dual (omzet JUMP 204.49m / pnl LOSS 2.11m / equity DROP 78.66m)",
    "entity_id": ENTITY,
    "beneficiary": "Lier-region hospital patients / Heilig Hart Lier",
    "legal_basis": "VZW/ASBL hospital (KBO 0412.080.645)",
    "decision_date": "2026-07-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0412080645",
    "stated_goal": "Regional hospital care (Lier)",
    "cut_option": "Publish NBB PDF assets/debt + pnl LOSS recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Antwerpen>Heilig_Hart_Lier>JR2025_statutory_L5",
    "notes": "tick2011; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Andries YE2025 also live deferred; Vlaamse Zorgkas already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_heilig_hart_lier_omzet_jump_204_49m_pnl_loss_2_11m_equity_drop_jr2025",
    "name": "Heilig Hart Lier omzet JUMP 204.49m / pnl LOSS 2.11m / equity DROP 78.66m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "Antwerpen>Heilig_Hart_Lier>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Lier patients via Heilig Hart Lier VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 204.49m omzet JUMP +5.40pct with deeper pnl LOSS -2.11m and equity DROP -2.94pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon deepening LOSS vs Zorgkas/OLVT/Glorieux",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2011 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2020",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "HeiligHartziekenhuis Lier / Heilig Hart Lier",
    "name_fr": "HeiligHartziekenhuis Lier",
    "name_en": "Heilig Hart Hospital Lier",
    "level": "asbl",
    "parent_id": "prov_antwerpen",
    "community_language": "nl",
    "website": "https://www.heilighartlier.be/",
    "foi_email": "info@heilighartlier.be",
    "foi_postal": "Mechelsestraat 24, 2500 Lier",
    "notes": "tick2011 YE2025 Medium CW NL+EN+FR + Strong KBO 0412.080.645 Actief VZW; omzet JUMP 204.49m pnl LOSS 2.11m equity DROP 78.66m bruto JUMP 92.49m FTE 1008.3; assets/debt Unknown; neerlegging 09.07.2026; 1 VE; FOI "
    + GAP
    + "; alt ombudsdienst@heilighartlier.be; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "Antwerpen>Heilig_Hart_Lier>NBB_PDF_assets_debt_pnl_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl LOSS deepening recon vs YE2024",
    "why_it_matters": "Medium CW shows 204.49m omzet Lier hospital VZW with deepening LOSS -2.11m and equity DROP without balance sheet",
    "priority": "7",
    "recipient_body": "HeiligHartziekenhuis Lier v.z.w.",
    "recipient_email": "info@heilighartlier.be",
    "recipient_postal": "Mechelsestraat 24, 2500 Lier",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_heilig_hart_lier_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_heilig_hart_lier_omzet_jump_204_49m_pnl_loss_2_11m_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2011; human-send only; Medium CW; alt ombudsdienst@heilighartlier.be; next every-10 2020",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — Heilig Hart Lier (NBB PDF / assets-debt / pnl LOSS)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** HeiligHartziekenhuis Lier v.z.w. — KBO **0412.080.645**  
**recipient:** info@heilighartlier.be · Mechelsestraat 24, 2500 Lier (alt: ombudsdienst@heilighartlier.be)  
**sources:** [CW NL](https://www.companyweb.be/nl/0412080645) · [CW EN](https://www.companyweb.be/en/0412080645) · [CW FR](https://www.companyweb.be/fr/0412080645) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0412080645) · [site](https://www.heilighartlier.be/)  
**tick:** 2011  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **09.07.2026**): omzet **EUR204,492,026** JUMP +5.40%; pnl **LOSS EUR-2,108,644** (deeper vs YE2024 LOSS −1.23m); equity **EUR78,662,672** DROP −2.94%; bruto **EUR92,494,807** JUMP +1.20%; FTE **1008.3**; assets/debt **Unknown**.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Sint-Andries YE2025 deferred. Vlaamse Zorgkas already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: HeiligHartziekenhuis Lier v.z.w. — Mechelsestraat 24, 2500 Lier
info@heilighartlier.be / ombudsdienst@heilighartlier.be
cc: Agentschap Zorg en Gezondheid / Provincie Antwerpen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 Heilig Hart Lier + balans (KBO 0412.080.645)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 09.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl LOSS (EUR-2.108.644 vs YE2024 EUR-1.225.911; dieper −72pct).
4. Dual vs OLVT / Glorieux / Zorgkas indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2011":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after Vlaamse Zorgkas — Heilig Hart Lier YE2025 Medium"
        x["notes"] = (
            "tick2011 Heilig Hart Lier Medium omzet JUMP 204.49m pnl LOSS 2.11m equity DROP 78.66m; FOI ready; "
            "AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Andries YE2025 deferred; next rq_2012; next every-10 2020"
        )
        x["instructions"] = (
            "Completed leftover Heilig Hart Lier YE2025 Medium CW; KBO 0412.080.645; "
            f"omzet JUMP {OMZET} pnl LOSS {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2012" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2012",
            "title": "leftover dual hole-fill after Heilig Hart Lier",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2011 after Heilig Hart Lier YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (Sint-Andries Tielt YE2025 live deferred / Sint-Trudo / Heilig Hart Leuven / AZ Sint-Jan Brugge / Vesalius / other unused YE2025 if live). "
                "Do NOT redo Heilig Hart Lier, Vlaamse Zorgkas, OLVT/AZ Sint-Blasius, AZ Oostende, Damiaan shell, Werken Glorieux, AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Zottegem/Turnhout/Waregem/Yperman/Maria Middelares/Imelda/Monica CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2011 Heilig Hart Lier; next every-10 2020; Sint-Andries YE2025 deferred",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "mode": "continuous",
        "current_sprint": "hole_fill",
        "last_tick_utc": UTC,
        "last_unit_id": "rq_2011",
        "ticks_completed": "2011",
        "paused": "no",
        "notes": (
            "tick2011 leftover Heilig Hart Lier 0412.080.645 Medium CW (omzet JUMP 204.49m pnl LOSS 2.11m equity DROP 78.66m bruto JUMP 92.49m FTE 1008.3; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; Sint-Andries YE2025 deferred; next rq_2012; next every-10 2020; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2011 - {UTC} - rq_2011 Heilig Hart Lier (omzet JUMP 204.49m / pnl LOSS 2.11m / Medium)

- Unit: **rq_2011** leftover dual after **rq_2010 EVERY-10 + Vlaamse Zorgkas**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **Heilig Hart Lier** YE2025 (KBO **0412.080.645**; Mechelsestraat 24 Lier; Antwerpen **hospital VZW**). **Sint-Andries Tielt** YE2025 also live deferred. Do not redo Vlaamse Zorgkas/OLVT/AZ Oostende/Werken Glorieux/AZ Alma/AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR204,492,026** JUMP +5.40%; pnl **LOSS EUR-2,108,644** (deeper vs YE2024 LOSS −1.23m); equity **EUR78,662,672** DROP −2.94%; bruto **EUR92,494,807** JUMP +1.20%; FTE **1008.3**; neerlegging **09.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 1 VE; email info@heilighartlier.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_heilig_hart_lier); foi + draft {GAP}; rq_2011=done + rq_2012 open; loop_state ticks=2011; raw under docs/doge/data/raw/tick2011/.
- FOI: **ready not sent** (human-gated; info@heilighartlier.be).
- NOT every-10 (**next every-10 is 2020**). Next: rq_2012 (AGB/FARO-if-YE2025 / AIESH-REW / Sint-Andries-Sint-Trudo / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
