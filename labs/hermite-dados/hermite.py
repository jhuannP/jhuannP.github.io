"""Hermite em um intervalo, aritmética racional e derivadas em x."""
from fractions import Fraction as F

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise TypeError('Use int ou Fraction; não use float.')
    if abs(x)>10**6: raise ValueError('Magnitude didática até um milhão.')
    return F(x)

def evaluate(a,b,y0,y1,d0,d1,x):
    a,b,y0,y1,d0,d1,x=map(rational,(a,b,y0,y1,d0,d1,x))
    if a>=b: raise ValueError('Nós crescentes distintos.')
    if not a<=x<=b: raise ValueError('Este laboratório não extrapola.')
    h=b-a;t=(x-a)/h
    basis=(2*t**3-3*t*t+1,t**3-2*t*t+t,-2*t**3+3*t*t,t**3-t*t)
    dbasis=(6*t*t-6*t,3*t*t-4*t+1,-6*t*t+6*t,3*t*t-2*t)
    data=(y0,h*d0,y1,h*d1)
    value=sum(c*v for c,v in zip(basis,data))
    derivative=sum(c*v for c,v in zip(dbasis,data))/h
    return value,derivative

def bound(a,b,M):
    a,b,M=map(rational,(a,b,M))
    if a>=b or M<0: raise ValueError('Intervalo crescente e M não negativo.')
    return M*(b-a)**4/384

if __name__=='__main__':
    value,slope=evaluate(-1,1,1,1,-4,4,0)
    print('f(x)=x⁴ em [-1,1]: H(0)=',value,'f(0)=0; limite=',bound(-1,1,24))
    assert value==-1 and slope==0 and bound(-1,1,24)==1
    clean=evaluate(0,2,0,8,0,12,1)[0]
    noisy=evaluate(0,2,0,8,F(1,4),12,1)[0]
    print('x³ em [0,2]: ponto médio limpo',clean,'derivada inicial perturbada',noisy)
    assert clean==1 and noisy==F(17,16)
