"""Células convencionais cúbicas monoatômicas prescritas; sem ajuste de material."""
from fractions import Fraction as Q
from itertools import product
from math import sqrt,pi,isfinite
AVOGADRO=6.02214076e23 # mol^-1, valor SI exato; cálculo em float.

def basis(kind):
    if kind not in ('SC','BCC','FCC'): raise ValueError('SC, BCC ou FCC')
    pts=[(Q(0),)*3]
    if kind=='BCC':pts.append((Q(1,2),)*3)
    if kind=='FCC':pts.extend([(Q(0),Q(1,2),Q(1,2)),(Q(1,2),Q(0),Q(1,2)),(Q(1,2),Q(1,2),Q(0))])
    return tuple(pts)

def closed_points(kind):
    return tuple(sorted(set(tuple(b[i]+s[i] for i in range(3))
        for b in basis(kind) for s in product((-1,0,1),repeat=3)
        if all(0<=b[i]+s[i]<=1 for i in range(3)))))

def weighted_count(kind):
    # Cada coordenada na fronteira duplica o compartilhamento.
    return sum((Q(1,2**sum(x in (0,1) for x in p)) for p in closed_points(kind)),Q(0))

def nearest(kind):
    distances={}
    for shift in product((-1,0,1),repeat=3):
        for b in basis(kind):
            p=tuple(b[i]+shift[i] for i in range(3));d=sum(x*x for x in p)
            if d:distances[p]=d
    dmin=min(distances.values())
    return dmin,tuple(sorted(p for p,d in distances.items() if d==dmin))

def geometry(kind):
    d2,neighbors=nearest(kind)
    r_over_a=sqrt(float(d2))/2
    packing=len(basis(kind))*4*pi*r_over_a**3/3
    return {'atoms':weighted_count(kind),'coordination':len(neighbors),
            'distance_squared_over_a2':d2,'radius_over_a':r_over_a,'packing':packing}

def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,float,Q)):raise TypeError('real requerido')
    try:v=float(x)
    except OverflowError:raise ValueError('entrada fora da faixa') from None
    if not isfinite(v):raise ValueError('finito requerido')
    return v

def density(kind,molar_mass_g,a_pm,occupancy=Q(1)):
    n=len(basis(kind));mass=number(molar_mass_g);a=number(a_pm);f=number(occupancy)
    if not 1e-3<=mass<=1e4 or not 1<=a<=1e5 or not 0<=f<=1:
        raise ValueError('M em [1e-3,1e4] g/mol, a em [1,1e5] pm, ocupação em [0,1]')
    # 1 pm = 1e-10 cm; ocupação média prescrita, sem relaxação estrutural.
    return f*n*mass/(AVOGADRO*(a*1e-10)**3)
