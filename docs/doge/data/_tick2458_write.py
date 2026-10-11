from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2458_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_soetkin_jr2025_nbb_pdf_2458"
SRC_KBO="src_soetkin_kbo_2458"
SRC_SBM="src_soetkin_sbm_2458"
SRC_SITE="src_soetkin_site_2458"
EID="vzw_soetkin_kortrijk"
GAP="gap_soetkin_opgroeien_matrix_opbr_7_05m_omzet_1_33m_73_5_59m_pnl_drop_699k_destin_empty_l5"
COMM="comm_soetkin_jr2025_statutory_opbr_7_05m_omzet_1_33m_73_5_59m_pnl_drop_699k"
LB="lb_soetkin_opbr_7_05m_omzet_1_33m_73_5_59m_pnl_drop_699k_destin_empty_jr2025"
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
f"{SRC_PDF},NBB VOL-VZW jaarrekening 2025 Soetkin deposit 2026-00270287,http://cdn.staatsbladmonitor.be/2026pdf/2026-00270287.pdf,NBB / Staatsbladmonitor CDN copy of WVV deposit,{DAY},budget,tick2458; official native PDF 98887 bytes 37p VOL-VZW 26.0.15 m05-f; header 07.07.2026; AV 31.03.2026; YE 01.01.2025-31.12.2025; CDN Last-Modified 2026-07-29; CreationDate 2026-07-09 04:00:31 UTC OpenPDF 1.3.26; all 37p native; VOL-VZW 6.1 6.2.1 6.2.2 6.2.3 6.2.4 6.3.4 6.3.5 6.4.2 6.5.2 6.6 6.10 6.16 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Soetkin 0443.641.970,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0443641970,KBO Public Search FOD Economie,{DAY},official_register,tick2458; Actief; 11 VE zetel Budastraat 30 8500 Kortrijk since 30.08.1999; VZW since 24.12.1990; begindatum 24.12.1990; RSZ2025 88.911; BTW2025 88.911+88.919; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI DIRECTIE@H-HART.BE; leftover mined city_kortrijk CIK; absorbed De Braamrakkertjes 0412.700.653 + Idefix 0453.819.349 since 31.03.2026 after YE2025; NOT t Sloeberke 0410.973.360 remine; NOT H.Hart WZC 0413.595.330; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche Soetkin 0443641970 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0443641970,NBB Consult / SBM,{DAY},official_register,tick2458; deposit-id 2026-00270287 YE 01.01.2025-31.12.2025 filing 09.07.2026 VOL-VZW; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},Soetkin FOI contact leftover city_kortrijk CIK,https://www.h-hart.be/,VZW Soetkin leftover city_kortrijk CIK Zorggroep H.Hart kinderopvang,{DAY},foi_contact,tick2458; FOI DIRECTIE@H-HART.BE; zetel Budastraat 30 8500 Kortrijk; leftover mined city_kortrijk after t Sloeberke different-KBO skip; 11 VE Kortrijk CIK; NOT Kloosterstraat 6 Drongen; NOT t Sloeberke remine; NOT H.Hart WZC remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Soetkin VZW,ASBL Soetkin,Soetkin VZW (leftover city_kortrijk CIK),parastatal,city_kortrijk,nl,https://www.h-hart.be/,DIRECTIE@H-HART.BE,Budastraat 30 8500 Kortrijk,tick2458 YE2025 Strong official native NBB PDF deposit 2026-00270287 + Strong KBO 0443.641.970 Actief 11 VE RSZ2025 88.911 BTW2025 88.911+88.919 toelating Kinderopvang Vlaamse Gemeenschap; omzet70 JUMP 1325536 commercial-only; 73 JUMP 5590556 all 733; 76A JUMP 6056; envelope 70/76A JUMP 7047286; bruto empty VOL; pnl DROP 699335; 9901 DROP 722007; equity JUMP 6276000; assets JUMP 8457267; debt JUMP 2181267; FTE 84.2 JUMP; kapitaalsubsidies DROP 1476725; destin691 empty; 791 empty; cash DROP 618230; geldbeleggingen empty; leftover mined city_kortrijk after t Sloeberke different-KBO skip; 11 VE CIK groepsopvang not private; NOT Kloosterstraat 6 Drongen; NOT t Sloeberke 0410.973.360 remine; NOT H.Hart WZC 0413.595.330; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Elief 0451.624.377 CDN 403; NOT VKA 0433.480.132 no deposit-id; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria CDN 403; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Villa Boempatat NOW YE2025 not taken this tick; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_soetkin_opbr_jr2025_statutory,{EID},2025,7047286,7047286,7047286,NBB VOL-VZW code 70/76A bedrijfsopbrengsten YE2025 JUMP +5.55% (VZW envelope because omzet 70 commercial-only vs large 73),{SRC_PDF},strong,tick2458; PDF p7 native; YE2024 identical 6676557; 76A 6056 JUMP",
f"bud_soetkin_omzet_jr2025_statutory,{EID},2025,1325536,1325536,1325536,NBB VOL-VZW code 70 omzet YE2025 JUMP +7.70% (commercial-only vs large 73 5590556; 6.9 omzet-uitsplitsing empty),{SRC_PDF},strong,tick2458; PDF p7 native; YE2024 identical 1230726; envelope is 70/76A 7047286",
f"bud_soetkin_73_jr2025_statutory,{EID},2025,5590556,5590556,5590556,NBB VOL-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +4.80% (all 733),{SRC_PDF},strong,tick2458; PDF p7+p23 native; YE2024 identical 5334701; FOI Opgroeien split behind 73 5590556",
f"bud_soetkin_pnl_jr2025_statutory,{EID},2025,699335,699335,699335,NBB VOL-VZW code 9904 winst van het boekjaar YE2025 DROP -5.72% (was 741770),{SRC_PDF},strong,tick2458; PDF p8 native; YE2024 identical 741770; bedrijfswinst 9901 722007 DROP; destin691 empty",
f"bud_soetkin_bedrijfswinst_jr2025_statutory,{EID},2025,722007,722007,722007,NBB VOL-VZW code 9901 bedrijfswinst YE2025 DROP -5.81% (was 766527),{SRC_PDF},strong,tick2458; PDF p7 native; YE2024 identical 766527; 62 4990506 JUMP; 630 283214 DROP; 640/8 14955 JUMP",
f"bud_soetkin_equity_jr2025_statutory,{EID},2025,6276000,6276000,6276000,NBB VOL-VZW code 10/15 eigen vermogen YE2025 JUMP +10.99%,{SRC_PDF},strong,tick2458; PDF p6 native; YE2024 identical 5654783; kapitaalsubsidies 1476725 DROP; overgedragen 14 4187325 JUMP; fondsen 10 611950 FLAT; bestemde fondsen 13 empty",
f"bud_soetkin_assets_jr2025_statutory,{EID},2025,8457267,8457267,8457267,NBB VOL-VZW code 20/58 totaal activa YE2025 JUMP +8.41%,{SRC_PDF},strong,tick2458; PDF p5 native; YE2024 identical 7801214; MVA 22/27 4758640 DROP; cash 618230 DROP; geldbeleggingen empty; aanbouw 27 3394 JUMP",
f"bud_soetkin_debt_jr2025_statutory,{EID},2025,2181267,2181267,2181267,NBB VOL-VZW code 17/49 schulden YE2025 JUMP +1.62%,{SRC_PDF},strong,tick2458; PDF p6 native; YE2024 identical 2146430; 17 932158 DROP; 42/48 1249109 JUMP",
f"bud_soetkin_cash_jr2025_statutory,{EID},2025,618230,618230,618230,NBB VOL-VZW code 54/58 liquide middelen YE2025 DROP -17.18%,{SRC_PDF},strong,tick2458; PDF p5 native; YE2024 identical 746506; geldbeleggingen 50/53 empty",
f"bud_soetkin_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VOL-VZW code 691 toevoeging bestemde fondsen YE2025 empty FLAT (791 empty; destin empty vs pnl 699335),{SRC_PDF},strong,tick2458; PDF p9 native; YE2024 destin empty; overgedragen 14 4187325 JUMP FOI",
f"bud_soetkin_62_jr2025_statutory,{EID},2025,4990506,4990506,4990506,NBB VOL-VZW code 62 bezoldigingen YE2025 JUMP +8.37%,{SRC_PDF},strong,tick2458; PDF p7 native; YE2024 identical 4605043; FTE 84.2 JUMP",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":1325536,\"\"2025_73\"\":5590556,\"\"2025_76A\"\":6056,"
"\"\"2025_opbr70_76A\"\":7047286,\"\"2025_bruto\"\":0,"
"\"\"2025_pnl\"\":699335,\"\"2025_bedrijfswinst\"\":722007,"
"\"\"2025_equity\"\":6276000,\"\"2025_assets\"\":8457267,\"\"2025_debt\"\":2181267,"
"\"\"2025_fte\"\":84.2,\"\"2025_kapitaalsubsidies\"\":1476725,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":618230,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":4990506,\"\"2025_gebouwen22\"\":4651258,"
"\"\"2025_aanbouw27\"\":3394,\"\"2025_66A\"\":3500,"
"\"\"2025_fondsen10\"\":611950,\"\"2025_overgedragen14\"\":4187325,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":283214,\"\"2025_capex\"\":58008,"
"\"\"2024_omzet\"\":1230726,\"\"2024_73\"\":5334701,"
"\"\"2024_opbr70_76A\"\":6676557,\"\"2024_pnl\"\":741770,\"\"2024_bedrijfswinst\"\":766527,"
"\"\"2024_equity\"\":5654783,\"\"2024_assets\"\":7801214,"
"\"\"2024_debt\"\":2146430,\"\"2024_cash\"\":746506,\"\"2024_fte\"\":77.8,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":1554844,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},Soetkin YE2025 (opbr JUMP 7.05m / omzet JUMP 1.33m commercial-only / 73 JUMP 5.59m / pnl DROP 699k / destin empty / Strong PDF),{EID},Opgroeien + leftover city_kortrijk CIK,VZW Soetkin (KBO 0443.641.970; Actief; 11 VE; RSZ2025 88.911; zetel + 4/11 VE Kortrijk),2026-03-31,2025,2025,7047286,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00270287.pdf,Public CIK dual of mined city_kortrijk,Publish Opgroeien matrix behind opbr 7.05m + why omzet 1.33m commercial-only vs 73 5.59m + why pnl DROP 699k while destin empty and cash DROP 618k and FTE JUMP 84.2,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>Soetkin>JR2025_statutory_L5,tick2458; Strong official native PDF; leftover mined city_kortrijk CIK; 11 VE; NOT Kloosterstraat 6 Drongen; NOT t Sloeberke remine; NOT H.Hart WZC remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"Soetkin opbr JUMP 7.05m / omzet JUMP 1.33m commercial-only / 73 JUMP 5.59m / pnl DROP 699k / destin empty (YE2025 leftover city_kortrijk CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Kortrijk>Soetkin>JR2025",
"7047286",
"7047286",
"PDF 70/76A 7047286 envelope; omzet 1325536 commercial-only; 73 5590556 all 733; 76A 6056; bruto empty VOL; bedrijfswinst DROP 722007; pnl DROP 699335; equity JUMP 6276000; assets JUMP 8457267; debt JUMP 2181267; FTE 84.2 JUMP; kapitaalsubsidies DROP 1476725; destin691 empty; cash DROP 618230; geldbeleggingen empty; 11 VE leftover city_kortrijk CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_kortrijk CIK",
"Kind en Gezin-vergunde groepsopvang leftover city_kortrijk",
"7.05m opbr envelope; omzet 1.33m commercial-only vs 73 5.59m; pnl DROP 699k; destin empty; cash DROP 618k; leftover city_kortrijk CIK",
"5.20",
"5.50",
"5.00",
"5.23",
"FOI Opgroeien matrix behind opbr 7.05m + why omzet 1.33m commercial-only vs 73 5.59m + why pnl DROP 699k while destin empty and cash DROP 618k and FTE JUMP 84.2",
"active",
"",
"tick2458 leftover mined city_kortrijk CIK after t Sloeberke different-KBO skip; 11 VE; NOT t Sloeberke remine; NOT H.Hart WZC remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Elief CDN 403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_path=DATA/"foi_queue.csv"
foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Kortrijk>Soetkin>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien split behind opbr 7047286 (omzet 70 1325536 commercial-only + 73 5590556 all 733) and why pnl DROP 699335 while destin empty and cash DROP 618230 and FTE JUMP 84.2",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_kortrijk; 7.05m opbr envelope; public Kind en Gezin-vergunde groepsopvang",
"priority": "8",
"recipient_body": "VZW Soetkin / Raad van Bestuur",
"recipient_email": "DIRECTIE@H-HART.BE",
"recipient_postal": "Budastraat 30 8500 Kortrijk",
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
"notes": "tick2458; ready NOT sent; Strong official native NBB PDF; leftover mined city_kortrijk CIK after t Sloeberke different-KBO skip; 11 VE; off Drongen",
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
if rq_raw.count(b"rq_2458,")!=1: raise SystemExit(f"bad 2458 count {rq_raw.count(b'rq_2458,')}")
if b"rq_2459," in rq_raw: raise SystemExit("2459 exists")
idx=rq_raw.rfind(b"rq_2458,")
if idx<0: raise SystemExit("rq_2458 not found")
new_2458=(
"rq_2458,leftover dual Soetkin YE2025,hole_fill,8,done,L5,vzw_soetkin_kortrijk,"
"Took unused leftover public CIK Soetkin 0443.641.970 leftover mined city_kortrijk. Official NBB VOL-VZW YE2025 2026-00270287 native 37p. Envelope 70/76A JUMP 7047286; omzet JUMP 1325536 commercial-only; 73 JUMP 5590556; pnl DROP 699335; destin empty. NOT t Sloeberke remine. NOT H.Hart WZC remine.,"
f",{STAMP},{STAMP},tick2458 leftover mined city_kortrijk CIK; Strong native PDF; 11 VE; next every-10 is 2460\n"
)
new_2459=(
"rq_2459,leftover dual after Soetkin — hunt unused public dual,hole_fill,8,open,L5,,"
"After Soetkin YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Villa Boempatat 0660.616.520 leftover city_gent NOW YE2025 filed 13.08.2026 — take ONLY if unused + official NBB/CDN YE2025 PDF. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. VKA 0433.480.132 leftover city_antwerpen YE2025 filed 29.06.2026 — take ONLY if unused + deposit-id + live 2026pdf. NOT Soetkin remine. NOT t Sloeberke remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels.,"
f",{STAMP},{STAMP},spawned after tick2458; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; De Pallieterkes taken leftover mined city_lier CIK; De Medemens Kinderdagverblijven taken leftover mined city_antwerpen CIK; OKO & ZO taken leftover mined city_zele CIK; KINDEROPVANG De Harlekijntjes taken leftover mined city_tielt CIK; Kinderdagverblijf De Hartjes Ninove taken leftover mined city_ninove CIK; Groepsopvang De Hartjes Tienen taken leftover mined city_tienen CIK\n"
)
if new_2458.count("\n")!=1 or new_2459.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2458.encode("utf-8"))
    f.write(new_2459.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2458", chk.count(b"rq_2458,"), "n2459", chk.count(b"rq_2459,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2458,2458,no,tick2458 leftover dual Soetkin 0443.641.970 Strong native PDF (omzet70 JUMP 1325536 commercial-only; 73 JUMP 5590556 all 733; 76A JUMP 6056; envelope 70/76A JUMP 7047286; bruto empty VOL; pnl DROP 699335; 9901 DROP 722007; equity JUMP 6276000; assets JUMP 8457267; debt JUMP 2181267; FTE 84.2 JUMP; kapitaalsubsidies DROP 1476725; destin691 empty; 791 empty; cash DROP 618230; geldbeleggingen empty; 11 VE leftover city_kortrijk CIK); leftover mined city_kortrijk CIK; NOT t Sloeberke remine; NOT H.Hart WZC remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes Ninove remine; NOT Hartjes Tienen remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT VKA no deposit-id; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; next every-10 is 2460; next rq_2459 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2458 - rq_2458 Soetkin (opbr JUMP 7.05m / omzet JUMP 1.33m commercial-only / 73 JUMP 5.59m / pnl DROP 699k / destin empty / Strong PDF)

- Unit: **rq_2458** leftover dual after **Kinderdagverblijf t Sloeberke Groenheuvel@2457**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. De Bolster 0861.680.989 still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. CAR Overleie 0454.250.505 still **YE2024**. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 0433.184.479 leftover city_leuven — CDN still **403** — not taken. AZ Sint-Maria 0467.967.491 leftover city_halle unused YE2025 NBB **2026-00299006** CDN still **403** skip. CAR Noorderkempen 0408.078.010 leftover city_wuustwezel YE2025 **2026-00145984** SCAN — not taken. De Linde Ronse 0778.279.401 leftover city_ronse still **YE2024** (Companyweb last balansjaar 2024; filed 14.08.2025) — not taken. Kinderlach 0450.275.186 leftover city_eeklo still **YE2024** (Companyweb last balansjaar 2024; filed 15.07.2025) — not taken. Villa Boempatat 0660.616.520 leftover city_gent **NOW YE2025** (Companyweb last balansjaar 2025; filed 13.08.2026) — not taken this tick (Soetkin locked first). Woon en Zorg H. Hart Kortrijk 0413.595.330 leftover city_kortrijk still **YE2024** — not taken. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. Jessa 0821.142.117 leftover city_hasselt hospital — no usable 2026pdf / hospital special schema — not taken. Mini-creches GO! Next 0896.468.060 leftover city_hasselt still **YE2024** (Companyweb last balansjaar 2024; filed 25.02.2026). Zo Groot Oostende 0818.420.771 leftover city_oostende still **YE2024** (Companyweb last balansjaar 2024; filed 17.03.2026). Familiehulp De Speelboom 0443.631.280 YE2025 unused but Brussels zetel 1210 — not taken (leftover-via-VE not enough per LOOP.md). Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Vrije Kinderdagverblijven Antwerpen 0433.480.132 leftover city_antwerpen unused YE2025 filed 29.06.2026 — no NBB deposit-id locked — not taken. Hebe Kenniscentrum 0451.789.772 leftover city_antwerpen kenniscentrum/training RSZ 85.592 — skip (VBJK-class). WZC OLVA 0430.977.136 leftover city_antwerpen already in entities tick2036 — do not remine. Kinderdagverblijf t Sloeberke Groenheuvel 0410.973.360 just mined — do not remine. DE GROENE VERTE WOON EN ZORG 0465.061.649 just mined — do not remine. De Vleugels 0431.408.290 leftover city_houthulst VAPH already mined — do not remine. Kinderdagverblijf De Pallieterkes 0418.538.865 just mined — do not remine. De Medemens Kinderdagverblijven 0893.678.915 just mined — do not remine. De Medemens parent 0428.692.191 already mined — do not remine. OKO & ZO 0862.154.608 just mined — do not remine. KINDEROPVANG De Harlekijntjes 0407.700.403 just mined — do not remine. Kinderdagverblijf De Hartjes Ninove 0446.391.327 just mined — do not remine. Groepsopvang De Hartjes Tienen 0441.374.348 just mined — do not remine. Familia 0461.401.779 just mined — do not remine. Peutertuinen GO Mariakerke 0410.221.116 just mined — do not remine. WZC Annuntiaten Heverlee **0895.366.220** already in entities — do not remine. Kinderkuren 0478.167.834 just mined — do not remine. Kinderdagverblijven Leuven 0413.321.255 absorbed into Zorg Leuven — skip. t Bremhuisje 0445.265.533 stopgezet 07.10.1993 — skip. De Knuffelboom XL 0478.310.859 leftover city_gent UZ-CIK — NBB Consult no results skip. De Zeppelin 0454.001.867 leftover city_gent CIK — no jaarrekening skip. Kobe & Nanou is Stad Gent skip. KDV De Regenboog 0671.670.560 leftover city_gent is **BV private** skip. Groep Zorg H. Familie already in entities skip. Sint-Rafaël 0410.549.332 leftover city_gent VAPH — no jaarrekening skip. Vormingscentrum leftover city_gent training — not taken. VBJK leftover city_gent training/innovation — not taken. Helan Kinderopvang Helan-HH-adjacent — not taken. Re-HEAD YE2024 leftovers: Kinderlach still YE2024; De Linde Ronse still YE2024; Mini-creches GO Next still YE2024; Zo Groot Oostende still YE2024; Soetkin FLIPPED YE2025. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Soetkin** YE2025 (KBO **0443.641.970**; zetel Budastraat 30 8500 Kortrijk; **Actief** **11 VE** incl. **2.150.779.020** Soetkin Dam 8a 8500 Kortrijk since 03.01.2006 + **2.169.188.927** de bolliezzz Bissegem + **2.169.189.224** t hoogappeltje + **2.250.863.422** Kinderclub H. Hart; RSZ2025 **88.911**; Kinderopvang Vlaamse Gemeenschap since 01.04.2014; leftover of mined **city_kortrijk**; DIRECTIE@H-HART.BE). Identity trap: Soetkin 0443.641.970 ≠ Kinderdagverblijf t Sloeberke Groenheuvel **0410.973.360** leftover city_kortrijk CIK just mined; ≠ Woon en Zorg H. Hart Kortrijk **0413.595.330** leftover city_kortrijk WZC still YE2024 (same zorggroep website different KBO); ≠ DE GROENE VERTE WOON EN ZORG **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ Kinderdagverblijf De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ KINDEROPVANG De Harlekijntjes **0407.700.403**; ≠ Kinderdagverblijf De Hartjes Ninove **0446.391.327**; ≠ Groepsopvang De Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ BKO GENK-OOST **0475.432.830**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Speelhuis Elief **0451.624.377** CDN 403; ≠ Vrije Kinderdagverblijven Antwerpen **0433.480.132** no deposit-id; ≠ Hebe **0451.789.772** training; ≠ WZC OLVA **0430.977.136** already in entities; ≠ De Pagadder **0888.028.268**; ≠ WZC De Ruyschaert **0434.996.993**; ≠ Quattro **0555.667.072**; ≠ De Braamrakkertjes **0412.700.653** absorbed 31.03.2026 after YE2025; ≠ Idefix **0453.819.349** absorbed 31.03.2026 after YE2025; ≠ TKDV Het Veer Kloosterstraat 6. 11 VE — leftover of mined city_kortrijk (zetel + 4/11 VE Kortrijk). Confirmed leftover public (Opgroeien CIK groepsopvang; Kind en Gezin-vergunde; Zorggroep H.Hart kinderopvang VZW) not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not t Sloeberke remine. VOL-VZW **native text** (not scan) — 98887 B / 37p all native euros (VOL-VZW 6.1 / 6.2.1 / 6.2.2 / 6.2.3 / 6.2.4 / 6.3.4 / 6.3.5 / 6.4.2 / 6.5.2 / 6.6 / 6.10 / 6.16 / 7 / 8 niet dienstig).
- Found: official NBB VOL-VZW native PDF deposit **2026-00270287** (98887 B / 37p; AV **31.03.2026**; header **07.07.2026**; CDN Last-Modified **29.07.2026**; CreationDate 09.07.2026 OpenPDF 1.3.26; all 37p native; prior-year identical not restated) — omzet 70 **EUR1325536** JUMP +7.70% (commercial-only vs large 73; 6.9 omzet-uitsplitsing empty); 73 **EUR5590556** JUMP +4.80% (all 733); 76A **EUR6056** JUMP; envelope 70/76A **EUR7047286** JUMP +5.55%; bruto 9900 **empty** (VOL); 62 **EUR4990506** JUMP +8.37%; 630 **EUR283214** DROP −0.49%; 66A **EUR3500** JUMP; 640/8 **EUR14955** JUMP; bedrijfswinst 9901 **EUR722007** DROP −5.81%; pnl 9904 **EUR699335** DROP −5.72%; equity **EUR6276000** JUMP +10.99%; assets **EUR8457267** JUMP +8.41%; debt **EUR2181267** JUMP +1.62%; FTE **84.2** JUMP +8.23% (was 77.8; 9087 84.2; 105 84.5); kapitaalsubsidies **EUR1476725** DROP −5.02%; destin 691 **empty** FLAT (destin empty vs pnl 699335); 791 **empty**; cash **EUR618230** DROP −17.18%; geldbeleggingen **empty**; gebouwen **EUR4651258** DROP; MVA 22/27 **EUR4758640** DROP; aanbouw **EUR3394** JUMP; capex **EUR58008**; fondsen 10 **EUR611950** FLAT; overgedragen 14 **EUR4187325** JUMP; bestemde fondsen 13 **empty**; voorzieningen 16 **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 11 VE leftover mined city_kortrijk CIK. NOT Kloosterstraat 6 Drongen. NOT t Sloeberke remine. NOT H.Hart WZC remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT KINDEROPVANG De Harlekijntjes remine. NOT Kinderdagverblijf De Hartjes Ninove remine. NOT Groepsopvang De Hartjes Tienen remine. NOT De Wissel remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT VKA no deposit-id. NOT Hebe training. NOT WZC OLVA remine.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.23); entities (+1 vzw_soetkin_kortrijk); foi + draft `gap_soetkin_opgroeien_matrix_opbr_7_05m_omzet_1_33m_73_5_59m_pnl_drop_699k_destin_empty_l5`; rq_2458=done + rq_2459 open; loop_state ticks=2458; raw tick2458/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2460**). Next: rq_2459 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT Soetkin remine / NOT Kinderdagverblijf t Sloeberke remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT Kinderdagverblijf De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT KINDEROPVANG De Harlekijntjes remine / NOT Kinderdagverblijf De Hartjes Ninove remine / NOT Groepsopvang De Hartjes Tienen remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT COB Annuntiaten remine / NOT WZC Annuntiaten remine / NOT Kinderkuren / NOT t Zonnetje / NOT Wigwam / NOT Jeugdhulp Don Bosco / NOT t Anemoontje / NOT De Hummeltjes / NOT De Ukkies / NOT De Slabbertjes / NOT De Wissel / NOT Monte Rosa / NOT Avida / NOT IZW / NOT Ferm Kinderopvang / NOT Kinderdagverblijven Leuven absorbed / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine). NOW leftover candidate: Villa Boempatat 0660.616.520 leftover city_gent **NOW YE2025** filed 13.08.2026 — take ONLY if unused + official NBB/CDN YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Vrije Kinderdagverblijven Antwerpen 0433.480.132 leftover city_antwerpen unused YE2025 filed 29.06.2026 — take ONLY if unused + official NBB/CDN YE2025 PDF. Kinderlach 0450.275.186 leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse 0778.279.401 leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa 0821.142.117 leftover city_hasselt hospital — take ONLY if unused + official YE2025 euros extract. Familiehulp De Speelboom 0443.631.280 YE2025 Brussels zetel — leftover of mined parent Familiehulp + Flanders VEs Oostende/Aalst only if LOOP.md leftover-via-VE is enough. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — only if leftover training of mined parent is in LOOP.md priority. VBJK leftover city_gent training/innovation — skip unless leftover training of mined parent is in LOOP.md priority. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2460** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
