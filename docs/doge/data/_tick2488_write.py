from pathlib import Path
import csv
from io import StringIO
ROOT=Path("/workspace/AIpolitics")
DATA=ROOT/"docs/doge/data"
STAMP,DAY=(DATA/"_tick2488_stamp.txt").read_text().strip().splitlines()
print("STAMP",STAMP)
SRC_PDF="src_kapoentjes_jr2025_nbb_pdf_2488"
SRC_KBO="src_kapoentjes_kbo_2488"
SRC_SBM="src_kapoentjes_sbm_2488"
SRC_SITE="src_kapoentjes_site_2488"
EID="vzw_kapoentjes_halle"
GAP="gap_kapoentjes_halle_opgroeien_matrix_bruto_808k_omzet73_empty_cash_jump_171k_equity_drop_145k_l5"
COMM="comm_kapoentjes_jr2025_statutory_bruto_808k_omzet73_empty_cash_jump_171k_equity_drop_145k"
LB="lb_kapoentjes_bruto_808k_omzet73_empty_cash_jump_171k_equity_drop_145k_jr2025"
assert (ROOT/f"docs/doge/foi/drafts/{GAP}.md").is_file()

def append_lines(path, lines):
    raw=path.read_bytes()
    if not raw.endswith(b"\n"): raise SystemExit(f"{path} no LF")
    with path.open("ab") as f:
        for line in lines:
            if not line.endswith("\n"): line=line+"\n"
            f.write(line.encode("utf-8"))
    print("appended",len(lines),"->",path.name)

NOTS=("NOT De Zonnewende 0735.627.214 remine tick2487; NOT WZC Sint-Vincentius Erpe-Mere 0422.620.585 YE2024 zetel Erpe-Mere no Ninove VE; NOT Sint Vincentius Tielt 0410.266.349 0 VE; NOT Hartjes Ninove 0446.391.327 remine; NOT CAR Halle Asse 0425.788.230 remine tick2398; NOT AZ Sint-Maria 0467.967.491 SCAN; NOT Sint-Augustinus Halle remine; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; NOT Kinderlach YE2024; NOT De Linde Ronse YE2024; NOT Molleke YE2024; NOT t Sas YE2024; NOT OpWeg YE2024")

append_lines(DATA/"sources.csv", [
f"{SRC_PDF},NBB VKT-VZW jaarrekening 2025 Kinderdagverblijf De Kapoentjes Halle deposit 2026-00238870,http://cdn.staatsbladmonitor.be/2026pdf/2026-00238870.pdf,NBB official WVV deposit PDF via CDN,{DAY},budget,tick2488; official native statutory PDF 58575 bytes 16p VKT-VZW 23.0.10 m04-f; header 30.06.2026; AV 15.06.2026; YE 01.01.2025-31.12.2025; CreationDate 2026-07-02 10:08:03 UTC OpenPDF 1.3.26; CDN Last-Modified 24.07.2026; statutory pages native; CDN 2026-00238870 GET 200 58575 MD5 f7b9cb1b9e0df60e05987414920ee385; official NBB UUID fed7f899-7448-11f1-ab7b-69c58403f3b5; VKT-VZW 6.1.3 6.2 6.5 6.6 7 8 niet dienstig; 6.1.1 6.1.2 6.3 6.4 6.7 6.8 present; prior-year identical not restated; euros from official NBB native PDF text not SBM table not Companyweb not Belscope not Busibee",
f"{SRC_KBO},KBO Kinderdagverblijf De Kapoentjes Halle 0821.882.483,https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0821882483,KBO Public Search FOD Economie,{DAY},official_register,tick2488; Actief; 1 VE 2.197.812.934 zetel Ziekenhuislaan 100 bus 2 1500 Halle since 01.04.2011; VZW since 30.12.2009; begindatum 30.12.2009; RSZ-werkgever RSZ2025 88.911 Kinderdagverblijven en creches; toelating Kinderopvang Vlaamse Gemeenschap since 01.04.2014; FOI info@dekapoentjes.be; leftover mined city_halle CIK; NOT Hartjes Ninove remine; NOT CAR Halle Asse remine; NOT AZ Sint-Maria SCAN; NOT De Zonnewende remine",
f"{SRC_SBM},NBB Consult / SBM fiche De Kapoentjes 0821882483 (deposit-id only),https://consult.cbso.nbb.be/consult-enterprise/0821882483,NBB Consult / SBM,{DAY},official_register,tick2488; deposit-id 2026-00238870 YE 01.01.2025-31.12.2025 filing VKT-VZW Verkort model vereniging Initial UUID fed7f899-7448-11f1-ab7b-69c58403f3b5; deposit-id discovery via NBB published-deposits OK euros NOT OK; used for deposit-id discovery only; euros NOT taken from SBM HTML table not Busibee not Companyweb not Belscope",
f"{SRC_SITE},De Kapoentjes Halle FOI contact leftover city_halle CIK,https://www.kinderopvanghalle.be/nl/de-kapoentjes,Kinderdagverblijf De Kapoentjes VZW leftover city_halle CIK 1 VE,{DAY},foi_contact,tick2488; FOI info@dekapoentjes.be; zetel Ziekenhuislaan 100 bus 2 1500 Halle; 40 plaatsen; leftover mined city_halle CIK after De Zonnewende lock; NOT Hartjes Ninove remine; NOT CAR Halle Asse remine; NOT AZ Sint-Maria SCAN; NOT De Zonnewende remine; NOT WZC Sint-Vincentius Erpe-Mere YE2024",
])
print("sources ok")

append_lines(DATA/"entities.csv", [
f"{EID},Kinderdagverblijf De Kapoentjes,ASBL Kinderdagverblijf De Kapoentjes,Kinderdagverblijf De Kapoentjes VZW (leftover city_halle CIK),parastatal,city_halle,nl,https://www.kinderopvanghalle.be/nl/de-kapoentjes,info@dekapoentjes.be,Ziekenhuislaan 100 bus 2 1500 Halle,tick2488 YE2025 Strong official native NBB PDF deposit 2026-00238870 + Strong KBO 0821.882.483 Actief 1 VE 2.197.812.934; omzet70 empty VKT; 73 empty VKT; 76A DROP 53681; envelope bruto 9900 JUMP 808125; pnl 9904 empty FLAT; 9901 DROP 7877; equity DROP 145227; assets DROP 644662; debt DROP 499435; FTE JUMP 10.6; kapitaalsubsidies DROP 145227; destin691 empty; 791 empty; cash JUMP 171212; geldbeleggingen empty; capex empty; leftover city_halle CIK 1 VE; prior-year identical; {NOTS}; not TE-additive",
])
append_lines(DATA/"budgets.csv", [
f"bud_kapoentjes_omzet_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 70 omzet YE2025 empty (VKT),{SRC_PDF},strong,tick2488; PDF p5 native; YE2024 empty; 73 empty; envelope bruto 9900 because omzet empty",
f"bud_kapoentjes_73_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 73 lidgeld schenkingen legaten en subsidies YE2025 empty (VKT),{SRC_PDF},strong,tick2488; PDF p5 native; YE2024 empty; FOI Opgroeien/Kind en Gezin/stad Halle matrix behind empty 73",
f"bud_kapoentjes_opbr_jr2025_statutory,{EID},2025,808125,808125,808125,NBB VKT-VZW envelope bruto 9900 YE2025 JUMP +6.65% (VKT envelope because omzet empty),{SRC_PDF},strong,tick2488; PDF p5 native; YE2024 757756; 70 empty; 73 empty; 76A DROP 53681",
f"bud_kapoentjes_76A_jr2025_statutory,{EID},2025,53681,53681,53681,NBB VKT-VZW code 76A niet-recurrente bedrijfsopbrengsten YE2025 DROP -32.06%,{SRC_PDF},strong,tick2488; PDF p5 native; YE2024 79007",
f"bud_kapoentjes_pnl_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 9904 winst van het boekjaar YE2025 empty FLAT (9903 208 / 67/77 208),{SRC_PDF},strong,tick2488; PDF p5 native; YE2024 also empty; bedrijfswinst 9901 7877 DROP",
f"bud_kapoentjes_bedrijfswinst_jr2025_statutory,{EID},2025,7877,7877,7877,NBB VKT-VZW code 9901 bedrijfswinst YE2025 DROP -11.05% (was 8856),{SRC_PDF},strong,tick2488; PDF p5 native; YE2024 8856; 62 741034 JUMP; 630 58772 FLAT; 66A 100 DROP; 640/8 342 JUMP; 635/9 empty; 631/4 empty",
f"bud_kapoentjes_equity_jr2025_statutory,{EID},2025,145227,145227,145227,NBB VKT-VZW code 10/15 eigen vermogen YE2025 DROP -15.79%,{SRC_PDF},strong,tick2488; PDF p4 native; YE2024 172457; kapitaalsubsidies 15 145227 DROP (entire equity); overgedragen 14 empty; fondsen 10 empty; bestemde fondsen 13 empty",
f"bud_kapoentjes_assets_jr2025_statutory,{EID},2025,644662,644662,644662,NBB VKT-VZW code 20/58 totaal activa YE2025 DROP -4.95%,{SRC_PDF},strong,tick2488; PDF p3 native; YE2024 678240; MVA 22/27 320236 DROP; cash 171212 JUMP; geldbeleggingen empty; aanbouw 27 empty; FVA 28 empty; LT recv 29 empty",
f"bud_kapoentjes_debt_jr2025_statutory,{EID},2025,499435,499435,499435,NBB VKT-VZW code 17/49 schulden YE2025 DROP -1.25%,{SRC_PDF},strong,tick2488; PDF p4 native; YE2024 505783; 17 346900 DROP; 42/48 152176 JUMP",
f"bud_kapoentjes_cash_jr2025_statutory,{EID},2025,171212,171212,171212,NBB VKT-VZW code 54/58 liquide middelen YE2025 JUMP +203.17%,{SRC_PDF},strong,tick2488; PDF p3 native; YE2024 56474; geldbeleggingen 50/53 empty; capex 8169 empty",
f"bud_kapoentjes_destin_jr2025_statutory,{EID},2025,0,0,0,NBB VKT-VZW code 691 toevoeging bestemde fondsen YE2025 empty (791 empty; 13 empty),{SRC_PDF},strong,tick2488; PDF p6 native; YE2024 destin empty; 791 empty; 14 empty; equity is entirely kapitaalsubsidies 15",
])
print("entities+budgets ok")

cash_json=(
"\"{\"\"2025_omzet\"\":0,\"\"2025_73\"\":0,\"\"2025_76A\"\":53681,"
"\"\"2025_opbr70\"\":0,\"\"2025_bruto9900\"\":808125,"
"\"\"2025_pnl\"\":0,\"\"2025_bedrijfswinst\"\":7877,"
"\"\"2025_equity\"\":145227,\"\"2025_assets\"\":644662,\"\"2025_debt\"\":499435,"
"\"\"2025_fte\"\":10.6,\"\"2025_kapitaalsubsidies\"\":145227,\"\"2025_destin691\"\":0,"
"\"\"2025_791\"\":0,\"\"2025_cash\"\":171212,\"\"2025_geldbeleggingen\"\":0,"
"\"\"2025_personnel62\"\":741034,\"\"2025_gebouwen22\"\":318159,"
"\"\"2025_aanbouw27\"\":0,\"\"2025_66A\"\":100,\"\"2025_66B\"\":0,"
"\"\"2025_fondsen10\"\":0,\"\"2025_overgedragen14\"\":0,"
"\"\"2025_bestemdefondsen13\"\":0,"
"\"\"2025_voorzieningen16\"\":0,\"\"2025_630\"\":58772,\"\"2025_capex\"\":0,"
"\"\"2025_ltrecv29\"\":0,\"\"2025_75\"\":33,\"\"2025_9903\"\":208,"
"\"\"2024_omzet\"\":0,\"\"2024_73\"\":0,"
"\"\"2024_opbr70\"\":0,\"\"2024_bruto9900\"\":757756,\"\"2024_pnl\"\":0,\"\"2024_bedrijfswinst\"\":8856,"
"\"\"2024_equity\"\":172457,\"\"2024_assets\"\":678240,"
"\"\"2024_debt\"\":505783,\"\"2024_cash\"\":56474,\"\"2024_fte\"\":9.8,"
"\"\"2024_destin691\"\":0,\"\"2024_kapitaalsubsidies\"\":172457,\"\"2024_76A\"\":79007,"
"\"\"2024_geldbeleggingen\"\":0}\""
)
append_lines(DATA/"commitments.csv", [
f"{COMM},De Kapoentjes YE2025 (bruto JUMP 808k / omzet+73 empty VKT / cash JUMP 171k / equity DROP 145k / Strong PDF),{EID},Opgroeien + leftover city_halle CIK,Kinderdagverblijf De Kapoentjes VZW (KBO 0821.882.483; Actief; 1 VE; zetel Halle),2026-06-15,2025,2025,808125,{cash_json},0,active,http://cdn.staatsbladmonitor.be/2026pdf/2026-00238870.pdf,Public CIK dual of mined city_halle,Publish Opgroeien / Kind en Gezin / stad Halle matrix behind envelope 808k and why omzet+73 empty VKT and why cash JUMP 171212 while equity DROP 145227,{SRC_PDF},strong,Vlaanderen>Vlaams-Brabant>Halle>De-Kapoentjes>JR2025_statutory_L5,tick2488; Strong official native PDF; leftover mined city_halle CIK; 1 VE; prior-year identical; NOT De Zonnewende remine; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Hartjes remine; NOT CAR Halle remine; not TE-additive",
])
print("commitments ok")

row = ",".join([
LB,
"De Kapoentjes bruto JUMP 808k / omzet+73 empty VKT / cash JUMP 171k / equity DROP 145k (YE2025 leftover city_halle CIK)",
"L5",
"cik_vzw_statutory",
"Vlaanderen>Vlaams-Brabant>Halle>De-Kapoentjes>JR2025",
"808125",
"808125",
"PDF envelope 808125 = bruto 9900 VKT because omzet empty; 70 empty; 73 empty; 76A DROP 53681; bedrijfswinst DROP 7877; pnl 9904 empty FLAT; equity DROP 145227; assets DROP 644662; debt DROP 499435; FTE 10.6; kapitaalsubsidies DROP 145227; destin691 empty; cash JUMP 171212; capex empty; leftover city_halle CIK",
"strong",
SRC_PDF,
"Opgroeien + leftover city_halle CIK",
"CIK leftover city_halle",
"808k envelope; cash JUMP 171k; equity DROP 145k; leftover city_halle CIK",
"5.22",
"4.72",
"5.00",
"5.08",
"FOI Opgroeien / Kind en Gezin / stad Halle matrix behind envelope bruto 808k + why omzet+73 empty VKT and why cash JUMP 171212 after YE2024 56474 while equity DROP 145227 (kapitaalsubsidies only) and pnl 9904 empty",
"active",
"",
"tick2488 leftover mined city_halle CIK after De Zonnewende lock; 1 VE; prior-year identical; NOT De Zonnewende remine; NOT WZC Sint-Vincentius Erpe-Mere YE2024; NOT Sint Vincentius 0 VE; NOT Hartjes remine; NOT CAR Halle remine; NOT AZ Sint-Maria SCAN; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine",
])
assert len(next(csv.reader(StringIO(row))))==21
append_lines(DATA/"leaderboard.csv", [row])
print("leaderboard ok")

foi_row={
"gap_id": GAP,
"hierarchy_path": "Vlaanderen>Vlaams-Brabant>Halle>De-Kapoentjes>CIK",
"entity_id": EID,
"what_is_missing": "Opgroeien / Kind en Gezin / stad Halle split behind envelope bruto 808125 (omzet 70 empty and 73 empty VKT vs 76A 53681) and why cash JUMP 171212 after YE2024 56474 while equity DROP 145227 (kapitaalsubsidies only) and pnl 9904 empty",
"why_it_matters": "Strong official PDF leftover public CIK of mined city_halle; VKT envelope 808k because omzet empty; public groepsopvang 1 VE Ziekenhuislaan 100; cash JUMP 171k / equity DROP 145k / 76A DROP 54k",
"priority": "8",
"recipient_body": "KINDERDAGVERBLIJF DE KAPOENTJES VZW / Raad van Bestuur",
"recipient_email": "info@dekapoentjes.be",
"recipient_postal": "Ziekenhuislaan 100 bus 2 1500 Halle",
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
"notes": "tick2488; ready NOT sent; Strong official native NBB PDF; leftover mined city_halle CIK after De Zonnewende lock; 1 VE; prior-year identical; off De Zonnewende remine; off WZC Sint-Vincentius Erpe-Mere YE2024; off Hartjes remine; off CAR Halle remine; off AZ Sint-Maria SCAN; off Armonea commercial; off Vulpia commercial; off Korian commercial",
}
foi_path=DATA/"foi_queue.csv"
raw=foi_path.read_bytes()
if not raw.endswith(b"\n"): raise SystemExit("foi_queue no LF")
with foi_path.open("a", newline="", encoding="utf-8") as f:
    w=csv.DictWriter(f, fieldnames=list(foi_row.keys()), extrasaction="raise", lineterminator="\n")
    w.writerow(foi_row)
print("foi_queue ok")
print("CORE APPEND DONE")

rq_path=DATA/"research_queue.csv"
rq_raw=rq_path.read_bytes()
if not rq_raw.endswith(b"\n"): raise SystemExit("rq no LF")
if b"\r\n" in rq_raw: raise SystemExit("CRLF")
if rq_raw.count(b"rq_2488,")!=1: raise SystemExit(f"bad 2488 count {rq_raw.count(b'rq_2488,')}")
if b"rq_2489," in rq_raw: raise SystemExit("2489 exists")
idx=rq_raw.rfind(b"rq_2488,")
if idx<0: raise SystemExit("rq_2488 not found")
new_2488=(
"rq_2488,leftover dual De Kapoentjes YE2025,hole_fill,8,done,L5,vzw_kapoentjes_halle,"
"Took unused leftover public CIK De Kapoentjes 0821.882.483 leftover mined city_halle. Official NBB VKT-VZW YE2025 2026-00238870 native statutory 16p 58.6kB. Envelope bruto 9900 JUMP 808125 (omzet+73 empty VKT); cash JUMP 171212; equity DROP 145227; 76A DROP 53681; FTE 10.6. FIRST WZC Sint-Vincentius Ninove = 0422.620.585 zetel Erpe-Mere YE2024 SKIP. NOT De Zonnewende remine. NOT Hartjes remine. NOT CAR Halle remine. NOT AZ Sint-Maria SCAN. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},tick2488 leftover mined city_halle CIK; Strong native PDF; 1 VE; prior-year identical; next every-10 is 2490\n"
)
new_2489=(
"rq_2489,leftover dual hunt after De Kapoentjes,hole_fill,8,open,L5,,"
"Unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf. Less-picked mined cities: dendermonde (Zonneschijn CIK taken; leftover VAPH/CAR) / geel (Augustientjes CIK taken; leftover VAPH/CAR) / herentals (Bremdael WZC taken; leftover VAPH/CAR; OpWeg YE2024) / eeklo (leftover WZC; Kinderlach YE2024) / halle (CAR + CIK De Kapoentjes taken; leftover WZC/VAPH still open) / kalmthout (leftover WZC/VAPH) / bornem (CAR taken; leftover WZC/VAPH) / puurs (maatwerk taken; leftover WZC/VAPH) / ronse (maatwerk + VAPH taken; De Linde WZC YE2024; GR.O.O.D. no JR) / vilvoorde / mol / zoersel / schilde / denderleeuw / knokke_heist (CAR+WZC+CIK taken) / waregem (VAPH taken) / schoten (VAPH taken) / lokeren (VAPH taken) / dilbeek (CIK+VAPH taken) / tremelo (VAPH taken) / tielt (CIK + WZC taken) / ninove (CIK taken; leftover WZC/VAPH still open — WZC Sint-Vincentius lead is Erpe-Mere YE2024). FIRST leftover unused WZC/VAPH/CAR/hospital/maatwerk of a mined Flanders city with official YE2025 native PDF. Molleke / t Sas / Kinderlach / De Linde Ronse / H.Hart Kortrijk / Mini-creches GO Next / Zo Groot / Aurora / Het Witte Huis / OpWeg still YE2024. Villa Boempatat YE2025 CDN 403 / SCAN. Speelhuis Elief CDN 403. Jessa hospital special schema. city_kapellen missing. NOT De Kapoentjes remine. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Hartjes remine. NOT CAR Halle remine. NOT AZ Sint-Maria SCAN. NOT Huize De Veuster remine. NOT Grijkoort remine. NOT GR.O.O.D. no JR. NOT Nektari remine. NOT Reva Ter Linde remine. NOT De Hagewinde remine. NOT BWP remine. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine.,"
f",{STAMP},{STAMP},spawned after tick2488 leftover city_halle CIK; De Kapoentjes taken leftover mined city_halle CIK; De Zonnewende taken leftover mined city_tielt WZC; next every-10 is 2490; this tick is NOT every-10\n"
)
if new_2488.count("\n")!=1 or new_2489.count("\n")!=1: raise SystemExit("bad rq newlines")
for label,line in [("2488",new_2488),("2489",new_2489)]:
    n=len(next(csv.reader(StringIO(line))))
    if n!=12: raise SystemExit(f"{label} fields {n} != 12")
before=len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2488.encode("utf-8"))
    f.write(new_2489.encode("utf-8"))
after=rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after-before)
chk=rq_path.read_bytes()
print("n2488", chk.count(b"rq_2488,"), "n2489", chk.count(b"rq_2489,"))
if chk[:idx]!=rq_raw[:idx]: raise SystemExit("prefix changed")
print("prefix intact")

state=DATA/"loop_state.csv"
state.write_text(
"state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
f"main,continuous,hole_fill,{STAMP},rq_2488,2488,no,tick2488 leftover dual De Kapoentjes 0821.882.483 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A DROP 53681; envelope bruto9900 JUMP 808125; pnl 9904 empty FLAT; 9901 DROP 7877; equity DROP 145227; assets DROP 644662; debt DROP 499435; FTE JUMP 10.6; kapitaalsubsidies DROP 145227; destin691 empty; 791 empty; cash JUMP 171212; geldbeleggingen empty; capex empty; 1 VE leftover city_halle CIK); leftover mined city_halle CIK; prior-year identical; FIRST WZC Sint-Vincentius Ninove = 0422.620.585 zetel Erpe-Mere YE2024 SKIP; NOT De Zonnewende remine; NOT Hartjes remine; NOT CAR Halle remine; NOT AZ Sint-Maria SCAN; NOT Huize De Veuster remine; NOT Grijkoort remine; NOT GR.O.O.D. no JR; NOT Nektari remine; NOT Reva Ter Linde remine; NOT De Hagewinde remine; NOT BWP remine; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT Evara remine; NOT Zorg-Saam remine; next every-10 is 2490; next rq_2489 leftover dual\n",
encoding="utf-8",
)
print("loop_state ok")

log=ROOT/"docs/doge/loop_log.md"
log_raw=log.read_bytes()
if not log_raw.endswith(b"\n"): raise SystemExit("loop_log no LF")
entry=f"""
### {STAMP} - tick 2488 - rq_2488 Kinderdagverblijf De Kapoentjes Halle (bruto JUMP 808k / omzet+73 empty VKT / cash JUMP 171k / equity DROP 145k / Strong PDF)

- Unit: **rq_2488** leftover dual after **De Zonnewende@2487**. NOT every-10 (next **2490**). Prefer NON-stall AGB/FARO YE2025: AGB Bornem still **JR2024**; FARO 2026-00010398 still **YE2024**. Discovery path: leftover **WZC / VAPH / CAR / hospital / maatwerk** (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city with official YE2025 native PDF. STOP leftover-note loop. FIRST: WZC Sint-Vincentius Ninove lead = official KBO **0422.620.585** zetel Aaigemdorp 68 9420 Erpe-Mere since 13.03.2001; **8 VE** (Erpe-Mere x2 / Evere / Sint-Lievens-Houtem / Ronse x2 / Sint-Pieters-Leeuw / Herent) — **no Ninove VE**; NBB last deposit **2025-00439448** period **2024-12-31** YE2024 — **SKIP** (not leftover city_ninove; still YE2024). Re-HEAD YE2024 leftovers still YE2024: Kinderlach / De Linde Ronse / H.Hart Kortrijk / Molleke / OpWeg / Aurora / Het Witte Huis / Zo Groot **2026-00055086** YE2024 / t Sas **2026-00050081** YE2024. Confirmed `city_halle` exists (mined; leftover CAR taken tick2398 — leftover CIK unused). FIRST leftover unused + live official YE2025 native euros: took FREE leftover Flemish **KINDERDAGVERBLIJF DE KAPOENTJES VZW** YE2025 (KBO **0821.882.483**; zetel Ziekenhuislaan 100 bus 2 1500 Halle; **Actief** **1 VE** **2.197.812.934** since 01.04.2011; RSZ2025 **88.911**; leftover of mined **city_halle**; info@dekapoentjes.be; Opgroeien groepsopvang; 40 plaatsen). Identity trap: 0821.882.483 ≠ Hartjes Ninove **0446.391.327** remine ≠ CAR Halle Asse **0425.788.230** remine ≠ AZ Sint-Maria **0467.967.491** SCAN ≠ De Zonnewende **0735.627.214** remine ≠ WZC Sint-Vincentius Erpe-Mere **0422.620.585** YE2024 ≠ Sint Vincentius Tielt **0410.266.349** 0 VE. 1 VE leftover of mined city_halle (zetel + VE Ziekenhuislaan 100 bus 2). Confirmed leftover public CIK not convent / not private / not WZC / not VAPH / not commercial NV. VKT-VZW **native text** (not scan) — 58575 B / 16p all native euros (VKT-VZW 6.1.3 / 6.2 / 6.5 / 6.6 / 7 / 8 niet dienstig).
- Found: official NBB VKT-VZW native PDF deposit **2026-00238870** (58575 B / 16p; AV **15.06.2026**; header **30.06.2026**; official NBB UUID fed7f899-7448-11f1-ab7b-69c58403f3b5; CDN GET **200** 58575 official NBB-generated OpenPDF 1.3.26 CreationDate 02.07.2026 Last-Modified 24.07.2026 MD5 f7b9cb1b9e0df60e05987414920ee385; all 16p native; prior-year identical not restated) — omzet 70 **empty** VKT; 73 **empty** VKT; 76A **EUR53681** DROP −32.06% (was 79007); envelope bruto 9900 **EUR808125** JUMP +6.65% (VKT because omzet empty; was 757756); 62 **EUR741034** JUMP +7.48%; 630 **EUR58772** FLAT; 66A **EUR100** DROP; 640/8 **EUR342** JUMP; 635/9 **empty**; 631/4 **empty**; bedrijfswinst 9901 **EUR7877** DROP −11.05% (was 8856); pnl 9904 **empty** FLAT (9903 208 / 67/77 208; YE2024 also empty); equity **EUR145227** DROP −15.79%; assets **EUR644662** DROP −4.95%; debt **EUR499435** DROP −1.25%; FTE **10.6** JUMP +8.16% (was 9.8; 100 10.6; 9087 10.6; 105 11.7); kapitaalsubsidies **EUR145227** DROP −15.79%; destin 691 **empty**; 791 **empty**; cash **EUR171212** JUMP +203.17%; geldbeleggingen **empty**; gebouwen **EUR318159** DROP; MVA 22/27 **EUR320236** DROP; aanbouw **empty**; capex **empty**. Strong KBO + Strong PDF (native all pages; not SBM table; not Companyweb euros). Site: 1 VE leftover mined city_halle CIK. NOT De Zonnewende remine. NOT WZC Sint-Vincentius Erpe-Mere YE2024. NOT Hartjes remine. NOT CAR Halle remine. NOT AZ Sint-Maria SCAN. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial.
- Wrote: sources (+4); budgets (+11); commitments (+1); leaderboard (+1 pi 5.08); entities (+1 vzw_kapoentjes_halle); foi + draft `gap_kapoentjes_halle_opgroeien_matrix_bruto_808k_omzet73_empty_cash_jump_171k_equity_drop_145k_l5`; rq_2488=done + rq_2489 open; loop_state ticks=2488; raw tick2488/ untracked.
- FOI: **ready not sent**. NOT every-10 (next **2490**). Next: rq_2489 unused leftover public ETA/VAPH/WZC/maatwerk/CAR/CIK/hospital with live 2026pdf elsewhere (NOT De Kapoentjes remine / NOT De Zonnewende remine / NOT WZC Sint-Vincentius Erpe-Mere YE2024 / NOT Hartjes remine / NOT CAR Halle remine / NOT AZ Sint-Maria SCAN / NOT Huize De Veuster remine / NOT Grijkoort remine / NOT GR.O.O.D. no JR / NOT Nektari remine / NOT Reva Ter Linde remine / NOT De Hagewinde remine / NOT BWP remine / NOT Armonea commercial / NOT Vulpia commercial / NOT Korian commercial / NOT Evara remine / NOT Zorg-Saam remine). NOW leftover city_halle CIK taken (CAR already taken). Leftover WZC/VAPH of city_halle still open.

"""
with log.open("ab") as f:
    f.write(entry.encode("utf-8"))
print("loop_log ok")
print("WRITE CORE DONE")
