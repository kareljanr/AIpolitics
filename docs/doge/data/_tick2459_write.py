from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2459_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_elief_jr2025_nbb_pdf_2459"
SRC_KBO="src_elief_kbo_2459"
SRC_SBM="src_elief_sbm_2459"
SRC_SITE="src_elief_site_2459"
EID="vzw_elief_antwerpen"
GAP="gap_elief_opgroeien_matrix_bruto_1_04m_omzet73_empty_pnl_jump_33k_destin_jump_33k_l5"
COMM="comm_elief_jr2025_statutory_bruto_1_04m_omzet73_empty_pnl_jump_33k"
LB="lb_elief_bruto_1_04m_omzet73_empty_pnl_jump_33k_destin_jump_33k_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 SPEELHUIS ELIEF deposit 2026-00374905,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/1c664634-873f-11f1-98e5-9fad28045fc6,NBB official WVV deposit PDF,{DAY},budget,tick2459; official native PDF 39078 bytes 10p VKT-VZW 25.0.13 m04-f; header 30.07.2026; AV 30.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-08-04 00:12:49 UTC OpenPDF 1.3.26; all 10p native; CDN 2026-00374905 403 so official NBB PDF used; VKT-VZW 6.1.1 6.2 6.3 6.5 6.6 6.7 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO SPEELHUIS ELIEF 0451.624.377,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0451624377,KBO Public Search FOD Economie,{DAY},official_register,tick2459; Actief; 4 VE incl 2.150.857.511 SPEELHUIS ELIEF Patriottenstraat 62 2600 Antwerpen since 03.01.2006; VZW since 17.11.1993; begindatum 17.11.1993; zetel Patriottenstraat 62 2600 Antwerpen since 17.11.1993; RSZ2025 88.911; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI walter@posthofvzw.be; leftover mined city_antwerpen CIK; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT De Medemens KDV 0893.678.915 remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche SPEELHUIS ELIEF 0451624377 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0451624377,NBB Consult,{DAY},official_register,tick2459; deposit-id 2026-00374905 YE 01.01.2025-31.12.2025 filing 30.07.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table; CDN 403",
f"{SRC_SITE},SPEELHUIS ELIEF FOI contact leftover city_antwerpen CIK,https://buurtcentrum-posthof.be/elief.html,VZW SPEELHUIS ELIEF leftover city_antwerpen CIK Kind en Gezin-vergunde groepsopvang,{DAY},foi_contact,tick2459; FOI walter@posthofvzw.be info@elief.be; zetel Patriottenstraat 62 2600 Antwerpen Berchem; uitbating Sint-Lambertusstraat 58; leftover mined city_antwerpen after Soetkin different-KBO skip; 4 VE Antwerpen CIK; NOT Kloosterstraat 6 Drongen; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN; NOT VKA not locked this tick; NOT Hebe training",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},SPEELHUIS ELIEF vzw,ASBL SPEELHUIS ELIEF,SPEELHUIS ELIEF VZW (leftover city_antwerpen CIK),parastatal,city_antwerpen,nl,https://buurtcentrum-posthof.be/elief.html,walter@posthofvzw.be,Patriottenstraat 62 2600 Antwerpen,tick2459 YE2025 Strong official native NBB PDF deposit 2026-00374905 + Strong KBO 0451.624.377 Actief 4 VE RSZ2025 88.911 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 empty VKT; 73 empty VKT; 76A empty; bruto DROP 1035435 envelope; pnl JUMP 33404; 9901 JUMP 31547; equity JUMP 1100487; assets JUMP 1709941; debt JUMP 609454; FTE 16.1 DROP; kapitaalsubsidies DROP 169808; destin691 JUMP 33404; 791 empty; cash JUMP 1427686; geldbeleggingen empty; leftover mined city_antwerpen after Soetkin different-KBO skip; 4 VE CIK groepsopvang not private; CDN 403 bypassed official NBB PDF; NOT Kloosterstraat 6 Drongen; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT H.Hart WZC 0413.595.330; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN 2026-00396513; NOT VKA 0433.480.132 leftover city_antwerpen YE2025 2026-00212541 not locked this tick; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_elief_bruto_jr2025_statutory,{EID},2025,1035435,1035435,1035435,NBB VKT-VZW code 9900 brutomarge YE2025 DROP -5.73% (VKT envelope because omzet 70 empty and 73 empty),{SRC_PDF},strong,tick2459; PDF p5 native; YE2024 identical 1098345; 76A empty",
f"bud_elief_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT; envelope is bruto 9900),{SRC_PDF},strong,tick2459; PDF p5 native; YE2024 identical empty; 73 also empty VKT",
f"bud_elief_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2459; PDF p5 native; YE2024 identical empty; FOI Opgroeien split behind bruto 1035435",
f"bud_elief_pnl_jr2025_statutory,{EID},2025,33404,33404,33404,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +1229.25% (was 2513),{SRC_PDF},strong,tick2459; PDF p5 native; YE2024 identical 2513; bedrijfswinst 9901 31547 JUMP; destin691 JUMP 33404",
f"bud_elief_bedrijfswinst_jr2025_statutory,{EID},2025,31547,31547,31547,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +482.26% (was 5418),{SRC_PDF},strong,tick2459; PDF p5 native; YE2024 identical 5418; 62 997346 DROP; 630 6542 FLAT; 640/8 empty",
f"bud_elief_equity_jr2025_statutory,{EID},2025,1100487,1100487,1100487,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +2.54%,{SRC_PDF},strong,tick2459; PDF p4 native; YE2024 identical 1073256; kapitaalsubsidies 169808 DROP; overgedragen 14 empty; fondsen 10 empty; bestemde fondsen 13 930679 JUMP",
f"bud_elief_assets_jr2025_statutory,{EID},2025,1709941,1709941,1709941,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +7.78%,{SRC_PDF},strong,tick2459; PDF p3 native; YE2024 identical 1586520; MVA 22/27 170527 DROP; cash 1427686 JUMP; geldbeleggingen empty; aanbouw 27 empty",
f"bud_elief_debt_jr2025_statutory,{EID},2025,609454,609454,609454,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +18.74%,{SRC_PDF},strong,tick2459; PDF p4 native; YE2024 identical 513264; 17 empty; 42/48 334250 JUMP",
f"bud_elief_cash_jr2025_statutory,{EID},2025,1427686,1427686,1427686,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +14.52%,{SRC_PDF},strong,tick2459; PDF p3 native; YE2024 identical 1246645; geldbeleggingen 50/53 empty",
f"bud_elief_destin_jr2025_statutory,{EID},2025,33404,33404,33404,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP (equals pnl 33404; 791 empty),{SRC_PDF},strong,tick2459; PDF p6 native; YE2024 destin 2513; bestemde fondsen 13 930679 JUMP FOI",
f"bud_elief_62_jr2025_statutory,{EID},2025,997346,997346,997346,NBB VKT-VZW code 62 bezoldigingen YE2025 DROP -8.20%,{SRC_PDF},strong,tick2459; PDF p5 native; YE2024 identical 1086385; FTE 16.1 DROP",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":0,"
"\"\"2025_bruto\"\":1035435,"
"\"\"2025_pnl\"\":33404,\"\"2025_bedrijfswinst\"\":31547,"
"\"\"2025_equity\"\":1100487,\"\"2025_assets\"\":1709941,\"\"2025_debt\"\":609454,"
"\"\"2025_fte\"\":16.1,\"\"2025_kapitaalsubsidies\"\":169808,\"\"2025_destin691\"\":33404,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":1427686,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":997346,\"\"2025_gebouwen22\"\":170527,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":930679,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":6542,\"\"2025_capex\"\":0,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_bruto\"\":1098345,\"\"2024_pnl\"\":2513,\"\"2024_bedrijfswinst\"\":5418,"
"\"\"2024_equity\"\":1073256,\"\"2024_assets\"\":1586520,"
"\"\"2024_debt\"\":513264,\"\"2024_cash\"\":1246645,\"\"2024_fte\"\":18.2,"
"\"\"2024_destin691\"\":2513,\"\"2024_kapitaalsubsidies\"\":175981,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},SPEELHUIS ELIEF YE2025 (bruto DROP 1.04m / omzet+73 empty VKT / pnl JUMP 33k / destin JUMP 33k / Strong PDF),{EID},Opgroeien + leftover city_antwerpen CIK,VZW SPEELHUIS ELIEF (KBO 0451.624.377; Actief; 4 VE; RSZ2025 88.911; zetel + 4/4 VE Antwerpen Berchem),2026-06-30,2025,2025,1035435,{cash_json},0,active,https://consult.cbso.nbb.be/api/external/broker/public/deposits/pdf/1c664634-873f-11f1-98e5-9fad28045fc6,Public CIK dual of mined city_antwerpen,Publish Opgroeien matrix behind bruto 1.04m + why omzet+73 empty VKT + why pnl JUMP 33k while destin JUMP 33k and cash JUMP 1.43m and FTE DROP 16.1,{SRC_PDF},strong,Vlaanderen>Antwerpen>Antwerpen>Elief>JR2025_statutory_L5,tick2459; Strong official native PDF; leftover mined city_antwerpen CIK; 4 VE; CDN 403 bypassed official NBB PDF; NOT Kloosterstraat 6 Drongen; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"SPEELHUIS ELIEF bruto DROP 1.04m / omzet+73 empty VKT / pnl JUMP 33k / destin JUMP 33k (YE2025 leftover city_antwerpen CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Antwerpen>Antwerpen>Elief>JR2025",
"1035435",
"1035435",
"PDF 9900 1035435 envelope; omzet empty VKT; 73 empty VKT; 76A empty; bruto DROP 1035435; bedrijfswinst JUMP 31547; pnl JUMP 33404; equity JUMP 1100487; assets JUMP 1709941; debt JUMP 609454; FTE 16.1 DROP; kapitaalsubsidies DROP 169808; destin691 JUMP 33404; cash JUMP 1427686; geldbeleggingen empty; 4 VE leftover city_antwerpen CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_antwerpen CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_antwerpen",
"1.04m bruto envelope; omzet+73 empty VKT; pnl JUMP 33k; destin JUMP 33k; cash JUMP 1.43m; leftover city_antwerpen CIK",
"5.15",
"5.10",
"5.00",
"5.08",
"FOI Opgroeien matrix behind bruto 1.04m + why omzet+73 empty VKT + why pnl JUMP 33k while destin JUMP 33k and cash JUMP 1.43m and FTE DROP 16.1",
"active",
"",
"tick2459 leftover mined city_antwerpen CIK after Soetkin different-KBO skip; 4 VE; CDN 403 bypassed official NBB PDF; NOT Soetkin remine; NOT t Sloeberke remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Villa Boempatat SCAN; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_path=DATA/"foi_queue.csv"
foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Antwerpen>Antwerpen>Elief>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind bruto 1035435 (omzet 70 empty + 73 empty VKT) and why pnl JUMP 33404 while destin JUMP 33404 and cash JUMP 1427686 and FTE DROP 16.1",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_antwerpen; 1.04m bruto envelope; public Kind en Gezin-vergunde groepsopvang",
"priority": "8",
"recipient_body": "VZW SPEELHUIS ELIEF / Raad van Bestuur",
"recipient_email": "walter@posthofvzw.be",
"recipient_postal": "Patriottenstraat 62 2600 Antwerpen",
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
"notes": "tick2459; ready NOT sent; Strong official native NBB PDF; leftover mined city_antwerpen CIK after Soetkin different-KBO skip; 4 VE; CDN 403 bypassed official NBB PDF; off Drongen",
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
if rq_raw.count(b"rq_2459,")!=1: raise SystemExit(f"bad 2459 count {rq_raw.count(b'rq_2459,')}")
if b"rq_2460," in rq_raw: raise SystemExit("2460 exists")
idx=rq_raw.rfind(b"rq_2459,")
if idx<0: raise SystemExit("rq_2459 not found")
new_2459=(
"rq_2459,leftover dual SPEELHUIS ELIEF YE2025,hole_fill,8,done,L5,vzw_elief_antwerpen,"
"Took unused leftover public CIK SPEELHUIS ELIEF 0451.624.377 leftover mined city_antwerpen. Official NBB VKT-VZW YE2025 2026-00374905 native 10p (CDN 403 bypassed). Envelope 9900 DROP 1035435; omzet+73 empty VKT; pnl JUMP 33404; destin JUMP 33404. NOT Soetkin remine. NOT t Sloeberke remine.,"
f",{STAMP},{STAMP},tick2459 leftover mined city_antwerpen CIK; Strong native PDF; 4 VE; CDN 403 bypassed official NBB PDF; next every-10 is 2460\n"
)
new_2460=(
"rq_2460,every-10 progress + leftover dual after Elief — hunt unused public dual,hole_fill,8,open,L5,,"
"EVERY-10 tick. Refresh progress_every_10_ticks.md layers A-E and doge_waste_top10_current.md. Then unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. VKA 0433.480.132 leftover city_antwerpen YE2025 2026-00212541 VOL-VZW — take ONLY if unused + official NBB/CDN YE2025 native PDF. CAR Antenne 3000 0433.184.479 leftover city_leuven YE2025 2026-00375503 CDN 403 — take ONLY if unused + official NBB native YE2025 PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 SCAN no extractable euros — skip unless native-text PDF. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. NOT Elief remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2459; Elief taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; De Pallieterkes taken leftover mined city_lier CIK; De Medemens Kinderdagverblijven taken leftover mined city_antwerpen CIK; EVERY-10 this tick\n"
)
if new_2459.count("\n")!=1 or new_2460.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2459.encode("utf-8"))
    f.write(new_2460.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2459", chk.count(b"rq_2459,"), "n2460", chk.count(b"rq_2460,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2459,2459,no,tick2459 leftover dual SPEELHUIS ELIEF 0451.624.377 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A empty; envelope 9900 DROP 1035435; bruto DROP 1035435; pnl JUMP 33404; 9901 JUMP 31547; equity JUMP 1100487; assets JUMP 1709941; debt JUMP 609454; FTE 16.1 DROP; kapitaalsubsidies DROP 169808; destin691 JUMP 33404; 791 empty; cash JUMP 1427686; geldbeleggingen empty; 4 VE leftover city_antwerpen CIK); leftover mined city_antwerpen CIK; CDN 403 bypassed official NBB PDF; NOT Soetkin remine; NOT t Sloeberke remine; NOT H.Hart WZC remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN 2026-00396513; NOT VKA 2026-00212541 not locked this tick; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; next every-10 is 2460; next rq_2460 leftover dual + every-10\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2459 - rq_2459 SPEELHUIS ELIEF (bruto DROP 1.04m / omzet+73 empty VKT / pnl JUMP 33k / destin JUMP 33k / Strong PDF)

- Unit: **rq_2459** leftover dual after **Soetkin@2458**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. De Bolster 0861.680.989 still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. CAR Overleie 0454.250.505 still **YE2024**. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 0433.184.479 leftover city_leuven unused YE2025 NBB **2026-00375503** CDN still **403** — not taken this tick (Elief locked first). AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB **2026-00299006** CDN still **403** / hospital special schema skip. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 **2026-00145984** SCAN — not taken. De Linde Ronse 0778.279.401 leftover city_ronse still **YE2024** — not taken. Kinderlach 0450.275.186 leftover city_eeklo still **YE2024** — not taken. Villa Boempatat 0660.616.520 leftover city_gent unused official YE2025 **2026-00396513** (filed 13.08.2026; AV 27.05.2026; 1470764 B / 9p Microsoft Print To PDF) **SCAN** no extractable euros — not taken. Woon en Zorg H. Hart Kortrijk 0413.595.330 leftover city_kortrijk still **YE2024** — not taken. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. Jessa 0821.142.117 leftover city_hasselt hospital — no usable 2026pdf / hospital special schema — not taken. Mini-creches GO! Next 0896.468.060 leftover city_hasselt still **YE2024**. Zo Groot Oostende 0818.420.771 leftover city_oostende still **YE2024**. Familiehulp De Speelboom 0443.631.280 YE2025 unused but Brussels zetel 1210 — not taken (leftover-via-VE not enough per LOOP.md). Vrije Kinderdagverblijven Antwerpen 0433.480.132 leftover city_antwerpen unused YE2025 **2026-00212541** VOL-VZW — not taken this tick (Elief locked first). Hebe Kenniscentrum 0451.789.772 leftover city_antwerpen kenniscentrum/training RSZ 85.592 — skip (VBJK-class). WZC OLVA 0430.977.136 leftover city_antwerpen already in entities tick2036 — do not remine. Soetkin 0443.641.970 just mined — do not remine. Kinderdagverblijf t Sloeberke Groenheuvel 0410.973.360 already mined — do not remine. DE GROENE VERTE WOON EN ZORG 0465.061.649 already mined — do not remine. De Vleugels 0431.408.290 leftover city_houthulst VAPH already mined — do not remine. Kinderdagverblijf De Pallieterkes 0418.538.865 already mined — do not remine. De Medemens Kinderdagverblijven 0893.678.915 already mined — do not remine. De Medemens parent 0428.692.191 already mined — do not remine. OKO & ZO 0862.154.608 already mined — do not remine. KINDEROPVANG De Harlekijntjes 0407.700.403 already mined — do not remine. Kinderdagverblijf De Hartjes Ninove 0446.391.327 already mined — do not remine. Groepsopvang De Hartjes Tienen 0441.374.348 already mined — do not remine. Familia 0461.401.779 already mined — do not remine. Peutertuinen GO Mariakerke 0410.221.116 already mined — do not remine. WZC Annuntiaten Heverlee **0895.366.220** already in entities — do not remine. Kinderkuren 0478.167.834 already mined — do not remine. Kinderdagverblijven Leuven 0413.321.255 absorbed into Zorg Leuven — skip. t Bremhuisje 0445.265.533 stopgezet 07.10.1993 — skip. De Knuffelboom XL 0478.310.859 leftover city_gent UZ-CIK — NBB Consult no results skip. De Zeppelin 0454.001.867 leftover city_gent CIK — no jaarrekening skip. Kobe & Nanou is Stad Gent skip. KDV De Regenboog 0671.670.560 leftover city_gent is **BV private** skip. Groep Zorg H. Familie already in entities skip. Sint-Rafaël 0410.549.332 leftover city_gent VAPH — no jaarrekening skip. Vormingscentrum leftover city_gent training — not taken. VBJK leftover city_gent training/innovation — not taken. Helan Kinderopvang Helan-HH-adjacent — not taken. Re-HEAD YE2024 leftovers: Kinderlach still YE2024; De Linde Ronse still YE2024; Mini-creches GO Next still YE2024; Zo Groot Oostende still YE2024; H.Hart Kortrijk still YE2024. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW SPEELHUIS ELIEF** YE2025 (KBO **0451.624.377**; zetel Patriottenstraat 62 2600 Antwerpen / Berchem; **Actief** **4 VE** incl. **2.150.857.511** SPEELHUIS ELIEF Patriottenstraat 62 since 03.01.2006; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover of mined **city_antwerpen**; walter@posthofvzw.be / info@elief.be). Identity trap: SPEELHUIS ELIEF 0451.624.377 ≠ Soetkin **0443.641.970** leftover city_kortrijk CIK just mined; ≠ Kinderdagverblijf t Sloeberke Groenheuvel **0410.973.360**; ≠ Woon en Zorg H. Hart Kortrijk **0413.595.330**; ≠ DE GROENE VERTE WOON EN ZORG **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ Kinderdagverblijf De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915** leftover city_antwerpen CIK already mined; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ KINDEROPVANG De Harlekijntjes **0407.700.403**; ≠ Kinderdagverblijf De Hartjes Ninove **0446.391.327**; ≠ Groepsopvang De Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ BKO GENK-OOST **0475.432.830**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Vrije Kinderdagverblijven Antwerpen **0433.480.132** leftover city_antwerpen YE2025 **2026-00212541**; ≠ Hebe **0451.789.772** training; ≠ WZC OLVA **0430.977.136** already in entities; ≠ Villa Boempatat **0660.616.520** leftover city_gent YE2025 SCAN **2026-00396513**; ≠ De Pagadder **0888.028.268**; ≠ Quattro **0555.667.072**; ≠ TKDV Het Veer Kloosterstraat 6. 4 VE — leftover of mined city_antwerpen (zetel + 4/4 VE Antwerpen Berchem). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergunde HCO 910002117; mede gefinancierd Stad Antwerpen) not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Soetkin remine. VKT-VZW **native text** (not scan) — 39078 B / 10p all native euros (VKT-VZW 6.1.1 / 6.2 / 6.3 / 6.5 / 6.6 / 6.7 / 7 / 8 niet dienstig). CDN **403** stall bypassed via official NBB PDF.
- Found: official NBB VKT-VZW native PDF deposit **2026-00374905** (39078 B / 10p; AV **30.06.2026**; header **30.07.2026**; CreationDate 04.08.2026 OpenPDF 1.3.26; all 10p native; prior-year identical not restated; CDN 403) — omzet 70 **empty** (VKT); 73 **empty** (VKT); 76A **empty**; bruto 9900 **EUR1035435** DROP −5.73% (VKT envelope); 62 **EUR997346** DROP −8.20%; 630 **EUR6542** FLAT; 66A **empty**; 640/8 **empty**; bedrijfswinst 9901 **EUR31547** JUMP +482.26%; pnl 9904 **EUR33404** JUMP +1229.25%; equity **EUR1100487** JUMP +2.54%; assets **EUR1709941** JUMP +7.78%; debt **EUR609454** JUMP +18.74%; FTE **16.1** DROP −11.54% (was 18.2; 9087 16.1); kapitaalsubsidies **EUR169808** DROP −3.51%; destin 691 **EUR33404** JUMP (equals pnl; was 2513); 791 **empty**; cash **EUR1427686** JUMP +14.52%; geldbeleggingen **empty**; gebouwen **EUR170527** DROP; MVA 22/27 **EUR170527** DROP; aanbouw **empty**; capex **empty**; fondsen 10 **empty**; overgedragen 14 **empty**; bestemde fondsen 13 **EUR930679** JUMP; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 4 VE leftover mined city_antwerpen CIK. NOT Kloosterstraat 6 Drongen. NOT Soetkin remine. NOT t Sloeberke remine. NOT H.Hart WZC remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT KINDEROPVANG De Harlekijntjes remine. NOT Kinderdagverblijf De Hartjes Ninove remine. NOT Groepsopvang De Hartjes Tienen remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Villa Boempatat SCAN. NOT VKA not locked this tick. NOT Hebe training. NOT WZC OLVA remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.08); entities (+1 vzw_elief_antwerpen); foi + draft `gap_elief_opgroeien_matrix_bruto_1_04m_omzet73_empty_pnl_jump_33k_destin_jump_33k_l5`; rq_2459=done + rq_2460 open; loop_state ticks=2459; raw tick2459/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2460** IS every-10). Next: rq_2460 every-10 progress + unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT SPEELHUIS ELIEF remine / NOT Soetkin remine / NOT Kinderdagverblijf t Sloeberke remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT Kinderdagverblijf De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT KINDEROPVANG De Harlekijntjes remine / NOT Kinderdagverblijf De Hartjes Ninove remine / NOT Groepsopvang De Hartjes Tienen remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT COB Annuntiaten remine / NOT WZC Annuntiaten remine / NOT Kinderkuren / NOT t Zonnetje / NOT Wigwam / NOT Jeugdhulp Don Bosco / NOT t Anemoontje / NOT De Hummeltjes / NOT De Ukkies / NOT De Slabbertjes / NOT De Wissel / NOT Monte Rosa / NOT Avida / NOT IZW / NOT Ferm Kinderopvang / NOT Kinderdagverblijven Leuven absorbed / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine). NOW leftover candidate: Vrije Kinderdagverblijven Antwerpen 0433.480.132 leftover city_antwerpen unused YE2025 **2026-00212541** VOL-VZW — take ONLY if unused + official NBB/CDN YE2025 native PDF. CAR Antenne 3000 0433.184.479 leftover city_leuven unused YE2025 **2026-00375503** CDN **403** — take ONLY if unused + official NBB native YE2025 PDF. Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** SCAN no extractable euros — skip unless native-text PDF. Kinderlach 0450.275.186 leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse 0778.279.401 leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa 0821.142.117 leftover city_hasselt hospital — take ONLY if unused + official YE2025 euros extract. Familiehulp De Speelboom 0443.631.280 YE2025 Brussels zetel — leftover of mined parent Familiehulp + Flanders VEs Oostende/Aalst only if LOOP.md leftover-via-VE is enough. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — only if leftover training of mined parent is in LOOP.md priority. VBJK leftover city_gent training/innovation — skip unless leftover training of mined parent is in LOOP.md priority. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2460** IS every-10.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
