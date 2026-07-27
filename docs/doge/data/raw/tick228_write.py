# tick228: Antwerp MJP youth/social — JES Kras Elegast Posthof
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

JES = {"jeugd": 2350000.00, "veiligheid": 36392.86}
JES_T = sum(JES.values())  # 2386392.86
KRAS = {"sport": 270000.00, "jeugd": 3950000.00, "veiligheid": 40000.00}
KRAS_T = sum(KRAS.values())  # 4260000
ELEGAST = {
    "samenleving": 280000.00,
    "onderwijs": 410000.00,
    "digitalisering": 55080.00,
    "veiligheid": 532974.30,
}
ELEGAST_T = sum(ELEGAST.values())  # 1278054.30
POSTHOF = {
    "samenleving": 280000.00,
    "sociale_economie": 85005.97,
    "digitalisering": 909125.44,
}
POSTHOF_T = sum(POSTHOF.values())  # 1274131.41
SAMPLE = JES_T + KRAS_T + ELEGAST_T + POSTHOF_T  # 9198578.57
PRIOR_SOCIAL = 21031665.79
COMBINED = PRIOR_SOCIAL + SAMPLE  # ~30.23m (overlap free - different orgs)

# --- sources ---
src = data / "sources.csv"
src_add = (
    "src_antwerp_mjp_2026_youth_nominatief,Antwerp MJP 2026 nominatief youth social JES Kras Elegast Posthof,"
    "https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Stad Antwerpen MJP 2026-2031 GR Dec 2025,2026-07-29,official_budget,"
    f'"JES {JES_T:.2f} Kras {KRAS_T:.2f} Elegast {ELEGAST_T:.2f} Posthof {POSTHOF_T:.2f} '
    f'sample {SAMPLE:.2f}; tick228"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_antwerp_mjp_2026_youth_nominatief" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_jes_total_2026,city_antwerpen,2026,{JES_T},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,JES vzw package 2.386m 2026 (jeugd 2.35 + veil 36.4k)",
    f"bud_jes_jeugd_2026,city_antwerpen,2026,{JES['jeugd']},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,JES jeugd 2.35m 2026",
    f"bud_kras_total_2026,city_antwerpen,2026,{KRAS_T},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,Kras Jeugdwerk package 4.26m 2026 (jeugd 3.95 + sport 0.27 + veil 40k)",
    f"bud_kras_jeugd_2026,city_antwerpen,2026,{KRAS['jeugd']},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,Kras jeugd 3.95m 2026",
    f"bud_elegast_total_2026,city_antwerpen,2026,{ELEGAST_T},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,Elegast package 1.278m 2026 (veil 0.533 + onderw 0.41 + sam 0.28 + digi 55k)",
    f"bud_posthof_total_2026,city_antwerpen,2026,{POSTHOF_T},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,Buurtwerk Posthof package 1.274m 2026 (digi 0.909 + sam 0.28 + SE 85k)",
    f"bud_antwerp_youth_social_sample_2026,city_antwerpen,2026,{SAMPLE},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,Youth/social L5 sample JES+Kras+Elegast+Posthof 9.199m 2026",
    f"bud_antwerp_social_youth_combined_2026,city_antwerpen,2026,{COMBINED},,,budgeted,src_antwerp_mjp_2026_youth_nominatief,strong,Combined social+youth sample 8 orgs ~30.23m 2026 (CAW ADIC FC VAGGA + JES Kras Elegast Posthof)",
]
text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_jes_total_2026" not in text:
    bud.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")
    print("budgets ok", len(rows))
else:
    print("budgets already")

# --- commitments ---
cmt = data / "commitments.csv"
raw = cmt.read_bytes()
if b"\x97" in raw:
    cmt.write_bytes(raw.replace(b"\x97", "\u2013".encode("utf-8")))

cmt_add = (
    "cmt_jes_2026_31,JES Antwerp youth multi-year MJP,"
    "city_antwerpen,JES vzw,MJP nominatief jeugd+veiligheid,"
    "2025-12-15,2026,2031,2386392.86,"
    '"{""2026_total"":2386392.86,""2026_jeugd"":2350000,""2026_veiligheid"":36392.86,'
    '""jeugd_path"":[2350000,2387600,2425801.60,2464614.43,2504048.26,2544113.03],'
    '""note"":""Strong MJP; large professional youthwork; dual VL residual""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Professional youth work city financing,Publish dual VL youthwork path,"
    "src_antwerp_mjp_2026_youth_nominatief,strong,Antwerpen>Jeugd>JES,tick228\n"
    "cmt_kras_2026_31,Kras Jeugdwerk multi-year MJP,"
    "city_antwerpen,Kras Jeugdwerk vzw,MJP nominatief jeugd+sport+veiligheid,"
    "2025-12-15,2026,2031,4260000,"
    '"{""2026_total"":4260000,""2026_jeugd"":3950000,""2026_sport"":270000,""2026_veiligheid"":40000,'
    '""jeugd_path"":[3950000,4013200,4077411.20,4142649.78,4208932.18,4276275.09],'
    '""note"":""Strong MJP; largest single youth NGO city line; dual VL residual""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Youthwork Kras city financing,Publish outcome KPIs dual VL,"
    "src_antwerp_mjp_2026_youth_nominatief,strong,Antwerpen>Jeugd>Kras,tick228\n"
    "cmt_elegast_2026_31,Elegast multi-year MJP package,"
    "city_antwerpen,Elegast vzw,MJP nominatief 4 domains,"
    "2025-12-15,2026,2031,1278054.30,"
    '"{""2026_total"":1278054.30,""2026_veiligheid"":532974.30,""2026_onderwijs"":410000,'
    '""2026_samenleving"":280000,""2026_digitalisering"":55080,'
    '""note"":""Strong MJP; youth justice/education social; digi one-year spike 2026""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Elegast youth justice social financing,Publish dual federal/VL justice residual,"
    "src_antwerp_mjp_2026_youth_nominatief,strong,Antwerpen>Social>Elegast,tick228\n"
    "cmt_posthof_2026_31,Buurtwerk Posthof multi-year MJP package,"
    "city_antwerpen,Buurtwerk Posthof vzw,MJP nominatief sam+SE+digi,"
    "2025-12-15,2026,2031,1274131.41,"
    '"{""2026_total"":1274131.41,""2026_samenleving"":280000,""2026_sociale_economie"":85005.97,'
    '""2026_digitalisering"":909125.44,""note"":""Strong MJP; digitalisering 0.909m 2026 one-year spike; community work core""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Neighbourhood work Posthof financing,Publish digi project L5; dual SE,"
    "src_antwerp_mjp_2026_youth_nominatief,strong,Antwerpen>Social>Posthof,tick228\n"
    f"cmt_antwerp_youth_social_sample_2026,Antwerp youth social L5 sample 4 orgs 2026,"
    f"city_antwerpen,JES Kras Elegast Posthof,MJP nominatief,"
    f"2025-12-15,2026,2026,{SAMPLE},"
    f'"{{""jes"":{JES_T},""kras"":{KRAS_T},""elegast"":{ELEGAST_T},""posthof"":{POSTHOF_T},'
    f'""sample_sum"":{SAMPLE},""prior_caw_adic_fc_vagga"":{PRIOR_SOCIAL},""combined_8orgs"":{COMBINED},'
    f'""note"":""Strong 4-org youth/social sample; combined with tick227 social 8 orgs ~30.23m; Mons FOI residual""}}",'
    f"0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    f"City youth social L5 transparency sample,Publish BAZZZ Axi residual; open register,"
    f"src_antwerp_mjp_2026_youth_nominatief,strong,Antwerpen>Jeugd>L5_sample,tick228\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_jes_2026_31" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = f"""lb_kras_4_26m,Kras Jeugdwerk 4.26m 2026,Flanders,ops,Antwerpen>Jeugd>Kras,{KRAS_T},{KRAS_T},Strong MJP: jeugd 3.95 + sport 0.27 + veil 40k = 4.26m; largest single youth NGO city line,strong,src_antwerp_mjp_2026_youth_nominatief,Youth families neighbourhoods,Professional youthwork Kras,Core youth social not pure waste; dual VL residual; outcome KPIs fair,3,7.5,5,5.85,Publish dual VL path outcome KPIs,seed,,tick228
lb_jes_2_39m,JES Antwerp youth 2.39m 2026,Flanders,ops,Antwerpen>Jeugd>JES,{JES_T},2544113.03,Strong MJP: jeugd 2.35m + veil 36k = 2.39m; path to 2.54m,strong,src_antwerp_mjp_2026_youth_nominatief,Youth 12-26 neighbourhoods,Professional youth work JES,Core youth social not pure waste; dual VL residual,3,7.0,4,5.3,Publish dual VL path,seed,,tick228
lb_elegast_1_28m,Elegast 1.28m 2026,Flanders,ops,Antwerpen>Social>Elegast,{ELEGAST_T},{ELEGAST_T},Strong MJP: veil 0.533 + onderw 0.41 + sam 0.28 + digi 55k = 1.278m,strong,src_antwerp_mjp_2026_youth_nominatief,Youth justice education neighbourhoods,Elegast multi-domain social,Core social; dual justice residual,3,6.5,4,5.05,Publish dual justice/VL path,seed,,tick228
lb_posthof_1_27m,Buurtwerk Posthof 1.27m 2026,Flanders,ops,Antwerpen>Social>Posthof,{POSTHOF_T},{POSTHOF_T},Strong MJP: digi 0.909 + sam 0.28 + SE 85k = 1.274m; digi spike 2026,strong,src_antwerp_mjp_2026_youth_nominatief,Neighbourhood residents,Community work + digi project,Core community; digi L5 residual,3,6.5,4,5.05,Publish digi project L5,seed,,tick228
lb_antwerp_youth_social_9_20m,Antwerp youth social L5 sample 4 orgs 9.20m 2026,Flanders,ops,Antwerpen>Jeugd>L5_sample,{SAMPLE},{SAMPLE},Strong MJP sum Kras 4.26 + JES 2.39 + Elegast 1.28 + Posthof 1.27 = 9.20m; combined social 8 orgs ~30.23m,strong,src_antwerp_mjp_2026_youth_nominatief,Youth vulnerable residents,City youth social third-party sample,Core social; residual BAZZZ etc; dual VL,5,8.0,5,6.5,Publish BAZZZ residual open register,seed,,tick228
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_kras_4_26m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_220,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp social youth JES Kras Elegast Posthof nominatief FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:35:00Z,,'
    '"Spawned tick227 after CAW 16.92m social sample 21.01m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_220,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp social youth JES Kras Elegast Posthof nominatief FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:35:00Z,2026-07-29T01:55:00Z,'
    f'"tick228: Kras 4.26m JES 2.39m Elegast 1.28m Posthof 1.27m youth sample 9.20m combined social 30.23m; Mons FOI; spawn rq_221"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_221,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons BI2026 Antwerp residual social BAZZZ Axi or utilities SOE FPS taxex other large FOI-adjacent) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:55:00Z,,'
        '"Spawned tick228 after youth sample 9.20m combined social 30.23m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_220")
    print(repr(text[i : i + 300]) if i >= 0 else "missing")

# --- foi ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
oldn = (
    "tick140+204+213-227: culture+Digipolis+CAW full 16.92m social sample 21.01m filled; "
    "residual register project L5 inside CAW Mons BI2026 dual VL human send"
)
newn = (
    "tick140+204+213-228: culture Digipolis CAW+youth social 8 orgs ~30.23m filled; "
    "residual register project L5 Mons BI2026 dual VL human send"
)
if oldn in ft:
    foi.write_text(ft.replace(oldn, newn), encoding="utf-8")
    print("foi ok")
else:
    import re

    lines = ft.splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("gap_antwerp_subsidies_top20,") and "tick140" in line:
            line = (
                re.sub(
                    r"tick140.*$",
                    "tick140+204+213-228: social+youth 8 orgs ~30.23m; residual register Mons dual VL human send",
                    line.rstrip("\n\r"),
                )
                + ("\n" if line.endswith("\n") else "")
            )
            print("foi loose")
        out.append(line)
    foi.write_text("".join(out), encoding="utf-8")

# --- state ---
(data / "loop_state.csv").write_text(
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T01:55:00Z,rq_220,228,no,"
    '"Scheduler 60s. Next prio5 rq_221; tick230 progress due; rq_116 SWA deferred. '
    'FOI ready human send. tick228 Kras 4.26 JES 2.39 youth sample 9.20m combined 30.23m."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = f"""
### 2026-07-29T01:55:00Z - tick 228
- Unit: **rq_220** (FOI-adjacent hole-fill - **JES + Kras + Elegast + Posthof** youth/social MJP)
- Found (strong MJP nominatief):
  - **Kras Jeugdwerk 2026 EUR 4.260m** (jeugd 3.95 + sport 0.27 + veil 40k).
  - **JES 2026 EUR 2.386m** (jeugd 2.35 + veil 36.4k).
  - **Elegast 2026 EUR 1.278m** (veil 0.533 + onderw 0.41 + sam 0.28 + digi 55k).
  - **Buurtwerk Posthof 2026 EUR 1.274m** (digi 0.909 spike + sam 0.28 + SE 85k).
  - Youth/social sample **4 orgs EUR 9.199m**; combined with tick227 social **8 orgs ~EUR 30.23m**.
  - Mons BI2026 still not public (FOI ready).
- Wrote: sources 1; budgets 8; cmt 5; lb 5; foi note; rq_220=done; seeded **rq_221**.
- FOI: register project L5 + Mons BI2026 + dual VL human send.
- Next: prio5 **rq_221**; **tick 230 progress coverage** due; deferred **rq_116** SWA.
"""
if "tick 228" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick228 sample", SAMPLE, "combined", COMBINED)
