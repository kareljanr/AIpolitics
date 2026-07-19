# Sjabloon — verzoek openbaarheid van bestuur

Kopieer naar `foi/drafts/{gap_id}.md`, vul aan, zet `foi_queue.status` op `ready`.  
**Verzenden:** menselijke stap. Agents markeren niet `sent` zonder bevestiging.

Pas de geadresseerde en de wettelijke verwijzing aan (federaal / Vlaams / lokaal verschillen in procedure en termijnen). Dit is **geen juridisch advies**.

---

## Brief

```text
[Naam verzoeker / organisatie]
[Adres]
[E-mail]
[Telefoon]
[Datum]

Aan: [Naam instelling / FOD / departement / gemeente]
t.a.v. de dienst openbaarheid van bestuur / informatieambtenaar
[Adres instelling]
[E-mail indien bekend]

Betreft: Verzoek om openbaarmaking van bestuursdocumenten — [korte titel dossier]

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(federaal: wet 11 april 1994 en aanvullende bepalingen waar van toepassing;
Vlaams: Bestuursdecreet e.a.; lokaal: overeenkomstige regeling)
dien ik hierbij een verzoek in tot openbaarmaking / inzage / afschrift
van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

Ik vraag openbaarmaking van:

1. [Precies document / beslissing / subsidiedossier]
2. [Begrotingslijnen / basisallocaties met codes indien bekend]
3. [Lijst van begunstigden, bedragen, looptijd (start–einde)]
4. [Evaluatie- of voortgangsrapporten indien die bestaan]
5. [Meerjarige verbintenissen / engagementen gekoppeld aan dit dossier]

Periode: van [JJJJ-MM-DD] tot [JJJJ-MM-DD] (of: alle nog lopende verbintenissen).

### 2. Context (waarom)

Dit verzoek kadert in onderzoek naar overheidsuitgaven en subsidies
(transparantie van publieke middelen). Hiërarchisch pad (intern):
[hierarchy_path, bv. Vlaanderen > Departement X > Programma Y].

### 3. Vorm

Bij voorkeur: digitale kopie (PDF/CSV) per e-mail naar [e-mail].
Indien weigering of gedeeltelijke openbaarmaking: gemotiveerde beslissing
met vermelding van de rechtsgrond en de beroepsmogelijkheden.

### 4. Identiteit

Naam: […]
Hoedanigheid: [burger / vertegenwoordiger van …]
Dossierreferentie intern: [gap_id]

Met vriendelijke groet,

[Naam]
[Handtekening indien per post]
```

---

## Checklist vóór `ready`

- [ ] Juiste instelling (wie heeft het document?)  
- [ ] Concrete documenten, geen vage “alles over cultuur”  
- [ ] Periode en bedragen gevraagd  
- [ ] Meerjarigheid expliciet gevraagd  
- [ ] Contactgegevens verzoeker ingevuld  
- [ ] `foi_queue.csv` bijgewerkt  

## Na verzending (mens)

1. `status=sent`, `date_sent=…`, schat `date_due`  
2. Bewaar kopie in `foi/archive/{gap_id}-sent.md`  
3. Bij antwoord: `answered` / `partial` / `refused` + `response_summary`  
4. Vul `commitments.csv` / `leaderboard.csv` bij  
