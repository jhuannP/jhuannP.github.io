"""Dois sólidos rígidos isolados, capacidades constantes, sem mudança de fase.
Equilíbrio final; não calcula gradientes nem tempo de relaxação. Valores em SI.
"""
from math import log, isclose

def balance(ch,cc,th,tc):
    if any(type(v) not in (int,float) for v in (ch,cc,th,tc)):
        raise ValueError('use números sem bool')
    from math import isfinite
    ch,cc,th,tc=map(float,(ch,cc,th,tc))
    if not all(isfinite(v) and v>0 for v in (ch,cc,th,tc)) or th<tc:
        raise ValueError('capacidades positivas; TH>=TC>0 K, finitos')
    tf=(ch*th+cc*tc)/(ch+cc)
    if not isfinite(tf):raise ArithmeticError('escala fora da representação')
    return dict(tf=tf,heat_cold=cc*(tf-tc),ds_hot=ch*log(tf/th),
                ds_cold=cc*log(tf/tc))

def simpson_entropy(cap,start,end,n=1000):
    # Integration path is auxiliary/reversible, not the actual heat-flow trajectory.
    h=(end-start)/n
    return h/3*(cap/start+cap/end+sum((4 if k%2 else 2)*cap/(start+k*h) for k in range(1,n)))

if __name__=='__main__':
    for ch,cc,th,tc in [(2,2,600,300),(1,3,500,250),(4,2,300,300)]:
        r=balance(ch,cc,th,tc);tf=r['tf']
        assert isclose(ch*(tf-th)+cc*(tf-tc),0,abs_tol=1e-10)
        for cap,start,key in [(ch,th,'ds_hot'),(cc,tc,'ds_cold')]:
            assert isclose(simpson_entropy(cap,start,tf),r[key],rel_tol=1e-10,abs_tol=1e-12)
        assert r['ds_hot']+r['ds_cold']>=-1e-12
        print(r,'ΔS total:',r['ds_hot']+r['ds_cold'])
    r=balance(2,2,600,300)
    assert isclose(r['ds_hot']+r['ds_cold'],2*log(9/8))
