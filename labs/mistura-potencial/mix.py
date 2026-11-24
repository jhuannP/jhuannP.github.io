"""Mistura binária ideal a T,P fixas; quantidades em mol."""
from math import log,isfinite
R=8.314462618

def real(v):
    if isinstance(v,bool):raise ValueError('Número real finito necessário')
    try:v=float(v)
    except (TypeError,ValueError,OverflowError):raise ValueError('Número real finito necessário') from None
    if not isfinite(v):raise ValueError('Número real finito necessário')
    return v

def mix(a,b,T=300):
    a,b,T=map(real,(a,b,T));n=a+b
    if min(a,b)<0 or n<=0 or T<=0 or not isfinite(n):raise ValueError('Quantidades não negativas,total e T positivos')
    x=a/n;y=b/n
    if (a>0 and x==0) or (b>0 and y==0):raise ValueError('Fração abaixo da resolução flutuante')
    h=sum(v*log(z) for v,z in ((a,x),(b,y)) if v>0)
    return dict(x=x,y=y,h=h,G=R*T*h,S=-R*h,H=0.0,
                muA=None if a==0 else R*T*log(x),
                muB=None if b==0 else R*T*log(y))

if __name__=='__main__':
    m=mix(1,1);new=mix(2,1)
    print(m)
    print('Adição de 1 mol A: ΔGmix/(RT)=',new['h']-m['h'],'mol')
