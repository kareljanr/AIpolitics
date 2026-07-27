# tick213: Digipolis Antwerpen city + PZA IT packages
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # docs/doge/data

def append(name: str, text: str) -> None:
    p = ROOT / name
    with p.open("a", encoding="utf-8", newline="\n") as f:
        if not text.endswith("\n"):
            text += "\n"
        f.write(text)

append(
    "sources.csv",
    """src_ebesluit_digipolis_2024,Antwerp Digipolis city werk+invest 2024 package,https://ebesluit.antwerpen.be/zittingen/23.0919.0800.9268/agendapunten/24.0122.7056.0669,Stad Antwerpen college 2 Feb 2024,2026-07-28,official_decision,"Werk 44.913m + invest 12.673m package 57.585m; personnel/contracts/cyber/LCM; tick213"
src_ebesluit_digipolis_2025_main,Antwerp Digipolis city werk+invest main 2025 Dec2024,https://ebesluit.antwerpen.be/zittingen/23.1017.8479.0217/agendapunten/24.1216.5294.6673,Stad Antwerpen college 20 Dec 2024,2026-07-28,official_decision,"Werk 46.346m + invest personnel 8.121m main 54.467m; index withhold 1.455m; tick213"
src_ebesluit_digipolis_2025_index,Antwerp Digipolis 2025 spilindex personnel delta Dec2025,https://ebesluit.antwerpen.be/zittingen/25.0115.8579.8154/agendapunten/25.1209.0732.0879,Stad Antwerpen college 19 Dec 2025,2026-07-28,official_decision,"+985.9k werk personnel +353.9k invest personnel index; tick213"
src_ebesluit_digipolis_2025_cyber,Antwerp Digipolis cyber versterking invest 2025,https://ebesluit.antwerpen.be/zittingen/25.0113.3127.5457/agendapunten/25.0325.7650.2405,Stad Antwerpen college 4 Apr 2025,2026-07-28,official_decision,"Cyber invest 19.395m incl 40.6k aftrekbare BTW; NIS2 project versterking; tick213"
src_ebesluit_digipolis_pza_2025,PZA Digipolis IT werk+invest package 2025,https://ebesluit.antwerpen.be/zittingen/24.0919.8839.0186/agendapunten/24.1216.4768.9273,Stad Antwerpen college 24 Jan 2025,2026-07-28,official_decision,"PZA Digipolis 53.092m (invest 33.878 + werk 19.214) + later +0.435m werk; tick213"
src_ebesluit_digipolis_pza_2025_extra,PZA Digipolis extra werkingskosten 2025 BW2025-1,https://ebesluit.antwerpen.be/zittingen/25.0113.4739.5953/agendapunten/25.0812.4138.9334,Stad Antwerpen college 12 Sep 2025,2026-07-28,official_decision,"+435456.01 werk; werk base to 19.649m class; tick213"
src_ebesluit_digipolis_2026_main,Antwerp Digipolis city werk+invest cameras 2026,https://ebesluit.antwerpen.be/zittingen/25.0916.4909.7689/agendapunten/26.0225.7520.4002,Stad Antwerpen college 6 Mar 2026,2026-07-28,official_decision,"Werk 37.750m (eigen+contracts+cam maint) + invest cam 1.064m = 38.814m; personnel residual vs 2025; tick213"
""",
)

append(
    "entities.csv",
    "digipolis_antwerpen,AG Digipolis Antwerpen,Digipolis Anvers,Antwerp municipal ICT AGB cost-sharing,parastatal,city_antwerpen,nl,https://www.digipolis.be,,,City IT AGB; 2025 city package class ~75.2m + PZA ~53.5m dual; 2024 city 57.6m; tick213\n",
)

append(
    "budgets.csv",
    """bud_digipolis_city_package_2024,city_antwerpen,2024,57585321.19,,,budgeted,src_ebesluit_digipolis_2024,strong,Digipolis city regular package 57.585m 2024 (werk 44.913 + invest 12.673)
bud_digipolis_city_werk_2024,city_antwerpen,2024,44912730.70,,,budgeted,src_ebesluit_digipolis_2024,strong,Digipolis city werk 44.913m 2024 (pers+eigen+contracts)
bud_digipolis_city_invest_2024,city_antwerpen,2024,12672590.49,,,budgeted,src_ebesluit_digipolis_2024,strong,Digipolis city invest general 12.673m 2024 (pers+cyber1.0+LCM)
bud_digipolis_city_main_2025,city_antwerpen,2025,54466529.70,,,budgeted,src_ebesluit_digipolis_2025_main,strong,Digipolis city main 54.467m 2025 (werk 46.346 + invest pers 8.121) pre-index pre-cyber
bud_digipolis_city_werk_2025,city_antwerpen,2025,46345778.05,,,budgeted,src_ebesluit_digipolis_2025_main,strong,Digipolis city werk main 46.346m 2025
bud_digipolis_city_invest_pers_2025,city_antwerpen,2025,8120751.65,,,budgeted,src_ebesluit_digipolis_2025_main,strong,Digipolis city invest personnel 8.121m 2025
bud_digipolis_city_index_delta_2025,city_antwerpen,2025,1339820.35,,,budgeted,src_ebesluit_digipolis_2025_index,strong,Digipolis spilindex delta 1.340m 2025 (werk 0.986 + invest 0.354)
bud_digipolis_city_cyber_2025,city_antwerpen,2025,19395056.92,,,budgeted,src_ebesluit_digipolis_2025_cyber,strong,Digipolis cyber versterking invest 19.395m 2025
bud_digipolis_city_package_2025,city_antwerpen,2025,75201406.97,,,budgeted,src_ebesluit_digipolis_2025_main,strong,Digipolis city package class 75.201m 2025 (main+index+cyber; excl ad-hoc projects)
bud_digipolis_pza_package_2025,city_antwerpen,2025,53527674.12,,,budgeted,src_ebesluit_digipolis_pza_2025,strong,PZA Digipolis IT package 53.528m 2025 (53.092 + 0.435 extra werk)
bud_digipolis_pza_invest_2025,city_antwerpen,2025,33878349.67,,,budgeted,src_ebesluit_digipolis_pza_2025,strong,PZA Digipolis invest+projects 33.878m 2025
bud_digipolis_pza_werk_2025,city_antwerpen,2025,19649324.45,,,budgeted,src_ebesluit_digipolis_pza_2025,strong,PZA Digipolis werk 19.649m 2025 after +0.435m
bud_digipolis_city_regular_2026,city_antwerpen,2026,38813888.41,,,budgeted,src_ebesluit_digipolis_2026_main,strong,Digipolis city locked regular 38.814m 2026 (werk 37.750 + cam invest 1.064); personnel residual
bud_digipolis_city_werk_2026,city_antwerpen,2026,37749888.41,,,budgeted,src_ebesluit_digipolis_2026_main,strong,Digipolis city werk 37.750m 2026 (eigen+contracts+cam maint)
bud_digipolis_city_pza_dual_2025,city_antwerpen,2025,128729081.09,,,budgeted,src_ebesluit_digipolis_2025_main,strong,Dual Digipolis city 75.2m + PZA 53.5m class 128.7m 2025; not full group members
""",
)

append(
    "commitments.csv",
    """cmt_digipolis_city_2024_26,AG Digipolis Antwerpen city IT financing multi-year,city_antwerpen,AG Digipolis Antwerpen,AGB kostendelende vereniging + beheersovereenkomst + MJP,2024-02-02,2024,2026,75201406.97,"{""2024_package"":57585321.19,""2025_package_class"":75201406.97,""2025_main"":54466529.70,""2025_index"":1339820.35,""2025_cyber"":19395056.92,""2026_regular_partial"":38813888.41,""2026_personnel_residual"":true,""note"":""Strong ebesluit; 2026 personnel lines not in Mar2026 lock vs prior years; dual PZA Digipolis separate; other members ZBA/SO residual""}",0,active,https://ebesluit.antwerpen.be/zittingen/23.1017.8479.0217/agendapunten/24.1216.5294.6673,Municipal ICT AGB city share cost-sharing,Publish full 2026 personnel package; group-member shares matrix; open L5 project portfolio,src_ebesluit_digipolis_2025_main,strong,Antwerpen>Digipolis,tick213
cmt_digipolis_pza_2025,PZA Digipolis IT package 2025 dual city,city_antwerpen,AG Digipolis Antwerpen via Politiezone,PZA begroting + college vastlegging Digipolis,2025-01-24,2025,2025,53527674.12,"{""main"":53092218.11,""invest"":33878349.67,""werk_main"":19213868.44,""werk_extra"":435456.01,""werk_total"":19649324.45,""note"":""Strong ebesluit; police IT dual to city Digipolis 75.2m; not additive with PZA toelage 321m (toelage funds PZA which pays Digipolis)""}",0,active,https://ebesluit.antwerpen.be/zittingen/24.0919.8839.0186/agendapunten/24.1216.4768.9273,Police zone IT infrastructure via Digipolis,Publish 2026 PZA Digipolis lock; dual unit-cost vs city IT,src_ebesluit_digipolis_pza_2025,strong,Antwerpen>PZA>Digipolis,tick213
cmt_digipolis_city_pza_dual_2025,Antwerp Digipolis city+PZA IT dual stack 2025,city_antwerpen,AG Digipolis Antwerpen,City + PZA ebesluit vastleggingen 2025,2024-12-20,2025,2025,128729081.09,"{""city_package"":75201406.97,""pza_package"":53527674.12,""stack_class"":128729081.09,""note"":""Strong dual; PZA Digipolis is internal spend of PZA not second city toelage; do not sum with care-safety 467m as pure additive city outlay without double-count caution on PZA perimeter""}",0,active,https://ebesluit.antwerpen.be/,City and police IT dual Digipolis financing,Publish group-wide Digipolis member matrix; 2026 full packages,src_ebesluit_digipolis_2025_main,strong,Antwerpen>Digipolis_dual,tick213
""",
)

append(
    "leaderboard.csv",
    """lb_digipolis_city_75m,AG Digipolis Antwerpen city IT package ~75.2m 2025,Flanders,ops,Antwerpen>Digipolis>city,75201406.97,75201406.97,Strong ebesluit: main 54.5 + index 1.3 + cyber 19.4 = 75.2m; 2024 57.6m; 2026 regular partial 38.8m,strong,src_ebesluit_digipolis_2025_main,City staff residents digital services,Municipal ICT AGB cost-sharing city share,Core digital ops not pure waste; cyber post-2022 attack; dual PZA Digipolis; project L5 residual,4,8.0,5,6.3,Publish full 2026 personnel; open project L5 portfolio; dual member matrix,seed,,tick213
lb_digipolis_pza_53m,PZA Digipolis IT package 53.5m 2025,Flanders,ops,Antwerpen>PZA>Digipolis,53527674.12,53527674.12,Strong ebesluit: 53.092m + 0.435m extra werk; invest 33.9 werk 19.6; dual city Digipolis 75.2m,strong,src_ebesluit_digipolis_pza_2025,Police staff residents,Police zone IT via Digipolis AGB,Core police IT not pure waste; large vs city IT; dual 2026 residual,3,7.5,5,5.75,Publish 2026 lock; unit-cost vs city Digipolis,seed,,tick213
lb_digipolis_dual_129m,Antwerp Digipolis city+PZA dual ~128.7m 2025 class,Flanders,ops,Antwerpen>Digipolis_dual,128729081.09,128729081.09,Strong: city 75.2 + PZA 53.5; PZA is zone spend not second city toelage; other members residual,strong,src_ebesluit_digipolis_2025_main,City and police digital,Dual municipal ICT AGB financing,Core ops; double-count caution with PZA toelage 321m; group matrix FOI,4,8.5,5,6.55,Publish group Digipolis matrix; 2026 full packages; open L5,seed,,tick213
""",
)

# research_queue: mark rq_206 done; seed rq_207
rq_path = ROOT / "research_queue.csv"
text = rq_path.read_text(encoding="utf-8")
old = 'rq_206,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills (Mons BI2026 Antwerp Zorgbedrijf 2026 Digipolis remaining culture L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-28T20:45:00Z,,"Spawned tick212 after Zorgbedrijf 65m; rq_116 SWA deferred Oct-Dec 2026"'
new = 'rq_206,Continuous FOI-adjacent public hole-fill batch,continuous,5,done,L5,gg_belgium,"Prefer public primary fills (Mons BI2026 Antwerp Zorgbedrijf 2026 Digipolis remaining culture L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-28T20:45:00Z,2026-07-28T21:05:00Z,"tick213: Digipolis city 75.2m 2025 + PZA 53.5m dual 128.7m; 2024 57.6m; 2026 regular 38.8m partial; residual Mons/personnel; spawn rq_207"'
if old not in text:
    raise SystemExit("rq_206 row not found as expected")
text = text.replace(old, new)
if not text.endswith("\n"):
    text += "\n"
text += 'rq_207,Continuous FOI-adjacent public hole-fill batch,continuous,5,open,L5,gg_belgium,"Prefer public primary fills (Mons BI2026 Antwerp Digipolis 2026 personnel Zorgbedrijf 2026 remaining culture L5 ebesluit FPS taxex other large FOI-adjacent SOEs utilities) if new PDFs appear; else next open rq; do not idle while public work remains.",,2026-07-28T21:05:00Z,,"Spawned tick213 after Digipolis 75m/53m dual; rq_116 SWA deferred Oct-Dec 2026"\n'
rq_path.write_text(text, encoding="utf-8")

# Update gap_antwerp_subsidies_top20 notes if present
foi_path = ROOT / "foi_queue.csv"
foi = foi_path.read_text(encoding="utf-8")
marker = "tick140+204: Toneelhuis 3.30m 2026 strong; culture 35m medium; Toneelhuis 3.30m OBV 1.79m ASO 0.61m DeSingel 0.10m Zomer 1.21m ExtraCity 0.15m JEF 0.24m FreeClinic 0.97m sample culture 7.40m/7houses; residual register top20 human send"
if marker in foi:
    foi = foi.replace(
        marker,
        "tick140+204+213: culture sample 7.40m + ZBA 65m + Digipolis city 75.2m 2025 + PZA Digipolis 53.5m dual; residual register top20 + Digipolis 2026 personnel + other-member shares human send",
    )
    foi_path.write_text(foi, encoding="utf-8")
    print("foi gap_antwerp updated")
else:
    print("foi gap_antwerp marker not found — skip note update")

print("tick213 writes complete")
