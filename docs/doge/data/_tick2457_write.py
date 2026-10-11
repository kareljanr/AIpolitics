from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2457_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_sloeberke_jr2025_nbb_pdf_2457"
SRC_KBO="src_sloeberke_kbo_2457"
SRC_SBM="src_sloeberke_sbm_2457"
SRC_SITE="src_sloeberke_site_2457"
EID="vzw_sloeberke_kortrijk"
GAP="gap_sloeberke_opgroeien_matrix_bruto_596k_omzet73_empty_pnl_jump_85k_destin_empty_l5"
COMM="comm_sloeberke_jr2025_statutory_bruto_596k_omzet73_empty_pnl_jump_85k"
LB="lb_sloeberke_bruto_596k_omzet73_empty_pnl_jump_85k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB MIC-VZW jaarrekening 2025 Kinderdagverblijf t Sloeberke Groenheuvel deposit 2026-00153565,http://cdn.staatsbladmonitor.be/2026pdf/2026-00153565.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2457; official native PDF 74938 bytes 16p MIC-VZW 25.0.12 m08-f; header 11.06.2026; AV 04.05.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-06-19; CreationDate 2026-06-11 22:01:10 UTC OpenPDF 1.3.26; all 16p native; MIC-VZW 6.1.3 6.3 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf t Sloeberke Groenheuvel 0410.973.360,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0410973360,KBO Public Search FOD Economie,{DAY},official_register,tick2457; Actief; 1 VE 2.159.526.143 KDV BELLEGEM T SLOEBERKE Dottenijsestraat 33 8510 Kortrijk since 15.02.2007; VZW since 01.02.1969; begindatum 01.02.1969; zetel Dottenijsestraat 33 8510 Kortrijk Bellegem since 21.08.2017; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI tsloeberke@lutgardiscollege.be; leftover mined city_kortrijk CIK; NOT De Groene Verte 0465.061.649 remine; NOT De Pallieterkes 0418.538.865 remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche t Sloeberke 0410973360 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0410973360,NBB Consult,{DAY},official_register,tick2457; deposit-id 2026-00153565 YE 31/12/2025 filing 11/06/2026 MIC-VZW Micro Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},t Sloeberke FOI contact leftover city_kortrijk CIK,https://tsloeberke.be/,VZW Kinderdagverblijf t Sloeberke Groenheuvel leftover city_kortrijk CIK,{DAY},foi_contact,tick2457; FOI tsloeberke@lutgardiscollege.be; zetel Dottenijsestraat 33 8510 Kortrijk Bellegem; leftover mined city_kortrijk after De Groene Verte different-KBO skip; 1 VE Kortrijk CIK; NOT Kloosterstraat 6 Drongen; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf 't Sloeberke - Groenheuvel VZW,ASBL Creche t Sloeberke Groenheuvel,Kinderdagverblijf t Sloeberke Groenheuvel VZW (leftover city_kortrijk CIK),parastatal,city_kortrijk,nl,https://tsloeberke.be/,tsloeberke@lutgardiscollege.be,Dottenijsestraat 33 8510 Kortrijk,tick2457 YE2025 Strong official native NBB PDF deposit 2026-00153565 + Strong KBO 0410.973.360 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty MIC; 73 empty MIC; 76A empty; bruto JUMP 596094 envelope; pnl JUMP 84612; 9901 JUMP 91083; equity JUMP 587816; assets JUMP 1015926; debt DROP 428111; FTE 6.5 FLAT; kapitaalsubsidies DROP 409783; destin691 empty; 791 empty; cash JUMP 132960; geldbeleggingen empty; leftover mined city_kortrijk after De Groene Verte different-KBO skip; 1 VE CIK groepsopvang not private; NOT Kloosterstraat 6 Drongen; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Soetkin 0443.641.970 leftover city_kortrijk YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Elief 0451.624.377 CDN 403; NOT VKA 0433.480.132 no deposit-id; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_sloeberke_bruto_jr2025_statutory,{EID},2025,596094,596094,596094,NBB MIC-VZW code 9900 brutomarge YE2025 JUMP +6.20% (MIC envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2457; PDF p5 native; YE2024 identical 561275; 76A empty",
f"bud_sloeberke_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 70 omzet YE2025 empty (MIC; envelope is bruto 9900),{SRC_PDF},strong,tick2457; PDF p5 native; YE2024 identical empty; 73 also empty MIC",
f"bud_sloeberke_73_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (MIC),{SRC_PDF},strong,tick2457; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 596094",
f"bud_sloeberke_pnl_jr2025_statutory,{EID},2025,84612,84612,84612,NBB MIC-VZW code 9904 winst van het boekjaar YE2025 JUMP +11.20% (was 76088),{SRC_PDF},strong,tick2457; PDF p5 native; YE2024 identical 76088; bedrijfswinst 9901 91083 JUMP; destin691 empty",
f"bud_sloeberke_bedrijfswinst_jr2025_statutory,{EID},2025,91083,91083,91083,NBB MIC-VZW code 9901 bedrijfswinst YE2025 JUMP +9.39% (was 83268),{SRC_PDF},strong,tick2457; PDF p5 native; YE2024 identical 83268; 62 462830 JUMP; 630 40817 JUMP; 640/8 1364 JUMP",
f"bud_sloeberke_equity_jr2025_statutory,{EID},2025,587816,587816,587816,NBB MIC-VZW code 10/15 eigen vermogen YE2025 JUMP +12.46%,{SRC_PDF},strong,tick2457; PDF p4 native; YE2024 identical 522690; kapitaalsubsidies 409783 DROP; overgedragen 14 114410 JUMP; fondsen 10 63622 FLAT; bestemde fondsen 13 empty",
f"bud_sloeberke_assets_jr2025_statutory,{EID},2025,1015926,1015926,1015926,NBB MIC-VZW code 20/58 totaal activa YE2025 JUMP +4.07%,{SRC_PDF},strong,tick2457; PDF p3 native; YE2024 identical 976215; MVA 22/27 843043 DROP; cash 132960 JUMP; geldbeleggingen empty; aanbouw 27 empty",
f"bud_sloeberke_debt_jr2025_statutory,{EID},2025,428111,428111,428111,NBB MIC-VZW code 17/49 schulden YE2025 DROP -5.60%,{SRC_PDF},strong,tick2457; PDF p4 native; YE2024 identical 453525; 17 302435 DROP; 42/48 125676 JUMP",
f"bud_sloeberke_cash_jr2025_statutory,{EID},2025,132960,132960,132960,NBB MIC-VZW code 54/58 liquide middelen YE2025 JUMP +159.49%,{SRC_PDF},strong,tick2457; PDF p3 native; YE2024 identical 51239; geldbeleggingen 50/53 empty",
f"bud_sloeberke_destin_jr2025_statutory,{EID},2025,0,0,0,NBB MIC-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; destin empty vs pnl 84612),{SRC_PDF},strong,tick2457; PDF p6 native; YE2024 destin empty; overgedragen 14 114410 JUMP FOI",
f"bud_sloeberke_62_jr2025_statutory,{EID},2025,462830,462830,462830,NBB MIC-VZW code 62 bezoldigingen YE2025 JUMP +5.92%,{SRC_PDF},strong,tick2457; PDF p5 native; YE2024 identical 436975; FTE 6.5 FLAT",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_bruto\"\":596094,"
"\"\"2025_pnl\"\":84612,\"\"2025_bedrijfswinst\"\":91083,"
"\"\"2025_equity\"\":587816,\"\"2025_assets\"\":1015926,\"\"2025_debt\"\":428111,"
"\"\"2025_fte\"\":6.5,\"\"2025_kapitaalsubsidies\"\":409783,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":132960,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":462830,\"\"2025_gebouwen22\"\":826785,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":63622,\"\"2025_overgedragen14\"\":114410,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":40817,\"\"2025_capex\"\":2187,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":561275,\"\"2024_pnl\"\":76088,\"\"2024_bedrijfswinst\"\":83268,"
"\"\"2024_equity\"\":522690,\"\"2024_assets\"\":976215,"
"\"\"2024_debt\"\":453525,\"\"2024_cash\"\":51239,\"\"2024_fte\"\":6.5,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":429269,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf t Sloeberke Groenheuvel YE2025 (bruto JUMP 596k / omzet+73 empty MIC / pnl JUMP 85k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_kortrijk CIK,VZW Kinderdagverblijf t Sloeberke Groenheuvel (KBO 0410.973.360; Actief; 1 VE; RSZ2025 88.911; 1/1 VE Kortrijk Bellegem),2026-05-04,2025,2025,596094,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00153565.pdf,Public CIK dual of mined city_kortrijk,Publish Opgroeien matrix behind bruto 596k + why omzet+73 empty MIC + why pnl JUMP 85k while destin empty and cash JUMP 133k and FTE FLAT 6.5,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>Sloeberke>JR2025_statutory_L5,tick2457; Strong official native PDF; leftover mined city_kortrijk CIK; 1 VE; NOT Kloosterstraat 6 Drongen; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Kinderdagverblijf t Sloeberke Groenheuvel bruto JUMP 596k / omzet+73 empty MIC / pnl JUMP 85k / destin empty (YE2025 leftover city_kortrijk CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Kortrijk>Sloeberke>JR2025",
"596094",
"596094",
"PDF 9900 596094 envelope; omzet empty MIC; 73 empty MIC; 76A empty; bruto JUMP 596094; bedrijfswinst JUMP 91083; pnl JUMP 84612; equity JUMP 587816; assets JUMP 1015926; debt DROP 428111; FTE 6.5 FLAT; kapitaalsubsidies DROP 409783; destin691 empty; cash JUMP 132960; geldbeleggingen empty; 1 VE leftover city_kortrijk CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_kortrijk CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_kortrijk",
"596k bruto envelope; omzet+73 empty MIC; pnl JUMP 85k; destin empty; cash JUMP 133k; leftover city_kortrijk CIK",
"4.95",
"4.70",
"5.00",
"4.96",
"FOI Opgroeien matrix behind bruto 596k + why omzet+73 empty MIC + why pnl JUMP 85k while destin empty and cash JUMP 133k and FTE FLAT 6.5",
"active",
"",
"tick2457 leftover mined city_kortrijk CIK after De Groene Verte different-KBO skip; 1 VE; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Elief CDN 403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_path=DATA/"foi_queue.csv"
foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Kortrijk>Sloeberke>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind bruto 596094 (omzet 70 empty + 73 empty MIC) and why pnl JUMP 84612 while destin empty and cash JUMP 132960 and FTE FLAT 6.5",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_kortrijk; 596k bruto envelope; public Kind en Gezin-vergunde groepsopvang",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf 't Sloeberke - Groenheuvel / Raad van Bestuur",
"recipient_email": "tsloeberke@lutgardiscollege.be",
"recipient_postal": "Dottenijsestraat 33 8510 Kortrijk",
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
"notes": "tick2457; ready NOT sent; Strong official native NBB PDF; leftover mined city_kortrijk CIK after De Groene Verte different-KBO skip; 1 VE; off Drongen",
}
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
if rq_raw.count(b"rq_2457,")!=1: raise SystemExit(f"bad 2457 count {rq_raw.count(b'rq_2457,')}")
if b"rq_2458," in rq_raw: raise SystemExit("2458 exists")
idx=rq_raw.rfind(b"rq_2457,")
if idx<0: raise SystemExit("rq_2457 not found")
new_2457=(
"rq_2457,leftover dual Kinderdagverblijf t Sloeberke Groenheuvel YE2025,hole_fill,8,done,L5,vzw_sloeberke_kortrijk,"
"Took unused leftover public CIK Kinderdagverblijf t Sloeberke Groenheuvel 0410.973.360 leftover mined city_kortrijk. Official NBB MIC-VZW YE2025 2026-00153565 native 16p. Envelope bruto9900 JUMP 596094; omzet+73 empty MIC; pnl JUMP 84612; destin empty. NOT De Groene Verte remine. NOT De Vleugels remine.,"
f",{STAMP},{STAMP},tick2457 leftover mined city_kortrijk CIK; Strong native PDF; 1 VE; next every-10 is 2460\n"
)
new_2458=(
"rq_2458,leftover dual after Kinderdagverblijf t Sloeberke Groenheuvel — hunt unused public dual,hole_fill,8,open,L5,,"
"After Kinderdagverblijf t Sloeberke Groenheuvel YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Kinderlach / De Linde Ronse / Villa Boempatat / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende / Soetkin still YE2024 — take ONLY if unused + official YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. VKA 0433.480.132 leftover city_antwerpen YE2025 filed 29.06.2026 — take ONLY if unused + deposit-id + live 2026pdf. NOT t Sloeberke remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2457; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; De Pallieterkes taken leftover mined city_lier CIK; De Medemens Kinderdagverblijven taken leftover mined city_antwerpen CIK; OKO & ZO taken leftover mined city_zele CIK; KINDEROPVANG De Harlekijntjes taken leftover mined city_tielt CIK; Kinderdagverblijf De Hartjes Ninove taken leftover mined city_ninove CIK; Groepsopvang De Hartjes Tienen taken leftover mined city_tienen CIK\n"
)
if new_2457.count("\n")!=1 or new_2458.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2457.encode("utf-8"))
    f.write(new_2458.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2457", chk.count(b"rq_2457,"), "n2458", chk.count(b"rq_2458,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2457,2457,no,tick2457 leftover dual Kinderdagverblijf t Sloeberke Groenheuvel 0410.973.360 Strong native PDF (omzet70 empty MIC; 73 empty MIC; 76A empty; bruto9900 JUMP 596094 envelope; pnl JUMP 84612; 9901 JUMP 91083; equity JUMP 587816; assets JUMP 1015926; debt DROP 428111; FTE 6.5 FLAT; kapitaalsubsidies DROP 409783; destin691 empty; 791 empty; cash JUMP 132960; geldbeleggingen empty; 1 VE leftover city_kortrijk CIK); leftover mined city_kortrijk CIK; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; next every-10 is 2460; next rq_2458 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")
print("WRITE CORE DONE")
