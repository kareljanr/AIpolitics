from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2460_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_hocus_jr2025_nbb_pdf_2460"
SRC_KBO="src_hocus_kbo_2460"
SRC_SBM="src_hocus_sbm_2460"
SRC_SITE="src_hocus_site_2460"
EID="vzw_hocus_pocus_roeselare"
GAP="gap_hocus_opgroeien_matrix_opbr_2_48m_omzet_459k_73_1_91m_pnl_jump_432k_destin_jump_600k_l5"
COMM="comm_hocus_jr2025_statutory_opbr_2_48m_omzet_459k_73_1_91m_pnl_jump_432k"
LB="lb_hocus_opbr_2_48m_omzet_459k_73_1_91m_pnl_jump_432k_destin_jump_600k_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 HOCUS-POCUS deposit 2026-00151355,http://cdn.staatsbladmonitor.be/2026pdf/2026-00151355.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2460; official native PDF 58808 bytes 18p VKT-VZW 23.0.9 m04-f; header 04.06.2026; AV 10.05.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-06-11 04:30:15 UTC OpenPDF 1.3.26; all 18p native; CDN 2026-00151355 HEAD 200 Last-Modified 18.06.2026; VKT-VZW 6.1.1 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO HOCUS-POCUS 0466.893.167,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0466893167,KBO Public Search FOD Economie,{DAY},official_register,tick2460; Actief; 2 VE 2.159.181.396 HOCUS-POCUS Vierwegstraat 205 8800 Roeselare since 05.02.2007 + 2.312.440.606 HOCUS-POCUS Iepersestraat 68-70 8800 Roeselare since 18.05.2020; VZW since 30.05.1999; begindatum 30.05.1999; zetel Vierwegstraat 205 8800 Roeselare since 30.05.1999; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@opvanghocuspocus.be; leftover mined city_roeselare CIK; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche HOCUS-POCUS 0466893167 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0466893167,NBB Consult / SBM,{DAY},official_register,tick2460; deposit-id 2026-00151355 YE 01.01.2025-31.12.2025 filing 04.06.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},HOCUS-POCUS FOI contact leftover city_roeselare CIK,https://www.kinderopvangwijzer.be/roeselare/initiatief/groepsopvang-hocus-pocus/,VZW HOCUS-POCUS leftover city_roeselare CIK Kind en Gezin-vergunde groepsopvang,{DAY},foi_contact,tick2460; FOI info@opvanghocuspocus.be; zetel Vierwegstraat 205 8800 Roeselare; 2 VE leftover mined city_roeselare after VKA different-city skip; NOT Kloosterstraat 6 Drongen; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},HOCUS-POCUS vzw,ASBL HOCUS-POCUS,HOCUS-POCUS VZW (leftover city_roeselare CIK),parastatal,city_roeselare,nl,https://www.kinderopvangwijzer.be/roeselare/initiatief/groepsopvang-hocus-pocus/,info@opvanghocuspocus.be,Vierwegstraat 205 8800 Roeselare,tick2460 YE2025 Strong official native NBB PDF deposit 2026-00151355 + Strong KBO 0466.893.167 Actief 2 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 JUMP 458986 commercial-only; 73 JUMP 1910358; 76A JUMP 108232; envelope 70/76A JUMP 2477576; bruto JUMP 2072280 VKT present; pnl JUMP 432178; 9901 JUMP 485581; equity JUMP 1009274; assets JUMP 2080620; debt DROP 1003346; FTE 24.8 JUMP; kapitaalsubsidies empty; destin691 JUMP 600000; 791 empty; cash JUMP 170123; geldbeleggingen empty; leftover mined city_roeselare after VKA different-city skip; 2 VE CIK groepsopvang not private; NOT Kloosterstraat 6 Drongen; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT H.Hart WZC 0413.595.330; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_hocus_omzet_jr2025_statutory,{EID},2025,458986,458986,458986,NBB VKT-VZW code 70 omzet YE2025 JUMP +4.57% (commercial-only vs large 73; envelope is 70/76A),{SRC_PDF},strong,tick2460; PDF p5 native; YE2024 identical 438935; 73 1910358 JUMP",
f"bud_hocus_73_jr2025_statutory,{EID},2025,1910358,1910358,1910358,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +21.00%,{SRC_PDF},strong,tick2460; PDF p5 native; YE2024 identical 1578845; FOI Opgroeien split behind envelope 2477576",
f"bud_hocus_opbr_jr2025_statutory,{EID},2025,2477576,2477576,2477576,NBB VKT-VZW envelope 70/76A YE2025 JUMP +17.81% (omzet 458986 commercial-only + 73 1910358 + 76A 108232),{SRC_PDF},strong,tick2460; PDF p5 native; YE2024 identical 2103036; bruto 9900 also 2072280 VKT present but envelope is 70/76A because omzet not empty",
f"bud_hocus_bruto_jr2025_statutory,{EID},2025,2072280,2072280,2072280,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +16.03% (VKT present; envelope remains 70/76A because omzet not empty),{SRC_PDF},strong,tick2460; PDF p5 native; YE2024 identical 1785933; 76A 108232 JUMP",
f"bud_hocus_pnl_jr2025_statutory,{EID},2025,432178,432178,432178,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +123.05% (was 193761),{SRC_PDF},strong,tick2460; PDF p5 native; YE2024 identical 193761; bedrijfswinst 9901 485581 JUMP; destin691 JUMP 600000",
f"bud_hocus_bedrijfswinst_jr2025_statutory,{EID},2025,485581,485581,485581,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +27.29% (was 381471),{SRC_PDF},strong,tick2460; PDF p5 native; YE2024 identical 381471; 62 1352020 JUMP; 630 119333 JUMP; 66A 54188 JUMP",
f"bud_hocus_equity_jr2025_statutory,{EID},2025,1009274,1009274,1009274,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +68.63%,{SRC_PDF},strong,tick2460; PDF p4 native; YE2024 identical 598511; kapitaalsubsidies empty; overgedragen 14 148969 DROP; fondsen 10 empty; bestemde fondsen 13 600000 JUMP",
f"bud_hocus_assets_jr2025_statutory,{EID},2025,2080620,2080620,2080620,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +21.79%,{SRC_PDF},strong,tick2460; PDF p3 native; YE2024 identical 1708404; MVA 22/27 1146195 JUMP; cash 170123 JUMP; geldbeleggingen empty; aanbouw 27 133100 JUMP",
f"bud_hocus_debt_jr2025_statutory,{EID},2025,1003346,1003346,1003346,NBB VKT-VZW code 17/49 schulden YE2025 DROP -9.03%,{SRC_PDF},strong,tick2460; PDF p4 native; YE2024 identical 1102893; 17 476400 DROP; 42/48 526946 JUMP",
f"bud_hocus_cash_jr2025_statutory,{EID},2025,170123,170123,170123,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +28.42%,{SRC_PDF},strong,tick2460; PDF p3 native; YE2024 identical 132475; geldbeleggingen 50/53 empty",
f"bud_hocus_destin_jr2025_statutory,{EID},2025,600000,600000,600000,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (600000 vs pnl 432178; 791 empty; 14P 316791 also moved),{SRC_PDF},strong,tick2460; PDF p6 native; YE2024 destin empty; bestemde fondsen 13 600000 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":458986,\"\"2025_73\"\":1910358,\"\"2025_76A\"\":108232,"
"\"\"2025_opbr70_76A\"\":2477576,\"\"2025_bruto\"\":2072280,"
"\"\"2025_pnl\"\":432178,\"\"2025_bedrijfswinst\"\":485581,"
"\"\"2025_equity\"\":1009274,\"\"2025_assets\"\":2080620,\"\"2025_debt\"\":1003346,"
"\"\"2025_fte\"\":24.8,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":600000,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":170123,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":1352020,\"\"2025_gebouwen22\"\":976103,"
"\"\"2025_aanbouw27\"\":133100,\"\"2025_66A\"\":54188,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":148969,"
"\"\"2025_bestemdefondsen13\"\":600000,"
"\"\"2025_voorzieningen16\"\":68000,\"\"2025_630\"\":119333,\"\"2025_capex\"\":229399,"
"\"\"2024_omzet\"\":438935,\"\"2024_73\"\":1578845,"
"\"\"2024_opbr70_76A\"\":2103036,\"\"2024_bruto\"\":1785933,\"\"2024_pnl\"\":193761,\"\"2024_bedrijfswinst\"\":381471,"
"\"\"2024_equity\"\":598511,\"\"2024_assets\"\":1708404,"
"\"\"2024_debt\"\":1102893,\"\"2024_cash\"\":132475,\"\"2024_fte\"\":21.6,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":85256,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},HOCUS-POCUS YE2025 (opbr JUMP 2.48m / omzet JUMP 459k commercial-only / 73 JUMP 1.91m / pnl JUMP 432k / destin JUMP 600k / Strong PDF),{EID},Opgroeien + leftover city_roeselare CIK,VZW HOCUS-POCUS (KBO 0466.893.167; Actief; 2 VE; RSZ2025 88.911; zetel + 2/2 VE Roeselare),2026-05-10,2025,2025,2477576,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00151355.pdf,Public CIK dual of mined city_roeselare,Publish Opgroeien matrix behind opbr 2.48m + why omzet 459k commercial-only vs 73 1.91m + why pnl JUMP 432k while destin JUMP 600k and cash JUMP 170k and FTE JUMP 24.8,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Roeselare>HocusPocus>JR2025_statutory_L5,tick2460; Strong official native PDF; leftover mined city_roeselare CIK; 2 VE; EVERY-10; NOT Kloosterstraat 6 Drongen; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"HOCUS-POCUS opbr JUMP 2.48m / omzet JUMP 459k commercial-only / 73 JUMP 1.91m / pnl JUMP 432k / destin JUMP 600k (YE2025 leftover city_roeselare CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Roeselare>HocusPocus>JR2025",
"2477576",
"2477576",
"PDF 70/76A 2477576 envelope; omzet 458986 commercial-only; 73 1910358; 76A 108232; bruto JUMP 2072280 VKT present; bedrijfswinst JUMP 485581; pnl JUMP 432178; equity JUMP 1009274; assets JUMP 2080620; debt DROP 1003346; FTE 24.8 JUMP; kapitaalsubsidies empty; destin691 JUMP 600000; cash JUMP 170123; geldbeleggingen empty; 2 VE leftover city_roeselare CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_roeselare CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_roeselare",
"2.48m opbr envelope; omzet 459k commercial-only vs 73 1.91m; pnl JUMP 432k; destin JUMP 600k; cash JUMP 170k; leftover city_roeselare CIK",
"5.15",
"5.20",
"5.00",
"5.16",
"FOI Opgroeien matrix behind opbr 2.48m + why omzet 459k commercial-only vs 73 1.91m + why pnl JUMP 432k while destin JUMP 600k and cash JUMP 170k and FTE JUMP 24.8",
"active",
"",
"tick2460 leftover mined city_roeselare CIK after VKA different-city skip; EVERY-10; 2 VE; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Roeselare>HocusPocus>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind opbr 2477576 (omzet 70 458986 commercial-only + 73 1910358 + 76A 108232) and why pnl JUMP 432178 while destin JUMP 600000 and cash JUMP 170123 and FTE JUMP 24.8",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_roeselare; 2.48m opbr envelope; public Kind en Gezin-vergunde groepsopvang",
"priority": "8",
"recipient_body": "VZW HOCUS-POCUS / Raad van Bestuur",
"recipient_email": "info@opvanghocuspocus.be",
"recipient_postal": "Vierwegstraat 205 8800 Roeselare",
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
"notes": "tick2460; ready NOT sent; Strong official native NBB PDF; leftover mined city_roeselare CIK after VKA different-city skip; 2 VE; EVERY-10; off Drongen",
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
if rq_raw.count(b"rq_2460,")!=1: raise SystemExit(f"bad 2460 count {rq_raw.count(b'rq_2460,')}")
if b"rq_2461," in rq_raw: raise SystemExit("2461 exists")
idx=rq_raw.rfind(b"rq_2460,")
if idx<0: raise SystemExit("rq_2460 not found")
new_2460=(
"rq_2460,leftover dual HOCUS-POCUS YE2025 + EVERY-10,hole_fill,8,done,L5,vzw_hocus_pocus_roeselare,"
"Took unused leftover public CIK HOCUS-POCUS 0466.893.167 leftover mined city_roeselare. Official NBB VKT-VZW YE2025 2026-00151355 native 18p. Envelope 70/76A JUMP 2477576; omzet JUMP 458986 commercial-only; 73 JUMP 1910358; pnl JUMP 432178; destin JUMP 600000. EVERY-10 refresh. NOT VKA remine. NOT Soetkin remine.,"
f",{STAMP},{STAMP},tick2460 leftover mined city_roeselare CIK; Strong native PDF; 2 VE; EVERY-10; next every-10 is 2470\n"
)
new_2461=(
"rq_2461,leftover dual after HOCUS-POCUS — hunt unused public dual,hole_fill,8,open,L5,,"
"After HOCUS-POCUS YE2025 EVERY-10. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. Gesticht der Zusters van de H. Vincentius 0410.918.031 leftover city_ieper YE2025 — take ONLY if unused leftover public + official native YE2025 PDF (convent-class check). NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2460; Hocus-Pocus taken leftover mined city_roeselare CIK EVERY-10; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2460.count("\n")!=1 or new_2461.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2460.encode("utf-8"))
    f.write(new_2461.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2460", chk.count(b"rq_2460,"), "n2461", chk.count(b"rq_2461,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2460,2460,no,tick2460 leftover dual HOCUS-POCUS 0466.893.167 Strong native PDF EVERY-10 (omzet70 JUMP 458986 commercial-only; 73 JUMP 1910358; 76A JUMP 108232; envelope 70/76A JUMP 2477576; bruto JUMP 2072280 VKT present; pnl JUMP 432178; 9901 JUMP 485581; equity JUMP 1009274; assets JUMP 2080620; debt DROP 1003346; FTE 24.8 JUMP; kapitaalsubsidies empty; destin691 JUMP 600000; 791 empty; cash JUMP 170123; geldbeleggingen empty; 2 VE leftover city_roeselare CIK); leftover mined city_roeselare CIK; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; next every-10 is 2470; next rq_2461 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")
print("WRITE CORE DONE")
