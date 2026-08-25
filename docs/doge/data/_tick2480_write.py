from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2480_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_bwp_jr2025_nbb_pdf_2480"
SRC_KBO="src_bwp_kbo_2480"
SRC_SBM="src_bwp_sbm_2480"
SRC_SITE="src_bwp_site_2480"
EID="vzw_bwp_dilbeek"
GAP="gap_bwp_dilbeek_vaph_matrix_bruto_3_31m_omzet73_empty_pnl_drop_239k_destin_7k_l5"
COMM="comm_bwp_jr2025_statutory_bruto_331m_pnl_drop_7k_destin_7k"
LB="lb_bwp_bruto_331m_omzet73_empty_pnl_drop_7k_destin_7k_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Begeleid Wonen Pajottenland Dilbeek deposit 2026-00154659,http://cdn.staatsbladmonitor.be/2026pdf/2026-00154659.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2480; official native statutory PDF 55785 bytes 15p VKT-VZW 23.0.9 m04-f; header 08.06.2026; AV 28.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-12 02:01:30 UTC OpenPDF 1.3.26; CDN Last-Modified 19.06.2026; all 15p native; CDN 2026-00154659 GET 200 55785 MD5 ae97530fd30f3cede885a8aef3f255e3; VKT-VZW 6.5 6.6 7 8 niet dienstig; 6.1.1 6.1.2 6.1.3 6.4 6.7 6.8 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Begeleid Wonen Pajottenland 0423.884.258,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0423884258,KBO Public Search FOD Economie,{DAY},official_register,tick2480; Actief; 2 VE zetel Lostraat 87 bus a 1703 Dilbeek since 26.05.2020; VZW since 30.09.1982; begindatum 30.09.1982; RSZ-werkgever since 01.07.1989; RSZ2025 88.999 Andere vormen van maatschappelijke dienstverlening zonder huisvesting; FOI administratie@bewopajot.be; leftover mined city_dilbeek VAPH; VE 2.306.788.474 Lostraat 87a + contact campus Keizerstraat 34 Ternat; NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Begeleid Wonen Pajottenland 0423884258 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0423884258,NBB Consult / SBM,{DAY},official_register,tick2480; deposit-id 2026-00154659 YE 01.01.2025-31.12.2025 filing 08.06.2026 published VKT-VZW Verkort model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Begeleid Wonen Pajottenland FOI contact leftover city_dilbeek VAPH,https://www.begeleidwonenpajottenland.be/,Begeleid Wonen Pajottenland VZW leftover city_dilbeek VAPH 2 VE,{DAY},foi_contact,tick2480; FOI administratie@bewopajot.be; tel 02 582 11 00; zetel Lostraat 87a 1703 Dilbeek; contact campus Keizerstraat 34 1740 Ternat; 2 VE leftover mined city_dilbeek after CVDO lock; VAPH begeleid wonen + RTH; NOT INFANO remine; NOT MWP Lennik remine; NOT Savio remine; NOT EVA Dilbeek remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Kindercentrum remine; NOT t Zonnetje remine; NOT Armonea commercial; NOT Orelia commercial; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Zusterhof remine; NOT Ter Engelen YE2024; NOT De Vlietoever BV commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial",
])
print("sources ok")

NOTS=("NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Dominiek Savio remine; NOT CVDO 0433.927.322 remine; NOT CAR De Klinker Ieper 0430.535.290 remine; NOT Dennenhof 0410.252.590 remine; NOT Ten Anker 0414.679.849 remine; NOT WZC Ten Anker Nieuwpoort 0475.837.260 remine; NOT Bremdael 0435.234.149 remine; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT 3Wplus remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea commercial; NOT Orelia commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Lindeboom remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals 0443.580.604 YE2024; NOT AZ Herentals 0821.734.213 remine; NOT Ter Engelen 0430.882.809 YE2024; NOT De Vlietoever BV 0898.596.122 commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial")

append_lines(DATA/"entities.csv", [
f"{EID},Begeleid Wonen Pajottenland VZW,ASBL Begeleid Wonen Pajottenland,Begeleid Wonen Pajottenland VZW (leftover city_dilbeek VAPH),parastatal,city_dilbeek,nl,https://www.begeleidwonenpajottenland.be/,administratie@bewopajot.be,Lostraat 87a 1703 Dilbeek,tick2480 YE2025 Strong official native NBB PDF deposit 2026-00154659 + Strong KBO 0423.884.258 Actief 2 VE; omzet70 empty VKT; 73 empty VKT; 76A DROP 29739; envelope bruto 9900 JUMP 3314484; bruto JUMP 3314484; pnl DROP 7364; 9901 DROP 1620; equity JUMP 1089388; assets JUMP 1850713; debt JUMP 761325; FTE JUMP 45; kapitaalsubsidies DROP 115557; destin691 7364; 791 empty; cash JUMP 879267; geldbeleggingen empty; leftover city_dilbeek VAPH 2 VE; prior-year identical; EVERY-10; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_bwp_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2480; PDF p5 native; YE2024 empty; 73 empty; 76A 29739 DROP",
f"bud_bwp_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2480; PDF p5 native; YE2024 empty; FOI VAPH / PVB / RTH matrix behind envelope 3314484",
f"bud_bwp_opbr_jr2025_statutory,{EID},2025,3314484,3314484,3314484,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +3.15% (omzet empty so envelope is bruto 9900),{SRC_PDF},strong,tick2480; PDF p5 native; YE2024 3213315; 70 empty; 73 empty; 76A 29739 DROP",
f"bud_bwp_bruto_jr2025_statutory,{EID},2025,3314484,3314484,3314484,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.15% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2480; PDF p5 native; YE2024 3213315; 76A 29739 DROP; 73 empty",
f"bud_bwp_pnl_jr2025_statutory,{EID},2025,7364,7364,7364,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -97.01% (was 246076),{SRC_PDF},strong,tick2480; PDF p5 native; YE2024 246076; bedrijfswinst 9901 1620 DROP; destin691 7364",
f"bud_bwp_bedrijfswinst_jr2025_statutory,{EID},2025,1620,1620,1620,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -99.33% (was 241938),{SRC_PDF},strong,tick2480; PDF p5 native; YE2024 241938; 62 3258979 JUMP; 630 37880 DROP; 66A 1860; 640/8 14145 DROP; 635/9 empty; 631/4 empty",
f"bud_bwp_equity_jr2025_statutory,{EID},2025,1089388,1089388,1089388,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +0.28%,{SRC_PDF},strong,tick2480; PDF p4 native; YE2024 1086304; kapitaalsubsidies 115557 DROP; overgedragen 14 empty; fondsen 10 empty; bestemde fondsen 13 JUMP 973831",
f"bud_bwp_assets_jr2025_statutory,{EID},2025,1850713,1850713,1850713,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.30%,{SRC_PDF},strong,tick2480; PDF p3 native; YE2024 1809093; MVA 22/27 810681 DROP; cash 879267 JUMP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 8400 FLAT; LT recv 29 empty",
f"bud_bwp_debt_jr2025_statutory,{EID},2025,761325,761325,761325,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +5.33%,{SRC_PDF},strong,tick2480; PDF p4 native; YE2024 722789; 17 165951 DROP; 42/48 595374 JUMP; 43 empty",
f"bud_bwp_cash_jr2025_statutory,{EID},2025,879267,879267,879267,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +2.65%,{SRC_PDF},strong,tick2480; PDF p3 native; YE2024 856578; geldbeleggingen 50/53 empty; capex 15943",
f"bud_bwp_destin_jr2025_statutory,{EID},2025,7364,7364,7364,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -97.44% (791 empty; 13 JUMP 973831 = 13P 966467 + destin 7364),{SRC_PDF},strong,tick2480; PDF p6 native; YE2024 destin 287439; bestemde fondsen 13 973831 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":29739,"
"\"\"2025_opbr70_76A\"\":0,\"\"2025_bruto\"\":3314484,"
"\"\"2025_pnl\"\":7364,\"\"2025_bedrijfswinst\"\":1620,"
"\"\"2025_equity\"\":1089388,\"\"2025_assets\"\":1850713,\"\"2025_debt\"\":761325,"
"\"\"2025_fte\"\":45,\"\"2025_kapitaalsubsidies\"\":115557,\"\"2025_destin691\"\":7364,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":879267,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":3258979,\"\"2025_gebouwen22\"\":780342,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":1860,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":973831,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":37880,\"\"2025_capex\"\":15943,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":8069,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":0,\"\"2024_bruto\"\":3213315,\"\"2024_pnl\"\":246076,\"\"2024_bedrijfswinst\"\":241938,"
"\"\"2024_equity\"\":1086304,\"\"2024_assets\"\":1809093,"
"\"\"2024_debt\"\":722789,\"\"2024_cash\"\":856578,\"\"2024_fte\"\":44.2,"
"\"\"2024_destin691\"\":287439,\"\"2024_kapitaalsubsidies\"\":119837,\"\"2024_76A\"\":217756,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Begeleid Wonen Pajottenland YE2025 (bruto JUMP 3.31m / omzet+73 empty VKT / pnl DROP 7.4k / destin 7.4k / Strong PDF),{EID},VAPH + leftover city_dilbeek VAPH,Begeleid Wonen Pajottenland VZW (KBO 0423.884.258; Actief; 2 VE; zetel Dilbeek),2026-05-28,2025,2025,3314484,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00154659.pdf,Public VAPH dual of mined city_dilbeek,Publish VAPH / PVB / RTH matrix behind bruto 3.31m and why pnl DROP 7364 and destin 7364 while 76A DROP 29739,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Dilbeek>Begeleid Wonen Pajottenland>JR2025_statutory_L5,tick2480 EVERY-10; Strong official native PDF; leftover mined city_dilbeek VAPH; 2 VE; prior-year identical; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT INFANO remine; NOT Savio remine; NOT MWP Lennik remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Begeleid Wonen Pajottenland bruto JUMP 3.31m / omzet+73 empty VKT / pnl DROP 7.4k / destin 7.4k (YE2025 leftover city_dilbeek VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Dilbeek>Begeleid Wonen Pajottenland>JR2025",
"3314484",
"3314484",
"PDF envelope 3314484 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A 29739 DROP; bruto 3314484; bedrijfswinst DROP 1620; pnl DROP 7364; equity JUMP 1089388; assets JUMP 1850713; debt JUMP 761325; FTE 45; kapitaalsubsidies 115557; destin691 7364; cash JUMP 879267; leftover city_dilbeek VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_dilbeek VAPH",
"VAPH begeleid wonen leftover city_dilbeek",
"3.31m envelope; omzet+73 empty VKT; pnl DROP 7364; destin 7364; leftover city_dilbeek VAPH",
"5.52",
"5.32",
"5.18",
"5.34",
"FOI VAPH / PVB / RTH matrix behind envelope 3.31m + why omzet+73 empty VKT and why pnl DROP 7364 while destin 7364 and 76A DROP 29739",
"active",
"",
"tick2480 leftover mined city_dilbeek VAPH after CVDO lock; EVERY-10; 2 VE; prior-year identical; NOT INFANO remine tick2470; NOT MWP Lennik remine tick2201; NOT Savio remine tick2467; NOT EVA Dilbeek remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Kindercentrum remine; NOT t Zonnetje remine; NOT WZC Ten Anker Nieuwpoort remine; NOT Hupskadee BV private BV; NOT Armonea commercial; NOT Orelia commercial; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Dilbeek>Begeleid Wonen Pajottenland>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / PVB / RTH split behind envelope bruto 3314484 (omzet+73 empty VKT; 76A DROP 29739) and why pnl DROP 7364 and destin 7364 while FTE JUMP 45 and 62 JUMP 3258979 plus identical 2024 comparatives",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_dilbeek; VKT envelope bruto 9900 3.31m because omzet empty; public VAPH 2 VE Lostraat 87a Dilbeek + Keizerstraat 34 Ternat; pnl DROP 239k / destin 7.4k / 76A DROP 188k / 62 JUMP 12pct",
"priority": "8",
"recipient_body": "Begeleid Wonen Pajottenland VZW / Raad van Bestuur",
"recipient_email": "administratie@bewopajot.be",
"recipient_postal": "Lostraat 87a 1703 Dilbeek",
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
"notes": "tick2480 EVERY-10; ready NOT sent; Strong official native NBB PDF; leftover mined city_dilbeek VAPH after CVDO lock; 2 VE; prior-year identical; off INFANO remine; off MWP Lennik remine; off Savio remine; off CVDO remine; off Dennenhof remine; off Ten Anker remine; off Bremdael remine; off Armonea commercial; off Orelia commercial",
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
if rq_raw.count(b"rq_2480,")!=1: raise SystemExit(f"bad 2480 count {rq_raw.count(b'rq_2480,')}")
if b"rq_2481," in rq_raw: raise SystemExit("2481 exists")
idx=rq_raw.rfind(b"rq_2480,")
if idx<0: raise SystemExit("rq_2480 not found")
new_2480=(
"rq_2480,leftover dual Begeleid Wonen Pajottenland YE2025 + every-10,hole_fill,8,done,L5,vzw_bwp_dilbeek,"
"Took unused leftover public VAPH Begeleid Wonen Pajottenland 0423.884.258 leftover mined city_dilbeek. Official NBB VKT-VZW YE2025 2026-00154659 native statutory 15p. Envelope bruto9900 JUMP 3314484 (omzet+73 empty VKT; 76A DROP 29739); pnl DROP 7364; destin 7364; FTE 45. EVERY-10 refresh after leftover write. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Bremdael remine. NOT Armonea commercial. NOT Orelia commercial.,"
f",{STAMP},{STAMP},tick2480 leftover mined city_dilbeek VAPH; Strong native PDF; 2 VE; prior-year identical; EVERY-10; next every-10 is 2490\n"
)
new_2481=(
"rq_2481,leftover dual hunt after Begeleid Wonen Pajottenland,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: vilvoorde / mol / denderleeuw / zoersel / schilde (Sint Lodewijk taken) / kalmthout (Bambi taken) / dendermonde (Zonneschijn taken) / geel (Augustientjes taken) / herentals (Bremdael WZC taken — different leftover type only; AZ already mined; OpWeg YE2024) / knokke_heist (De Lindeboom + Duinhuisjes + CVDO taken) / waregem (Kindercentrum + t Zonnetje + Ten Anker taken) / schoten (De Vier Notelaars + Dennenhof taken) / dilbeek (Savio CIK + BWP VAPH taken — different leftover type only). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. OpWeg 0443.580.604 leftover city_herentals VAPH YE2024 — take ONLY if unused + official YE2025 native PDF. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW. Ter Bake / Rodenbach Denderleeuw Armonea commercial. De Vlietoever Bornem BV commercial. Ter Engelen Lokeren YE2024 already mined. NOT Begeleid Wonen Pajottenland remine. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT EVA Dilbeek remine. NOT CVDO remine. NOT CAR De Klinker Ieper remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT WZC Ten Anker Nieuwpoort remine. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck/Ter Bake commercial. NOT Orelia Koningshof commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed. NOT Sint Lodewijk remine. NOT De Lindeboom remine. NOT De Vier Notelaars remine. NOT Lidwina remine. NOT Homevil remine. NOT Schoonderhage remine. NOT AZ Herentals remine.,"
f",{STAMP},{STAMP},spawned after tick2480 leftover city_dilbeek VAPH EVERY-10; Begeleid Wonen Pajottenland taken; CVDO taken leftover mined city_knokke_heist CAR; Dennenhof taken leftover mined city_schoten VAPH; Ten Anker taken leftover mined city_waregem VAPH; Bremdael taken leftover mined city_herentals WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2480.count("\n")!=1 or new_2481.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2480",new_2480),("2481",new_2481)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2480.encode("utf-8"))
    f.write(new_2481.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2480", chk.count(b"rq_2480,"), "n2481", chk.count(b"rq_2481,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2480,2480,no,tick2480 leftover dual Begeleid Wonen Pajottenland 0423.884.258 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A DROP 29739; envelope bruto9900 JUMP 3314484; pnl DROP 7364; 9901 DROP 1620; equity JUMP 1089388; assets JUMP 1850713; debt JUMP 761325; FTE JUMP 45; kapitaalsubsidies DROP 115557; destin691 7364; 791 empty; cash JUMP 879267; geldbeleggingen empty; 2 VE leftover city_dilbeek VAPH); leftover mined city_dilbeek VAPH; prior-year identical; EVERY-10; NOT INFANO remine; NOT MWP Lennik remine; NOT Savio remine; NOT EVA Dilbeek remine; NOT CVDO remine; NOT CAR De Klinker Ieper remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT WZC Ten Anker Nieuwpoort remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Hupskadee BV 0476.248.224 private; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Infano remine; NOT Vijverbeek remine; NOT t Zonnetje remine; NOT Kindercentrum remine; NOT 3Wplus remine; NOT Mater Dei remine; NOT WZC Mater Dei Heikruis remine; NOT Dominiek Savio remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels leftover-via-VE; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn Turnhout leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea Vogelzang/Hemelrijck/Ter Bake commercial; NOT Orelia Koningshof commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Lindeboom remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Ter Engelen YE2024; NOT De Vlietoever BV commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; next every-10 is 2490; next rq_2481 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2480 - rq_2480 Begeleid Wonen Pajottenland Dilbeek (bruto JUMP 3.31m / omzet+73 empty VKT / pnl DROP 7.4k / destin 7.4k / Strong PDF) + EVERY-10

- Unit: **rq_2480** leftover dual after **CVDO@2479**. THIS TICK IS EVERY-10. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of less-picked mined Flanders cities (CIK lists herentals/schoten/vilvoorde/mol exhausted at 2476; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde this failed hunt). Confirmed `city_dilbeek` / `city_herentals` / `city_geel` / `city_dendermonde` / `city_waregem` / `city_denderleeuw` / `city_zoersel` exist. FIRST locked: Begeleid Wonen Pajottenland **0423.884.258** leftover city_dilbeek VAPH unused YE2025 **2026-00154659** VKT 56kB — unused + leftover mined parent + official CDN GET **200** 55785 native extractable euros — **LOCKED**. Skips this hunt: WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW; Ter Bake / Rodenbach Denderleeuw Armonea commercial; AZ St.-Elisabeth Herentals **0821.734.213** already mined tick2005; OpWeg Herentals **0443.580.604** leftover VAPH YE2024; De Vlietoever Bornem BV commercial; Ter Engelen Lokeren YE2024 already mined; De Karmel Waregem = Curando already mined; Zusterhof Geel already mined; Den Toeter Zoersel private BV; leftover VZW CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: 0423.884.258 ≠ INFANO **0477.578.411** (Keizerstraat 35 Ternat) ≠ MWP Pajottenland **0413.313.535** Lennik ≠ Savio Dilbeek **0472.564.501**. 2 VE leftover of mined city_dilbeek (zetel Lostraat 87a + campus Keizerstraat 34 Ternat). Confirmed leftover public VAPH not convent / not private / not CIK / not WZC. VKT-VZW native 15p (6.5 6.6 7 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00154659** (55785 B / 15p; AV **28.05.2026**; header **08.06.2026**; CDN GET **200** 55785 official NBB-generated OpenPDF 1.3.26 CreationDate 12.06.2026 Last-Modified 19.06.2026 MD5 ae97530fd30f3cede885a8aef3f255e3; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **EUR29739** DROP −86.34% (was 217756); envelope bruto 9900 **EUR3314484** JUMP +3.15% (VKT because omzet empty); pnl 9904 **EUR7364** DROP −97.01% (was 246076); bedrijfswinst 9901 **EUR1620** DROP −99.33%; equity **EUR1089388** JUMP +0.28%; assets **EUR1850713** JUMP +2.30%; debt **EUR761325** JUMP +5.33%; FTE **45** JUMP +1.81% (was 44.2); kapitaalsubsidies **EUR115557** DROP −3.57%; destin 691 **EUR7364** DROP (791 empty; 13 JUMP 973831 = 966467 + 7364); cash **EUR879267** JUMP +2.65%; 62 **EUR3258979** JUMP +12.07%. Strong KBO + Strong PDF. NOT INFANO remine. NOT Savio remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Armonea commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.34); entities (+1 vzw_bwp_dilbeek); foi + draft `gap_bwp_dilbeek_vaph_matrix_bruto_3_31m_omzet73_empty_pnl_drop_239k_destin_7k_l5`; rq_2480=done + rq_2481 open; loop_state ticks=2480; raw tick2480/ untracked. EVERY-10 refresh of progress_every_10_ticks.md + doge_waste_top10_current.md from live inventory after leftover write.
- FOI: **ready not sent**. Tick **2480 IS every-10**. Next: rq_2481 leftover dual (NOT every-10; next every-10 is **2490**).

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
