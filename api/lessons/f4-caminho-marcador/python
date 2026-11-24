"""Duas alternativas e marcador2D, amplitudes complexas racionais."""
from fractions import Fraction as Q

def scalar(x,lo=-1,hi=1):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or not lo<=x<=hi:
        raise ValueError('Use int/Fraction no intervalo declarado')
    return Q(x)

def marker(t):
    t=scalar(t,0,1)
    return (1-t*t)/(1+t*t),2*t/(1+t*t)

def amplitudes(t,phase=(1,0)):
    g,h=marker(t)
    if not isinstance(phase,(tuple,list)) or len(phase)!=2:raise ValueError('Fase(cosseno,seno)')
    c,s=map(scalar,phase)
    if c*c+s*s!=1:raise ValueError('Fase precisa ter módulo1')
    return (((1+g*c)/2,g*s/2),(h*c/2,h*s/2),
            ((1-g*c)/2,-g*s/2),(-h*c/2,-h*s/2))

def norm2(z):return z[0]**2+z[1]**2

def probabilities(t,phase=(1,0)):
    a=amplitudes(t,phase)
    plus=norm2(a[0])+norm2(a[1]);minus=norm2(a[2])+norm2(a[3])
    assert plus+minus==1
    return plus,minus

if __name__=='__main__':
    for phase in ((1,0),(0,1),(-1,0)):
        p,m=probabilities(Q(1,3),phase)
        print('fase',phase,'P+',p,'P-',m,'médias em200:',200*p,200*m)
    assert probabilities(1)==(Q(1,2),Q(1,2))
