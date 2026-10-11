from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2461_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_gesticht_jr2025_nbb_pdf_2461"
SRC_KBO="src_gesticht_kbo_2461"
SRC_SBM="src_gesticht_sbm_2461"
SRC_SITE="src_gesticht_site_2461"
EID="vzw_gesticht_zusters_ieper"
GAP="gap_gesticht_opgroeien_matrix_opbr_3_16m_omzet_770k_73_2_39m_pnl_jump_324k_destin_empty_l5"
COMM="comm_gesticht_jr2025_statutory_opbr_3_16m_omzet_770k_73_2_39m_pnl_jump_324k"
LB="lb_gesticht_opbr_3_16m_omzet_770k_73_2_39m_pnl_jump_324k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Gesticht der Zusters van de H. Vincentius deposit 2026-00236818,http://cdn.staatsbladmonitor.be/2026pdf/2026-00236818.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2461; official native PDF 386167 bytes 26p VKT-VZW 26.0.15 m04-f; header 29.06.2026; AV 10.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-02 09:28:03 UTC OpenPDF 1.3.26; all 26p native; CDN 2026-00236818 HEAD 200 Last-Modified 24.07.2026; VKT-VZW 6.1.1 6.1.3 7 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Gesticht der Zusters van de H. Vincentius 0410.918.031,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410918031,KBO Public Search FOD Economie,{DAY},official_register,tick2461; Actief; 2 VE 2.153.745.240 Gesticht der Zusters van de Heilige Vincentius de Stuersstraat 32 8900 Ieper since 30.05.2006 + 2.216.097.830 Minneke poes Robrecht van Bethunelaan 1 8900 Ieper since 01.01.2013; VZW since 16.05.1924; begindatum 16.05.1924; zetel Robrecht van Bethunelaan 1 8900 Ieper since 25.10.2023; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@kinderopvangieper.be; leftover mined city_ieper CIK; convent-class check PASSED (2 VE FTE 25.6 omzet+73 present); NOT Grauwzusters 0409.771.748 convent; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Gesticht der Zusters 0410918031 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0410918031,NBB Consult / SBM,{DAY},official_register,tick2461; deposit-id 2026-00236818 YE 01.01.2025-31.12.2025 filing 29.06.2026 published 02.07.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Gesticht der Zusters / Minneke Poes FOI contact leftover city_ieper CIK,https://www.kinderopvangieper.be/,VZW Gesticht der Zusters van de H. Vincentius leftover city_ieper CIK Kind en Gezin-vergunde groepsopvang,{DAY},foi_contact,tick2461; FOI info@kinderopvangieper.be; zetel Robrecht van Bethunelaan 1 8900 Ieper; 2 VE leftover mined city_ieper after HOCUS-POCUS different-city skip; Minneke Poes HCO 910027272; NOT Kloosterstraat 6 Drongen; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Grauwzusters convent",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Gesticht der Zusters van de H. Vincentius,ASBL Gesticht der Zusters van de H. Vincentius,Gesticht der Zusters van de H. Vincentius VZW (leftover city_ieper CIK),parastatal,city_ieper,nl,https://www.kinderopvangieper.be/,info@kinderopvangieper.be,Robrecht van Bethunelaan 1 8900 Ieper,tick2461 YE2025 Strong official native NBB PDF deposit 2026-00236818 + Strong KBO 0410.918.031 Actief 2 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; convent-class check PASSED; omzet70 DROP 769820 commercial-only; 73 JUMP 2387710; 76A empty; envelope 70/76A JUMP 3157530; bruto JUMP 2127224 VKT present; pnl JUMP 323957; 9901 JUMP 330869; equity JUMP 5006689; assets JUMP 6808404; debt DROP 1801715; FTE 25.6 JUMP; kapitaalsubsidies DROP 1341554; destin691 empty; 791 empty; cash DROP 1007825; geldbeleggingen DROP 1368669; leftover mined city_ieper after HOCUS-POCUS different-city skip; 2 VE CIK groepsopvang not convent not private; NOT Kloosterstraat 6 Drongen; NOT Grauwzusters 0409.771.748 convent; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT H.Hart WZC 0413.595.330; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT BOI Ieper remine; NOT Huize Zonnelied remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_gesticht_omzet_jr2025_statutory,{EID},2025,769820,769820,769820,NBB VKT-VZW code 70 omzet YE2025 DROP -6.58% (commercial-only vs large 73; envelope is 70/76A),{SRC_PDF},strong,tick2461; PDF p6 native; YE2024 identical 824216; 73 2387710 JUMP",
f"bud_gesticht_73_jr2025_statutory,{EID},2025,2387710,2387710,2387710,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +8.58%,{SRC_PDF},strong,tick2461; PDF p6 native; YE2024 identical 2199102; FOI Opgroeien split behind envelope 3157530",
f"bud_gesticht_opbr_jr2025_statutory,{EID},2025,3157530,3157530,3157530,NBB VKT-VZW envelope 70/76A YE2025 JUMP +4.44% (omzet 769820 commercial-only + 73 2387710 + 76A empty),{SRC_PDF},strong,tick2461; PDF p6 native; YE2024 identical 3023318; bruto 9900 also 2127224 VKT present but envelope is 70/76A because omzet not empty",
f"bud_gesticht_bruto_jr2025_statutory,{EID},2025,2127224,2127224,2127224,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +11.82% (VKT present; envelope remains 70/76A because omzet not empty),{SRC_PDF},strong,tick2461; PDF p6 native; YE2024 identical 1902287; 76A empty",
f"bud_gesticht_pnl_jr2025_statutory,{EID},2025,323957,323957,323957,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +0.25% (was 323152),{SRC_PDF},strong,tick2461; PDF p6 native; YE2024 identical 323152; bedrijfswinst 9901 330869 JUMP; destin691 empty",
f"bud_gesticht_bedrijfswinst_jr2025_statutory,{EID},2025,330869,330869,330869,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +34.72% (was 245601),{SRC_PDF},strong,tick2461; PDF p6 native; YE2024 identical 245601; 62 1631057 JUMP; 630 165268 DROP; 66A empty",
f"bud_gesticht_equity_jr2025_statutory,{EID},2025,5006689,5006689,5006689,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +5.39%,{SRC_PDF},strong,tick2461; PDF p5 native; YE2024 identical 4750785; kapitaalsubsidies 1341554 DROP; overgedragen 14 3001292 JUMP; fondsen 10 63843 FLAT; bestemde fondsen 13 600000 FLAT Bouwfonds",
f"bud_gesticht_assets_jr2025_statutory,{EID},2025,6808404,6808404,6808404,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +2.87%,{SRC_PDF},strong,tick2461; PDF p4 native; YE2024 identical 6618143; MVA 22/27 3839725 DROP; cash 1007825 DROP; geldbeleggingen 1368669 DROP; aanbouw 27 empty",
f"bud_gesticht_debt_jr2025_statutory,{EID},2025,1801715,1801715,1801715,NBB VKT-VZW code 17/49 schulden YE2025 DROP -3.51%,{SRC_PDF},strong,tick2461; PDF p5 native; YE2024 identical 1867358; 17 1134722 DROP; 42/48 654022 JUMP",
f"bud_gesticht_cash_jr2025_statutory,{EID},2025,1007825,1007825,1007825,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -9.19%,{SRC_PDF},strong,tick2461; PDF p4 native; YE2024 identical 1109840; geldbeleggingen 50/53 1368669 DROP",
f"bud_gesticht_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (destin empty vs pnl 323957; 13 Bouwfonds 600000 FLAT),{SRC_PDF},strong,tick2461; PDF p7 native; YE2024 destin empty; bestemde fondsen 13 600000 FLAT FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":769820,\"\"2025_73\"\":2387710,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":3157530,\"\"2025_bruto\"\":2127224,"
"\"\"2025_pnl\"\":323957,\"\"2025_bedrijfswinst\"\":330869,"
"\"\"2025_equity\"\":5006689,\"\"2025_assets\"\":6808404,\"\"2025_debt\"\":1801715,"
"\"\"2025_fte\"\":25.6,\"\"2025_kapitaalsubsidies\"\":1341554,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1007825,\"\"2025_geldbeleggingen\"\":1368669,"
"\"\"2025_personnel62\"\":1631057,\"\"2025_gebouwen22\"\":3658299,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":63843,\"\"2025_overgedragen14\"\":3001292,"
"\"\"2025_bestemdefondsen13\"\":600000,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":165268,\"\"2025_capex\"\":23484,"
"\"\"2024_omzet\"\":824216,\"\"2024_73\"\":2199102,"
"\"\"2024_opbr70_76A\"\":3023318,\"\"2024_bruto\"\":1902287,\"\"2024_pnl\"\":323152,\"\"2024_bedrijfswinst\"\":245601,"
"\"\"2024_equity\"\":4750785,\"\"2024_assets\"\":6618143,"
"\"\"2024_debt\"\":1867358,\"\"2024_cash\"\":1109840,\"\"2024_fte\"\":21.4,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1409607,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":1393814}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Gesticht der Zusters van de H. Vincentius YE2025 (opbr JUMP 3.16m / omzet DROP 770k commercial-only / 73 JUMP 2.39m / pnl JUMP 324k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_ieper CIK,VZW Gesticht der Zusters van de H. Vincentius (KBO 0410.918.031; Actief; 2 VE; RSZ2025 88.911; zetel + 2/2 VE Ieper),2026-06-10,2025,2025,3157530,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00236818.pdf,Public CIK dual of mined city_ieper,Publish Opgroeien matrix behind opbr 3.16m + why omzet 770k commercial-only vs 73 2.39m + why pnl JUMP 324k while destin empty and cash DROP 1.01m and FTE JUMP 25.6,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Ieper>GestichtZusters>JR2025_statutory_L5,tick2461; Strong official native PDF; leftover mined city_ieper CIK; convent-class check PASSED; 2 VE; NOT every-10; NOT Kloosterstraat 6 Drongen; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Gesticht der Zusters van de H. Vincentius opbr JUMP 3.16m / omzet DROP 770k commercial-only / 73 JUMP 2.39m / pnl JUMP 324k / destin empty (YE2025 leftover city_ieper CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Ieper>GestichtZusters>JR2025",
"3157530",
"3157530",
"PDF 70/76A 3157530 envelope; omzet 769820 commercial-only; 73 2387710; 76A empty; bruto JUMP 2127224 VKT present; bedrijfswinst JUMP 330869; pnl JUMP 323957; equity JUMP 5006689; assets JUMP 6808404; debt DROP 1801715; FTE 25.6 JUMP; kapitaalsubsidies DROP 1341554; destin691 empty; cash DROP 1007825; geldbeleggingen DROP 1368669; 2 VE leftover city_ieper CIK convent-class check PASSED",
"strong",
SRC_PDF,
"Opgroeien + leftover city_ieper CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_ieper",
"3.16m opbr envelope; omzet 770k commercial-only vs 73 2.39m; pnl JUMP 324k; destin empty; cash DROP 1.01m; leftover city_ieper CIK",
"5.17",
"5.22",
"5.00",
"5.18",
"FOI Opgroeien matrix behind opbr 3.16m + why omzet 770k commercial-only vs 73 2.39m + why pnl JUMP 324k while destin empty and cash DROP 1.01m and FTE JUMP 25.6",
"active",
"",
"tick2461 leftover mined city_ieper CIK after HOCUS-POCUS different-city skip; convent-class check PASSED; 2 VE; NOT every-10; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Ieper>GestichtZusters>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind opbr 3157530 (omzet 70 769820 commercial-only + 73 2387710 + 76A empty) and why pnl JUMP 323957 while destin empty and cash DROP 1007825 and FTE JUMP 25.6",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_ieper; 3.16m opbr envelope; public Kind en Gezin-vergunde groepsopvang; convent-class check PASSED",
"priority": "8",
"recipient_body": "VZW Gesticht der Zusters van de H. Vincentius / Raad van Bestuur",
"recipient_email": "info@kinderopvangieper.be",
"recipient_postal": "Robrecht van Bethunelaan 1 8900 Ieper",
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
"notes": "tick2461; ready NOT sent; Strong official native NBB PDF; leftover mined city_ieper CIK after HOCUS-POCUS different-city skip; convent-class check PASSED; 2 VE; NOT every-10; off Drongen",
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
if rq_raw.count(b"rq_2461,")!=1: raise SystemExit(f"bad 2461 count {rq_raw.count(b'rq_2461,')}")
if b"rq_2462," in rq_raw: raise SystemExit("2462 exists")
idx=rq_raw.rfind(b"rq_2461,")
if idx<0: raise SystemExit("rq_2461 not found")
new_2461=(
"rq_2461,leftover dual Gesticht der Zusters van de H. Vincentius YE2025,hole_fill,8,done,L5,vzw_gesticht_zusters_ieper,"
"Took unused leftover public CIK Gesticht der Zusters van de H. Vincentius 0410.918.031 leftover mined city_ieper. Official NBB VKT-VZW YE2025 2026-00236818 native 26p. Envelope 70/76A JUMP 3157530; omzet DROP 769820 commercial-only; 73 JUMP 2387710; pnl JUMP 323957; destin empty. Convent-class check PASSED. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine.,"
f",{STAMP},{STAMP},tick2461 leftover mined city_ieper CIK; Strong native PDF; 2 VE; convent-class check PASSED; next every-10 is 2470\n"
)
new_2462=(
"rq_2462,leftover dual after Gesticht der Zusters — hunt unused public dual,hole_fill,8,open,L5,,"
"After Gesticht der Zusters YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2461; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2461.count("\n")!=1 or new_2462.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2461.encode("utf-8"))
    f.write(new_2462.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2461", chk.count(b"rq_2461,"), "n2462", chk.count(b"rq_2462,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2461,2461,no,tick2461 leftover dual Gesticht der Zusters 0410.918.031 Strong native PDF (omzet70 DROP 769820 commercial-only; 73 JUMP 2387710; 76A empty; envelope 70/76A JUMP 3157530; bruto JUMP 2127224 VKT present; pnl JUMP 323957; 9901 JUMP 330869; equity JUMP 5006689; assets JUMP 6808404; debt DROP 1801715; FTE 25.6 JUMP; kapitaalsubsidies DROP 1341554; destin691 empty; 791 empty; cash DROP 1007825; geldbeleggingen DROP 1368669; 2 VE leftover city_ieper CIK convent-class check PASSED); leftover mined city_ieper CIK; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; next every-10 is 2470; next rq_2462 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2461 - rq_2461 Gesticht der Zusters van de H. Vincentius (opbr JUMP 3.16m / omzet DROP 770k commercial-only / 73 JUMP 2.39m / pnl JUMP 324k / destin empty / Strong PDF)

- Unit: **rq_2461** leftover dual after **HOCUS-POCUS@2460**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. De Bolster 0861.680.989 still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. CAR Overleie 0454.250.505 still **YE2024**. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle CDN still **403**. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024** (filed 14.08.2025). Kinderlach leftover city_eeklo still **YE2024** (filed 15.07.2025). Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024** (filed 26.06.2025). Jessa leftover city_hasselt hospital — no usable 2026pdf / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024** (filed 25.02.2026). Zo Groot Oostende leftover city_oostende still **YE2024** (filed 17.03.2026). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. HOCUS-POCUS 0466.893.167 just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Gesticht der Zusters van de H. Vincentius** YE2025 (KBO **0410.918.031**; zetel Robrecht van Bethunelaan 1 8900 Ieper; **Actief** **2 VE** **2.153.745.240** Gesticht der Zusters van de Heilige Vincentius de Stuersstraat 32 since 30.05.2006 + **2.216.097.830** Minneke poes Robrecht van Bethunelaan 1 since 01.01.2013; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover of mined **city_ieper**; info@kinderopvangieper.be). Convent-class check **PASSED** (2 VE; FTE 25.6; omzet 70 769820 + 73 2387710; Kinderopvang toelating; commissaris; sociale balans; optie nieuw kinderdagverblijf — NOT 0 VE / empty 73/omzet / no FTE / destin fonds for zusters like Grauwzusters). Identity trap: Gesticht der Zusters 0410.918.031 ≠ Grauwzusters **0409.771.748** convent skip; ≠ HOCUS-POCUS **0466.893.167** leftover city_roeselare just mined; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ BOI Ieper **0431.691.669**; ≠ Huize Zonnelied **0415.082.497**; ≠ Wintershove **0459.245.312**; ≠ TKDV Het Veer Kloosterstraat 6. 2 VE both Ieper — leftover of mined city_ieper (zetel + 2/2 VE). Confirmed leftover public (Opgroeien CIK groepsopvang Minneke Poes HCO 910027272; Kind en Gezin-vergunde) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not HOCUS-POCUS remine. VKT-VZW **native text** (not scan) — 386167 B / 26p all native euros (VKT-VZW 6.1.1 / 6.1.3 / 7 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00236818** (386167 B / 26p; AV **10.06.2026**; header **29.06.2026**; CDN Last-Modified **24.07.2026**; CreationDate 02.07.2026 OpenPDF 1.3.26; all 26p native; prior-year identical not restated) — omzet 70 **EUR769820** DROP −6.58% (commercial-only vs large 73); 73 **EUR2387710** JUMP +8.58%; 76A **empty**; envelope 70/76A **EUR3157530** JUMP +4.44%; bruto 9900 **EUR2127224** JUMP +11.82% (VKT present; envelope remains 70/76A because omzet not empty); 62 **EUR1631057** JUMP +9.62%; 630 **EUR165268** DROP −1.67%; 66A **empty**; 640/8 **EUR31** FLAT; bedrijfswinst 9901 **EUR330869** JUMP +34.72%; pnl 9904 **EUR323957** JUMP +0.25%; equity **EUR5006689** JUMP +5.39%; assets **EUR6808404** JUMP +2.87%; debt **EUR1801715** DROP −3.51%; FTE **25.6** JUMP +19.63% (was 21.4; 9087 25.6; 105 25.2); kapitaalsubsidies **EUR1341554** DROP −4.83%; destin 691 **empty** FLAT (destin empty vs pnl 323957; 13 Bouwfonds 600000 FLAT); 791 **empty**; cash **EUR1007825** DROP −9.19%; geldbeleggingen **EUR1368669** DROP −1.80%; gebouwen **EUR3658299** DROP; MVA 22/27 **EUR3839725** DROP; aanbouw **empty**; capex **EUR23484**; fondsen 10 **EUR63843** FLAT; overgedragen 14 **EUR3001292** JUMP; bestemde fondsen 13 **EUR600000** FLAT; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 2 VE leftover mined city_ieper CIK. NOT Kloosterstraat 6 Drongen. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.18); entities (+1 vzw_gesticht_zusters_ieper); foi + draft `gap_gesticht_opgroeien_matrix_opbr_3_16m_omzet_770k_73_2_39m_pnl_jump_324k_destin_empty_l5`; rq_2461=done + rq_2462 open; loop_state ticks=2461; raw tick2461/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2462 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine). NOW leftover candidate: Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital — take ONLY if unused + official YE2025 euros extract. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip unless LOOP.md leftover training priority. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
