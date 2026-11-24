"""Modelos axiais clássicos exatos; entradas SI racionais."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction.')
    return Q(x)


def inertia(particles):
    values=[]
    for part in particles:
        if len(part)!=3:raise ValueError('Cada partícula: massa,x,y.')
        m,x,y=map(rational,part)
        if m<=0:raise ValueError('Massa positiva.')
        values.append(m*(x*x+y*y))
    if not values or sum(values)<=0:raise ValueError('Inércia total positiva.')
    return sum(values)


def driven(I,w0,tau,t):
    I,w0,tau,t=map(rational,(I,w0,tau,t))
    if I<=0 or t<0:raise ValueError('Inércia positiva,tempo não negativo.')
    alpha=tau/I;w=w0+alpha*t;theta=w0*t+alpha*t*t/2
    return dict(alpha=alpha,w=w,theta=theta,L0=I*w0,L=I*w,
                impulse=tau*t,K0=I*w0*w0/2,K=I*w*w/2,
                work=tau*theta,power0=tau*w0,power=tau*w)


def rearranged(I1,I2,w1):
    I1,I2,w1=map(rational,(I1,I2,w1))
    if min(I1,I2)<=0:raise ValueError('Inércias positivas.')
    L=I1*w1;w2=L/I2
    return dict(L=L,w2=w2,K1=I1*w1*w1/2,K2=I2*w2*w2/2,
                deltaK=I2*w2*w2/2-I1*w1*w1/2)


if __name__=='__main__':
    I=inertia(((1,2,0),(1,-2,0)))
    print('Rotação rígida constanteI:',I,driven(I,1,4,2))
    print('Rearranjo,apenas estados finais:',rearranged(8,4,1))
    print('Sem dinâmica tensorial,trajetória de rearranjo ou validação experimental.')
