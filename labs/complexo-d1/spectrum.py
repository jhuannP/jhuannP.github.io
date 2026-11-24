"""Recortes exatos de energia d1 e paridade; não calcula espectro de molécula."""
from fractions import Fraction as Q
from itertools import product
H=Q(662607015,10**42)  # J s, constante SI exata
C=Q(299792458)         # m/s

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction; não float')
    return Q(x)

def d1(gap_cm):
    gap=rational(gap_cm)
    if not 1000<=gap<=50000:
        raise ValueError('Faixa didática: 1000..50000 cm^-1')
    return {'lower_cm':-Q(2,5)*gap,'upper_cm':Q(3,5)*gap,
            'gap_cm':gap,'wavelength_nm':10**7/gap,
            'frequency_hz':C*100*gap,'photon_j':H*C*100*gap}

def parity(initial,operator,final):
    if any(isinstance(x,bool) or type(x) is not int or x not in (-1,1)
           for x in (initial,operator,final)):
        raise ValueError('Paridades inteiras +1 ou -1')
    return initial*operator*final

def pair_sum(values,initial,operator,final):
    """Soma sobre pares r,-r escolhidos; se paridade ímpar cancela exatamente.
    values são valores do integrando em representantes, não orbitais calculados.
    """
    values=tuple(values)
    if not 1<=len(values)<=64:raise ValueError('Use 1..64 pares')
    sign=parity(initial,operator,final)
    return sum(((1+sign)*rational(v) for v in values),Q(0))

def borrowed_strength(epsilon):
    """|<f|mu|g0>|²/d², f=(g1+epsilon*u)/sqrt(1+epsilon²).
    g0,g1,u ortonormais; paridades +,+,-; único elemento usado mu[u,g0]=d.
    Sem autovalores do Hamiltoniano, intensidades absolutas ou molécula.
    """
    epsilon=rational(epsilon)
    if abs(epsilon)>1:raise ValueError('Recorte didático |epsilon|<=1')
    return epsilon**2/(1+epsilon**2)

if __name__=='__main__':
    print(d1(16000))
    print('Par g-dipolo-g:',pair_sum((1,2,-3),1,-1,1))
    print('Força relativa epsilon=1/5:',borrowed_strength(Q(1,5)))
