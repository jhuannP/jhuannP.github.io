"""Translação acelerada 1D: mecânica newtoniana, sem rotação."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiros ou Fraction para a referência exata.')
    return Q(x)


def motion(m,F,A,t,x0=0,v0=0,X0=0,V0=0):
    m,F,A,t,x0,v0,X0,V0=map(rational,(m,F,A,t,x0,v0,X0,V0))
    if m<=0 or t<0:raise ValueError('Massa positiva e tempo não negativo.')
    a=F/m
    x=x0+v0*t+a*t*t/2
    X=X0+V0*t+A*t*t/2
    return dict(x=x,X=X,relative_x=x-X,v=v0+a*t,relative_v=v0+a*t-V0-A*t,
                a=a,relative_a=a-A,inertial_force=-m*A,effective_force=F-m*A)


def floor_normal(m,g,A):
    m,g,A=map(rational,(m,g,A))
    if m<=0 or g<=0:raise ValueError('Massa e módulo de g positivos.')
    if A < -g:raise ValueError('Contato com piso não pode sustentar normal negativa.')
    return m*(g+A)


if __name__=='__main__':
    print('Partícula livre vista de origem acelerada:',motion(2,0,1,2))
    print('Força física 6 N e massa 2 kg; origem acelera 1 m/s²:',motion(2,6,1,2))
    print('Normal no piso: m=2 kg, g=10 m/s², A=2 m/s² para cima:',floor_normal(2,10,2),'N')
    print('O termo −mA não é interação entre dois corpos; decorre do referencial.')
