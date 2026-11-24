"""Interface eletrostática linear: epsilon0=1 em grandezas normalizadas."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def interface(k1,k2,E1n,Et,sigma_free):
    k1,k2,E1n,Et,sigma_free=map(rational,(k1,k2,E1n,Et,sigma_free))
    if k1<=0 or k2<=0:raise ValueError('Permissividades relativas positivas neste modelo.')
    E2n=(k1*E1n+sigma_free)/k2
    D1n=k1*E1n;D2n=k2*E2n
    P1n=(k1-1)*E1n;P2n=(k2-1)*E2n
    bound=P1n-P2n
    return dict(E1n=E1n,E2n=E2n,E1t=Et,E2t=Et,D1n=D1n,D2n=D2n,
                P1n=P1n,P2n=P2n,sigma_free=sigma_free,sigma_bound=bound,
                sigma_total=sigma_free+bound)


if __name__=='__main__':
    print('Normal de 1 para 2; E em E_ref, D/P/sigma em epsilon0 E_ref.')
    print('k1=2, k2=4, E1n=1, Et=1, sigma livre=0:',interface(2,4,1,1,0))
    print('Com sigma livre=1:',interface(2,4,1,1,1))
    print('Continuidade de D normal exige sigma livre zero; não exige E normal contínuo.')
