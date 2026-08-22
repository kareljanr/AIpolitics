import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1777'; utc='2026-08-24T19:15:00Z'
eid='nv_vertbocage'; sid='src_vertbocage_jr2025_nbb'
gap='gap_vertbocage_marge_3_75m_related_recv_4_66m_rivage_135m_l5'
lb='lb_vertbocage_marge_3_75m_related_recv_4_66m_rivage_135m_l5'
comm='comm_vertbocage_jr2025_marge_3_75m'
hier='Wallonie>Provinces>Liege>Communes>Ans>Loncin>MRPA>AuVertBocage>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'AU VERT BOCAGE SA NBB A-cap YE2025 deposit 2026-00176184','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176184.pdf','Nationale Bank van België / AU VERT BOCAGE SA','2026-08-24','primary_official','tick1777; AV 21.05.2026; A-cap abbrev; Vivalto Home Belgium admin; opinion sans reserve; Loncin Rue du Plope 12; marge 3.75m; controllers 4.66m; RIVAGE gage 135.6m; dividend 0.33m'])
    w.writerow(['src_vertbocage_site','Vivalto Home — Au Vert Bocage maisons','https://www.vivaltohome.com/maisons/au-vert-bocage/','Vivalto Home','2026-08-24','primary_official','tick1777; Rue du Plope 12 4431 Loncin; auvertbocage@vivaltohome.com'])
    w.writerow(['src_vertbocage_kbo','KBO AU VERT BOCAGE SA 0433.536.550','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0433536550','KBO','2026-08-24','primary_official','tick1777; SA/NV; Rue du Plope 12 4431 Loncin; RPR Liege; denomination AU VERT BOCAGE - VIVALTO HOME'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Au Vert Bocage NV (leftover Vivalto WZC dual / Loncin)','AU VERT BOCAGE SA (WZC Vivalto résiduel / Loncin)','AU VERT BOCAGE SA leftover Vivalto nursing-home dual Loncin Ans','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/au-vert-bocage/','auvertbocage@vivaltohome.com','Rue du Plope 12 4431 Loncin','tick1777 leftover Vivalto WZC dual after L ETRIER D ARGENT; KBO 0433.536.550 Actief; SA (denom AU VERT BOCAGE - VIVALTO HOME); official NBB A-cap YE2025 deposit 2026-00176184 CDN 200 28p; AV 21.05.2026; mère Vivalto Home Belgium; opinion sans réserve; RIVAGE/VIVALTO LEASE gage 135600000 undivided twin Etrier/ClosRoses/RAPSODE; controllers 9500=4661950; FVA 5028114; dividend apport 325000; sourced euros assets 8299399 equity 1807206 debt 6229994 leasing LT 1848566 marge 3746548 staff 3012400 VTE 46 expl 512460 pnl 426107; FOI ready RIZIV/related recv/RIVAGE share/dividend'])

buds=[
 ('bud_vertbocage_assets_2025',8299399,'stock','Assets YE2025 8299399 DROP vs 8983433; tick1777'),
 ('bud_vertbocage_equity_2025',1807206,'stock','Equity 1807206 DROP vs 1880591; tick1777'),
 ('bud_vertbocage_debt_2025',6229994,'stock','Debt 6229994; tick1777'),
 ('bud_vertbocage_leasing_lt_2025',1848566,'stock','LT credit/leasing 172/3=1848566; option achat 472500; tick1777'),
 ('bud_vertbocage_fva_2025',5028114,'stock','Immobilisations financieres 5028114; tick1777'),
 ('bud_vertbocage_autres_creances_2025',1100782,'stock','Autres creances ST 1100782 DROP vs 1703439; tick1777'),
 ('bud_vertbocage_controllers_recv_2025',4661950,'stock','Creances sur administrateurs/controleurs 9500=4661950; tick1777'),
 ('bud_vertbocage_cash_2025',208470,'stock','Cash 208470 JUMP vs 160524; tick1777'),
 ('bud_vertbocage_marge_2025',3746548,'realized','Marge bruto 3746548 (A-cap; CA undisclosed); tick1777'),
 ('bud_vertbocage_staff_2025',3012400,'realized','Staff 3012400 / VTE 46; tick1777'),
 ('bud_vertbocage_expl_2025',512460,'realized','Benefice exploitation 512460; tick1777'),
 ('bud_vertbocage_pnl_2025',426107,'realized','PnL 426107; dividend apport 325000 + admin 163242; autres dettes ST=distribuer 488242; tick1777'),
 ('bud_vertbocage_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage fonds commerce 135600000 group undivided; assets grevés 6742435; tick1777'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'AU VERT BOCAGE SA JR2025 leftover Vivalto dual (marge 3.75m / related recv 4.66m / RIVAGE 135.6m)',eid,'AU VERT BOCAGE SA / Vivalto Home Belgium / residents Loncin','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-21',2025,2025,3746548,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176184.pdf','Local leftover Vivalto WZC map WAL Loncin — marge 3.75m / controllers recv + RIVAGE gage twin Etrier/ClosRoses/RAPSODE','Publish CA/RIZIV split + related recv map + RIVAGE share of 135.6m + dividend rationale; unit-cost',sid,'strong',hier,'tick1777; assets 8.30m equity 1.81m debt 6.23m FVA 5.03m leasing LT 1.85m marge 3.75m staff 3.01m VTE 46 expl 0.51m pnl 0.43m dividend 0.33m controllers 4.66m RIVAGE 135.6m; FOI ready not sent; not TE-additive; A-cap CA undisclosed'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'AU VERT BOCAGE SA 2025: marge 3.75m / staff 3.01m (controllers recv 4.66m + RIVAGE gage 135.6m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),3746548,135600000,'Envelope=marge 3746548 (A-cap; CA undisclosed); staff 3.01m VTE 46; controllers recv 4.66m; FVA 5.03m; dividend 0.33m (prior 0.80m); equity DROP; RIVAGE/VIVALTO LEASE gage 135.6m group undivided (twin Etrier/ClosRoses/RAPSODE); leasing LT 1.85m','strong',sid,'MRPA/WZC residents Loncin / Vivalto group','Nursing-home care (MRPA/MRS)','Same Vivalto RIVAGE bond/lease cascade plus large controller receivables while equity DROPs; A-cap hides CA',6.3,6.8,5,6.5,'Publish CA/RIZIV; disclose related recv + RIVAGE share; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 3746548 but CA undisclosed; controllers recv 9500=4661950 + FVA 5028114 + autres creances ST 1100782 counterparties/terms; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need VertBocage share; leasing LT 1848566 + option achat 472500; dividend apport 325000 + admin 163242 (autres dettes ST 488242=distribuer); equity DROP','Vivalto Loncin WZC with abbreviated schema + controller receivables + undivided RIVAGE gage twin Etrier/ClosRoses/RAPSODE — opacity on public care-euro path and group extraction',8,'AU VERT BOCAGE SA / Vivalto Home Belgium SA','auvertbocage@vivaltohome.com','Rue du Plope 12 4431 Loncin',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1777; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; CDN live Tonnelle/AgeDor; NOT Etrier continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1777':
        row['status']='done'
        row['title']='AU VERT BOCAGE SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: AU VERT BOCAGE SA leftover Vivalto WZC dual Loncin after L ETRIER D ARGENT; '
            'KBO 0433.536.550 Actief; live JR2025 official NBB A-cap PDF (207761 bytes 28p deposit 2026-00176184; AV 21.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 8299399 equity 1807206 debt 6229994 marge 3746548 staff 3012400 VTE 46 '
            'pnl 426107 dividend 325000 controllers 4661950 FVA 5028114 RIVAGE 135600000; '
            'FOI ready not sent; NOT Etrier continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1777 AU VERT BOCAGE leftover Vivalto residual; KBO 0433.536.550; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1778 residual dual L5'
        print('updated rq_1777'); break
else:
    raise SystemExit('missing rq_1777')
if not any(r.get('task_id')=='rq_1778' for r in rows):
    rows.append({
        'task_id':'rq_1778','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1778 after 1777 AU VERT BOCAGE. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(LA TONNELLE 2026-00176186 / L AGE D OR 2026-00176187 live), '
                 'other IOED/HVZ/IGS. Do NOT redo VertBocage/Etrier/ClosRoses/Centenaire/Braine/Meridienne continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1777 AU VERT BOCAGE; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Tonnelle/AgeDor; next every-10 1780'
    })
    print('spawned rq_1778')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1777',1777,'no',
        'tick1777 leftover AU VERT BOCAGE Loncin; KBO 0433.536.550; NBB YE2025 marge 3746548 staff 3012400 VTE 46 pnl 426107 dividend 325000 controllers 4661950 FVA 5028114 RIVAGE gage 135600000 equity DROP; FOI RIZIV/related recv/RIVAGE share/dividend; Brembloem still no JR2025; AGB Bornem JR2024; CDN live Tonnelle 00176186 AgeDor 00176187; NOT every-10 (next 1780); next rq_1778 AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Tonnelle/AgeDor; continuous hole_fill'])
print('OK')
