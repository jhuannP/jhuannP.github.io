"""Um multiplete isotrópico isolado; momento e campo adimensionais."""
from math import exp,fsum,isfinite,sqrt

def number(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v):
        raise ValueError('Número real finito, sem bool')
    return float(v)

def response(twice_s,g,x):
    if isinstance(twice_s,bool) or not isinstance(twice_s,int) or not 0<=twice_s<=20:
        raise ValueError('2S inteiro de 0 a 20')
    g=number(g);x=number(x)
    if not 0<g<=10 or abs(x)>1000:raise ValueError('0<g<=10 e |x|<=1000')
    s=twice_s/2
    projections=[-s+i for i in range(twice_s+1)]
    exponents=[g*x*m for m in projections];shift=max(exponents)
    weights=[exp(a-shift) for a in exponents];z=fsum(weights)
    probabilities=[w/z for w in weights]
    mean=fsum(m*p for m,p in zip(projections,probabilities))
    variance=fsum((m-mean)**2*p for m,p in zip(projections,probabilities))
    return dict(projections=projections,probabilities=probabilities,
                moment=g*mean,slope=g*g*variance,
                curie_slope=g*g*s*(s+1)/3,
                effective=g*sqrt(s*(s+1)),saturation=g*s)

if __name__=='__main__':
    for x in (0,.01,1,10):
        a=response(4,2,x)
        print('x=',x,'momento/μB=',a['moment'],'tangente Curie=',8*x)
