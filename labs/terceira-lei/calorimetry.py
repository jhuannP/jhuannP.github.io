"""Modelo sintético de uma fase: Cp,m=alpha*T³, somente0<=T<=20K.

Não é tabela de substância real nem extrapolação validada experimentalmente.
"""
from fractions import Fraction as Q
ALPHA=Q(1,500)

def rational(x):
    if type(x) not in (int,Q):raise ValueError('use int/Fraction')
    return Q(x)

def inputs(T,alpha):
    T,alpha=map(rational,(T,alpha))
    if not 0<=T<=20 or alpha<0:raise ValueError('T em0..20K e alpha>=0')
    return T,alpha

def cp(T,alpha=ALPHA):
    T,alpha=inputs(T,alpha);return alpha*T**3

def cp_over_t(T,alpha=ALPHA):
    """Extensão contínua em zero, sem avaliar Cp(0)/0."""
    T,alpha=inputs(T,alpha);return alpha*T*T

def entropy(T,s0=0,alpha=ALPHA):
    T,alpha=inputs(T,alpha);s0=rational(s0)
    if s0<0:raise ValueError('referência não negativa neste modelo')
    return s0+alpha*T**3/3

def increment(a,b,alpha=ALPHA):
    a,alpha=inputs(a,alpha);b,_=inputs(b,alpha)
    if a>b:raise ValueError('aquecimento exige a<=b')
    return entropy(b,alpha=alpha)-entropy(a,alpha=alpha)

def phase_change(delta_h,T):
    """Salto molar de entropia para transição reversível fornecida em T>0."""
    delta_h,T=map(rational,(delta_h,T))
    if T<=0:raise ValueError('temperatura absoluta positiva')
    return delta_h/T

if __name__=='__main__':
    assert entropy(10)==Q(2,3)
    assert entropy(20)==Q(16,3)
    assert phase_change(30,10)==3
    print('S_m(10K):',entropy(10),'J/(mol K)')
