from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2470_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_infano_jr2025_nbb_pdf_2470"
SRC_KBO="src_infano_kbo_2470"
SRC_SBM="src_infano_sbm_2470"
SRC_SITE="src_infano_site_2470"
EID="vzw_infano_ternat"
GAP="gap_infano_opgroeien_matrix_opbr_46_52m_omzet_14_46m_73_31_07m_pnl_jump_866k_destin_300k_l5"
COMM="comm_infano_jr2025_statutory_opbr_46_52m_omzet_14_46m_73_31_07m_pnl_jump_866k"
LB="lb_infano_opbr_46_52m_omzet_14_46m_73_31_07m_pnl_jump_866k_destin_300k_jr2025"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 INFANO deposit 2026-00205409,http://cdn.staatsbladmonitor.be/2026pdf/2026-00205409.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2470; official native PDF 559435 bytes 42p VOL-VZW 25.0.13 m05-f; header 26.06.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-27 00:04:37 UTC OpenPDF 1.3.26; all 42p native; CDN 2026-00205409 GET 200 Last-Modified 10.07.2026; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.3.6 6.4.1 6.4.2 6.5.1 6.5.2 6.5.3 6.14 6.16 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO INFANO 0477.578.411,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0477578411,KBO Public Search FOD Economie,{DAY},official_register,tick2470; Actief; 86 VE; VZW since 11.03.2002; begindatum 11.03.2002; zetel Keizerstraat 35 1740 Ternat since 11.03.2002; vervangt 0852.017.514 afgesloten 29.11.2012; FOI info@infano.be; leftover mined city_ternat CIK; NOT Vijverbeek Asse 0448.164.744 remine; NOT Savio Dilbeek 0472.564.501 remine",
f"{SRC_SBM},NBB Consult / SBM fiche INFANO 0477578411 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0477578411,NBB Consult / SBM,{DAY},official_register,tick2470; deposit-id 2026-00205409 YE 01.01.2025-31.12.2025 filing 26.06.2026 published 26.06.2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},INFANO FOI contact leftover city_ternat CIK,https://www.infano.be/,VZW INFANO leftover city_ternat CIK Opgroeien groepsopvang 86 VE,{DAY},foi_contact,tick2470; FOI info@infano.be; zetel Keizerstraat 35 1740 Ternat; 86 VE leftover mined city_ternat after Vijverbeek different-city skip; NOT Vijverbeek remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT Savio remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT t Zonnetje; NOT Ferm Kinderopvang remine",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},INFANO,ASBL INFANO,INFANO VZW (leftover city_ternat CIK),parastatal,city_ternat,nl,https://www.infano.be/,info@infano.be,Keizerstraat 35 1740 Ternat,tick2470 YE2025 Strong official native NBB PDF deposit 2026-00205409 + Strong KBO 0477.578.411 Actief 86 VE; omzet70 JUMP 14460807 commercial-only; 73 JUMP 31066744; 76A JUMP 21687; envelope 70/76A JUMP 46522446; VOL no 9900; pnl JUMP 866039; 9901 JUMP 852477; equity JUMP 11477684; assets JUMP 24585792; debt DROP 11296111; FTE JUMP 671.2; kapitaalsubsidies DROP 1403474; destin691 JUMP 300000; 791 empty; cash DROP 8616420; geldbeleggingen DROP 2650000; leftover city_ternat CIK 86 VE; NOT Vijverbeek Asse 0448.164.744 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine (Infano VE Zonnetje Dilbeek 2.150.843.851 at Stationsstraat 277 is different KBO); NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT t Zonnetje; NOT ZONNESTRAAL; NOT Zonnestraal Junior; Hupskadee 0863.886.651 leftover city_begijnendijk year TBD not taken; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_infano_omzet_jr2025_statutory,{EID},2025,14460807,14460807,14460807,NBB VOL-VZW code 70 omzet YE2025 JUMP +9.51% (commercial-only vs large 73; envelope is 70/76A),{SRC_PDF},strong,tick2470; PDF p7 native; YE2024 13205344; 73 31066744 JUMP",
f"bud_infano_73_jr2025_statutory,{EID},2025,31066744,31066744,31066744,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +16.24% (code 733 subsidies all of 73),{SRC_PDF},strong,tick2470; PDF p7+p21 native; YE2024 26725259; FOI Opgroeien split behind envelope 46522446",
f"bud_infano_opbr_jr2025_statutory,{EID},2025,46522446,46522446,46522446,NBB VOL-VZW envelope 70/76A YE2025 JUMP +14.00% (omzet 14460807 commercial-only + 73 31066744 + 72 526350 + 74 446858 + 76A 21687),{SRC_PDF},strong,tick2470; PDF p7 native; YE2024 40810259; VOL no 9900; envelope is 70/76A because omzet not empty",
f"bud_infano_76A_jr2025_statutory,{EID},2025,21687,21687,21687,NBB VOL-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 JUMP +75.26% (VOL no 9900; envelope remains 70/76A),{SRC_PDF},strong,tick2470; PDF p7 native; YE2024 12374; 72 526350; 74 446858",
f"bud_infano_pnl_jr2025_statutory,{EID},2025,866039,866039,866039,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 JUMP +37.99% (was 627606),{SRC_PDF},strong,tick2470; PDF p8 native; YE2024 627606; bedrijfswinst 9901 852477 JUMP; destin691 JUMP 300000",
f"bud_infano_bedrijfswinst_jr2025_statutory,{EID},2025,852477,852477,852477,NBB VOL-VZW code 9901 bedrijfswinst YE2025 JUMP +34.40% (was 634263),{SRC_PDF},strong,tick2470; PDF p7 native; YE2024 634263; 62 32733570 JUMP; 630 1519514 JUMP; 66A 495; 640/8 71533; 635/9 1016269 JUMP; 631/4 23481 JUMP",
f"bud_infano_equity_jr2025_statutory,{EID},2025,11477684,11477684,11477684,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +6.09%,{SRC_PDF},strong,tick2470; PDF p6 native; YE2024 10818841; kapitaalsubsidies 1403474 DROP; overgedragen 14 5316548 JUMP; fondsen 10 432663 FLAT; bestemde fondsen 13 4325000 JUMP",
f"bud_infano_assets_jr2025_statutory,{EID},2025,24585792,24585792,24585792,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +6.60%,{SRC_PDF},strong,tick2470; PDF p5 native; YE2024 23063036; MVA 22/27 10367065 JUMP; cash 8616420 DROP; geldbeleggingen 2650000 DROP; aanbouw 27 empty",
f"bud_infano_debt_jr2025_statutory,{EID},2025,11296111,11296111,11296111,NBB VOL-VZW code 17/49 schulden YE2025 DROP -1.50%,{SRC_PDF},strong,tick2470; PDF p6 native; YE2024 11468468; 17 583154 DROP; 42/48 10097814 FLAT",
f"bud_infano_cash_jr2025_statutory,{EID},2025,8616420,8616420,8616420,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -0.82%,{SRC_PDF},strong,tick2470; PDF p5 native; YE2024 8687566; geldbeleggingen 50/53 2650000 DROP",
f"bud_infano_destin_jr2025_statutory,{EID},2025,300000,300000,300000,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +50.00% (300000 vs pnl 866039; 791 empty; 14 JUMP 5316548 = prior 4750509 + pnl 866039 - destin 300000),{SRC_PDF},strong,tick2470; PDF p9 native; YE2024 destin 200000; bestemde fondsen 13 4325000 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":14460807,\"\"2025_73\"\":31066744,\"\"2025_76A\"\":21687,"
"\"\"2025_opbr70_76A\"\":46522446,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":866039,\"\"2025_bedrijfswinst\"\":852477,"
"\"\"2025_equity\"\":11477684,\"\"2025_assets\"\":24585792,\"\"2025_debt\"\":11296111,"
"\"\"2025_fte\"\":671.2,\"\"2025_kapitaalsubsidies\"\":1403474,\"\"2025_destin691\"\":300000,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":8616420,\"\"2025_geldbeleggingen\"\":2650000,"
"\"\"2025_personnel62\"\":32733570,\"\"2025_gebouwen22\"\":3313626,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":495,"
"\"\"2025_fondsen10\"\":432663,\"\"2025_overgedragen14\"\":5316548,"
"\"\"2025_bestemdefondsen13\"\":4325000,"
"\"\"2025_voorzieningen16\"\":1811996,\"\"2025_630\"\":1519514,\"\"2025_capex\"\":2195142,"
"\"\"2024_omzet\"\":13205344,\"\"2024_73\"\":26725259,"
"\"\"2024_opbr70_76A\"\":40810259,\"\"2024_bruto\"\":0,\"\"2024_pnl\"\":627606,\"\"2024_bedrijfswinst\"\":634263,"
"\"\"2024_equity\"\":10818841,\"\"2024_assets\"\":23063036,"
"\"\"2024_debt\"\":11468468,\"\"2024_cash\"\":8687566,\"\"2024_fte\"\":618,"
"\"\"2024_destin691\"\":200000,\"\"2024_kapitaalsubsidies\"\":1610669,\"\"2024_76A\"\":12374,"
"\"\"2024_geldbeleggingen\"\":2700000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},INFANO YE2025 (opbr JUMP 46.52m / omzet JUMP 14.46m commercial-only / 73 JUMP 31.07m / pnl JUMP 866k / destin JUMP 300k / Strong PDF),{EID},Opgroeien + leftover city_ternat CIK,VZW INFANO (KBO 0477.578.411; Actief; 86 VE; zetel Ternat),2026-06-25,2025,2025,46522446,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00205409.pdf,Public CIK dual of mined city_ternat,Publish Opgroeien matrix behind envelope 46.52m + why omzet 14.46m commercial-only vs 73 31.07m + why pnl JUMP 866039 while destin JUMP 300000 and cash DROP 8616420 and FTE JUMP 671.2,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Ternat>INFANO>JR2025_statutory_L5,tick2470; Strong official native PDF; leftover mined city_ternat CIK; 86 VE; prior-year identical; EVERY-10; NOT Vijverbeek remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"INFANO opbr JUMP 46.52m / omzet JUMP 14.46m commercial-only / 73 JUMP 31.07m / pnl JUMP 866k / destin JUMP 300k (YE2025 leftover city_ternat CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Ternat>INFANO>JR2025",
"46522446",
"46522446",
"PDF 70/76A 46522446 envelope; omzet 14460807 commercial-only; 73 31066744; 76A 21687; VOL no 9900; bedrijfswinst JUMP 852477; pnl JUMP 866039; equity JUMP 11477684; assets JUMP 24585792; debt DROP 11296111; FTE 671.2; kapitaalsubsidies 1403474 DROP; destin691 JUMP 300000; cash DROP 8616420; geldbeleggingen 2650000; leftover city_ternat CIK 86 VE",
"strong",
SRC_PDF,
"Opgroeien + leftover city_ternat CIK",
"CIK / Kind en Gezin groepsopvang leftover city_ternat",
"46.52m opbr envelope; omzet 14.46m commercial-only vs 73 31.07m; pnl JUMP 866039; destin JUMP 300000; leftover city_ternat CIK",
"5.55",
"5.60",
"5.00",
"5.52",
"FOI Opgroeien matrix behind envelope 46.52m + why omzet 14.46m commercial-only vs 73 31.07m + why pnl JUMP 866039 while destin JUMP 300000 and cash DROP 8616420 and FTE JUMP 671.2",
"active",
"",
"tick2470 leftover mined city_ternat CIK after Vijverbeek different-city skip; EVERY-10; 86 VE; prior-year identical; NOT Vijverbeek remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Ternat>INFANO>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 46522446 (omzet 70 14460807 commercial-only + 73 31066744 + 76A 21687) and why destin JUMP 300000 while pnl JUMP 866039 and cash DROP 8616420 and FTE JUMP 671.2",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_ternat; VOL envelope 46.52m because omzet commercial-only vs large 73; public Opgroeien groepsopvang 86 VE Keizerstraat 35",
"priority": "8",
"recipient_body": "VZW INFANO / Raad van Bestuur",
"recipient_email": "info@infano.be",
"recipient_postal": "Keizerstraat 35 1740 Ternat",
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
"notes": "tick2470; ready NOT sent; Strong official native NBB PDF; leftover mined city_ternat CIK after Vijverbeek different-city skip; 86 VE; EVERY-10; off Vijverbeek remine; off Savio remine",
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
if rq_raw.count(b"rq_2470,")!=1: raise SystemExit(f"bad 2470 count {rq_raw.count(b'rq_2470,')}")
if b"rq_2471," in rq_raw: raise SystemExit("2471 exists")
idx=rq_raw.rfind(b"rq_2470,")
if idx<0: raise SystemExit("rq_2470 not found")
new_2470=(
"rq_2470,leftover dual INFANO YE2025 + EVERY-10,hole_fill,8,done,L5,vzw_infano_ternat,"
"Took unused leftover public CIK INFANO 0477.578.411 leftover mined city_ternat. Official NBB VOL-VZW YE2025 2026-00205409 native 42p. Envelope 70/76A JUMP 46522446; omzet JUMP 14460807 commercial-only; 73 JUMP 31066744; pnl JUMP 866039; destin JUMP 300000. EVERY-10 refresh. NOT Vijverbeek remine. NOT Savio remine.,"
f",{STAMP},{STAMP},tick2470 leftover mined city_ternat CIK; Strong native PDF; 86 VE; EVERY-10; next every-10 is 2480\n"
)
new_2471=(
"rq_2471,leftover dual after INFANO — hunt unused public dual,hole_fill,8,open,L5,,"
"After INFANO YE2025 EVERY-10. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine.,"
f",{STAMP},{STAMP},spawned after tick2470; Infano taken leftover mined city_ternat CIK EVERY-10; Vijverbeek taken leftover mined city_asse CIK; Mater Dei taken leftover mined city_brasschaat CIK; Savio taken leftover mined city_dilbeek CIK; Paideia taken leftover mined city_brugge CIK; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2480\n"
)
if new_2470.count("\n")!=1 or new_2471.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2470.encode("utf-8"))
    f.write(new_2471.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2470", chk.count(b"rq_2470,"), "n2471", chk.count(b"rq_2471,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2470,2470,no,tick2470 leftover dual INFANO 0477.578.411 Strong native PDF EVERY-10 (omzet70 JUMP 14460807 commercial-only; 73 JUMP 31066744; 76A JUMP 21687; envelope 70/76A JUMP 46522446; VOL no 9900; pnl JUMP 866039; 9901 JUMP 852477; equity JUMP 11477684; assets JUMP 24585792; debt DROP 11296111; FTE JUMP 671.2; kapitaalsubsidies DROP 1403474; destin691 JUMP 300000; 791 empty; cash DROP 8616420; geldbeleggingen DROP 2650000; 86 VE leftover city_ternat CIK); leftover mined city_ternat CIK; prior-year identical; NOT Vijverbeek remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; next every-10 is 2480; next rq_2471 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2470 - rq_2470 INFANO (opbr JUMP 46.52m / omzet JUMP 14.46m commercial-only / 73 JUMP 31.07m / pnl JUMP 866k / destin JUMP 300k / Strong PDF) + EVERY-10

- Unit: **rq_2470** leftover dual after **Vijverbeek@2469** + **EVERY-10**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. Vijverbeek 0448.164.744 just mined — do not remine. Mater Dei 0431.168.859 already mined — do not remine. Savio 0472.564.501 already mined — do not remine. Paideia 0445.129.931 already mined — do not remine. Ooievaarsnest 0418.588.256 already mined — do not remine. DE ZONNEKINDJES 0416.541.952 already mined — do not remine. D'n Opvang 0676.442.465 already mined — do not remine. CAR Overleie already mined — do not remine. Gesticht already mined — do not remine. HOCUS-POCUS already mined — do not remine. VKA already mined — do not remine. Soetkin already mined — do not remine. t Sloeberke already mined — do not remine. De Groene Verte already mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes already mined — do not remine. De Medemens Kinderdagverblijven already mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Hartjes Tienen 0441.374.348 already mined — do not remine. De Wissel 0421.913.376 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. EVA-vzw Gemeentelijke Kinderopvang Dilbeek 0477.276.325 already mined — do not remine. Dominiek Savio Hooglede VAPH already mined — do not remine. 3Wplus Kinderopvang Asse 0893.870.539 already mined — do not remine. Ferm Kinderopvang 0416.117.627 already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW INFANO** YE2025 (KBO **0477.578.411**; zetel Keizerstraat 35 1740 Ternat; **Actief** **86 VE**; RSZ2025 **88.911**; leftover of mined **city_ternat**; info@infano.be; Opgroeien groepsopvang / IBO / bedrijfsopvang; Kind en Gezin-vergund). Identity trap: INFANO 0477.578.411 ≠ Kinderdagverblijf Vijverbeek **0448.164.744** leftover city_asse just mined; ≠ 3Wplus Kinderopvang VZW Asse **0893.870.539**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis Pepingen; ≠ Kinderdagverblijf Savio **0472.564.501** leftover city_dilbeek (Infano VE Zonnetje Dilbeek **2.150.843.851** at Stationsstraat 277 is a different KBO); ≠ Dominiek Savio VZW Hooglede-Gits; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ D'n Opvang **0676.442.465**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ t Zonnetje / ZONNESTRAAL / Zonnestraal Junior; ≠ Hupskadee **0863.886.651**. 86 VE leftover of mined city_ternat (zetel Keizerstraat 35 1740 Ternat + Maantje/Zonnetje Ternat Keizerstraat 35A + Maantje Wambeek 1741 + Maantje/Zonnetje Sint-Katherina-Lombeek 1742). Confirmed leftover public (Opgroeien CIK groepsopvang/IBO/bedrijfsopvang; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Vijverbeek remine / not Savio remine. VOL-VZW **native text** (not scan) — 559435 B / 42p all native euros (VOL-VZW 6.1 / 6.2.1 / 6.2.3 / 6.2.4 / 6.3.4 / 6.3.6 / 6.4.1 / 6.4.2 / 6.5.1 / 6.5.2 / 6.5.3 / 6.14 / 6.16 / 8 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00205409** (559435 B / 42p; AV **25.06.2026**; header **26.06.2026**; CDN Last-Modified **10.07.2026**; CreationDate 27.06.2026 OpenPDF 1.3.26; all 42p native; prior-year identical not restated) — omzet 70 **EUR14460807** JUMP +9.51% (commercial-only vs large 73; was 13205344); 73 **EUR31066744** JUMP +16.24% (subsidies 733; was 26725259); 76A **EUR21687** JUMP +75.26%; envelope 70/76A **EUR46522446** JUMP +14.00% (70+72+73+74+76A; was 40810259); VOL no 9900; 62 **EUR32733570** JUMP +13.80%; 630 **EUR1519514** JUMP +16.57%; 66A **EUR495**; 640/8 **EUR71533**; 635/9 **EUR1016269** JUMP; 631/4 **EUR23481** JUMP; bedrijfswinst 9901 **EUR852477** JUMP +34.40%; pnl 9904 **EUR866039** JUMP +37.99%; equity **EUR11477684** JUMP +6.09%; assets **EUR24585792** JUMP +6.60%; debt **EUR11296111** DROP −1.50%; FTE **671.2** JUMP +8.61% (was 618; 9086 808 was 799); kapitaalsubsidies **EUR1403474** DROP −12.86%; destin 691 **EUR300000** JUMP +50.00% (791 empty; 14 JUMP 5316548 = prior 4750509 + pnl 866039 − destin 300000); 791 **empty**; cash **EUR8616420** DROP −0.82%; geldbeleggingen **EUR2650000** DROP −1.85%; gebouwen **EUR3313626** DROP; MVA 22/27 **EUR10367065** JUMP; aanbouw **empty**; capex **EUR2195142**; fondsen 10 **EUR432663** FLAT; overgedragen 14 **EUR5316548** JUMP; bestemde fondsen 13 **EUR4325000** JUMP; voorzieningen 16 **EUR1811996** JUMP +133.59%. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 86 VE leftover mined city_ternat CIK. NOT Vijverbeek remine. NOT 3Wplus remine. NOT Mater Dei remine. NOT WZC Mater Dei Heikruis remine. NOT Savio remine. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT DE ZONNEKINDJES remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Ferm Kinderopvang remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.52); entities (+1 vzw_infano_ternat); foi + draft `gap_infano_opgroeien_matrix_opbr_46_52m_omzet_14_46m_73_31_07m_pnl_jump_866k_destin_300k_l5`; rq_2470=done + rq_2471 open; loop_state ticks=2470; raw tick2470/ untracked; EVERY-10 refresh `progress_every_10_ticks.md` + `doge_waste_top10_current.md`.
- FOI: **ready not sent**. EVERY-10 done (next **2480**). Next: rq_2471 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Infano remine / NOT Vijverbeek remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine). NOW leftover candidate: Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
