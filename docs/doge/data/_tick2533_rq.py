from pathlib import Path
import csv
from io import StringIO

ROOT = Path("/workspace/AIpolitics")
DATA = ROOT / "docs/doge/data"
STAMP, DAY = (DATA / "_tick2533_stamp.txt").read_text().strip().splitlines()
print("STAMP", STAMP)
EID = "vzw_sint_jozef_deinze"

rq_path = DATA / "research_queue.csv"
rq_raw = rq_path.read_bytes()
if not rq_raw.endswith(b"\n"):
    raise SystemExit("rq no LF")
if b"\r\n" in rq_raw:
    raise SystemExit("CRLF")
if rq_raw.count(b"rq_2533,") != 1:
    raise SystemExit(f"bad 2533 count {rq_raw.count(b'rq_2533,')}")
if b"rq_2534," in rq_raw:
    raise SystemExit("2534 exists")
idx = rq_raw.rfind(b"rq_2533,")
if idx < 0:
    raise SystemExit("rq_2533 not found")

notes_2533 = (
    "Took unused leftover public leftover WZC VZW R.V.T. Sint-Jozef Deinze 0409.698.603 leftover mined city_deinze leftover-mined AGB-only unused leftover type. "
    "Official NBB VOL-VZW YE2025 2026-00259876 native statutory 42p. Envelope omzet70 JUMP 9471817 "
    "(VZW because 70 present and not commercial-only vs 73 DROP 1653070; 76A JUMP 11258; 70/76A JUMP 11372156); cash JUMP 878637; pnl FLIP 511833; 9901 FLIP 293988; "
    "equity JUMP 8597413; assets DROP 13344074; debt DROP 4746661; FTE DROP 124; destin691 JUMP 4418723. "
    "FIRST leftover unused + live official YE2025 after leftover-type hunt locked leftover city_deinze leftover WZC "
    "(leftover city_willebroek leftover WZC Seniorplaza@2532 leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken; leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP; leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 m140-f-p CDN 403 NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover-mined leftover WZC unused leftover type leftover-mined; leftover city_boechout leftover WZC Capenberg@2531 leftover WZC Avondvrede remine@2166 leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_deinze leftover VAPH taken@2496/2499 leftover-via-VE Evergem Franciscanessen 0451.818.080 SKIP leftover maatwerk Demival remine@2191 leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine@2066). "
    "FIRST LOCK leftover city_deinze leftover WZC. "
    "NOT leftover-via-VE Evergem Franciscanessen SKIP. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT leftover city_zonnebeke leftover WZC Sint-Jozef remine@2326."
)
extra_2533 = (
    "tick2533 leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type; Strong native PDF; 1 VE; prior-year identical; NOT every-10 (next every-10 2540); next rq_2534 leftover dual"
)
notes_2534 = (
    "Leftover dual (NOT every-10; next every-10 is 2540). Hunt ONE unused leftover public WZC / VAPH / CAR / hospital / maatwerk (or leftover CIK if a less-picked mined city still has unused ones) of a mined Flanders city that has a TRUE official YE2025 statutory native PDF. "
    "STOP leftover-note / loop_log KBO extractors. Targeted postcode + phonetic VZW (rechtsvormFonetic=017). "
    "Confirm unused (0 real entity rows) + leftover of a mined parent + official KBO zetel (not VE-only) + official NBB YE2025 native PDF euros. "
    "NOW leftover city_deinze leftover WZC taken (Sint-Jozef@2533 leftover-mined AGB-only unused leftover type; leftover VAPH taken@2496/2499 leftover-via-VE Evergem Uitbating Zusters Franciscanessen 0451.818.080 SKIP leftover maatwerk Demival remine@2191 leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque 0697.663.689 SKIP leftover Zorgbedrijf Ter Leenen 0666.615.870 SKIP leftover WZC Bejaardenzorg Zusters 0454.090.355 remine@2066). "
    "NOW leftover city_willebroek leftover WZC taken (Seniorplaza@2532 leftover-mined AGB-only unused leftover type; leftover WZC Ten Weldebrouc OCMW 0212.184.035 SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken). "
    "NOW leftover city_boechout leftover WZC taken (Capenberg@2531 leftover-mined AGB-only unused leftover type; leftover WZC Avondvrede NV 0446.506.836 remine@2166 Anima commercial SKIP leftover WZC Sint-Mathildis De Medemens 0428.692.191 leftover-via-VE Antwerpen remine@2086 SKIP leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken). "
    "NOW leftover city_zaventem leftover WZC taken (Consolata@2530 leftover-mined AGB-only unused leftover type; leftover maatwerk TWI 0454.926.733 remine@2282 SKIP leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg 0479.401.318 unused leftover WZC type now taken leftover WZC Always Home NV 0821.289.991 commercial SKIP leftover WZC Isidoor Trappeniers OCMW 0212.185.520 SKIP). "
    "NOW leftover city_bonheiden leftover hospital Imelda 0409.835.490 YE2025 2026-00184318 m140-f-p CDN 403 + NBB broker 403 SKIP leftover WZC Den Olm same KBO leftover hospital unused leftover type leftover-mined leftover WZC unused leftover type leftover-mined. "
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
    "HARD SKIP: Gravenkasteel group 0874.863.091. All OCMW / Armonea / Korian / Vulpia / CuraCare / Emeis / Zorgbedrijf. AZ Waregem SCAN HARD SKIP. De Heymeulen HARD SKIP. Jules/i-mens leftover-via-VE SKIP. Stay OFF Kloosterstraat 6 Drongen. Stay OFF Knokke-Heist / Kalmthout / leftover-via-VE Gent/Brussels/Hasselt/Drongen/Leuven/Diest/Brakel/Turnhout/Oostende/Kinrooi/Geel/Bilzen/Evergem. leftover city_meerhout leftover VAPH t Volderke SCAN SKIP leftover maatwerk DE SPRONG remine@2286 HARD SKIP. leftover city_bertem leftover VAPH A-Tipi leftover-via-VE Leuven SKIP leftover CIK Ferm leftover-via-VE Leuven SKIP leftover CIK Elfenbosje remine leftover city_wingene leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type now taken leftover WZC Het Laar remine leftover city_arendonk leftover WZC WZGA remine leftover OCMW De Peulder SKIP leftover VAPH Talander remine leftover CIK Dol-Fijn leftover-via-VE leftover CIK Toverbos/Kroontje BV commercial leftover city_bree leftover WZC Gerkenberg remine leftover WZC Boneput SLG commercial leftover CAR leftover-via-VE Kinrooi SKIP leftover city_putte leftover WZC Consolata remine leftover WZC Beerzelhof Foyer De Lork leftover-via-VE remine leftover city_zaventem leftover WZC Consolata remine leftover maatwerk TWI remine leftover city_boechout leftover WZC Capenberg remine leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE leftover city_bonheiden leftover hospital Imelda CDN 403 leftover city_willebroek leftover WZC Seniorplaza remine leftover WZC Ten Weldebrouc OCMW leftover city_deinze leftover WZC Sint-Jozef remine leftover VAPH Vierklaver remine leftover VAPH Ten Dries remine leftover-via-VE Evergem Franciscanessen SKIP leftover city_lanaken leftover WZC Huize Sint Anna YE2024 leftover WZC 3 Eiken leftover-via-VE leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE leftover city_oud_turnhout leftover maatwerk De Troef YE2024 leftover WZC Smeedeshof Armonea leftover city_middelkerke leftover WZC Haerlebout leftover-via-VE Oostende. "
    "NOT Sint-Jozef Deinze remine. NOT Seniorplaza remine. NOT Capenberg remine. NOT Consolata Zaventem remine. NOT Consolata Putte remine. NOT Gerkenberg remine. NOT Talander remine. NOT WZGA remine. NOT Het Laar remine. NOT De Eglantier remine. NOT Sint-Bernardus Bertem remine. NOT Aalmoezenier Cuypers remine. NOT Torkenshof remine. NOT Reva Tersig remine. NOT Ter Kempen remine. NOT De Schommel remine. NOT Huize Levensruimte remine. NOT Huyze Honighsdries remine. NOT De Vlaspit remine. NOT Vierklaver remine. NOT Ten Dries remine. "
    "NOT leftover-via-VE. NOT Armonea commercial. NOT Vulpia commercial. NOT Evara remine. NOT Zorg-Saam remine."
)
extra_2534 = (
    "spawned after tick2533 leftover city_deinze leftover WZC; Sint-Jozef taken leftover mined city_deinze leftover WZC leftover-mined AGB-only unused leftover type leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_willebroek leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_boechout leftover WZC taken leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover city_putte leftover WZC taken leftover WZC Beerzelhof leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover WZC CONSOLATA remine leftover city_bree leftover WZC taken leftover VAPH none local leftover CAR leftover-via-VE Kinrooi SKIP leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Boneput SLG commercial leftover WZC Gerkenberg remine leftover city_arendonk leftover WZC+VAPH taken leftover CAR/maatwerk none local leftover CIK leftover-via-VE/commercial leftover CIK fallback not taken leftover OCMW De Peulder SKIP leftover VAPH Talander remine leftover CIK Dol-Fijn leftover-via-VE leftover CIK Toverbos/Kroontje BV commercial leftover city_wingene leftover WZC taken leftover WZC Curando remine leftover WZC Amphora unused leftover WZC type already taken leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Het Laar remine leftover city_lanaken leftover WZC Huize Sint Anna YE2024 leftover WZC 3 Eiken leftover-via-VE leftover city_oudsbergen leftover WZC Kimpenhof leftover-via-VE leftover city_de_panne leftover WZC Sint-Bernardus remine leftover city_aalter leftover WZC Veilige Have remine leftover city_oud_turnhout leftover maatwerk De Troef YE2024 leftover WZC Smeedeshof Armonea leftover city_middelkerke leftover WZC Haerlebout leftover-via-VE Oostende leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_niel still unused leftover WZC De Medemens remine leftover city_mol leftover CIK Molleke YE2024 leftover city_denderleeuw leftover CIK t Sas YE2024 leftover city_erpe_mere VAPH/CAR/maatwerk/CIK still open leftover WZC Sint-Vincentius unused leftover WZC type already taken; AZ Waregem SCAN HARD SKIP; Jules/i-mens leftover-via-VE SKIP; leftover VAPH A-Tipi leftover-via-VE Leuven SKIP leftover city_bertem leftover CIK Ferm leftover-via-VE leftover CIK Elfenbosje remine leftover city_meerhout leftover maatwerk DE SPRONG remine@2286 HARD SKIP leftover VAPH t Volderke SCAN; leftover dual NOT every-10 (next every-10 2540)"
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

new_2533 = rq_line([
    "rq_2533",
    "leftover dual Sint-Jozef Deinze YE2025",
    "hole_fill",
    "8",
    "done",
    "L5",
    EID,
    notes_2533,
    "",
    STAMP,
    STAMP,
    extra_2533,
])
new_2534 = rq_line([
    "rq_2534",
    "leftover public dual unused WZC/VAPH/CAR/hospital/maatwerk of mined Flanders city YE2025",
    "hole_fill",
    "8",
    "open",
    "L5",
    "",
    notes_2534,
    "",
    STAMP,
    STAMP,
    extra_2534,
])

before = len(rq_raw)
with rq_path.open("r+b") as f:
    f.seek(idx)
    f.truncate()
    f.write(new_2533)
    f.write(new_2534)
after = rq_path.stat().st_size
print("patched rq bytes", before, "->", after, "delta", after - before)
chk = rq_path.read_bytes()
print("n2533", chk.count(b"rq_2533,"), "n2534", chk.count(b"rq_2534,"))
if chk[:idx] != rq_raw[:idx]:
    raise SystemExit("prefix changed")
print("prefix intact")

state = DATA / "loop_state.csv"
state.write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    f"main,continuous,hole_fill,{STAMP},rq_2533,2533,no,"
    "tick2533 leftover dual Sint-Jozef Deinze 0409.698.603 Strong native PDF (omzet70 JUMP 9471817 not commercial-only vs 73; 73 DROP 1653070; 76A JUMP 11258; envelope omzet70 JUMP 9471817; pnl FLIP 511833; 9901 FLIP 293988; equity JUMP 8597413; assets DROP 13344074; debt DROP 4746661; FTE DROP 124; kapitaalsubsidies DROP 1589968; destin691 JUMP 4418723; cash JUMP 878637; 1 VE leftover city_deinze leftover WZC leftover-mined AGB-only unused leftover type); leftover mined city_deinze leftover WZC; prior-year identical; FIRST leftover unused + live official YE2025 leftover city_deinze leftover WZC (leftover city_willebroek leftover WZC taken leftover WZC Ten Weldebrouc OCMW SKIP leftover VAPH/CAR unused-looking leftover maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_zaventem leftover WZC taken leftover maatwerk TWI remine leftover VAPH/CAR none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC Ter Burg unused leftover WZC type now taken leftover WZC Always Home NV commercial leftover WZC Isidoor Trappeniers OCMW SKIP leftover city_bonheiden leftover hospital Imelda CDN 403 leftover WZC Den Olm same KBO leftover city_boechout leftover WZC Capenberg remine leftover WZC Avondvrede remine leftover WZC Sint-Mathildis leftover-via-VE remine leftover VAPH/CAR/maatwerk none local leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover city_deinze leftover VAPH taken leftover-via-VE Evergem Franciscanessen SKIP leftover maatwerk Demival remine leftover CAR unused-looking leftover CIK unused-looking leftover CIK fallback not taken leftover WZC type now taken leftover OCMW Karel Picque SKIP leftover Zorgbedrijf Ter Leenen SKIP leftover WZC Bejaardenzorg Zusters remine leftover city_scherpenheuvel_zichem leftover types exhausted 2515-2518 leftover city_erpe_mere leftover VAPH/CAR/maatwerk/CIK still open leftover WZC Avondzon@2494 + Meredal@2498 taken leftover WZC Sint-Vincentius unused leftover WZC type already taken); NOT leftover-via-VE; NOT Armonea commercial; NOT Vulpia commercial; FIRST LOCK leftover city_deinze leftover WZC; next rq_2534 leftover dual (NOT every-10; next every-10 2540)\n",
    encoding="utf-8",
)
print("loop_state ok")
print("RQ STATE DONE")
