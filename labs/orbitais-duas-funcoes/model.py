"""Problema generalizado Hc=ESc, duas funções reais equivalentes."""
from fractions import Fraction as F

def rational(x):
    if type(x) not in (int,F): raise TypeError('Use int ou Fraction')
    return F(x)

def levels(alpha,beta,overlap=0):
    a,b,s=map(rational,(alpha,beta,overlap))
    if not -1<s<1: raise ValueError('Exija |sobreposição|<1')
    return {'plus':(a+b)/(1+s),'minus':(a-b)/(1-s),
            'norm_plus_squared':2*(1+s),'norm_minus_squared':2*(1-s)}

def filling(electrons):
    """Somente ordem convencional: um orbital ligante abaixo de um antiligante."""
    if type(electrons) is not int: raise TypeError('Contagem inteira necessária')
    if not 0<=electrons<=4: raise ValueError('Dois orbitais, zero a quatro elétrons')
    bonding=min(electrons,2);antibonding=max(electrons-2,0)
    return bonding,antibonding,F(bonding-antibonding,2)

if __name__=='__main__':
    print(levels(-1,F(-2,5),F(1,5)))
    print('Ocupações e ordem formal para três elétrons:',filling(3))
