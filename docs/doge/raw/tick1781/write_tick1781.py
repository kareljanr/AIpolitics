import csv
from pathlib import Path
csv.field_size_limit(10_000_000)
data=Path('docs/doge/data')
tick='1781'; utc='2026-08-24T20:35:00Z'
eid='nv_brembloem_immo'; sid='src_brembloem_immo_jr2025_nbb'
gap='gap_brembloem_immo_marge_1_27m_debt_8_65m_mortgage_l5'
lb='lb_brembloem_immo_marge_1_27m_debt_8_65m_mortgage_l5'
comm='comm_brembloem_immo_jr2025_marge_1_27m'
hier='Vlaanderen>Provincies>Oost-Vlaanderen>Gemeenten>Gent>WZC>BrembloemImmo>JR2025_L5'

with open(data/'sources.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([sid,'Brembloem Immo NV NBB VKT-kap YE2025 deposit 2026-00140604','http://cdn.staatsbladmonitor.be/2026pdf/2026-00140604.pdf','Nationale Bank van België / Brembloem Immo NV','2026-08-24','primary_official','tick1781; AV 18.05.2026; VKT-kap abbrev; Bultinck bestuur; Gent Stapelplein 70; marge 1.27m; debt 8.65m; MVA 14.52m mortgage mandate 16.98m'])
    w.writerow(['src_brembloem_immo_kbo','KBO Brembloem Immo NV 0644.744.944','https://kbopub.economie.fgov.be/kbopub/toonondernemingps.html?ondernemingsnummer=0644744944','KBO','2026-08-24','primary_official','tick1781; SA/NV; Stapelplein 70 bus 100 9000 Gent; RPR Gent; NACE 88.999'])
    w.writerow(['src_brembloem_wzc_dual_pointer','Vivalto WZC Brembloem/Stuivenberg dual pointer for landlord FOI cc','https://www.vivaltohome.com/nl/maisons/stuivenberg/','Vivalto Home / WZC Brembloem','2026-08-24','primary_official','tick1781; Patrijzenstraat Evergem; administratiebrembloemstuivenberg@vivaltohome.com; Brembloem VZW still no JR2025 CDN'])

with open(data/'entities.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([eid,'Brembloem Immo NV (leftover property dual / Gent)','Brembloem Immo SA (immobilier résiduel / Gand)','Brembloem Immo NV leftover care-named property dual Gent','other','gg_belgium','nl','','','Stapelplein 70 bus 100 9000 Gent','tick1781 leftover property dual after every-10; KBO 0644.744.944 Actief; SA; official NBB VKT-kap YE2025 deposit 2026-00140604 CDN 200 14p; AV 18.05.2026; Bultinck Filip/Urbain bestuur (not Vivalto on board); name-linked to Vivalto WZC Brembloem/Stuivenberg while Brembloem VZW still no JR2025; sourced euros assets 14897447 equity 4703547 debt 8654588 MVA 14517471 marge 1274371 staff empty expl 756884 pnl 434277 LT credit 6548230 autres ST 1159029 mortgage mandate 16976379; FOI ready CA/tenant/RIZIV path/debt'])

buds=[
 ('bud_brembloem_immo_assets_2025',14897447,'stock','Assets YE2025 14897447 DROP vs 15429774; tick1781'),
 ('bud_brembloem_immo_equity_2025',4703547,'stock','Equity 4703547 UP vs 4269270; tick1781'),
 ('bud_brembloem_immo_debt_2025',8654588,'stock','Debt 8654588 DROP vs 9546617; tick1781'),
 ('bud_brembloem_immo_mva_2025',14517471,'stock','Terreinen en gebouwen 14517471; tick1781'),
 ('bud_brembloem_immo_lt_credit_2025',6548230,'stock','LT credit/leasing 172/3=6548230; tick1781'),
 ('bud_brembloem_immo_autres_st_2025',1159029,'stock','Overige schulden ST 1159029; tick1781'),
 ('bud_brembloem_immo_cash_2025',352694,'stock','Cash 352694; tick1781'),
 ('bud_brembloem_immo_marge_2025',1274371,'realized','Marge bruto 1274371 (VKT-kap; CA undisclosed); tick1781'),
 ('bud_brembloem_immo_expl_2025',756884,'realized','Bedrijfswinst 756884; 0 staff code; tick1781'),
 ('bud_brembloem_immo_pnl_2025',434277,'realized','PnL 434277; no dividend; tick1781'),
]
with open(data/'budgets.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    for bid,amt,basis,notes in buds:
        w.writerow([bid,eid,2025,amt,'','',basis,sid,'strong',notes])

with open(data/'commitments.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([comm,'Brembloem Immo NV JR2025 leftover property dual (marge 1.27m / debt 8.65m)',eid,'Brembloem Immo NV / possible WZC Brembloem tenants / residents Evergem','CSA NV; FOI best-effort private property dual for care-euro path','2026-05-18',2025,2025,1274371,'','','active','http://cdn.staatsbladmonitor.be/2026pdf/2026-00140604.pdf','Local leftover Brembloem-named property dual Gent — marge 1.27m / 14.5m buildings / mortgage mandate 17.0m','Publish CA/tenant map + link to Vivalto WZC Brembloem + debt counterparties; unit-cost',sid,'strong',hier,'tick1781; assets 14.90m equity 4.70m debt 8.65m MVA 14.52m marge 1.27m expl 0.76m pnl 0.43m LT credit 6.55m; FOI ready not sent; not TE-additive; VKT CA undisclosed; Brembloem VZW still no JR2025'])

with open(data/'leaderboard.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([lb,'Brembloem Immo NV 2025: marge 1.27m / debt 8.65m (MVA 14.52m mortgage mandate 16.98m)','L5','nursing_home_property_dual',hier.replace('>JR2025_L5',''),1274371,16976379,'Envelope=marge 1274371 (VKT; CA undisclosed); 0 staff; MVA buildings 14.52m; LT credit 6.55m; autres ST 1.16m; mortgage mandate 16.98m on 14.52m assets; name-linked to Vivalto WZC Brembloem while VZW JR2025 still missing','strong',sid,'Possible WZC Brembloem/Stuivenberg tenants / Evergem residents','Property shell for care-named Brembloem site','Care-named property dual with opaque rent CA while operating VZW JR2025 still unpublished — public-care euro path via landlord',6.0,5.5,5,6.2,'Publish CA/tenant + WZC link + debt map; chase Brembloem VZW JR2025','listed','',f'tick{tick}; FOI {gap}'])

with open(data/'foi_queue.csv','a',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow([gap,hier,eid,'NBB VKT-kap YE2025 live marge 1274371 but CA/rent split + tenant identity unpublished; LT credit 6548230 + overige ST 1159029 counterparties; mortgage inscription 25000 vs mandate 16976379 on MVA 14517471; link to Vivalto WZC Brembloem/De Molen + Brembloem VZW 0863.576.449 still no JR2025','Brembloem-named property dual with 1.27m opaque marge and 14.5m leveraged buildings while operating VZW JR2025 still missing — opacity on public care-euro rent path',8,'Brembloem Immo NV / Bestuursorgaan','administratiebrembloemstuivenberg@vivaltohome.com','Stapelplein 70 bus 100 9000 Gent',f'docs/doge/foi/drafts/{gap}.md','ready','2026-08-24','','','','',comm,lb,utc,utc,'tick1781; human-send only; private NV FOI best-effort; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403'])

path=data/'research_queue.csv'
with open(path,encoding='utf-8',newline='') as f:
    r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
    if row.get('task_id')=='rq_1781':
        row['status']='done'
        row['title']='Brembloem Immo NV JR2025 leftover property dual residual'
        row['entity_id']=eid
        row['hierarchy_target']='L5'
        row['instructions']=('Completed: Brembloem Immo NV leftover property dual Gent after every-10; '
            'KBO 0644.744.944 Actief; live JR2025 official NBB VKT-kap PDF (51230 bytes 14p deposit 2026-00140604; AV 18.05.2026; '
            'Bultinck bestuur); sourced euros assets 14897447 equity 4703547 debt 8654588 MVA 14517471 marge 1274371 '
            'expl 756884 pnl 434277 LT credit 6548230; FOI ready not sent; Brembloem VZW still no JR2025; NSZ still 403')
        row['blocked_gap_id']=gap
        row['updated_utc']=utc
        row['notes']='tick1781 Brembloem Immo leftover property dual; KBO 0644.744.944; live JR2025 NBB VKT-kap PDF; sourced euros; FOI ready not sent; next rq_1782 residual dual L5'
        print('updated rq_1781'); break
else:
    raise SystemExit('missing rq_1781')
if not any(r.get('task_id')=='rq_1782' for r in rows):
    rows.append({
        'task_id':'rq_1782','title':'leftover AGB/APB/IGS/Bosgroep/IOED/HVZ dual residual hole-fill',
        'sprint':'hole_fill','priority':'5','status':'open','hierarchy_target':'L5','entity_id':'gg_belgium',
        'instructions':('Tick 1782 after 1781 Brembloem Immo. Next every-10 is 1790. Prefer leftover AGB/APB if PDF live (Bornem still JR2024), '
                 'else NSZ/Dijk92/APEFE if CDN 200, Bosgroep residual, Brembloem VZW if CDN 200, other unused Vivalto maisons '
                 '(aux-lilas-de-bonlez / cottage-rose / e-carpentier / floreal / la-maison-dieu / charlemagne / cedre-bleu / '
                 'jardin-des-chantoirs / le-marronnier / manoir-du-menil) if CDN 200, other IOED/HVZ/IGS. '
                 'Do NOT redo Brembloem Immo/AgeDor/Tonnelle/VertBocage/Etrier/ClosRoses continuum.'),
        'blocked_gap_id':'','created_utc':utc,'updated_utc':utc,
        'notes':'spawned after tick1781 Brembloem Immo; NEXT AGB/NSZ-if-200/Bosgroep/BrembloemVZW-if-200/unused-Vivalto-maisons; next every-10 1790'
    })
    print('spawned rq_1782')
with open(path,'w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(rows)

with open(data/'loop_state.csv','w',encoding='utf-8',newline='') as f:
    w=csv.writer(f)
    w.writerow(['state_id','mode','current_sprint','last_tick_utc','last_unit_id','ticks_completed','paused','notes'])
    w.writerow(['main','continuous','hole_fill',utc,'rq_1781',1781,'no',
        'tick1781 leftover Brembloem Immo Gent; KBO 0644.744.944; NBB YE2025 marge 1274371 MVA 14517471 debt 8654588 LT credit 6548230 pnl 434277 mortgage mandate 16976379; FOI CA/tenant/WZC link; Brembloem VZW still no JR2025; AGB Bornem JR2024; NSZ/Dijk92/APEFE still 403; unused Vivalto maisons still live candidates; NOT every-10 (next 1790); next rq_1782 AGB/NSZ-if-200/Bosgroep/BrembloemVZW-if-200/unused-Vivalto; continuous hole_fill'])
print('OK')
