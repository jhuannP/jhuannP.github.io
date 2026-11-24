"""Poiseuille racional: valores SI e coeficientes de Q/pi e potência/pi."""
from fractions import Fraction as F

def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):raise ValueError('Use inteiro ou Fraction')
    return F(x)

def parameters(a,L,eta,drop):
    a,L,eta,drop=map(number,(a,L,eta,drop))
    if min(a,L,eta)<=0:raise ValueError('Raio,comprimento e viscosidade positivos')
    return a,L,eta,drop

def speed(a,L,eta,drop,r):
    a,L,eta,drop=parameters(a,L,eta,drop);r=number(r)
    if not 0<=r<=a:raise ValueError('Posição radial deve pertencer ao tubo')
    return drop*(a*a-r*r)/(4*eta*L)

def flow(a,L,eta,drop,density):
    a,L,eta,drop=parameters(a,L,eta,drop);density=number(density)
    if density<=0:raise ValueError('Densidade positiva')
    peak=drop*a*a/(4*eta*L);mean=peak/2
    q_over_pi=mean*a*a
    return dict(peak=peak,mean=mean,q_over_pi=q_over_pi,
                power_over_pi=drop*q_over_pi,reynolds=density*abs(mean)*2*a/eta,
                wall_stress_magnitude=abs(drop)*a/(2*L))

if __name__=='__main__':
    from math import pi
    r=flow(F(1,1000),1,F(1,10),1000,1000)
    print(r)
    print('Q em microlitros/s:',float(r['q_over_pi'])*pi*1e9)
