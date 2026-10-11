#!/usr/bin/env python3
"""Surgical tick 2369 writes — append/patch only, never rewrite whole CSVs."""
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
NOW = datetime.now(timezone.utc)
STAMP = NOW.strftime("%Y-%m-%dT%H:%M:%SZ")
DAY = NOW.strftime("%Y-%m-%d")
print("STAMP", STAMP)

EID = "vzw_mozaiek"
SRC_PDF = "src_mozaiek_jr2025_nbb_pdf_2369"
SRC_KBO = "src_mozaiek_kbo_2369"
SRC_SBM = "src_mozaiek_sbm_2369"
SRC_SITE = "src_mozaiek_site_2369"
COMM = "comm_mozaiek_jr2025_statutory_opbr_15_58m_73_13_18m_600k_destin"
LB = "lb_mozaiek_opbr_15_58m_73_13_18m_600k_destin_jr2025"
GAP = "gap_mozaiek_vaph_vl_matrix_73_13_18m_vs_733_22k_600k_destin_kapitaalsubsidies_3_13m_l5"
DRAFT = f"docs/doge/foi/drafts/{GAP}.md"

foi = f"""# FOI draft — Mozaïek vzw (opbr 15.58m / 73 13.18m vs 733 22k / 600k destin / 3.13m kapitaalsubsidies)

**gap_id:** `{GAP}`  
**status:** ready (NOT sent)  
**entity:** Mozaïek vzw — KBO **0415.272.935** (Actief; 4 VE: **2.153.629.038** Dienstencentrum Mozaïek Kloosterstraat 6 9031 Gent/Drongen; **2.245.762.905** Dienstencentrum Mozaïek Wolfputstraat 106 9041 Oostakker; **2.366.147.229** Leeuwerikstraat 28 9000 Gent sinds 15.11.2024; **2.366.147.823** Campus Sint-Amandsberg Antwerpsesteenweg 587 9040 Gent sinds 15.11.2024; zetel Kloosterstraat 6, 9031 Gent/Drongen; RSZ2025 **87.202** instellingen met huisvesting voor volwassenen met een mentale handicap; paritair comité **31901**; voorzitter RvB Marc Colson; commissaris BV Guy Van De Velde Bedrijfsrevisor 0890.848.295)  
**recipient:** Mozaïek vzw / Marc Colson (voorzitter RvB) — info@mozaiekvzw.be — Campus Wolfput, Wolfputstraat 106, 9041 Oostakker / zetel Kloosterstraat 6, 9031 Drongen  
**sources:** official NBB WVV VOL-VZW PDF deposit **2026-00206415** (header neerlegging **24.06.2026**; CDN Last-Modified **10.07.2026**; AV **28.05.2026**; **71192** bytes / **22p**; model **VOL-VZW** 26.0.15 m05-f); [official CDN](http://cdn.staatsbladmonitor.be/2026pdf/2026-00206415.pdf); [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0415272935); [KBO 0415.272.935](https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415272935); [site](https://www.mozaiekvzw.be/)  
**tick:** 2369 (NOT every-10; next every-10 is **2370**)

## Context (primary official NBB VOL-VZW JR2025)

- Leftover dual public **VAPH woon-/dagondersteuning-VZW** (verstandelijke beperking / psychische kwetsbaarheid / autisme / NAH) of mined **DiGOR@2368** + **Sig@2367** + **CAR Wegwijs@2366** + **TKDV Het Veer@2365** + **Kapelhof@2364** + **De Steijger@2363** + **De Steijgertjes@2362** + **De Elfjes@2361** + **Noordhoek@2360** + **Oostakker@2359** + **Stappie@2358** + **'t Vlot@2357** + **CAR Het Veer@2356** + **Ter Kouter@2355** — same statutory seat Kloosterstraat 6 Drongen + shared board (Adriaens Jacques/Bart). Prefix `vzw_mozaiek` unused. Parent `sec_flanders`. Confirmed leftover public (VAPH-erkende woon-/dagondersteuning + same-zetel public CAR/inclusie cluster) not private clinic.
- Stalls this tick: AGB Bornem still **JR2024**; FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). First unused leftover same-zetel with live 2026pdf after DiGOR: Mozaiek (deposit HEAD 200 / 71192 B).
- EUR **strong** from official PDF (not Companyweb / not SBM table): omzet 70 **1310545** JUMP +7.70% (commercial-only vs large 73); code 73 **13178905** JUMP +9.01%; bedrijfsopbrengsten 70/76A **15575272** JUMP +7.68% (VOL envelope); pnl 9905 **652763** DROP −20.85%; equity **10585730** JUMP +4.51%; assets **12684232** JUMP +3.84%; debt **2098502** JUMP +0.62%; FTE **167.9** JUMP +6.40%; kapitaalsubsidies 15 **3127494** DROP −5.90%; destin 691 **600000** JUMP (sociaal passief); bestemde fondsen 13 **2312739** JUMP +35.03%; cash **2678112** JUMP +17.38%; 6.9 split of 73 only shows 733 subsidies **22128** + 732 legaten **41979** (lidgelden/schenkingen empty) — residual ~13.11m of code 73 unpublished. Strong KBO + Strong PDF.
- Named Drongen stack now **exhausted** (Ter Kouter / Het Veer CAR / 't Vlot / Stappie / Oostakker / Noordhoek / De Elfjes / De Steijgertjes / De Steijger / Kapelhof / TKDV Het Veer / Wegwijs / SIG / DIGOR / Mozaiek). DCGZ 0411.917.131 empty shell. Steunfonds Martens-Sotteau absorbed. Unnamed same-zetel: SBM lists 19 other KBOs at Kloosterstraat 6.

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: Mozaïek vzw
t.a.v. de dienst openbaarheid van bestuur / Marc Colson
(voorzitter Raad van Bestuur)
Wolfputstraat 106
9041 Oostakker
info@mozaiekvzw.be
https://www.mozaiekvzw.be/

Betreft: Verzoek om openbaarmaking van bestuursdocumenten —
JR2025 Mozaïek vzw (KBO 0415.272.935)
bedrijfsopbrengsten 15.575.272
/ lidgeld-schenkingen-subsidies code 73 13.178.905
(toelichting 733 subsidies slechts 22.128)
/ bestemming 600.000 sociaal passief
/ kapitaalsubsidies 3.127.494
/ liquide middelen 2.678.112
/ FTE 167,9

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur)
dien ik hierbij een verzoek in tot openbaarmaking / inzage /
afschrift van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. De volledige jaarrekening 2025 (NBB VOL-VZW deposit
   2026-00206415) plus het activiteitenverslag 2025 en
   het verslag van het bestuursorgaan aan de AV van
   28 mei 2026.
2. De uitsplitsing van code 73 EUR 13.178.905
   (was 12.089.523; JUMP +9,01%) — waarom toelichting
   6.9 slechts subsidies 733 EUR 22.128 + legaten 732
   EUR 41.979 toont (lidgelden 730 en schenkingen 731
   leeg) terwijl circa 13,11 miljoen ongeplitst blijft.
   Matrix VAPH (PVF / RTH / vergunde zorg) /
   Departement Zorg / RIZIV / lokale besturen /
   overige per bedrag / looptijd / KPI.
3. De uitsplitsing van omzet code 70 EUR 1.310.545
   (was 1.216.812; JUMP +7,70%) versus
   bedrijfsopbrengsten 70/76A EUR 15.575.272 —
   welke stromen zijn commerciële eigen bijdragen
   / winkel / dagbesteding versus publieke financiering.
4. De toelichting bij toevoeging bestemde fondsen
   code 691 EUR 600.000 (sociaal passief) en stand
   code 13 EUR 2.312.739 (was 1.712.739; JUMP +35,03%).
5. De toelichting bij kapitaalsubsidies code 15
   EUR 3.127.494 (was 3.323.563; DROP −5,90%) —
   bron / afschrijving / geoormerkte gebouwen
   (Kloosterstraat 6; Wolfputstraat 106;
   Leeuwerikstraat 28; Campus Sint-Amandsberg
   Antwerpsesteenweg 587).
6. De toelichting bij liquide middelen code 54/58
   EUR 2.678.112 (was 2.281.643; JUMP +17,38%) —
   treasurybeleid / geoormerkte publieke middelen.
7. De toelichting bij personeel code 62
   EUR 12.003.809 (was 10.894.641; JUMP +10,18%)
   versus FTE 167,9 (was 157,8; JUMP +6,40%) en
   211 koppen — uitsplitsing per campus / functie.
8. De relatie duale rechtspersonen op dezelfde
   statutaire zetel Drongen (Kloosterstraat 6 —
   zelfde adres als DiGOR, Sig, CAR Ter Kouter,
   CAR Het Veer, CAR 't Vlot, CAR Stappie,
   CAR Oostakker, CAR Noordhoek, CAR De Steijger,
   CAR Kapelhof, CAR Wegwijs, KDV De Elfjes,
   KDV De Steijgertjes, TKDV Het Veer) —
   ledenlijst, interne rekeningen, subsidies,
   gedeelde raad.
9. De notulen van de algemene vergadering van
   28 mei 2026 (niet-persoonsgebonden delen).

Periode: boekjaar 01.01.2025–31.12.2025 en lopende
meerjarige verbintenissen.

### 2. Context (waarom)

Dit verzoek kadert in onderzoek naar overheidsuitgaven
en subsidies (transparantie van publieke middelen).
Hiërarchisch pad (intern):
Vlaanderen > Oost-Vlaanderen > Drongen / Gent >
Mozaïek vzw > JR2025 statutory L5.

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

- [x] Juiste instelling (Mozaïek vzw / voorzitter RvB)
- [x] Concrete documenten (VAPH/VL-matrix 73 13.18m vs 733 22k; 600k destin; 3.13m kapitaalsubsidies)
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
    f"{SRC_PDF},NBB WVV VOL-VZW jaarrekening 2025 Mozaiek vzw deposit 2026-00206415,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206415.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2369; official PDF 71192 bytes 22p VOL-VZW 26.0.15 m05-f; header 24.06.2026; AV 28.05.2026; YE 01.01.2025-31.12.2025; euros extracted from PDF text not SBM table",
    f"{SRC_KBO},KBO Mozaiek vzw 0415.272.935,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0415272935,KBO Public Search FOD Economie,{DAY},official_register,tick2369; Actief; 4 VE 2.153.629.038 Kloosterstraat 6 + 2.245.762.905 Wolfputstraat 106 + 2.366.147.229 Leeuwerikstraat 28 + 2.366.147.823 Campus Sint-Amandsberg; zetel Kloosterstraat 6 9031 Gent/Drongen; RSZ2025 87.202; voorzitter Colson Marc",
    f"{SRC_SBM},Staatsbladmonitor fiche Mozaiek vzw 0415272935 (deposit-id only),https://staatsbladmonitor.be/bedrijfsfiche.html?ondernemingsnummer=0415272935,Staatsbladmonitor,{DAY},official_register,tick2369; deposit-id 2026-00206415 and CDN Last-Modified 2026-07-10; euros NOT taken from SBM HTML table",
    f"{SRC_SITE},Mozaiek vzw FOI contact / VAPH woon-dagondersteuning Gent,https://www.mozaiekvzw.be/,Mozaiek vzw,{DAY},foi_contact,tick2369; FOI info@mozaiekvzw.be; campus Wolfputstraat 106 9041 Oostakker; zetel Kloosterstraat 6 9031 Drongen; leftover same-zetel Ter Kouter/DIGOR cluster",
])

# entities (+1)
append_lines(DATA / "entities.csv", [
    f'{EID},Mozaiek VZW (Drongen-Gent / VAPH woon-dagondersteuning),Mozaiek ASBL (Drongen-Gand / hebergement VAPH),Mozaiek VZW (Drongen-Ghent / VAPH housing-day support),parastatal,sec_flanders,nl,https://www.mozaiekvzw.be/,info@mozaiekvzw.be,"Kloosterstraat 6, 9031 Drongen / Wolfputstraat 106, 9041 Oostakker",tick2369 YE2025 Strong official NBB PDF deposit 2026-00206415 + Strong KBO 0415.272.935 Actief 4 VE RSZ2025 87.202; omzet 1310545 commercial-only; code73 JUMP 13178905; opbr JUMP 15575272 VOL envelope; pnl DROP 652763; equity JUMP 10585730; assets JUMP 12684232; debt JUMP 2098502; FTE JUMP 167.9; destin691 JUMP 600000; kapitaalsubsidies DROP 3127494; cash JUMP 2678112; leftover DIGOR@2368 same zetel; AGB/FARO/Gandae YE2024; not TE-additive',
])

# budgets (+10) — envelope = bedrijfsopbrengsten 70/76A (VOL + omzet commercial-only vs large 73)
append_lines(DATA / "budgets.csv", [
    f"bud_mozaiek_opbr_jr2025_statutory,{EID},2025,15575272,15575272,15575272,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +7.68% (primary L5 envelope; omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2369; PDF p6; YE2024 14464606; VOL envelope because omzet 1.31m vs 73 13.18m",
    f"bud_mozaiek_code73_jr2025_statutory,{EID},2025,13178905,13178905,13178905,NBB VOL-VZW code 73 lidgeld/schenkingen/subsidies YE2025 JUMP +9.01%,{SRC_PDF},strong,tick2369; PDF p6; YE2024 12089523; 6.9 split only 733=22128 + 732=41979",
    f"bud_mozaiek_omzet_jr2025_statutory,{EID},2025,1310545,1310545,1310545,NBB VOL-VZW code 70 omzet YE2025 JUMP +7.70% (commercial-only vs large 73),{SRC_PDF},strong,tick2369; PDF p6; YE2024 1216812; not primary envelope",
    f"bud_mozaiek_pnl_jr2025_statutory,{EID},2025,652763,652763,652763,NBB VOL-VZW code 9905 te bestemmen winst YE2025 DROP -20.85%,{SRC_PDF},strong,tick2369; PDF p7; YE2024 824756; bedrijfswinst 9901 634949 DROP -21.80%",
    f"bud_mozaiek_equity_jr2025_statutory,{EID},2025,10585730,10585730,10585730,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +4.51%,{SRC_PDF},strong,tick2369; PDF p5; YE2024 10129037; kapitaalsubsidies 3127494; bestemde fondsen 2312739",
    f"bud_mozaiek_assets_jr2025_statutory,{EID},2025,12684232,12684232,12684232,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +3.84%,{SRC_PDF},strong,tick2369; PDF p4; YE2024 12214682",
    f"bud_mozaiek_debt_jr2025_statutory,{EID},2025,2098502,2098502,2098502,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +0.62%,{SRC_PDF},strong,tick2369; PDF p5; YE2024 2085646",
    f"bud_mozaiek_cash_jr2025_statutory,{EID},2025,2678112,2678112,2678112,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +17.38%,{SRC_PDF},strong,tick2369; PDF p4; YE2024 2281643",
    f"bud_mozaiek_destin691_jr2025_statutory,{EID},2025,600000,600000,600000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (sociaal passief),{SRC_PDF},strong,tick2369; PDF p8+p13; YE2024 empty; stand 13 = 2312739",
    f"bud_mozaiek_fte_jr2025_statutory,{EID},2025,167.9,167.9,167.9,NBB VOL-VZW code 9087/1003 FTE YE2025 JUMP +6.40%,{SRC_PDF},strong,tick2369; PDF p14+p17; YE2024 157.8; koppen 9086=211",
])

# commitments (+1)
cash_json = (
    '"{""2025_omzet"":1310545,""2025_code73"":13178905,""2025_opbr"":15575272,""2025_pnl"":652763,'
    '""2025_equity"":10585730,""2025_assets"":12684232,""2025_debt"":2098502,""2025_fte"":167.9,'
    '""2025_kapitaalsubsidies"":3127494,""2025_destin691"":600000,""2025_destin13"":2312739,'
    '""2025_cash"":2678112,""2025_personnel62"":12003809,""2025_subsidies733"":22128,'
    '""2024_omzet"":1216812,""2024_code73"":12089523,""2024_opbr"":14464606,""2024_pnl"":824756,'
    '""2024_equity"":10129037,""2024_assets"":12214682,""2024_debt"":2085646,""2024_fte"":157.8,'
    '""2024_kapitaalsubsidies"":3323563,""2024_destin13"":1712739,""2024_cash"":2281643}"'
)
append_lines(DATA / "commitments.csv", [
    f"{COMM},Mozaiek vzw YE2025 (opbr 15.58m / 73 13.18m / 600k destin / Strong PDF),{EID},VAPH woon-dagondersteuning Gent / dual same zetel,VZW Mozaiek (KBO 0415.272.935; Actief; 4 VE; RSZ2025 87.202),2026-06-24,2025,2025,15575272,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00206415.pdf,VAPH woon- en dagondersteuning verstandelijke beperking + dual Drongen Ter Kouter cluster,Publish VAPH/VL matrix inside code 73 13.18m (6.9 shows only 733=22k); explain 600k destin sociaal passief + 3.13m kapitaalsubsidies,{SRC_PDF},strong,Vlaanderen>Oost_Vlaanderen>Gent>Mozaiek>JR2025_statutory_L5,tick2369; Strong official PDF; leftover DIGOR@2368 same Drongen zetel; not TE-additive",
])

# leaderboard (+1) pi = 0.4*5.6 + 0.4*6.8 + 0.2*5 = 5.96
append_lines(DATA / "leaderboard.csv", [
    f"{LB},Mozaiek vzw opbr 15.58m / 73 13.18m vs 733 22k / 600k destin (YE2025 VAPH Gent),L5,vaph_woon_dag_vzw_statutory,Vlaanderen>Oost_Vlaanderen>Gent>Mozaiek>JR2025,15575272,15575272,PDF omzet 1310545 commercial-only; code73 JUMP 13178905; opbr JUMP 15575272; pnl DROP 652763; equity JUMP 10585730; assets JUMP 12684232; debt JUMP 2098502; FTE JUMP 167.9; destin691 JUMP 600000; kapitaalsubsidies DROP 3127494; cash JUMP 2678112,strong,{SRC_PDF},adults with intellectual disability / mental vulnerability / autism / ABI (VAPH),VAPH-erkende woon- en dagondersteuning + individuele begeleiding,code 73 13.18m but 6.9 only shows 733=22k + 732=42k; 600k destin sociaal passief; 3.13m kapitaalsubsidies; dual leftover same-zetel of DIGOR/Ter Kouter cluster; VAPH/VL split unpublished,5.6,6.8,5,5.96,FOI VAPH/VL matrix inside 73 13.18m (vs 733 22k) + 600k destin + 3.13m kapitaalsubsidies + dual Drongen cluster,active,,tick2369; Strong official NBB PDF + Strong KBO; leftover DIGOR@2368 same zetel; named Drongen stack exhausted",
])

# foi_queue (+1)
append_lines(DATA / "foi_queue.csv", [
    f'{GAP},Vlaanderen>Oost_Vlaanderen>Gent>Mozaiek>VAPH_VL_73_vs_733,vzw_mozaiek,VAPH vs VL vs other split inside code 73 13178905 given 6.9 only shows 733 subsidies 22128 + 732 legaten 41979; toelichting destin 691 600000 sociaal passief; kapitaalsubsidies 3127494; cash 2678112 JUMP; dual Drongen zetel,Strong official PDF leftover VAPH-VZW of DIGOR@2368 same zetel; 13.18m code 73 barely split; 600k destin; public woon-dagondersteuning not private clinic,8,Mozaiek VZW / Marc Colson voorzitter RvB,info@mozaiekvzw.be,"Wolfputstraat 106, 9041 Oostakker / Kloosterstraat 6, 9031 Drongen",{DRAFT},ready,{DAY},,,,,{COMM},{LB},{STAMP},{STAMP},tick2369; ready NOT sent; Strong official NBB PDF; after DIGOR@2368; leftover same-zetel VAPH; named Drongen stack exhausted; AGB/FARO/Gandae still YE2024',
])

# research_queue: patch rq_2369 + append rq_2370 only
rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("research_queue missing trailing LF")
rq_text = rq_raw.decode("utf-8")
n = sum(1 for ln in rq_text.splitlines() if ln.startswith("rq_2369,"))
if n != 1:
    raise SystemExit(f"expected 1 rq_2369 line, found {n}")
if "rq_2370," in rq_text:
    raise SystemExit("rq_2370 already exists")

new_2369 = (
    "rq_2369,leftover dual — Mozaiek vzw YE2025 Strong (opbr JUMP 15.58m / 73 13.18m / 600k destin),"
    "hole_fill,8,done,L5,vzw_mozaiek,"
    "After DiGOR YE2025. Prefer AGB/FARO if YE2025 else leftover same-zetel Mozaiek 0415.272.935 deposit 2026-00206415 if live 2026pdf. "
    "Do NOT redo DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.,"
    f"{GAP},2026-08-24T22:04:10Z,{STAMP},"
    "tick2369 Mozaiek 0415.272.935 YE2025 Strong official PDF 2026-00206415; omzet 1310545 commercial-only; code73 JUMP 13178905; opbr JUMP 15575272 VOL envelope; pnl DROP 652763; equity JUMP 10585730; assets JUMP 12684232; debt JUMP 2098502; FTE JUMP 167.9; destin691 JUMP 600000; kapitaalsubsidies DROP 3127494; cash JUMP 2678112; FOI ready NOT sent; leftover DIGOR@2368 same zetel; named Drongen stack exhausted\n"
)
parts = []
replaced = 0
for line in rq_text.splitlines(keepends=True):
    if line.startswith("rq_2369,"):
        parts.append(new_2369)
        replaced += 1
    else:
        parts.append(line)
if replaced != 1:
    raise SystemExit(f"rq_2369 replace count {replaced}")
new_rq = "".join(parts)
new_2370 = (
    "rq_2370,EVERY-10 progress + leftover dual after Mozaiek — named Drongen stack exhausted,"
    "hole_fill,8,open,L5,,"
    "Tick 2370 EVERY-10 MANDATORY: refresh progress_every_10_ticks.md (layers A-E of EUR 347.956 bn TE) + doge_waste_top10_current.md (top 10 by priority_index). "
    "Then leftover after named Drongen stack (Ter Kouter/Het Veer/'t Vlot/Stappie/Oostakker/Noordhoek/De Elfjes/De Steijgertjes/De Steijger/Kapelhof/TKDV Het Veer/Wegwijs/SIG/DIGOR/Mozaiek taken; DCGZ empty skip; Steunfonds absorbed). "
    "Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live official JR2025 (incl. unnamed same-zetel Kloosterstraat 6 if unused public + live 2026pdf). "
    "Do NOT redo named Drongen stack or Adem/MFC Combo/De Branding/Korenbloem/Leieborg.,,"
    f"{STAMP},{STAMP},"
    "spawned after tick2369; named Drongen stack exhausted; AGB/FARO/Gandae still YE2024; 2370 IS EVERY-10\n"
)
new_rq = new_rq + new_2370
rq_path.write_text(new_rq, encoding="utf-8")
print("patched research_queue rq_2369 + rq_2370; bytes", rq_path.stat().st_size)

# loop_state replace data row only
state_path = DATA / "loop_state.csv"
state_hdr = "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
state_row = (
    "main,continuous,hole_fill,"
    f"{STAMP},rq_2369,2369,no,"
    "tick2369 leftover dual Mozaiek 0415.272.935 Strong PDF (omzet 1310545 commercial-only; code73 JUMP 13178905; opbr JUMP 15575272 VOL envelope; pnl DROP 652763; equity JUMP 10585730; assets JUMP 12684232; debt JUMP 2098502; FTE JUMP 167.9; destin691 JUMP 600000; kapitaalsubsidies DROP 3127494; cash JUMP 2678112; 4 VE RSZ2025 87.202); after DIGOR@2368 same zetel; named Drongen stack exhausted; AGB/FARO/Gandae YE2024; next rq_2370 EVERY-10\n"
)
cur = state_path.read_text(encoding="utf-8")
if not cur.startswith(state_hdr):
    raise SystemExit("loop_state header mismatch")
state_path.write_text(state_hdr + state_row, encoding="utf-8")
print("wrote loop_state")

# loop_log append
log_path = ROOT / "docs/doge/loop_log.md"
log = f"""
### {STAMP} - tick 2369 - rq_2369 Mozaiek vzw Gent (opbr JUMP 15.58m / 73 13.18m vs 733 22k / 600k destin / Strong PDF)

- Unit: **rq_2369** leftover dual after **DiGOR@2368**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (bornem.be JR2024 only); FARO/AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024** (no live 2026pdf; not re-downloaded). Took FREE leftover Flemish **Mozaïek VZW** YE2025 (KBO **0415.272.935**; zetel Kloosterstraat 6, 9031 Drongen — same seat as Ter Kouter + CAR Het Veer + 't Vlot + Stappie + Oostakker + Noordhoek + De Elfjes + De Steijgertjes + De Steijger + Kapelhof + TKDV Het Veer + Wegwijs + Sig + DiGOR; 4 VE **2.153.629.038** Kloosterstraat 6 + **2.245.762.905** Wolfputstraat 106 Oostakker + **2.366.147.229** Leeuwerikstraat 28 Gent + **2.366.147.823** Campus Sint-Amandsberg; **Actief**; RSZ2025 **87.202**; leftover same-zetel VAPH woon-/dagondersteuning of mined **DiGOR@2368** / **Sig@2367** / **Wegwijs@2366** / **TKDV Het Veer@2365** / **Kapelhof@2364** / **De Steijger@2363** / **De Steijgertjes@2362** / **De Elfjes@2361** / **Noordhoek@2360** / **Oostakker@2359** / **Stappie@2358** / **'t Vlot@2357** / **CAR Het Veer@2356** / **Ter Kouter@2355**; info@mozaiekvzw.be). Confirmed leftover public (VAPH-erkende woon-/dagondersteuning verstandelijke beperking / psychische kwetsbaarheid / autisme / NAH + same-zetel public CAR cluster) not private clinic. Do not redo DIGOR/SIG/Wegwijs/TKDV Het Veer/Kapelhof/De Steijger/De Steijgertjes/De Elfjes/Noordhoek/Oostakker/Stappie/'t Vlot/Het Veer/Ter Kouter/Adem/MFC Combo/De Branding/Korenbloem/Leieborg stack.
- Found: official NBB VOL-VZW PDF deposit **2026-00206415** (71192 B / 22p; AV **28.05.2026**; header **24.06.2026**) — omzet 70 **EUR1310545** JUMP +7.70% (commercial-only vs large 73); code 73 **EUR13178905** JUMP +9.01%; bedrijfsopbrengsten **EUR15575272** JUMP +7.68% (VOL envelope); pnl **EUR652763** DROP −20.85%; equity **EUR10585730** JUMP +4.51%; assets **EUR12684232** JUMP +3.84%; debt **EUR2098502** JUMP +0.62%; FTE **167.9** JUMP +6.40%; kapitaalsubsidies **EUR3127494** DROP −5.90%; destin 691 **EUR600000** JUMP (sociaal passief); cash **EUR2678112** JUMP +17.38%; 6.9 split of 73 only 733 **EUR22128** + 732 **EUR41979**. Strong KBO + Strong PDF.
- Wrote: sources (+4); budgets (+10); commitments (+1); leaderboard (+1 pi 5.96); entities (+1 vzw_mozaiek); foi + draft `{GAP}`; rq_2369=done + rq_2370 open; loop_state ticks=2369; raw tick2369/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2370 IS every-10**). Named Drongen stack **exhausted**. Next: rq_2370 EVERY-10 + unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK with live 2026pdf (incl. unnamed same-zetel Kloosterstraat 6 if unused public).
"""
with log_path.open("a", encoding="utf-8") as f:
    f.write(log)
print("appended loop_log")
print("done")
