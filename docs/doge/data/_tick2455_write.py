from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2455_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_pallieterkes_jr2025_nbb_pdf_2455"
SRC_KBO="src_pallieterkes_kbo_2455"
SRC_SBM="src_pallieterkes_sbm_2455"
SRC_SITE="src_pallieterkes_site_2455"
EID="vzw_pallieterkes_lier"
GAP="gap_pallieterkes_opgroeien_matrix_bruto_978k_omzet73_empty_pnl_drop_108k_destin_empty_l5"
COMM="comm_pallieterkes_jr2025_statutory_bruto_978k_omzet73_empty_pnl_drop_108k"
LB="lb_pallieterkes_bruto_978k_omzet73_empty_pnl_drop_108k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf De Pallieterkes deposit 2026-00264045,http://cdn.staatsbladmonitor.be/2026pdf/2026-00264045.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2455; official native PDF 49512 bytes 12p VKT-VZW 25.0.13 m04-f; header 02.07.2026; AV 25.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-28; CreationDate 2026-07-08 01:07:44 UTC OpenPDF 1.3.26; all 12p native; VKT-VZW 6.1.1 6.1.3 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf De Pallieterkes 0418.538.865,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0418538865,KBO Public Search FOD Economie,{DAY},official_register,tick2455; Actief; 1 VE 2.150.892.054; VZW since 01.01.1978; begindatum 01.01.1978; zetel Mechelsestraat 24 2500 Lier since 01.12.2004; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; RSZ2025 88.911; FOI pallieterkes@heilighartlier.be; leftover mined city_lier CIK; NOT De Medemens KDV 0893.678.915 remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf De Pallieterkes 0418538865 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0418538865,NBB Consult,{DAY},official_register,tick2455; deposit-id 2026-00264045 YE 30/12/2025 filing 02/07/2026 VKT-VZW Verkort; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Pallieterkes FOI contact leftover city_lier CIK,https://www.depallieterkes.be,VZW Kinderdagverblijf De Pallieterkes leftover city_lier CIK,{DAY},foi_contact,tick2455; FOI pallieterkes@heilighartlier.be; zetel Mechelsestraat 24 2500 Lier; leftover mined city_lier after De Medemens Kinderdagverblijven different-KBO skip; 1 VE Lier CIK; NOT Kloosterstraat 6 Drongen; NOT De Medemens KDV remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf De Pallieterkes VZW,ASBL Creche De Pallieterkes,Kinderdagverblijf De Pallieterkes VZW (leftover city_lier CIK),parastatal,city_lier,nl,https://www.depallieterkes.be,pallieterkes@heilighartlier.be,Mechelsestraat 24 2500 Lier,tick2455 YE2025 Strong official native NBB PDF deposit 2026-00264045 + Strong KBO 0418.538.865 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto JUMP 978180 envelope; pnl DROP 108202; 9901 DROP 107988; equity JUMP 1594787; assets JUMP 1859325; debt JUMP 264538; FTE 13 DROP; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 1369153; geldbeleggingen FLAT 150016; leftover mined city_lier after De Medemens Kinderdagverblijven different-KBO skip; 1 VE CIK groepsopvang not private; NOT Kloosterstraat 6 Drongen; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Elief 0451.624.377 CDN 403; NOT VKA 0433.480.132 no deposit-id; NOT Hebe training; NOT WZC OLVA remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_pallieterkes_bruto_jr2025_statutory,{EID},2025,978180,978180,978180,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.03% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2455; PDF p5 native; YE2024 identical 949416; 76A empty",
f"bud_pallieterkes_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2455; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_pallieterkes_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2455; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 978180",
f"bud_pallieterkes_pnl_jr2025_statutory,{EID},2025,108202,108202,108202,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -26.81% (was 147830),{SRC_PDF},strong,tick2455; PDF p5 native; YE2024 identical 147830; bedrijfswinst 9901 107988 DROP; destin691 empty",
f"bud_pallieterkes_bedrijfswinst_jr2025_statutory,{EID},2025,107988,107988,107988,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -26.90% (was 147695),{SRC_PDF},strong,tick2455; PDF p5 native; YE2024 identical 147695; 62 850615 JUMP; 630 19364 JUMP; 640/8 213 JUMP",
f"bud_pallieterkes_equity_jr2025_statutory,{EID},2025,1594787,1594787,1594787,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +7.28%,{SRC_PDF},strong,tick2455; PDF p4 native; YE2024 identical 1486585; kapitaalsubsidies empty; overgedragen 14 1577434 JUMP; fondsen 10 empty; bestemde fondsen 13 17353 FLAT",
f"bud_pallieterkes_assets_jr2025_statutory,{EID},2025,1859325,1859325,1859325,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +8.56%,{SRC_PDF},strong,tick2455; PDF p3 native; YE2024 identical 1712742; MVA 22/27 259809 DROP; cash 1369153 JUMP; geldbeleggingen 150016 FLAT; aanbouw 27 empty",
f"bud_pallieterkes_debt_jr2025_statutory,{EID},2025,264538,264538,264538,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +16.97%,{SRC_PDF},strong,tick2455; PDF p4 native; YE2024 identical 226158; 42/48 264501 JUMP",
f"bud_pallieterkes_cash_jr2025_statutory,{EID},2025,1369153,1369153,1369153,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +11.89%,{SRC_PDF},strong,tick2455; PDF p3 native; YE2024 identical 1223636; geldbeleggingen 50/53 150016 FLAT",
f"bud_pallieterkes_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; destin empty vs pnl 108202),{SRC_PDF},strong,tick2455; PDF p6 native; YE2024 destin empty; overgedragen 14 1577434 JUMP FOI",
f"bud_pallieterkes_62_jr2025_statutory,{EID},2025,850615,850615,850615,NBB VKT-VZW code 62 bezoldigingen YE2025 JUMP +8.75%,{SRC_PDF},strong,tick2455; PDF p5 native; YE2024 identical 782210; FTE 13 DROP",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_bruto\"\":978180,"
"\"\"2025_pnl\"\":108202,\"\"2025_bedrijfswinst\"\":107988,"
"\"\"2025_equity\"\":1594787,\"\"2025_assets\"\":1859325,\"\"2025_debt\"\":264538,"
"\"\"2025_fte\"\":13,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1369153,\"\"2025_geldbeleggingen\"\":150016,"
"\"\"2025_personnel62\"\":850615,\"\"2025_gebouwen22\"\":241765,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":1577434,"
"\"\"2025_bestemdefondsen13\"\":17353,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":19364,\"\"2025_capex8169\"\":1354,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":949416,\"\"2024_pnl\"\":147830,\"\"2024_bedrijfswinst\"\":147695,"
"\"\"2024_equity\"\":1486585,\"\"2024_assets\"\":1712742,"
"\"\"2024_debt\"\":226158,\"\"2024_cash\"\":1223636,\"\"2024_fte\"\":13.2,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":150016}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf De Pallieterkes YE2025 (bruto JUMP 978k / omzet+73 empty VKT / pnl DROP 108k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_lier CIK,VZW Kinderdagverblijf De Pallieterkes (KBO 0418.538.865; Actief; 1 VE; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap; 1/1 VE Lier),2026-06-25,2025,2025,978180,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00264045.pdf,Public CIK dual of mined city_lier,Publish Opgroeien matrix behind bruto 978k + why omzet+73 empty VKT + why pnl DROP 108k while destin empty and cash JUMP 1.37m and FTE DROP 13,{SRC_PDF},strong,Vlaanderen>Antwerpen>Lier>Pallieterkes>JR2025_statutory_L5,tick2455; Strong official native PDF; leftover mined city_lier CIK; 1 VE; NOT Kloosterstraat 6 Drongen; NOT De Medemens KDV remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Kinderdagverblijf De Pallieterkes bruto JUMP 978k / omzet+73 empty VKT / pnl DROP 108k / destin empty (YE2025 leftover city_lier CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Lier>Pallieterkes>JR2025",
"978180",
"978180",
"PDF 9900 978180 envelope; omzet empty VKT; 73 empty VKT; 76A empty; bruto JUMP 978180; bedrijfswinst DROP 107988; pnl DROP 108202; equity JUMP 1594787; assets JUMP 1859325; debt JUMP 264538; FTE 13 DROP; kapitaalsubsidies empty; destin691 empty; cash JUMP 1369153; geldbeleggingen FLAT 150016; 1 VE leftover city_lier CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_lier CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_lier",
"978k bruto envelope; omzet+73 empty VKT; pnl DROP 108k; destin empty; cash JUMP 1.37m; leftover city_lier CIK",
"5.10",
"5.10",
"4.90",
"5.07",
"FOI Opgroeien matrix behind bruto 978k + why omzet+73 empty VKT + why pnl DROP 108k while destin empty and cash JUMP 1.37m and FTE DROP 13",
"active",
"",
"tick2455 leftover mined city_lier CIK after De Medemens Kinderdagverblijven different-KBO skip; 1 VE; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Elief CDN 403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

# FOI via csv.writer to guarantee 21 fields
foi_path=DATA/"foi_queue.csv"
foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Lier>Pallieterkes>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind bruto 978180 (omzet+73 empty VKT) and why pnl DROP 108202 while destin empty and cash JUMP 1369153 and FTE DROP 13",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_lier; 978k bruto envelope; public Kind en Gezin-vergunde groepsopvang",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf De Pallieterkes / Raad van Bestuur",
"recipient_email": "pallieterkes@heilighartlier.be",
"recipient_postal": "Mechelsestraat 24 2500 Lier",
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
"notes": "tick2455; ready NOT sent; Strong official native NBB PDF; leftover mined city_lier CIK after De Medemens Kinderdagverblijven different-KBO skip; 1 VE; off Drongen",
}
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")

# surgical RQ patch
rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2455,")!=1: raise SystemExit(f"bad 2455 count {rq_raw.count(b'rq_2455,')}")
if b"rq_2456," in rq_raw: raise SystemExit("2456 exists")
idx=rq_raw.rfind(b"rq_2455,")
if idx<0: raise SystemExit("rq_2455 not found")
new_2455=(
"rq_2455,leftover dual Kinderdagverblijf De Pallieterkes YE2025,hole_fill,8,done,L5,vzw_pallieterkes_lier,"
"Took unused leftover public CIK Kinderdagverblijf De Pallieterkes 0418.538.865 leftover mined city_lier. Official NBB VKT-VZW YE2025 2026-00264045 native 12p. Envelope bruto9900 JUMP 978180; omzet+73 empty VKT; pnl DROP 108202; destin empty. NOT De Medemens remine.,"
f",{STAMP},{STAMP},tick2455 leftover mined city_lier CIK; Strong native PDF; 1 VE; next every-10 is 2460\n"
)
new_2456=(
"rq_2456,leftover dual after Kinderdagverblijf De Pallieterkes — hunt unused public dual,hole_fill,8,open,L5,,"
"After Kinderdagverblijf De Pallieterkes YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Kinderlach / De Linde Ronse / Villa Boempatat / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende / t Sloeberke / Soetkin still YE2024 — take ONLY if unused + official YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. VKA 0433.480.132 leftover city_antwerpen YE2025 filed 29.06.2026 — take ONLY if unused + deposit-id + live 2026pdf. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2455; Kinderdagverblijf De Pallieterkes taken leftover mined city_lier CIK; De Medemens Kinderdagverblijven taken leftover mined city_antwerpen CIK; OKO & ZO taken leftover mined city_zele CIK; KINDEROPVANG De Harlekijntjes taken leftover mined city_tielt CIK; Kinderdagverblijf De Hartjes Ninove taken leftover mined city_ninove CIK; Groepsopvang De Hartjes Tienen taken leftover mined city_tienen CIK\n"
)
if new_2455.count("\n")!=1 or new_2456.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2455.encode("utf-8"))
    f.write(new_2456.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2455", chk.count(b"rq_2455,"), "n2456", chk.count(b"rq_2456,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2455,2455,no,tick2455 leftover dual Kinderdagverblijf De Pallieterkes 0418.538.865 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; bruto9900 JUMP 978180 envelope; pnl DROP 108202; 9901 DROP 107988; equity JUMP 1594787; assets JUMP 1859325; debt JUMP 264538; FTE 13 DROP; kapitaalsubsidies empty; destin691 empty; 791 empty; cash JUMP 1369153; geldbeleggingen FLAT 150016; 1 VE leftover city_lier CIK); leftover mined city_lier CIK; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id; NOT Hebe training; NOT WZC OLVA remine; next every-10 is 2460; next rq_2456 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")
print("WRITE CORE DONE")
