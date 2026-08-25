from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2466_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_paideia_jr2025_nbb_pdf_2466"
SRC_KBO="src_paideia_kbo_2466"
SRC_SBM="src_paideia_sbm_2466"
SRC_SITE="src_paideia_site_2466"
EID="vzw_paideia_brugge"
GAP="gap_paideia_opgroeien_matrix_bruto_2_53m_omzet73_empty_pnl_drop_141k_destin_empty_l5"
COMM="comm_paideia_jr2025_statutory_bruto_2_53m_omzet73_empty_pnl_drop_141k"
LB="lb_paideia_bruto_2_53m_omzet73_empty_pnl_drop_141k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Paideia deposit 2026-00259827,http://cdn.staatsbladmonitor.be/2026pdf/2026-00259827.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2466; official native PDF 54226 bytes 16p VKT-VZW 26.0.15 m04-f; header 06.07.2026; AV 09.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-07 06:19:24 UTC OpenPDF 1.3.26; all 16p native; CDN 2026-00259827 GET 200 Last-Modified 27.07.2026; VKT-VZW 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Paideia 0445.129.931,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0445129931,KBO Public Search FOD Economie,{DAY},official_register,tick2466; Actief; 5 VE all Brugge; VZW since 13.03.1991; begindatum 13.03.1991; zetel Koude-Keukenstraat 8B 8200 Brugge since 04.02.2021; Werkgever RSZ since 15.03.1997; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI secretariaat@ibokakelbont.net; leftover mined city_brugge CIK; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine",
f"{SRC_SBM},NBB Consult / SBM fiche Paideia 0445129931 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0445129931,NBB Consult / SBM,{DAY},official_register,tick2466; deposit-id 2026-00259827 YE 01.01.2025-31.12.2025 filing 06.07.2026 published 06.07.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Paideia FOI contact leftover city_brugge CIK,https://www.ibokakelbont.net/,VZW Paideia leftover city_brugge CIK Opgroeien groepsopvang KDV Hermelijn + BKO Kakelbont,{DAY},foi_contact,tick2466; FOI secretariaat@ibokakelbont.net; zetel Koude-Keukenstraat 8B 8200 Brugge; 5 VE leftover mined city_brugge after Ooievaarsnest different-city skip; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Paideia,ASBL Paideia,Paideia VZW (leftover city_brugge CIK),parastatal,city_brugge,nl,https://www.ibokakelbont.net/,secretariaat@ibokakelbont.net,Koude-Keukenstraat 8B 8200 Brugge,tick2466 YE2025 Strong official native NBB PDF deposit 2026-00259827 + Strong KBO 0445.129.931 Actief 5 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto JUMP 2530206 envelope; pnl DROP 141275; 9901 DROP 146737; equity JUMP 1029234; assets JUMP 1887493; debt JUMP 858259; FTE 38.5 JUMP; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 293729; geldbeleggingen JUMP 501400; 5 VE leftover city_brugge CIK; NOT Ooievaarsnest 0418.588.256 remine; NOT DE ZONNEKINDJES 0416.541.952 remine; NOT D'n Opvang 0676.442.465 remine; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT De Elfjes 0455.636.912 remine; NOT De Steijgertjes 0413.421.720 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; NOT Vormingscentrum 0413.342.338 training; NOT Zwarte Zusters 0413.272.260 dissolved; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_paideia_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900 because omzet empty),{SRC_PDF},strong,tick2466; PDF p6 native; YE2024 identical empty; 73 empty; 76A empty",
f"bud_paideia_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2466; PDF p6 native; YE2024 identical empty; FOI Opgroeien matrix behind bruto 2530206",
f"bud_paideia_opbr_jr2025_statutory,{EID},2025,2530206,2530206,2530206,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +18.29% (omzet 70 empty + 73 empty so VKT envelope is 9900; 76A empty),{SRC_PDF},strong,tick2466; PDF p6 native; YE2024 identical 2139018; 70 empty; 73 empty",
f"bud_paideia_bruto_jr2025_statutory,{EID},2025,2530206,2530206,2530206,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +18.29% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2466; PDF p6 native; YE2024 identical 2139018; 76A empty; 73 empty",
f"bud_paideia_pnl_jr2025_statutory,{EID},2025,141275,141275,141275,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -31.70% (was 206858),{SRC_PDF},strong,tick2466; PDF p6 native; YE2024 identical 206858; bedrijfswinst 9901 146737 DROP; destin691 empty",
f"bud_paideia_bedrijfswinst_jr2025_statutory,{EID},2025,146737,146737,146737,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -31.31% (was 213630),{SRC_PDF},strong,tick2466; PDF p6 native; YE2024 identical 213630; 62 2274825 JUMP; 630 104719 JUMP; 66A empty; 640/8 3924 JUMP",
f"bud_paideia_equity_jr2025_statutory,{EID},2025,1029234,1029234,1029234,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +15.91%,{SRC_PDF},strong,tick2466; PDF p5 native; YE2024 identical 887959; kapitaalsubsidies empty; overgedragen 14 724646 JUMP; fondsen 10 104588 FLAT; bestemde fondsen 13 200000 FLAT",
f"bud_paideia_assets_jr2025_statutory,{EID},2025,1887493,1887493,1887493,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +10.43%,{SRC_PDF},strong,tick2466; PDF p4 native; YE2024 identical 1709155; MVA 22/27 808536 DROP; cash 293729 JUMP; geldbeleggingen 501400 JUMP; aanbouw 27 empty",
f"bud_paideia_debt_jr2025_statutory,{EID},2025,858259,858259,858259,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +4.51%,{SRC_PDF},strong,tick2466; PDF p5 native; YE2024 identical 821196; 17 383827 DROP; 42/48 472844 JUMP",
f"bud_paideia_cash_jr2025_statutory,{EID},2025,293729,293729,293729,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +55.19%,{SRC_PDF},strong,tick2466; PDF p4 native; YE2024 identical 189277; geldbeleggingen 50/53 501400 JUMP was 490723",
f"bud_paideia_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (destin empty; 14 JUMP 724646 = prior 583371 + pnl 141275),{SRC_PDF},strong,tick2466; PDF p7 native; YE2024 destin empty; bestemde fondsen 13 200000 FLAT FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":0,\"\"2025_bruto\"\":2530206,"
"\"\"2025_pnl\"\":141275,\"\"2025_bedrijfswinst\"\":146737,"
"\"\"2025_equity\"\":1029234,\"\"2025_assets\"\":1887493,\"\"2025_debt\"\":858259,"
"\"\"2025_fte\"\":38.5,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":293729,\"\"2025_geldbeleggingen\"\":501400,"
"\"\"2025_personnel62\"\":2274825,\"\"2025_gebouwen22\"\":574807,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":104588,\"\"2025_overgedragen14\"\":724646,"
"\"\"2025_bestemdefondsen13\"\":200000,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":104719,\"\"2025_capex\"\":97751,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":0,\"\"2024_bruto\"\":2139018,\"\"2024_pnl\"\":206858,\"\"2024_bedrijfswinst\"\":213630,"
"\"\"2024_equity\"\":887959,\"\"2024_assets\"\":1709155,"
"\"\"2024_debt\"\":821196,\"\"2024_cash\"\":189277,\"\"2024_fte\"\":28.3,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":490723}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Paideia YE2025 (bruto JUMP 2.53m / omzet+73 empty VKT / pnl DROP 141k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_brugge CIK,VZW Paideia (KBO 0445.129.931; Actief; 5 VE; RSZ2025 88.911; zetel + 5/5 VE Brugge),2026-06-09,2025,2025,2530206,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00259827.pdf,Public CIK dual of mined city_brugge,Publish Opgroeien matrix behind bruto 2.53m + why omzet+73 empty and why pnl DROP 141k while destin empty and FTE JUMP 38.5 and cash JUMP 294k,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Brugge>Paideia>JR2025_statutory_L5,tick2466; Strong official native PDF; leftover mined city_brugge CIK; 5 VE; NOT every-10; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Paideia bruto JUMP 2.53m / omzet+73 empty VKT / pnl DROP 141k / destin empty (YE2025 leftover city_brugge CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Brugge>Paideia>JR2025",
"2530206",
"2530206",
"PDF bruto 2530206 envelope because omzet empty; 70 empty; 73 empty; 76A empty; bedrijfswinst DROP 146737; pnl DROP 141275; equity JUMP 1029234; assets JUMP 1887493; debt JUMP 858259; FTE 38.5 JUMP; kapitaalsubsidies empty; destin691 empty; cash JUMP 293729; geldbeleggingen JUMP 501400; 5 VE leftover city_brugge CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_brugge CIK",
"CIK / Kind en Gezin groepsopvang leftover city_brugge",
"2.53m bruto envelope; omzet+73 empty VKT; pnl DROP 141k; destin empty; FTE JUMP 38.5; leftover city_brugge CIK",
"5.18",
"5.18",
"5.05",
"5.16",
"FOI Opgroeien matrix behind bruto 2.53m + why omzet+73 empty and why pnl DROP 141k while destin empty and FTE JUMP 38.5 and cash JUMP 294k",
"active",
"",
"tick2466 leftover mined city_brugge CIK after Ooievaarsnest different-city skip; 5 VE; NOT every-10; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels; NOT De Elfjes remine; NOT De Steijgertjes remine",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Brugge>Paideia>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind envelope bruto 2530206 (omzet 70 empty VKT + 73 empty VKT + 76A empty) and why destin empty while pnl DROP 141275 and FTE JUMP 38.5 and cash JUMP 293729",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_brugge; VKT envelope bruto 9900 2.53m because omzet empty; public Opgroeien groepsopvang KDV Hermelijn + BKO Kakelbont",
"priority": "8",
"recipient_body": "VZW Paideia / Raad van Bestuur",
"recipient_email": "secretariaat@ibokakelbont.net",
"recipient_postal": "Koude-Keukenstraat 8B 8200 Brugge",
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
"notes": "tick2466; ready NOT sent; Strong official native NBB PDF; leftover mined city_brugge CIK after Ooievaarsnest different-city skip; 5 VE; NOT every-10; off Ooievaarsnest remine; off Zonnekindjes remine",
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
if rq_raw.count(b"rq_2466,")!=1: raise SystemExit(f"bad 2466 count {rq_raw.count(b'rq_2466,')}")
if b"rq_2467," in rq_raw: raise SystemExit("2467 exists")
idx=rq_raw.rfind(b"rq_2466,")
if idx<0: raise SystemExit("rq_2466 not found")
new_2466=(
"rq_2466,leftover dual Paideia YE2025,hole_fill,8,done,L5,vzw_paideia_brugge,"
"Took unused leftover public CIK Paideia 0445.129.931 leftover mined city_brugge. Official NBB VKT-VZW YE2025 2026-00259827 native 16p. Envelope bruto 9900 JUMP 2530206 (omzet+73 empty VKT; 76A empty); pnl DROP 141275; destin empty; FTE JUMP 38.5. NOT Ooievaarsnest remine. NOT DE ZONNEKINDJES remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2466 leftover mined city_brugge CIK; Strong native PDF; 5 VE; next every-10 is 2470\n"
)
new_2467=(
"rq_2467,leftover dual after Paideia — hunt unused public dual,hole_fill,8,open,L5,,"
"After Paideia YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT Paideia remine. NOT Ooievaarsnest remine. NOT De Zonnekindjes remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine. NOT De Elfjes remine. NOT De Steijgertjes remine. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.,"
f",{STAMP},{STAMP},spawned after tick2466; Paideia taken leftover mined city_brugge CIK; Ooievaarsnest taken leftover mined city_tienen CIK; Zonnekindjes taken leftover mined city_diepenbeek CIK; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2466.count("\n")!=1 or new_2467.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2466.encode("utf-8"))
    f.write(new_2467.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2466", chk.count(b"rq_2466,"), "n2467", chk.count(b"rq_2467,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2466,2466,no,tick2466 leftover dual Paideia 0445.129.931 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto 9900 JUMP 2530206; pnl DROP 141275; 9901 DROP 146737; equity JUMP 1029234; assets JUMP 1887493; debt JUMP 858259; FTE 38.5 JUMP; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 293729; geldbeleggingen JUMP 501400; 5 VE leftover city_brugge CIK); leftover mined city_brugge CIK; NOT Ooievaarsnest remine; NOT DE ZONNEKINDJES remine; NOT D'n Opvang remine; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT De Wissel remine; NOT Familia remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; NOT De Elfjes remine; NOT De Steijgertjes remine; NOT Vormingscentrum training; NOT Zwarte Zusters dissolved; next every-10 is 2470; next rq_2467 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2466 - rq_2466 Paideia (bruto JUMP 2.53m / omzet+73 empty VKT / pnl DROP 141k / destin empty / Strong PDF)

- Unit: **rq_2466** leftover dual after **Ooievaarsnest@2465**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — De Elfjes Kloosterstraat 6 already mined. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024**. Kinderlach leftover city_eeklo still **YE2024**. Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024**. Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024**. Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. Vormingscentrum 0413.342.338 leftover city_gent training — skip. Helan Kinderopvang 0464.151.037 already skipped. Zwarte Zusters 0413.272.260 dissolved — skip. Ooievaarsnest 0418.588.256 just mined — do not remine. DE ZONNEKINDJES 0416.541.952 just mined — do not remine. D'n Opvang 0676.442.465 just mined — do not remine. CAR Overleie just mined — do not remine. Gesticht just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. De Elfjes 0455.636.912 already mined — do not remine. De Steijgertjes 0413.421.720 already mined — do not remine. Hartjes Tienen 0441.374.348 already mined — do not remine. De Wissel 0421.913.376 already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Paideia** YE2025 (KBO **0445.129.931**; zetel Koude-Keukenstraat 8B 8200 Brugge; **Actief** **5 VE** all Brugge — 2.151.264.614 KDV Hermelijn Minicrèche Kiekeboe Vrijheidsstraat 28 8310 since 01.02.2006; 2.151.615.101 KDV Hermelijn Molenwiekstraat-West 30 8200 since 13.02.2006; 2.151.615.495 BKO Kakelbont AKK Koude-Keukenstraat 8b 8200 since 13.02.2006; 2.232.352.456 BKO Kakelbont MOK Oudekerkstraat 23a 8200 since 01.01.2008; 2.354.774.869 KDV Hermelijn De Poppenkast Torhoutse Steenweg 9 8200 since 08.01.2024; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover of mined **city_brugge**; secretariaat@ibokakelbont.net). Identity trap: Paideia 0445.129.931 ≠ KDV Ooievaarsnest **0418.588.256** leftover city_tienen just mined; ≠ DE ZONNEKINDJES **0416.541.952** leftover city_diepenbeek just mined; ≠ D'n Opvang **0676.442.465** leftover city_oostende just mined; ≠ De Elfjes **0455.636.912** already mined; ≠ De Steijgertjes **0413.421.720** already mined; ≠ CAR Overleie **0454.250.505**; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6; ≠ Vormingscentrum **0413.342.338** training; ≠ Zwarte Zusters **0413.272.260** dissolved. 5 VE Brugge — leftover of mined city_brugge (zetel + 5/5 VE). Confirmed leftover public (Opgroeien CIK groepsopvang KDV Hermelijn + BKO Kakelbont; Kind en Gezin-vergund) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Ooievaarsnest remine / not Zonnekindjes remine. VKT-VZW **native text** (not scan) — 54226 B / 16p all native euros (VKT-VZW 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00259827** (54226 B / 16p; AV **09.06.2026**; header **06.07.2026**; CDN Last-Modified **27.07.2026**; CreationDate 07.07.2026 OpenPDF 1.3.26; all 16p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **empty**; envelope bruto 9900 **EUR2530206** JUMP +18.29% (VKT envelope because omzet empty; was 2139018); bruto 9900 **EUR2530206** JUMP +18.29%; 62 **EUR2274825** JUMP +24.51%; 630 **EUR104719** JUMP +9.23%; 66A **empty**; 640/8 **EUR3924** JUMP +56.15%; 635/9 **empty**; bedrijfswinst 9901 **EUR146737** DROP −31.31%; pnl 9904 **EUR141275** DROP −31.70%; equity **EUR1029234** JUMP +15.91%; assets **EUR1887493** JUMP +10.43%; debt **EUR858259** JUMP +4.51%; FTE **38.5** JUMP +36.04% (was 28.3; 100 38.5 was 31.1; 105 39.1; 9087 38.5); kapitaalsubsidies **empty**; destin 691 **empty** (791 empty; 14 JUMP 724646 = prior 583371 + pnl 141275); 791 **empty**; cash **EUR293729** JUMP +55.19%; geldbeleggingen **EUR501400** JUMP +2.18% (was 490723); gebouwen **EUR574807** DROP; MVA 22/27 **EUR808536** DROP; aanbouw **empty**; capex **EUR97751**; fondsen 10 **EUR104588** FLAT; overgedragen 14 **EUR724646** JUMP; bestemde fondsen 13 **EUR200000** FLAT; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 5 VE leftover mined city_brugge CIK. NOT Ooievaarsnest remine. NOT DE ZONNEKINDJES remine. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale. NOT Vormingscentrum training. NOT Zwarte Zusters dissolved.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.16); entities (+1 vzw_paideia_brugge); foi + draft `gap_paideia_opgroeien_matrix_bruto_2_53m_omzet73_empty_pnl_drop_141k_destin_empty_l5`; rq_2466=done + rq_2467 open; loop_state ticks=2466; raw tick2466/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2467 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Paideia remine / NOT Ooievaarsnest remine / NOT De Zonnekindjes remine / NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT De Wissel remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine / NOT De Elfjes remine / NOT De Steijgertjes remine / NOT Vormingscentrum training / NOT Zwarte Zusters dissolved). NOW leftover candidate: Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
