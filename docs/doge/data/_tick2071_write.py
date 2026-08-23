# ephemeral tick2071 — MSW NZVL YE2025 Medium (leftover dual after Welvaart)
import csv
import sys
from pathlib import Path

csv.field_size_limit(sys.maxsize)

UTC = "2026-08-24T22:50:00Z"
ENTITY = "vzw_msw_nzvl"
GAP = "gap_msw_nzvl_nbb_pdf_assets_debt_pnl_flip_loss_matrix_l5"
SRC = "src_msw_nzvl_jr2025_cw"
SRC_EN = "src_msw_nzvl_jr2025_cw_en"
SRC_FR = "src_msw_nzvl_jr2025_cw_fr"
SRC_KBO = "src_msw_nzvl_kbo_2071"
SRC_SITE = "src_msw_nzvl_site_2071"

OMZET = "435516"
PNL = "-304338"
EQUITY = "3081864"
BRUTO = "-12115"
FTE = "0"
OMZET24 = "420000"
PNL24 = "10918"
EQUITY24 = "3386202"
BRUTO24 = "305484"
PI = "4.2"


def load(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        fields = list(rows[0].keys()) if rows else []
        fields = [f.lstrip("\ufeff") for f in fields]
        for row in rows:
            if any(k.startswith("\ufeff") for k in row):
                for k in list(row):
                    if k.startswith("\ufeff"):
                        row[k.lstrip("\ufeff")] = row.pop(k)
        return rows, fields


def save(path, rows, fields):
    fields = [f.lstrip("\ufeff") for f in fields]
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


qrows, qfields = load("docs/doge/data/research_queue.csv")
r = next(x for x in qrows if x.get("task_id") == "rq_2071")
st = (r.get("status") or "").lower()
if st not in ("open", "in_progress"):
    raise SystemExit("RACE:" + str(r.get("status")))

srows, sfields = load("docs/doge/data/sources.csv")
for ns in [
    {
        **{k: "" for k in sfields},
        "source_id": SRC,
        "title": "Companyweb NL VZW MSW NZVL YE2025 statutory",
        "url": "https://www.companyweb.be/nl/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": f"tick2071; YE2025 omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto FLIP {BRUTO} FTE {FTE}; neerlegging 24.04.2026; assets/debt Unknown; raw docs/doge/data/raw/tick2071/msw_nl.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_EN,
        "title": "Companyweb EN VZW MSW NZVL YE2025 statutory",
        "url": "https://www.companyweb.be/en/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2071; EN mirror YE2025 Medium; filed 24-04-2026; FTE 0; raw docs/doge/data/raw/tick2071/msw_en.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_FR,
        "title": "Companyweb FR VZW MSW NZVL YE2025 statutory",
        "url": "https://www.companyweb.be/fr/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen",
        "publisher": "Companyweb (NBB-derived)",
        "accessed_date": "2026-08-24",
        "source_class": "secondary_aggregator",
        "notes": "tick2071; FR mirror YE2025 Medium; raw docs/doge/data/raw/tick2071/msw_fr.html",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_KBO,
        "title": "KBO VZW MSW NZVL 0419.384.646 Actief VZW Aalter",
        "url": "https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419384646",
        "publisher": "KBO FOD Economie",
        "accessed_date": "2026-08-24",
        "source_class": "official_register",
        "notes": "tick2071; Actief VZW; Maldegemseweg 5 9910 Aalter; 0 VE; afkorting VZW MSW NZVL; KBO email/web empty; aanbestedende flag not present; 7 bestuurders",
    },
    {
        **{k: "" for k in sfields},
        "source_id": SRC_SITE,
        "title": "Neutraal Ziekenfonds Vlaanderen contact (info@nzvl.be)",
        "url": "https://www.nzvl.be/contact",
        "publisher": "NZVL",
        "accessed_date": "2026-08-24",
        "source_class": "official_org",
        "notes": "tick2071; parent mutualiteit contact info@nzvl.be / 053 76 99 99; MSW VZW is medical-social works arm; raw docs/doge/data/raw/tick2071/nzvl_contact.html",
    },
]:
    if ns["source_id"] not in {x["source_id"] for x in srows}:
        srows.append(ns)
save("docs/doge/data/sources.csv", srows, sfields)
print("sources", len(srows))

brows, bfields = load("docs/doge/data/budgets.csv")
for nb in [
    {
        "budget_id": "bud_msw_nzvl_omzet_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": OMZET,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 omzet / Turnover",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2071; omzet JUMP {OMZET} +3.69pct vs YE2024 {OMZET24}",
    },
    {
        "budget_id": "bud_msw_nzvl_pnl_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": PNL,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Profit/Loss",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2071; pnl FLIP LOSS {PNL} vs YE2024 profit {PNL24}",
    },
    {
        "budget_id": "bud_msw_nzvl_equity_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": EQUITY,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Eigen vermogen / Equity",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2071; equity DROP {EQUITY} -8.99pct vs YE2024 {EQUITY24}",
    },
    {
        "budget_id": "bud_msw_nzvl_bruto_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": BRUTO,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW YE2025 Brutomarge / Gross margin",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2071; bruto FLIP {BRUTO} -103.97pct vs YE2024 {BRUTO24}",
    },
    {
        "budget_id": "bud_msw_nzvl_fte_jr2025_statutory",
        "entity_id": ENTITY,
        "year": "2025",
        "amount_eur": FTE,
        "amount_min_eur": "",
        "amount_max_eur": "",
        "basis": "CW social-balance FTE",
        "source_id": SRC_EN,
        "confidence": "medium",
        "notes": f"tick2071; YE2025 FTE {FTE} (CW Employees=0 FTE)",
    },
]:
    if nb["budget_id"] not in {x["budget_id"] for x in brows}:
        brows.append({**{k: "" for k in bfields}, **nb})
save("docs/doge/data/budgets.csv", brows, bfields)
print("budgets", len(brows))

crows, cfields = load("docs/doge/data/commitments.csv")
nc = {
    **{k: "" for k in cfields},
    "commitment_id": "comm_msw_nzvl_jr2025_statutory_mutualiteit",
    "title": "VZW MSW NZVL YE2025 leftover dual (omzet JUMP 0.44m / pnl FLIP LOSS 0.30m)",
    "entity_id": ENTITY,
    "beneficiary": "NZVL members via medical-social works VZW (mutualiteit arm)",
    "legal_basis": "VZW Medische en Sociale Werken Neutraal Ziekenfonds Vlaanderen (KBO 0419.384.646)",
    "decision_date": "2026-04-24",
    "start_year": "2025",
    "end_year": "2025",
    "total_envelope_eur": OMZET,
    "cash_by_year": f'{{"2025_omzet":{OMZET},"2025_pnl":{PNL},"2025_equity":{EQUITY},"2025_bruto":{BRUTO},"2025_fte":{FTE}}}',
    "remaining_eur": "0",
    "status": "active",
    "evaluation_url": "https://www.companyweb.be/en/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen",
    "stated_goal": "Medical-social works of Neutraal Ziekenfonds Vlaanderen (ziekenfondsen/zorgkassen dual)",
    "cut_option": "Publish NBB PDF assets/debt + RIZIV/mutualiteit subsidy vs own-revenue split FOI; explain pnl FLIP LOSS with bruto FLIP",
    "source_id": SRC_EN,
    "confidence": "medium",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Aalter>MSW_NZVL>JR2025_statutory_L5",
    "notes": "tick2071; Medium CW; assets/debt Unknown; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; not TE-additive of 348bn",
}
if not any(x.get("commitment_id") == nc["commitment_id"] for x in crows):
    crows.append(nc)
save("docs/doge/data/commitments.csv", crows, cfields)
print("commitments", len(crows))

lrows, lfields = load("docs/doge/data/leaderboard.csv")
nl = {
    **{k: "" for k in lfields},
    "item_id": "lb_msw_nzvl_omzet_jump_0_44m_pnl_flip_loss_jr2025",
    "name": "VZW MSW NZVL omzet JUMP 0.44m / pnl FLIP LOSS 0.30m (YE2025)",
    "level": "L5",
    "type": "vzw_mutualiteit_dual",
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Aalter>MSW_NZVL>JR2025_statutory_L5",
    "annual_cost_eur": OMZET,
    "total_cost_eur": EQUITY,
    "tco_notes": f"statutory omzet JUMP {OMZET} pnl FLIP LOSS {PNL} equity DROP {EQUITY} bruto FLIP {BRUTO} FTE {FTE}; assets/debt Unknown; mutualiteit MSW VZW dual",
    "confidence": "medium",
    "source_id": SRC_EN,
    "beneficiaries": "NZVL members via MSW medical-social works",
    "stated_goal": "Medical-social works / mutualiteit support",
    "measured_outcome": "Medium CW YE2025; 0.44m omzet JUMP +3.69pct with pnl FLIP LOSS -304k and bruto FLIP -12k; NBB PDF residual",
    "absurdity_score": "7.5",
    "cost_score": "1.5",
    "difficulty": "4.0",
    "priority_index": PI,
    "cut_proposal": "Publish NBB PDF assets/debt FOI; explain pnl FLIP LOSS vs YE2024 profit + bruto FLIP; map RIZIV/mutualiteit flows",
    "status": "active",
    "struck_reason": "",
    "notes": "tick2071 leftover dual; Medium CW; TE-adjacent mutualiteit flow not pure-waste top10; next every-10 2080",
}
if not any(x.get("item_id") == nl["item_id"] for x in lrows):
    lrows.append(nl)
save("docs/doge/data/leaderboard.csv", lrows, lfields)
print("leaderboard", len(lrows))

erows, efields = load("docs/doge/data/entities.csv")
ne = {
    **{k: "" for k in efields},
    "entity_id": ENTITY,
    "name_nl": "VZW MSW NZVL (Medische en Sociale Werken Neutraal Ziekenfonds Vlaanderen)",
    "name_fr": "ASBL MSW NZVL (oeuvres medico-sociales mutualite Neutraal Ziekenfonds)",
    "name_en": "VZW MSW NZVL (medical-social works Neutraal Ziekenfonds Vlaanderen)",
    "level": "other",
    "parent_id": "sec_flanders",
    "community_language": "nl",
    "website": "https://www.nzvl.be/",
    "foi_email": "info@nzvl.be",
    "foi_postal": "Maldegemseweg 5, 9910 Aalter",
    "notes": "tick2071 YE2025 Medium CW NL+EN+FR + Strong KBO 0419.384.646 Actief VZW 0 VE; omzet JUMP 0.44m pnl FLIP LOSS 0.30m equity DROP 3.08m bruto FLIP -12k FTE 0; assets/debt Unknown; neerlegging 24.04.2026; FOI "
    + GAP
    + "; preferred AGB Bornem JR2024; FARO/AIESH/REW YE2024; do not redo Welvaart/Vulpia/Compostela/Leiehome/Deinze/OLV Bornem/Huize SJ Ieper/Sint-Antonius/Wezembeek/Ter Burg/Christine/Vrijzicht/Pandje/H.Familie",
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
    "hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Aalter>MSW_NZVL>NBB_PDF_assets_debt_pnl_flip_loss",
    "entity_id": ENTITY,
    "what_is_missing": "NBB PDF jaarrekening 2025 full (assets/debt LT-ST/cash); RIZIV/mutualiteit subsidy vs own-revenue split; explanation of pnl FLIP LOSS -304k with bruto FLIP -12k",
    "why_it_matters": "Medium CW shows 0.44m omzet MSW VZW with pnl FLIP LOSS nearly equal to turnover and bruto FLIP without balanstotaal/assets/debt; material L5 residual for FOI",
    "priority": "8",
    "recipient_body": "VZW MSW NZVL / Neutraal Ziekenfonds Vlaanderen",
    "recipient_email": "info@nzvl.be",
    "recipient_postal": "Maldegemseweg 5, 9910 Aalter (also Statieplein 12, 9300 Aalst HQ)",
    "draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
    "status": "ready",
    "date_ready": "2026-08-24",
    "date_sent": "",
    "date_due": "",
    "date_answered": "",
    "response_summary": "",
    "linked_commitment_id": "comm_msw_nzvl_jr2025_statutory_mutualiteit",
    "linked_leaderboard_id": "lb_msw_nzvl_omzet_jump_0_44m_pnl_flip_loss_jr2025",
    "created_utc": UTC,
    "updated_utc": UTC,
    "notes": "tick2071; human-send only; Medium CW; next every-10 2080",
}
if not any(x.get("gap_id") == GAP for x in frows):
    frows.append(nf)
save("docs/doge/data/foi_queue.csv", frows, ffields)
print("foi", len(frows))

Path(f"docs/doge/foi/drafts/{GAP}.md").write_text(
    f"""# FOI draft — VZW MSW NZVL (NBB PDF / assets-debt / pnl-flip-loss)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** VZW MSW NZVL — KBO **0419.384.646**  
**recipient:** info@nzvl.be · Maldegemseweg 5, 9910 Aalter (HQ also Statieplein 12, 9300 Aalst)  
**sources:** [CW NL](https://www.companyweb.be/nl/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen) · [CW EN](https://www.companyweb.be/en/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen) · [CW FR](https://www.companyweb.be/fr/0419384646/vzw-medische-en-sociale-werken-van-het-neutraal-ziekenfonds-vlaanderen) · [KBO](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0419384646) · [NZVL contact](https://www.nzvl.be/contact)  
**tick:** 2071  
**confidence:** Medium (CW NL+EN+FR; assets/debt Unknown)

## Context
- YE **2025** (neerlegging **24.04.2026**): omzet **EUR435,516** JUMP +3.69%; pnl **LOSS EUR-304,338** FLIP vs YE2024 profit EUR10,918; equity **EUR3,081,864** DROP −8.99%; bruto **EUR-12,115** FLIP −103.97% vs YE2024 EUR305,484; FTE **0**; assets/debt **Unknown**.
- KBO: Actief VZW; **0 VE**; zetel Maldegemseweg 5 Aalter; afkorting VZW MSW NZVL; KBO email empty; parent contact info@nzvl.be.
- Preferred stall: AGB Bornem JR2024; FARO/AIESH/REW YE2024. Distinct from WZC Welvaart continuum.

## Brief
```text
[Naam] [Adres] [E-mail] [Datum]
Aan: VZW MSW NZVL / Neutraal Ziekenfonds Vlaanderen — Maldegemseweg 5, 9910 Aalter
info@nzvl.be
cc: RIZIV / Departement Zorg indien relevant
Betreft: Openbaarmaking NBB-jaarrekening 2025 VZW MSW NZVL + subsidiematrix (KBO 0419.384.646)
Geachte, op grond van het Bestuursdecreet / toepasselijke openbaarheidsregels (publiek gesubsidieerde mutualiteit/MSW-activiteit) vraag ik:
1. NBB PDF jaarrekening 2025 (neerlegging 24.04.2026).
2. Assets / schulden LT-ST / cash / balanstotaal.
3. Split RIZIV/mutualiteit-toelagen vs eigen inkomsten 2025.
4. Toelichting winstflip van EUR10.918 (YE2024) naar VERLIES EUR-304.338 (YE2025) en brutoflip naar EUR-12.115.
Periode 01.01.2025–31.12.2025. Ref: {GAP}
Met vriendelijke groeten, [Naam]
```
- [x] ready NOT sent (human-gated)
""",
    encoding="utf-8",
)
print("foi draft written")

do_not_redo = (
    "Do NOT redo VZW MSW NZVL, WZC Welvaart, Vulpia Vlaanderen, Compostela, Leiehome, Bejaardenzorg Zusters SV Deinze, Seniorencentrum OLV Bornem, "
    "Huize Sint-Jozef Ieper, WZC Sint-Antonius, OLV Wezembeek, WZC Ter Burg, WZC Christine, Home Vrijzicht, 't Pandje, "
    "Groep Zorg H. Familie, Huize Westerhauwe, Centrum Ganspoel, Seniorenzorg Lendelede, Walfergem, Ter Berk, Van Lierde, "
    "Hof ter Waarbeek, Huize Vincent, Ter Kimme, Integro, Curando, AGB Bornem, WZC De Verlosser Dilbeek, "
    "Zorggroep Zusters van Berlaar, Psychogeriatrisch Centrum, WZC De Linde Lievegem, Woonzorg Samen Ouder, "
    "C.W.Z.C. Zonhoven, Orelia Zorg, WZC Kanunnik Triest, OLVA Antwerpen, WZC OLV Roosdaal, WZC Sint-Bernardus Assenede, "
    "Cassiers WZC, WZC OLV Lourdes Kortenberg, WZC St Vincentius Antwerpen/Ekeren, WZC Sint-Jozef Rillaar, Karus, "
    "WZC De Foyer Gent, Sint-Jozef Rumst, Veilige Have, Witte Meren, Zusterhof, Werken Glorieux, Woonhaven Antwerpen, "
    "Always Home, Armonea, IPFBW, IGRETEC, Aquiris, SPGE, IRE*, FANC, SCK CEN, EURIDICE, Hydria, Vivaqua, Belgoprocess, "
    "Laborelec, CILE, NIRAS, Bel V, Dijk92, Synergrid, AIEG, Synatom, Atrias, RESA, Enodia, Fluxys*, ETB, Elia, BNO, SWDE, BRUGEL. "
    "Jessa/ZOL/Vesalius/SFZ/Noorderhart CW N/A omzet — take only if figures appear."
)

for x in qrows:
    if x.get("task_id") == "rq_2071":
        x["status"] = "done"
        x["updated_utc"] = UTC
        x["entity_id"] = ENTITY
        x["title"] = "leftover dual — VZW MSW NZVL YE2025 Medium"
        x["notes"] = (
            "tick2071 MSW NZVL Medium omzet JUMP 0.44m pnl FLIP LOSS 0.30m equity DROP 3.08m bruto FLIP -12k; "
            "FOI ready; AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2072; next every-10 2080"
        )
        x["instructions"] = (
            f"Completed leftover MSW NZVL YE2025 Medium CW; KBO 0419.384.646; omzet JUMP {OMZET} pnl FLIP LOSS {PNL} "
            f"equity DROP {EQUITY} bruto FLIP {BRUTO} FTE {FTE}; FOI {GAP}"
        )
        x["blocked_gap_id"] = GAP

if not any(x.get("task_id") == "rq_2072" for x in qrows):
    qrows.append(
        {
            **{k: "" for k in qfields},
            "task_id": "rq_2072",
            "title": "leftover dual hole-fill after MSW NZVL — prefer AGB/FARO-YE2025/AIESH-REW/unused WZC",
            "sprint": "hole_fill",
            "priority": "8",
            "status": "open",
            "hierarchy_target": "L5",
            "entity_id": "",
            "instructions": (
                "Tick 2071 after MSW NZVL YE2025 Medium. Prefer leftover AGB/APB if JR2025 PDF live, else FARO if TRUE NBB YE2025, "
                "else AIESH/REW if YE2025, else unused water/DSO/IGS/HVZ/energy/hospital/WZC/psych. " + do_not_redo
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "spawned after tick2071 MSW NZVL; next every-10 2080",
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
        "last_unit_id": "rq_2071",
        "ticks_completed": "2071",
        "paused": "no",
        "notes": (
            "tick2071 leftover MSW NZVL 0419.384.646 Medium CW (omzet JUMP 0.44m pnl FLIP LOSS 0.30m equity DROP 3.08m "
            "bruto FLIP -12k FTE 0; assets/debt Unknown); AGB Bornem JR2024; FARO/AIESH/REW YE2024; next rq_2072; "
            "next every-10 2080; continuous hole_fill"
        ),
    }
)
save("docs/doge/data/loop_state.csv", lsrows, lsfields)
print("state ok")

log_path = Path("docs/doge/loop_log.md")
log_path.write_text(
    log_path.read_text(encoding="utf-8")
    + f"""

## Tick 2071 - 2026-08-24T22:50:00Z - rq_2071 MSW NZVL (omzet JUMP 0.44m / pnl FLIP LOSS 0.30m / Medium)

- Unit: **rq_2071** leftover dual after **rq_2070 WZC Welvaart**. Prefer NON-stall live: AGB Bornem still **JR2024-only**; FARO still **YE2024**; AIESH still **YE2024**; REW still **YE2024**. Took deferred leftover **VZW MSW NZVL** YE2025 (KBO **0419.384.646**; Maldegemseweg 5 Aalter; Oost-Vlaanderen **VZW** medical-social works of Neutraal Ziekenfonds / **0 VE**). Do not redo Welvaart/Vulpia/Compostela/Leiehome/Zusters SV Deinze/OLV Bornem/Huize Sint-Jozef Ieper/Sint-Antonius/OLV Wezembeek/Ter Burg/Christine/Vrijzicht/'t Pandje/H.Familie/Westerhauwe/Ganspoel/Lendelede/Walfergem/Ter Berk/Van Lierde/Hof ter Waarbeek/Huize Vincent/Ter Kimme/Integro/Curando/AGB Bornem/Armonea/Always Home.
- Found: Companyweb NL+EN+FR YE2025 - omzet **EUR435,516** JUMP +3.69%; pnl **LOSS EUR-304,338** FLIP vs YE2024 profit EUR10,918; equity **EUR3,081,864** DROP -8.99%; bruto **EUR-12,115** FLIP -103.97% vs YE2024 EUR305,484; FTE **0**; neerlegging **24.04.2026**. Assets/debt Unknown. Medium confidence. Strong KBO Actief VZW 0 VE; email info@nzvl.be (parent NZVL contact).
- Wrote: sources (+5); budgets (+5); commitments (+1); leaderboard (+1 pi {PI}); entities (+1 {ENTITY}); foi + draft {GAP}; rq_2071=done + rq_2072 open; loop_state ticks=2071; raw under docs/doge/data/raw/tick2071/.
- FOI: **ready not sent** (human-gated; info@nzvl.be).
- NOT every-10 (**next every-10 is 2080**). Next: rq_2072 (AGB/FARO-if-YE2025 / AIESH-REW / unused DSO-IGS-HVZ-WZC-psych).
""",
    encoding="utf-8",
)
print("log ok")
print("DONE tick2071")
