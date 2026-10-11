from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2464_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_zonnekindjes_jr2025_nbb_pdf_2464"
SRC_KBO="src_zonnekindjes_kbo_2464"
SRC_SBM="src_zonnekindjes_sbm_2464"
SRC_SITE="src_zonnekindjes_site_2464"
EID="vzw_zonnekindjes_diepenbeek"
GAP="gap_zonnekindjes_opgroeien_matrix_opbr_2_02m_omzet_605k_73_1_40m_destin_drop_100k_l5"
COMM="comm_zonnekindjes_jr2025_statutory_opbr_2_02m_omzet_605k_destin_drop_100k"
LB="lb_zonnekindjes_opbr_2_02m_omzet_605k_73_1_40m_destin_drop_100k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 DE ZONNEKINDJES deposit 2026-00135397,http://cdn.staatsbladmonitor.be/2026pdf/2026-00135397.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2464; official native PDF 45628 bytes 10p MIC-VZW 25.0.12 m08-f; header 03.06.2026; AV 26.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-04 00:32:29 UTC OpenPDF 1.3.26; all 10p native; CDN 2026-00135397 HEAD 200 Last-Modified 11.06.2026; MIC-VZW 6.1.1 6.1.3 6.2 6.3 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO DE ZONNEKINDJES 0416.541.952,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0416541952,KBO Public Search FOD Economie,{DAY},official_register,tick2464; Actief; 1 VE 2.150.890.470 PeutertuinZonnekindjes vzw Kloosterstraat 1E 3590 Diepenbeek since 03.01.2006; VZW since 05.10.1976; begindatum 05.10.1976; zetel Kloosterstraat 1E 3590 Diepenbeek since 01.11.2020; Werkgever RSZ since 01.10.1976; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI kinderdagverblijf@zonnekindjes.be; leftover mined city_diepenbeek CIK; NOT D'n Opvang 0676.442.465 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine",
f"{SRC_SBM},NBB Consult / SBM fiche DE ZONNEKINDJES 0416541952 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0416541952,NBB Consult / SBM,{DAY},official_register,tick2464; deposit-id 2026-00135397 YE 01.01.2025-31.12.2025 filing 04.06.2026 published 04.06.2026 MIC-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},DE ZONNEKINDJES FOI contact leftover city_diepenbeek CIK,https://zonnekindjes.be/,VZW DE ZONNEKINDJES leftover city_diepenbeek CIK Opgroeien groepsopvang,{DAY},foi_contact,tick2464; FOI kinderdagverblijf@zonnekindjes.be; zetel + 1 VE Kloosterstraat 1E 3590 Diepenbeek; 1 VE leftover mined city_diepenbeek after D'n Opvang different-city skip; NOT Kloosterstraat 6 Drongen De Elfjes remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},DE ZONNEKINDJES,ASBL DE ZONNEKINDJES,De Zonnekindjes VZW (leftover city_diepenbeek CIK),parastatal,city_diepenbeek,nl,https://zonnekindjes.be/,kinderdagverblijf@zonnekindjes.be,Kloosterstraat 1E 3590 Diepenbeek,tick2464 YE2025 Strong official native NBB PDF deposit 2026-00135397 + Strong KBO 0416.541.952 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 JUMP 605224 commercial-only; 73 JUMP 1400630; 76A JUMP 9315; envelope 70/76A JUMP 2015169; bruto JUMP 1377639; pnl JUMP 144298; 9901 JUMP 132596; equity JUMP 1360542; assets JUMP 1587086; debt DROP 226544; FTE 23.0 JUMP; kapitaalsubsidies DROP 310061; destin691 DROP 100480; 791 empty; cash JUMP 764804; geldbeleggingen DROP 242524 was 591188; leftover mined city_diepenbeek after D'n Opvang different-city skip; 1 VE CIK groepsopvang not private; NOT Kloosterstraat 6 Drongen De Elfjes remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ooievaarsnest 0418.588.256 leftover city_tienen unused YE2025 2026-00113832; NOT Paideia 0445.129.931 leftover city_brugge unused YE2025 2026-00259827; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_zonnekindjes_omzet_jr2025_statutory,{EID},2025,605224,605224,605224,NBB MIC-VZW code 70 omzet YE2025 JUMP +0.48% (commercial-only vs large 73),{SRC_PDF},strong,tick2464; PDF p5 native; YE2024 identical 602336; 73 1400630; 76A 9315",
f"bud_zonnekindjes_73_jr2025_statutory,{EID},2025,1400630,1400630,1400630,NBB MIC-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +1.42%,{SRC_PDF},strong,tick2464; PDF p5 native; YE2024 identical 1380961; FOI Opgroeien matrix behind 73 1400630",
f"bud_zonnekindjes_opbr_jr2025_statutory,{EID},2025,2015169,2015169,2015169,NBB MIC-VZW envelope 70/76A YE2025 JUMP +1.16% (omzet 70 605224 commercial-only + 73 1400630 + 76A 9315),{SRC_PDF},strong,tick2464; PDF p5 native; YE2024 identical 1992044; envelope remains 70/76A because omzet not empty",
f"bud_zonnekindjes_bruto_jr2025_statutory,{EID},2025,1377639,1377639,1377639,NBB MIC-VZW code 9900 brutomarge YE2025 JUMP +1.01% (MIC present; envelope remains 70/76A because omzet not empty),{SRC_PDF},strong,tick2464; PDF p5 native; YE2024 identical 1363916; 76A 9315",
f"bud_zonnekindjes_pnl_jr2025_statutory,{EID},2025,144298,144298,144298,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 JUMP +1.12% (was 142695),{SRC_PDF},strong,tick2464; PDF p5 native; YE2024 identical 142695; bedrijfswinst 9901 132596 JUMP; destin691 100480 DROP not full pnl",
f"bud_zonnekindjes_bedrijfswinst_jr2025_statutory,{EID},2025,132596,132596,132596,NBB MIC-VZW code 9901 bedrijfswinst YE2025 JUMP +1.02% (was 131253),{SRC_PDF},strong,tick2464; PDF p5 native; YE2024 identical 131253; 62 1187954 JUMP; 630 49408 DROP; 66A 4533 JUMP",
f"bud_zonnekindjes_equity_jr2025_statutory,{EID},2025,1360542,1360542,1360542,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +10.43%,{SRC_PDF},strong,tick2464; PDF p4 native; YE2024 identical 1232089; kapitaalsubsidies 310061 DROP; overgedragen 14 784533 JUMP; fondsen 10 49579 FLAT; bestemde fondsen 13 216369 JUMP",
f"bud_zonnekindjes_assets_jr2025_statutory,{EID},2025,1587086,1587086,1587086,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +6.90%,{SRC_PDF},strong,tick2464; PDF p3 native; YE2024 identical 1484677; MVA 22/27 445211 DROP; cash 764804 JUMP; geldbeleggingen 242524 DROP; aanbouw 27 empty",
f"bud_zonnekindjes_debt_jr2025_statutory,{EID},2025,226544,226544,226544,NBB MIC-VZW code 17/49 schulden YE2025 DROP -10.31%,{SRC_PDF},strong,tick2464; PDF p4 native; YE2024 identical 252588; 17 empty; 42/48 224487 DROP",
f"bud_zonnekindjes_cash_jr2025_statutory,{EID},2025,764804,764804,764804,NBB MIC-VZW code 54/58 liquide middelen YE2025 JUMP +176.59%,{SRC_PDF},strong,tick2464; PDF p3 native; YE2024 identical 276514; geldbeleggingen 50/53 242524 DROP was 591188",
f"bud_zonnekindjes_destin_jr2025_statutory,{EID},2025,100480,100480,100480,NBB MIC-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -13.30% (not full pnl 144298; remainder 43818 to overgedragen 14; 13 JUMP 216369),{SRC_PDF},strong,tick2464; PDF p6 native; YE2024 destin 115888; bestemde fondsen 13 216369 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":605224,\"\"2025_73\"\":1400630,\"\"2025_76A\"\":9315,"
"\"\"2025_opbr70_76A\"\":2015169,\"\"2025_bruto\"\":1377639,"
"\"\"2025_pnl\"\":144298,\"\"2025_bedrijfswinst\"\":132596,"
"\"\"2025_equity\"\":1360542,\"\"2025_assets\"\":1587086,\"\"2025_debt\"\":226544,"
"\"\"2025_fte\"\":23.0,\"\"2025_kapitaalsubsidies\"\":310061,\"\"2025_destin691\"\":100480,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":764804,\"\"2025_geldbeleggingen\"\":242524,"
"\"\"2025_personnel62\"\":1187954,\"\"2025_gebouwen22\"\":323869,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":4533,"
"\"\"2025_fondsen10\"\":49579,\"\"2025_overgedragen14\"\":784533,"
"\"\"2025_bestemdefondsen13\"\":216369,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":49408,\"\"2025_capex\"\":10789,"
"\"\"2024_omzet\"\":602336,\"\"2024_73\"\":1380961,"
"\"\"2024_opbr70_76A\"\":1992044,\"\"2024_bruto\"\":1363916,\"\"2024_pnl\"\":142695,\"\"2024_bedrijfswinst\"\":131253,"
"\"\"2024_equity\"\":1232089,\"\"2024_assets\"\":1484677,"
"\"\"2024_debt\"\":252588,\"\"2024_cash\"\":276514,\"\"2024_fte\"\":22.4,"
"\"\"2024_destin691\"\":115888,\"\"2024_kapitaalsubsidies\"\":325907,\"\"2024_76A\"\":8747,"
"\"\"2024_geldbeleggingen\"\":591188}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},DE ZONNEKINDJES YE2025 (opbr JUMP 2.02m / omzet JUMP 605k commercial-only / 73 JUMP 1.40m / destin DROP 100k / Strong PDF),{EID},Opgroeien + leftover city_diepenbeek CIK,VZW DE ZONNEKINDJES (KBO 0416.541.952; Actief; 1 VE; RSZ2025 88.911; zetel + 1/1 VE Diepenbeek),2026-05-26,2025,2025,2015169,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00135397.pdf,Public CIK dual of mined city_diepenbeek,Publish Opgroeien matrix behind envelope 2.02m + why omzet 605k commercial-only vs 73 1.40m and why destin DROP 100k while pnl JUMP 144k and cash JUMP 765k,{SRC_PDF},strong,Vlaanderen>Limburg>Diepenbeek>Zonnekindjes>JR2025_statutory_L5,tick2464; Strong official native PDF; leftover mined city_diepenbeek CIK; 1 VE; NOT every-10; NOT Kloosterstraat 6 Drongen De Elfjes remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Zonnekindjes opbr JUMP 2.02m / omzet JUMP 605k commercial-only / 73 JUMP 1.40m / destin DROP 100k (YE2025 leftover city_diepenbeek CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Limburg>Diepenbeek>Zonnekindjes>JR2025",
"2015169",
"2015169",
"PDF envelope 70/76A 2015169; 70 605224 commercial-only; 73 1400630; 76A 9315; bruto 1377639; bedrijfswinst JUMP 132596; pnl JUMP 144298; equity JUMP 1360542; assets JUMP 1587086; debt DROP 226544; FTE 23.0 JUMP; kapitaalsubsidies DROP 310061; destin691 DROP 100480; cash JUMP 764804; geldbeleggingen DROP 242524 was 591188; 1 VE leftover city_diepenbeek CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_diepenbeek CIK",
"CIK / Kind en Gezin groepsopvang leftover city_diepenbeek",
"2.02m envelope; omzet 605k commercial-only vs 73 1.40m; destin DROP 100k; cash JUMP 765k; leftover city_diepenbeek CIK",
"5.16",
"5.14",
"5.05",
"5.13",
"FOI Opgroeien matrix behind envelope 2.02m + why omzet 605k commercial-only vs 73 1.40m and why destin DROP 100k while pnl JUMP 144k and cash JUMP 765k and FTE 23.0",
"active",
"",
"tick2464 leftover mined city_diepenbeek CIK after D'n Opvang different-city skip; 1 VE; NOT every-10; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Limburg>Diepenbeek>Zonnekindjes>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 2015169 (omzet 70 605224 commercial-only + 73 1400630 + 76A 9315) and why destin DROP 100480 while pnl JUMP 144298 and cash JUMP 764804 and geldbeleggingen DROP 242524 (was 591188) and FTE 23.0",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_diepenbeek; MIC envelope 70/76A 2.02m because omzet commercial-only vs large 73; public Opgroeien groepsopvang PeutertuinZonnekindjes",
"priority": "8",
"recipient_body": "VZW DE ZONNEKINDJES / Raad van Bestuur",
"recipient_email": "kinderdagverblijf@zonnekindjes.be",
"recipient_postal": "Kloosterstraat 1E 3590 Diepenbeek",
"draft_letter_path": f"docs/doge/foi/drafts/{GAP}.md",
"status": "ready",
"date_ready": DAY,
"date_sent": "",
"date_due": "",
"date_answered": "",
"response_summary": "",
"linked_commitment_id": COMM,
"linked_leaderboard_id": LB,
"created_utc": STAMP,
"updated_utc": STAMP,
"notes": "tick2464; ready NOT sent; Strong official native NBB PDF; leftover mined city_diepenbeek CIK after D'n Opvang different-city skip; 1 VE; NOT every-10; off Drongen De Elfjes remine",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2464,")!=1: raise SystemExit(f"bad 2464 count {rq_raw.count(b'rq_2464,')}")
if b"rq_2465," in rq_raw: raise SystemExit("2465 exists")
idx=rq_raw.rfind(b"rq_2464,")
if idx<0: raise SystemExit("rq_2464 not found")
new_2464=(
"rq_2464,leftover dual DE ZONNEKINDJES YE2025,hole_fill,8,done,L5,vzw_zonnekindjes_diepenbeek,"
"Took unused leftover public CIK DE ZONNEKINDJES 0416.541.952 leftover mined city_diepenbeek. Official NBB MIC-VZW YE2025 2026-00135397 native 10p. Envelope 70/76A JUMP 2015169 (omzet 605224 commercial-only + 73 1400630 + 76A 9315); pnl JUMP 144298; destin DROP 100480; cash JUMP 764804. NOT D'n Opvang remine. NOT De Elfjes remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2464 leftover mined city_diepenbeek CIK; Strong native PDF; 1 VE; next every-10 is 2470\n"
)
new_2465=(
"rq_2465,leftover dual after DE ZONNEKINDJES — hunt unused public dual,hole_fill,8,open,L5,,"
"After DE ZONNEKINDJES YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Ooievaarsnest 0418.588.256 leftover city_tienen YE2025 2026-00113832 CDN 200 51kB — take ONLY if unused + official native-text YE2025 PDF. Paideia 0445.129.931 leftover city_brugge YE2025 2026-00259827 CDN 200 54kB — take ONLY if unused + official native-text YE2025 PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.,"
f",{STAMP},{STAMP},spawned after tick2464; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2464.count("\n")!=1 or new_2465.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2464.encode("utf-8"))
    f.write(new_2465.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2464", chk.count(b"rq_2464,"), "n2465", chk.count(b"rq_2465,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2464,2464,no,tick2464 leftover dual DE ZONNEKINDJES 0416.541.952 Strong native PDF (omzet70 JUMP 605224 commercial-only; 73 JUMP 1400630; 76A JUMP 9315; envelope 70/76A JUMP 2015169; pnl JUMP 144298; 9901 JUMP 132596; equity JUMP 1360542; assets JUMP 1587086; debt DROP 226544; FTE 23.0 JUMP; kapitaalsubsidies DROP 310061; destin691 DROP 100480; 791 empty; cash JUMP 764804; geldbeleggingen DROP 242524 was 591188; 1 VE leftover city_diepenbeek CIK); leftover mined city_diepenbeek CIK; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; next every-10 is 2470; next rq_2465 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2464 - rq_2464 DE ZONNEKINDJES (opbr JUMP 2.02m / omzet JUMP 605k commercial-only / 73 JUMP 1.40m / destin DROP 100k / Strong PDF)

- Unit: **rq_2464** leftover dual after **D'n Opvang@2463**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. D'n Opvang 0676.442.465 just mined — do not remine. CAR Overleie just mined — do not remine. Gesticht just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW DE ZONNEKINDJES** YE2025 (KBO **0416.541.952**; zetel Kloosterstraat 1E 3590 Diepenbeek; **Actief** **1 VE** **2.150.890.470** PeutertuinZonnekindjes vzw Kloosterstraat 1E since 03.01.2006; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover of mined **city_diepenbeek**; kinderdagverblijf@zonnekindjes.be). Identity trap: DE ZONNEKINDJES 0416.541.952 ≠ D'n Opvang **0676.442.465** leftover city_oostende just mined; ≠ De Elfjes **0455.636.912** already mined; ≠ De Steijgertjes **0413.421.720** already mined; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ Ooievaarsnest **0418.588.256** leftover city_tienen unused YE2025; ≠ Paideia **0445.129.931** leftover city_brugge unused YE2025; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved. 1 VE Diepenbeek — leftover of mined city_diepenbeek (zetel + 1/1 VE). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergunde; PeutertuinZonnekindjes) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not D'n Opvang remine / not De Elfjes remine. MIC-VZW **native text** (not scan) — 45628 B / 10p all native euros (MIC-VZW 6.1.1 / 6.1.3 / 6.2 / 6.3 / 7 / 8 niet dienstig).
- Found: official NBB MIC-VZW native PDF deposit **2026-00135397** (45628 B / 10p; AV **26.05.2026**; header **03.06.2026**; CDN Last-Modified **11.06.2026**; CreationDate 04.06.2026 OpenPDF 1.3.26; all 10p native; prior-year identical not restated) — omzet 70 **EUR605224** JUMP +0.48% (commercial-only vs large 73; was 602336); 73 **EUR1400630** JUMP +1.42% (was 1380961); 76A **EUR9315** JUMP +6.49% (was 8747); envelope 70/76A **EUR2015169** JUMP +1.16% (70+73+76A; was 1992044); bruto 9900 **EUR1377639** JUMP +1.01% (MIC present; envelope remains 70/76A because omzet not empty; was 1363916); 62 **EUR1187954** JUMP +1.04%; 630 **EUR49408** DROP −0.22%; 66A **EUR4533** JUMP +8.21%; 640/8 **EUR3148** DROP −1.10%; 635/9 **empty**; bedrijfswinst 9901 **EUR132596** JUMP +1.02%; pnl 9904 **EUR144298** JUMP +1.12%; equity **EUR1360542** JUMP +10.43%; assets **EUR1587086** JUMP +6.90%; debt **EUR226544** DROP −10.31%; FTE **23.0** JUMP +2.68% (was 22.4; 100 23.0; 105 20.3); kapitaalsubsidies **EUR310061** DROP −4.86%; destin 691 **EUR100480** DROP −13.30% (not full pnl 144298; remainder 43818 to overgedragen 14; 13 JUMP 216369); 791 **empty**; cash **EUR764804** JUMP +176.59%; geldbeleggingen **EUR242524** DROP −58.98% (was 591188); gebouwen **EUR323869** DROP; MVA 22/27 **EUR445211** DROP; aanbouw **empty**; capex **EUR10789**; fondsen 10 **EUR49579** FLAT; overgedragen 14 **EUR784533** JUMP; bestemde fondsen 13 **EUR216369** JUMP; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_diepenbeek CIK. NOT Kloosterstraat 6 Drongen De Elfjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.13); entities (+1 vzw_zonnekindjes_diepenbeek); foi + draft `gap_zonnekindjes_opgroeien_matrix_opbr_2_02m_omzet_605k_73_1_40m_destin_drop_100k_l5`; rq_2464=done + rq_2465 open; loop_state ticks=2464; raw tick2464/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2465 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved). NOW leftover candidate: Ooievaarsnest 0418.588.256 leftover city_tienen unused YE2025 **2026-00113832** CDN **200** 51kB — take ONLY if unused + official native-text YE2025 PDF. Paideia 0445.129.931 leftover city_brugge unused YE2025 **2026-00259827** CDN **200** 54kB — take ONLY if unused + official native-text YE2025 PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
