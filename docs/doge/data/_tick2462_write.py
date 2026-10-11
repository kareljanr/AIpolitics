from pathlib import Path
import csv
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2462_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_overleie_jr2025_nbb_pdf_2462"
SRC_KBO="src_overleie_kbo_2462"
SRC_SBM="src_overleie_sbm_2462"
SRC_SITE="src_overleie_site_2462"
EID="vzw_car_overleie"
GAP="gap_overleie_riziv_vl_matrix_73_688m_vs_bruto_6_41m_pnl_destin_jump_318k_l5"
COMM="comm_overleie_jr2025_statutory_73_688m_vs_bruto_6_41m_pnl_jump_318k"
LB="lb_overleie_73_688m_vs_bruto_6_41m_pnl_destin_jump_318k_jr2025"
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
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 CAR Overleie deposit 2026-00330137,http://cdn.staatsbladmonitor.be/2026pdf/2026-00330137.pdf,NBB official WVV deposit PDF,{DAY},budget,tick2462; official native PDF 47611 bytes 12p VKT-VZW 26.0.15 m04-f; header 23.07.2026; AV 22.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-25 01:36:23 UTC OpenPDF 1.3.26; all 12p native; CDN 2026-00330137 HEAD 200 Last-Modified 05.08.2026; VKT-VZW 6.1.1 6.1.3 6.3 6.5 6.6 7 8 niet dienstig; prior-year identical not restated; euros from native PDF text not SBM table not Companyweb not Belscope not Busibee; official printed 73 is 687976485",
f"{SRC_KBO},KBO Centrum voor Ambulante Revalidatie Overleie 0454.250.505,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0454250505,KBO Public Search FOD Economie,{DAY},official_register,tick2462; Actief; 1 VE 2.156.450.649 Revalidatiecentrum Overleie Overleiestraat 57 8500 Kortrijk since 05.10.2006; VZW since 01.12.1994; begindatum 01.12.1994; zetel Overleiestraat 57 8500 Kortrijk since 01.12.1994; Werkgever RSZ since 09.01.1995; RSZ2025 86.101; BTW since 01.07.2020; FOI info@rcoverleie.be; leftover mined city_kortrijk CAR; NOT CAR Accent 0413.208.122 remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT Gesticht remine; NOT Kloosterstraat 6",
f"{SRC_SBM},NBB Consult / SBM fiche CAR Overleie 0454250505 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0454250505,NBB Consult / SBM,{DAY},official_register,tick2462; deposit-id 2026-00330137 YE 01.01.2025-31.12.2025 filing 23.07.2026 published 25.07.2026 VKT-VZW Verkort Initial; used for deposit-id discovery only; euros NOT taken from SBM HTML table",
f"{SRC_SITE},CAR Overleie FOI contact leftover city_kortrijk CAR,https://www.rcoverleie.be/,VZW Centrum voor Ambulante Revalidatie Overleie leftover city_kortrijk CAR RIZIV-VL ambulante revalidatie,{DAY},foi_contact,tick2462; FOI info@rcoverleie.be; zetel Overleiestraat 57 8500 Kortrijk; 1 VE leftover mined city_kortrijk after Gesticht different-city skip; NOT Kloosterstraat 6 Drongen; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat SCAN/CDN403; NOT Elief CDN 403; NOT Hebe training; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Centrum voor Ambulante Revalidatie Overleie,ASBL Centre de revalidation ambulatoire Overleie,CAR Overleie VZW (leftover city_kortrijk CAR),parastatal,city_kortrijk,nl,https://www.rcoverleie.be/,info@rcoverleie.be,Overleiestraat 57 8500 Kortrijk,tick2462 YE2025 Strong official native NBB PDF deposit 2026-00330137 + Strong KBO 0454.250.505 Actief 1 VE RSZ2025 86.101; omzet70 JUMP 257050 commercial-only; 73 JUMP 687976485 official printed (104x vs prior 6606860 and vs bruto 6412822 FOI glitch); 76A empty; envelope 70/76A JUMP 688233535; bruto JUMP 6412822 VKT present; pnl JUMP 318445; 9901 JUMP 306807; equity JUMP 5139546; assets JUMP 6246702; debt JUMP 1107157; FTE 69.6 JUMP; kapitaalsubsidies DROP 238795; destin691 JUMP 318445; 791 empty; cash DROP 310888; geldbeleggingen DROP 3192280; leftover mined city_kortrijk after Gesticht different-city skip; 1 VE CAR not convent not private; NOT Kloosterstraat 6 Drongen; NOT Gesticht 0410.918.031 remine; NOT HOCUS-POCUS 0466.893.167 remine; NOT VKA 0433.480.132 remine; NOT Soetkin 0443.641.970 remine; NOT t Sloeberke 0410.973.360 remine; NOT CAR Accent 0413.208.122 remine; NOT H.Hart WZC 0413.595.330; NOT Zonnebloem 0421.039.386 remine; NOT De Groene Verte 0465.061.649 remine; NOT De Vleugels 0431.408.290 remine; NOT De Pallieterkes 0418.538.865 remine; NOT De Medemens KDV 0893.678.915 remine; NOT De Medemens parent 0428.692.191 remine; NOT OKO & ZO 0862.154.608 remine; NOT Harlekijntjes 0407.700.403 remine; NOT Hartjes Ninove 0446.391.327 remine; NOT Hartjes Tienen 0441.374.348 remine; NOT De Wissel 0421.913.376 remine; NOT Familia 0461.401.779; NOT Peutertuinen GO Mariakerke 0410.221.116; NOT Mini-creches GO Next 0896.468.060 leftover city_hasselt YE2024; NOT Kinderlach 0450.275.186; NOT Helan; NOT De Speelboom Brussels; NOT Villa Boempatat 0660.616.520 leftover city_gent YE2025 SCAN/CDN403 2026-00396513; NOT Elief 0451.624.377 CDN 403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster 0861.680.989 YE2025 zetel Zwalm city_zwalm not mined; NOT GERUST 0776.808.068 zorgcentrale; NOT Jessa hospital special schema; AGB/FARO/Gandae YE2024; Antenne 3000 CDN 403; AZ Sint-Maria SCAN; Noorderkempen scan not taken; De Linde Ronse YE2024 not taken; Kinderlach YE2024 not taken; Zo Groot Oostende YE2024 not taken; H.Hart Kortrijk YE2024 not taken; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_overleie_omzet_jr2025_statutory,{EID},2025,257050,257050,257050,NBB VKT-VZW code 70 omzet YE2025 JUMP +26.86% (commercial-only vs printed 73 687976485; envelope is 70/76A),{SRC_PDF},strong,tick2462; PDF p5 native; YE2024 identical 202624; 73 official printed 687976485 JUMP",
f"bud_overleie_73_jr2025_statutory,{EID},2025,687976485,687976485,687976485,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 JUMP +10311.31% (official PDF text+glyph 687.976.485; 104x vs prior 6606860 and vs bruto 6412822 FOI filing-glitch),{SRC_PDF},strong,tick2462; PDF p5 native; YE2024 identical 6606860; FOI RIZIV-VL split + why 73 printed 688m",
f"bud_overleie_opbr_jr2025_statutory,{EID},2025,688233535,688233535,688233535,NBB VKT-VZW envelope 70/76A YE2025 JUMP +10008.05% (omzet 257050 commercial-only + official printed 73 687976485 + 76A empty),{SRC_PDF},strong,tick2462; PDF p5 native; YE2024 identical 6809484; bruto 9900 also 6412822 VKT present but envelope is 70/76A because omzet not empty",
f"bud_overleie_bruto_jr2025_statutory,{EID},2025,6412822,6412822,6412822,NBB VKT-VZW code 9900 brutomarge YE2025 JUMP +3.01% (VKT present; envelope remains 70/76A because omzet not empty),{SRC_PDF},strong,tick2462; PDF p5 native; YE2024 identical 6225355; 76A empty; 73 printed 688m vs bruto 6.41m FOI",
f"bud_overleie_pnl_jr2025_statutory,{EID},2025,318445,318445,318445,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 JUMP +37.49% (was 231605),{SRC_PDF},strong,tick2462; PDF p5 native; YE2024 identical 231605; bedrijfswinst 9901 306807 JUMP; destin691 318445 JUMP full pnl to fonds gebouwen",
f"bud_overleie_bedrijfswinst_jr2025_statutory,{EID},2025,306807,306807,306807,NBB VKT-VZW code 9901 bedrijfswinst YE2025 JUMP +43.01% (was 214532),{SRC_PDF},strong,tick2462; PDF p5 native; YE2024 identical 214532; 62 6142612 JUMP; 630 50477 DROP; 66A empty",
f"bud_overleie_equity_jr2025_statutory,{EID},2025,5139546,5139546,5139546,NBB VKT-VZW code 10/15 eigen vermogen YE2025 JUMP +6.01%,{SRC_PDF},strong,tick2462; PDF p4 native; YE2024 identical 4848114; kapitaalsubsidies 238795 DROP; overgedragen 14 empty; fondsen 10 empty; bestemde fondsen 13 4900751 JUMP",
f"bud_overleie_assets_jr2025_statutory,{EID},2025,6246702,6246702,6246702,NBB VKT-VZW code 20/58 totaal activa YE2025 JUMP +4.18%,{SRC_PDF},strong,tick2462; PDF p3 native; YE2024 identical 5995945; MVA 22/27 676632 DROP; cash 310888 DROP; geldbeleggingen 3192280 DROP; aanbouw 27 empty",
f"bud_overleie_debt_jr2025_statutory,{EID},2025,1107157,1107157,1107157,NBB VKT-VZW code 17/49 schulden YE2025 JUMP +4.91%,{SRC_PDF},strong,tick2462; PDF p4 native; YE2024 identical 1055370; 17 empty; 42/48 1084684 JUMP",
f"bud_overleie_cash_jr2025_statutory,{EID},2025,310888,310888,310888,NBB VKT-VZW code 54/58 liquide middelen YE2025 DROP -31.43%,{SRC_PDF},strong,tick2462; PDF p3 native; YE2024 identical 453358; geldbeleggingen 50/53 3192280 DROP",
f"bud_overleie_destin_jr2025_statutory,{EID},2025,318445,318445,318445,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 JUMP +37.49% (full pnl 318445 to fonds gebouwen; 13 JUMP 4900751),{SRC_PDF},strong,tick2462; PDF p6 native; YE2024 destin 231605; bestemde fondsen 13 4900751 JUMP FOI",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":257050,\"\"2025_73\"\":687976485,\"\"2025_76A\"\":0,"
"\"\"2025_opbr70_76A\"\":688233535,\"\"2025_bruto\"\":6412822,"
"\"\"2025_pnl\"\":318445,\"\"2025_bedrijfswinst\"\":306807,"
"\"\"2025_equity\"\":5139546,\"\"2025_assets\"\":6246702,\"\"2025_debt\"\":1107157,"
"\"\"2025_fte\"\":69.6,\"\"2025_kapitaalsubsidies\"\":238795,\"\"2025_destin691\"\":318445,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":310888,\"\"2025_geldbeleggingen\"\":3192280,"
"\"\"2025_personnel62\"\":6142612,\"\"2025_gebouwen22\"\":638645,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":4900751,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":50477,\"\"2025_capex\"\":0,"
"\"\"2024_omzet\"\":202624,\"\"2024_73\"\":6606860,"
"\"\"2024_opbr70_76A\"\":6809484,\"\"2024_bruto\"\":6225355,\"\"2024_pnl\"\":231605,\"\"2024_bedrijfswinst\"\":214532,"
"\"\"2024_equity\"\":4848114,\"\"2024_assets\"\":5995945,"
"\"\"2024_debt\"\":1055370,\"\"2024_cash\"\":453358,\"\"2024_fte\"\":68.7,"
"\"\"2024_destin691\"\":231605,\"\"2024_kapitaalsubsidies\"\":265808,\"\"2024_76A\"\":0,"
"\"\"2024_geldbeleggingen\"\":3467850}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},CAR Overleie YE2025 (73 JUMP 688m vs bruto 6.41m / omzet 257k commercial-only / pnl JUMP 318k / destin JUMP 318k / Strong PDF),{EID},RIZIV-VL + leftover city_kortrijk CAR,VZW Centrum voor Ambulante Revalidatie Overleie (KBO 0454.250.505; Actief; 1 VE; RSZ2025 86.101; zetel + 1/1 VE Kortrijk),2026-06-22,2025,2025,688233535,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00330137.pdf,Public CAR dual of mined city_kortrijk,Publish RIZIV-VL matrix behind printed 73 688m + why 73 688m vs bruto 6.41m and prior 6.61m + why pnl JUMP 318k while destin JUMP 318k and cash DROP 311k and FTE 69.6,{SRC_PDF},strong,Vlaanderen>West-Vlaanderen>Kortrijk>CAROverleie>JR2025_statutory_L5,tick2462; Strong official native PDF; leftover mined city_kortrijk CAR; 1 VE; official printed 73 687976485 recorded as-is; NOT every-10; NOT Kloosterstraat 6 Drongen; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"CAR Overleie 73 JUMP 688m vs bruto 6.41m / omzet 257k commercial-only / pnl JUMP 318k / destin JUMP 318k (YE2025 leftover city_kortrijk CAR)",
"L5",
"car_vzw_statutory",
"Vlaanderen>West-Vlaanderen>Kortrijk>CAROverleie>JR2025",
"688233535",
"688233535",
"PDF 70/76A 688233535 envelope; omzet 257050 commercial-only; official printed 73 687976485 (104x vs prior 6606860 and vs bruto 6412822 FOI glitch); 76A empty; bruto JUMP 6412822 VKT present; bedrijfswinst JUMP 306807; pnl JUMP 318445; equity JUMP 5139546; assets JUMP 6246702; debt JUMP 1107157; FTE 69.6 JUMP; kapitaalsubsidies DROP 238795; destin691 JUMP 318445; cash DROP 310888; geldbeleggingen DROP 3192280; 1 VE leftover city_kortrijk CAR",
"strong",
SRC_PDF,
"RIZIV-VL + leftover city_kortrijk CAR",
"CAR / Vlaamse tweede-lijn GGZ leftover city_kortrijk",
"688m printed 73 envelope; omzet 257k commercial-only vs printed 73 688m; pnl JUMP 318k; destin JUMP 318k; cash DROP 311k; leftover city_kortrijk CAR",
"5.45",
"5.40",
"5.00",
"5.36",
"FOI RIZIV-VL matrix behind printed 73 688m + why 73 688m vs bruto 6.41m and prior 6.61m + why pnl JUMP 318k while destin JUMP 318k and cash DROP 311k and FTE 69.6",
"active",
"",
"tick2462 leftover mined city_kortrijk CAR after Gesticht different-city skip; 1 VE; official printed 73 687976485 recorded as-is; NOT every-10; NOT Gesticht remine; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT Kinderlach YE2024; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT De Speelboom Brussels",
])
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>West-Vlaanderen>Kortrijk>CAROverleie>CAR",
"entity_id": EID,
"what_is_missing": "RIZIV-VL split behind printed 73 687976485 (omzet 70 257050 commercial-only + 73 687976485 + 76A empty) and why 73 printed 688m vs bruto 6412822 / prior 6606860 and why pnl JUMP 318445 while destin JUMP 318445 and cash DROP 310888 and FTE 69.6",
"why_it_matters": "Strong official PDF leftover public CAR of mined city_kortrijk; official printed 73 688m vs bruto 6.41m filing-glitch; public RIZIV-VL ambulante revalidatie",
"priority": "8",
"recipient_body": "VZW Centrum voor Ambulante Revalidatie Overleie / Raad van Bestuur",
"recipient_email": "info@rcoverleie.be",
"recipient_postal": "Overleiestraat 57 8500 Kortrijk",
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
"notes": "tick2462; ready NOT sent; Strong official native NBB PDF; leftover mined city_kortrijk CAR after Gesticht different-city skip; 1 VE; official printed 73 687976485 recorded as-is; NOT every-10; off Drongen",
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
if rq_raw.count(b"rq_2462,")!=1: raise SystemExit(f"bad 2462 count {rq_raw.count(b'rq_2462,')}")
if b"rq_2463," in rq_raw: raise SystemExit("2463 exists")
idx=rq_raw.rfind(b"rq_2462,")
if idx<0: raise SystemExit("rq_2462 not found")
new_2462=(
"rq_2462,leftover dual CAR Overleie YE2025,hole_fill,8,done,L5,vzw_car_overleie,"
"Took unused leftover public CAR Centrum voor Ambulante Revalidatie Overleie 0454.250.505 leftover mined city_kortrijk. Official NBB VKT-VZW YE2025 2026-00330137 native 12p. Envelope 70/76A JUMP 688233535; omzet JUMP 257050 commercial-only; official printed 73 JUMP 687976485 (104x vs prior/bruto FOI); pnl JUMP 318445; destin JUMP 318445. NOT Gesticht remine. NOT CAR Accent remine. NOT Soetkin remine.,"
f",{STAMP},{STAMP},tick2462 leftover mined city_kortrijk CAR; Strong native PDF; 1 VE; official printed 73 687976485 recorded as-is; next every-10 is 2470\n"
)
new_2463=(
"rq_2463,leftover dual after CAR Overleie — hunt unused public dual,hole_fill,8,open,L5,,"
"After CAR Overleie YE2025. Prefer AGB/FARO if YE2025 else unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Villa Boempatat 0660.616.520 leftover city_gent YE2025 2026-00396513 CDN 403 / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen YE2025 2026-00374905 CDN 403 — take ONLY if CDN 200 native. Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO! Next / Zo Groot Oostende still YE2024 — take ONLY if unused + official YE2025 PDF. De Bolster 0861.680.989 NOW YE2025 2026-00210039 zetel Zwalm (city_zwalm not mined) — take ONLY if leftover of a mined parent. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. NOT CAR Overleie remine. NOT Gesticht remine. NOT Grauwzusters convent. NOT Hocus-Pocus remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Helan. NOT Hebe training. NOT WZC OLVA remine. NOT De Speelboom Brussels. NOT GERUST zorgcentrale.,"
f",{STAMP},{STAMP},spawned after tick2462; CAR Overleie taken leftover mined city_kortrijk CAR; Gesticht taken leftover mined city_ieper CIK convent-class check PASSED; Hocus-Pocus taken leftover mined city_roeselare CIK; VKA taken leftover mined city_antwerpen CIK; Soetkin taken leftover mined city_kortrijk CIK; t Sloeberke taken leftover mined city_kortrijk CIK; De Groene Verte taken leftover mined city_houthulst WZC; next every-10 is 2470\n"
)
if new_2462.count("\n")!=1 or new_2463.count("\n")!=1: raise SystemExit("bad rq newlines")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2462.encode("utf-8"))
    f.write(new_2463.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2462", chk.count(b"rq_2462,"), "n2463", chk.count(b"rq_2463,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2462,2462,no,tick2462 leftover dual CAR Overleie 0454.250.505 Strong native PDF (omzet70 JUMP 257050 commercial-only; official printed 73 JUMP 687976485 104x vs prior/bruto FOI; 76A empty; envelope 70/76A JUMP 688233535; bruto JUMP 6412822 VKT present; pnl JUMP 318445; 9901 JUMP 306807; equity JUMP 5139546; assets JUMP 6246702; debt JUMP 1107157; FTE 69.6 JUMP; kapitaalsubsidies DROP 238795; destin691 JUMP 318445; 791 empty; cash DROP 310888; geldbeleggingen DROP 3192280; 1 VE leftover city_kortrijk CAR); leftover mined city_kortrijk CAR; NOT Gesticht remine; NOT Grauwzusters convent; NOT HOCUS-POCUS remine; NOT VKA remine; NOT Soetkin remine; NOT t Sloeberke remine; NOT CAR Accent remine; NOT De Groene Verte remine; NOT De Vleugels remine; NOT De Pallieterkes remine; NOT De Medemens KDV remine; NOT De Medemens parent remine; NOT OKO & ZO remine; NOT Harlekijntjes remine; NOT Hartjes remine; NOT Familia remine; NOT De Wissel remine; NOT Mini-creches GO Next remine; NOT Kinderlach; NOT De Speelboom Brussels; NOT Elief CDN 403; NOT Villa Boempatat SCAN/CDN403; NOT Hebe training; NOT WZC OLVA remine; NOT Quattro remine; NOT De Bolster Zwalm not leftover mined parent; NOT GERUST zorgcentrale; next every-10 is 2470; next rq_2463 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2462 - rq_2462 CAR Overleie (73 JUMP 688m vs bruto 6.41m / omzet 257k commercial-only / pnl JUMP 318k / destin JUMP 318k / Strong PDF)

- Unit: **rq_2462** leftover dual after **Gesticht@2461**. Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024** (not re-downloaded); FARO 2026-00010398 still **YE2024** (HEAD-only policy Last-Modified 21.01.2026; not re-downloaded); AIESH/Gandae/Aralea/Manupal/Vlotter still **YE2024**. Zeepreventorium still **YE2024**. Drongen named+unnamed CARs **exhausted** — left Kloosterstraat 6. Kohesi family **exhausted**. Quattro WZC members **exhausted** except already-in-entities St Jozef Zonnebeke / Sint-Vincentius Avelgem. CAR Antenne 3000 leftover city_leuven CDN still **403**. AZ Sint-Maria leftover city_halle YE2025 **2026-00299006** NBB PDF SCAN (Canon iR-ADV) — not taken. CAR Noorderkempen leftover city_wuustwezel still SCAN. De Linde Ronse leftover city_ronse still **YE2024** (filed 14.08.2025). Kinderlach leftover city_eeklo still **YE2024** (filed 15.07.2025). Villa Boempatat leftover city_gent **YE2025** **2026-00396513** NBB PDF 1.47MB / 9p **SCAN** no extractable euros (CDN still **403**) — not taken. Woon en Zorg H. Hart Kortrijk leftover city_kortrijk still **YE2024** (filed 26.06.2025). Jessa leftover city_hasselt hospital YE2025 PDF 4.3MB / hospital special schema — not taken (Overleie locked first). Mini-creches GO! Next leftover city_hasselt still **YE2024** (filed 25.02.2026). Zo Groot Oostende leftover city_oostende still **YE2024** (2026-00055086 is YE2024). Familiehulp De Speelboom YE2025 unused Brussels zetel — not taken. Speelhuis Elief leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — not taken. Hebe Kenniscentrum leftover city_antwerpen training — skip. WZC OLVA leftover city_antwerpen already in entities — do not remine. De Bolster 0861.680.989 **NOW YE2025** **2026-00210039** zetel Zwalm (city_zwalm not mined) — not taken. GERUST Zorgcentrale 0776.808.068 leftover city_herentals YE2025 **2026-00195429** — zorgcentrale not in dual types — not taken. Gesticht 0410.918.031 just mined — do not remine. HOCUS-POCUS just mined — do not remine. VKA just mined — do not remine. Soetkin just mined — do not remine. t Sloeberke just mined — do not remine. De Groene Verte just mined — do not remine. De Vleugels already mined — do not remine. De Pallieterkes just mined — do not remine. De Medemens Kinderdagverblijven just mined — do not remine. De Medemens parent already mined — do not remine. CAR Accent already mined — do not remine. Grauwzusters Franciscanessen Hasselt 0409.771.748 leftover city_hasselt convent skip. Zwarte Zusters Oudenaarde 0413.272.260 convent 0 VE skip. First leftover unused + live official YE2025 native euros: took FREE leftover Flemish **VZW Centrum voor Ambulante Revalidatie Overleie / CAR Overleie** YE2025 (KBO **0454.250.505**; zetel Overleiestraat 57 8500 Kortrijk; **Actief** **1 VE** **2.156.450.649** Revalidatiecentrum Overleie Overleiestraat 57 since 05.10.2006; RSZ2025 **86.101**; leftover of mined **city_kortrijk**; info@rcoverleie.be). Identity trap: CAR Overleie 0454.250.505 ≠ CAR Accent **0413.208.122** leftover city_kortrijk already mined; ≠ Soetkin **0443.641.970**; ≠ t Sloeberke **0410.973.360**; ≠ H.Hart Kortrijk **0413.595.330**; ≠ Zonnebloem **0421.039.386**; ≠ Gesticht **0410.918.031** leftover city_ieper just mined; ≠ HOCUS-POCUS **0466.893.167**; ≠ VKA **0433.480.132**; ≠ Speelhuis Elief **0451.624.377**; ≠ Villa Boempatat **0660.616.520**; ≠ De Groene Verte **0465.061.649**; ≠ De Vleugels **0431.408.290**; ≠ De Pallieterkes **0418.538.865**; ≠ De Medemens Kinderdagverblijven **0893.678.915**; ≠ De Medemens **0428.692.191**; ≠ OKO & ZO **0862.154.608**; ≠ Harlekijntjes **0407.700.403**; ≠ Hartjes Ninove **0446.391.327**; ≠ Hartjes Tienen **0441.374.348**; ≠ De Wissel **0421.913.376**; ≠ Ferm Kinderopvang **0416.117.627**; ≠ Familia **0461.401.779**; ≠ Peutertuinen GO Mariakerke **0410.221.116**; ≠ Mini-crèches GO! Next **0896.468.060**; ≠ Kinderlach **0450.275.186**; ≠ Helan 0464.151.037; ≠ Hebe **0451.789.772**; ≠ WZC OLVA **0430.977.136**; ≠ De Linde Ronse **0778.279.401**; ≠ De Bolster **0861.680.989**; ≠ GERUST **0776.808.068**; ≠ Jessa **0821.142.117**; ≠ AZ Sint-Maria **0467.967.491**; ≠ TKDV Het Veer Kloosterstraat 6. 1 VE Kortrijk — leftover of mined city_kortrijk (zetel + 1/1 VE). Confirmed leftover public (CAR / Vlaamse tweede-lijn GGZ; RIZIV-VL ambulante revalidatie) not convent / not private clinic / not school / not OVBJ / not WZC / not VAPH / not Ferm / not Gesticht remine / not CAR Accent remine. VKT-VZW **native text** (not scan) — 47611 B / 12p all native euros (VKT-VZW 6.1.1 / 6.1.3 / 6.3 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00330137** (47611 B / 12p; AV **22.06.2026**; header **23.07.2026**; CDN Last-Modified **05.08.2026**; CreationDate 25.07.2026 OpenPDF 1.3.26; all 12p native; prior-year identical not restated) — omzet 70 **EUR257050** JUMP +26.86% (commercial-only vs printed 73; was 202624); 73 **EUR687976485** JUMP +10311.31% (official PDF text+glyph **687.976.485**; was 6606860; 104x vs prior and vs bruto 6412822 — FOI filing-glitch; recorded as-is never invented); 76A **empty**; envelope 70/76A **EUR688233535** JUMP +10008.05%; bruto 9900 **EUR6412822** JUMP +3.01% (VKT present; envelope remains 70/76A because omzet not empty); 62 **EUR6142612** JUMP +2.78%; 630 **EUR50477** DROP −13.64%; 66A **empty**; 640/8 **EUR5387** JUMP +52.26%; 635/9 **EUR-92461**; bedrijfswinst 9901 **EUR306807** JUMP +43.01%; pnl 9904 **EUR318445** JUMP +37.49%; equity **EUR5139546** JUMP +6.01%; assets **EUR6246702** JUMP +4.18%; debt **EUR1107157** JUMP +4.91%; FTE **69.6** JUMP +1.31% (was 68.7; 9087 69.6; 105 70.5); kapitaalsubsidies **EUR238795** DROP −10.16%; destin 691 **EUR318445** JUMP +37.49% (full pnl to fonds gebouwen; 13 JUMP 4900751); 791 **empty**; cash **EUR310888** DROP −31.43%; geldbeleggingen **EUR3192280** DROP −7.95%; gebouwen **EUR638645** DROP; MVA 22/27 **EUR676632** DROP; aanbouw **empty**; capex **empty**; fondsen 10 **empty**; overgedragen 14 **empty**; bestemde fondsen 13 **EUR4900751** JUMP; voorzieningen 16 **empty** DROP (was 92461). Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_kortrijk CAR. NOT Kloosterstraat 6 Drongen. NOT Gesticht remine. NOT Grauwzusters convent. NOT HOCUS-POCUS remine. NOT VKA remine. NOT Soetkin remine. NOT t Sloeberke remine. NOT CAR Accent remine. NOT De Groene Verte remine. NOT De Vleugels remine. NOT De Pallieterkes remine. NOT De Medemens remine. NOT OKO & ZO remine. NOT Harlekijntjes remine. NOT Hartjes remine. NOT Familia remine. NOT Mini-creches GO Next Hasselt. NOT Kinderlach. NOT Helan. NOT De Speelboom Brussels. NOT Elief CDN 403. NOT Villa Boempatat SCAN/CDN403. NOT Hebe training. NOT WZC OLVA remine. NOT De Bolster Zwalm. NOT GERUST zorgcentrale.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.36); entities (+1 vzw_car_overleie); foi + draft `gap_overleie_riziv_vl_matrix_73_688m_vs_bruto_6_41m_pnl_destin_jump_318k_l5`; rq_2462=done + rq_2463 open; loop_state ticks=2462; raw tick2462/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2470**). Next: rq_2463 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT CAR Overleie remine / NOT Gesticht remine / NOT Grauwzusters convent / NOT HOCUS-POCUS remine / NOT VKA remine / NOT Soetkin remine / NOT t Sloeberke remine / NOT CAR Accent remine / NOT De Groene Verte remine / NOT De Vleugels remine / NOT De Pallieterkes remine / NOT De Medemens Kinderdagverblijven remine / NOT De Medemens parent remine / NOT OKO & ZO remine / NOT Harlekijntjes remine / NOT Hartjes remine / NOT Familia remine / NOT BKO GENK-OOST remine / NOT Peutertuinen GO Mariakerke remine / NOT Mini-creches GO Next remine / NOT WZC OLVA remine / NOT Hebe training / NOT Quattro remine / NOT GERUST zorgcentrale). NOW leftover candidate: Villa Boempatat 0660.616.520 leftover city_gent YE2025 **2026-00396513** CDN **403** / SCAN — take ONLY if unused + official native-text YE2025 PDF. Speelhuis Elief 0451.624.377 leftover city_antwerpen unused YE2025 **2026-00374905** CDN **403** — take ONLY if unused + CDN 200 native YE2025 PDF. Kinderlach leftover city_eeklo still YE2024 — take ONLY if unused + official YE2025 PDF. De Linde Ronse leftover city_ronse still YE2024 — take ONLY if unused + official YE2025 PDF. H.Hart Kortrijk leftover city_kortrijk still YE2024 — take ONLY if unused + official YE2025 PDF. Jessa leftover city_hasselt hospital YE2025 PDF — take ONLY if unused + official YE2025 euros extract. De Bolster 0861.680.989 NOW YE2025 zetel Zwalm — leftover of mined parent only. Familiehulp De Speelboom YE2025 Brussels zetel — leftover-via-VE not enough per LOOP.md. Mini-creches GO! Next leftover city_hasselt still YE2024 — skip unless YE2025. Zo Groot Oostende leftover city_oostende still YE2024 — skip unless YE2025. Vormingscentrum leftover city_gent training — skip unless LOOP.md leftover training priority. VBJK leftover city_gent training — skip. Helan Kinderopvang Helan-HH-adjacent — skip. Hebe Kenniscentrum training — skip. Tick **2470** is next every-10.
"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
