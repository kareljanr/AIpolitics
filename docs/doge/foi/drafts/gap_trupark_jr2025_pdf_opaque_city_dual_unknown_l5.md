# FOI draft — AGB Trupark Sint-Truiden JR2025 residual (PDF opaque / city dual unknown)

**gap_id:** `gap_trupark_jr2025_pdf_opaque_city_dual_unknown_l5`  
**status:** ready (NOT sent)  
**entity:** AGB Trupark — Autonoom Gemeentebedrijf parkeer/mobiliteit Sint-Truiden (KBO 0761.818.697)  
**recipient:** AGB Trupark / Stad Sint-Truiden — info.trupark@sint-truiden.be / openbaarheid@sint-truiden.be — Gazometerstraat 13 3800 Sint-Truiden  
**sources:** [AGB Trupark portal](https://www.sint-truiden.be/agb-trupark); [JR2024 vaststelling (BBC+NBB PDFs; no 2025)](https://www.sint-truiden.be/vaststelling-jaarrekening-2024-agb-trupark); [KBO 0761.818.697](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html?nummer=0761818697); [NBB consult](https://consult.cbso.nbb.be/consult-enterprise/0761818697); [AGB hub](https://www.sint-truiden.be/autonome-gemeentebedrijven)  
**tick:** 1278

## Context (honest search; no invented euros)

- Entity II parking/mobility AGB after AGOST tick1156 + city Sint-Truiden GE (already mined). **Distinct from** AGB AGOST (0810.744.410), AGB PATRI (0635.564.190; also unmined), Zorgbedrijf Sint-Truiden (site unpublished — skipped). Legal form: Autonoom gemeentebedrijf since 29.06.2020 (GR 20.06.2020). Seat Gazometerstraat 13, 3800 Sint-Truiden since 6.02.2023. 1 VE. Bestuurder / RvB-voorzitter Ludwig Vandenhove since 27.01.2025; secretaris AD Kathleen Bergoets. College = directiecomité. NACE 52.210. RSZ employer since 1.01.2022. Contact info.trupark@sint-truiden.be / 011 87 28 82.
- **JR2024 is public** on the city site (RvB 26.05.2025): BBC + NBB + documentatie + jaarverslag PDFs. **JR2025 is not** on the AGB Trupark bekendmakingen list (only the 2024 vaststelling is linked).
- **Missing after honest fetch:** BBC J1–J5 / NBB VenB internals for 2025 (assets, fin debt, AFM/BBR, PnL, personeel €, city dual lock). City page has no 2025 download. NBB consult/API 403/SPA this box. Do **not** invent euros. Do **not** use Belscope/Companyweb.

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: AGB Trupark
     / Stad Sint-Truiden
t.a.v. de dienst openbaarheid van bestuur
Gazometerstraat 13
3800 Sint-Truiden
info.trupark@sint-truiden.be
openbaarheid@sint-truiden.be

Betreft: Verzoek om openbaarmaking van bestuursdocumenten — JR2025 dual
AGB Trupark (KBO 0761.818.697; city site publiceert JR2024 BBC+NBB,
geen JR2025-download)

Geachte,

Op grond van het Bestuursdecreet (openbaarheid van bestuur) dien ik hierbij een verzoek in tot
openbaarmaking / inzage / afschrift van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. De BBC-jaarrekening 2025 van AGB Trupark (schema's J1–J5, T-toelichtingen),
   in het bijzonder J2: autofinancieringsmarge, gecorrigeerde AFM,
   budgettair resultaat van het boekjaar en beschikbaar BBR.
2. De vennootschapsrechtelijke / NBB-jaarrekening 2025 (volledig of verkort
   model) inclusief balans, resultatenrekening, toelichting en
   commissarisverslag, in dezelfde vorm als de publieke JR2024-bundel
   (Trupark AGB 2024 - jaarrekening BBC.pdf / NBB.pdf).
3. City dual 2025: nominatieve werkings- en investeringssubsidies,
   vergoedingen, on-lend en eventuele overdracht van parkeerontvangsten
   tussen Stad Sint-Truiden en AGB Trupark (en omgekeerd), met splitsing
   per beleidsveld. Nominatieve lock 2026–2031.
4. Financiële schuld YE2025 (bank vs stad vs leasing),
   pensioenvoorzieningen, personeelskost en VTE.
5. Het besluit van de Raad van Bestuur (integrale gemeenteraad) tot
   vaststelling van de jaarrekening 2025, met directe download-URL
   (niet alleen de raadpleeg-SPA), analoog aan
   https://www.sint-truiden.be/vaststelling-jaarrekening-2024-agb-trupark
6. NBB Consult working URL / neerleggingsnummer van de jaarrekening 2025.
   De consult-API is van deze omgeving vaak 403/SPA.

Periode: boekjaar 2025 en nog lopende verbintenissen 2026–2031.

### 2. Context (waarom)

Onderzoek naar overheidsuitgaven (transparantie van publieke middelen).
Hiërarchisch pad: Vlaanderen>Gemeenten>Sint-Truiden>AGB_Trupark>jr2025_L5.

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail.
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: burger
Dossierreferentie intern: gap_trupark_jr2025_pdf_opaque_city_dual_unknown_l5

Met vriendelijke groet,

[Naam]
```

## Checklist vóór `ready`

- [x] Juiste instelling (AGB Trupark / Stad Sint-Truiden)
- [x] Concrete documenten (BBC J2, NBB VenB, city dual, RvB besluit, NBB URL)
- [x] Periode gevraagd (bedragen onbekend — niet verzonnen)
- [x] Meerjarigheid expliciet gevraagd
- [ ] Contactgegevens verzoeker ingevuld (human)
- [x] `foi_queue.csv` bijgewerkt

## Na verzending (mens)

1. `status=sent`, `date_sent=…`, schat `date_due`
2. Bewaar kopie in `foi/archive/{gap_id}-sent.md`
3. Bij antwoord: `answered` / `partial` / `refused` + `response_summary`
4. Vul `commitments.csv` / `leaderboard.csv` / `budgets.csv` bij — geen euro's tot primary PDF
