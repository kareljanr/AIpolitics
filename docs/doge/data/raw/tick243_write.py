# tick 243: FWB Maisons de Justice DO18 + VL Justitiehuizen federal dotatie dual
import csv
import json
import os
from pathlib import Path

base = r"C:\Users\karel\dev\AIpolitics\docs\doge\data"
src_fwb = "src_fwb_budget_do18_mdj_2026"
src_vl = "src_vl_bbt_fb_bo2026_justitiehuizen_dotatie"
utc = "2026-07-29T08:30:00Z"
gap_mdj = "gap_fwb_mdj_partner_l5"
gap_vl = "gap_vl_justitiehuizen_spend"

# FWB DO18 kEUR -> EUR (table en milliers d'euros)
do18_eng_2026 = 28_362_000
do18_liq_2026 = 30_124_000
do18_eng_2025 = 28_700_000
do18_liq_2025 = 30_276_000

prog0_eng = 575_000
prog0_liq = 837_000
prog1_eng = 3_433_000  # Centre surveillance electronique credits totaux
prog1_liq = 4_958_000
prog3_eng = 24_354_000  # Partenariats
prog3_liq = 24_292_000
prog4_eng = 0
prog4_liq = 37_000

# Act 31 partners (eng/liq)
aide_jur = (1_244_000, 1_241_000)
aide_soc = (4_180_000, 4_169_000)
aide_psy = (5_668_000, 5_653_000)
aide_lien = (6_851_000, 6_832_000)
aide_comm = (1_734_000, 1_730_000)
aide_accomp = (3_792_000, 3_782_000)
act31_eng = 23_469_000
act31_liq = 23_407_000

# Electronic monitoring aid
se_aide_detenus = 3_203_000
se_fonctionnement_liq = 1_655_000  # 130 eng / 1655 liq goods

# Particular projects
projets_part = 605_000
urgences = 280_000

# Infra shared SAJ-SPJ + MDJ (DO15 act14) — not pure MDJ
infra_saj_mdj_2026 = 10_595_000
infra_saj_mdj_2025 = 9_983_000

# VL federal receipt BFW art 47/10 (kEUR in BBT)
vl_dot_ba2025 = 88_767_000
vl_dot_bo2026 = 90_357_000
vl_dot_delta = 1_590_000

# Partnership L5 sample sum (eng 2026)
partner_l5_eng = act31_eng + projets_part + urgences

with open(os.path.join(base, "sources.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            src_fwb,
            "FWB budget initial 2026 DO18 Maisons de Justice table eng/liq",
            "docs/doge/data/raw/fwb_budget_dep_2026.pdf",
            "Federation Wallonie-Bruxelles Budget",
            "2026-07-29",
            "budget_decree",
            "DO18 eng 28.362m liq 30.124m; partenariats 24.35m; SE 3.43/4.96m; dual VL Justitiehuizen; tick243",
        ]
    )
    w.writerow(
        [
            src_vl,
            "BBT Financien en Begroting BO2026 Dotatie Justitiehuizen art 47/10 BFW",
            "https://themis-test.vlaanderen.be/files/642f7b00-b09e-11f0-9b44-3797f8128cc9/download",
            "Vlaamse Regering / Departement FB BBT BO2026",
            "2026-07-29",
            "budget_decree",
            "Federal receipt VL justitiehuizen BA2025 88.767m BO2026 90.357m kEUR table; tick243 dual FWB MDJ",
        ]
    )

with open(os.path.join(base, "entities.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "fwb_maisons_justice",
            "FWB Maisons de Justice",
            "Maisons de Justice de la Federation Wallonie-Bruxelles",
            "FWB community justice houses (sentence execution outside prison)",
            "agency",
            "fwb_gov",
            "fr",
            "https://www.maisonsdejustice.be",
            "",
            "",
            "DO18 total liq ~30.1m 2026; dual VL Justitiehuizen; tick243",
        ]
    )
    w.writerow(
        [
            "vl_justitiehuizen",
            "Vlaamse Justitiehuizen (AJH)",
            "Maisons de Justice flamandes",
            "Flemish justice houses under Agentschap Justitie en Handhaving",
            "agency",
            "vlaanderen_gov",
            "nl",
            "https://www.vlaanderen.be/justitie-en-handhaving",
            "openbaarheid@vlaanderen.be",
            "",
            "BFW federal dotatie receipt 90.357m BO2026; full AJH spend residual FOI; tick243",
        ]
    )

rows_b = [
    (
        "bud_fwb_do18_eng_2026",
        "fwb_maisons_justice",
        2026,
        do18_eng_2026,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "DO18 total eng 28.362m BI2026",
    ),
    (
        "bud_fwb_do18_liq_2026",
        "fwb_maisons_justice",
        2026,
        do18_liq_2026,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "DO18 total liq 30.124m BI2026",
    ),
    (
        "bud_fwb_do18_eng_2025",
        "fwb_maisons_justice",
        2025,
        do18_eng_2025,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "DO18 eng 28.700m BI2025 compare",
    ),
    (
        "bud_fwb_do18_liq_2025",
        "fwb_maisons_justice",
        2025,
        do18_liq_2025,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "DO18 liq 30.276m BI2025 compare",
    ),
    (
        "bud_fwb_mdj_partenariats_2026",
        "fwb_maisons_justice",
        2026,
        prog3_eng,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Prog3 Partenariats eng 24.354 / liq 24.292m (~81pct DO18 eng)",
    ),
    (
        "bud_fwb_mdj_act31_agrege_2026",
        "fwb_maisons_justice",
        2026,
        act31_eng,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Act31 decret 2016 agrege services eng 23.469 / liq 23.407m",
    ),
    (
        "bud_fwb_mdj_aide_lien_2026",
        "fwb_maisons_justice",
        2026,
        aide_lien[0],
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Subs services agrege aide au lien 6.851m eng (largest partner line)",
    ),
    (
        "bud_fwb_mdj_aide_psy_2026",
        "fwb_maisons_justice",
        2026,
        aide_psy[0],
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Subs services agrege aide psychologique 5.668m eng",
    ),
    (
        "bud_fwb_mdj_aide_sociale_2026",
        "fwb_maisons_justice",
        2026,
        aide_soc[0],
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Subs services agrege aide sociale 4.180m eng",
    ),
    (
        "bud_fwb_mdj_se_2026",
        "fwb_maisons_justice",
        2026,
        prog1_eng,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Prog1 Centre surveillance electronique eng 3.433 / liq 4.958m",
    ),
    (
        "bud_fwb_mdj_se_aide_detenus_2026",
        "fwb_maisons_justice",
        2026,
        se_aide_detenus,
        "",
        "",
        "budgeted",
        src_fwb,
        "strong",
        "Aide financiere detenus sans moyens sous SE 3.203m",
    ),
    (
        "bud_fwb_infra_saj_mdj_2026",
        "fwb_maisons_justice",
        2026,
        infra_saj_mdj_2026,
        "",
        "",
        "budgeted",
        src_fwb,
        "medium",
        "DO15 act14 infra SAJ-SPJ + Maisons de justice 10.595m (shared not pure MDJ)",
    ),
    (
        "bud_vl_justitiehuizen_dotatie_rec_2026",
        "vl_justitiehuizen",
        2026,
        vl_dot_bo2026,
        "",
        "",
        "budgeted",
        src_vl,
        "strong",
        "Federal BFW art47/10 receipt Dotatie Justitiehuizen BO2026 90.357m (not full AJH spend)",
    ),
    (
        "bud_vl_justitiehuizen_dotatie_rec_2025",
        "vl_justitiehuizen",
        2025,
        vl_dot_ba2025,
        "",
        "",
        "budgeted",
        src_vl,
        "strong",
        "BA2025 Dotatie Justitiehuizen 88.767m receipt compare",
    ),
]
with open(os.path.join(base, "budgets.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    for row in rows_b:
        w.writerow(list(row))

cash = json.dumps(
    {
        "do18_eng": do18_eng_2026,
        "do18_liq": do18_liq_2026,
        "prog0_subsistance": {"eng": prog0_eng, "liq": prog0_liq},
        "prog1_surveillance_electronique": {"eng": prog1_eng, "liq": prog1_liq},
        "prog3_partenariats": {"eng": prog3_eng, "liq": prog3_liq},
        "act31_agrege": {"eng": act31_eng, "liq": act31_liq},
        "lines_eng": {
            "aide_lien": aide_lien[0],
            "aide_psy": aide_psy[0],
            "aide_sociale": aide_soc[0],
            "accompagnement": aide_accomp[0],
            "communication": aide_comm[0],
            "aide_juridique": aide_jur[0],
            "projets_particuliers": projets_part,
            "urgences_collectives": urgences,
            "se_aide_detenus": se_aide_detenus,
        },
        "vl_dotatie_justitiehuizen_rec": vl_dot_bo2026,
        "dual_note": "FWB DO18 ~30m programme credits (personnel may be outside DO18); VL federal receipt 90.4m; not additive; VL full spend FOI",
    }
)

with open(os.path.join(base, "commitments.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "cmt_fwb_maisons_justice_2026",
            "FWB Maisons de Justice DO18 package 2026 dual VL Justitiehuizen",
            "fwb_maisons_justice",
            "Justiciables community sentence execution / partner ASBL FR community",
            "FWB budget initial 2026 DO18",
            "2025-10-10",
            "2026",
            "2026",
            do18_liq_2026,
            cash,
            0,
            "active",
            "docs/doge/data/raw/fwb_budget_dep_2026.pdf",
            "Community justice houses FWB",
            "Named partner ASBL inside 23.5m act31; dual VL AJH full spend vs 90.4m federal receipt",
            src_fwb,
            "strong",
            "FWB>Maisons_de_Justice",
            "tick243 dual VL Justitiehuizen receipt 90.4m",
        ]
    )
    w.writerow(
        [
            "cmt_vl_justitiehuizen_dotatie_2026",
            "VL federal Dotatie Justitiehuizen BFW 47/10 receipt BO2026",
            "vl_justitiehuizen",
            "Vlaamse Gemeenschap justitiehuizen financing receipt",
            "BFW art 47/10; BBT FB BO2026",
            "2025-10-24",
            "2026",
            "2026",
            vl_dot_bo2026,
            json.dumps(
                {
                    "ba_2025": vl_dot_ba2025,
                    "bo_2026": vl_dot_bo2026,
                    "delta": vl_dot_delta,
                    "note": "Receipt only; VL tops up per beleidsnota; full AJH VEK residual FOI",
                }
            ),
            0,
            "active",
            "https://themis-test.vlaanderen.be/files/642f7b00-b09e-11f0-9b44-3797f8128cc9/download",
            "Federal financing of VL justice houses",
            "Publish AJH full spend + top-up vs federal receipt series",
            src_vl,
            "strong",
            "Vlaanderen>Justitie_Handhaving>Justitiehuizen",
            "tick243 dual FWB MDJ 30m",
        ]
    )

with open(os.path.join(base, "leaderboard.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            "lb_fwb_mdj_30m",
            "FWB Maisons de Justice DO18 30.1m liq 2026",
            "FWB",
            "ops",
            "FWB>Maisons_de_Justice",
            do18_liq_2026,
            do18_liq_2026,
            "Strong DO18 liq 30.124m; partenariats 24.3m 81pct eng; dual VL federal receipt 90.4m different metric",
            "strong",
            src_fwb,
            "Justiciables FR community",
            "Community sentence execution + victim support",
            "Core justice function not pure waste; dual VL; partner ASBL L5 residual; personnel likely outside DO18",
            3,
            6.5,
            4,
            5.15,
            "Open named partner matrix act31 23.5m; dual unit-cost VL",
            "seed",
            "",
            "tick243",
        ]
    )
    w.writerow(
        [
            "lb_fwb_mdj_partenariats_24m",
            "FWB MDJ partenariats agrege 24.3m 2026",
            "FWB",
            "ops",
            "FWB>Maisons_de_Justice>partenariats",
            prog3_eng,
            prog3_eng,
            "Strong prog3 eng 24.354m; act31 23.469m six service classes; named ASBL residual",
            "strong",
            src_fwb,
            "Agreed partner services",
            "Social/psych/legal aid to justiciables via partners",
            "Category totals public; end-receiver names residual",
            3,
            7.0,
            4,
            5.3,
            "Publish top partner ASBL with EUR",
            "seed",
            "",
            "tick243",
        ]
    )
    w.writerow(
        [
            "lb_justice_houses_dual_fwb_vl",
            "Justice houses dual FWB MDJ 30m vs VL federal receipt 90m",
            "Belgium",
            "ops",
            "BE>Justice_houses>dual_FWB_VL",
            0,
            0,
            "Strong dual: FWB DO18 30.1m liq vs VL BFW justitiehuizen receipt 90.4m BO2026; metrics not comparable (receipt vs programme; personnel scope); do not sum",
            "strong",
            src_fwb,
            "Justiciables BE",
            "Community dual justice-house systems post-6th reform",
            "Institutional dual + financing asymmetry; VL full spend FOI",
            4,
            7.0,
            5,
            5.6,
            "Map dual full spend + unit cost same mandate class",
            "seed",
            "",
            "tick243 dual not additive",
        ]
    )

with open(os.path.join(base, "foi_queue.csv"), "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(
        [
            gap_mdj,
            "FWB>Maisons_de_Justice>partenaires_L5",
            "fwb_maisons_justice",
            "Named top partner ASBL with EUR 2024-2026 inside act31 23.5m (6 service classes) + projets 0.6m",
            "Category totals strong DO18; end-receiver names residual for dual VL map",
            6,
            "FWB Maisons de Justice / publicite de l administration",
            "",
            "https://www.maisonsdejustice.be",
            f"docs/doge/foi/drafts/{gap_mdj}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_fwb_maisons_justice_2026",
            "lb_fwb_mdj_partenariats_24m|lb_fwb_mdj_30m",
            utc,
            utc,
            "tick243 draft ready human send",
        ]
    )
    w.writerow(
        [
            gap_vl,
            "Vlaanderen>Justitie_Handhaving>Justitiehuizen_spend",
            "vl_justitiehuizen",
            "Full AJH / justitiehuizen VEK-VAK spend 2024-2026 vs federal BFW receipt 90.357m; VL top-up amount; named partner subsidies if any",
            "Receipt public; full spend and top-up opaque; dual FWB DO18 30m incomplete without VL spend side",
            6,
            "Vlaamse overheid Team Openbaarheid / Agentschap Justitie en Handhaving",
            "openbaarheid@vlaanderen.be",
            "Havenlaan 88 bus 20 1000 Brussel",
            f"docs/doge/foi/drafts/{gap_vl}.md",
            "ready",
            "2026-07-29",
            "",
            "",
            "",
            "",
            "cmt_vl_justitiehuizen_dotatie_2026",
            "lb_justice_houses_dual_fwb_vl",
            utc,
            utc,
            "tick243 draft ready human send",
        ]
    )

# FOI drafts
drafts = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\foi\drafts")
(drafts / f"{gap_mdj}.md").write_text(
    f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{gap_mdj}`  
**Status:** ready (human send only)  
**Linked:** rq_234 · cmt_fwb_maisons_justice_2026 · lb_fwb_mdj_partenariats_24m

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Maisons de Justice / Administration FWB (publicité de l'administration)
     https://www.maisonsdejustice.be

Betreft: Verzoek om openbaarmaking — Maisons de Justice partenaires L5 2024-2026

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp

1. Liste nominative (ou export machine-readable) des services agréés
   bénéficiaires avec montants 2024-2026 pour au minimum les classes:
   - aide au lien (~6,851 mEUR eng 2026)
   - aide psychologique (~5,668 mEUR)
   - aide sociale (~4,180 mEUR)
   - accompagnement (~3,792 mEUR)
   - aide à la communication (~1,734 mEUR)
   - aide juridique de première ligne (~1,244 mEUR)
   - projets particuliers d'opérateurs (~0,605 mEUR)
2. Réconciliation avec les totaux DO18 BI2026 (eng 28,362 / liq 30,124 mEUR)
   et activité 31 (eng 23,469 / liq 23,407 mEUR).
3. Si disponible: effectifs / mandats gérés par les Maisons de Justice 2024-2025
   (comparabilité duale justitiehuizen Flandre).

Période: 2024-01-01 à la date la plus récente.

### 2. Context

Les totaux par catégorie de service sont publics (budget FWB DO18). Les
end-receivers nominatifs manquent pour la cartographie duale avec les
justitiehuizen flamands (dotatie fédérale BFW 90,4 mEUR reçu VL 2026).

Hiérarchie: FWB > Maisons de Justice > partenaires agréés.

### 3. Vorm

Kopie digitale (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {gap_mdj}

Met vriendelijke groet,
[Naam]
```

---

## Checklist vóór `ready`

- [x] Juiste instelling (FWB Maisons de Justice)
- [x] Concrete documenten
- [x] Periode en bedragen
- [x] Meerjarigheid
- [ ] Contactgegevens verzoeker (human)
- [x] `foi_queue.csv` bijgewerkt
""",
    encoding="utf-8",
)

(drafts / f"{gap_vl}.md").write_text(
    f"""# Sjabloon — verzoek openbaarheid van bestuur

**gap_id:** `{gap_vl}`  
**Status:** ready (human send only)  
**Linked:** rq_234 · cmt_vl_justitiehuizen_dotatie_2026 · lb_justice_houses_dual_fwb_vl

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Vlaamse overheid
     Team Openbaarheid van Bestuur
     openbaarheid@vlaanderen.be
     Havenlaan 88 bus 20, 1000 Brussel
     (Agentschap Justitie en Handhaving / justitiehuizen)

Betreft: Verzoek om openbaarmaking — Justitiehuizen / AJH uitgaven 2024-2026

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Bestuursdecreet e.a.) dien ik hierbij een verzoek in tot openbaarmaking van:

### 1. Voorwerp van het verzoek

1. Volledige VEK/VAK-uitgaven Agentschap Justitie en Handhaving of
   programma justitiehuizen 2024-2026 (begrotingsartikelen + realisatie).
2. Aansluiting met de federale Dotatie Justitiehuizen (BFW art. 47/10):
   BA2025 88,767 mEUR / BO2026 90,357 mEUR ontvangst — gevraagd:
   welk deel dekt de justitiehuizen-exploitatie en welk bedrag is Vlaamse
   bijpassing (top-up).
3. Lijst van derden/subsidies (werkstrafplaatsen, partnerorganisaties)
   met bedragen 2024-2026 indien op de justitiehuizen-begroting.
4. Indien beschikbaar: caseload / mandaten 2024-2025 (dual vergelijking
   FWB Maisons de Justice DO18 ~30 mEUR).

Periode: 2024-01-01 tot de meest recente stand.

### 2. Context (waarom)

De federale ontvangstdotatie is publiek (BBT FB BO2026). De volledige
uitgavenzijde en bijpassing zijn nodig voor de duale kaart met FWB
Maisons de Justice (DO18 liq 30,1 mEUR 2026). Beleidsnota Justitie wijst
op structurele bijpassing door Vlaanderen.

Hiërarchie: Vlaanderen > Justitie en Handhaving > Justitiehuizen.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].

### 4. Identiteit

Naam: […]
Dossierreferentie intern: {gap_vl}

Met vriendelijke groet,
[Naam]
```

---

## Checklist vóór `ready`

- [x] Juiste instelling (VL openbaarheid / AJH)
- [x] Concrete documenten
- [x] Periode en bedragen
- [x] Meerjarigheid
- [ ] Contactgegevens verzoeker (human)
- [x] `foi_queue.csv` bijgewerkt
""",
    encoding="utf-8",
)

rows = []
with open(os.path.join(base, "research_queue.csv"), encoding="utf-8-sig", newline="") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    for row in r:
        if row["task_id"] == "rq_234":
            row["status"] = "done"
            row["updated_utc"] = utc
            row["blocked_gap_id"] = f"{gap_mdj}|{gap_vl}"
            row["notes"] = (
                "tick243: FWB MDJ DO18 liq 30.1m partenariats 24.3m; VL federal justitiehuizen receipt 90.4m; "
                "FOI partner L5 + VL full spend ready; spawn rq_235"
            )
        rows.append(row)

rows.append(
    {
        "task_id": "rq_235",
        "title": "Continuous FOI-adjacent public hole-fill batch",
        "sprint": "continuous",
        "priority": "5",
        "status": "open",
        "hierarchy_target": "L5",
        "entity_id": "gg_belgium",
        "instructions": (
            "Prefer public primary fills (Mons ASBL L5 if public; FPS taxex utilities SOE; "
            "VL AJH full spend if public PDF; DG/COCOM residual dual justice; other FOI-adjacent)."
        ),
        "blocked_gap_id": "",
        "created_utc": utc,
        "updated_utc": "",
        "notes": "Spawned tick243 after FWB MDJ 30m dual VL receipt 90m; rq_116 SWA deferred",
    }
)

with open(os.path.join(base, "research_queue.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

with open(os.path.join(base, "loop_state.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(
        [
            "state_id",
            "mode",
            "current_sprint",
            "last_tick_utc",
            "last_unit_id",
            "ticks_completed",
            "paused",
            "notes",
        ]
    )
    w.writerow(
        [
            "main",
            "continuous",
            "hole_fill",
            utc,
            "rq_234",
            243,
            "no",
            "Scheduler 60s. Next prio5 rq_235; rq_116 SWA deferred. FOI ready human send. tick243 FWB MDJ 30.1m dual VL receipt 90.4m.",
        ]
    )

# Append loop log
log_path = Path(r"C:\Users\karel\dev\AIpolitics\docs\doge\loop_log.md")
entry = f"""
### 2026-07-29T08:30:00Z — tick 243
- Unit: rq_234 (Maisons de Justice deepen + VL Justitiehuizen dual)
- Found (strong primary):
  - **FWB DO18 Maisons de Justice BI2026** (`fwb_budget_dep_2026.pdf`): **eng €28.362m / liq €30.124m** (2025 eng 28.700 / liq 30.276).
  - Split 2026: Prog0 subsistance 0.575/0.837m; **Prog1 surveillance électronique 3.433/4.958m** (aide détenus SE **3.203m**); **Prog3 partenariats eng 24.354 / liq 24.292m** (~81% eng); Prog4 0/0.037m.
  - Act31 agréés (eng): aide au lien **6.851m**, psy **5.668m**, sociale **4.180m**, accompagnement **3.792m**, communication **1.734m**, juridique **1.244m** (sum eng **23.469m**); projets particuliers **0.605m**; urgences **0.280m**.
  - Related infra DO15 act14 SAJ-SPJ+MDJ **10.595m** (shared; medium).
  - **VL dual receipt** BBT FB BO2026: Dotatie Justitiehuizen art. 47/10 BFW **BA2025 €88.767m → BO2026 €90.357m** (+1.590m). Receipt only — full AJH spend/top-up residual (beleidsnota: VL tops up).
  - Dual note: **not additive** (programme credits vs federal receipt; FWB personnel likely outside DO18).
- Wrote: sources (+2); entities fwb_maisons_justice + vl_justitiehuizen; budgets (+14); commitments (+2); leaderboard (+3); foi_queue ready gap_fwb_mdj_partner_l5 + gap_vl_justitiehuizen_spend; drafts; rq_234=done; spawn rq_235; loop_state ticks=243
- FOI opened: gap_fwb_mdj_partner_l5, gap_vl_justitiehuizen_spend (ready, human send)
- Next: rq_235 hole-fill; rq_116 SWA deferred Oct–Dec 2026
"""
with open(log_path, "a", encoding="utf-8") as f:
    f.write(entry)

print(
    "tick243 OK do18_liq",
    do18_liq_2026,
    "partenariats",
    prog3_eng,
    "vl_dot",
    vl_dot_bo2026,
    "partner_l5_eng",
    partner_l5_eng,
)
