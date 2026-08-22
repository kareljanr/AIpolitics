import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1775'; utc='2026-08-24T18:35:00Z'
eid='nv_closroses'; sid='src_closroses_jr2025_nbb'
gap='gap_closroses_ca_5_17m_related_recv_5_83m_rivage_135m_l5'
lb='lb_closroses_ca_5_17m_related_recv_5_83m_rivage_135m_l5'
comm='comm_closroses_jr2025_ca_5_17m'
hier='Wallonie>Provinces>Liege>Communes>ComblainAuPont>Poulseur>MRPA>LeClosDesRoses>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'LE CLOS DES ROSES SA NBB C-cap YE2025 deposit 2026-00176179','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176179.pdf','Nationale Bank van België / LE CLOS DES ROSES SA','2026-08-24','primary_official','tick1775; AV 21.05.2026; C-cap full; Vivalto Home Belgium admin; opinion sans reserve; Poulseur Rue des Ecoles 53; CA 5.17m; related FVA 5.83m; RIVAGE gage 135.6m; dividend 0.33m'])
    w.writerow(['src_closroses_site','Vivalto Home — Le Clos des Roses maisons','https://www.vivaltohome.com/maisons/le-clos-des-roses/','Vivalto Home','2026-08-24','primary_official','tick1775; Rue des Ecoles 53 4171 Poulseur; closdesroses@vivaltohome.com'])
    w.writerow(['src_closroses_kbo','KBO LE CLOS DES ROSES SA 0438.414.066','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0438414066','KBO','2026-08-24','primary_official','tick1775; SA/NV; Rue des Ecoles 53 4171 Poulseur; RPR Liege division Huy'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Le Clos des Roses NV (leftover Vivalto WZC dual / Poulseur)','LE CLOS DES ROSES SA (WZC Vivalto résiduel / Poulseur)','LE CLOS DES ROSES SA leftover Vivalto nursing-home dual Poulseur','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/le-clos-des-roses/','closdesroses@vivaltohome.com','Rue des Ecoles 53 4171 Poulseur','tick1775 leftover Vivalto WZC dual after LE CENTENAIRE; KBO 0438.414.066 Actief; SA; official NBB C-cap YE2025 deposit 2026-00176179 CDN 200 54p; AV 21.05.2026; mère Vivalto Home Belgium; opinion sans réserve; RIVAGE/VIVALTO LEASE gage 135600000 undivided twin RAPSODE; related FVA créances 5833909; controllers 9500=5545446; related debt 7068447; dividend apport 325000; sourced euros assets 11188312 equity 2271728 debt 8472309 FVA 5834109 leasing LT 3526879 CA 5173715 staff 3268771 VTE 56.7 expl 523803 pnl 367088; FOI ready RIZIV/related recv/RIVAGE share/dividend'])

buds=[
 ('bud_closroses_assets_2025',11188312,'stock','Assets YE2025 11188312 DROP vs 12128514; tick1775'),
 ('bud_closroses_equity_2025',2271728,'stock','Equity 2271728 DROP vs 2399146; tick1775'),
 ('bud_closroses_debt_2025',8472309,'stock','Debt 8472309; tick1775'),
 ('bud_closroses_leasing_lt_2025',3526879,'stock','LT leasing dettes 3526879; option achat 413000; tick1775'),
 ('bud_closroses_fva_2025',5834109,'stock','Immobilisations financieres 5834109 mostly related créances 5833909; tick1775'),
 ('bud_closroses_related_recv_fva_2025',5833909,'stock','Créances entreprises liées FVA 281=5833909; tick1775'),
 ('bud_closroses_related_recv_st_2025',1239162,'stock','Créances liées ST 1239162 DROP vs 1903578; tick1775'),
 ('bud_closroses_controllers_recv_2025',5545446,'stock','Créances sur administrateurs/controleurs 9500=5545446; tick1775'),
 ('bud_closroses_related_debt_2025',7068447,'stock','Dettes entreprises liées 7068447 (LT 6916624 + ST 151823); tick1775'),
 ('bud_closroses_cash_2025',145963,'stock','Cash 145963 JUMP vs 74943; tick1775'),
 ('bud_closroses_ca_2025',5173715,'realized','CA 5173715 / ventes prestations 5174999; tick1775'),
 ('bud_closroses_staff_2025',3268771,'realized','Staff 3268771 / VTE 56.7; tick1775'),
 ('bud_closroses_expl_2025',523803,'realized','Benefice exploitation 523803; tick1775'),
 ('bud_closroses_pnl_2025',367088,'realized','PnL 367088; dividend apport 325000 + admin 167175; tick1775'),
 ('bud_closroses_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage fonds commerce 135600000 group undivided; assets grevés 7604853; tick1775'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'LE CLOS DES ROSES SA JR2025 leftover Vivalto dual (CA 5.17m / related recv 5.83m / RIVAGE 135.6m)',eid,'LE CLOS DES ROSES SA / Vivalto Home Belgium / residents Poulseur','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-21',2025,2025,5173715,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176179.pdf','Local leftover Vivalto WZC map WAL Poulseur — CA 5.17m / related FVA + RIVAGE gage twin RAPSODE','Publish RIZIV split + related recv/debt map + RIVAGE share of 135.6m + dividend rationale; unit-cost',sid,'strong',hier,'tick1775; assets 11.19m equity 2.27m debt 8.47m FVA 5.83m leasing LT 3.53m CA 5.17m staff 3.27m VTE 56.7 expl 0.52m pnl 0.37m dividend 0.33m related recv FVA 5.83m controllers 5.55m related debt 7.07m RIVAGE 135.6m; FOI ready not sent; not TE-additive'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'LE CLOS DES ROSES SA 2025: CA 5.17m / staff 3.27m (related FVA 5.83m + RIVAGE gage 135.6m)', 'L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),5173715,135600000,'Envelope=CA 5173715; staff 3.27m VTE 56.7; related FVA créances 5.83m + controllers 5.55m; related debt 7.07m; dividend 0.33m; equity DROP; RIVAGE/VIVALTO LEASE gage 135.6m group undivided (twin RAPSODE); leasing LT 3.53m','strong',sid,'MRPA/WZC residents Poulseur / Vivalto group','Nursing-home care (MRPA/MRS)','Same Vivalto RIVAGE bond/lease cascade as RAPSODE plus large related-party receivables while equity DROPs',6.4,6.8,5,6.6,'Publish RIZIV split; disclose related recv/debt + RIVAGE share; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB C-cap YE2025 live CA 5173715 but RIZIV/residentie split unpublished; related FVA créances 5833909 + related ST 1239162 + controllers 9500=5545446 counterparties/terms; related debt 7068447; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need ClosRoses share; leasing LT 3526879 + option achat 413000; dividend apport 325000 vs prior 940000; admin 167175; equity DROP','Vivalto Poulseur WZC with full CA but opaque related-party recv/debt cascade and undivided RIVAGE gage twin RAPSODE — opacity on public care-euro path and group extraction',8,'LE CLOS DES ROSES SA / Vivalto Home Belgium SA','closdesroses@vivaltohome.com','Rue des Ecoles 53 4171 Poulseur',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1775; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; CDN live Etrier/VertBocage/Tonnelle/AgeDor; NOT Centenaire continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1775':
        row['status']='done'
        row['title']='LE CLOS DES ROSES SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: LE CLOS DES ROSES SA leftover Vivalto WZC dual Poulseur after LE CENTENAIRE; '
            'KBO 0438.414.066 Actief; live JR2025 official NBB C-cap PDF (1159591 bytes 54p deposit 2026-00176179; AV 21.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 11188312 equity 2271728 debt 8472309 CA 5173715 staff 3268771 VTE 56.7 '
            'pnl 367088 dividend 325000 related FVA 5833909 controllers 5545446 related debt 7068447 RIVAGE 135600000; '
            'FOI ready not sent; NOT Centenaire continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1775 LE CLOS DES ROSES leftover Vivalto residual; KBO 0438.414.066; live JR2025 NBB C-cap PDF; sourced euros; FOI ready not sent; next rq_1776 residual dual L5'
        print('updated rq_1775'); break
else:
    raise SystemExit('missing rq_1775')
if not any(r.get('task_id')=='rq_1776' for r in rows):
    rows.append({
        'task_id':'rq_1776','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1776 after 1775 LE CLOS DES ROSES. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(L ETRIER D ARGENT 2026-00176181 / AU VERT BOCAGE 2026-00176184 / LA TONNELLE 2026-00176186 / L AGE D OR 2026-00176187 live), '
                 'other IOED/HVZ/IGS. Do NOT redo ClosRoses/Centenaire/Braine/Meridienne continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1775 LE CLOS DES ROSES; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Etrier/VertBocage/Tonnelle/AgeDor; next every-10 1780'
    })
    print('spawned rq_1776')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1775',1775,'no',
        'tick1775 leftover LE CLOS DES ROSES Poulseur; KBO 0438.414.066; NBB YE2025 CA 5173715 staff 3268771 VTE 56.7 pnl 367088 dividend 325000 related FVA 5833909 controllers 5545446 related debt 7068447 RIVAGE gage 135600000 equity DROP; FOI RIZIV/related recv/RIVAGE share/dividend; Brembloem still no JR2025; AGB Bornem JR2024; CDN live Etrier 00176181 VertBocage 00176184 Tonnelle 00176186 AgeDor 00176187; NOT every-10 (next 1780); next rq_1776 AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/Etrier/VertBocage/Tonnelle/AgeDor; continuous hole_fill'])
print('OK')
