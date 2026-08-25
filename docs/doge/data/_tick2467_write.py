from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2467_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_savio_jr2025_nbb_pdf_2467"
SRC_KBO="src_savio_kbo_2467"
SRC_SBM="src_savio_sbm_2467"
SRC_SITE="src_savio_site_2467"
EID="vzw_savio_dilbeek"
GAP="gap_savio_opgroeien_matrix_opbr_734k_omzet_drop_151k_73_578k_pnl_drop_336_destin_empty_l5"
COMM="comm_savio_jr2025_statutory_opbr_734k_omzet_drop_151k_73_578k_pnl_drop_336"
LB="lb_savio_opbr_734k_omzet_drop_151k_73_578k_pnl_drop_336_destin_empty_jr2025"
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
f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 Kinderdagverblijf Savio deposit 2026-00109816,http://cdn.staatsbladmonitor.be/2026pdf/2026-00109816.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2467; official native PDF 36381 bytes 8p MIC-VZW 26.0.11 m08-f; header 13.05.2026; AV 12.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-13 05:26:47 UTC OpenPDF 1.3.26; all 8p native; CDN 2026-00109816 GET 200 Last-Modified 06.06.2026; MIC-VZW 6.1.1 6.1.3 6.2 6.3 6.4 6.5 7 8 niet dienstig; prior-year restated (niet identiek); euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf Savio 0472.564.501,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472564501,KBO Public Search FOD Economie,{DAY},official_register,tick2467; Actief; 0 VE zetel-only; VZW since 26.04.2000; begindatum 26.04.2000; zetel Stationsstraat 277 1700 Dilbeek since 26.04.2000; FOI savio277@skynet.be; leftover mined city_dilbeek CIK; NOT Dominiek Savio Hooglede VAPH remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf Savio 0472564501 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0472564501,NBB Consult / SBM,{DAY},official_register,tick2467; deposit-id 2026-00109816 YE 01.01.2025-31.12.2025 filing 13.05.2026 published 13.05.2026 MIC-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Savio FOI contact leftover city_dilbeek CIK,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0472564501,VZW Kinderdagverblijf Savio leftover city_dilbeek CIK Opgroeien groepsopvang 37 plaatsen,{DAY},foi_contact,tick2467; FOI savio277@skynet.be; zetel Stationsstraat 277 1700 Dilbeek; 0 VE leftover mined city_dilbeek after Paideia different-city skip; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf Savio,ASBL Kinderdagverblijf Savio,Kinderdagverblijf Savio VZW (leftover city_dilbeek CIK),parastatal,city_dilbeek,nl,,savio277@skynet.be,Stationsstraat 277 1700 Dilbeek,tick2467 YE2025 Strong official native NBB PDF deposit 2026-00109816 + Strong KBO 0472.564.501 Actief 0 VE zetel-only; omzet70 DROP 150899 commercial-only; 73 JUMP 577675; 76A DROP 5392; envelope 70/76A JUMP 733966; bruto JUMP 632751; pnl DROP 336; 9901 DROP -8255; equity JUMP 225261; assets JUMP 599992; debt JUMP 58731; FTE empty MIC 6.5 niet dienstig; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 42619; geldbeleggingen JUMP 465000; voorzieningen JUMP 316000; leftover city_dilbeek CIK 37 plaatsen; NOT Dominiek Savio Hooglede VAPH remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; Mater Dei Brasschaat 0431.168.859 unused YE2025 not taken; Vijverbeek Asse 0448.164.744 unused YE2025 not taken; Infano Ternat 0477.578.411 unused YE2025 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_savio_omzet_jr2025_statutory,{EID},2025,150899,150899,150899,NBB MIC-VZW code 70 omzet YE2025 DROP -5.81% (commercial-only vs large 73; was 160210 restated),{SRC_PDF},strong,tick2467; PDF p6 native; YE2024 restated 160210; 73 577675; 76A 5392",
f"bud_savio_73_jr2025_statutory,{EID},2025,577675,577675,577675,NBB MIC-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +3.01% (was 560797 restated),{SRC_PDF},strong,tick2467; PDF p6 native; YE2024 restated 560797; FOI Opgroeien matrix behind envelope 733966",
f"bud_savio_opbr_jr2025_statutory,{EID},2025,733966,733966,733966,NBB MIC-VZW envelope 70/76A YE2025 JUMP +0.61% (omzet 70 commercial-only vs large 73 so envelope is 70+73+76A),{SRC_PDF},strong,tick2467; PDF p6 native; YE2024 restated 729508; 70 150899; 73 577675; 76A 5392",
f"bud_savio_bruto_jr2025_statutory,{EID},2025,632751,632751,632751,NBB MIC-VZW code 9900 brutomarge YE2025 JUMP +0.43% (MIC present; envelope remains 70/76A because omzet not empty),{SRC_PDF},strong,tick2467; PDF p6 native; YE2024 restated 630015; 76A 5392; 73 577675",
f"bud_savio_pnl_jr2025_statutory,{EID},2025,336,336,336,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 DROP -75.20% (was 1355 restated),{SRC_PDF},strong,tick2467; PDF p6 native; YE2024 restated 1355; bedrijfswinst 9901 -8255 DROP; destin691 empty",
f"bud_savio_bedrijfswinst_jr2025_statutory,{EID},2025,-8255,-8255,-8255,NBB MIC-VZW code 9901 bedrijfswinst YE2025 DROP (was -4668 restated),{SRC_PDF},strong,tick2467; PDF p6 native; YE2024 restated -4668; 62 552355 JUMP; 630 8256 JUMP; 66A empty; 640/8 395 JUMP; 635/9 80000 JUMP",
f"bud_savio_equity_jr2025_statutory,{EID},2025,225261,225261,225261,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +0.15%,{SRC_PDF},strong,tick2467; PDF p5 native; YE2024 restated 224925; kapitaalsubsidies empty; overgedragen 14 225261 JUMP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_savio_assets_jr2025_statutory,{EID},2025,599992,599992,599992,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +16.92%,{SRC_PDF},strong,tick2467; PDF p4 native; YE2024 restated 513182; MVA 22/27 35351 JUMP; cash 42619 JUMP; geldbeleggingen 465000 JUMP; aanbouw 27 empty",
f"bud_savio_debt_jr2025_statutory,{EID},2025,58731,58731,58731,NBB MIC-VZW code 17/49 schulden YE2025 JUMP +12.39%,{SRC_PDF},strong,tick2467; PDF p5 native; YE2024 restated 52257; 17 empty; 42/48 58731 JUMP",
f"bud_savio_cash_jr2025_statutory,{EID},2025,42619,42619,42619,NBB MIC-VZW code 54/58 liquide middelen YE2025 JUMP +39.43%,{SRC_PDF},strong,tick2467; PDF p4 native; YE2024 restated 30566; geldbeleggingen 50/53 465000 JUMP was 420000 restated",
f"bud_savio_destin_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty; 14 JUMP 225261 = prior 224925 restated + pnl 336),{SRC_PDF},strong,tick2467; PDF p7 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":150899,\"\"2025_73\"\":577675,\"\"2025_76A\"\":5392,"
"\"\"2025_opbr70_76A\"\":733966,\"\"2025_bruto\"\":632751,"
"\"\"2025_pnl\"\":336,\"\"2025_bedrijfswinst\"\":-8255,"
"\"\"2025_equity\"\":225261,\"\"2025_assets\"\":599992,\"\"2025_debt\"\":58731,"
"\"\"2025_fte\"\":0,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":42619,\"\"2025_geldbeleggingen\"\":465000,"
"\"\"2025_personnel62\"\":552355,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":225261,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":316000,\"\"2025_630\"\":8256,\"\"2025_capex\"\":2110,"
"\"\"2024_omzet\"\":160210,\"\"2024_73\"\":560797,"
"\"\"2024_opbr70_76A\"\":729508,\"\"2024_bruto\"\":630015,\"\"2024_pnl\"\":1355,\"\"2024_bedrijfswinst\"\":-4668,"
"\"\"2024_equity\"\":224925,\"\"2024_assets\"\":513182,"
"\"\"2024_debt\"\":52257,\"\"2024_cash\"\":30566,\"\"2024_fte\"\":0,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":8501,"
"\"\"2024_geldbeleggingen\"\":420000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf Savio YE2025 (opbr JUMP 734k / omzet DROP 151k commercial-only / 73 JUMP 578k / pnl DROP 336 / destin empty / Strong PDF),{EID},Opgroeien + leftover city_dilbeek CIK,VZW Kinderdagverblijf Savio (KBO 0472.564.501; Actief; 0 VE zetel-only; zetel Dilbeek),2026-05-12,2025,2025,733966,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00109816.pdf,Public CIK dual of mined city_dilbeek,Publish Opgroeien matrix behind envelope 734k + why omzet commercial-only vs 73 578k and why pnl DROP 336 while destin empty and voorzieningen JUMP 316k,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Dilbeek>Kinderdagverblijf Savio>JR2025_statutory_L5,tick2467; Strong official native PDF; leftover mined city_dilbeek CIK; 0 VE zetel-only; prior-year restated; NOT every-10; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Kinderdagverblijf Savio opbr JUMP 734k / omzet DROP 151k commercial-only / 73 JUMP 578k / pnl DROP 336 / destin empty (YE2025 leftover city_dilbeek CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Dilbeek>Kinderdagverblijf Savio>JR2025",
"733966",
"733966",
"PDF envelope 733966 = 70+73+76A; omzet 150899 commercial-only; 73 577675; 76A 5392; bruto 632751; bedrijfswinst DROP -8255; pnl DROP 336; equity JUMP 225261; assets JUMP 599992; debt JUMP 58731; FTE empty; kapitaalsubsidies empty; destin691 empty; cash JUMP 42619; geldbeleggingen JUMP 465000; voorzieningen JUMP 316000; leftover city_dilbeek CIK 37 plaatsen",
"strong",
SRC_PDF,
"Opgroeien + leftover city_dilbeek CIK",
"CIK / Kind en Gezin groepsopvang leftover city_dilbeek",
"734k envelope; omzet DROP 151k commercial-only; 73 JUMP 578k; pnl DROP 336; destin empty; leftover city_dilbeek CIK",
"5.10",
"5.02",
"5.05",
"5.06",
"FOI Opgroeien matrix behind envelope 734k + why omzet commercial-only vs 73 578k and why pnl DROP 336 while destin empty and voorzieningen JUMP 316k",
"active",
"",
"tick2467 leftover mined city_dilbeek CIK after Paideia different-city skip; 0 VE zetel-only; prior-year restated; NOT every-10; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Dilbeek>Kinderdagverblijf Savio>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 733966 (omzet 70 150899 commercial-only + 73 577675 + 76A 5392) and why destin empty while pnl DROP 336 and voorzieningen JUMP 316000 and cash JUMP 42619",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_dilbeek; MIC envelope 70/76A 734k because omzet commercial-only vs large 73; public Opgroeien groepsopvang 37 plaatsen Stationsstraat 277",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf Savio / Raad van Bestuur",
"recipient_email": "savio277@skynet.be",
"recipient_postal": "Stationsstraat 277 1700 Dilbeek",
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
"notes": "tick2467; ready NOT sent; Strong official native NBB PDF; leftover mined city_dilbeek CIK after Paideia different-city skip; 0 VE zetel-only; prior-year restated; NOT every-10; off Paideia remine; off Dominiek Savio remine; off EVA Dilbeek remine",
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
if rq_raw.count(b"rq_2467,")!=1: raise SystemExit(f"bad 2467 count {rq_raw.count(b'rq_2467,')}")
if b"rq_2468," in rq_raw: raise SystemExit("2468 exists")
idx=rq_raw.rfind(b"rq_2467,")
if idx<0: raise SystemExit("rq_2467 not found")
new_2467=(
"rq_2467,leftover dual Kinderdagverblijf Savio YE2025,hole_fill,8,done,L5,vzw_savio_dilbeek,"
"Took unused leftover public CIK Kinderdagverblijf Savio 0472.564.501 leftover mined city_dilbeek. Official NBB MIC-VZW YE2025 2026-00109816 native 8p. Envelope 70/76A JUMP 733966 (omzet DROP 150899 commercial-only; 73 JUMP 577675; 76A 5392); pnl DROP 336; destin empty; FTE empty MIC 6.5. NOT Paideia remine. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2467 leftover mined city_dilbeek CIK; Strong native PDF; 0 VE zetel-only; prior-year restated; next every-10 is 2470\n"
)
new_2468=(
"rq_2468,leftover dual after Kinderdagverblijf Savio — hunt unused public dual,hole_fill,8,open,L5,,"
"After Kinderdagverblijf Savio YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Groepsopvang Mater Dei 0431.168.859 leftover city_brasschaat YE2025 2026-00145548 — take ONLY if unused + official native-text YE2025 PDF. KDV Vijverbeek 0448.164.744 leftover city_asse YE2025 2026-00119084 — take ONLY if unused + official native-text YE2025 PDF. Infano 0477.578.411 leftover city_ternat YE2025 2026-00205409 — take ONLY if unused + official native-text YE2025 PDF. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT Savio remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine.,"
f",{STAMP},{STAMP},spawned after tick2467; Savio taken leftover mined city_dilbeek CIK; Paideia taken leftover mined city_brugge CIK; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2467.count("\n")!=1 or new_2468.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2467.encode("utf-8"))
    f.write(new_2468.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2467", chk.count(b"rq_2467,"), "n2468", chk.count(b"rq_2468,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2467,2467,no,tick2467 leftover dual Kinderdagverblijf Savio 0472.564.501 Strong native PDF (omzet70 DROP 150899 commercial-only; 73 JUMP 577675; 76A DROP 5392; envelope 70/76A JUMP 733966; bruto JUMP 632751; pnl DROP 336; 9901 DROP -8255; equity JUMP 225261; assets JUMP 599992; debt JUMP 58731; FTE empty MIC 6.5; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 42619; geldbeleggingen JUMP 465000; voorzieningen JUMP 316000; 0 VE leftover city_dilbeek CIK); leftover mined city_dilbeek CIK; prior-year restated; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; next every-10 is 2470; next rq_2468 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2467 - rq_2467 Kinderdagverblijf Savio (opbr JUMP 734k / omzet DROP 151k commercial-only / 73 JUMP 578k / pnl DROP 336 / destin empty / Strong PDF)

- Unit: **rq_2467** leftover dual after **Paideia@2466**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. Paideia 0445.129.931 just mined — do not remine. Ooievaarsnest 0418.588.256 just mined — do not remine. DE ZONNEKINDJES 0416.541.952 just mined — do not remine. D'n Opvang 0676.442.465 just mined — do not remine. CAR Overleie just mined — do not remine. Gesticht just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Hartjes Tienen 0441.374.348 already mined — do not remine. De Wissel 0421.913.376 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. EVA-vzw Gemeentelijke Kinderopvang Dilbeek 0477.276.325 already mined — do not remine. Dominiek Savio Hooglede VAPH already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Kinderdagverblijf Savio** YE2025 (KBO **0472.564.501**; zetel Stationsstraat 277 1700 Dilbeek; **Actief** **0 VE** zetel-only since 26.04.2000; leftover of mined **city_dilbeek**; savio277@skynet.be; Opgroeien groepsopvang **37 plaatsen**). Identity trap: Kinderdagverblijf Savio 0472.564.501 ≠ Dominiek Savio VZW Hooglede-Gits VAPH already mined; ≠ EVA-vzw Gemeentelijke Kinderopvang Dilbeek **0477.276.325** leftover city_dilbeek already mined; ≠ Paideia **0445.129.931** leftover city_brugge just mined; ≠ KDV Ooievaarsnest **0418.588.256** leftover city_tienen just mined; ≠ DE ZONNEKINDJES **0416.541.952** leftover city_diepenbeek just mined; ≠ D'n Opvang **0676.442.465** leftover city_oostende just mined; ≠ De Elfjes **0455.636.912** already mined; ≠ De Steijgertjes **0413.421.720** already mined; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ Groepsopvang Mater Dei **0431.168.859** leftover city_brasschaat unused YE2025; ≠ KDV Vijverbeek **0448.164.744** leftover city_asse unused YE2025; ≠ Infano **0477.578.411** leftover city_ternat unused YE2025. 0 VE Dilbeek — leftover of mined city_dilbeek (zetel-only Stationsstraat 277). Confirmed leftover public (Opgroeien CIK groepsopvang 37 plaatsen; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Dominiek Savio remine / not EVA Dilbeek remine / not Paideia remine. MIC-VZW **native text** (not scan) — 36381 B / 8p all native euros (MIC-VZW 6.1.1 / 6.1.3 / 6.2 / 6.3 / 6.4 / 6.5 / 7 / 8 niet dienstig).
- Found: official NBB MIC-VZW native PDF deposit **2026-00109816** (36381 B / 8p; AV **12.05.2026**; header **13.05.2026**; CDN Last-Modified **06.06.2026**; CreationDate 13.05.2026 OpenPDF 1.3.26; all 8p native; prior-year **restated**) — omzet 70 **EUR150899** DROP −5.81% (commercial-only vs large 73; was 160210 restated); 73 **EUR577675** JUMP +3.01% (was 560797 restated); 76A **EUR5392** DROP −36.57% (was 8501 restated); envelope 70/76A **EUR733966** JUMP +0.61% (70+73+76A; was 729508 restated); bruto 9900 **EUR632751** JUMP +0.43% (MIC present; envelope remains 70/76A because omzet not empty; was 630015 restated); 62 **EUR552355** JUMP +0.17%; 630 **EUR8256** JUMP +2.94%; 66A **empty**; 640/8 **EUR395** JUMP +50.76%; 635/9 **EUR80000** JUMP +6.67%; bedrijfswinst 9901 **EUR-8255** DROP (was −4668 restated); pnl 9904 **EUR336** DROP −75.20% (was 1355 restated); equity **EUR225261** JUMP +0.15%; assets **EUR599992** JUMP +16.92%; debt **EUR58731** JUMP +12.39%; FTE **empty** (MIC-VZW 6.5 niet dienstig); kapitaalsubsidies **empty**; destin 691 **empty** (791 empty; 14 JUMP 225261 = prior 224925 restated + pnl 336); 791 **empty**; cash **EUR42619** JUMP +39.43%; geldbeleggingen **EUR465000** JUMP +10.71% (was 420000 restated); gebouwen **empty**; MVA 22/27 **EUR35351** JUMP; aanbouw **empty**; capex **EUR2110**; fondsen 10 **empty**; overgedragen 14 **EUR225261** JUMP; bestemde fondsen 13 **empty**; voorzieningen 16 **EUR316000** JUMP +33.90%. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: zetel-only leftover mined city_dilbeek CIK. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT DE ZONNEKINDJES remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.06); entities (+1 vzw_savio_dilbeek); foi + draft `gap_savio_opgroeien_matrix_opbr_734k_omzet_drop_151k_73_578k_pnl_drop_336_destin_empty_l5`; rq_2467=done + rq_2468 open; loop_state ticks=2467; raw tick2467/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2468 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Savio remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine). NOW leftover candidate: Groepsopvang Mater Dei 0431.168.859 leftover city_brasschaat unused YE2025 **2026-00145548** CDN **200** 48kB — take ONLY if unused + official native-text YE2025 PDF. KDV Vijverbeek 0448.164.744 leftover city_asse unused YE2025 **2026-00119084** CDN **200** 258kB — take ONLY if unused + official native-text YE2025 PDF. Infano 0477.578.411 leftover city_ternat unused YE2025 **2026-00205409** CDN **200** 559kB — take ONLY if unused + official native-text YE2025 PDF. Hupskadee 0863.886.651 leftover city_begijnendijk 2026 deposits — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
