"""Right-going crests in a stationary ideal medium; SI units, exact rationals."""
from fractions import Fraction as Q

def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)): raise ValueError('use int or Fraction')
    return Q(x)

def parameters(c,f,source=0,observer=0):
    c,f,source,observer=map(number,(c,f,source,observer))
    if c<=0 or f<=0 or abs(source)>=c or abs(observer)>=c:
        raise ValueError('positive c,f; both speeds strictly subsonic')
    return c,f,source,observer

def frequency(c,f,source=0,observer=0):
    c,f,source,observer=parameters(c,f,source,observer)
    return f*(c-observer)/(c-source)

def arrival(n,c,f,distance,source=0,observer=0):
    c,f,source,observer=parameters(c,f,source,observer)
    distance=number(distance)
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=10000 or distance<=0:
        raise ValueError('positive initial distance; integer crest index 0..10000')
    emitted=Q(n)/f
    if distance+(observer-source)*emitted<=0:
        raise ValueError('observer must remain ahead at emission for this ray family')
    return (distance+(c-source)*emitted)/(c-observer)

if __name__=='__main__':
    for n in range(3): print(n,'emissão',Q(n,20),'s; chegada',arrival(n,300,20,120,60,-30),'s')
    print('Frequência observada:',frequency(300,20,60,-30),'Hz')
