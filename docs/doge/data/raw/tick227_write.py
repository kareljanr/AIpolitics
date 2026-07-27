# tick227: Antwerp MJP social L5 — full CAW + ADIC + Free Clinic + VAGGA
from pathlib import Path

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# Strong MJP nominatief 2026
CAW = {
    "gezondheid": 110000.00,
    "sociale": 12684459.99,
    "samenleving": 171148.00,
    "onderwijs": 520367.00,
    "veiligheid": 3429991.10,
}
CAW_TOTAL = sum(CAW.values())  # 16915966.09
ADIC = 735034.87
FREE_CLINIC = 2435715.20
VAGGA = {
    "sociale": 836950.81,
    "sociale_economie": 31826.24,
    "veiligheid": 76172.58,
}
VAGGA_TOTAL = sum(VAGGA.values())  # 944949.63
SOCIAL_SAMPLE = CAW_TOTAL + ADIC + FREE_CLINIC + VAGGA_TOTAL

# --- sources ---
src = data / "sources.csv"
# reuse existing mjp source if present else add social extract note
src_add = (
    "src_antwerp_mjp_2026_social_nominatief,Antwerp MJP 2026 nominatief social L5 CAW ADIC FreeClinic VAGGA,"
    "https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Stad Antwerpen MJP 2026-2031 GR Dec 2025,2026-07-29,official_budget,"
    f'"CAW total {CAW_TOTAL:.2f} (soc 12.684m + veil 3.430m + onderw 0.520m + sam 0.171m + gez 0.110m); '
    f'ADIC 0.735m; FreeClinic 2.436m; VAGGA 0.945m; tick227"\n'
)
text = src.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_antwerp_mjp_2026_social_nominatief" not in text:
    src.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud = data / "budgets.csv"
rows = [
    f"bud_caw_mjp_total_2026,city_antwerpen,2026,{CAW_TOTAL},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,CAW Antwerpen full MJP nominatief package 16.916m 2026 (5 domains)",
    f"bud_caw_mjp_sociale_2026,city_antwerpen,2026,{CAW['sociale']},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,CAW MJP sociale zaken 12.684m 2026",
    f"bud_caw_mjp_veiligheid_2026,city_antwerpen,2026,{CAW['veiligheid']},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,CAW MJP veiligheid 3.430m 2026",
    f"bud_caw_mjp_onderwijs_2026,city_antwerpen,2026,{CAW['onderwijs']},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,CAW MJP onderwijs 0.520m 2026",
    f"bud_caw_mjp_samenleving_2026,city_antwerpen,2026,{CAW['samenleving']},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,CAW MJP samenlevingsopbouw 0.171m 2026",
    f"bud_caw_mjp_gezondheid_2026,city_antwerpen,2026,{CAW['gezondheid']},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,CAW MJP gezondheidszorg 0.110m 2026",
    f"bud_adic_2026,city_antwerpen,2026,{ADIC},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,ADIC drug intervention centre 0.735m 2026 MJP",
    f"bud_freeclinic_mjp_total_2026,city_antwerpen,2026,{FREE_CLINIC},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,Free Clinic full MJP sociale 2.436m 2026 (broader than drug ebesluit 0.97m)",
    f"bud_vagga_total_2026,city_antwerpen,2026,{VAGGA_TOTAL},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,VAGGA ambulatory mental health package 0.945m 2026",
    f"bud_vagga_sociale_2026,city_antwerpen,2026,{VAGGA['sociale']},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,VAGGA sociale zaken 0.837m 2026",
    f"bud_antwerp_social_l5_sample_2026,city_antwerpen,2026,{SOCIAL_SAMPLE},,,budgeted,src_antwerp_mjp_2026_social_nominatief,strong,Social L5 sample CAW+ADIC+FreeClinic+VAGGA 21.031m 2026",
]
text = bud.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_caw_mjp_total_2026" not in text:
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
    "cmt_caw_mjp_full_2026_31,CAW Antwerpen full city MJP nominatief multi-year,"
    "city_antwerpen,CAW Antwerpen vzw,MJP 2026-2031 nominatief 5 domains,"
    "2025-12-15,2026,2031,16915966.09,"
    '"{""2026_total"":16915966.09,""2026_sociale"":12684459.99,""2026_veiligheid"":3429991.10,'
    '""2026_onderwijs"":520367.00,""2026_samenleving"":171148.00,""2026_gezondheid"":110000.00,'
    '""prior_ebesluit_sample"":2273441.66,""note"":""Strong MJP full package; prior Kwadraat+Parkours 2.27m is subset of project locks inside/alongside; dual VL CAW residual; core social not pure waste""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "City CAW full safety-net financing,Publish project L5 inside 12.7m social line; dual VL CAW,"
    "src_antwerp_mjp_2026_social_nominatief,strong,Antwerpen>CAW>full,tick227\n"
    "cmt_adic_2026_31,ADIC Antwerp drug intervention multi-year MJP,"
    "city_antwerpen,Antwerps Drug Interventie Centrum vzw,MJP nominatief sociale,"
    "2025-12-15,2026,2031,735034.87,"
    '"{""2026"":735034.87,""2027"":749735.57,""2028"":764730.28,""2029"":780024.88,'
    '""2030"":795625.38,""2031"":811537.89,""note"":""Strong MJP; harm-reduction dual FreeClinic""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Drug intervention demand reduction,Publish dual FreeClinic/federal MSOC path,"
    "src_antwerp_mjp_2026_social_nominatief,strong,Antwerpen>Social>ADIC,tick227\n"
    "cmt_freeclinic_mjp_2026_31,Free Clinic full MJP sociale package multi-year,"
    "city_antwerpen,Free Clinic vzw,MJP nominatief sociale zaken,"
    "2025-12-15,2026,2031,2435715.20,"
    '"{""2026"":2435715.20,""2027"":2491229.50,""2028"":2547854.10,""2029"":2605611.18,'
    '""2030"":2664523.40,""2031"":2724613.87,""ebesluit_drug_subset_2026"":974381.30,'
    '""note"":""Strong MJP full 2.436m; ebesluit drug MSOC/GoiA/Nomaad 0.974m is subset""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Free Clinic full city social financing,Publish residual lines beyond drug package,"
    "src_antwerp_mjp_2026_social_nominatief,strong,Antwerpen>Social>FreeClinic,tick227\n"
    "cmt_vagga_2026_31,VAGGA ambulatory mental health multi-year MJP,"
    "city_antwerpen,VAGGA vzw,MJP nominatief social+econ+veiligheid,"
    "2025-12-15,2026,2031,944949.63,"
    '"{""2026_total"":944949.63,""2026_sociale"":836950.81,""2026_sociale_economie"":31826.24,'
    '""2026_veiligheid"":76172.58,""note"":""Strong MJP; dual care/safety domains""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Ambulatory mental health city financing,Publish outcome KPIs dual federal GGZ,"
    "src_antwerp_mjp_2026_social_nominatief,strong,Antwerpen>Social>VAGGA,tick227\n"
    "cmt_antwerp_social_l5_sample_2026,Antwerp social L5 sample CAW ADIC FreeClinic VAGGA 2026,"
    "city_antwerpen,CAW ADIC FreeClinic VAGGA,MJP nominatief,"
    "2025-12-15,2026,2026,21012665.79,"
    '"{""caw"":16915966.09,""adic"":735034.87,""freeclinic"":2435715.20,""vagga"":944949.63,'
    '""sample_sum"":21012665.79,""note"":""Strong 4-org social sample; residual JES Kras Elegast Posthof etc large youth/social still open""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "City social third-party L5 transparency sample,Publish JES Kras Elegast next; open register,"
    "src_antwerp_mjp_2026_social_nominatief,strong,Antwerpen>Social>L5_sample,tick227\n"
)
text = cmt.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_caw_mjp_full_2026_31" not in text:
    cmt.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb = data / "leaderboard.csv"
lb_add = f"""lb_caw_mjp_16_92m,CAW Antwerpen full MJP package 16.92m 2026,Flanders,ops,Antwerpen>CAW>full,{CAW_TOTAL},{CAW_TOTAL},Strong MJP: sociale 12.68 + veiligheid 3.43 + onderwijs 0.52 + samenleving 0.17 + gezondheid 0.11 = 16.92m; prior ebesluit sample 2.27m subset,strong,src_antwerp_mjp_2026_social_nominatief,Vulnerable youth homeless families neighbourhoods,City CAW full safety-net financing,Core social duty not pure waste; dual VL residual; L5 project split inside 12.7m residual,4,8.5,5,6.55,Publish project L5 inside social line; dual VL CAW,seed,,tick227
lb_adic_0_74m,ADIC Antwerp drug intervention 0.74m 2026,Flanders,ops,Antwerpen>Social>ADIC,{ADIC},811537.89,Strong MJP 735k 2026 path to 812k; dual FreeClinic,strong,src_antwerp_mjp_2026_social_nominatief,People who use drugs neighbourhoods,Drug intervention centre,Core harm-reduction not pure waste,3,6.5,4,5.05,Publish dual FreeClinic/federal path,seed,,tick227
lb_freeclinic_mjp_2_44m,Free Clinic full MJP 2.44m 2026,Flanders,ops,Antwerpen>Social>FreeClinic,{FREE_CLINIC},2724613.87,Strong MJP 2.436m 2026; ebesluit drug subset 0.974m; path to 2.72m,strong,src_antwerp_mjp_2026_social_nominatief,People who use drugs families,Free Clinic full city social package,Core social; residual lines beyond drug package,3,7.0,4,5.3,Publish residual line split vs drug ebesluit,seed,,tick227
lb_vagga_0_94m,VAGGA ambulatory mental health 0.94m 2026,Flanders,ops,Antwerpen>Social>VAGGA,{VAGGA_TOTAL},{VAGGA_TOTAL},Strong MJP: sociale 0.837 + SE 0.032 + veil 0.076 = 0.945m,strong,src_antwerp_mjp_2026_social_nominatief,People with mental health needs,Ambulatory GGZ city financing,Core care not pure waste; dual federal residual,3,6.5,4,5.05,Publish dual federal GGZ path,seed,,tick227
lb_antwerp_social_l5_21m,Antwerp social L5 sample 4 orgs 21.01m 2026,Flanders,ops,Antwerpen>Social>L5_sample,{SOCIAL_SAMPLE},{SOCIAL_SAMPLE},Strong MJP sum CAW 16.92 + FreeClinic 2.44 + VAGGA 0.94 + ADIC 0.74 = 21.01m,strong,src_antwerp_mjp_2026_social_nominatief,Vulnerable residents youth homeless,City social third-party sample,Core social; residual JES Kras Elegast large youth packages,5,8.0,5,6.5,Publish JES Kras Elegast; open register,seed,,tick227
"""
text = lb.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_caw_mjp_16_92m" not in text:
    lb.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- research_queue ---
rq = data / "research_queue.csv"
text = rq.read_text(encoding="utf-8")
old = (
    'rq_219,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp social L5 ebesluit CAW ADIC large nominatief FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:15:00Z,,'
    '"Spawned tick226 after Digipolis member matrix 245m; rq_116 SWA deferred Oct-Dec 2026"'
)
new = (
    'rq_219,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp social L5 ebesluit CAW ADIC large nominatief FPS taxex other large FOI-adjacent SOEs utilities) "
    'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:15:00Z,2026-07-29T01:35:00Z,'
    f'"tick227: CAW full MJP 16.92m + FreeClinic 2.44 + VAGGA 0.94 + ADIC 0.74 = social sample 21.01m; Mons still FOI; spawn rq_220"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_220,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons BI2026 Antwerp social youth JES Kras Elegast Posthof nominatief FPS taxex other large FOI-adjacent SOEs utilities) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T01:35:00Z,,'
        '"Spawned tick227 after CAW 16.92m social sample 21.01m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq fail")
    i = text.find("rq_219")
    print(repr(text[i : i + 300]) if i >= 0 else "missing")

# --- foi ---
foi = data / "foi_queue.csv"
ft = foi.read_text(encoding="utf-8")
oldn = (
    "tick140+204+213-226: culture 16/16 + Digipolis AGB 245.6m personnel + member matrix 245.07m filled; "
    "residual register project L5 Mons BI2026 dual VL human send"
)
newn = (
    "tick140+204+213-227: culture+Digipolis+CAW full 16.92m social sample 21.01m filled; "
    "residual register project L5 inside CAW Mons BI2026 dual VL human send"
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
                    "tick140+204+213-227: CAW 16.92m social sample 21m; residual CAW project L5 Mons dual VL human send",
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
    "main,continuous,hole_fill,2026-07-29T01:35:00Z,rq_219,227,no,"
    '"Scheduler 60s. Next prio5 rq_220 JES/Kras/Mons; rq_116 SWA deferred. '
    'FOI ready human send. tick227 CAW 16.92m social sample 21.01m."\n',
    encoding="utf-8",
)
print("state ok")

# --- log ---
log = root / "docs/doge/loop_log.md"
lt = log.read_text(encoding="utf-8", errors="replace")
entry = f"""
### 2026-07-29T01:35:00Z - tick 227
- Unit: **rq_219** (FOI-adjacent hole-fill - **Antwerp social L5 MJP full CAW + ADIC + FreeClinic + VAGGA**)
- Found (strong MJP nominatief):
  - **CAW Antwerpen full package 2026 EUR 16.916m**: sociale **12.684m** + veiligheid **3.430m** + onderwijs **0.520m** + samenleving **0.171m** + gezondheid **0.110m** (prior ebesluit Kwadraat+Parkours 2.27m is subset).
  - **Free Clinic MJP EUR 2.436m** (broader than drug ebesluit subset 0.974m).
  - **VAGGA EUR 0.945m** (sociale 0.837 + SE 0.032 + veil 0.076).
  - **ADIC EUR 0.735m** 2026 (path to 0.812m 2031).
  - Social L5 sample **4 orgs EUR 21.013m** 2026.
  - Residual large youth: JES ~2.39m, Kras ~4.26m, Elegast ~1.28m (next tick); Mons BI2026 still FOI.
- Wrote: sources 1; budgets 11; cmt 5; lb 5; foi note; rq_219=done; seeded **rq_220**.
- FOI: CAW project L5 inside 12.7m + Mons BI2026 + dual VL + register human send.
- Next: prio5 **rq_220**; deferred **rq_116** SWA.
"""
if "tick 227" not in lt:
    log.write_text(lt.rstrip() + "\n" + entry, encoding="utf-8", newline="\n")
    print("log ok")
else:
    print("log already")

print("DONE tick227 CAW", CAW_TOTAL, "sample", SOCIAL_SAMPLE)
