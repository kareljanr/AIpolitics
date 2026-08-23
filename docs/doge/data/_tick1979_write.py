# ephemeral tick1979 — IFIGA YE2025
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-23T22:00:00Z"
ENTITY = "igs_ifiga"
GAP = "gap_ifiga_nbb_pdf_assets_debt_ores_dividend_matrix_l5"
SRC = "src_ifiga_jr2025_cw"
SRC_EN = "src_ifiga_jr2025_cw_en"
SRC_KBO = "src_ifiga_kbo_1979"


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
r = next(x for x in qrows if x.get("task_id") == "rq_1979")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))
if st == "done":
    raise SystemExit("ALREADY_DONE")

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL IFIGA YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0257838371/ifiga",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1979; YE2025 pnl JUMP 604960 equity JUMP 10086790 bruto NEG -82556 FTE 1; omzet/assets/debt Unknown; neerlegging 09.07.2026; raw docs/doge/data/raw/tick1979/ifiga_cw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN IFIGA YE2025 statutory",
        "url": "https://www.companyweb.be/en/0257838371/ifiga",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-23",
        "source_class": "secondary_aggregator",
        "notes": "tick1979; EN mirror YE2025 Medium; raw docs/doge/data/raw/tick1979/ifiga_cw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO IFIGA 0257.838.371 Actief CV Comines-Warneton",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0257838371",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-23",
        "source_class": "official_register",
        "notes": "tick1979; Actief CV; Sinte-Annaplein(KOM)/Place Sainte-Anne 21 7780 Comines-Warneton; Aanbestedende overheid; NACE 84.119; no KBO email/web",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_ifiga_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "604960",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1979; pnl JUMP 604960 +26.78pct vs YE2024 477188",
    },
    {
        "budget_id": "bud_ifiga_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "10086790",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1979; equity JUMP 10086790 +3.12pct vs YE2024 9781830",
    },
    {
        "budget_id": "bud_ifiga_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "-82556",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge NEG",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1979; bruto NEG -82556 improved +24.24pct vs YE2024 -108964 still NEG",
    },
    {
        "budget_id": "bud_ifiga_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": "1",
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC,
        "confidence": "medium",
        "notes": "tick1979; YE2025 FTE 1 IPF shell",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_ifiga_jr2025_statutory_ipf",
    "title": "IFIGA YE2025 leftover Picardie Wallonne ORES IPF dual (pnl JUMP 0.605m equity JUMP 10.09m)",
    "entity_id": ENTITY,
    "beneficiary": "Comines-Warneton / Picardie Wallonne communes + ORES Assets dual",
    "legal_basis": "Code democratie locale intercommunale pure financement CV",
    "decision_date": "2026-07-09",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": "604960",
    "cash_by_year": '{"2025_pnl":604960,"2025_equity":10086790,"2025_bruto":-82556,"2025_fte":1}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/nl/0257838371/ifiga",
    "stated_goal": "Pure financing intercommunale for municipal energy stakes (ORES IPF cluster)",
    "cut_option": "Publish NBB PDF assets/debt + ORES Assets dividend/parts matrix FOI",
    "source_id": SRC,
    "confidence": "medium",
    "hierarchy_path": "Wallonie>Hainaut>Comines-Warneton>IFIGA>JR2025_statutory_L5",
    "notes": "tick1979; Medium CW; omzet/assets/debt Unknown; classic ORES IPF after SOFILUX; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_ifiga_pnl_jump_0_605m_equity_jump_10_09m_bruto_neg_jr2025",
    "name": "IFIGA pnl JUMP 0.605m / equity JUMP 10.09m / bruto NEG 82.6k (Picardie Wallonne ORES IPF YE2025)",
    "level": "L5",
    "type": "walloon_igs_energy_ipf_dual",
    "hierarchy_path": "Wallonie>Hainaut>Comines-Warneton>IFIGA>JR2025_statutory_L5",
    "annual_cost_eur": "604960",
    "total_cost_eur": "10086790",
    "tco_notes": "statutory pnl JUMP 604960 equity JUMP 10086790 bruto NEG -82556 FTE 1; omzet/assets/debt Unknown",
    "confidence": "medium",
    "source_id": SRC,
    "beneficiaries": "Comines-Warneton / Picardie Wallonne communes via ORES Assets financing shell",
    "stated_goal": "Municipal pure-financing vehicle for energy network stakes",
    "measured_outcome": "Medium CW YE2025; thin FTE 1 shell with 10.09m equity; bruto still NEG; NBB PDF residual",
    "absurdity_score": "4.5",
    "cost_score": "2.5",
    "difficulty": "3.0",
    "priority_index": "3.5",
    "cut_proposal": "Publish NBB PDF + ORES dividend attribution + dual vs SOFILUX/FINIMO/FINEST/IDEFIN FOI; scrutinise persistent bruto NEG",
    "status": "active",
    "struck_reason": "",
    "notes": "tick1979 leftover dual; Medium CW; unused Picardie Wallonne IPF after SOFILUX; not TE-additive pure-waste top10",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "IFIGA (Picardie Wallonne ORES IPF)",
    "name_fr": "IFIGA (IPF Picardie wallonne / Comines-Warneton)",
    "name_en": "IFIGA (Picardie Wallonne ORES pure financing IGS)",
    "level": "intercommunale",
    "parent_id": "wallonie_gov",
    "community_language": "fr",
    "website": "",
    "foi_email": "",
    "foi_postal": "Place Sainte-Anne 21, 7780 Comines-Warneton",
    "notes": "tick1979 YE2025 Medium CW NL+EN + Strong KBO 0257.838.371 Actief CV; pnl JUMP 0.605m equity JUMP 10.09m bruto NEG 82.6k FTE 1; omzet/assets/debt Unknown; neerlegging 09.07.2026; classic ORES IPF cluster (with Finest/Finimo/Idefin/Sofilux/IPFBW/CENEO/IEG); FOI gap_ifiga_nbb_pdf_assets_debt_ores_dividend_matrix_l5; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP Environnement/LOGIPOLE/BEP NAMUR/IBH/CENEO/IEG/IPFBW/ORES Assets/SOCOFE",
}
if not any(x.get("entity_id") == ENTITY for x in erows):
    erows.append(ne)
save("docs/doge/data/entities.csv", erows, efields)
print("entities", len(erows))

frows, ffields = load("docs/doge/data/foi_queue.csv")
nf = {
    **{k: "" for k in ffields},
    "gap_id": GAP,
    "hierarchy_path": "Wallonie>Hainaut>Comines-Warneton>IFIGA>NBB_PDF_assets_debt_ores_matrix",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash/omzet); ORES Assets dividend and parts attribution matrix; bruto NEG recon; dual vs SOFILUX/FINIMO/FINEST/IDEFIN/IPFBW",
    "why_it_matters": "Medium CW shows 10.09m equity / 0.605m pnl IPF shell with persistent bruto NEG without balance sheet or turnover; ORES Assets dual opacity",
    "priority": "6",
    "recipient_body": "IFIGA / Ville de Comines-Warneton",
    "recipient_email": "",
    "recipient_postal": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0257838371",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-23",
    "linked_commitment_id": "comm_ifiga_jr2025_statutory_ipf",
    "linked_leaderboard_id": "lb_ifiga_pnl_jump_0_605m_equity_jump_10_09m_bruto_neg_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick1979; human-send only; Medium CW; next every-10 1980; KBO has no email — route via commune openbaarheid if needed",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — IFIGA (NBB PDF / assets-debt / ORES dividend matrix)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** IFIGA CV — KBO **0257.838.371**  
**recipient:** IFIGA / Ville de Comines-Warneton (KBO has no email; route via commune openbaarheid if needed)  
**sources:** [CW NL](https://www.companyweb.be/nl/0257838371/ifiga) · [CW EN](https://www.companyweb.be/en/0257838371/ifiga) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0257838371)  
**tick:** 1979  
**confidence:** Medium (CW NL+EN; omzet/assets/debt Unknown)

## Context
- YE **2025** (neerlegging **09.07.2026**): pnl **EUR604,960** JUMP +26.78%; equity **EUR10,086,790** JUMP +3.12%; bruto **NEG EUR-82,556** (improved vs -108,964); FTE **1**; omzet/assets/debt **Unknown**.
- Classic Walloon ORES Assets IPF (cluster with Finest/Finimo/Idefin/Sofilux/IPFBW/CENEO/IEG). Preferred stall: AGB Bornem / FARO / AIESH / REW still YE2024.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: IFIGA — Place Sainte-Anne 21, 7780 Comines-Warneton
cc: Ville de Comines-Warneton openbaarheid / ORES Assets / SPW transparence
Betreft: Openbaarmaking NBB-jaarrekening 2025 IFIGA + balans + ORES-dividendmatrix (KBO 0257.838.371)
Geachte, op grond van decret wallon / CDLD vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 09.07.2026).
2. Assets / schulden LT-ST / cash / omzet indien niet gepubliceerd.
3. ORES Assets parts + dividend attribution 2025.
4. Recon bruto NEG persistent (-82.6k vs -109.0k YE2024).
5. Dual vs SOFILUX / FINIMO / FINEST / IDEFIN / IPFBW indien relevant.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)

for x in qrows:
    if x.get("task_id") == "rq_1979":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual hole-fill after SOFILUX — IFIGA YE2025 Medium"
        x["notes"] = "tick1979 IFIGA Medium pnl JUMP 0.605m equity JUMP 10.09m; FOI ready; next rq_1980; next every-10 1980"
        x["instructions"] = (
            "Completed leftover IFIGA Picardie Wallonne ORES IPF YE2025 Medium CW; KBO 0257.838.371; "
            "pnl JUMP 604960 equity JUMP 10086790 bruto NEG -82556 FTE 1; FOI " + GAP
        )
if not any(x.get("task_id") == "rq_1980" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_1980",
            "title": "EVERY-10 + leftover dual hole-fill after IFIGA",
            "sprint": "hole_fill",
            "priority": "9",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": "Tick 1979 after IFIGA YE2025 Medium. MANDATORY every-10: refresh progress_every_10_ticks.md + doge_waste_top10_current.md THEN one leftover dual. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy. Do NOT redo IFIGA, SOFILUX, IDEFIN, FINIMO, FINEST, HYGEA, BEP Environnement, LOGIPOLE, BEP NAMUR, IBH, BEP Crematorium, BEP Expansion, IEG, CENEO, CISCH, HELORA, iMio, Passelecq, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL, ORES Assets, SOCOFE.",
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick1979 IFIGA; EVERY-10 at 1980",
        }
    )
save("docs/doge/data/research_queue.csv", qrows, qfields)
print("queue ok")

lsrows, lsfields = load("docs/doge/data/loop_state.csv")
lsrows[-1].update(
    {
        "last_tick_utc": UTC,
        "last_unit_id": "rq_1979",
        "ticks_completed": "1979",
        "paused": "no",
        "notes": "tick1979 leftover IFIGA 0257.838.371 Medium CW (pnl JUMP 0.605m equity JUMP 10.09m bruto NEG 82.6k FTE 1; omzet/assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_1980 EVERY-10; continuous hole_fill",
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

logp = Path("docs/doge/loop_log.md")
entry = """

## Tick 1979 - 2026-08-23T22:00:00Z - rq_1979 IFIGA (pnl JUMP 0.605m / equity JUMP 10.09m / Medium)

- Unit: **rq_1979** leftover dual after **rq_1978 SOFILUX**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH/REW still **YE2024**. Took unused leftover **IFIGA** YE2025 (KBO **0257.838.371**; Place Sainte-Anne 21 Comines-Warneton; Picardie Wallonne **ORES Assets IPF**). Do not redo SOFILUX/IDEFIN/FINIMO/FINEST/HYGEA/BEP Environnement/LOGIPOLE/BEP NAMUR/IBH/BEP Crematorium/BEP Expansion/IEG/CENEO/CISCH/HELORA/ORES Assets/SOCOFE/IPFBW/IGRETEC/Aquiris/SPGE/IRE*/FANC/SCK/EURIDICE/BRUGEL.
- Found: Companyweb NL+EN YE2025 - pnl **EUR604,960** JUMP +26.78%; equity **EUR10,086,790** JUMP +3.12%; bruto **NEG EUR-82,556** (improved vs -108,964); FTE **1**; neerlegging **09.07.2026**. Omzet/assets/debt Unknown. Medium confidence. Strong KBO Actief CV; no KBO email/web.
- Wrote: sources (+3); budgets (+4); commitments (+1); leaderboard (+1); entities (+1 igs_ifiga); foi + draft gap_ifiga_nbb_pdf_assets_debt_ores_dividend_matrix_l5; rq_1979=done + rq_1980 open (EVERY-10); loop_state ticks=1979.
- FOI: **ready not sent** (human-gated; no KBO email — route via commune if needed).
- NOT every-10 (**next every-10 is 1980**). Next: rq_1980 (EVERY-10 progress + AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ).
"""
text = logp.read_text(encoding="utf-8")
if "## Tick 1979" not in text:
    logp.write_text(text.rstrip() + entry + "\n", encoding="utf-8")
    print("log appended")
else:
    print("log already has 1979")
