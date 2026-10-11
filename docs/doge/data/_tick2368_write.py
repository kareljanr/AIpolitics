#!/usr/bin/env python3
"""Surgical tick 2368 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_digor"
SRC_PDF = "src_digor_jr2025_nbb_pdf_2368"
SRC_KBO = "src_digor_kbo_2368"
SRC_SBM = "src_digor_sbm_2368"
SRC_SITE = "src_digor_site_2368"
COMM = "comm_digor_jr2025_statutory_bruto_0_76m_pnl_jump_cash_1_72m"
LB = "lb_digor_bruto_0_76m_pnl_jump_cash_1_72m_jr2025"
GAP = "gap_digor_vl_matrix_bruto_0_76m_omzet_empty_cash_1_72m_jump_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

# --- FOI draft ---
foi = f"""# FOI draft — DiGOR vzw (bruto 0.76m / omzet+73 empty / cash 1.72m JUMP / pnl JUMP)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** DIGOR Netwerk voor inclusieve zorg-en welzijnsorganisaties vzw (DiGOR / Dienstencentrum voor Gehandicaptenzorg Onderwijs en Revalidatie) — KBO **0870.833.435** (Actief; 1 VE **2.160.628.775** naam V.Z.W. Dienstencentrum voor Gehandicaptenzorg, Onderwijs en Revalidatie; zetel + VE Kloosterstraat 6, 9031 Gent/Drongen; RSZ2025 **94.992** verenigingen en bewegingen voor volwassenen; voorzitter Jacques Adriaens; dagelijks bestuur o.a. Stefaan Singelée)  
**recipient:** DiGOR vzw / Jacques Adriaens (voorzitter RvB) — dienstencentrum@digor.be — Kloosterstraat 6, 9031 Drongen  
**sources:** official NBB WVV VKT-VZW PDF deposit **2026-00205516** (neerlegging **26.06.2026**; CDN Last-Modified **10.07.2026**; AV **05.06.2026**; **48559** bytes / **12p**; model **VKT-VZW** 26.0.15 m04-f); [official CDN](http://cdn.staatsbladmonitor.be/2026pdf/2026-00205516.pdf); [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0870833435); [KBO 0870.833.435](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0870833435); [site](https://www.digor.be/)  
**tick:** 2368 (NOT every-10; next every-10 is **2370**)

## Context (primary official NBB VKT-VZW JR2025)

- Leftover dual public **koepel-/dienstencentrum-VZW** (gehandicaptenzorg / onderwijs / revalidatie netwerk) of mined **Sig@2367** + **CAR Wegwijs@2366** + **TKDV Het Veer@2365** + **Kapelhof@2364** + **De Steijger@2363** + **De Steijgertjes@2362** + **De Elfjes@2361** + **Noordhoek@2360** + **Oostakker@2359** + **Stappie@2358** + **'t Vlot@2357** + **CAR Het Veer@2356** + **Ter Kouter@2355** — same statutory seat Kloosterstraat 6 Drongen + shared board (Singelée dagelijks bestuur; DCGZ 0411.917.131 empty-shell bestuurder). Prefix `vzw_digor` unused. Parent `sec_flanders`. Confirmed leftover public (dienstencentrum/koepel van autonome publieke VZW-leden; same-zetel public CAR cluster) not private clinic.
- Stalls this tick: AGB Bornem still **JR2024**; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). First unused leftover same-zetel with live 2026pdf after Sig: DIGOR (deposit HEAD 200 / 48559 B).
- EUR **strong** from official PDF (not Companyweb / not SBM table): omzet 70 **empty**; code 73 **empty**; bruto **764649** JUMP +12.83% (VKT envelope); pnl **162203** JUMP +72.67%; equity **2545841** JUMP +6.81%; assets **2633598** JUMP +6.59%; debt **87757** JUMP +0.76%; FTE **7.1** FLAT; kapitaalsubsidies **empty**; destin 691 **empty**; bestemde fondsen 13 **empty**; cash **1721124** JUMP +45.30% (~225% of bruto); 350k LT receivable YE2024 collected (code 29 empty). Strong KBO + Strong PDF.
- Next leftover same-zetel / cluster if live 2026pdf: Mozaiek **0415.272.935** deposit **2026-00206415** (HEAD 200 / 71192 B at 2367). DCGZ 0411.917.131 empty shell. Steunfonds Martens-Sotteau **0476.428.861** absorbed into empty DCGZ (2022).

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: DiGOR vzw
t.a.v. de dienst openbaarheid van bestuur / Jacques Adriaens
(voorzitter Raad van Bestuur)
Kloosterstraat 6
9031 Drongen
dienstencentrum@digor.be
https://www.digor.be/

Betreft: Verzoek om openbaarmaking van bestuursdocumenten —
JR2025 DiGOR vzw (KBO 0870.833.435)
brutomarge 764.649 (omzet 70 leeg / code 73 leeg)
/ winst 162.203 (JUMP +72,67%)
/ liquide middelen 1.721.124 (JUMP +45,30%)
/ FTE 7,1

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur)
dien ik hierbij een verzoek in tot openbaarmaking / inzage /
afschrift van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. De volledige jaarrekening 2025 (NBB VKT-VZW deposit
   2026-00205516) plus het activiteitenverslag 2025 en
   het verslag van het bestuursorgaan aan de AV van
   5 juni 2026.
2. De uitsplitsing van brutomarge code 9900 EUR 764.649
   (was 677.667; JUMP +12,83%) — waarom omzet code 70
   én lidgeld/schenkingen/subsidies code 73 leeg zijn
   terwijl de brutomarge 0,76 miljoen bedraagt.
   Uitsplitsing lidgelden leden-VZW / adviesdiensten /
   subsidies (Vlaanderen / andere) / overige.
3. De toelichting bij liquide middelen code 54/58
   EUR 1.721.124 (was 1.184.554; JUMP +45,30% — circa
   225% van de brutomarge) — treasurybeleid / geoormerkte
   publieke middelen / relatie tot de verdwenen
   vordering op meer dan één jaar code 29 EUR 350.000
   (YE2024; YE2025 leeg).
4. De toelichting bij eigen vermogen code 10/15
   EUR 2.545.841 (was 2.383.638; JUMP +6,81%) —
   volledig overgedragen winst code 14; waarom bestemde
   fondsen code 13 én kapitaalsubsidies code 15 én
   destin 691 leeg zijn.
5. De toelichting bij materiële vaste activa
   (terreinen en gebouwen code 22 EUR 773.675) en
   aanschaffingen 2025 EUR 28.612.
6. De relatie duale / koepel-rechtspersonen op dezelfde
   statutaire zetel Drongen (Kloosterstraat 6, zelfde
   adres als CAR Ter Kouter, CAR Het Veer, CAR 't Vlot,
   CAR Stappie, CAR Oostakker, CAR Noordhoek, CAR De
   Steijger, CAR Kapelhof, CAR Wegwijs, KDV De Elfjes,
   KDV De Steijgertjes, TKDV Het Veer, Sig) —
   ledenlijst, lidgelden, interne rekeningen, subsidies,
   gedeelde raad, rol van bestuurder DCGZ 0411.917.131.
7. Het personeelsbestand 2025: 7,1 VTE gemiddeld
   (ongewijzigd) versus bezoldigingen code 62
   EUR 543.087 — uitsplitsing per functie.
8. De notulen van de algemene vergadering van
   5 juni 2026 (niet-persoonsgebonden delen).
9. Eventuele Vlaamse of lokale subsidies 2025
   (Departement Zorg / Onderwijs) — bedrag / looptijd /
   KPI's. Toelichting waarom die niet onder code 73
   verschijnen.

Periode: boekjaar 01.01.2025–31.12.2025 en lopende
meerjarige verbintenissen.

### 2. Context (waarom)

Dit verzoek kadert in onderzoek naar overheidsuitgaven
en subsidies (transparantie van publieke middelen).
Hiërarchisch pad (intern):
Vlaanderen > Oost-Vlaanderen > Drongen >
DiGOR vzw > JR2025 statutory L5.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail.
Indien weigering of gedeeltelijke openbaarmaking:
gemotiveerde beslissing met rechtsgrond en beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern:
{GAP}

Met vriendelijke groet,
[Naam]
```

## Checklist vóór `ready`

- [x] Juiste instelling (DiGOR vzw / voorzitter RvB)
- [x] Concrete documenten (VL-matrix, omzet+73 empty, cash 1.72m JUMP, 350k receivable)
- [x] Periode en bedragen gevraagd (PDF-sourced)
- [x] Meerjarigheid expliciet gevraagd
- [ ] Contactgegevens verzoeker ingevuld (human)
- [x] `foi_queue.csv` bijgewerkt
- [x] ready NOT sent (human-gated)
"""
draft_path = ROOT / DRAFT
draft_path.write_text(foi, encoding="utf-8")
print("wrote", draft_path, draft_path.stat().st_size)

def append_lines(path: Path, lines):
    raw = path.read_bytes()
    if not raw.endswith(b"\n"):
        raise SystemExit(f"{path} does not end with LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"):
                line = line + "\n"
            f.write(line.encode("utf-8"))
    print("appended", len(lines), "->", path.name)

# sources (+4)
append_lines(DATA / "sources.csv", [
    f"{SRC_PDF},NBB WVV VKT-VZW jaarrekening 2025 DiGOR vzw deposit 2026-00205516,http://cdn.staatsbladmonitor.be/2026pdf/2026-00205516.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2368; official PDF 48559 bytes 12p VKT-VZW 26.0.15 m04-f; neerlegging 26.06.2026; AV 05.06.2026; YE 01.01.2025-31.12.2025; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO DiGOR vzw 0870.833.435,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0870833435,KBO Public Search FOD Economie,{DAY},official_register,tick2368; Actief; 1 VE 2.160.628.775 naam Dienstencentrum voor Gehandicaptenzorg Onderwijs en Revalidatie; zetel+VE Kloosterstraat 6 9031 Gent/Drongen; RSZ2025 94.992; voorzitter Adriaens Jacques; dagelijks bestuur Singelee Stefaan; bestuurder DCGZ 0411.917.131",
    f"{SRC_SBM},Staatsbladmonitor fiche DiGOR vzw 0870833435 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0870833435,Staatsbladmonitor,{DAY},official_register,tick2368; deposit-id 2026-00205516 and CDN Last-Modified 2026-07-10; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},DiGOR vzw FOI contact / koepel dienstencentrum Drongen,https://www.digor.be/,DiGOR vzw,{DAY},foi_contact,tick2368; zetel Kloosterstraat 6 9031 Drongen; FOI dienstencentrum@digor.be; leftover same-zetel Ter Kouter/CAR cluster koepel",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},DiGOR VZW (Drongen / koepel dienstencentrum),DiGOR ASBL (Drongen / federation centre de services),DiGOR VZW (Drongen / disability-rehab-education network hub),parastatal,sec_flanders,nl,https://www.digor.be/,dienstencentrum@digor.be,"Kloosterstraat 6, 9031 Drongen",tick2368 YE2025 Strong official NBB PDF deposit 2026-00205516 + Strong KBO 0870.833.435 Actief 1 VE 2.160.628.775 RSZ2025 94.992; omzet empty; code73 empty; bruto JUMP 764649; pnl JUMP 162203; equity JUMP 2545841; assets JUMP 2633598; debt JUMP 87757; FTE FLAT 7.1; destin691 empty; kapitaalsubsidies empty; cash JUMP 1721124; leftover Sig@2367 same zetel; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+9) — envelope = bruto 9900 (VKT + omzet empty)
append_lines(DATA / "budgets.csv", [
    f"bud_digor_bruto_jr2025_statutory,{EID},2025,764649,764649,764649,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +12.83% (primary L5 envelope; omzet 70 empty),{SRC_PDF},strong,tick2368; PDF p5; YE2024 677667; VKT envelope because omzet empty; koepel-VZW not commercial-only",
    f"bud_digor_pnl_jr2025_statutory,{EID},2025,162203,162203,162203,NBB VKT-VZW code 9904 winst YE2025 JUMP +72.67%,{SRC_PDF},strong,tick2368; PDF p5; YE2024 93939; bedrijfswinst 9901 150853",
    f"bud_digor_equity_jr2025_statutory,{EID},2025,2545841,2545841,2545841,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +6.81%,{SRC_PDF},strong,tick2368; PDF p4; YE2024 2383638; kapitaalsubsidies empty; bestemde fondsen empty",
    f"bud_digor_assets_jr2025_statutory,{EID},2025,2633598,2633598,2633598,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +6.59%,{SRC_PDF},strong,tick2368; PDF p3; YE2024 2470732",
    f"bud_digor_debt_jr2025_statutory,{EID},2025,87757,87757,87757,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +0.76%,{SRC_PDF},strong,tick2368; PDF p4; YE2024 87094",
    f"bud_digor_cash_jr2025_statutory,{EID},2025,1721124,1721124,1721124,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +45.30% ~225pct bruto,{SRC_PDF},strong,tick2368; PDF p3; YE2024 1184554; 350k LT receivable YE2024 collected",
    f"bud_digor_buildings_jr2025_statutory,{EID},2025,773675,773675,773675,NBB VKT-VZW code 22 terreinen en gebouwen YE2025,{SRC_PDF},strong,tick2368; PDF p3; YE2024 781042; aanschaffingen 28612",
    f"bud_digor_personnel_jr2025_statutory,{EID},2025,543087,543087,543087,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +4.53%,{SRC_PDF},strong,tick2368; PDF p5; YE2024 519550; sociale balans 102 503980",
    f"bud_digor_fte_jr2025_statutory,{EID},2025,7.1,7.1,7.1,NBB VKT-VZW code 9087 FTE YE2025 FLAT,{SRC_PDF},strong,tick2368; PDF p8; YE2024 7.1",
])

# commitments (+1) — JSON doubled quotes like prior ticks
cash_json = (
    '"{""2025_omzet"":null,""2025_bruto"":764649,""2025_pnl"":162203,""2025_equity"":2545841,'
    '""2025_assets"":2633598,""2025_debt"":87757,""2025_fte"":7.1,""2025_code73"":null,'
    '""2025_kapitaalsubsidies"":null,""2025_destin691"":null,""2025_cash"":1721124,'
    '""2025_buildings"":773675,""2025_personnel62"":543087,'
    '""2024_omzet"":null,""2024_bruto"":677667,""2024_pnl"":93939,""2024_equity"":2383638,'
    '""2024_assets"":2470732,""2024_debt"":87094,""2024_fte"":7.1,""2024_cash"":1184554,'
    '""2024_lt_receivable"":350000}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},DiGOR vzw YE2025 (bruto 0.76m / pnl JUMP +73% / cash 1.72m JUMP / Strong PDF),{EID},koepel dienstencentrum Drongen / dual same zetel,VZW DiGOR (KBO 0870.833.435; Actief; 1 VE; RSZ2025 94.992),2026-06-26,2025,2025,764649,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00205516.pdf,Koepel/dienstencentrum gehandicaptenzorg onderwijs revalidatie + dual Drongen Ter Kouter cluster,Publish VL vs lidgeld vs other matrix inside bruto 764k (omzet+73 empty); explain cash 1.72m JUMP +45pct ~225pct bruto + 350k LT receivable collected,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Drongen>DiGOR>JR2025_statutory_L5,tick2368; Strong official PDF; leftover Sig@2367 same Drongen zetel; not TE-additive",
])

# leaderboard (+1) pi = 0.4*5.5 + 0.4*4.6 + 0.2*5 = 5.04
append_lines(DATA / "leaderboard.csv", [
    f"{LB},DiGOR vzw bruto 0.76m / pnl JUMP +73% / cash 1.72m JUMP (YE2025 koepel Drongen),L5,koepel_dienstencentrum_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Drongen>DiGOR>JR2025,764649,764649,PDF omzet empty; code73 empty; bruto JUMP 764649; pnl JUMP 162203; equity JUMP 2545841; assets JUMP 2633598; debt JUMP 87757; FTE FLAT 7.1; destin691 empty; kapitaalsubsidies empty; cash JUMP 1721124; buildings 773675,strong,{SRC_PDF},member VZW network disability/rehab/education (koepel Drongen Ter Kouter cluster),Dienstencentrum/koepel autonome VZW-leden gehandicaptenzorg onderwijs revalidatie,omzet+73 empty while bruto 0.76m; cash 1.72m ~225% bruto JUMP +45%; 350k LT receivable collected; dual leftover same-zetel koepel of Sig/Wegwijs/Ter Kouter cluster; VL/lidgeld split unpublished,5.5,4.6,5,5.04,FOI VL/lidgeld matrix inside bruto 764k (omzet+73 empty) + cash 1.72m JUMP + 350k receivable + dual Drongen Ter Kouter cluster,active,,tick2368; Strong official NBB PDF + Strong KBO; leftover Sig@2367 same zetel; next leftover Mozaiek",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Drongen>DiGOR>VL_bruto_omzet_empty,vzw_digor,VL vs lidgeld vs other split inside bruto 764649 given omzet 70 empty + code 73 empty; toelichting cash 1721124 JUMP +45pct ~225pct bruto; 350k LT receivable YE2024 collected; dual Drongen koepel zetel,Strong official PDF leftover koepel-VZW of Sig@2367 same zetel; omzet+73 empty while 0.76m bruto; cash 1.72m JUMP; public dienstencentrum not private clinic,8,DiGOR VZW / Jacques Adriaens voorzitter RvB,dienstencentrum@digor.be,"Kloosterstraat 6, 9031 Drongen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2368; ready NOT sent; Strong official NBB PDF; after Sig@2367; leftover same-zetel koepel; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2368 + append rq_2369 only
rq_path = DATA / "research_queue.csv"
rq_text = rq_path.read_text(encoding="utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2368,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2368 line, found {n}")
if not rq_text.endswith("\n"):
    raise SystemExit("research_queue missing trailing LF")

new_2368 = (
    "rq_2368,leftover dual — DiGOR vzw YE2025 Strong (bruto JUMP 0.76m / pnl JUMP +73% / cash 1.72m JUMP),hole_fill,8,done,L5,vzw_digor,"
    "After Sig YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel DIGOR 0870.833.435 deposit 2026-00205516 if live 2026pdf. "
    "Do NOT redo SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.,"
    f"{GAP},2026-08-24T21:58:20Z,{STAMP},"
    "tick2368 DiGOR 0870.833.435 YE2025 Strong official PDF 2026-00205516; omzet empty; code73 empty; bruto JUMP 764649; pnl JUMP 162203; equity JUMP 2545841; assets JUMP 2633598; debt JUMP 87757; FTE FLAT 7.1; destin691 empty; kapitaalsubsidies empty; cash JUMP 1721124; FOI ready NOT sent; leftover Sig@2367 same zetel; next leftover Mozaiek\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2368,"):
        parts.append(new_2368)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2368 replace count {replaced}")
new_rq = "".join(parts)
new_2369 = (
    "rq_2369,leftover dual after DiGOR — prefer AGB/FARO-YE2025/or leftover Mozaiek,hole_fill,8,open,L5,,"
    "After DiGOR YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel Mozaiek 0415.272.935 deposit 2026-00206415 if live 2026pdf. "
    "Do NOT redo DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2368; leftover Mozaiek still unused; DCGZ 0411.917.131 empty-shell skip; next EVERY-10 2370\n"
)
new_rq = new_rq + new_2369
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2368 + rq_2369; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2368,2368,no,"
    "tick2368 leftover dual DiGOR 0870.833.435 Strong PDF (omzet empty; code73 empty; bruto JUMP 764649 VKT envelope; pnl JUMP 162203; equity JUMP 2545841; assets JUMP 2633598; debt JUMP 87757; FTE FLAT 7.1; destin691 empty; kapitaalsubsidies empty; cash JUMP 1721124; 1 VE RSZ2025 94.992); after Sig@2367 same zetel; leftover Mozaiek; AGB/FARO/Gandae YE2024; next rq_2369; next EVERY-10 2370\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2368 - rq_2368 DiGOR vzw Drongen (bruto JUMP 0.76m / pnl JUMP +73% / cash 1.72m JUMP / Strong PDF)

- Unit: **rq_2368** leftover dual after **Sig@2367**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Took FREE leftover Flemish **DiGOR VZW** YE2025 (KBO **0870.833.435**; zetel Kloosterstraat 6, 9031 Drongen — same seat as Ter Kouter + CAR Het Veer + 't Vlot + Stappie + Oostakker + Noordhoek + De Elfjes + De Steijgertjes + De Steijger + Kapelhof + TKDV Het Veer + Wegwijs + Sig; VE **2.160.628.775** same address; **Actief** **1 VE**; RSZ2025 **94.992**; leftover same-zetel koepel/dienstencentrum of mined **Sig@2367** / **Wegwijs@2366** / **TKDV Het Veer@2365** / **Kapelhof@2364** / **De Steijger@2363** / **De Steijgertjes@2362** / **De Elfjes@2361** / **Noordhoek@2360** / **Oostakker@2359** / **Stappie@2358** / **'t Vlot@2357** / **CAR Het Veer@2356** / **Ter Kouter@2355**; dienstencentrum@digor.be). Confirmed leftover public (koepel/dienstencentrum autonome VZW-leden gehandicaptenzorg onderwijs revalidatie + same-zetel public CAR cluster) not private clinic. Do not redo SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.
- Found: official NBB VKT-VZW PDF deposit **2026-00205516** (48559 B / 12p; AV **05.06.2026**; neerlegging **26.06.2026**) — omzet 70 **empty**; code 73 **empty**; bruto **EUR764649** JUMP +12.83% (VKT envelope); pnl **EUR162203** JUMP +72.67%; equity **EUR2545841** JUMP +6.81%; assets **EUR2633598** JUMP +6.59%; debt **EUR87757** JUMP +0.76%; FTE **7.1** FLAT; kapitaalsubsidies **empty**; destin 691 **empty**; cash **EUR1721124** JUMP +45.30% (~225% bruto); 350k LT receivable YE2024 collected. Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+9); commitments (+1); leaderboard (+1 pi 5.04); entities (+1 vzw_digor); foi + draft `{GAP}`; rq_2368=done + rq_2369 open; loop_state ticks=2368; raw tick2368/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2370**). Next: rq_2369 leftover same-zetel Mozaiek 0415.272.935 deposit 2026-00206415 if live 2026pdf.
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")

(DATA / "_tick2368_stamp.txt").write_text(STAMP + "\n", encoding="utf-8")
print("done")
