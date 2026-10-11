from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2535_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_annendael_diest"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2535,") != 1:
    raise SystemExit(f"bad 2535 count {rq_raw.count(b'rq_2535,')}")
if b"rq_2536," in rq_raw:
    raise SystemExit("2536 exists")
idx = rq_raw.rfind(b"rq_2535,")
if idx < 0:
    raise SystemExit("rq_2535 not found")

notes_2535 = (
    "Took unused leftover public leftover WZC VZW Zorggroep Annendael 0414.604.526 leftover mined city_diest leftover-mined AGB-only unused leftover type. "
    "Official NBB VOL-VZW YE2025 2026-00283395 native statutory 53p. Envelope omzet70 JUMP 36063571 "
    "(VZW because 70 present and not commercial-only vs 73 5994527; 70 JUMP 36063571; 73 JUMP 5994527; 76A JUMP 853984); cash DROP 8929733; pnl FLIP -451172; 9901 DROP 808373; "
    "equity DROP 42367160; assets DROP 97618819; debt DROP 51863562; FTE JUMP 398.9; destin691 JUMP 3211567. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt locked leftover city_diest leftover WZC "
    "(leftover city_willebroek leftover VAPH De Meerpaal@2534 leftover WZC Seniorplaza@2532 leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken; leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine; leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined). "
    "FIRST LOCK leftover city_diest leftover WZC. "
    "NOT leftover-via-VE of a DIFFERENT leftover city. NOT Armonea commercial. NOT Vulpia commercial. NOT leftover De Meerpaal remine@2534."
)
extra_2535 = (
    "tick2535 leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type; Strong native PDF; 4 VE; prior-year identical; NOT every-10 (next every-10 2540); next rq_2536 leftover dual"
)
notes_2536 = (
    "Leftover dual (NOT every-10; next every-10 is 2540). Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. HARD SKIP leftover CIK. HARD SKIP KBO activity POST/GET. Targeted official WZC list /tmp/tick2519/wzc.csv leftover-mined AGB-only slugs. "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_diest leftover WZC taken (Annendael@2535 leftover-mined AGB-only unused leftover type; leftover hospital same KBO Annendael SKIP leftover VAPH/CAR/maatwerk unused-looking leftover CIK HARD SKIP leftover WZC type now taken leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC). "
    "NOW leftover city_willebroek leftover VAPH taken (De Meerpaal@2534 leftover-mined AGB-only unused leftover type) leftover WZC taken (Seniorplaza@2532 leftover-mined AGB-only unused leftover type; leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken). "
    "NOW leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine. "
    "NOW leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 CDN 403 + NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover-mined leftover WZC unused leftover type leftover-mined. "
    "NOW leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP. "
    "NOW leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken. "
    "NOW leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover CIK Pamperbroekje BV unused. "
    "NOW leftover city_oostkamp leftover WZC Ter Luchte 0738.896.510 YE2025 unused leftover WZC type unused leftover-mined AGB-only. leftover city_vleteren leftover WZC Benaja 0431.261.604 YE2024 SKIP leftover-mined OCMW-only leftover WZC type unused. leftover city_oud_heverlee leftover WZC De Kouter 0848.738.221 YE2025 unused leftover-mined OCMW-only leftover WZC type unused. leftover city_machelen leftover WZC Residentie Woluwedal Zorg Voor Senioren 0823.372.721 likely commercial SKIP. leftover city_niel still unused sports/culture only leftover WZC De Medemens remine. leftover city_wingene leftover WZC taken leftover WZC Amphora unused leftover WZC type already taken leftover VAPH/CAR/maatwerk none local leftover CIK HARD SKIP. leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_scherpenheuvel_zichem leftover types exhausted leftover Huis Sterre same KBO leftover-via-VE of leftover city_diest leftover WZC. leftover city_lanaken leftover WZC Huize Sint Anna YE2024 leftover WZC 3 Eiken leftover-via-VE Geel leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE Bilzen leftover city_oud_turnhout leftover maatwerk De Troef YE2024 leftover WZC Smeedeshof Armonea leftover city_middelkerke leftover WZC Haerlebout leftover-via-VE Oostende leftover city_meerhout leftover maatwerk DE SPRONG remine leftover VAPH t Volderke SCAN leftover CIK HARD SKIP. "
    "HARD SKIP remine leftover WZCs Annendael@2535 De Meerpaal@2534 Seniorplaza@2532 Sint-Jozef Deinze@2533 Capenberg@2531 Consolata Zaventem@2530 CONSOLATA Putte@2529 Gerkenberg@2528 WZGA@2526 Talander@2527 Het Laar@2525. De Heymeulen HARD SKIP. AZ Waregem SCAN HARD SKIP. t Volderke SCAN HARD SKIP. leftover city_bonheiden leftover hospital Imelda 403 stall max 3 min. HARD SKIP leftover CIK. HARD SKIP KBO activity POST/GET. Stay OFF Kloosterstraat 6 Drongen. leftover-via-VE of Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel/Turnhout/Oostende/Kinrooi/Geel/Bilzen/Evergem/Antwerpen seated parent is NOT enough for a DIFFERENT leftover city — leftover city_diest leftover WZC with official zetel Diest IS enough and now taken. Commercial Armonea/Korian/Vulpia/CuraCare/SLG/OCMW skip. leftover CIK of a less-picked mined city is LAST fallback only. "
    "NOT Annendael remine. NOT De Meerpaal remine. NOT Seniorplaza remine. NOT Sint-Jozef Deinze remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial."
)
extra_2536 = (
    "spawned after tick2535 leftover city_diest leftover WZC; Annendael taken leftover mined city_diest leftover WZC leftover-mined AGB-only unused leftover type leftover hospital same KBO SKIP leftover VAPH/CAR/maatwerk unused-looking leftover CIK HARD SKIP leftover WZC type now taken leftover Huis Sterre same KBO leftover city_scherpenheuvel_zichem leftover WZC type exhausted leftover-via-VE of leftover city_diest leftover WZC leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_oostkamp leftover WZC Ter Luchte unused leftover WZC type unused leftover-mined AGB-only leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_niel sports/culture only leftover city_scherpenheuvel_zichem leftover types exhausted leftover Huis Sterre same KBO leftover-via-VE of leftover city_diest leftover WZC; leftover dual NOT every-10 (next every-10 2540)"
)

def rq_line(fields):
    buf = StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(fields)
    line = buf.getvalue()
    n = len(next(csv.reader(StringIO(line))))
    if n != 12:
        raise SystemExit(f"rq fields {n} != 12 for {fields[0]}")
    if not line.endswith("\n"):
        raise SystemExit("rq line no LF")
    if line.count("\n") != 1:
        raise SystemExit("rq line extra NL")
    return line.encode("utf-8")

new_2535 = rq_line([
    "rq_2535",
    "leftover dual Annendael Diest YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2535,
    "",
    STAMP,
    STAMP,
    extra_2535,
])
new_2536 = rq_line([
    "rq_2536",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2536,
    "",
    STAMP,
    STAMP,
    extra_2536,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2535)
    f.write(new_2536)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2535", chk.count(b"rq_2535,"), "n2536", chk.count(b"rq_2536,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2535,2535,no,"
    "tick2535 leftover dual Annendael Diest 0414.604.526 Strong native PDF (omzet70 JUMP 36063571; 73 JUMP 5994527; 76A JUMP 853984; envelope omzet70 JUMP 36063571; pnl FLIP -451172; 9901 DROP 808373; equity DROP 42367160; assets DROP 97618819; debt DROP 51863562; FTE JUMP 398.9; kapitaalsubsidies DROP 12754931; destin691 JUMP 3211567; cash DROP 8929733; 4 VE leftover city_diest leftover WZC leftover-mined AGB-only unused leftover type); leftover mined city_diest leftover WZC; prior-year identical; FIRST leftover unused + live official YE2025 leftover city_diest leftover WZC (leftover city_willebroek leftover VAPH taken leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK HARD SKIP leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK HARD SKIP leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK HARD SKIP leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk empty-looking leftover CIK HARD SKIP leftover WZC type already taken leftover city_oostkamp leftover WZC Ter Luchte unused leftover WZC type unused leftover-mined AGB-only leftover city_vleteren leftover WZC Benaja YE2024 SKIP leftover city_oud_heverlee leftover WZC De Kouter YE2025 unused leftover-mined OCMW-only leftover city_machelen leftover WZC Woluwedal likely commercial SKIP leftover city_scherpenheuvel_zichem leftover types exhausted leftover Huis Sterre same KBO leftover-via-VE of leftover city_diest leftover WZC); NOT leftover-via-VE of a DIFFERENT leftover city; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_diest leftover WZC; next rq_2536 leftover dual (NOT every-10; next every-10 2540)\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
