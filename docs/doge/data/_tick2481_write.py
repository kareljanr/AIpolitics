from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2481_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hagewinde_jr2025_nbb_pdf_2481"
SRC_KBO="src_hagewinde_kbo_2481"
SRC_SBM="src_hagewinde_sbm_2481"
SRC_SITE="src_hagewinde_site_2481"
EID="vzw_hagewinde_lokeren"
GAP="gap_hagewinde_lokeren_vaph_matrix_70_76A_26_39m_omzet_commercial_73_jump_24_73m_pnl_flip_loss_550k_66B_1_20m_l5"
COMM="comm_hagewinde_jr2025_statutory_70_76A_2639m_73_jump_2473m_pnl_flip_loss_550k"
LB="lb_hagewinde_70_76A_2639m_73_jump_2473m_pnl_flip_loss_550k_66B_12m_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT Ter Engelen 0430.882.809 remine; NOT CAR Waas 0415.472.279 remine; NOT Sakura 0684.613.726 remine; NOT Kaliber 0407.201.941 remine; NOT Begeleid Wonen Pajottenland 0423.884.258 remine; NOT INFANO 0477.578.411 remine; NOT MWP Pajottenland 0413.313.535 remine; NOT Savio Dilbeek 0472.564.501 remine; NOT EVA Dilbeek 0477.276.325 remine; NOT Dominiek Savio remine; NOT CVDO 0433.927.322 remine; NOT CAR De Klinker Ieper 0430.535.290 remine; NOT Dennenhof 0410.252.590 remine; NOT Ten Anker 0414.679.849 remine; NOT WZC Ten Anker Nieuwpoort 0475.837.260 remine; NOT Bremdael 0435.234.149 remine; NOT De Augustientjes 0445.602.360 remine; NOT Hupskadee 0863.886.651 remine; NOT Hupskadee BV 0476.248.224 private BV; NOT Pardoes 0417.400.205 remine; NOT Bambi 0443.006.522 remine; NOT Zonneschijn 0877.850.493 remine; NOT Vijverbeek 0448.164.744 remine; NOT t Zonnetje Waregem 0443.648.306 remine; NOT Kindercentrum Waregem 0408.226.775 remine; NOT 3Wplus remine; NOT Mater Dei 0431.168.859 remine; NOT WZC Mater Dei Heikruis remine; NOT Paideia remine; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels leftover-via-VE; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; NOT Ferm Kinderopvang remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; NOT Huis Perrekes 0444.947.611 remine; NOT Sint-Augustinus Halle 0459.770.496 remine; NOT OLV Bornem 0436.595.020 remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Kaliber YE2024 remine; NOT Philippus Neri 0471.795.132 YE2024 Sint-Niklaas seat leftover-via-VE; NOT De Linde Ronse 0778.279.401 YE2024; NOT De Maretak 0881.890.049 Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW Geel; NOT CAR Glorieux Werken Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT Pardoes NV bookshop; NOT Olliebollie BV private; NOT In de wolken BV private; NOT Troetelland Geel private BV; NOT De Zandkapoentjes BV private; NOT Armonea commercial; NOT Orelia commercial; NOT Stijn leftover-via-VE Hasselt remine; NOT Felies leftover-via-VE Brussels; NOT Klein Hemelrijk absorbed; NOT Sint Lodewijk remine; NOT De Lindeboom remine; NOT De Vier Notelaars remine; NOT Lidwina remine; NOT Homevil remine; NOT Schoonderhage remine; NOT OpWeg Herentals 0443.580.604 YE2024; NOT AZ Herentals 0821.734.213 remine; NOT De Vlietoever BV 0898.596.122 commercial; NOT WZC Joostens Zoersel Zorgbedrijf Antwerpen; NOT Ter Bake Armonea commercial")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Zorg en onderwijs De Hagewinde Lokeren deposit 2026-00276108,http://cdn.staatsbladmonitor.be/2026pdf/2026-00276108.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2481; official native statutory PDF 2994546 bytes 50p VOL-VZW 23.0.10 m05-f; header 06.07.2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-10 03:46:31 UTC OpenPDF 1.3.26; CDN Last-Modified 29.07.2026; statutory pages native; CDN 2026-00276108 GET 200 2994546 MD5 28e6b209757ae23685d59b3002b197d2; VOL-VZW 6.1 6.2.2 6.2.3 6.2.4 6.4.1 6.4.2 6.5.2 6.5.3 6.7 6.10 6.14 6.16 niet dienstig; 6.2.1 6.3.1-6.3.6 6.5.1 6.6 6.8 6.9 6.11 6.12 6.17 present; prior-year identical not restated; commissaris Verifin BV / Van Hemelryck Geert; pages 45-50 Penneo scan; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Zorg en onderwijs De Hagewinde 0861.262.010,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0861262010,KBO Public Search FOD Economie,{DAY},official_register,tick2481; Actief; 6 VE zetel Poststraat 6 9160 Lokeren since 01.01.2025; VZW since 16.10.2003; begindatum 23.10.2003; RSZ-werkgever since 01.01.2013; aanbestedende overheid since 16.10.2003; RSZ2025 88.105 Activiteiten van dagcentra voor minderjarigen met een mentale handicap; FOI info@hagewinde.be; leftover mined city_lokeren VAPH; absorbed Scholen De Hagewinde 0408.579.044 since 01.01.2018; NOT Ter Engelen remine; NOT CAR Waas remine; NOT Sakura remine",
f"{SRC_SBM},NBB Consult / SBM fiche De Hagewinde 0861262010 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0861262010,NBB Consult / SBM,{DAY},official_register,tick2481; deposit-id 2026-00276108 YE 01.01.2025-31.12.2025 filing 06.07.2026 published VOL-VZW Volledig model vereniging Initial; Companyweb last-balansjaar 2025 deposit-id discovery OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Hagewinde FOI contact leftover city_lokeren VAPH,https://www.hagewinde.be/,Zorg en onderwijs De Hagewinde VZW leftover city_lokeren VAPH 6 VE,{DAY},foi_contact,tick2481; FOI info@hagewinde.be; tel 09 337 89 00; zetel Poststraat 6 9160 Lokeren; 6 VE leftover mined city_lokeren after BWP lock; VAPH MFC + BuSO De Karwij + De Vinderij; NOT Ter Engelen remine; NOT CAR Waas remine; NOT Sakura remine; NOT Kaliber remine; NOT BWP remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Zorg en onderwijs De Hagewinde VZW,ASBL Soins et enseignement De Hagewinde,De Hagewinde VZW (leftover city_lokeren VAPH),parastatal,city_lokeren,nl,https://www.hagewinde.be/,info@hagewinde.be,Poststraat 6 9160 Lokeren,tick2481 YE2025 Strong official native NBB PDF deposit 2026-00276108 + Strong KBO 0861.262.010 Actief 6 VE; omzet70 JUMP 961172 commercial-only vs large 73; 73 JUMP 24730647; 76A JUMP 10469; envelope 70/76A JUMP 26389520; pnl FLIP LOSS -549643; 9901 DROP 589398; equity JUMP 29744304; assets DROP 35767720; debt DROP 6023416; FTE JUMP 263.2; kapitaalsubsidies JUMP 16311859; destin691 empty; 791 JUMP 1278891; cash JUMP 3546732; geldbeleggingen DROP 7461; leftover city_lokeren VAPH 6 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hagewinde_omzet_jr2025_statutory,{EID},2025,961172,961172,961172,NBB VOL-VZW code 70 omzet YE2025 JUMP +7.19% (commercial-only vs large 73),{SRC_PDF},strong,tick2481; PDF p6 native; YE2024 896728; 73 JUMP 24730647; 76A JUMP 10469",
f"bud_hagewinde_73_jr2025_statutory,{EID},2025,24730647,24730647,24730647,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +10.05%,{SRC_PDF},strong,tick2481; PDF p6 native; YE2024 22472637; 731 28579; 732 empty; 733 23843789; FOI VAPH/MFC/onderwijs/VIPA matrix behind 73",
f"bud_hagewinde_opbr_jr2025_statutory,{EID},2025,26389520,26389520,26389520,NBB VOL-VZW envelope 70/76A YE2025 JUMP +11.13% (VZW envelope because omzet commercial-only vs large 73),{SRC_PDF},strong,tick2481; PDF p6 native; YE2024 23747104; 70 961172; 73 24730647; 76A 10469; 74 687232",
f"bud_hagewinde_bruto_jr2025_statutory,{EID},2025,26389520,26389520,26389520,NBB VOL-VZW 70/76A bedrijfsopbrengsten YE2025 JUMP +11.13% (VOL envelope; omzet commercial-only vs large 73),{SRC_PDF},strong,tick2481; PDF p6 native; YE2024 23747104; 76A 10469 JUMP; 73 JUMP 24730647",
f"bud_hagewinde_pnl_jr2025_statutory,{EID},2025,-549643,-549643,-549643,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 FLIP LOSS (was +869999),{SRC_PDF},strong,tick2481; PDF p7 native; YE2024 869999; bedrijfswinst 9901 589398 DROP; 66B 1204372 VAPH vakantiegeld; destin691 empty; 791 1278891",
f"bud_hagewinde_bedrijfswinst_jr2025_statutory,{EID},2025,589398,589398,589398,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -24.79% (was 783626),{SRC_PDF},strong,tick2481; PDF p6 native; YE2024 783626; 62 20487446 JUMP; 630 1501755 FLAT; 66A empty; 640/8 64846 DROP; 635/9 -23812; 631/4 empty",
f"bud_hagewinde_equity_jr2025_statutory,{EID},2025,29744304,29744304,29744304,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +1.03%,{SRC_PDF},strong,tick2481; PDF p5 native; YE2024 29442418; kapitaalsubsidies 16311859 JUMP; overgedragen 14 2403667 DROP; fondsen 10 3888930 FLAT; bestemde fondsen 13 7139848 FLAT",
f"bud_hagewinde_assets_jr2025_statutory,{EID},2025,35767720,35767720,35767720,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -1.25%,{SRC_PDF},strong,tick2481; PDF p4 native; YE2024 36219814; MVA 22/27 26959907 JUMP; cash 3546732 JUMP; geldbeleggingen 7461 DROP; aanbouw 27 1353734 JUMP; FVA 28 25849 DROP; LT recv 29 908771 DROP",
f"bud_hagewinde_debt_jr2025_statutory,{EID},2025,6023416,6023416,6023416,NBB VOL-VZW code 17/49 schulden YE2025 DROP -10.81%,{SRC_PDF},strong,tick2481; PDF p5 native; YE2024 6753583; 17 1201450 DROP; 42/48 3476374 DROP; 43 empty",
f"bud_hagewinde_cash_jr2025_statutory,{EID},2025,3546732,3546732,3546732,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +5.25%,{SRC_PDF},strong,tick2481; PDF p4 native; YE2024 3369898; geldbeleggingen 50/53 7461 DROP; capex 3062744",
f"bud_hagewinde_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 JUMP 1278891; 13 FLAT 7139848),{SRC_PDF},strong,tick2481; PDF p8 native; YE2024 destin 819999; 791 1278891 JUMP FOI 14P vs 14",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":961172,\"\"2025_73\"\":24730647,\"\"2025_76A\"\":10469,"
"\"\"2025_opbr70_76A\"\":26389520,\"\"2025_bruto\"\":26389520,"
"\"\"2025_pnl\"\":-549643,\"\"2025_bedrijfswinst\"\":589398,"
"\"\"2025_equity\"\":29744304,\"\"2025_assets\"\":35767720,\"\"2025_debt\"\":6023416,"
"\"\"2025_fte\"\":263.2,\"\"2025_kapitaalsubsidies\"\":16311859,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":1278891,\"\"2025_cash\"\":3546732,\"\"2025_geldbeleggingen\"\":7461,"
"\"\"2025_personnel62\"\":20487446,\"\"2025_gebouwen22\"\":24679802,"
"\"\"2025_aanbouw27\"\":1353734,\"\"2025_66A\"\":0,\"\"2025_66B\"\":1204372,"
"\"\"2025_fondsen10\"\":3888930,\"\"2025_overgedragen14\"\":2403667,"
"\"\"2025_bestemdefondsen13\"\":7139848,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":1501755,\"\"2025_capex\"\":3062744,"
"\"\"2025_ltrecv29\"\":908771,\"\"2025_75\"\":120427,\"\"2025_74\"\":687232,"
"\"\"2025_731\"\":28579,\"\"2025_733\"\":23843789,"
"\"\"2024_omzet\"\":896728,\"\"2024_73\"\":22472637,"
"\"\"2024_opbr70_76A\"\":23747104,\"\"2024_bruto\"\":23747104,\"\"2024_pnl\"\":869999,\"\"2024_bedrijfswinst\"\":783626,"
"\"\"2024_equity\"\":29442418,\"\"2024_assets\"\":36219814,"
"\"\"2024_debt\"\":6753583,\"\"2024_cash\"\":3369898,\"\"2024_fte\"\":253.3,"
"\"\"2024_destin691\"\":819999,\"\"2024_kapitaalsubsidies\"\":15460331,\"\"2024_76A\"\":2493,"
"\"\"2024_geldbeleggingen\"\":3108511}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Hagewinde YE2025 (70/76A JUMP 26.39m / omzet commercial vs 73 JUMP 24.73m / pnl FLIP LOSS 550k / 66B 1.20m / Strong PDF),{EID},VAPH + leftover city_lokeren VAPH,Zorg en onderwijs De Hagewinde VZW (KBO 0861.262.010; Actief; 6 VE; zetel Lokeren),2026-06-22,2025,2025,26389520,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00276108.pdf,Public VAPH dual of mined city_lokeren,Publish VAPH / MFC / onderwijs / VIPA matrix behind 70/76A 26.39m and why pnl FLIP LOSS 549643 while 66B 1204372 and 791 1278891,{SRC_PDF},strong,Vlaanderen>Oost-Vlaanderen>Lokeren>De Hagewinde>JR2025_statutory_L5,tick2481; Strong official native PDF; leftover mined city_lokeren VAPH; 6 VE; prior-year identical; NOT Ter Engelen remine; NOT CAR Waas remine; NOT Sakura remine; NOT Kaliber remine; NOT BWP remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Hagewinde 70/76A JUMP 26.39m / omzet commercial vs 73 JUMP 24.73m / pnl FLIP LOSS 550k / 66B 1.20m (YE2025 leftover city_lokeren VAPH)",
"L5",
"vaph_vzw_statutory",
"Vlaanderen>Oost-Vlaanderen>Lokeren>De Hagewinde>JR2025",
"26389520",
"26389520",
"PDF envelope 26389520 = 70/76A VZW because omzet commercial-only vs large 73; 70 961172; 73 24730647; 76A 10469; 66B 1204372; bedrijfswinst DROP 589398; pnl FLIP LOSS -549643; equity JUMP 29744304; assets DROP 35767720; debt DROP 6023416; FTE 263.2; kapitaalsubsidies 16311859; destin691 empty; 791 1278891; cash JUMP 3546732; leftover city_lokeren VAPH",
"strong",
SRC_PDF,
"VAPH + leftover city_lokeren VAPH",
"VAPH MFC leftover city_lokeren",
"26.39m envelope; omzet commercial vs 73 24.73m; pnl FLIP LOSS 550k; 66B 1.20m; leftover city_lokeren VAPH",
"5.68",
"5.55",
"5.22",
"5.52",
"FOI VAPH / MFC / onderwijs / VIPA matrix behind envelope 26.39m + why omzet commercial-only vs 73 JUMP 24.73m and why pnl FLIP LOSS 549643 while 66B 1204372 and 791 1278891",
"active",
"",
"tick2481 leftover mined city_lokeren VAPH after BWP lock; 6 VE; prior-year identical; NOT Ter Engelen remine; NOT CAR Waas remine; NOT Sakura remine; NOT Kaliber remine; NOT BWP remine tick2480; NOT INFANO remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT KIOS Schoten no deposits; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Oost-Vlaanderen>Lokeren>De Hagewinde>VAPH",
"entity_id": EID,
"what_is_missing": "VAPH / MFC / onderwijs / VIPA split behind envelope 70/76A 26389520 (omzet commercial-only 961172 vs 73 JUMP 24730647) and why pnl FLIP LOSS -549643 while 66B 1204372 VAPH vakantiegeld write-off and 791 JUMP 1278891 plus 14P vs 14 opening",
"why_it_matters": "Strong official PDF leftover public VAPH of mined city_lokeren; VOL envelope 70/76A 26.39m because omzet commercial-only vs large 73; public VAPH MFC + BuSO 6 VE Poststraat 6 Lokeren; pnl FLIP LOSS 550k / 66B 1.20m / 791 1.28m / geldbeleggingen DROP 3.10m",
"priority": "8",
"recipient_body": "Zorg en onderwijs De Hagewinde VZW / Raad van Bestuur",
"recipient_email": "info@hagewinde.be",
"recipient_postal": "Poststraat 6 9160 Lokeren",
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
"notes": "tick2481; ready NOT sent; Strong official native NBB PDF; leftover mined city_lokeren VAPH after BWP lock; 6 VE; prior-year identical; off Ter Engelen remine; off CAR Waas remine; off Sakura remine; off Kaliber remine; off BWP remine; off CVDO remine; off Dennenhof remine; off Ten Anker remine; off Bremdael remine; off Armonea commercial; off Vulpia commercial",
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
if rq_raw.count(b"rq_2481,")!=1: raise SystemExit(f"bad 2481 count {rq_raw.count(b'rq_2481,')}")
if b"rq_2482," in rq_raw: raise SystemExit("2482 exists")
idx=rq_raw.rfind(b"rq_2481,")
if idx<0: raise SystemExit("rq_2481 not found")
new_2481=(
"rq_2481,leftover dual De Hagewinde YE2025,hole_fill,8,done,L5,vzw_hagewinde_lokeren,"
"Took unused leftover public VAPH Zorg en onderwijs De Hagewinde 0861.262.010 leftover mined city_lokeren. Official NBB VOL-VZW YE2025 2026-00276108 native statutory 50p. Envelope 70/76A JUMP 26389520 (omzet commercial-only vs large 73 JUMP 24730647); pnl FLIP LOSS -549643; 66B 1204372; destin 691 empty; 791 JUMP 1278891; FTE 263.2. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT BWP remine. NOT CVDO remine. NOT Dennenhof remine. NOT Armonea commercial. NOT Vulpia commercial.,"
f",{STAMP},{STAMP},tick2481 leftover mined city_lokeren VAPH; Strong native PDF; 6 VE; prior-year identical; next every-10 is 2490\n"
)
new_2482=(
"rq_2482,leftover dual hunt after De Hagewinde,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: vilvoorde / mol / denderleeuw (WZC/VAPH leftover; skip Armonea Ter Bake/Rodenbach) / zoersel / schilde (Sint Lodewijk taken) / kalmthout (Bambi CIK taken; leftover WZC/VAPH; skip Vulpia Beukenhof / De Medemens remine) / dendermonde (Zonneschijn CIK taken; leftover WZC/VAPH/CAR; skip OCMW Aymonshof/De Cocon; skip Zorg-Saam/Broeders leftover-via-VE) / geel (Augustientjes CIK taken; leftover VAPH/CAR; WZC Zusterhof+Perrekes remine; skip Armonea Laarsveld / Vulpia Het Veld / OCMW Wedbos) / herentals (Bremdael WZC taken — leftover VAPH/CAR only; AZ already mined; OpWeg YE2024; Kaliber maatwerk remine) / knokke_heist (De Lindeboom + Duinhuisjes + CVDO taken) / waregem (Kindercentrum + t Zonnetje + Ten Anker taken) / schoten (De Vier Notelaars + Dennenhof taken) / dilbeek (Savio CIK + BWP VAPH taken) / lokeren (CAR Waas + Ter Engelen + Sakura + Hagewinde VAPH taken — different leftover type only) / eeklo (CAR Ascendere + KISME + Don Bosco taken; leftover WZC; skip Zorg-Saam Gent seat; Philippus Neri YE2024 Sint-Niklaas seat) / ronse (De Linde WZC YE2024 0778.279.401) / halle (CAR taken; Sint-Augustinus WZC remine; skip De Maretak Korian; Zonnig Huis city) / bornem (OLV WZC remine; skip De Vlietoever BV). Molleke 0448.186.520 leftover city_mol YE2024 — take ONLY if unused + official YE2025 native PDF. t Sas 0448.731.106 leftover city_denderleeuw YE2024 only 2026-00050081 — skip unless YE2025. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. KIOS 0882.468.881 leftover city_schoten — no jaarrekening skip unless deposits appear. OpWeg 0443.580.604 leftover city_herentals VAPH YE2024 — take ONLY if unused + official YE2025 native PDF. Dol-Fijn 0439.731.880 zetel Turnhout leftover-via-VE Herentals — not enough. city_kapellen slug missing. WZC Joostens Zoersel = Zorgbedrijf Antwerpen not local VZW. Ter Bake / Rodenbach Denderleeuw Armonea commercial. De Vlietoever Bornem BV commercial. NOT De Hagewinde remine. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT Begeleid Wonen Pajottenland remine. NOT INFANO remine. NOT MWP Lennik remine. NOT Savio remine. NOT EVA Dilbeek remine. NOT CVDO remine. NOT CAR De Klinker Ieper remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT WZC Ten Anker Nieuwpoort remine. NOT Bremdael remine. NOT De Augustientjes remine. NOT Hupskadee remine. NOT Hupskadee BV private. NOT Pardoes remine. NOT Bambi remine. NOT Zonneschijn remine. NOT Infano remine. NOT Vijverbeek remine. NOT Mater Dei remine. NOT 3Wplus remine. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT t Zonnetje remine. NOT Kindercentrum remine. NOT Duinhuisjes remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels leftover-via-VE. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved. NOT Dominiek Savio remine. NOT WZC Mater Dei Heikruis remine. NOT Ferm Kinderopvang remine. NOT Molleke YE2024 remine. NOT t Sas YE2024 remine. NOT Witte Meren remine. NOT Zusterhof remine. NOT Huis Perrekes remine. NOT Sint-Augustinus Halle remine. NOT OLV Bornem remine. NOT AZ Alma remine. NOT AZ Sint-Blasius remine. NOT Philippus Neri YE2024 leftover-via-VE. NOT De Linde Ronse YE2024. NOT De Maretak Korian commercial. NOT Het Veld Vulpia commercial. NOT Laarsveld Armonea commercial. NOT Wedbos OCMW. NOT CAR Glorieux remine. NOT CAR Wegwijs Kloosterstraat 6 Drongen. NOT Pardoes NV bookshop. NOT Olliebollie BV private. NOT In de wolken BV private. NOT Troetelland Geel private BV. NOT De Zandkapoentjes BV private. NOT Armonea Vogelzang/Hemelrijck/Ter Bake commercial. NOT Orelia Koningshof commercial. NOT Stijn leftover-via-VE Hasselt remine. NOT Felies leftover-via-VE Brussels. NOT Klein Hemelrijk absorbed. NOT Sint Lodewijk remine. NOT De Lindeboom remine. NOT De Vier Notelaars remine. NOT Lidwina remine. NOT Homevil remine. NOT Schoonderhage remine. NOT AZ Herentals remine.,"
f",{STAMP},{STAMP},spawned after tick2481 leftover city_lokeren VAPH; De Hagewinde taken; Begeleid Wonen Pajottenland taken leftover mined city_dilbeek VAPH; CVDO taken leftover mined city_knokke_heist CAR; Dennenhof taken leftover mined city_schoten VAPH; Ten Anker taken leftover mined city_waregem VAPH; Bremdael taken leftover mined city_herentals WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2481.count("\n")!=1 or new_2482.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2481",new_2481),("2482",new_2482)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2481.encode("utf-8"))
    f.write(new_2482.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2481", chk.count(b"rq_2481,"), "n2482", chk.count(b"rq_2482,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2481,2481,no,tick2481 leftover dual De Hagewinde 0861.262.010 Strong native PDF (omzet70 JUMP 961172 commercial-only vs large 73; 73 JUMP 24730647; 76A JUMP 10469; envelope 70/76A JUMP 26389520; pnl FLIP LOSS -549643; 9901 DROP 589398; equity JUMP 29744304; assets DROP 35767720; debt DROP 6023416; FTE JUMP 263.2; kapitaalsubsidies JUMP 16311859; destin691 empty; 791 JUMP 1278891; cash JUMP 3546732; geldbeleggingen DROP 7461; 6 VE leftover city_lokeren VAPH); leftover mined city_lokeren VAPH; prior-year identical; NOT Ter Engelen remine; NOT CAR Waas remine; NOT Sakura remine; NOT Kaliber remine; NOT BWP remine; NOT INFANO remine; NOT CVDO remine; NOT Dennenhof remine; NOT Ten Anker remine; NOT Bremdael remine; NOT De Augustientjes remine; NOT Hupskadee remine; NOT Pardoes remine; NOT Bambi remine; NOT Zonneschijn remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Orelia commercial; NOT OpWeg Herentals YE2024; NOT AZ Herentals remine; NOT Huis Perrekes remine; NOT Sint-Augustinus Halle remine; NOT OLV Bornem remine; NOT AZ Alma remine; NOT AZ Sint-Blasius remine; NOT Philippus Neri YE2024 leftover-via-VE; NOT De Linde Ronse YE2024; NOT De Maretak Korian commercial; NOT Het Veld Vulpia commercial; NOT Laarsveld Armonea commercial; NOT Wedbos OCMW; NOT CAR Glorieux remine; NOT CAR Wegwijs Kloosterstraat 6 Drongen; NOT Molleke city_mol YE2024; NOT t Sas city_denderleeuw YE2024 2026-00050081; NOT Dol-Fijn leftover-via-VE; NOT Witte Meren remine; NOT Zusterhof remine; next every-10 is 2490; next rq_2482 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2481 - rq_2481 Zorg en onderwijs De Hagewinde Lokeren (70/76A JUMP 26.39m / omzet commercial vs 73 JUMP 24.73m / pnl FLIP LOSS 550k / 66B 1.20m / Strong PDF)

- Unit: **rq_2481** leftover dual after **BWP@2480**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** of less-picked mined Flanders cities (CIK lists herentals/schoten/vilvoorde/mol exhausted at 2476; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde). Confirmed `city_lokeren` / `city_denderleeuw` / `city_dendermonde` / `city_geel` / `city_herentals` / `city_kalmthout` / `city_bornem` / `city_eeklo` / `city_ronse` / `city_halle` exist (`city_kapellen` missing). FIRST locked: Zorg en onderwijs De Hagewinde **0861.262.010** leftover city_lokeren VAPH unused YE2025 **2026-00276108** VOL 3.0MB — unused + leftover mined parent + official CDN GET **200** 2994546 native extractable euros — **LOCKED**. Skips this hunt: Kaliber Herentals already mined tick2202 (NBB consult still YE2024); Huis Perrekes Geel remine tick2343; Sint-Augustinus Halle remine tick2085; OLV Bornem remine tick2065; AZ Alma remine tick2006; AZ Sint-Blasius remine tick2009; Philippus Neri / Avondzegen YE2024 Sint-Niklaas seat leftover-via-VE; De Linde Ronse YE2024; De Maretak Halle Korian commercial; Het Veld Geel Vulpia commercial; Laarsveld Geel Armonea commercial; Wedbos Geel OCMW; CAR Glorieux = Werken Glorieux remine; CAR Wegwijs Kloosterstraat 6 Drongen stay OFF; Ter Engelen already mined; leftover CIK empty vilvoorde/mol/denderleeuw/zoersel/schilde. Identity trap: 0861.262.010 ≠ Ter Engelen **0430.882.809** ≠ CAR Waas **0415.472.279** ≠ Sakura **0684.613.726** ≠ Kaliber **0407.201.941** ≠ BWP **0423.884.258**. 6 VE leftover of mined city_lokeren (zetel Poststraat 6 + 5 Lokeren VE + 1 Sint-Niklaas school VE). Confirmed leftover public VAPH not convent / not private / not CIK / not WZC. VOL-VZW native statutory (6.1 6.2.2 6.2.3 6.2.4 6.4.1 6.4.2 6.5.2 6.5.3 6.7 6.10 6.14 6.16 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00276108** (2994546 B / 50p; AV **22.06.2026**; header **06.07.2026**; CDN GET **200** 2994546 official NBB-generated OpenPDF 1.3.26 CreationDate 10.07.2026 Last-Modified 29.07.2026 MD5 28e6b209757ae23685d59b3002b197d2; statutory pages native; prior-year identical not restated; commissaris Verifin BV / Van Hemelryck Geert; pages 45–50 Penneo scan) — omzet 70 **EUR961172** JUMP +7.19% (commercial-only vs large 73; was 896728); 73 **EUR24730647** JUMP +10.05% (was 22472637; 731 28579; 733 23843789); 76A **EUR10469** JUMP +319.94% (was 2493); envelope 70/76A **EUR26389520** JUMP +11.13% (VZW envelope because omzet commercial-only vs large 73; was 23747104); 74 **EUR687232** JUMP +83.14%; 62 **EUR20487446** JUMP +10.34%; 630 **EUR1501755** FLAT; 66A **empty**; 66B **EUR1204372** JUMP (VAPH vakantiegeld write-off); 640/8 **EUR64846** DROP; 635/9 **EUR-23812**; 631/4 **empty**; bedrijfswinst 9901 **EUR589398** DROP −24.79% (was 783626); pnl 9904 **EUR-549643** FLIP LOSS (was +869999); equity **EUR29744304** JUMP +1.03%; assets **EUR35767720** DROP −1.25%; debt **EUR6023416** DROP −10.81%; FTE **263.2** JUMP +3.91% (was 253.3; 1003 263.2; 105 268.9; 9086 341); kapitaalsubsidies **EUR16311859** JUMP +5.51%; destin 691 **empty** (was 819999; 791 JUMP 1278891; 13 FLAT 7139848); 791 **EUR1278891** JUMP; cash **EUR3546732** JUMP +5.25%; geldbeleggingen **EUR7461** DROP −99.76% (was 3108511); gebouwen **EUR24679802** JUMP; MVA 22/27 **EUR26959907** JUMP; aanbouw **EUR1353734** JUMP; capex **EUR3062744**. Strong KBO + Strong PDF (native statutory; not SBM table; not Companyweb euros). Site: 6 VE leftover mined city_lokeren VAPH. NOT Ter Engelen remine. NOT CAR Waas remine. NOT Sakura remine. NOT Kaliber remine. NOT BWP remine. NOT CVDO remine. NOT Dennenhof remine. NOT Ten Anker remine. NOT Bremdael remine. NOT Armonea commercial. NOT Vulpia commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.52); entities (+1 vzw_hagewinde_lokeren); foi + draft `gap_hagewinde_lokeren_vaph_matrix_70_76A_26_39m_omzet_commercial_73_jump_24_73m_pnl_flip_loss_550k_66B_1_20m_l5`; rq_2481=done + rq_2482 open; loop_state ticks=2481; raw tick2481/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2482 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT De Hagewinde remine / NOT Ter Engelen remine / NOT CAR Waas remine / NOT Sakura remine / NOT Kaliber remine / NOT BWP remine / NOT CVDO remine / NOT Dennenhof remine / NOT Ten Anker remine / NOT Bremdael remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Huis Perrekes remine / NOT Sint-Augustinus Halle remine / NOT OLV Bornem remine).

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
