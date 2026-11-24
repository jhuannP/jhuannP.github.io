"""Covariância total de uma lei finita conhecida,sem estimativa amostral."""
from fractions import Fraction as Q

def _q(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)

def model(q=Q(1,2)):
    q=_q(q)
    if not 0<=q<=1:raise ValueError('Peso entre0 e1.')
    return [(str(g),Q(4*g+u),Q(4*g-u),mass/2) for g,mass in [(0,1-q),(1,q)] for u in [-1,1]]

def moments(rows):
    ex=sum((x*w for g,x,y,w in rows),Q(0));ey=sum((y*w for g,x,y,w in rows),Q(0))
    return dict(ex=ex,ey=ey,vx=sum((w*(x-ex)**2 for g,x,y,w in rows),Q(0)),vy=sum((w*(y-ey)**2 for g,x,y,w in rows),Q(0)),cov=sum((w*(x-ex)*(y-ey) for g,x,y,w in rows),Q(0)))

def decompose(rows):
    if not isinstance(rows,(list,tuple)) or not 1<=len(rows)<=64:raise ValueError('Uma a64linhas.')
    checked=[]
    for row in rows:
        if not isinstance(row,(list,tuple)) or len(row)!=4:raise ValueError('Use grupo,x,y,peso.')
        g,x,y,w=row
        if not isinstance(g,str) or not 1<=len(g)<=32:raise ValueError('Grupo textual1–32caracteres.')
        x,y,w=map(_q,(x,y,w))
        if w<0:raise ValueError('Peso não negativo.')
        checked.append((g,x,y,w))
    if sum(w for g,x,y,w in checked)!=1:raise ValueError('Os pesos devem somar1.')
    global_m=moments(checked);within=Q(0);groups=[];mean_rows=[]
    for g in sorted({r[0] for r in checked}):
        part=[r for r in checked if r[0]==g];mass=sum(r[3] for r in part)
        if mass==0:continue
        cond=moments([(g,x,y,w/mass) for g,x,y,w in part])
        within+=mass*cond['cov'];groups.append(dict(group=g,mass=mass,**cond))
        mean_rows.append((g,cond['ex'],cond['ey'],mass))
    between=moments(mean_rows)['cov']
    return dict(global_moments=global_m,within=within,between=between,groups=groups)

if __name__=='__main__':
    for q in [Q(1,2),Q(1,16),Q(0)]:print('q=',q,decompose(model(q)))
