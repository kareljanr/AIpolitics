from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2456_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_groene_verte_jr2025_nbb_pdf_2456"
SRC_KBO="src_groene_verte_kbo_2456"
SRC_SBM="src_groene_verte_sbm_2456"
SRC_SITE="src_groene_verte_site_2456"
EID="vzw_groene_verte_houthulst"
GAP="gap_groene_verte_zorg_matrix_omzet_6_05m_73_1_21m_pnl_drop_335k_destin_drop_268k_l5"
COMM="comm_groene_verte_jr2025_statutory_omzet_6_05m_73_1_21m_pnl_drop_335k"
LB="lb_groene_verte_omzet_6_05m_73_1_21m_pnl_drop_335k_destin_drop_268k_jr2025"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 De Groene Verte woon en zorg deposit 2026-00200541,http://cdn.staatsbladmonitor.be/2026pdf/2026-00200541.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2456; official native PDF 483459 bytes 47p VOL-VZW 26.0.15 m05-f; header 22.06.2026; AV 16.06.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-09; CreationDate 2026-06-26 02:45:19 UTC OpenPDF 1.3.26; all 47p native; VOL-VZW 6.1 6.2.1 6.2.3 6.2.4 6.3.4 6.4.1 6.4.2 6.5.1 6.5.2 6.16 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO DE GROENE VERTE WOON EN ZORG 0465.061.649,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0465061649,KBO Public Search FOD Economie,{DAY},official_register,tick2456; Actief; 1 VE 2.150.787.829 Merkem Seniorenzorg woon- en zorgcentrum Kouterstraat 46 8650 Houthulst since 03.01.2006; VZW since 08.12.1998; begindatum 08.12.1998; zetel Kouterstraat 46 8650 Houthulst since 08.12.1998; RSZ2025 87.101; BTW2025 87.992; FOI info@degroeneverte.be; leftover mined city_houthulst WZC; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche De Groene Verte 0465061649 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0465061649,NBB Consult,{DAY},official_register,tick2456; deposit-id 2026-00200541 YE 30/12/2025 filing 22/06/2026 VOL-VZW Volledig Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},De Groene Verte FOI contact leftover city_houthulst WZC,http://www.degroeneverte.be/,VZW DE GROENE VERTE WOON EN ZORG leftover city_houthulst WZC,{DAY},foi_contact,tick2456; FOI info@degroeneverte.be; statutory PDF wzcmerkem@skynet.be; zetel Kouterstraat 46 8650 Houthulst Merkem; leftover mined city_houthulst after De Pallieterkes different-KBO skip; 1 VE Houthulst WZC; NOT Kloosterstraat 6 Drongen; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Kinderlach; NOT Helan; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},DE GROENE VERTE WOON EN ZORG VZW,ASBL DE GROENE VERTE WOON EN ZORG,DE GROENE VERTE WOON EN ZORG VZW (leftover city_houthulst WZC),parastatal,city_houthulst,nl,http://www.degroeneverte.be/,info@degroeneverte.be,Kouterstraat 46 8650 Houthulst,tick2456 YE2025 Strong official native NBB PDF deposit 2026-00200541 + Strong KBO 0465.061.649 Actief 1 VE RSZ2025 87.101 BTW2025 87.992; omzet70 JUMP 6054692 envelope; 73 JUMP 1212686; 76A empty DROP; 70/76A JUMP 7426417; bruto empty VOL; pnl DROP 335472; 9901 DROP 382667; equity JUMP 8670513; assets DROP 12123011; debt DROP 3441502; FTE 76.2 JUMP; kapitaalsubsidies DROP 3037049; destin691 DROP 268378; 791 empty; cash JUMP 94916; geldbeleggingen JUMP 2766663; leftover mined city_houthulst after De Pallieterkes different-KBO skip; 1 VE WZC RVT not private; NOT Kloosterstraat 6 Drongen; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT t Sloeberke 0410.973.360 leftover city_kortrijk YE2024; NOT Soetkin 0443.641.970 YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Elief 0451.624.377 CDN 403; NOT VKA 0433.480.132 no deposit-id; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_groene_verte_omzet_jr2025_statutory,{EID},2025,6054692,6054692,6054692,NBB VOL-VZW code 70 omzet YE2025 JUMP +1.49% (envelope because omzet not commercial-only vs 73 1212686),{SRC_PDF},strong,tick2456; PDF p7 native; YE2024 identical 5965700; 6.9 omzet-uitsplitsing empty",
f"bud_groene_verte_73_jr2025_statutory,{EID},2025,1212686,1212686,1212686,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +0.11% (733 subsidies 1212686),{SRC_PDF},strong,tick2456; PDF p7 native; YE2024 identical 1211367; 730/731/732 empty YE2025",
f"bud_groene_verte_opbr_jr2025_statutory,{EID},2025,7426417,7426417,7426417,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +1.06%,{SRC_PDF},strong,tick2456; PDF p7 native; YE2024 identical 7348547; 74 159038; 76A empty DROP",
f"bud_groene_verte_pnl_jr2025_statutory,{EID},2025,335472,335472,335472,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -50.63% (was 679487),{SRC_PDF},strong,tick2456; PDF p8 native; YE2024 identical 679487; bedrijfswinst 9901 382667 DROP; destin691 268378 DROP",
f"bud_groene_verte_bedrijfswinst_jr2025_statutory,{EID},2025,382667,382667,382667,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -46.52% (was 715558),{SRC_PDF},strong,tick2456; PDF p7 native; YE2024 identical 715558; 62 5245596 JUMP; 630 587728 JUMP; 66A 3964 DROP",
f"bud_groene_verte_equity_jr2025_statutory,{EID},2025,8670513,8670513,8670513,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +2.03%,{SRC_PDF},strong,tick2456; PDF p6 native; YE2024 identical 8497678; kapitaalsubsidies 3037049 DROP; overgedragen 14 947763 JUMP; fondsen 10 894647 FLAT; bestemde fondsen 13 3791053 JUMP",
f"bud_groene_verte_assets_jr2025_statutory,{EID},2025,12123011,12123011,12123011,NBB VOL-VZW code 20/58 totaal activa YE2025 DROP -1.12%,{SRC_PDF},strong,tick2456; PDF p5 native; YE2024 identical 12260614; MVA 22/27 8427329 DROP; cash 94916 JUMP; geldbeleggingen 2766663 JUMP; aanbouw 27 12674 JUMP",
f"bud_groene_verte_debt_jr2025_statutory,{EID},2025,3441502,3441502,3441502,NBB VOL-VZW code 17/49 schulden YE2025 DROP -8.17%,{SRC_PDF},strong,tick2456; PDF p6 native; YE2024 identical 3747885; 17 1919363 DROP; 42/48 1483109 JUMP",
f"bud_groene_verte_cash_jr2025_statutory,{EID},2025,94916,94916,94916,NBB VOL-VZW code 54/58 liquide middelen YE2025 JUMP +218.92%,{SRC_PDF},strong,tick2456; PDF p5 native; YE2024 identical 29762; geldbeleggingen 50/53 2766663 JUMP +0.23%",
f"bud_groene_verte_destin_jr2025_statutory,{EID},2025,268378,268378,268378,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -50.63% (791 empty; destin 268378 vs pnl 335472),{SRC_PDF},strong,tick2456; PDF p9 native; YE2024 destin 543589; overgedragen 14 947763 JUMP FOI",
f"bud_groene_verte_62_jr2025_statutory,{EID},2025,5245596,5245596,5245596,NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +6.09%,{SRC_PDF},strong,tick2456; PDF p7 native; YE2024 identical 4944649; FTE 76.2 JUMP",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":6054692,\"\"2025_73\"\":1212686,\"\"2025_76A\"\":0,"
"\"\"2025_opbr7076A\"\":7426417,"
"\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":335472,\"\"2025_bedrijfswinst\"\":382667,"
"\"\"2025_equity\"\":8670513,\"\"2025_assets\"\":12123011,\"\"2025_debt\"\":3441502,"
"\"\"2025_fte\"\":76.2,\"\"2025_kapitaalsubsidies\"\":3037049,\"\"2025_destin691\"\":268378,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":94916,\"\"2025_geldbeleggingen\"\":2766663,"
"\"\"2025_personnel62\"\":5245596,\"\"2025_gebouwen22\"\":8095155,"
"\"\"2025_aanbouw27\"\":12674,\"\"2025_66A\"\":3964,"
"\"\"2025_fondsen10\"\":894647,\"\"2025_overgedragen14\"\":947763,"
"\"\"2025_bestemdefondsen13\"\":3791053,"
"\"\"2025_voorzieningen16\"\":10996,\"\"2025_630\"\":587728,\"\"2025_capex\"\":343572,"
"\"\"2024_omzet\"\":5965700,\"\"2024_73\"\":1211367,"
"\"\"2024_opbr7076A\"\":7348547,\"\"2024_pnl\"\":679487,\"\"2024_bedrijfswinst\"\":715558,"
"\"\"2024_equity\"\":8497678,\"\"2024_assets\"\":12260614,"
"\"\"2024_debt\"\":3747885,\"\"2024_cash\"\":29762,\"\"2024_fte\"\":73.6,"
"\"\"2024_destin691\"\":543589,\"\"2024_kapitaalsubsidies\"\":3199687,\"\"2024_76A\"\":9278,"
"\"\"2024_geldbeleggingen\"\":2760222}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Groene Verte woon en zorg YE2025 (omzet JUMP 6.05m / 73 1.21m / pnl DROP 335k / destin DROP 268k / Strong PDF),{EID},Departement Zorg + leftover city_houthulst WZC,VZW DE GROENE VERTE WOON EN ZORG (KBO 0465.061.649; Actief; 1 VE; RSZ2025 87.101; BTW2025 87.992; 1/1 VE Houthulst Merkem),2026-06-16,2025,2025,6054692,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00200541.pdf,Public WZC dual of mined city_houthulst,Publish Zorg/RIZIV matrix behind omzet 6.05m + 73 1.21m + why pnl DROP 335k while destin DROP 268k and cash JUMP 95k and FTE JUMP 76.2,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Houthulst>GroeneVerte>JR2025_statutory_L5,tick2456; Strong official native PDF; leftover mined city_houthulst WZC; 1 VE; NOT Kloosterstraat 6 Drongen; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT t Sloeberke YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Groene Verte woon en zorg omzet JUMP 6.05m / 73 1.21m / pnl DROP 335k / destin DROP 268k (YE2025 leftover city_houthulst WZC)",
"L5",
"wzc_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Houthulst>GroeneVerte>JR2025",
"6054692",
"6054692",
"PDF 70 6054692 envelope; 73 1212686; 76A empty; 70/76A 7426417; bruto empty VOL; bedrijfswinst DROP 382667; pnl DROP 335472; equity JUMP 8670513; assets DROP 12123011; debt DROP 3441502; FTE 76.2 JUMP; kapitaalsubsidies DROP 3037049; destin691 DROP 268378; cash JUMP 94916; geldbeleggingen JUMP 2766663; 1 VE leftover city_houthulst WZC",
"strong",
SRC_PDF,
"Departement Zorg + leftover city_houthulst WZC",
"Departement Zorg-erkend WZC leftover city_houthulst",
"6.05m omzet envelope; 73 1.21m; pnl DROP 335k; destin DROP 268k; cash JUMP 95k; leftover city_houthulst WZC",
"5.22",
"4.00",
"5.00",
"5.20",
"FOI Zorg/RIZIV matrix behind omzet 6.05m + 73 1.21m + why pnl DROP 335k while destin DROP 268k and cash JUMP 95k and FTE JUMP 76.2",
"active",
"",
"tick2456 leftover mined city_houthulst WZC after De Pallieterkes different-KBO skip; 1 VE; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT t Sloeberke YE2024; NOT Elief CDN 403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_path=DATA/"foi_queue.csv"
foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Houthulst>GroeneVerte>WZC",
"entity_id": EID,
"what_is_missing": "Zorg/RIZIV split behind omzet 6054692 + 73 1212686 (6.9 omzet empty) and why pnl DROP 335472 while destin DROP 268378 and cash JUMP 94916 and FTE JUMP 76.2",
"why_it_matters": "Strong official PDF leftover public WZC of mined city_houthulst; 6.05m omzet envelope; public Departement Zorg-erkend RVT",
"priority": "8",
"recipient_body": "VZW DE GROENE VERTE WOON EN ZORG / Raad van Bestuur",
"recipient_email": "info@degroeneverte.be",
"recipient_postal": "Kouterstraat 46 8650 Houthulst",
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
"notes": "tick2456; ready NOT sent; Strong official native NBB PDF; leftover mined city_houthulst WZC after De Pallieterkes different-KBO skip; 1 VE; off Drongen",
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
if rq_raw.count(b"rq_2456,")!=1: raise SystemExit(f"bad 2456 count {rq_raw.count(b'rq_2456,')}")
if b"rq_2457," in rq_raw: raise SystemExit("2457 exists")
idx=rq_raw.rfind(b"rq_2456,")
if idx<0: raise SystemExit("rq_2456 not found")
new_2456=(
"rq_2456,leftover dual De Groene Verte woon en zorg YE2025,hole_fill,8,done,L5,vzw_groene_verte_houthulst,"
"Took unused leftover public WZC DE GROENE VERTE WOON EN ZORG 0465.061.649 leftover mined city_houthulst. Official NBB VOL-VZW YE2025 2026-00200541 native 47p. Envelope omzet70 JUMP 6054692; 73 JUMP 1212686; pnl DROP 335472; destin DROP 268378. NOT De Pallieterkes remine. NOT De Vleugels remine.,"
f",{STAMP},{STAMP},tick2456 leftover mined city_houthulst WZC; Strong native PDF; 1 VE; next every-10 is 2460\n"
)
new_2457=(
"rq_2457,leftover dual after De Groene Verte woon en zorg — hunt unused public dual,hole_fill,8,open,L5,,"
"After De Groene Verte woon en zorg YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Kinderlach / De Linde Ronse / Villa Boempatat / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende / t Sloeberke / Soetkin still YE2024 — take ONLY if unused + official YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. VKA 0433.480.132 leftover city_antwerpen YE2025 filed 29.06.2026 — take ONLY if unused + deposit-id + live 2026pdf. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2456; De Groene Verte taken leftover mined city_houthulst WZC; De Pallieterkes taken leftover mined city_lier CIK; De Medemens Kinderdagverblijven taken leftover mined city_antwerpen CIK; OKO & ZO taken leftover mined city_zele CIK; KINDEROPVANG De Harlekijntjes taken leftover mined city_tielt CIK; Kinderdagverblijf De Hartjes Ninove taken leftover mined city_ninove CIK; Groepsopvang De Hartjes Tienen taken leftover mined city_tienen CIK\n"
)
if new_2456.count("\n")!=1 or new_2457.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2456.encode("utf-8"))
    f.write(new_2457.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2456", chk.count(b"rq_2456,"), "n2457", chk.count(b"rq_2457,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2456,2456,no,tick2456 leftover dual DE GROENE VERTE WOON EN ZORG 0465.061.649 Strong native PDF (omzet70 JUMP 6054692 envelope; 73 JUMP 1212686; 76A empty DROP; 70/76A JUMP 7426417; bruto empty VOL; pnl DROP 335472; 9901 DROP 382667; equity JUMP 8670513; assets DROP 12123011; debt DROP 3441502; FTE 76.2 JUMP; kapitaalsubsidies DROP 3037049; destin691 DROP 268378; 791 empty; cash JUMP 94916; geldbeleggingen JUMP 2766663; 1 VE leftover city_houthulst WZC); leftover mined city_houthulst WZC; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT t Sloeberke YE2024; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; next every-10 is 2460; next rq_2457 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")
print("WRITE CORE DONE")
