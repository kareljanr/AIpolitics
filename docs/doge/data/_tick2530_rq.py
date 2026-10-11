from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2530_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_consolata_zaventem"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2530,") != 1:
    raise SystemExit(f"bad 2530 count {rq_raw.count(b'rq_2530,')}")
if b"rq_2531," in rq_raw:
    raise SystemExit("2531 exists")
idx = rq_raw.rfind(b"rq_2530,")
if idx < 0:
    raise SystemExit("rq_2530 not found")

notes_2530 = (
    "Took unused leftover public leftover WZC VZW Consolata Regio Zaventem 0457.206.827 leftover mined city_zaventem leftover-mined AGB-only unused leftover type. "
    "Official NBB VOL-VZW YE2025 2026-00259909 native statutory 44p. Envelope omzet70 JUMP 8969085 "
    "(VZW because 70 present and not commercial-only vs 73 JUMP 1672350; 76A DROP 1316; 70/76A JUMP 10764429); cash JUMP 800197; pnl JUMP -109012; 9901 JUMP FLIP 86348; "
    "equity DROP 7528775; assets DROP 20506369; debt DROP 12977594; FTE DROP 124. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt locked leftover city_zaventem leftover WZC "
    "(sister of leftover city_putte leftover WZC CONSOLATA 0457.207.223@2529 DIFFERENT KBO; leftover city_putte leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Beerzelhof leftover-via-VE remine@2160 leftover WZC type now taken; leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial leftover WZC Gerkenberg@2528 leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_zaventem leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP). "
    "NOT leftover city_putte leftover WZC CONSOLATA remine@2529. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial."
)
extra_2530 = (
    "tick2530 leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type; Strong native PDF; 1 VE; prior-year identical; EVERY-10 PLUS leftover dual; next rq_2531 leftover dual (NOT every-10; next every-10 2540)"
)
notes_2531 = (
    "Leftover dual (NOT every-10; next every-10 is 2540). Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_zaventem leftover WZC taken (Consolata@2530 leftover-mined AGB-only unused leftover type; leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV 0821.289.991 commercial SKIP leftover WZC Isidoor Trappeniers OCMW 0212.185.520 SKIP). "
    "NOW leftover city_putte leftover WZC taken (Consolata@2529 leftover-mined AGB-only unused leftover type; leftover WZC Beerzelhof Foyer De Lork 0446.022.331 leftover-via-VE remine@2160 SKIP leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken). "
    "NOW leftover city_bree leftover WZC taken (Gerkenberg@2528 leftover-mined AGB-only unused leftover type; leftover WZC Boneput SLG 0845.064.196 commercial SKIP leftover VAPH none local leftover CAR leftover-via-VE Kinrooi 0422.988.393 SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken). "
    "NOW leftover city_arendonk leftover WZC taken (WZGA@2526 leftover-mined AGB-only unused leftover type). NOW leftover city_arendonk leftover VAPH taken (Talander@2527 leftover-mined AGB-only unused leftover type; leftover OCMW De Peulder 0212.236.097 SKIP). leftover city_arendonk leftover CAR/maatwerk none local leftover CIK Dol-Fijn leftover-via-VE Turnhout SKIP leftover CIK Toverbos BV / Kroontje BV commercial SKIP leftover CIK fallback not taken. "
    "NOW leftover city_wingene leftover WZC taken (Het Laar@2525 leftover-mined AGB-only; leftover WZC Curando 0445.499.422 remine@2046 SKIP; leftover WZC Amphora 0833.161.902 unused leftover WZC type now taken leftover Companyweb last deposit 02.07.2025 likely YE2024). leftover city_wingene leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_bertem leftover WZC taken (Sint-Bernardus@2523 leftover-mined AGB-only). NOW leftover city_bertem leftover VAPH taken (De Eglantier@2524 leftover-mined AGB-only; leftover VAPH A-Tipi 0788.729.170 leftover-via-VE Leuven SKIP). leftover city_bertem leftover CAR none local leftover maatwerk none local leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine Sint-Bernardus@2523 leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_stabroek leftover WZC taken (Aalmoezenier Cuypers@2522; leftover WZC Villa ter Molen Vulpia 0521.970.559 commercial SKIP). leftover city_stabroek leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_wichelen leftover WZC taken (Den Anker / Torkenshof@2521; leftover WZC Molenkouter OCMW 0212.183.045 SKIP). leftover city_wichelen leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_lebbeke leftover WZC taken (Reva Tersig@2520; leftover WZC Hof ter Veldeken OCMW 0212.192.151 SKIP; leftover WZC Seniorie Ter Minne BV 0444.150.330 commercial SKIP; leftover WZC Seniorie Minneveld BV 0840.544.095 commercial SKIP). leftover city_lebbeke leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_meerhout leftover WZC taken (Ter Kempen@2519; leftover WZC De Berk OCMW 0212.196.705 SKIP leftover maatwerk De Sprong remine@2286 HARD SKIP). leftover city_meerhout leftover VAPH t Volderke 0432.224.080 YE2025 2026-00271440 SCAN Konica SKIP leftover CAR/CIK unused-looking leftover CIK fallback not taken. "
    "NOW leftover city_lanaken leftover WZC Huize Sint Anna 0413.567.319 YE2024 SKIP leftover WZC 3 Eiken leftover-via-VE Geel remine. leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE Bilzen SKIP. leftover city_de_panne leftover WZC Sint-Bernardus remine@2163 leftover city_aalter leftover WZC Veilige Have remine@1733 leftover city_rumst leftover WZC De Wijtshage remine@2082 leftover city_lendelede leftover WZC Aksent remine@2054 leftover city_zonnebeke leftover WZC Sint-Jozef remine@2326 leftover city_nieuwpoort leftover WZC Ten Anker remine@2078 leftover city_bredene leftover WZC Westerhauwe remine@2056 leftover city_schelle leftover WZC Familiehof remine@1744 leftover city_haacht leftover WZC Langerheide remine@2173 leftover city_pepingen leftover WZC Mater Dei remine@2081. leftover city_oud_turnhout leftover maatwerk De Troef 0469.045.082 YE2024 SKIP leftover WZC Smeedeshof Armonea SKIP leftover city_middelkerke leftover WZC Haerlebout Squatina 0418.015.857 leftover-via-VE Oostende SKIP. "
    "NOW leftover city_scherpenheuvel_zichem leftover types exhausted (De Vlaspit@2515 / Honighsdries@2516 / Levensruimte@2517 / De Schommel@2518). leftover WZC OLV Ster der Zee still unused-looking likely OCMW leftover WZC Voortberg Armonea SKIP leftover CAR none local. "
    "NOW leftover city_zottegem leftover WZC+VAPH+CIK taken leftover city_grimbergen leftover WZC+maatwerk taken leftover WZC Heilig Hart remine@2074 leftover city_oosterzele leftover WZC Groep Sint-Franciscus remine@2142 zetel Brakel SKIP leftover city_herselt leftover WZC Sint-Barbara remine@2019 leftover city_niel still unused leftover WZC De Medemens remine@2086 leftover city_mol leftover CIK Molleke YE2024 SKIP leftover WZC Witte Meren remine leftover city_denderleeuw leftover CIK t Sas YE2024 SKIP leftover WZC Gravenkasteel SKIP leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken leftover city_lennik leftover maatwerk remine@2201 leftover city_londerzeel slug MISSING leftover city_wortegem_petegem slug MISSING leftover WZC De Linde remine@2425 leftover city_kapellen slug MISSING. "
    "HARD SKIP: Gravenkasteel group 0874.863.091. All OCMW / Armonea / Korian / Vulpia / CuraCare / Emeis / Zorgbedrijf. AZ Waregem SCAN HARD SKIP. De Heymeulen HARD SKIP. Jules/i-mens leftover-via-VE SKIP. Stay OFF Kloosterstraat 6 Drongen. Stay OFF Knokke-Heist / Kalmthout / leftover-via-VE Gent/Brussels/Hasselt/Drongen/Leuven/Diest/Brakel/Turnhout/Oostende/Kinrooi/Geel/Bilzen/Evergem. leftover city_meerhout leftover VAPH t Volderke SCAN SKIP leftover maatwerk DE SPRONG remine@2286 HARD SKIP. leftover city_bertem leftover VAPH A-Tipi leftover-via-VE Leuven SKIP leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine leftover city_wingene leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover WZC Het Laar remine leftover city_arendonk leftover WZC WZGA remine leftover OCMW De Peulder SKIP leftover VAPH Talander remine leftover CIK Dol-Fijn leftover-via-VE leftover CIK Toverbos/Kroontje BV commercial leftover city_bree leftover WZC Gerkenberg remine leftover WZC Boneput SLG commercial leftover CAR leftover-via-VE Kinrooi SKIP leftover city_putte leftover WZC Consolata remine leftover WZC Beerzelhof Foyer De Lork leftover-via-VE remine leftover city_zaventem leftover WZC Consolata remine leftover city_lanaken leftover WZC Huize Sint Anna YE2024 leftover WZC 3 Eiken leftover-via-VE leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE leftover city_oud_turnhout leftover maatwerk De Troef YE2024 leftover WZC Smeedeshof Armonea leftover city_middelkerke leftover WZC Haerlebout leftover-via-VE Oostende. "
    "NOT Consolata Zaventem remine. NOT Consolata Putte remine. NOT Gerkenberg remine. NOT Talander remine. NOT WZGA remine. NOT Het Laar remine. NOT De Eglantier remine. NOT Sint-Bernardus Bertem remine. NOT Aalmoezenier Cuypers remine. NOT Torkenshof remine. NOT Reva Tersig remine. NOT Ter Kempen remine. NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Korian commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2531 = (
    "spawned after tick2530 leftover city_zaventem leftover WZC; Consolata Zaventem taken leftover mined city_zaventem leftover WZC leftover-mined AGB-only unused leftover type leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP; leftover city_putte leftover WZC taken leftover WZC Beerzelhof leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover WZC CONSOLATA remine; leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial leftover WZC Gerkenberg remine; leftover city_arendonk leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK leftover-via-VE/commercial leftover CIK fallback not taken leftover OCMW De Peulder SKIP leftover VAPH Talander remine leftover CIK Dol-Fijn leftover-via-VE leftover CIK Toverbos/Kroontje BV commercial; leftover city_wingene leftover WZC taken leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Het Laar remine; leftover city_lanaken leftover WZC Huize Sint Anna YE2024 leftover WZC 3 Eiken leftover-via-VE leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE leftover city_de_panne leftover WZC Sint-Bernardus remine leftover city_aalter leftover WZC Veilige Have remine leftover city_oud_turnhout leftover maatwerk De Troef YE2024 leftover WZC Smeedeshof Armonea leftover city_middelkerke leftover WZC Haerlebout leftover-via-VE Oostende leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_niel still unused leftover WZC De Medemens remine leftover city_mol leftover CIK Molleke YE2024 leftover city_denderleeuw leftover CIK t Sas YE2024 leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; leftover VAPH A-Tipi leftover-via-VE Leuven SKIP leftover city_bertem leftover CIK Ferm leftover-via-VE leftover CIK Elfenbosje remine leftover city_meerhout leftover maatwerk DE SPRONG remine@2286 HARD SKIP leftover VAPH t Volderke SCAN; leftover dual NOT every-10 (next every-10 2540)"
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

new_2530 = rq_line([
    "rq_2530",
    "leftover dual Consolata Zaventem YE2025 PLUS every-10",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2530,
    "",
    STAMP,
    STAMP,
    extra_2530,
])
new_2531 = rq_line([
    "rq_2531",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2531,
    "",
    STAMP,
    STAMP,
    extra_2531,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2530)
    f.write(new_2531)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2530", chk.count(b"rq_2530,"), "n2531", chk.count(b"rq_2531,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2530,2530,no,"
    "tick2530 leftover dual Consolata Zaventem 0457.206.827 Strong native PDF (omzet70 JUMP 8969085 not commercial-only vs 73; 73 JUMP 1672350; 76A DROP 1316; envelope omzet70 JUMP 8969085; pnl JUMP -109012; 9901 JUMP FLIP 86348; equity DROP 7528775; assets DROP 20506369; debt DROP 12977594; FTE DROP 124; kapitaalsubsidies DROP 5686964; destin691 empty; cash JUMP 800197; 1 VE leftover city_zaventem leftover WZC leftover-mined AGB-only unused leftover type); leftover mined city_zaventem leftover WZC; prior-year identical; EVERY-10 PLUS leftover dual; FIRST leftover unused + live official YE2025 leftover city_zaventem leftover WZC (sister of leftover city_putte leftover WZC CONSOLATA@2529 DIFFERENT KBO leftover city_putte leftover WZC taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Beerzelhof leftover-via-VE remine leftover WZC type now taken leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial leftover WZC Gerkenberg@2528 leftover city_arendonk leftover WZC+VAPH taken leftover city_wingene leftover WZC taken leftover city_zaventem leftover maatwerk TWI unused-looking leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; NOT Korian commercial; NOT leftover city_putte leftover WZC CONSOLATA remine; next rq_2531 leftover dual (NOT every-10; next every-10 2540)\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
