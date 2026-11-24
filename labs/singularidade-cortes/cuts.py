"""Cortes próprios de integrais singulares: fatores exatos e logaritmos float.
Não define uma integral usual a partir de cancelamentos sincronizados.
"""
from fractions import Fraction as Q
from math import log

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def power_cut(k,degree=2):
    if type(k) is not int or not 0<=k<=256 or type(degree) is not int or degree not in (2,3):
        raise ValueError("k inteiro 0..256 e grau 2 ou 3.")
    epsilon=Q(1,2**(degree*k));tail=Q(degree,2**k)
    return dict(epsilon=epsilon,integral=Q(degree)-tail,tail=tail,limit=Q(degree))

def choose_cut(tolerance,degree=2):
    tolerance=rational(tolerance)
    if tolerance<=0:raise ValueError("Tolerância positiva.")
    if type(degree) is not int or degree not in (2,3):raise ValueError("Grau 2 ou 3.")
    for k in range(257):
        if power_cut(k,degree)['tail']<=tolerance:return k,power_cut(k,degree)
    raise ValueError("Tolerância abaixo do domínio implementado k<=256.")

def logq(v):return log(v.numerator)-log(v.denominator)

def signed_cut(epsilon_left,epsilon_right):
    left,right=map(rational,(epsilon_left,epsilon_right))
    if not 0<left<=1 or not 0<right<=1:raise ValueError("Cortes em (0,1].")
    ratio=left/right
    return dict(left=logq(left),right=-logq(right),combined=logq(ratio),ratio=ratio)

if __name__=='__main__':
    print(choose_cut(Q(1,100)))
    for e in [Q(1,10),Q(1,100)]:
        print('simétrico',signed_cut(e,e),'assimétrico',signed_cut(2*e,e))
