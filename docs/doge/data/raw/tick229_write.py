# tick229: Antwerp MJP residual social/equality — BAZZZ Axi BattleDroids ATK VVS Unik GAMS
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

BAZZZ = {"gelijke": 90000.00, "jeugd": 315000.00}
BAZZZ_T = sum(BAZZZ.values())  # 405000
AXI = 155000.00
BATTLE = 163000.00
ATK = 262658.91
VVS = 400000.00
UNIK = 120000.00
GAMS = {"sociale": 8611.83, "gelijke": 42000.00}
GAMS_T = sum(GAMS.values())  # 50611.83
SAMPLE = BAZZZ_T + AXI + BATTLE + ATK + VVS + UNIK + GAMS_T  # 1556270.74
PRIOR8 = 30230244.36
COMBINED15 = PRIOR8 + SAMPLE  # ~31.79m class (additive orgs)

# --- sources ---
src = data / "sources.csv"
src_add = (
    "src_antwerp_mjp_2026_social_residual,Antwerp MJP 2026 residual social equality nominatief,"
    "https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Stad Antwerpen MJP 2026-2031 GR Dec 2025,2026-07-29,official_budget,"
    f'"BAZZZ {BAZZZ_T:.0f} Axi {AXI:.0f} BattleDroids {BATTLE:.0f} ATK {ATK:.2f} VVS {VVS:.0f} '
    f'Unik {UNIK:.0f} GAMS {GAMS_T:.2f} sample {SAMPLE:.2f}; tick229"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_antwerp_mjp_2026_social_residual" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_bazzz_total_2026,city_antwerpen,2026,{BAZZZ_T},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,BAZZZ package 405k 2026 (gelijke 90k + jeugd 315k)",
    f"bud_axi_2026,city_antwerpen,2026,{AXI},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,Axi vzw gelijke kansen 155k 2026",
    f"bud_battle_droids_2026,city_antwerpen,2026,{BATTLE},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,Battle Droids Factory youth 163k 2026",
    f"bud_armen_te_kort_2026,city_antwerpen,2026,{ATK},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,Armen Te Kort poverty support 262.7k 2026",
    f"bud_vvs_2026,city_antwerpen,2026,{VVS},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,VVS gezondheidszorg 400k 2026",
    f"bud_buurthuis_unik_2026,city_antwerpen,2026,{UNIK},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,Buurthuis Unik samenleving 120k 2026",
    f"bud_gams_total_2026,city_antwerpen,2026,{GAMS_T},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,GAMS package 50.6k 2026 (sociale 8.6k + gelijke 42k)",
    f"bud_antwerp_social_residual_sample_2026,city_antwerpen,2026,{SAMPLE},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,Residual social/equality sample 7 orgs 1.556m 2026",
    f"bud_antwerp_social_youth_15org_2026,city_antwerpen,2026,{COMBINED15},,,budgeted,src_antwerp_mjp_2026_social_residual,strong,Combined social+youth sample ~15 orgs 31.79m 2026 class",
]
text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_bazzz_total_2026" not in text:
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
    "cmt_bazzz_2026_31,BAZZZ multi-year MJP gelijke kansen+jeugd,"
    "city_antwerpen,BAZZZ vzw,MJP nominatief,"
    "2025-12-15,2026,2031,405000,"
    '"{""2026_total"":405000,""2026_gelijke"":90000,""2026_jeugd"":315000,'
    '""jeugd_path"":[315000,320040,325160.64,330363.21,335649.02,341019.41],'
    '""note"":""Strong MJP; youth+equality dual""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Youth equality BAZZZ financing,Publish dual VL residual,"
    "src_antwerp_mjp_2026_social_residual,strong,Antwerpen>Social>BAZZZ,tick229\n"
    "cmt_axi_2026_31,Axi gelijke kansen multi-year MJP,"
    "city_antwerpen,Axi vzw,MJP nominatief gelijke kansen,"
    "2025-12-15,2026,2031,155000,"
    '"{""2026"":155000,""2027"":157480,""2028"":159999.68,""2029"":162559.68,'
    '""2030"":165160.63,""2031"":167803.20,""note"":""Strong MJP equality body residual""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Equality Axi city financing,Publish outcome KPIs,"
    "src_antwerp_mjp_2026_social_residual,strong,Antwerpen>Social>Axi,tick229\n"
    "cmt_battle_droids_2026_31,Battle Droids Factory youth multi-year MJP,"
    "city_antwerpen,Battle Droids Factory vzw,MJP nominatief jeugd,"
    "2025-12-15,2026,2031,163000,"
    '"{""2026"":163000,""2027"":165608,""2028"":168257.73,""2029"":170949.85,'
    '""2030"":173685.05,""2031"":176464.01,""note"":""Strong MJP youth STEM/maker""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Youth maker Battle Droids financing,Publish dual residual,"
    "src_antwerp_mjp_2026_social_residual,strong,Antwerpen>Jeugd>BattleDroids,tick229\n"
    "cmt_armen_te_kort_2026_31,Armen Te Kort poverty multi-year MJP,"
    "city_antwerpen,Armen Te Kort vzw,MJP nominatief sociale,"
    "2025-12-15,2026,2031,262658.91,"
    '"{""2026"":262658.91,""2027"":238144.08,""2028"":242906.96,""2029"":247765.11,'
    '""2030"":252720.41,""2031"":257774.81,""note"":""Strong MJP; 2026 spike vs later years""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Poverty support Armen Te Kort,Publish dual federal residual,"
    "src_antwerp_mjp_2026_social_residual,strong,Antwerpen>Social>ATK,tick229\n"
    "cmt_vvs_2026_31,VVS gezondheidszorg multi-year MJP,"
    "city_antwerpen,Vereniging voor Solidariteit vzw,MJP nominatief gezondheid,"
    "2025-12-15,2026,2031,400000,"
    '"{""2026"":400000,""2027"":406800,""2028"":413715.60,""2029"":420748.77,'
    '""2030"":427901.49,""2031"":435175.82,""note"":""Strong MJP health solidarity""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Health solidarity VVS financing,Publish dual residual,"
    "src_antwerp_mjp_2026_social_residual,strong,Antwerpen>Social>VVS,tick229\n"
    f"cmt_antwerp_social_residual_sample_2026,Antwerp residual social equality sample 7 orgs 2026,"
    f"city_antwerpen,BAZZZ Axi BattleDroids ATK VVS Unik GAMS,MJP nominatief,"
    f"2025-12-15,2026,2026,{SAMPLE},"
    f'"{{""bazzz"":{BAZZZ_T},""axi"":{AXI},""battle_droids"":{BATTLE},""atk"":{ATK},'
    f'""vvs"":{VVS},""unik"":{UNIK},""gams"":{GAMS_T},""sample_sum"":{SAMPLE},'
    f'""prior_8orgs"":{PRIOR8},""combined_class"":{COMBINED15},'
    f'""note"":""Strong residual mid-tier social/equality; combined with prior 8 orgs ~31.79m class; Mons FOI""}}",'
    f"0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    f"City residual social equality L5 sample,Open Gent-style register; Mons BI2026,"
    f"src_antwerp_mjp_2026_social_residual,strong,Antwerpen>Social>residual_sample,tick229\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_bazzz_2026_31" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = f"""lb_bazzz_0_41m,BAZZZ youth+equality 405k 2026,Flanders,ops,Antwerpen>Social>BAZZZ,{BAZZZ_T},{BAZZZ_T},Strong MJP: jeugd 315k + gelijke 90k = 405k,strong,src_antwerp_mjp_2026_social_residual,Youth equality audiences,BAZZZ dual youth equality,Core social mid-tier,2,5.5,3,4.15,Publish dual VL,seed,,tick229
lb_vvs_0_40m,VVS gezondheidszorg 400k 2026,Flanders,ops,Antwerpen>Social>VVS,{VVS},435175.82,Strong MJP 400k 2026 path to 435k,strong,src_antwerp_mjp_2026_social_residual,Health solidarity beneficiaries,VVS health financing,Core care mid-tier,2,5.5,3,4.15,Publish dual residual,seed,,tick229
lb_antwerp_social_residual_1_56m,Antwerp residual social equality sample 1.56m 2026,Flanders,ops,Antwerpen>Social>residual_sample,{SAMPLE},{SAMPLE},Strong MJP 7 orgs 1.556m; combined social+youth class ~31.79m with prior 8 orgs,strong,src_antwerp_mjp_2026_social_residual,Vulnerable residents youth,City residual social equality sample,Core social mid-tier batch; register residual,4,7.0,4,5.5,Open register Mons BI2026,seed,,tick229
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_bazzz_0_41m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_221,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp residual social BAZZZ Axi or utilities SOE FPS taxex other large FOI-adjacent) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:55:00Z,,'
    '"Spawned tick228 after youth sample 9.20m combined social 30.23m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_221,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp residual social BAZZZ Axi or utilities SOE FPS taxex other large FOI-adjacent) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:55:00Z,2026-07-29T02:15:00Z,'
    f'"tick229: BAZZZ 405k VVS 400k residual social sample 1.56m combined ~31.79m; Mons FOI; spawn rq_222; tick230 progress due"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_222,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons BI2026 utilities SOE FPS taxex other large FOI-adjacent programmes) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T02:15:00Z,,'
        '"Spawned tick229 after residual social 1.56m; tick230 progress; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_221")
    print(repr(text[i : i + 300]) if i >= 0 else "missing")

# --- foi ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
oldn = (
    "tick140+204+213-228: culture Digipolis CAW+youth social 8 orgs ~30.23m filled; "
    "residual register project L5 Mons BI2026 dual VL human send"
)
newn = (
    "tick140+204+213-229: culture Digipolis social+youth ~15 orgs ~31.79m filled; "
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
                    "tick140+204+213-229: social+youth ~15 orgs ~31.79m; residual register Mons dual VL human send",
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
    "main,continuous,hole_fill,2026-07-29T02:15:00Z,rq_221,229,no,"
    '"Scheduler 60s. NEXT tick230 MANDATORY progress coverage % + waste top10; then rq_222. '
    'rq_116 SWA deferred. FOI ready human send. tick229 residual social 1.56m combined ~31.79m."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = f"""
### 2026-07-29T02:15:00Z - tick 229
- Unit: **rq_221** (FOI-adjacent hole-fill - residual social/equality **BAZZZ Axi BattleDroids ATK VVS Unik GAMS**)
- Found (strong MJP nominatief):
  - **BAZZZ EUR 405k** (jeugd 315 + gelijke 90).
  - **VVS EUR 400k** gezondheid; **Axi EUR 155k**; **Battle Droids EUR 163k**.
  - **Armen Te Kort EUR 262.7k**; **Buurthuis Unik EUR 120k**; **GAMS EUR 50.6k**.
  - Residual sample **7 orgs EUR 1.556m**; combined social+youth class **~EUR 31.79m** (~15 orgs with prior).
  - Mons BI2026 still not public (FOI ready).
- Wrote: sources 1; budgets 9; cmt 6; lb 3; foi note; rq_221=done; seeded **rq_222**.
- FOI: register + Mons BI2026 + dual VL human send.
- Next: **tick 230 mandatory progress coverage % + waste top10**; then prio5 **rq_222**; deferred **rq_116** SWA.
"""
if "tick 229" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick229 sample", SAMPLE, "combined", COMBINED15)
