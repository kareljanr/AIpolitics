import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1784'; utc='2026-08-24T21:35:00Z'
eid='nv_lilas'; sid='src_lilas_jr2025_nbb'
gap='gap_lilas_marge_3_27m_controllers_4_11m_rivage_135m_l5'
lb='lb_lilas_marge_3_27m_controllers_4_11m_rivage_135m_l5'
comm='comm_lilas_jr2025_marge_3_27m'
hier='Wallonie>Provinces>BrabantWallon>Communes>ChaumontGistoux>Bonlez>MRPA>AuxLilasDeBonlez>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'AUX LILAS DE BONLEZ SA NBB A-cap YE2025 deposit 2026-00137101','http://cdn.staatsbladmonitor.be/2026pdf/2026-00137101.pdf','Nationale Bank van België / AUX LILAS DE BONLEZ SA','2026-08-24','primary_official','tick1784; AV 12.05.2026; A-cap abbrev; Vivalto Home Belgium admin; opinion sans reserve; Bonlez Rue Bas Bonlez 57; marge 3.27m; controllers 4.11m; RIVAGE 135.6m'])
    w.writerow(['src_lilas_site','Vivalto Home — Aux Lilas de Bonlez maisons','https://www.vivaltohome.com/maisons/aux-lilas-de-bonlez/','Vivalto Home','2026-08-24','primary_official','tick1784; Rue Bas Bonlez 57 1325 Chaumont-Gistoux; lilasdebonlez.info@vivaltohome.com'])
    w.writerow(['src_lilas_kbo','KBO AUX LILAS DE BONLEZ SA 0459.968.951','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0459968951','KBO','2026-08-24','primary_official','tick1784; SA/NV; Rue Bas Bonlez 57 1325 Chaumont-Gistoux; RPR Liege division Arlon'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Aux Lilas de Bonlez NV (leftover Vivalto WZC dual / Bonlez)','AUX LILAS DE BONLEZ SA (WZC Vivalto résiduel / Bonlez)','AUX LILAS DE BONLEZ SA leftover Vivalto nursing-home dual Bonlez Chaumont-Gistoux','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/aux-lilas-de-bonlez/','lilasdebonlez.info@vivaltohome.com','Rue Bas Bonlez 57 1325 Chaumont-Gistoux','tick1784 leftover unused Vivalto maison after CHARLEMAGNE; KBO 0459.968.951 Actief; SA; official NBB A-cap YE2025 deposit 2026-00137101 CDN 200 28p; AV 12.05.2026; mère Vivalto Home Belgium; opinion sans réserve; RIVAGE gage 135600000; controllers 9500=4110235; FVA 5098317; sourced euros assets 11306623 equity 2413697 debt 8668535 marge 3266353 staff 2456066 VTE 37.9 expl 428357 pnl 254282; FOI ready RIZIV/controllers/RIVAGE'])

buds=[
 ('bud_lilas_assets_2025',11306623,'stock','Assets YE2025 11306623; tick1784'),
 ('bud_lilas_equity_2025',2413697,'stock','Equity 2413697; tick1784'),
 ('bud_lilas_debt_2025',8668535,'stock','Debt 8668535; tick1784'),
 ('bud_lilas_leasing_lt_2025',3625551,'stock','LT credit/leasing 172/3=3625551; option 479100; tick1784'),
 ('bud_lilas_autres_emprunts_lt_2025',3553695,'stock','Autres emprunts LT 174=3553695; tick1784'),
 ('bud_lilas_fva_2025',5098317,'stock','Immobilisations financieres 5098317; tick1784'),
 ('bud_lilas_controllers_recv_2025',4110235,'stock','Creances sur administrateurs/controleurs 9500=4110235; tick1784'),
 ('bud_lilas_autres_creances_2025',792693,'stock','Autres creances ST 792693; tick1784'),
 ('bud_lilas_cash_2025',244941,'stock','Cash 244941 JUMP vs 62253; tick1784'),
 ('bud_lilas_marge_2025',3266353,'realized','Marge bruto 3266353 (A-cap; CA undisclosed); tick1784'),
 ('bud_lilas_staff_2025',2456066,'realized','Staff 2456066 / VTE 37.9; tick1784'),
 ('bud_lilas_expl_2025',428357,'realized','Benefice exploitation 428357; tick1784'),
 ('bud_lilas_pnl_2025',254282,'realized','PnL 254282 flip from prior loss; admin 110978 no dividend apport; tick1784'),
 ('bud_lilas_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage 135600000 group undivided; assets grevés 6486834; tick1784'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'AUX LILAS DE BONLEZ SA JR2025 leftover Vivalto dual (marge 3.27m / controllers 4.11m / RIVAGE 135.6m)',eid,'AUX LILAS DE BONLEZ SA / Vivalto Home Belgium / residents Bonlez','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-12',2025,2025,3266353,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00137101.pdf','Local leftover Vivalto WZC map WAL Bonlez — marge 3.27m / controllers + RIVAGE twin CedreBleu batch','Publish CA/RIZIV + controllers map + RIVAGE share; unit-cost',sid,'strong',hier,'tick1784; assets 11.31m equity 2.41m debt 8.67m FVA 5.10m leasing LT 3.63m marge 3.27m staff 2.46m VTE 37.9 expl 0.43m pnl 0.25m controllers 4.11m RIVAGE 135.6m; FOI ready not sent; not TE-additive; A-cap CA undisclosed'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'AUX LILAS DE BONLEZ SA 2025: marge 3.27m / staff 2.46m (controllers 4.11m + RIVAGE gage 135.6m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),3266353,135600000,'Envelope=marge 3266353 (A-cap; CA undisclosed); staff 2.46m VTE 37.9; controllers recv 4.11m; FVA 5.10m; RIVAGE gage 135.6m undivided; cash JUMP; loss-flip to profit; no dividend apport','strong',sid,'MRPA/WZC residents Bonlez / Vivalto group','Nursing-home care (MRPA/MRS)','Vivalto RIVAGE cascade sister with large controller receivables and opaque A-cap CA',6.3,6.8,5,6.5,'Publish CA/RIZIV; disclose controllers + RIVAGE share; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB A-cap YE2025 live marge 3266353 but CA undisclosed; controllers recv 9500=4110235 + FVA 5098317 + autres creances 792693 counterparties/terms; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need Lilas share; leasing LT 3625551 + autres emprunts LT 3553695 + option 479100; admin 110978','Vivalto Bonlez WZC with abbreviated schema + controller receivables + undivided RIVAGE gage — opacity on public care-euro path',8,'AUX LILAS DE BONLEZ SA / Vivalto Home Belgium SA','lilasdebonlez.info@vivaltohome.com','Rue Bas Bonlez 57 1325 Chaumont-Gistoux',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1784; human-send only; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; unused Vivalto maisons remain'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1784':
        row['status']='done'
        row['title']='AUX LILAS DE BONLEZ SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: AUX LILAS DE BONLEZ SA leftover unused Vivalto maison Bonlez after CHARLEMAGNE; '
            'KBO 0459.968.951 Actief; live JR2025 official NBB A-cap PDF (236234 bytes 28p deposit 2026-00137101; AV 12.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); sourced euros assets 11306623 equity 2413697 debt 8668535 '
            'marge 3266353 staff 2456066 VTE 37.9 pnl 254282 controllers 4110235 RIVAGE 135600000; '
            'FOI ready not sent; NOT Charlemagne continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1784 LILAS leftover Vivalto residual; KBO 0459.968.951; live JR2025 NBB A-cap PDF; sourced euros; FOI ready not sent; next rq_1785 residual dual L5'
        print('updated rq_1784'); break
else:
    raise SystemExit('missing rq_1784')
if not any(r.get('task_id')=='rq_1785' for r in rows):
    rows.append({
        'task_id':'rq_1785','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1785 after 1784 LILAS. Next every-10 is 1790. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other unused Vivalto maisons '
                 '(cottage-rose / e-carpentier / floreal / la-maison-dieu / jardin-des-chantoirs / le-marronnier / manoir-du-menil) '
                 'if CDN 200 (REPOS FLEURI 2026-00137105 live candidate), other IOED/HVZ/IGS. '
                 'Do NOT redo Lilas/Charlemagne/CedreBleu/BrembloemImmo continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1784 LILAS; NEXT AGB/NSZ-if-200/Bosgroep/BrembloemVZW-if-200/unused-Vivalto/ReposFleuri-if-vivalto; next every-10 1790'
    })
    print('spawned rq_1785')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1784',1784,'no',
        'tick1784 leftover AUX LILAS DE BONLEZ; KBO 0459.968.951; NBB YE2025 marge 3266353 staff 2456066 VTE 37.9 pnl 254282 controllers 4110235 FVA 5098317 RIVAGE gage 135600000 cash JUMP; FOI RIZIV/controllers/RIVAGE; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; CDN live ReposFleuri 00137105; unused Vivalto maisons remain; NOT every-10 (next 1790); next rq_1785 AGB/NSZ-if-200/Bosgroep/unused-Vivalto/ReposFleuri; continuous hole_fill'])
print('OK')
