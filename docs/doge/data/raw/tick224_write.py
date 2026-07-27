# tick224: complete residual 16 culture partners DeRoma Trix DeStudio AntwerpArt
from pathlib import Path
import re

root = Path(r"C:\Users\karel\dev\AIpolitics")
data = root / "docs/doge/data"

# --- sources ---
src_path = data / "sources.csv"
src_add = (
    'src_antwerp_mjp_2026_werk_nominatief,Antwerp MJP 2026-2031 toegestane werkingssubsidies nominatief table,'
    "https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,Stad Antwerpen MJP 2026-2031 GR Dec 2025,"
    '2026-07-29,official_budget,"Nominatief culture/youth L5: De Roma 936k Trix cult 355k+jeugd 350k De Studio 153k '
    'Antwerp Art 97.5k + path 2026-31; tick224"\n'
    "src_ebesluit_destudio_2026,Antwerp De Studio Villanella nominatief 2026-2031 college lock,"
    "https://ebesluit.antwerpen.be/zittingen/25.0115.8579.8154/agendapunten/25.1218.7646.2534,"
    'Stad Antwerpen college 19 Dec 2025,2026-07-29,official_decision,"De Studio 153k 2026; max 940.188 2026-31; '
    'OO cash-by-year match MJP; tick224"\n'
)
text = src_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "src_antwerp_mjp_2026_werk_nominatief" not in text:
    src_path.write_text(text + src_add, encoding="utf-8")
    print("sources ok")
else:
    print("sources already")

# --- budgets ---
bud_path = data / "budgets.csv"
bud_add = """bud_deroma_2026,city_antwerpen,2026,936000,,,budgeted,src_antwerp_mjp_2026_werk_nominatief,strong,De Roma vzw culture werk 936k 2026 MJP nominatief (college lock Jun2026 postponed)
bud_trix_culture_2026,city_antwerpen,2026,355000,,,budgeted,src_antwerp_mjp_2026_werk_nominatief,strong,Trx/Trix vzw culture werk 355k 2026 MJP
bud_trix_youth_2026,city_antwerpen,2026,350000,,,budgeted,src_antwerp_mjp_2026_werk_nominatief,strong,Trx/Trix vzw youth werk 350k 2026 MJP
bud_trix_package_2026,city_antwerpen,2026,705000,,,budgeted,src_antwerp_mjp_2026_werk_nominatief,strong,Trx/Trix package 705k 2026 (culture 355 + youth 350)
bud_destudio_2026,city_antwerpen,2026,153000,,,budgeted,src_ebesluit_destudio_2026,strong,De Studio Villanella culture 153k 2026 college+MJP
bud_antwerp_art_2026,city_antwerpen,2026,97500,,,budgeted,src_antwerp_mjp_2026_werk_nominatief,strong,Antwerp Art vzw culture 97.5k 2026 MJP
bud_antwerp_culture_l5_sample_16houses_2026,city_antwerpen,2026,14583700,,,budgeted,src_antwerp_mjp_2026_werk_nominatief,strong,Culture L5 sample 16/16 houses complete 14.584m of ~35m envelope (~41.7pct)
"""
text = bud_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "bud_deroma_2026" not in text:
    bud_path.write_text(text + bud_add, encoding="utf-8")
    print("budgets ok")
else:
    print("budgets already")

# --- commitments ---
cmt_path = data / "commitments.csv"
cmt_add = (
    'cmt_deroma_2026_31,De Roma culture multi-year MJP path,city_antwerpen,De Roma vzw,'
    "MJP 2026-2031 nominatief werkingssubsidies,2025-12-15,2026,2031,5751744,"
    '"{""2026"":936000,""2027"":950976,""2028"":966192,""2029"":966192,""2030"":966192,""2031"":966192,'
    '""max_6y"":5751744,""note"":""Strong MJP; college vastlegging Jun2026 postponed Verdaagd; dual VL residual""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Culture house concertzaal Borgerhout,Publish college lock when re-tabled; dual VL,"
    "src_antwerp_mjp_2026_werk_nominatief,strong,Antwerpen>Cultuur>DeRoma,tick224\n"
    "cmt_trix_2026_31,Trix youth music centre multi-year MJP path,city_antwerpen,Trx vzw (Trix),"
    "MJP 2026-2031 nominatief culture+youth,2025-12-15,2026,2031,4367298,"
    '"{""2026_package"":705000,""2026_culture"":355000,""2026_youth"":350000,""culture_6y"":2181484,'
    '""youth_6y"":2185814,""max_6y_class"":4367298,'
    '""note"":""Strong MJP Trx vzw; dual culture+youth like FAMEUS; college separate residual""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Youth music centre Borgerhout,Publish college lock; dual VL,"
    "src_antwerp_mjp_2026_werk_nominatief,strong,Antwerpen>Cultuur>Trix,tick224\n"
    "cmt_destudio_2026_31,De Studio Villanella multi-year city support,city_antwerpen,"
    "Kunstencentrum De Studio - Villanella vzw,College 19 Dec 2025 + OO + MJP,2025-12-19,2026,2031,940188,"
    '"{""2026"":153000,""2027"":155448,""2028"":157935,""2029"":157935,""2030"":157935,""2031"":157935,'
    '""max_6y"":940188,""note"":""Strong ebesluit college+OO cash-by-year; dual VL Kunstendecreet residual; '
    'youth 0-30 arts""}",0,active,'
    "https://ebesluit.antwerpen.be/zittingen/25.0115.8579.8154/agendapunten/25.1218.7646.2534,"
    "Youth arts house culture partner,Publish dual VL grant,"
    "src_ebesluit_destudio_2026,strong,Antwerpen>Cultuur>DeStudio,tick224\n"
    "cmt_antwerp_art_2026_31,Antwerp Art Weekend multi-year MJP path,city_antwerpen,Antwerp Art vzw,"
    "MJP 2026-2031 nominatief,2025-12-15,2026,2031,599140,"
    '"{""2026"":97500,""2027"":99060,""2028"":100645,""2029"":100645,""2030"":100645,""2031"":100645,'
    '""max_6y"":599140,""note"":""Strong MJP; on 16-partner list as AntwerpArtWeekend class""}",'
    "0,active,https://ebesluit.antwerpen.be/document/69247909a60702536ea8b438,"
    "Contemporary art weekend platform,Publish college lock if separate,"
    "src_antwerp_mjp_2026_werk_nominatief,strong,Antwerpen>Cultuur>AntwerpArt,tick224\n"
    "cmt_antwerp_culture_l5_sample_2026_v8,Antwerp culture L5 sample complete 16/16 houses 2026,"
    "city_antwerpen,16 flagship culture partners,College ebesluit + MJP nominatief,2025-12-15,2026,2026,14583700,"
    '"{""prior_12_houses"":12692200,""deroma_2026"":936000,""trix_package_2026"":705000,""destudio_2026"":153000,'
    '""antwerp_art_2026"":97500,""sample_sum"":14583700,""culture_envelope_medium"":35000000,'
    '""sample_share_pct_class"":41.7,""note"":""Strong complete 16/16 named partners; sample is city werk lines '
    'not full dual VL; envelope 35m medium; Digipolis personnel Mons residual separate""}",'
    "0,active,https://ebesluit.antwerpen.be/,City culture flagship L5 transparency ladder complete,"
    "Open Gent-style machine register; dual VL matrix,"
    "src_antwerp_mjp_2026_werk_nominatief,strong,Antwerpen>Cultuur>L5_sample,tick224\n"
)
text = cmt_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "cmt_deroma_2026_31" not in text:
    cmt_path.write_text(text + cmt_add, encoding="utf-8")
    print("commitments ok")
else:
    print("commitments already")

# --- leaderboard ---
lb_path = data / "leaderboard.csv"
lb_add = """lb_deroma_936k,De Roma culture house 936k 2026,Flanders,ops,Antwerpen>Cultuur>DeRoma,936000,5751744,Strong MJP nominatief 936k 2026 path to 966k; college lock postponed Jun2026; dual VL residual,strong,src_antwerp_mjp_2026_werk_nominatief,Concert audiences Borgerhout,Culture house concertzaal,Core culture not pure waste; large mid-tier house,3,6.5,4,5.05,Publish college lock; dual VL,seed,,tick224
lb_trix_705k,Trix youth music centre package 705k 2026,Flanders,ops,Antwerpen>Cultuur>Trix,705000,4367298,Strong MJP: culture 355k + youth 350k = 705k; 6y class ~4.37m,strong,src_antwerp_mjp_2026_werk_nominatief,Youth 12-26 music audiences,Youth music centre dual culture/youth,Core youth culture not pure waste,3,6.5,4,5.05,Publish college lock; dual VL,seed,,tick224
lb_destudio_153k,De Studio Villanella 153k 2026,Flanders,ops,Antwerpen>Cultuur>DeStudio,153000,940188,Strong ebesluit+OO: 153k 2026 max 940k/6y; dual VL residual,strong,src_ebesluit_destudio_2026,Youth 0-30 arts audiences,Youth arts house Kunstenpartner,Core culture not pure waste; smaller vs Toneelhuis/HETPALEIS,2,5.5,4,4.25,Publish dual VL grant,seed,,tick224
lb_antwerp_art_97k,Antwerp Art 97.5k 2026,Flanders,ops,Antwerpen>Cultuur>AntwerpArt,97500,599140,Strong MJP 97.5k 2026 path ~100.6k; 6y ~599k,strong,src_antwerp_mjp_2026_werk_nominatief,Art weekend visitors galleries,Contemporary art platform,Core culture small L5,2,5.0,3,3.7,Publish annual path,seed,,tick224
lb_antwerp_culture_l5_sample_14_58m,Antwerp culture L5 sample 16 houses 14.58m of 35m envelope,Flanders,ops,Antwerpen>Cultuur>L5_sample,14583700,35000000,Strong complete 16/16 houses 14.58m; envelope 35m medium; ~41.7pct class,strong,src_antwerp_mjp_2026_werk_nominatief,Culture houses festival audiences,City culture flagship transparency sample complete,Core culture; partial envelope; dual VL + Gent register residual,5,7.5,5,6.4,Open machine-readable register; dual VL matrix,seed,,tick224
"""
text = lb_path.read_text(encoding="utf-8")
if not text.endswith("\n"):
    text += "\n"
if "lb_deroma_936k" not in text:
    lb_path.write_text(text + lb_add, encoding="utf-8")
    print("leaderboard ok")
else:
    print("leaderboard already")

# --- research_queue ---
rq_path = data / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = (
    'rq_216,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp Digipolis 2026 personnel remaining culture DeRoma Trix DeStudio social L5 ebesluit FPS taxex "
    'other large FOI-adjacent SOEs utilities) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ",2026-07-29T00:15:00Z,,\"Spawned tick223 after HETPALEIS 3.41m culture sample 12.69m; rq_116 SWA deferred Oct-Dec 2026\""
)
new = (
    'rq_216,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills '
    "(Mons BI2026 Antwerp Digipolis 2026 personnel remaining culture DeRoma Trix DeStudio social L5 ebesluit FPS taxex "
    'other large FOI-adjacent SOEs utilities) if new PDFs appear; else next open rq; do not idle while public work remains.",'
    ",2026-07-29T00:15:00Z,2026-07-29T00:35:00Z,\"tick224: DeRoma 936k Trix 705k DeStudio 153k AAW 97.5k; culture sample "
    '16/16 complete 14.58m; residual Digipolis personnel Mons; spawn rq_217"'
)
if old in text:
    text = text.replace(old, new)
    if not text.endswith("\n"):
        text += "\n"
    text += (
        'rq_217,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills '
        "(Mons BI2026 Antwerp Digipolis 2026 personnel social L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) "
        'if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-29T00:35:00Z,,'
        '"Spawned tick224 after culture 16/16 complete 14.58m; rq_116 SWA deferred Oct-Dec 2026"\n'
    )
    rq_path.write_text(text, encoding="utf-8")
    print("rq ok")
else:
    print("rq not matched")
    idx = text.find("rq_216")
    print(repr(text[idx : idx + 400]) if idx >= 0 else "no rq_216")

# --- foi note ---
foi_path = data / "foi_queue.csv"
text = foi_path.read_text(encoding="utf-8")
old_note = (
    "tick140+204+213-223: AGB packages + culture sample 12 houses 12.69m (+HETPALEIS 3.41m); "
    "residual register Digipolis personnel Mons DeRoma Trix DeStudio dual VL human send"
)
new_note = (
    "tick140+204+213-224: AGB packages + culture sample 16/16 houses 14.58m complete; "
    "residual register Digipolis 2026 personnel Mons BI2026 dual VL human send"
)
if old_note in text:
    foi_path.write_text(text.replace(old_note, new_note), encoding="utf-8")
    print("foi ok")
else:
    # patch gap_antwerp line notes field more loosely
    lines = text.splitlines(keepends=True)
    out = []
    for line in lines:
        if line.startswith("gap_antwerp_subsidies_top20,") and "tick140" in line:
            line = re.sub(
                r"tick140.*$",
                "tick140+204+213-224: culture 16/16 14.58m complete; residual Digipolis personnel Mons dual VL human send",
                line.rstrip("\n\r"),
            ) + ("\n" if line.endswith("\n") else "")
            print("foi loose patch")
        out.append(line)
    foi_path.write_text("".join(out), encoding="utf-8")

# --- loop_state ---
state = (
    "state_id,mode,current_sprint,last_tick_utc,last_unit_id,ticks_completed,paused,notes\n"
    "main,continuous,hole_fill,2026-07-29T00:35:00Z,rq_216,224,no,"
    '"Scheduler 60s. Next prio5 rq_217 Digipolis/Mons/social; rq_116 SWA deferred. '
    'FOI ready human send. tick224 culture 16/16 complete 14.58m DeRoma 936k Trix 705k."\n'
)
(data / "loop_state.csv").write_text(state, encoding="utf-8")
print("state ok")

# --- loop_log ---
log_path = root / "docs/doge/loop_log.md"
log_entry = """
### 2026-07-29T00:35:00Z - tick 224
- Unit: **rq_216** (FOI-adjacent hole-fill - residual culture **DeRoma + Trix + DeStudio + Antwerp Art**)
- Found (strong primary):
  - **De Roma** MJP 2026 **EUR 936k** culture; 6y path **5.752m**; college vastlegging Jun2026 **Verdaagd** (MJP still budgeted).
  - **Trix (Trx vzw)** 2026 **EUR 705k** (culture 355 + youth 350); 6y class **~4.367m**.
  - **De Studio** ebesluit college 19 Dec 2025 **EUR 153k** 2026; max **940.188k** 2026-31 (OO cash-by-year = MJP).
  - **Antwerp Art** MJP 2026 **EUR 97.5k**; 6y **599.1k**.
  - Culture L5 sample **16/16 houses complete EUR 14.584m** of ~35m envelope (**~41.7%** class).
- Wrote: sources 2; budgets 7; cmt 5; lb 5; foi note; rq_216=done; seeded **rq_217**.
- FOI: Digipolis 2026 personnel + Mons BI2026 + dual VL residual + Gent-style register human send.
- Next: prio5 **rq_217**; deferred **rq_116** SWA.
"""
log_text = log_path.read_text(encoding="utf-8")
if "tick 224" not in log_text:
    log_path.write_text(log_text.rstrip() + "\n" + log_entry, encoding="utf-8")
    print("log ok")
else:
    print("log already")

print("DONE tick224")
