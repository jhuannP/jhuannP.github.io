"""Dilatação livre linear escolhida: metros, kelvins e coeficientes em K^-1."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool ou float.')
    return Q(x)


def length(L0,alpha,deltaT):
    L0,alpha,deltaT=map(rational,(L0,alpha,deltaT))
    if L0<=0 or alpha<0:raise ValueError('L0>0 e alpha>=0 neste recorte.')
    strain=alpha*deltaT
    if abs(strain)>Q(1,20):raise ValueError('Limite didático |alpha deltaT|<=5%.')
    return {'change':L0*strain,'final':L0*(1+strain),'strain':strain}


def square(side,alpha,deltaT):
    r=length(side,alpha,deltaT);side=rational(side)
    area0=side**2
    area=r['final']**2
    first_order=area0*(1+2*r['strain'])
    return {'area0':area0,'area':area,'first_order':first_order,
            'difference':area-first_order}


def gap(L1,a1,L2,a2,g0,deltaT):
    L1,a1,L2,a2,g0,deltaT=map(rational,(L1,a1,L2,a2,g0,deltaT))
    if g0<0:raise ValueError('Folga inicial não negativa.')
    one=length(L1,a1,deltaT);two=length(L2,a2,deltaT)
    rate=L1*a1+L2*a2
    free_gap=g0-one['change']-two['change']
    return {'free_gap':free_gap,'first_contact_deltaT':Q(0) if g0==0 else (g0/rate if rate else None),
            'status':'livre' if free_gap>0 else 'contato: modelo livre termina'}


if __name__=='__main__':
    alpha=Q(1,10000)
    print('Barra1m,deltaT50K:',length(1,alpha,50))
    print('Quadrado1m:',square(1,alpha,50))
    for t in (20,40,50):print('deltaT',t,'K:',gap(1,alpha,Q(1,2),alpha,Q(6,1000),t))
    print('Folga livre negativa é extrapolação hipotética, não sobreposição física.')
