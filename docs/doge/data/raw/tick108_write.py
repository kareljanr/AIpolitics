"""Tick 108: rq_108 VLAIO FIO bedrijfssteun O&O L5 sample from PQs + Speurgids."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1]
ROOT = DATA.parent
UTC = "2026-07-27T01:20:00Z"

# --- sources ---
with (DATA / "sources.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "src_vl_pq_177_innovatie_limburg,VP SV 177 Pieters/Diependaele innovatiesteun Limburg 19 Jan 2026,"
        "https://docs.vlaamsparlement.be/pfile?id=2282507,Vlaams Parlement / Diependaele,2026-07-27,parliament,"
        '"OND+ONTW+ICON Flanders 2025 196.90m / 388 firms; full portfolio 214.15m; raw vl_pq_limburg_vlaio.pdf"\n'
    )
    f.write(
        "src_vl_pq_209_ontwikkelingsprojecten,VP SV 209 Warnez/Diependaele ontwikkelingsprojecten 28 Jan 2026,"
        "https://docs.vlaamsparlement.be/pfile?id=2288201,Vlaams Parlement / Diependaele,2026-07-27,parliament,"
        '"ONTW 2021-25 443m; 918/1093 approved 2023-25; province split; confidential project L5; raw vl_pq_vlaio_prov.pdf"\n'
    )
    f.write(
        "src_vl_pq_351_woosh,VP SV 351 Van Looy/Brouns Woosh subsidies 31 Jan 2025,"
        "https://docs.vlaamsparlement.be/pfile?id=2128708,Vlaams Parlement / Brouns,2026-07-27,parliament,"
        '"Named Woosh VLAIO L5: ONTW 158k+376k; KMOGS 50k; haalbaarheid 46k; Schaalklaar 350k; raw vl_pq_woosh.pdf"\n'
    )
    f.write(
        "src_speurgids_2025_clusters,Speurgids 2025 cluster+Moonshot tables (VLAIO data),"
        "https://www.ewi-vlaanderen.be/speurgids-2025,Departement WEWIS / VLAIO,2026-07-27,budget,"
        '"Cluster earmarked 2024 decided 54.2m; Moonshot 24.54m/10 projects; Edtech Station 1.8m/3y; raw speurgids2025_full.pdf"\n'
    )

# --- programmes ---
with (DATA / "programmes.csv").open("a", encoding="utf-8", newline="") as f:
    f.write(
        "fio_innovatie_ond_ontw_icon_2025,vlaio,,FIO_INN,Innovatiesteun OND+ONTW+ICON decision-year 2025,,"
        "2025,196895177,src_vl_pq_177_innovatie_limburg,strong,Vlaanderen>VLAIO>FIO>innovatie,"
        '"PQ177 table3a: 196895176.59 EUR; 388 firms; 390 projects"\n'
    )
    f.write(
        "fio_innovatie_full_portfolio_2025,vlaio,,FIO_INN_FULL,Innovatiesteun full portfolio incl ISS Schaalklaar haalbaarheid 2025,,"
        "2025,214147402,src_vl_pq_177_innovatie_limburg,strong,Vlaanderen>VLAIO>FIO>innovatie_full,"
        '"PQ177 table3b: 214147401.59 EUR Flanders"\n'
    )
    f.write(
        "fio_ontwikkelingsprojecten_2021_25,vlaio,,ONTW,Ontwikkelingsprojecten cumulative decisions 2021-2025,,"
        "2025,443000000,src_vl_pq_209_ontwikkelingsprojecten,strong,Vlaanderen>VLAIO>FIO>ONTW,"
        '"PQ209: 443m EUR on 1275m project cost ~35pct avg intensity"\n'
    )
    f.write(
        "fio_cluster_earmarked_2024,vlaio,,CLUSTER,Speerpuntcluster geoormerkte projecten decided 2024,,"
        "2024,54200000,src_speurgids_2025_clusters,strong,Vlaanderen>VLAIO>clusters,"
        '"Speurgids Table18: 54.2m decided / 38 projects; reserve 47.8m"\n'
    )
    f.write(
        "fio_moonshot_2024,vlaio,,MOONSHOT,Moonshot ESI+LSI projects decided 2024,,"
        "2024,24540891,src_speurgids_2025_clusters,strong,Vlaanderen>VLAIO>Moonshot,"
        '"Speurgids Table28: 24.540891m / 10 projects (ESI 21.1 LSI 3.4)"\n'
    )

# --- commitments L5 samples ---
new_cmts = [
    {
        "commitment_id": "cmt_vlaio_innovatie_portfolio_2025",
        "title": "VLAIO innovatiesteun OND+ONTW+ICON decision-year 2025",
        "entity_id": "vlaio",
        "beneficiary": "Flemish companies knowledge partners R&D",
        "legal_basis": "FIO research and development project grants + ICON",
        "decision_date": "2025-01-01",
        "start_year": "2020",
        "end_year": "2025",
        "total_envelope_eur": "196895177",
        "cash_by_year": (
            '{"2020":256795549,"2021":258808208.50,"2022":160088962,"2023":179898031.04,'
            '"2024":221485174.85,"2025":196895176.59,"firms_2025":388,"projects_2025":390}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Private R&D additionality and competitiveness",
        "cut_option": "Tighten selectivity (already BO2026 -12m path); publish full L5 register",
        "source_id": "src_vl_pq_177_innovatie_limburg",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VLAIO>FIO>innovatie",
        "notes": "PQ177 strong multi-year; Speurgids FIO bedrijfssteun O&O BO 210.9m is budget not same as awards",
    },
    {
        "commitment_id": "cmt_vlaio_ontw_2021_25",
        "title": "VLAIO ontwikkelingsprojecten cumulative 2021-2025",
        "entity_id": "vlaio",
        "beneficiary": "Companies with R&D in Flanders",
        "legal_basis": "Ontwikkelingsproject 25-50pct max 3m per project",
        "decision_date": "2021-01-01",
        "start_year": "2021",
        "end_year": "2025",
        "total_envelope_eur": "443000000",
        "cash_by_year": (
            '{"cumul_2021_25":443000000,"project_cost":1275000000,"avg_intensity_pct":35,'
            '"ANT":110900000,"OV":132500000,"WVL":79300000,"VBR":70300000,"LIM":38000000,"other":12000000,'
            '"approved_2023_25":918,"filed_2023_25":1093}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Near-market product process service innovation",
        "cut_option": "Publish named project L5; additionality KPIs; FOI if annex withheld",
        "source_id": "src_vl_pq_209_ontwikkelingsprojecten",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VLAIO>FIO>ONTW",
        "notes": "PQ209: province EUR public; individual project names confidential in answer; Excel bijlage not in PDF",
    },
    {
        "commitment_id": "cmt_woosh_vlaio_package",
        "title": "Woosh BV VLAIO innovation subsidy package (named L5)",
        "entity_id": "vlaio",
        "beneficiary": "Woosh BV diaper recycling startup",
        "legal_basis": "Multiple VLAIO instruments HBC/KMOGS/Schaalklaar",
        "decision_date": "2021-02-01",
        "start_year": "2021",
        "end_year": "2026",
        "total_envelope_eur": "980493",
        "cash_by_year": (
            '{"KMOGS_2021_0543":50000,"HBC_2021_0054_ONTW":158345.56,"HBC_2023_0447_haal":46160.07,'
            '"HBC_2023_1042_ONTW":375988,"HBC_2024_0916_schaalklaar":350000,"prov_OVL_circular":25000}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Circular diaper logistics and recycling scale-up",
        "cut_option": "Outcome KPIs tonnes recycled; path dependency check",
        "source_id": "src_vl_pq_351_woosh",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VLAIO>L5>Woosh",
        "notes": "PQ351 named codes+EUR; 3 closed positive; 2 ongoing; prov OVL separate 25k",
    },
    {
        "commitment_id": "cmt_moonshot_2024",
        "title": "Moonshot Flanders industry CO2 projects decided 2024",
        "entity_id": "vlaio",
        "beneficiary": "Knowledge institutions + industry partners ESI/LSI",
        "legal_basis": "Moonshot Catalisti programme FIO",
        "decision_date": "2024-01-01",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "24540891",
        "cash_by_year": '{"2024":24540891,"ESI_projects":8,"ESI_m":21100000,"LSI_projects":2,"LSI_m":3400000}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.moonshotflanders.be",
        "stated_goal": "Carbon-circular CO2-poor Flemish industry by 2050",
        "cut_option": "Publish full 10 project L5 names+EUR; additionality vs CIE",
        "source_id": "src_speurgids_2025_clusters",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VLAIO>Moonshot",
        "notes": "Speurgids Table28 strong aggregate; individual project names not in Speurgids table",
    },
    {
        "commitment_id": "cmt_cluster_earmarked_2024",
        "title": "Speerpuntcluster earmarked project package decided 2024",
        "entity_id": "vlaio",
        "beneficiary": "Catalisti BlauweCluster FlandersFood Flux50 Medvia SIM VIL intercluster",
        "legal_basis": "FIO geoormerkte cluster project middelen",
        "decision_date": "2024-01-01",
        "start_year": "2024",
        "end_year": "2024",
        "total_envelope_eur": "54200000",
        "cash_by_year": (
            '{"Catalisti":5310000,"BlauweCluster":10100000,"FlandersFood":6800000,"Flux50":7700000,'
            '"Medvia":2700000,"SIM":6200000,"VIL":1100000,"Intercluster":14200000,"projects":38}'
        ),
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "",
        "stated_goal": "Cluster competitiveness programmes collaborative innovation",
        "cut_option": "Open project L5 partner EUR lists; evaluate deadweight",
        "source_id": "src_speurgids_2025_clusters",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VLAIO>clusters>2024",
        "notes": "Speurgids Table18; intercluster partners knowledge-heavy 12.25m of 14.23m",
    },
    {
        "commitment_id": "cmt_edtech_station_vlaio",
        "title": "Edtech Station cluster VLAIO 1.8m over 3 years",
        "entity_id": "vlaio",
        "beneficiary": "Edtech Station (ITEC KU Leuven / Hangar K Kortrijk ecosystem)",
        "legal_basis": "Cluster decision innovative ecosystems",
        "decision_date": "2022-05-01",
        "start_year": "2022",
        "end_year": "2025",
        "total_envelope_eur": "1800000",
        "cash_by_year": '{"envelope_3y":1800000}',
        "remaining_eur": "",
        "status": "active",
        "evaluation_url": "https://www.edtechstation.be",
        "stated_goal": "Strengthen Flemish education technology ecosystem",
        "cut_option": "Outcome KPIs startups/jobs; sunset review",
        "source_id": "src_speurgids_2025_clusters",
        "confidence": "strong",
        "hierarchy_path": "Vlaanderen>VLAIO>ecosystems>Edtech",
        "notes": "Speurgids 4.5: 1.8m EUR for 3 years from May 2022",
    },
]

with (DATA / "commitments.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    fields = r.fieldnames
    rows = list(r)
ids = {x["commitment_id"] for x in rows}
for c in new_cmts:
    if c["commitment_id"] not in ids:
        rows.append({k: c.get(k, "") for k in fields})
with (DATA / "commitments.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
print("commitments", len(rows))

# --- leaderboard seeds ---
with (DATA / "leaderboard.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    lb_fields = r.fieldnames
    lb_rows = list(r)
lb_ids = {x["item_id"] for x in lb_rows}

def add_lb(item):
    if item["item_id"] not in lb_ids:
        row = {k: "" for k in lb_fields}
        row.update(item)
        lb_rows.append(row)
        lb_ids.add(item["item_id"])

add_lb(
    {
        "item_id": "lb_vlaio_innovatie_portfolio",
        "name": "VLAIO innovatiesteun OND+ONTW+ICON annual awards",
        "level": "Flanders",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>VLAIO>FIO>innovatie",
        "annual_cost_eur": "196895177",
        "total_cost_eur": "1273971102",
        "tco_notes": "2025 awards 196.9m; multi-year sum 2020-25 ~1.27bn from PQ177 series",
        "confidence": "strong",
        "source_id": "src_vl_pq_177_innovatie_limburg",
        "beneficiaries": "~390 projects / ~388 firms per year",
        "stated_goal": "Private R&D additionality",
        "measured_outcome": "Portfolio claims O&O spend/jobs up; VCO evaluation study pending",
        "absurdity_score": "3",
        "cost_score": "7.5",
        "difficulty": "5",
        "priority_index": "5.35",
        "cut_proposal": "Selectivity already tightening -12m; full L5 open data; additionality KPIs",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick108; steelman growth policy; opacity of full named register remains",
    }
)
add_lb(
    {
        "item_id": "lb_vlaio_ontw_cumul",
        "name": "VLAIO ontwikkelingsprojecten 5y cumulative",
        "level": "Flanders",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>VLAIO>FIO>ONTW",
        "annual_cost_eur": "88600000",
        "total_cost_eur": "443000000",
        "tco_notes": "443m over 2021-25 (~88.6m/yr avg); on 1.275bn project cost",
        "confidence": "strong",
        "source_id": "src_vl_pq_209_ontwikkelingsprojecten",
        "beneficiaries": "Companies R&D Flanders (bottom-up)",
        "stated_goal": "Near-market innovation",
        "measured_outcome": "PQ: names withheld confidentiality; Excel bijlage not public PDF",
        "absurdity_score": "3",
        "cost_score": "7",
        "difficulty": "5",
        "priority_index": "5.1",
        "cut_proposal": "Publish machine-readable project L5; FOI gap_vl_fio_project_l5",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick108; not pure waste — transparency gap",
    }
)
add_lb(
    {
        "item_id": "lb_moonshot_2024",
        "name": "Moonshot industrial decarbonisation research 2024 awards",
        "level": "Flanders",
        "type": "subsidy",
        "hierarchy_path": "Vlaanderen>VLAIO>Moonshot",
        "annual_cost_eur": "24540891",
        "total_cost_eur": "122704455",
        "tco_notes": "24.54m 2024; multi-year illustrative 5y",
        "confidence": "strong",
        "source_id": "src_speurgids_2025_clusters",
        "beneficiaries": "Knowledge institutions (10) + industry",
        "stated_goal": "Carbon-circular industry 2050",
        "measured_outcome": "10 projects aggregate only; project names not in Speurgids table",
        "absurdity_score": "3",
        "cost_score": "5.5",
        "difficulty": "5",
        "priority_index": "4.25",
        "cut_proposal": "Publish 10 project L5; coordinate with CIE industrial policy",
        "status": "seed",
        "struck_reason": "",
        "notes": "tick108 Speurgids",
    }
)

with (DATA / "leaderboard.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=lb_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(lb_rows)
print("leaderboard", len(lb_rows))

# --- FOI for bulk project L5 (jaarverslag lists + ONTW names) ---
gap_id = "gap_vl_fio_project_l5"
draft_path = ROOT / "foi" / "drafts" / f"{gap_id}.md"
draft_path.write_text(
    f"""# FOI draft — {gap_id}

**Status:** ready for human send (fill requester identity first)  
**gap_id:** {gap_id}  
**Recipient email:** openbaarheid@vlaanderen.be  
**Recipient body:** Vlaamse overheid — Team Openbaarheid / VLAIO (Fonds Innoveren en Ondernemen)  
**Address:** Havenlaan 88 bus 20 / Ellipsgebouw Koning Albert II-laan 35, 1030 Brussel  

---

## Brief (kopieer/plak)

```text
[NAAM VERZOEKER]
[ADRES]
[E-MAIL]
[TELEFOON]
[DATUM]

Aan: Vlaamse overheid
Team Openbaarheid van Bestuur
Herman Teirlinckgebouw
Havenlaan 88 bus 20
1000 Brussel
openbaarheid@vlaanderen.be

Betreft: Verzoek om openbaarmaking — L5-projecten en steunbedragen
VLAIO / Fonds Innoveren en Ondernemen (OND, ONTW, ICON, clusters, Moonshot)
Intern dossier: {gap_id} (AIpolitics / DOGE research)

Geachte,

Op grond van de toepasselijke regels inzake openbaarheid van bestuur
(Bestuursdecreet e.a.) dien ik hierbij een verzoek in tot openbaarmaking
van de hieronder omschreven bestuursdocumenten.

### 1. Voorwerp van het verzoek

1. De **lijsten van gesteunde rechtspersonen** zoals opgenomen als bijlage bij
   de VLAIO-jaarverslagen **2024 en 2025** (of machineleesbare export), met
   per toekenning minstens: begunstigde, KBO, instrument, projectcode,
   steunbedrag (EUR), beslissingsjaar.

2. Voor **onderzoeksprojecten (OND), ontwikkelingsprojecten (ONTW) en ICON**
   in beslissingsjaren **2023, 2024 en 2025**: een overzicht met projectnaam
   of -code, begunstigde(n), toegekende steun, en indien beschikbaar
   projectkost en steunpercentage.

3. Voor **Moonshot 2024** (10 projecten, ca. 24,54 miljoen euro): naam/code
   en steunbedrag per project.

4. Voor **speerpuntcluster-projecten 2024** op geoormerkte middelen
   (ca. 54,2 miljoen euro): projectcode/naam, cluster, steunbedrag en
   hoofdpartners voor zover bijgehouden.

5. Eventuele **open data / ICAROS-KRIS export** of andere publieke registers
   die bovenstaande reeds publiceren (URL + extractiedatum).

Periode: beslissingsjaren 2023–2025 (en 2026 indien al beschikbaar).

### 2. Context

Aggregaten zijn publiek (o.a. Speurgids 2025; parlementaire antwoorden:
innovatiesteun OND+ONTW+ICON 2025 ca. 196,9 miljoen euro; ONTW 2021–2025
443 miljoen euro). Individuele project-L5 is deels vertrouwelijk verklaard
in SV 209 (ontwikkelingsprojecten West-Vlaanderen). De jaarverslagbijlagen
“gesteunde rechtspersonen” worden op vlaio.be vermeld maar zijn voor
automatische toegang niet betrouwbaar ophaalbaar. Dit verzoek kadert in
transparantieonderzoek naar publieke middelen.
Hiërarchisch pad: Vlaanderen > VLAIO > FIO > project_L5.

### 3. Vorm

Bij voorkeur: PDF + machineleesbare CSV/XLSX per e-mail naar [E-MAIL].
Indien gedeeltelijke weigering: gemotiveerde beslissing met rechtsgrond.

### 4. Identiteit

Naam: […]
Hoedanigheid: […]
Dossierreferentie intern: {gap_id}

Met vriendelijke groet,

[Naam]
```

**Niet verzonden door agent.**
""",
    encoding="utf-8",
)

with (DATA / "foi_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    foi_fields = r.fieldnames
    foi_rows = list(r)
if not any(x["gap_id"] == gap_id for x in foi_rows):
    row = {k: "" for k in foi_fields}
    row.update(
        {
            "gap_id": gap_id,
            "hierarchy_path": "Vlaanderen>VLAIO>FIO>project_L5",
            "entity_id": "vlaio",
            "what_is_missing": (
                "Machine-readable L5 lists OND/ONTW/ICON/Moonshot/cluster projects "
                "with names amounts 2023-2025 (jaarverslag annex + registers)"
            ),
            "why_it_matters": (
                "Awards ~197-214m/yr innovatiesteun; aggregates public; bulk project L5 opaque"
            ),
            "priority": "7",
            "recipient_body": "Vlaamse overheid Team Openbaarheid / VLAIO FIO",
            "recipient_email": "openbaarheid@vlaanderen.be",
            "recipient_postal": "Havenlaan 88 bus 20 1000 Brussel",
            "draft_letter_path": f"docs/doge/foi/drafts/{gap_id}.md",
            "status": "ready",
            "date_ready": "2026-07-27",
            "linked_commitment_id": "cmt_vlaio_innovatie_portfolio_2025",
            "linked_leaderboard_id": "lb_vlaio_innovatie_portfolio",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "rq_108; sample L5 found (Woosh clusters Moonshot); bulk FOI human send",
        }
    )
    foi_rows.append(row)
with (DATA / "foi_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=foi_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(foi_rows)
print("foi ok")

# --- research_queue ---
with (DATA / "research_queue.csv").open(newline="", encoding="utf-8") as f:
    r = csv.DictReader(f)
    rq_fields = r.fieldnames
    rq_rows = list(r)
for row in rq_rows:
    if row["task_id"] == "rq_108":
        row["status"] = "done"
        row["blocked_gap_id"] = gap_id
        row["updated_utc"] = UTC
        row["notes"] = (
            "tick108: innovatiesteun 2025 196.9m/388 firms; ONTW 5y 443m; Woosh 5 named L5; "
            "Moonshot 24.54m; clusters 54.2m; FOI bulk gap_vl_fio_project_l5 ready"
        )
# spawn next public unit
if not any(r["task_id"] == "rq_109" for r in rq_rows):
    rq_rows.append(
        {
            "task_id": "rq_109",
            "title": "FPS FFS or taxex inventory micro-update or federal L5",
            "sprint": "continuous",
            "priority": "3",
            "status": "open",
            "hierarchy_target": "taxex",
            "entity_id": "fod_finance",
            "instructions": (
                "Recheck FPS fossil fuel subsidy inventory or other federal primary L5 "
                "if new edition; else pick one opaque FOI-ready gap to deepen publicly."
            ),
            "blocked_gap_id": "",
            "created_utc": UTC,
            "updated_utc": UTC,
            "notes": "After Speurgids/VLAIO map; keep federal taxex current",
        }
    )
with (DATA / "research_queue.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rq_fields, lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rq_rows)
print(
    "rq",
    [(r["task_id"], r["status"], r["priority"]) for r in rq_rows if r["status"] in ("open", "blocked_foi", "done") and r["task_id"].startswith("rq_10")],
)

# --- loop_state ---
with (DATA / "loop_state.csv").open("w", newline="", encoding="utf-8") as f:
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
            "continuous",
            UTC,
            "rq_108",
            108,
            "no",
            "tick108 VLAIO innovatiesteun L5 sample; FOI bulk ready. Next: rq_109 or rq_107; human FOI CIE+FIO.",
        ]
    )

# --- log ---
with (ROOT / "loop_log.md").open("a", encoding="utf-8") as f:
    f.write(
        f"""
### {UTC} — tick 108
- Unit: **rq_108** (VLAIO FIO bedrijfssteun O&O named L5 / open data)
- Found (strong aggregates + partial named L5; bulk list FOI):
  - **PQ177** innovatiesteun OND+ONTW+ICON decision-year: Flanders **2025 €196.90m** (388 firms / 390 projects); multi-year path 2020–25 public; full portfolio incl ISS/Schaalklaar/haalbaarheid **€214.15m** 2025.
  - **PQ209** ontwikkelingsprojecten only: **€443m** 2021–25 on **€1.275bn** project cost (~35% avg); 918/1093 approved 2023–25; province split ANT 110.9 / OV 132.5 / WVL 79.3 / VBR 70.3 / LIM 38.0 / other 12.0 mEUR. Individual project names **withheld for confidentiality** (Excel bijlage not in PDF).
  - **PQ351 named L5 Woosh**: KMOGS €50k; ONTW €158.3k + €376.0k; haalbaarheid €46.2k; Schaalklaar €350k (codes public).
  - **Speurgids 2025**: speerpuntcluster geoormerkt **€54.2m** / 38 projects 2024 (Catalisti 5.31 … Intercluster 14.2); **Moonshot €24.54m** / 10 projects; Edtech Station **€1.8m**/3y.
  - VLAIO.be jaarverslag annex media/3057 still **403 blocked** for agent download.
- Wrote: sources +4; programmes +5; commitments +6 L5; leaderboard +3; **FOI gap_vl_fio_project_l5 ready**; rq_108=done; spawned rq_109; raw PQs; ticks=108
- FOI opened: **gap_vl_fio_project_l5** → ready (human send; complements gap_vl_cie_l5)
- Next: **rq_109** federal TE/FFS recheck or **rq_107** SWA year-end (low)
"""
    )
print("DONE tick108")
