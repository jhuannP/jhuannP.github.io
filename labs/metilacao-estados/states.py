"""Lei de um DNA-filho uniformemente escolhido; manutenção hipotética p."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def distribution(state):
    s=tuple(map(rational,state))
    if len(s)!=3 or min(s)<0 or sum(s)!=1:
        raise ValueError('Três probabilidades não negativas de soma1.')
    return s


def cycle(state,p):
    M,H,U=distribution(state);p=rational(p)
    if not 0<=p<=1:raise ValueError('p entre0 e1.')
    hemi=M+H/2
    return p*hemi,(1-p)*hemi,U+H/2


def law(n,p,state=(1,0,0)):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=100:
        raise ValueError('n inteiro entre0 e100.')
    s=distribution(state);p=rational(p)
    if not 0<=p<=1:raise ValueError('p entre0 e1.')
    for _ in range(n):s=cycle(s,p)
    return s


def metrics(state):
    M,H,U=distribution(state)
    return dict(fully=M,any_mark=M+H,marked_targets=M+H/2)


if __name__=='__main__':
    s=law(2,Q(1,2));print('Após2 rodadas,leiM/H/U:',s)
    print('Observáveis distintos:',metrics(s))
    print('Probabilidades/expectativas,não frações medidas numa população finita.')
