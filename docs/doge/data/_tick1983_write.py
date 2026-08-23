# ephemeral tick1983 — IDETA YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T23:30:00Z"
ENTITY = "igs_ideta"
GAP = "gap_ideta_nbb_pdf_assets_debt_omzet_drop_matrix_l5"
SRC = "src_ideta_jr2025_cw"
SRC_EN = "src_ideta_jr2025_cw_en"
SRC_KBO = "src_ideta_kbo_1983"
SRC_SITE = "src_ideta_site_1983"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1983")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL IDETA YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0241098844/agence-intercommunale-de-developpement-economique-des-arrondissements-de-tournai-ath-et-des-communes-avoisinantes",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1983; YE2025 omzet DROP 12487300 pnl DROP 6266011 equity DROP 149646031 bruto DROP 9241984 FTE 78.6; neerlegging 07.08.2026; assets/debt Unknown; raw docs/doge/data/raw/tick1983/ideta_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN IDETA YE2025 statutory",
        "url": "https://www.companyweb.be/en/0241098844/agence-intercommunale-de-developpement-economique-des-arrondissements-de-tournai-ath-et-des-communes-avoisinantes",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1983; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1983/ideta_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO IDETA 0241.098.844 Actief CV Tournai",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0241098844",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1983; Actief CV; Quai Saint-Brice 35 7500 Tournai; email officiel.ic-ideta@ideta.be; 10 VE; Aanbestedende overheid; Wallonie picarde ADT",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "ideta.be Wallonie picarde territorial development ADT",
        "url": "https://ideta.be/",
        "publisher": "IDETA",
        "accessed_date": "2026-08-23",
        "source_class": "official_org",
        "notes": "tick1983; Tournai-Ath ADT / ZAE dual; sister of SPI",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ideta_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "12487300",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1983; omzet DROP 12487300 -30.41pct vs YE2024 17944125",
    },
    {
        "budget_id": "bud_ideta_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "6266011",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1983; pnl DROP 6266011 -34.33pct vs YE2024 9541269",
    },
    {
        "budget_id": "bud_ideta_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "149646031",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1983; equity DROP 149646031 -0.86pct vs YE2024 150950349",
    },
    {
        "budget_id": "bud_ideta_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "9241984",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1983; bruto DROP 9241984 -29.33pct vs YE2024 13077272",
    },
    {
        "budget_id": "bud_ideta_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "78.6",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1983; YE2025 FTE 78.6 vs YE2024 72.8",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ideta_jr2025_statutory_adt",
    "title": "IDETA YE2025 leftover Wallonie picarde ADT dual (omzet DROP 12.49m / pnl DROP 6.27m)",
    "entity_id": ENTITY,
    "beneficiary": "Tournai-Ath communes + ZAE dual",
    "legal_basis": "Code democratie locale intercommunale developpement economique CV",
    "decision_date": "2026-08-07",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "12487300",
    "cash_by_year": '{"2025_omzet":12487300,"2025_pnl":6266011,"2025_equity":149646031,"2025_bruto":9241984,"2025_fte":78.6}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0241098844/agence-intercommunale-de-developpement-economique-des-arrondissements-de-tournai-ath-et-des-communes-avoisinantes",
    "stated_goal": "Wallonie picarde territorial economic development ADT / ZAE parks",
    "cut_option": "Publish NBB PDF assets/debt + omzet/pnl DROP recon + ZAE sales matrix FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>Tournai>IDETA>JR2025_statutory_L5",
    "notes": "tick1983; Medium CW; assets/debt Unknown; dual of SPI; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHwapi YE2025 deferred",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ideta_omzet_drop_12_49m_pnl_drop_6_27m_jr2025",
    "name": "IDETA omzet DROP 12.49m / pnl DROP 6.27m / equity 149.65m (Wallonie picarde ADT YE2025)",
    "level": "L5",
    "type": "walloon_igs_adt_dual",
    "hierarchy_path": "Wallonie>Hainaut>Tournai>IDETA>JR2025_statutory_L5",
    "annual_cost_eur": "12487300",
    "total_cost_eur": "149646031",
    "tco_notes": "statutory omzet DROP 12487300 pnl DROP 6266011 equity DROP 149646031 bruto DROP 9241984 FTE 78.6; assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Tournai-Ath communes via ADT / ZAE financing shell",
    "stated_goal": "Territorial economic development and industrial parks",
    "measured_outcome": "Medium CW YE2025; omzet/pnl ~-30pct; 150m equity shell; NBB PDF residual",
    "absurdity_score": "4.5",
    "cost_score": "5.5",
    "difficulty": "3.5",
    "priority_index": "4.85",
    "cut_proposal": "Publish NBB PDF + omzet/pnl DROP recon + ZAE sales / SPI dual FOI",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1983 leftover dual; Medium CW; not TE-additive pure-waste top10; next every-10 1990; CHwapi YE2025 unused deferred",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "IDETA (Wallonie picarde ADT / developpement economique)",
    "name_fr": "IDETA (ADT Wallonie picarde / developpement economique)",
    "name_en": "IDETA (Wallonie picarde territorial development ADT IGS)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "https://ideta.be/",
    "foi_email": "officiel.ic-ideta@ideta.be",
    "foi_postal": "Quai Saint-Brice 35, 7500 Tournai",
    "notes": "tick1983 YE2025 Medium CW NL+EN + Strong KBO 0241.098.844 Actief CV; omzet DROP 12.49m pnl DROP 6.27m equity DROP 149.65m bruto DROP 9.24m FTE 78.6; assets/debt Unknown; neerlegging 07.08.2026; 10 VE; FOI gap_ideta_nbb_pdf_assets_debt_omzet_drop_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHwapi YE2025 deferred; do not redo SPI/Vivalia/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP*/IBH/IGRETEC",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Hainaut>Tournai>IDETA>NBB_PDF_assets_debt_omzet",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); omzet/pnl DROP ~-30pct recon; ZAE sales matrix; dual vs SPI",
    "why_it_matters": "Medium CW shows ~150m equity ADT with omzet/pnl ~-30pct without balance sheet; ZAE dual opacity",
    "priority": "6",
    "recipient_body": "IDETA",
    "recipient_email": "officiel.ic-ideta@ideta.be",
    "recipient_postal": "https://ideta.be/",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_ideta_jr2025_statutory_adt",
    "linked_leaderboard_id": "lb_ideta_omzet_drop_12_49m_pnl_drop_6_27m_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1983; human-send only; Medium CW; next every-10 1990; CHwapi YE2025 unused deferred",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — IDETA (NBB PDF / assets-debt / omzet DROP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** IDETA CV — KBO **0241.098.844**  
**recipient:** officiel.ic-ideta@ideta.be  
**sources:** [CW NL](https://www.companyweb.be/nl/0241098844/agence-intercommunale-de-developpement-economique-des-arrondissements-de-tournai-ath-et-des-communes-avoisinantes) · [CW EN](https://www.companyweb.be/en/0241098844/agence-intercommunale-de-developpement-economique-des-arrondissements-de-tournai-ath-et-des-communes-avoisinantes) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0241098844) · [site](https://ideta.be/)  
**tick:** 1983  
**confidence:** Medium (CW NL+EN; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **07.08.2026**): omzet **EUR12,487,300** DROP -30.41%; pnl **EUR6,266,011** DROP -34.33%; equity **EUR149,646,031** DROP -0.86%; bruto **EUR9,241,984** DROP -29.33%; FTE **78.6**; assets/debt **Unknown**.
- Wallonie picarde ADT (Tournai-Ath). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024. CHwapi YE2025 deferred.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: IDETA — officiel.ic-ideta@ideta.be
Quai Saint-Brice 35, 7500 Tournai
cc: SPW economie / Province Hainaut transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 IDETA + balans + omzet/ZAE recon (KBO 0241.098.844)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 07.08.2026).
2. Assets / schulden LT-ST / cash.
3. Recon omzet/pnl DROP (~-30pct vs YE2024).
4. ZAE sales / terrain matrix 2025.
5. Dual vs SPI indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1983":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after SPI — IDETA YE2025 Medium"
        x["notes"] = "tick1983 IDETA Medium omzet DROP 12.49m pnl DROP 6.27m; FOI ready; CHwapi YE2025 deferred; next rq_1984; next every-10 1990"
        x["instructions"] = (
            "Completed leftover IDETA Wallonie picarde ADT YE2025 Medium CW; KBO 0241.098.844; "
            "omzet DROP 12487300 pnl DROP 6266011 equity DROP 149646031 bruto DROP 9241984 FTE 78.6; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1984" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1984",
            "title": "leftover dual hole-fill after IDETA",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1983 after IDETA YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital (CHwapi if YE2025 / other). Do NOT redo IDETA, SPI, Vivalia, IDELUX Finances, IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE, IPALLE, INTRADEL, TIBI, IDELUX Environnement, IDELUX Eau.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1983 IDETA; CHwapi YE2025 deferred; next every-10 1990",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1983",
        "ticks_completed": "1983",
        "paused": "no",
        "notes": "tick1983 leftover IDETA 0241.098.844 Medium CW (omzet DROP 12.49m pnl DROP 6.27m equity DROP 149.65m bruto DROP 9.24m FTE 78.6; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; CHwapi YE2025 deferred; next rq_1984; next every-10 1990; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1983 - 2026-08-23T23:30:00Z - rq_1983 IDETA (omzet DROP 12.49m / pnl DROP 6.27m / Medium)

- Unit: **rq_1983** leftover dual after **rq_1982 SPI**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO/AIESH/REW still **YE2024**. Took preferred leftover **IDETA** YE2025 (KBO **0241.098.844**; Quai Saint-Brice 35 Tournai; Wallonie picarde **ADT**). **CHwapi** YE2025 also live (omzet 337.7m / equity DROP 46pct) deferred. Do not redo SPI/Vivalia/IDELUX Finances/IFIGA/SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/HELORA/BEP*/IBH/IGRETEC/IPFBW.
- Found: Companyweb NL+EN YE2025 - omzet **EUR12,487,300** DROP -30.41%; pnl **EUR6,266,011** DROP -34.33%; equity **EUR149,646,031** DROP -0.86%; bruto **EUR9,241,984** DROP -29.33%; FTE **78.6**; neerlegging **07.08.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief CV 10 VE; email officiel.ic-ideta@ideta.be.
- Wrote: sources (+4); budgets (+5); commitments (+1); leaderboard (+1); entities (+1 igs_ideta); foi + draft gap_ideta_nbb_pdf_assets_debt_omzet_drop_matrix_l5; rq_1983=done + rq_1984 open; loop_state ticks=1983.
- FOI: **ready not sent** (human-gated).
- NOT every-10 (**next every-10 is 1990**). Next: rq_1984 (AGB/FARO-if-YE2025 / AIESH-REW / CHwapi / unused DSO-IGS-HVZ).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1983" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1983")
