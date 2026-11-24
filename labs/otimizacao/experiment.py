"""Otimização de área: referências racionais e domínio fechado."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def area(P,x):
    P,x=rational(P),rational(x)
    if P<=0:raise ValueError('Perímetro positivo.')
    if not 0<=x<=P/2:raise ValueError('Lados não negativos.')
    return x*(P/2-x)


def best_rectangle(P,lower=0,upper=None):
    P,lower=rational(P),rational(lower)
    upper=P/2 if upper is None else rational(upper)
    if P<=0 or not 0<=lower<=upper<=P/2:raise ValueError('Intervalo admissível inválido.')
    # Comparação de fronteiras e do ponto estacionário quando admissível.
    candidates=[lower,upper]
    if lower<=P/4<=upper:candidates.append(P/4)
    x=max(candidates,key=lambda v:area(P,v))
    return dict(x=x,y=P/2-x,area=area(P,x),candidates=candidates)


def loss(P,x):
    P,x=rational(P),rational(x)
    return P*P/16-area(P,x)


if __name__=='__main__':
    print('Perímetro 20 m:',best_rectangle(20))
    print('Restrição 0≤x≤3 m:',best_rectangle(20,0,3))
    print('Perda ao escolher x=3 m:',loss(20,3),'m²')
    print('Derivada zero de x³ em 0 não fornece extremo: −1<0<1.')
    print('Uma grade finita não garante encontrar um extremo contínuo.')
