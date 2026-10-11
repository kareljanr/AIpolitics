from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2463_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_dnopvang_jr2025_nbb_pdf_2463"
SRC_KBO="src_dnopvang_kbo_2463"
SRC_SBM="src_dnopvang_sbm_2463"
SRC_SITE="src_dnopvang_site_2463"
EID="vzw_dn_opvang_oostende"
GAP="gap_dnopvang_opgroeien_matrix_bruto_988k_omzet73_empty_pnl_drop_144k_destin_drop_144k_l5"
COMM="comm_dnopvang_jr2025_statutory_bruto_988k_omzet73_empty_pnl_drop_144k"
LB="lb_dnopvang_bruto_988k_omzet73_empty_pnl_drop_144k_destin_drop_144k_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf D'n Opvang deposit 2026-00096188,http://cdn.staatsbladmonitor.be/2026pdf/2026-00096188.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2463; official native PDF 43847 bytes 11p VKT-VZW 23.0.8 m04-f; header 30.04.2026; AV 02.04.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-04-30 14:22:23 UTC OpenPDF 1.3.26; all 11p native; CDN 2026-00096188 HEAD 200 Last-Modified 05.05.2026; VKT-VZW 6.1.1 6.1.3 6.2 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf D'n Opvang 0676.442.465,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0676442465,KBO Public Search FOD Economie,{DAY},official_register,tick2463; Actief; 1 VE 2.270.723.280 Kinderdagverblijf D'n VZW Langestraat 65 8400 Oostende since 01.01.2018; VZW since 28.04.2017; begindatum 28.04.2017; zetel Langestraat 65 8400 Oostende since 28.04.2017; Werkgever RSZ since 01.01.2018; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 11.10.2017; FOI info@denopvang.be; leftover mined city_oostende CIK; NOT Zo Groot 0818.420.771 remine; NOT CAR Overleie remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Kinderdagverblijf D'n Opvang 0676442465 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0676442465,NBB Consult / SBM,{DAY},official_register,tick2463; deposit-id 2026-00096188 YE 01.01.2025-31.12.2025 filing 30.04.2026 published 30.04.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Kinderdagverblijf D'n Opvang FOI contact leftover city_oostende CIK,https://denopvang.be/,VZW Kinderdagverblijf D'n Opvang leftover city_oostende CIK Opgroeien groepsopvang,{DAY},foi_contact,tick2463; FOI info@denopvang.be; zetel Langestraat 65 8400 Oostende; opvanglocatie Louisastraat 5 8400 Oostende; 1 VE leftover mined city_oostende after CAR Overleie different-city skip; NOT Kloosterstraat 6 Drongen; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT Zo Groot YE2024; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf D'n Opvang,ASBL Kinderdagverblijf D'n Opvang,D'n Opvang VZW (leftover city_oostende CIK),parastatal,city_oostende,nl,https://denopvang.be/,info@denopvang.be,Langestraat 65 8400 Oostende,tick2463 YE2025 Strong official native NBB PDF deposit 2026-00096188 + Strong KBO 0676.442.465 Actief 1 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto DROP 987967 envelope; pnl DROP 144454; 9901 DROP 141492; equity JUMP 725999; assets JUMP 1221930; debt DROP 495931; FTE 16.2 JUMP; kapitaalsubsidies empty; destin691 DROP 144454; 791 empty; cash JUMP 1133862; geldbeleggingen empty DROP was 200000; leftover mined city_oostende after CAR Overleie different-city skip; 1 VE CIK groepsopvang not private; NOT Kloosterstraat 6 Drongen; NOT CAR Overleie 0454.250.505 remine; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT H.Hart WZC 0413.595.330; NOT Zo Groot 0818.420.771 leftover city_oostende YE2024; NOT Kinderopvang Scholengroep Stroom 0891.472.362 already in entities; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_dnopvang_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900 because omzet empty),{SRC_PDF},strong,tick2463; PDF p5 native; YE2024 identical empty; 73 empty; 76A empty",
f"bud_dnopvang_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2463; PDF p5 native; YE2024 identical empty; FOI Opgroeien matrix behind bruto 987967",
f"bud_dnopvang_opbr_jr2025_statutory,{EID},2025,987967,987967,987967,NBB VKT-VZW envelope bruto 9900 YE2025 DROP -1.27% (omzet 70 empty + 73 empty + 76A empty so VKT envelope is 9900),{SRC_PDF},strong,tick2463; PDF p5 native; YE2024 identical 1000663; 70/76A empty",
f"bud_dnopvang_bruto_jr2025_statutory,{EID},2025,987967,987967,987967,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -1.27% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2463; PDF p5 native; YE2024 identical 1000663; 76A empty; 73 empty",
f"bud_dnopvang_pnl_jr2025_statutory,{EID},2025,144454,144454,144454,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 DROP -31.15% (was 209823),{SRC_PDF},strong,tick2463; PDF p5 native; YE2024 identical 209823; bedrijfswinst 9901 141492 DROP; destin691 144454 DROP full pnl to bestemde fondsen",
f"bud_dnopvang_bedrijfswinst_jr2025_statutory,{EID},2025,141492,141492,141492,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -31.25% (was 205820),{SRC_PDF},strong,tick2463; PDF p5 native; YE2024 identical 205820; 62 842213 JUMP; 630 2278 DROP; 66A empty",
f"bud_dnopvang_equity_jr2025_statutory,{EID},2025,725999,725999,725999,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +24.84%,{SRC_PDF},strong,tick2463; PDF p4 native; YE2024 identical 581544; kapitaalsubsidies empty; overgedragen 14 empty; fondsen 10 empty; bestemde fondsen 13 725999 JUMP",
f"bud_dnopvang_assets_jr2025_statutory,{EID},2025,1221930,1221930,1221930,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +8.78%,{SRC_PDF},strong,tick2463; PDF p3 native; YE2024 identical 1123312; MVA 22/27 18169 DROP; cash 1133862 JUMP; geldbeleggingen empty DROP; aanbouw 27 empty",
f"bud_dnopvang_debt_jr2025_statutory,{EID},2025,495931,495931,495931,NBB VKT-VZW code 17/49 schulden YE2025 DROP -8.46%,{SRC_PDF},strong,tick2463; PDF p4 native; YE2024 identical 541768; 17 empty; 42/48 494981 DROP",
f"bud_dnopvang_cash_jr2025_statutory,{EID},2025,1133862,1133862,1133862,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +34.71%,{SRC_PDF},strong,tick2463; PDF p3 native; YE2024 identical 841694; geldbeleggingen 50/53 empty DROP was 200000",
f"bud_dnopvang_destin_jr2025_statutory,{EID},2025,144454,144454,144454,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 DROP -31.15% (full pnl 144454 to bestemde fondsen; 13 JUMP 725999),{SRC_PDF},strong,tick2463; PDF p6 native; YE2024 destin 209823; bestemde fondsen 13 725999 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":0,\"\"2025_bruto\"\":987967,"
"\"\"2025_pnl\"\":144454,\"\"2025_bedrijfswinst\"\":141492,"
"\"\"2025_equity\"\":725999,\"\"2025_assets\"\":1221930,\"\"2025_debt\"\":495931,"
"\"\"2025_fte\"\":16.2,\"\"2025_kapitaalsubsidies\"\":0,\"\"2025_destin691\"\":144454,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1133862,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":842213,\"\"2025_gebouwen22\"\":0,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":725999,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":2278,\"\"2025_capex\"\":0,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70_76A\"\":0,\"\"2024_bruto\"\":1000663,\"\"2024_pnl\"\":209823,\"\"2024_bedrijfswinst\"\":205820,"
"\"\"2024_equity\"\":581544,\"\"2024_assets\"\":1123312,"
"\"\"2024_debt\"\":541768,\"\"2024_cash\"\":841694,\"\"2024_fte\"\":15.2,"
"\"\"2024_destin691\"\":209823,\"\"2024_kapitaalsubsidies\"\":0,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":200000}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Kinderdagverblijf D'n Opvang YE2025 (bruto DROP 988k / omzet+73 empty VKT / pnl DROP 144k / destin DROP 144k / Strong PDF),{EID},Opgroeien + leftover city_oostende CIK,VZW Kinderdagverblijf D'n Opvang (KBO 0676.442.465; Actief; 1 VE; RSZ2025 88.911; zetel + 1/1 VE Oostende),2026-04-02,2025,2025,987967,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00096188.pdf,Public CIK dual of mined city_oostende,Publish Opgroeien matrix behind bruto 988k + why omzet+73 empty and why pnl DROP 144k while destin DROP 144k and cash JUMP 1.13m and FTE 16.2,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Oostende>DnOpvang>JR2025_statutory_L5,tick2463; Strong official native PDF; leftover mined city_oostende CIK; 1 VE; NOT every-10; NOT Kloosterstraat 6 Drongen; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"D'n Opvang bruto DROP 988k / omzet+73 empty VKT / pnl DROP 144k / destin DROP 144k (YE2025 leftover city_oostende CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Oostende>DnOpvang>JR2025",
"987967",
"987967",
"PDF bruto 987967 envelope because omzet empty; 70 empty; 73 empty; 76A empty; bedrijfswinst DROP 141492; pnl DROP 144454; equity JUMP 725999; assets JUMP 1221930; debt DROP 495931; FTE 16.2 JUMP; kapitaalsubsidies empty; destin691 DROP 144454; cash JUMP 1133862; geldbeleggingen empty DROP was 200000; 1 VE leftover city_oostende CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_oostende CIK",
"CIK / Kind en Gezin groepsopvang leftover city_oostende",
"988k bruto envelope; omzet+73 empty VKT; pnl DROP 144k; destin DROP 144k; cash JUMP 1.13m; leftover city_oostende CIK",
"5.15",
"5.10",
"5.00",
"5.09",
"FOI Opgroeien matrix behind bruto 988k + why omzet+73 empty and why pnl DROP 144k while destin DROP 144k and cash JUMP 1.13m and FTE 16.2",
"active",
"",
"tick2463 leftover mined city_oostende CIK after CAR Overleie different-city skip; 1 VE; NOT every-10; NOT CAR Overleie remine; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Zo Groot YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Oostende>DnOpvang>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind bruto 987967 (omzet 70 empty + 73 empty + 76A empty) and why pnl DROP 144454 while destin DROP 144454 and cash JUMP 1133862 and geldbeleggingen DROP to empty (was 200000) and FTE 16.2",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_oostende; VKT envelope bruto 988k because omzet empty; public Opgroeien groepsopvang 80 plaatsen",
"priority": "8",
"recipient_body": "VZW Kinderdagverblijf D'n Opvang / Raad van Bestuur",
"recipient_email": "info@denopvang.be",
"recipient_postal": "Langestraat 65 8400 Oostende",
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
"notes": "tick2463; ready NOT sent; Strong official native NBB PDF; leftover mined city_oostende CIK after CAR Overleie different-city skip; 1 VE; NOT every-10; off Drongen",
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
if rq_raw.count(b"rq_2463,")!=1: raise SystemExit(f"bad 2463 count {rq_raw.count(b'rq_2463,')}")
if b"rq_2464," in rq_raw: raise SystemExit("2464 exists")
idx=rq_raw.rfind(b"rq_2463,")
if idx<0: raise SystemExit("rq_2463 not found")
new_2463=(
"rq_2463,leftover dual Kinderdagverblijf D'n Opvang YE2025,hole_fill,8,done,L5,vzw_dn_opvang_oostende,"
"Took unused leftover public CIK Kinderdagverblijf D'n Opvang 0676.442.465 leftover mined city_oostende. Official NBB VKT-VZW YE2025 2026-00096188 native 11p. Envelope bruto DROP 987967 (omzet+73 empty); pnl DROP 144454; destin DROP 144454; cash JUMP 1133862. NOT CAR Overleie remine. NOT Zo Groot remine. NOT Kinderlach YE2024.,"
f",{STAMP},{STAMP},tick2463 leftover mined city_oostende CIK; Strong native PDF; 1 VE; next every-10 is 2470\n"
)
new_2464=(
"rq_2464,leftover dual after Kinderdagverblijf D'n Opvang — hunt unused public dual,hole_fill,8,open,L5,,"
"After Kinderdagverblijf D'n Opvang YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT D'n Opvang remine. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale. NOT Zo Groot remine.,"
f",{STAMP},{STAMP},spawned after tick2463; D'n Opvang taken leftover mined city_oostende CIK; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2463.count("\n")!=1 or new_2464.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2463.encode("utf-8"))
    f.write(new_2464.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2463", chk.count(b"rq_2463,"), "n2464", chk.count(b"rq_2464,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2463,2463,no,tick2463 leftover dual Kinderdagverblijf D'n Opvang 0676.442.465 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope bruto DROP 987967; pnl DROP 144454; 9901 DROP 141492; equity JUMP 725999; assets JUMP 1221930; debt DROP 495931; FTE 16.2 JUMP; kapitaalsubsidies empty; destin691 DROP 144454; 791 empty; cash JUMP 1133862; geldbeleggingen empty DROP was 200000; 1 VE leftover city_oostende CIK); leftover mined city_oostende CIK; NOT CAR Overleie remine; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT Zo Groot YE2024; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; next every-10 is 2470; next rq_2464 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2463 - rq_2463 Kinderdagverblijf D'n Opvang (bruto DROP 988k / omzet+73 empty VKT / pnl DROP 144k / destin DROP 144k / Strong PDF)

- Unit: **rq_2463** leftover dual after **CAR Overleie@2462**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 SCAN — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024** (NBB last periodEnd 2024-12-31; filed 13.08.2025). Kinderlach leftover city_eeklo still **YE2024** (NBB last periodEnd 2024-12-31; filed 09.07.2025). Villa Boempatat leftover city_gent **YE2025** **2026-00396513** CDN **403** / SCAN no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024** (NBB last periodEnd 2024-12-31; filed 26.06.2025). Jessa leftover city_hasselt hospital YE2025 PDF / hospital special schema — not taken. Mini-creches GO! Next leftover city_hasselt still **YE2024** (NBB last periodEnd 2024-12-31; filed 23.02.2026). Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024; second 2026 deposit is YE2023 restatement). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 YE2025 zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale leftover city_herentals YE2025 — zorgcentrale not in dual types — not taken. CAR Overleie 0454.250.505 just mined — do not remine. Gesticht just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. Vriendenkring Revalidatiecentrum Halle 0436.787.139 leftover city_halle — NBB 0 deposits — not taken. Gezondheid en Welzijn Oost-Vlaanderen 0457.777.246 YE2025 0 VE / no dual-type toelating — not taken. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Kinderdagverblijf D'n Opvang** YE2025 (KBO **0676.442.465**; zetel Langestraat 65 8400 Oostende; **Actief** **1 VE** **2.270.723.280** Kinderdagverblijf D'n VZW Langestraat 65 since 01.01.2018; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 11.10.2017; leftover of mined **city_oostende**; info@denopvang.be). Identity trap: D'n Opvang 0676.442.465 ≠ Zo Groot **0818.420.771** leftover city_oostende still YE2024; ≠ Kinderopvang Scholengroep Stroom **0891.472.362** leftover city_oostende already in entities; ≠ CAR Overleie **0454.250.505** leftover city_kortrijk just mined; ≠ Gesticht **0410.918.031**; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ CAR Accent **0413.208.122**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6. 1 VE Oostende — leftover of mined city_oostende (zetel + 1/1 VE). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergunde; 80 plaatsen 0–3 Louisastraat 5) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not CAR Overleie remine / not Zo Groot remine. VKT-VZW **native text** (not scan) — 43847 B / 11p all native euros (VKT-VZW 6.1.1 / 6.1.3 / 6.2 / 6.3 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00096188** (43847 B / 11p; AV **02.04.2026**; header **30.04.2026**; CDN Last-Modified **05.05.2026**; CreationDate 30.04.2026 OpenPDF 1.3.26; all 11p native; prior-year identical not restated) — omzet 70 **empty** (VKT); 73 **empty** (VKT); 76A **empty**; envelope bruto 9900 **EUR987967** DROP −1.27% (VKT envelope because omzet empty; was 1000663); bruto 9900 **EUR987967** DROP −1.27%; 62 **EUR842213** JUMP +6.59%; 630 **EUR2278** DROP −20.29%; 66A **empty**; 640/8 **EUR1983** JUMP +6.21%; bedrijfswinst 9901 **EUR141492** DROP −31.25%; pnl 9904 **EUR144454** DROP −31.15%; equity **EUR725999** JUMP +24.84%; assets **EUR1221930** JUMP +8.78%; debt **EUR495931** DROP −8.46%; FTE **16.2** JUMP +6.58% (was 15.2; 9087 16.2; 105 17.6); kapitaalsubsidies **empty**; destin 691 **EUR144454** DROP −31.15% (full pnl to bestemde fondsen; 13 JUMP 725999); 791 **empty**; cash **EUR1133862** JUMP +34.71%; geldbeleggingen **empty** DROP (was 200000); gebouwen **empty**; MVA 22/27 **EUR18169** DROP; aanbouw **empty**; capex **empty**; fondsen 10 **empty**; overgedragen 14 **empty**; bestemde fondsen 13 **EUR725999** JUMP; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_oostende CIK. NOT Kloosterstraat 6 Drongen. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT Zo Groot YE2024. NOT De Bolster Zwalm. NOT GERUST zorgcentrale.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.09); entities (+1 vzw_dn_opvang_oostende); foi + draft `gap_dnopvang_opgroeien_matrix_bruto_988k_omzet73_empty_pnl_drop_144k_destin_drop_144k_l5`; rq_2463=done + rq_2464 open; loop_state ticks=2463; raw tick2463/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2464 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT D'n Opvang remine / NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale / NOT Zo Groot remine). NOW leftover candidate: Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip unless LOOP.md leftover training priority. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
