"""Modelo reduzido consistente v=tau/pi+d, h=c*tau+d*pi. Não é dado de gás real."""
from fractions import Fraction as F
import math

def rational(x):
    if type(x) is int:return F(x)
    if isinstance(x,F):return x
    raise ValueError("use int ou Fraction")

def state(tau,pi,d,c=3):
    tau,pi,d,c=map(rational,(tau,pi,d,c))
    if tau<=0 or pi<=0 or c<=1:raise ValueError("tau,pi>0 e c>1")
    v=tau/pi+d
    if v<=0:raise ValueError("volume do modelo precisa ser positivo")
    return {"tau":tau,"pi":pi,"v":v,"h":c*tau+d*pi,"u":(c-1)*tau,"mu":-d/c,"c":c,"d":d}

def throttle(tau,pi1,pi2,d,c=3):
    first=state(tau,pi1,d,c);pi2=rational(pi2)
    if not 0<pi2<first['pi']:raise ValueError("queda de pressão necessária")
    tau2=(first['h']-first['d']*pi2)/first['c']
    return first,state(tau2,pi2,d,c)

def entropy_change(first,last):
    # sigma=s_m/R; logaritmos somente de razões adimensionais positivas.
    if first['c']!=last['c'] or first['d']!=last['d']:raise ValueError("mesmo modelo necessário")
    return float(first['c'])*math.log(float(last['tau']/first['tau']))-math.log(float(last['pi']/first['pi']))

if __name__=="__main__":
    for d in (-1,0,1):
        before,after=throttle(1,F(1,10),F(1,20),d)
        print("d=",d,"tau2=",after['tau'],"delta h=",after['h']-before['h'],"delta sigma≈",entropy_change(before,after))
