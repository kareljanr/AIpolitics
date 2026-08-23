# ephemeral tick2006 — AZ Alma YE2025 Medium (leftover dual after AZ St.-Elisabeth Herentals)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T05:40:00Z"
ENTITY = "vzw_az_alma"
GAP = "gap_az_alma_nbb_pdf_assets_debt_pnl_jump_matrix_l5"
SRC = "src_az_alma_jr2025_cw"
SRC_EN = "src_az_alma_jr2025_cw_en"
SRC_FR = "src_az_alma_jr2025_cw_fr"
SRC_KBO = "src_az_alma_kbo_2006"
SRC_SITE = "src_az_alma_site_2006"

OMZET = "191400137"
PNL = "2635911"
EQUITY = "105261488"
BRUTO = "99167846"
FTE = "1125.4"
OMZET24 = "183221510"
PNL24 = "1445603"
EQUITY24 = "106540679"
BRUTO24 = "95492173"


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
r = next(x for x in qrows if x.get("task_id") == "rq_2006")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL AZ Alma YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0463862908/algemeen-ziekenhuis-alma",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2006; YE2025 omzet JUMP {OMZET} pnl JUMP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; neerlegging 16.07.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2006/alma_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN AZ Alma YE2025 statutory",
        "url": "https://www.companyweb.be/en/0463862908/algemeen-ziekenhuis-alma",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2006; EN mirror YE2025 Medium; filed 16-07-2026; Last balance sheet year 2025; raw docs/doge/data/raw/tick2006/alma_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR AZ Alma YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0463862908/algemeen-ziekenhuis-alma",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2006; FR mirror YE2025 Medium; deposés le 16-07-2026; raw docs/doge/data/raw/tick2006/alma_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO AZ Alma 0463.862.908 Actief VZW Eeklo",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463862908",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2006; Actief VZW since 06.07.1998; Algemeen Ziekenhuis Alma; Ringlaan 15 9900 Eeklo; no KBO email; 2 VE; Aanbestedende overheid",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "azalma.be AZ Alma",
        "url": "https://www.azalma.be/",
        "publisher": "AZ Alma",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2006; Eeklo regional hospital; info@azalma.be",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_az_alma_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2006; omzet JUMP {OMZET} +4.46pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_az_alma_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2006; pnl JUMP {PNL} +82.34pct vs YE2024 {PNL24}",
    },
    {
        "budget_id": "bud_az_alma_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2006; equity DROP {EQUITY} -1.20pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_az_alma_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2006; bruto JUMP {BRUTO} +3.85pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_az_alma_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": f"tick2006; YE2025 FTE {FTE}",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_az_alma_jr2025_statutory_hospital",
    "title": "AZ Alma YE2025 leftover hospital dual (omzet JUMP 191.40m / pnl JUMP 2.64m / equity DROP 105.26m)",
    "entity_id": ENTITY,
    "beneficiary": "Eeklo-region hospital patients / AZ Alma",
    "legal_basis": "VZW/ASBL hospital (KBO 0463.862.908)",
    "decision_date": "2026-07-16",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0463862908/algemeen-ziekenhuis-alma",
    "stated_goal": "Regional hospital care (Eeklo / Meetjesland)",
    "cut_option": "Publish NBB PDF assets/debt + pnl JUMP recon FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "OostVlaanderen>AZ_Alma>JR2025_statutory_L5",
    "notes": "tick2006; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO YE2024; Maria Middelares/Imelda CW N/A omzet; AZ St.-Elisabeth Herentals already mined",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

# priority_index = 0.55*5.5 + 0.35*5.5 + 0.10*4.0 = 5.35
lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_az_alma_omzet_jump_191_40m_pnl_jump_2_64m_equity_drop_jr2025",
    "name": "AZ Alma omzet JUMP 191.40m / pnl JUMP 2.64m / equity DROP 105.26m (YE2025)",
    "level": "L5",
    "type": "flemish_hospital_vzw_dual",
    "hierarchy_path": "OostVlaanderen>AZ_Alma>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl JUMP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Eeklo patients via AZ Alma VZW",
    "stated_goal": "Regional hospital care",
    "measured_outcome": "Medium CW YE2025; 191.40m omzet JUMP +4.46pct with pnl JUMP +82pct and mild equity DROP -1.2pct; NBB PDF residual",
    "absurdity_score": "5.5",
    "cost_score": "5.5",
    "difficulty": "4.0",
    "priority_index": "5.35",
    "cut_proposal": "Publish NBB PDF assets/debt FOI; recon pnl JUMP path vs Herentals/Vitaz/Emmaüs",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2006 leftover dual; Medium CW; TE-adjacent hospital flow not pure-waste top10; next every-10 2010",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "AZ Alma / Algemeen Ziekenhuis Alma",
    "name_fr": "AZ Alma / Algemeen Ziekenhuis Alma",
    "name_en": "AZ Alma (Eeklo hospital)",
    "level": "asbl",
    "parent_id": "prov_oost_vlaanderen",
    "community_language": "nl",
    "website": "https://www.azalma.be/",
    "foi_email": "info@azalma.be",
    "foi_postal": "Ringlaan 15, 9900 Eeklo",
    "notes": "tick2006 YE2025 Medium CW NL+EN+FR + Strong KBO 0463.862.908 Actief VZW; omzet JUMP 191.40m pnl JUMP 2.64m equity DROP 105.26m bruto JUMP 99.17m FTE 1125.4; assets/debt Unknown; neerlegging 16.07.2026; 2 VE; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO YE2024; Maria Middelares/Imelda CW N/A; do not redo AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC",
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
    "hierarchy_path": "OostVlaanderen>AZ_Alma>NBB_PDF_assets_debt_pnl_jump",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); pnl JUMP recon vs YE2024",
    "why_it_matters": "Medium CW shows 191.40m omzet Eeklo hospital VZW with pnl JUMP +82pct without balance sheet",
    "priority": "7",
    "recipient_body": "Algemeen Ziekenhuis Alma VZW / AZ Alma",
    "recipient_email": "info@azalma.be",
    "recipient_postal": "Ringlaan 15, 9900 Eeklo",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "linked_commitment_id": "comm_az_alma_jr2025_statutory_hospital",
    "linked_leaderboard_id": "lb_az_alma_omzet_jump_191_40m_pnl_jump_2_64m_equity_drop_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2006; human-send only; Medium CW; next every-10 2010",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — AZ Alma (NBB PDF / assets-debt / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Algemeen Ziekenhuis Alma VZW / AZ Alma — KBO **0463.862.908**  
**recipient:** info@azalma.be · Ringlaan 15, 9900 Eeklo  
**sources:** [CW NL](https://www.companyweb.be/nl/0463862908/algemeen-ziekenhuis-alma) · [CW EN](https://www.companyweb.be/en/0463862908/algemeen-ziekenhuis-alma) · [CW FR](https://www.companyweb.be/fr/0463862908/algemeen-ziekenhuis-alma) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0463862908) · [site](https://www.azalma.be/)  
**tick:** 2006  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **16.07.2026**): omzet **EUR191,400,137** JUMP +4.46%; pnl **EUR2,635,911** JUMP +82.34%; equity **EUR105,261,488** DROP −1.20%; bruto **EUR99,167,846** JUMP +3.85%; FTE **1125.4**; assets/debt **Unknown**.
- Eeklo VZW hospital. Preferred stall: AGB Bornem / FARO still YE2024. Maria Middelares/Imelda CW N/A omzet. AZ St.-Elisabeth Herentals already mined.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: Algemeen Ziekenhuis Alma VZW / AZ Alma — Ringlaan 15, 9900 Eeklo
info@azalma.be
cc: Agentschap Zorg en Gezondheid / Provincie Oost-Vlaanderen indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 AZ Alma + balans (KBO 0463.862.908)
Geachte, op grond van toepasselijke openbaarheidsregels vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 16.07.2026).
2. Assets / schulden LT-ST / cash.
3. Recon pnl JUMP (EUR2.635.911 vs YE2024 EUR1.445.603; +82,34pct).
4. Dual vs Vitaz / Herentals indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

for x in qrows:
    if x.get("task_id") == "rq_2006":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after AZ St.-Elisabeth Herentals — AZ Alma YE2025 Medium"
        x["notes"] = (
            "tick2006 AZ Alma Medium omzet JUMP 191.40m pnl JUMP 2.64m equity DROP 105.26m; FOI ready; "
            "AGB Bornem JR2024; FARO YE2024; Maria Middelares/Imelda CW N/A; next rq_2007; next every-10 2010"
        )
        x["instructions"] = (
            "Completed leftover AZ Alma YE2025 Medium CW; KBO 0463.862.908; "
            f"omzet JUMP {OMZET} pnl JUMP {PNL} equity DROP {EQUITY} bruto JUMP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
if not any(x.get("task_id") == "rq_2007" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2007",
            "title": "leftover dual hole-fill after AZ Alma",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2006 after AZ Alma YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (AZ Maria Middelares / AZ Glorieux / AZ Oostende / other unused YE2025 if live). "
                "Do NOT redo AZ Alma, AZ St.-Elisabeth Herentals, Vitaz, Emmaüs, AZORG, Z.org KU Leuven, AZ Delta, AZJP, ZAS, CHR Verviers, CNDG, Haute Senne, CHBA, Saint-Luc, GHdC, Humani, CHIREC, CHU Tivoli, CHR Citadelle, ISoSL, Epicura, CHwapi, CHU UCL Namur, IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, "
                "BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, "
                "IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, "
                "Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, Tibi, IDELUX Environnement, IDELUX Eau, IDEA. "
                "Maria Middelares/Imelda CW N/A omzet — take only if figures appear. OLV Aalst deferred AZORG double-count."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2006 AZ Alma; next every-10 2010; Maria Middelares CW N/A omzet",
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
        "last_unit_id": "rq_2006",
        "ticks_completed": "2006",
        "paused": "no",
        "notes": (
            "tick2006 leftover AZ Alma 0463.862.908 Medium CW (omzet JUMP 191.40m pnl JUMP 2.64m equity DROP 105.26m bruto JUMP 99.17m FTE 1125.4; "
            "assets/debt Unknown); AGB Bornem JR2024; FARO YE2024; Maria Middelares/Imelda CW N/A; next rq_2007; next every-10 2010; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_block = f"""

## Tick 2006 - {UTC} - rq_2006 AZ Alma (omzet JUMP 191.40m / pnl JUMP 2.64m / Medium)

- Unit: **rq_2006** leftover dual after **rq_2005 AZ St.-Elisabeth Herentals**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**. Maria Middelares/Imelda CW **N/A omzet**. Took preferred leftover **AZ Alma** YE2025 (KBO **0463.862.908**; Ringlaan 15 Eeklo; Oost-Vlaanderen **hospital VZW**). Do not redo AZ St.-Elisabeth Herentals/Vitaz/Emmaüs/AZORG/Z.org KU Leuven/AZ Delta/AZJP/ZAS/CHR Verviers/CNDG/Haute Senne/CHBA/Saint-Luc/GHdC/Humani/CHIREC.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR191,400,137** JUMP +4.46%; pnl **EUR2,635,911** JUMP +82.34%; equity **EUR105,261,488** DROP −1.20%; bruto **EUR99,167,846** JUMP +3.85%; FTE **1125.4**; neerlegging **16.07.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 2 VE; email info@azalma.be.
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 vzw_az_alma); foi + draft {GAP}; rq_2006=done + rq_2007 open; loop_state ticks=2006; raw under docs/doge/data/raw/tick2006/.
- FOI: **ready not sent** (human-gated; info@azalma.be).
- NOT every-10 (**next every-10 is 2010**). Next: rq_2007 (AGB/FARO-if-YE2025 / AIESH-REW / AZ Maria Middelares-Glorieux-Oostende / unused DSO-IGS-HVZ).
"""
log_path.write_text(log_path.read_text(encoding="utf-8") + log_block, encoding="utf-8")
print("log ok")
