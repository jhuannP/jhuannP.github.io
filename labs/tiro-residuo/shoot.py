"""Euler racional para u''=-c*x, contorno zero em [0,1]."""
from fractions import Fraction as Q

def params(n,c):
    if isinstance(n,bool) or not isinstance(n,int) or not 2<=n<=200:
        raise ValueError('n inteiro de 2 a 200')
    if isinstance(c,bool) or not isinstance(c,(int,Q)) or not 0<c<=12:
        raise ValueError('c int/Fraction em (0,12]')
    return Q(1,n),Q(c)

def integrate(s,n,c=6):
    h,c=params(n,c)
    if isinstance(s,bool) or not isinstance(s,(int,Q)) or abs(s)>100:
        raise ValueError('s int/Fraction de módulo até100')
    u=Q(0);v=Q(s);rows=[(Q(0),u,v)]
    for k in range(n):
        x=k*h
        # Atualizações explícitas usam ambas o estado antigo.
        u,v=u+h*v,v-h*c*x
        rows.append(((k+1)*h,u,v))
    return rows

def shoot(n,c=6):
    # Duas inclinações e uma secante exata do mapa de Euler.
    a=integrate(0,n,c)[-1][1];b=integrate(2,n,c)[-1][1]
    if a==b:raise ValueError('Sem inclinação distinguível')
    s=-2*a/(b-a)
    trace=integrate(s,n,c)
    assert trace[-1][1]==0
    return s,trace

if __name__=='__main__':
    for n in (10,20,40):
        s,trace=shoot(n)
        mid=trace[n//2][1]
        print('N=',n,'s=',s,'resíduo Euler=',trace[-1][1],
              'resíduo verdadeiro=',s-1,'u(1/2)=',mid,'erro=',Q(3,8)-mid)
