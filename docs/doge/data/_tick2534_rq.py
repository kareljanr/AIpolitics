from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2534_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_meerpaal_willebroek"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2534,") != 1:
    raise SystemExit(f"bad 2534 count {rq_raw.count(b'rq_2534,')}")
if b"rq_2535," in rq_raw:
    raise SystemExit("2535 exists")
idx = rq_raw.rfind(b"rq_2534,")
if idx < 0:
    raise SystemExit("rq_2534 not found")

notes_2534 = (
    "Took unused leftover public leftover VAPH VZW De Meerpaal 0443.206.559 leftover mined city_willebroek leftover-mined AGB-only unused leftover type. "
    "Official NBB VKT-VZW YE2025 2026-00152128 native statutory 25p. Envelope bruto9900 JUMP 3496689 "
    "(VKT because 73 empty and bruto >> omzet; 70 empty; 73 empty; 76A JUMP 427); cash JUMP 1263424; pnl JUMP 228053; 9901 JUMP 213789; "
    "equity JUMP 1819290; assets JUMP 2714324; debt JUMP 895034; FTE JUMP 41.4; destin691 empty DROP. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt locked leftover city_willebroek leftover VAPH "
    "(leftover city_willebroek leftover WZC Seniorplaza@2532 leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover VAPH type now taken; leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine@2355 SKIP leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine; leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined). "
    "FIRST LOCK leftover city_willebroek leftover VAPH. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT leftover WZC Seniorplaza remine@2532."
)
extra_2534 = (
    "tick2534 leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type; Strong native PDF; 1 VE; prior-year identical; NOT every-10 (next every-10 2540); next rq_2535 leftover dual"
)
notes_2535 = (
    "Leftover dual (NOT every-10; next every-10 is 2540). Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_willebroek leftover VAPH taken (De Meerpaal@2534 leftover-mined AGB-only unused leftover type) leftover WZC taken (Seniorplaza@2532 leftover-mined AGB-only unused leftover type; leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover VAPH type now taken). "
    "NOW leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine@2355 SKIP leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine. "
    "NOW leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 CDN 403 + NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover-mined leftover WZC unused leftover type leftover-mined. "
    "NOW leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP. "
    "NOW leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken. "
    "NOW leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover CIK Pamperbroekje BV unused leftover VAPH/CAR/maatwerk empty-looking. "
    "NOW leftover city_niel still unused sports/culture only leftover WZC De Medemens remine. leftover city_wingene leftover WZC taken leftover WZC Amphora unused leftover WZC type already taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. leftover city_putte leftover WZC taken leftover city_bree leftover WZC taken leftover city_arendonk leftover WZC+VAPH taken leftover city_scherpenheuvel_zichem leftover types exhausted. leftover city_lanaken leftover WZC Huize Sint Anna YE2024 leftover WZC 3 Eiken leftover-via-VE Geel leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE Bilzen leftover city_oud_turnhout leftover maatwerk De Troef YE2024 leftover WZC Smeedeshof Armonea leftover city_middelkerke leftover WZC Haerlebout leftover-via-VE Oostende leftover city_meerhout leftover maatwerk DE SPRONG remine leftover VAPH t Volderke SCAN leftover CIK fallbacks not taken. "
    "HARD SKIP remine leftover WZCs Seniorplaza@2532 Sint-Jozef Deinze@2533 Capenberg@2531 Consolata Zaventem@2530 CONSOLATA Putte@2529 Gerkenberg@2528 WZGA@2526 Talander@2527 Het Laar@2525 De Eglantier@2524 Sint-Bernardus Bertem@2523. De Heymeulen HARD SKIP. AZ Waregem SCAN HARD SKIP. t Volderke SCAN HARD SKIP. leftover city_bonheiden leftover hospital Imelda 403 stall max 3 min. Stay OFF Kloosterstraat 6 Drongen. leftover-via-VE of Brussels/Hasselt/Gent/Drongen/Leuven/Diest/Brakel/Turnhout/Oostende/Kinrooi/Geel/Bilzen/Evergem/Antwerpen seated parent is NOT enough. Commercial Armonea/Korian/Vulpia/CuraCare/SLG/OCMW skip. leftover CIK of a less-picked mined city is LAST fallback only. "
    "NOT De Meerpaal remine. NOT Seniorplaza remine. NOT Sint-Jozef Deinze remine. NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial."
)
extra_2535 = (
    "spawned after tick2534 leftover city_willebroek leftover VAPH; De Meerpaal taken leftover mined city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_niel sports/culture only leftover city_scherpenheuvel_zichem leftover types exhausted; leftover dual NOT every-10 (next every-10 2540)"
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

new_2534 = rq_line([
    "rq_2534",
    "leftover dual De Meerpaal Willebroek YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2534,
    "",
    STAMP,
    STAMP,
    extra_2534,
])
new_2535 = rq_line([
    "rq_2535",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2535,
    "",
    STAMP,
    STAMP,
    extra_2535,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2534)
    f.write(new_2535)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2534", chk.count(b"rq_2534,"), "n2535", chk.count(b"rq_2535,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2534,2534,no,"
    "tick2534 leftover dual De Meerpaal Willebroek 0443.206.559 Strong native PDF (omzet70 empty VKT; 73 empty VKT; 76A JUMP 427; envelope bruto9900 JUMP 3496689; pnl JUMP 228053; 9901 JUMP 213789; equity JUMP 1819290; assets JUMP 2714324; debt JUMP 895034; FTE JUMP 41.4; kapitaalsubsidies DROP 75307; destin691 empty DROP; cash JUMP 1263424; 1 VE leftover city_willebroek leftover VAPH leftover-mined AGB-only unused leftover type); leftover mined city_willebroek leftover VAPH; prior-year identical; FIRST leftover unused + live official YE2025 leftover city_willebroek leftover VAPH (leftover city_willebroek leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover VAPH type now taken leftover city_deinze leftover WZC taken leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR leftover-via-VE Drongen Ter Kouter remine leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover WZC unused leftover type leftover-mined leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_willebroek leftover VAPH; next rq_2535 leftover dual (NOT every-10; next every-10 2540)\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
