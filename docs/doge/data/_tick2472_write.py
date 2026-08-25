from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2472_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_bambi_jr2025_nbb_pdf_2472"
SRC_KBO="src_bambi_kbo_2472"
SRC_SBM="src_bambi_sbm_2472"
SRC_SITE="src_bambi_site_2472"
EID="vzw_kdv_bambi_kalmthout"
GAP="gap_bambi_opgroeien_matrix_bruto_661k_omzet73_empty_pnl_flip_4k_cash_drop_destin_empty_l5"
COMM="comm_bambi_jr2025_statutory_bruto_661k_omzet73_empty_pnl_flip_4k_cash_drop"
LB="lb_bambi_bruto_661k_omzet73_empty_pnl_flip_4k_cash_drop_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf Bambi deposit 2026-00123006,http://cdn.staatsbladmonitor.be/2026pdf/2026-00123006.pdf,NBB official WVV deposit PDF via SBM CDN,{DAY},budget,tick2472; official native PDF 47776 bytes 12p VKT-VZW 25.0.12 m04-f; header 27.05.2026; AV 12.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-05-28 01:29:54 UTC OpenPDF 1.3.26; all 12p native; CDN 2026-00123006 GET 200 47776 official NBB-generated PDF; official NBB broker UUID 3f20e6ff-5120-11f1-9044-51fb9750ce3e HEAD 403 without SPA session; VKT-VZW 6.1.1 6.2 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf Bambi 0443.006.522,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443006522,KBO Public Search FOD Economie,{DAY},official_register,tick2472; Actief; 1 VE 2.156.383.937 Kinderdagverblijf Bambi vzw Ijzerenwegstraat (Dp) 65 2920 Kalmthout since 03.10.2006; VZW since 21.03.1990; begindatum 21.03.1990; zetel Ijzerenwegstraat (Dp) 65 2920 Kalmthout since 01.10.1990; toelating Kinderopvang VL since 01.04.2014; RSZ-werkgever since 01.09.1990; RSZ2025 88.911; FOI bambi.vzw@telenet.be; leftover mined city_kalmthout CIK; NOT Zonneschijn 0877.850.493 remine; NOT Infano 0477.578.411 remine; NOT Molleke 0448.186.520 YE2024",
f"{SRC_SBM},NBB Consult / SBM fiche Bambi 0443006522 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0443006522,NBB Consult / SBM,{DAY},official_register,tick2472; deposit-id 2026-00123006 YE 01.01.2025-31.12.2025 filing 27.05.2026 published VKT-VZW Verkort model vereniging Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK",
f"{SRC_SITE},Kinderdagverblijf Bambi FOI contact leftover city_kalmthout CIK,http://kinderdagverblijfbambi.be/,VZW Kinderdagverblijf Bambi leftover city_kalmthout CIK Opgroeien groepsopvang 1 VE,{DAY},foi_contact,tick2472; FOI bambi.vzw@telenet.be; zetel Ijzerenwegstraat (Dp) 65 2920 Kalmthout; 1 VE leftover mined city_kalmthout after Zonneschijn different-city skip; Opgroeien 9100000571; 42 plaatsen inkomenstarief; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Hupskadee YE2024; NOT KIOS Schoten no deposits; NOT Pardoes Mechelen YE2024; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw unused",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf Bambi,ASBL Kinderdagverblijf Bambi,Kinderdagverblijf Bambi VZW (leftover city_kalmthout CIK),parastatal,city_kalmthout,nl,http://kinderdagverblijfbambi.be/,bambi.vzw@telenet.be,Ijzerenwegstraat (Dp) 65 2920 Kalmthout,tick2472 YE2025 Strong official native NBB PDF deposit 2026-00123006 + Strong KBO 0443.006.522 Actief 1 VE 2.156.383.937; omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 661108; bruto JUMP 661108; pnl FLIP 3931; 9901 FLIP 3715; equity JUMP 101363; assets JUMP 190822; debt JUMP 89459; FTE DROP 12.5; kapitaalsubsidies empty; destin691 empty; 791 empty; cash DROP 85696; geldbeleggingen empty; leftover city_kalmthout CIK 1 VE; NOT Zonneschijn Dendermonde 0877.850.493 remine; NOT Infano Ternat 0477.578.411 remine; NOT Vijverbeek Asse 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT Duinhuisjes 0413.323.037 remine; NOT 3Wplus Kinderopvang Asse 0893.870.539 remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Savio Dilbeek 0472.564.501 remine; NOT Dominiek Savio remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Paideia 0445.129.931 remine; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; NOT Ferm Kinderopvang 0416.117.627 remine; NOT ZONNESTRAAL; NOT Molleke 0448.186.520 leftover city_mol YE2024; NOT t Sas 0448.731.106 leftover city_denderleeuw unused; NOT Dol-Fijn 0439.731.880 Turnhout zetel leftover-via-VE; Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 2026-00053030 not taken; KIOS 0882.468.881 leftover city_schoten no deposits not taken; Pardoes 0417.400.205 leftover city_mechelen YE2024 not taken; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_bambi_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2472; PDF p5 native; YE2024 empty; 73 empty; 76A empty",
f"bud_bambi_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2472; PDF p5 native; YE2024 empty; FOI Opgroeien matrix behind envelope 661108",
f"bud_bambi_opbr_jr2025_statutory,{EID},2025,661108,661108,661108,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +10.77% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2472; PDF p5 native; YE2024 596845; 70 empty; 73 empty; 76A empty",
f"bud_bambi_bruto_jr2025_statutory,{EID},2025,661108,661108,661108,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +10.77% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2472; PDF p5 native; YE2024 596845; 76A empty; 73 empty",
f"bud_bambi_pnl_jr2025_statutory,{EID},2025,3931,3931,3931,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 FLIP from LOSS (was -66165),{SRC_PDF},strong,tick2472; PDF p5 native; YE2024 -66165; bedrijfswinst 9901 3715 FLIP; destin691 empty",
f"bud_bambi_bedrijfswinst_jr2025_statutory,{EID},2025,3715,3715,3715,NBB VKT-VZW code 9901 bedrijfswinst YE2025 FLIP from LOSS (was -67673),{SRC_PDF},strong,tick2472; PDF p5 native; YE2024 -67673; 62 641380 DROP; 630 13707 DROP; 66A empty; 640/8 1221 JUMP; 635/9 empty; 631/4 1086",
f"bud_bambi_equity_jr2025_statutory,{EID},2025,101363,101363,101363,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +4.04%,{SRC_PDF},strong,tick2472; PDF p4 native; YE2024 97431; kapitaalsubsidies empty; overgedragen 14 101363 JUMP; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_bambi_assets_jr2025_statutory,{EID},2025,190822,190822,190822,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +3.86%,{SRC_PDF},strong,tick2472; PDF p3 native; YE2024 183726; MVA 22/27 86540 JUMP; cash 85696 DROP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 250 FLAT; LT recv 29 empty",
f"bud_bambi_debt_jr2025_statutory,{EID},2025,89459,89459,89459,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +3.67%,{SRC_PDF},strong,tick2472; PDF p4 native; YE2024 86295; 17 empty; 42/48 78240 DROP",
f"bud_bambi_cash_jr2025_statutory,{EID},2025,85696,85696,85696,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -30.57%,{SRC_PDF},strong,tick2472; PDF p3 native; YE2024 123422; geldbeleggingen 50/53 empty; capex 56281 gebouwen JUMP 80637",
f"bud_bambi_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty; 14 JUMP 101363 approx prior 97431 + pnl 3931),{SRC_PDF},strong,tick2472; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 empty FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":661108,\"\"2025_bruto\"\":661108,"
"\"\"2025_pnl\"\":3931,\"\"2025_bedrijfswinst\"\":3715,"
"\"\"2025_equity\"\":101363,\"\"2025_assets\"\":190822,\"\"2025_debt\"\":89459,"
"\"\"2025_fte\"\":12.5,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":85696,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":641380,\"\"2025_gebouwen22\"\":80637,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":101363,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":13707,\"\"2025_capex\"\":56281,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":596845,\"\"2024_bruto\"\":596845,\"\"2024_pnl\"\":-66165,\"\"2024_bedrijfswinst\"\":-67673,"
"\"\"2024_equity\"\":97431,\"\"2024_assets\"\":183726,"
"\"\"2024_debt\"\":86295,\"\"2024_cash\"\":123422,\"\"2024_fte\"\":12.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf Bambi YE2025 (bruto JUMP 661k / omzet+73 empty VKT / pnl FLIP 3.9k / cash DROP / destin empty / Strong PDF),{EID},Opgroeien + leftover city_kalmthout CIK,VZW Kinderdagverblijf Bambi (KBO 0443.006.522; Actief; 1 VE; zetel Kalmthout),2026-04-12,2025,2025,661108,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00123006.pdf,Public CIK dual of mined city_kalmthout,Publish Opgroeien matrix behind envelope 661k + why omzet+73 empty VKT and why pnl FLIP 3931 while destin empty and cash DROP 85696,{SRC_PDF},strong,Vlaanderen>Antwerpen>Kalmthout>Kinderdagverblijf Bambi>JR2025_statutory_L5,tick2472; Strong official native PDF; leftover mined city_kalmthout CIK; 1 VE; prior-year identical; NOT every-10; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Bambi bruto JUMP 661k / omzet+73 empty VKT / pnl FLIP 3.9k / cash DROP / destin empty (YE2025 leftover city_kalmthout CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Kalmthout>Kinderdagverblijf Bambi>JR2025",
"661108",
"661108",
"PDF envelope 661108 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A empty; bruto 661108; bedrijfswinst FLIP 3715; pnl FLIP 3931; equity JUMP 101363; assets JUMP 190822; debt JUMP 89459; FTE 12.5; kapitaalsubsidies empty; destin691 empty; cash DROP 85696; leftover city_kalmthout CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_kalmthout CIK",
"CIK / Kind en Gezin groepsopvang leftover city_kalmthout",
"661k envelope; omzet+73 empty VKT; pnl FLIP 3931; cash DROP 85696; destin empty; leftover city_kalmthout CIK",
"5.25",
"4.80",
"5.05",
"5.08",
"FOI Opgroeien matrix behind envelope 661k + why omzet+73 empty VKT and why pnl FLIP 3931 while destin empty and cash DROP 85696",
"active",
"",
"tick2472 leftover mined city_kalmthout CIK after Zonneschijn different-city skip; 1 VE; prior-year identical; NOT every-10; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT Mater Dei remine; NOT Savio remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT Hupskadee YE2024; NOT KIOS Schoten no deposits; NOT Pardoes Mechelen YE2024; NOT Molleke city_mol YE2024",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Kalmthout>Kinderdagverblijf Bambi>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope 661108 (omzet 70 empty + 73 empty + 76A empty; VKT bruto 9900) and why destin empty while pnl FLIP 3931 and cash DROP 85696 and capex 56281 gebouwen JUMP 80637",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_kalmthout; VKT envelope bruto 661k because omzet empty; public Opgroeien groepsopvang 1 VE Ijzerenwegstraat 65 Kalmthout",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf Bambi / Raad van Bestuur",
"recipient_email": "bambi.vzw@telenet.be",
"recipient_postal": "Ijzerenwegstraat (Dp) 65 2920 Kalmthout",
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
"notes": "tick2472; ready NOT sent; Strong official native NBB PDF; leftover mined city_kalmthout CIK after Zonneschijn different-city skip; 1 VE; prior-year identical; NOT every-10; off Zonneschijn remine; off Infano remine; off Molleke YE2024",
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
if rq_raw.count(b"rq_2472,")!=1: raise SystemExit(f"bad 2472 count {rq_raw.count(b'rq_2472,')}")
if b"rq_2473," in rq_raw: raise SystemExit("2473 exists")
idx=rq_raw.rfind(b"rq_2472,")
if idx<0: raise SystemExit("rq_2472 not found")
new_2472=(
"rq_2472,leftover dual Kinderdagverblijf Bambi YE2025,hole_fill,8,done,L5,vzw_kdv_bambi_kalmthout,"
"Took unused leftover public CIK Kinderdagverblijf Bambi 0443.006.522 leftover mined city_kalmthout. Official NBB VKT-VZW YE2025 2026-00123006 native 12p. Envelope bruto 9900 JUMP 661108 (omzet+73 empty VKT); pnl FLIP 3931; cash DROP 85696; destin empty; FTE 12.5. NOT Zonneschijn remine. NOT Infano remine. NOT Molleke YE2024. NOT Hupskadee YE2024.,"
f",{STAMP},{STAMP},tick2472 leftover mined city_kalmthout CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2480\n"
)
new_2473=(
"rq_2473,leftover dual after Bambi — hunt unused public dual,hole_fill,8,open,L5,,"
"After Bambi YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Molleke 0448.186.520 leftover city_mol YE2024 (filed 26.06.2025) — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw unused — take ONLY if unused + official YE2025 native PDF. Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 2026-00053030 — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. Pardoes 0417.400.205 leftover city_mechelen — YE2024 skip unless YE2025. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT Savio remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT EVA Dilbeek remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine.,"
f",{STAMP},{STAMP},spawned after tick2472; Bambi taken leftover mined city_kalmthout CIK; Zonneschijn taken leftover mined city_dendermonde CIK; Infano taken leftover mined city_ternat CIK EVERY-10; Vijverbeek taken leftover mined city_asse CIK; Mater Dei taken leftover mined city_brasschaat CIK; Savio taken leftover mined city_dilbeek CIK; Molleke city_mol YE2024; t Sas city_denderleeuw unused; KIOS Schoten no deposits; Pardoes Mechelen YE2024; next every-10 is 2480\n"
)
if new_2472.count("\n")!=1 or new_2473.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2472.encode("utf-8"))
    f.write(new_2473.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2472", chk.count(b"rq_2472,"), "n2473", chk.count(b"rq_2473,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2472,2472,no,tick2472 leftover dual Kinderdagverblijf Bambi 0443.006.522 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 661108; bruto JUMP 661108; pnl FLIP 3931; 9901 FLIP 3715; equity JUMP 101363; assets JUMP 190822; debt JUMP 89459; FTE DROP 12.5; kapitaalsubsidies empty; destin691 empty; 791 empty; cash DROP 85696; geldbeleggingen empty; 1 VE leftover city_kalmthout CIK); leftover mined city_kalmthout CIK; prior-year identical; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT Duinhuisjes remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Savio remine; NOT Dominiek Savio remine; NOT EVA Dilbeek remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT Hupskadee YE2024; NOT KIOS Schoten no deposits; NOT Pardoes Mechelen YE2024; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw unused; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; next every-10 is 2480; next rq_2473 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2472 - rq_2472 Kinderdagverblijf Bambi (bruto JUMP 661k / omzet+73 empty VKT / pnl FLIP 3.9k / cash DROP / destin empty / Strong PDF)

- Unit: **rq_2472** leftover dual after **Zonneschijn@2471**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy). Discovery path: less-picked mined Flanders cities with 0 leftover CIK (mechelen / herentals / schoten / vilvoorde / geel / mol / kalmthout / denderleeuw). Kinderdagverblijf Molleke **0448.186.520** leftover city_mol last-balansjaar **2024** (neerlegging 26.06.2025) — skip. Dol-Fijn **0439.731.880** zetel Turnhout leftover-via-VE Herentals — not enough. Witte Meren leftover city_mol already mined tick1732. Zusterhof leftover city_geel already mined tick1747. KIOS leftover city_schoten — no jaarrekening — skip. Pardoes leftover city_mechelen — last deposit YE2024 — skip. Hupskadee leftover city_begijnendijk YE2024 only (2026-00053030 already on disk) — not taken. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Kinderlach leftover city_eeklo still **YE2024**. De Linde Ronse leftover city_ronse still **YE2024**. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024**. Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum leftover city_gent training — skip. Helan Kinderopvang already skipped. Zwarte Zusters dissolved — skip. Private BVs (Ello Mechelen / Troetelland Geel / Regenboog Vilvoorde / Vlindertje Schoten) skipped. Zonneschijn 0877.850.493 just mined — do not remine. Infano 0477.578.411 already mined — do not remine. Vijverbeek already mined — do not remine. Mater Dei already mined — do not remine. Savio already mined — do not remine. t Zonnetje Waregem already mined — do not remine. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Kinderdagverblijf Bambi** YE2025 (KBO **0443.006.522**; zetel Ijzerenwegstraat (Dp) 65 2920 Kalmthout; **Actief** **1 VE** **2.156.383.937** since 03.10.2006; RSZ2025 **88.911**; leftover of mined **city_kalmthout**; bambi.vzw@telenet.be; Opgroeien groepsopvang 9100000571; Kind en Gezin-vergund; 42 plaatsen inkomenstarief). Identity trap: Bambi 0443.006.522 ≠ Zonneschijn **0877.850.493** leftover city_dendermonde just mined; ≠ INFANO **0477.578.411**; ≠ Kinderdagverblijf Vijverbeek **0448.164.744**; ≠ t Zonnetje Waregem **0443.648.306**; ≠ DE ZONNEKINDJES **0416.541.952**; ≠ ZONNESTRAAL / Zonnestraal Junior; ≠ Kindercentrum Waregem **0408.226.775**; ≠ Duinhuisjes **0413.323.037**; ≠ Groepsopvang Mater Dei **0431.168.859**; ≠ WZC Mater Dei Heikruis; ≠ Kinderdagverblijf Savio **0472.564.501**; ≠ Dominiek Savio; ≠ EVA Dilbeek **0477.276.325**; ≠ Paideia **0445.129.931**; ≠ KDV Ooievaarsnest **0418.588.256**; ≠ D'n Opvang **0676.442.465**; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ De Elfjes **0455.636.912**; ≠ De Steijgertjes **0413.421.720**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved; ≠ Hupskadee **0863.886.651**; ≠ KIOS **0882.468.881**; ≠ Pardoes **0417.400.205**; ≠ Molleke **0448.186.520**; ≠ t Sas **0448.731.106**; ≠ Dol-Fijn **0439.731.880**; ≠ Witte Meren **0418.234.997**; ≠ Zusterhof **0473.762.450**. 1 VE Kalmthout — leftover of mined city_kalmthout (zetel + Ijzerenwegstraat 65). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Zonneschijn remine / not Infano remine / not Molleke YE2024. VKT-VZW **native text** (not scan) — 47776 B / 12p all native euros (VKT-VZW 6.1.1 / 6.2 / 6.3 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00123006** (47776 B / 12p; AV **12.04.2026**; header **27.05.2026**; CDN GET **200** 47776 official NBB-generated OpenPDF 1.3.26; official NBB broker UUID 3f20e6ff HEAD **403** without SPA session; CreationDate 28.05.2026; all 12p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR661108** JUMP +10.77% (VKT envelope because omzet empty; was 596845); bruto 9900 **EUR661108** JUMP +10.77%; 62 **EUR641380** DROP −0.46%; 630 **EUR13707** DROP −27.84%; 66A **empty**; 640/8 **EUR1221** JUMP +2.43%; 635/9 **empty**; 631/4 **EUR1086**; bedrijfswinst 9901 **EUR3715** FLIP from LOSS (was −67673); pnl 9904 **EUR3931** FLIP from LOSS (was −66165); equity **EUR101363** JUMP +4.04%; assets **EUR190822** JUMP +3.86%; debt **EUR89459** JUMP +3.67%; FTE **12.5** DROP −0.79% (was 12.6; 100 12.5; 105 12.4); kapitaalsubsidies **empty**; destin 691 **empty** (791 empty; 14 JUMP 101363 ≈ prior 97431 + pnl 3931); 791 **empty**; cash **EUR85696** DROP −30.57%; geldbeleggingen **empty**; gebouwen **EUR80637** JUMP; MVA 22/27 **EUR86540** JUMP; aanbouw **empty**; capex **EUR56281**; fondsen 10 **empty**; overgedragen 14 **EUR101363** JUMP; bestemde fondsen 13 **empty**; voorzieningen 16 **empty**; FVA 28 **EUR250** FLAT; LT recv 29 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_kalmthout CIK. NOT Zonneschijn remine. NOT Infano remine. NOT Molleke YE2024. NOT t Sas unused. NOT Hupskadee YE2024. NOT KIOS no deposits. NOT Pardoes YE2024.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.08); entities (+1 vzw_kdv_bambi_kalmthout); foi + draft `gap_bambi_opgroeien_matrix_bruto_661k_omzet73_empty_pnl_flip_4k_cash_drop_destin_empty_l5`; rq_2472=done + rq_2473 open; loop_state ticks=2472; raw tick2472/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2480**). Next: rq_2473 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Bambi remine / NOT Zonneschijn remine / NOT Infano remine / NOT Vijverbeek remine / NOT t Zonnetje remine / NOT Kindercentrum remine / NOT Duinhuisjes remine / NOT Mater Dei remine / NOT Savio remine / NOT 3Wplus remine / NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved / NOT Dominiek Savio remine / NOT EVA Dilbeek remine / NOT WZC Mater Dei Heikruis remine / NOT Ferm Kinderopvang remine / NOT Molleke YE2024 / NOT Witte Meren remine / NOT Zusterhof remine). NOW leftover candidate: Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw unused — take ONLY if unused + official YE2025 native PDF. Hupskadee 0863.886.651 leftover city_begijnendijk YE2024 2026-00053030 — take ONLY if unused + official YE2025 native PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. KIOS leftover city_schoten no deposits — skip. Pardoes leftover city_mechelen YE2024 — skip unless YE2025. Tick **2480** is next every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
