import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1778'; utc='2026-08-24T19:35:00Z'
eid='nv_tonnelle'; sid='src_tonnelle_jr2025_nbb'
gap='gap_tonnelle_ca_6_76m_related_recv_3_35m_rivage_135m_l5'
lb='lb_tonnelle_ca_6_76m_related_recv_3_35m_rivage_135m_l5'
comm='comm_tonnelle_jr2025_ca_6_76m'
hier='Wallonie>Provinces>Liege>Communes>Hannut>MRPA>LaTonnelle>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'LA TONNELLE SA NBB C-cap YE2025 deposit 2026-00176186','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176186.pdf','Nationale Bank van België / LA TONNELLE SA','2026-08-24','primary_official','tick1778; AV 21.05.2026; C-cap full; Vivalto Home Belgium admin; opinion sans reserve; Hannut Rue de Landen 107; CA 6.76m; related FVA 3.35m; RIVAGE gage 135.6m; dividend 0.53m'])
    w.writerow(['src_tonnelle_site','Vivalto Home — La Tonnelle maisons','https://www.vivaltohome.com/maisons/la-tonnelle/','Vivalto Home','2026-08-24','primary_official','tick1778; Rue de Landen 107 4280 Hannut; tonnelle.d@vivaltohome.com'])
    w.writerow(['src_tonnelle_kbo','KBO LA TONNELLE SA 0431.602.587','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0431602587','KBO','2026-08-24','primary_official','tick1778; SA/NV; Rue de Landen 107 4280 Hannut; RPR Liege division Huy'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'La Tonnelle NV (leftover Vivalto WZC dual / Hannut)','LA TONNELLE SA (WZC Vivalto résiduel / Hannut)','LA TONNELLE SA leftover Vivalto nursing-home dual Hannut','other','nv_vivalto_home_be','fr','https://www.vivaltohome.com/maisons/la-tonnelle/','tonnelle.d@vivaltohome.com','Rue de Landen 107 4280 Hannut','tick1778 leftover Vivalto WZC dual after AU VERT BOCAGE; KBO 0431.602.587 Actief; SA; official NBB C-cap YE2025 deposit 2026-00176186 CDN 200 55p; AV 21.05.2026; mère Vivalto Home Belgium; opinion sans réserve; RIVAGE/VIVALTO LEASE gage 135600000 undivided twin VertBocage/Etrier/ClosRoses/RAPSODE; related FVA créances 3354539; controllers 9500=2920500; related debt 7555451; dividend apport 525000; sourced euros assets 12640456 equity 2782042 debt 9209747 FVA 3359659 leasing LT 3811594 CA 6764837 staff 4006575 VTE 63.2 expl 711511 pnl 456687; FOI ready RIZIV/related recv/RIVAGE share/dividend'])

buds=[
 ('bud_tonnelle_assets_2025',12640456,'stock','Assets YE2025 12640456 DROP vs 13727667; tick1778'),
 ('bud_tonnelle_equity_2025',2782042,'stock','Equity 2782042 DROP vs 3073783; tick1778'),
 ('bud_tonnelle_debt_2025',9209747,'stock','Debt 9209747; tick1778'),
 ('bud_tonnelle_leasing_lt_2025',3811594,'stock','LT leasing dettes 3811594; option achat 623000; tick1778'),
 ('bud_tonnelle_fva_2025',3359659,'stock','Immobilisations financieres 3359659 mostly related créances 3354539; tick1778'),
 ('bud_tonnelle_related_recv_fva_2025',3354539,'stock','Créances entreprises liées FVA 281=3354539; tick1778'),
 ('bud_tonnelle_related_recv_st_2025',2058672,'stock','Créances liées ST 2058672 DROP vs 2691418; tick1778'),
 ('bud_tonnelle_controllers_recv_2025',2920500,'stock','Créances sur administrateurs/controleurs 9500=2920500; tick1778'),
 ('bud_tonnelle_related_debt_2025',7555451,'stock','Dettes entreprises liées 7555451 (LT 6692203 + ST 863249); tick1778'),
 ('bud_tonnelle_cash_2025',126972,'stock','Cash 126972 DROP vs 138962; tick1778'),
 ('bud_tonnelle_ca_2025',6764837,'realized','CA 6764837 / ventes prestations 6777954; tick1778'),
 ('bud_tonnelle_staff_2025',4006575,'realized','Staff 4006575 / VTE 63.2; tick1778'),
 ('bud_tonnelle_expl_2025',711511,'realized','Benefice exploitation 711511; tick1778'),
 ('bud_tonnelle_pnl_2025',456687,'realized','PnL 456687; dividend apport 525000 + admin 213229; autres dettes ST 1466848; tick1778'),
 ('bud_tonnelle_rivage_gage_2025',135600000,'stock','VIVALTO LEASE/RIVAGE gage fonds commerce 135600000 group undivided; assets grevés 6098806; tick1778'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'LA TONNELLE SA JR2025 leftover Vivalto dual (CA 6.76m / related recv 3.35m / RIVAGE 135.6m)',eid,'LA TONNELLE SA / Vivalto Home Belgium / residents Hannut','CSA SA; decret wallon openbaarheid analog for dual care euros','2026-05-21',2025,2025,6764837,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00176186.pdf','Local leftover Vivalto WZC map WAL Hannut — CA 6.76m / related FVA + RIVAGE gage twin VertBocage continuum','Publish RIZIV split + related recv/debt map + RIVAGE share of 135.6m + dividend rationale; unit-cost',sid,'strong',hier,'tick1778; assets 12.64m equity 2.78m debt 9.21m FVA 3.35m leasing LT 3.81m CA 6.76m staff 4.01m VTE 63.2 expl 0.71m pnl 0.46m dividend 0.53m related recv FVA 3.35m controllers 2.92m related debt 7.56m RIVAGE 135.6m; FOI ready not sent; not TE-additive'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'LA TONNELLE SA 2025: CA 6.76m / staff 4.01m (related FVA 3.35m + RIVAGE gage 135.6m)','L5','nursing_home_private_dual',hier.replace('>JR2025_L5',''),6764837,135600000,'Envelope=CA 6764837; staff 4.01m VTE 63.2; related FVA créances 3.35m + controllers 2.92m; related debt 7.56m; dividend 0.53m; equity DROP; RIVAGE/VIVALTO LEASE gage 135.6m group undivided (twin VertBocage/Etrier/ClosRoses/RAPSODE); leasing LT 3.81m','strong',sid,'MRPA/WZC residents Hannut / Vivalto group','Nursing-home care (MRPA/MRS)','Same Vivalto RIVAGE bond/lease cascade plus large related-party receivables while equity DROPs',6.4,6.8,5,6.6,'Publish RIZIV split; disclose related recv/debt + RIVAGE share; unit-cost','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB C-cap YE2025 live CA 6764837 but RIZIV/residentie split unpublished; related FVA créances 3354539 + related ST 2058672 + controllers 9500=2920500 counterparties/terms; related debt 7555451; VIVALTO LEASE/RIVAGE gage 135600000 group undivided — need Tonnelle share; leasing LT 3811594 + option achat 623000; dividend apport 525000 + admin 213229; equity DROP','Vivalto Hannut WZC with full CA but opaque related-party recv/debt cascade and undivided RIVAGE gage twin VertBocage continuum — opacity on public care-euro path and group extraction',8,'LA TONNELLE SA / Vivalto Home Belgium SA','tonnelle.d@vivaltohome.com','Rue de Landen 107 4280 Hannut',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1778; human-send only; Brembloem still no JR2025; AGB Bornem JR2024; CDN live AgeDor; NOT VertBocage continuum'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1778':
        row['status']='done'
        row['title']='LA TONNELLE SA JR2025 leftover Vivalto dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: LA TONNELLE SA leftover Vivalto WZC dual Hannut after AU VERT BOCAGE; '
            'KBO 0431.602.587 Actief; live JR2025 official NBB C-cap PDF (1227064 bytes 55p deposit 2026-00176186; AV 21.05.2026; '
            'Vivalto Home Belgium; opinion sans réserve); '
            'sourced euros assets 12640456 equity 2782042 debt 9209747 CA 6764837 staff 4006575 VTE 63.2 '
            'pnl 456687 dividend 525000 related FVA 3354539 controllers 2920500 related debt 7555451 RIVAGE 135600000; '
            'FOI ready not sent; NOT VertBocage continuum')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1778 LA TONNELLE leftover Vivalto residual; KBO 0431.602.587; live JR2025 NBB C-cap PDF; sourced euros; FOI ready not sent; next rq_1779 residual dual L5'
        print('updated rq_1778'); break
else:
    raise SystemExit('missing rq_1778')
if not any(r.get('task_id')=='rq_1779' for r in rows):
    rows.append({
        'task_id':'rq_1779','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1779 after 1778 LA TONNELLE. Next every-10 is 1780. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other Vivalto sisters if CDN 200 '
                 '(L AGE D OR 2026-00176187 live), '
                 'other IOED/HVZ/IGS. Do NOT redo Tonnelle/VertBocage/Etrier/ClosRoses/Centenaire/Braine/Meridienne continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1778 LA TONNELLE; NEXT AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/AgeDor; next every-10 1780'
    })
    print('spawned rq_1779')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1778',1778,'no',
        'tick1778 leftover LA TONNELLE Hannut; KBO 0431.602.587; NBB YE2025 CA 6764837 staff 4006575 VTE 63.2 pnl 456687 dividend 525000 related FVA 3354539 controllers 2920500 related debt 7555451 RIVAGE gage 135600000 equity DROP; FOI RIZIV/related recv/RIVAGE share/dividend; Brembloem still no JR2025; AGB Bornem JR2024; CDN live AgeDor 00176187; NOT every-10 (next 1780); next rq_1779 AGB/NSZ-if-200/Bosgroep/Brembloem-if-200/AgeDor; continuous hole_fill'])
print('OK')
