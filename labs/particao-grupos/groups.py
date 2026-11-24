"""Níveis inteiros E/epsilon e q=exp(-beta epsilon) racional, 0<q<1."""
from fractions import Fraction as Q
from math import log,isclose

def grouped(levels,g,q):
    if not isinstance(levels,(list,tuple)) or not isinstance(g,(list,tuple)) or not 1<=len(levels)<=20 or len(levels)!=len(g):raise ValueError('grupos pareados1..20')
    if any(type(e) is not int or abs(e)>100 for e in levels) or any(type(n) is not int or not 1<=n<=100 for n in g):raise ValueError('níveis inteiros-100..100 e multiplicidades1..100')
    if type(q) not in (int,Q) or not 0<q<1:raise ValueError('q racional em(0,1)')
    q=Q(q);weights=[n*q**e for e,n in zip(levels,g)];z=sum(weights);p=[w/z for w in weights]
    mean=sum(v*e for v,e in zip(p,levels));var=sum(v*(e-mean)**2 for v,e in zip(p,levels))
    micro=[v/n for v,n in zip(p,g) for _ in range(n)]
    entropy=-sum(float(v)*log(float(v)) for v in micro)
    label_entropy=-sum(float(v)*log(float(v)) for v in p)
    return dict(z=z,p=p,mean=mean,variance=var,micro=micro,entropy=entropy,label_entropy=label_entropy)

if __name__=='__main__':
    r=grouped([0,1],[1,3],Q(1,3))
    assert r['z']==2 and r['p']==[Q(1,2),Q(1,2)]
    assert r['micro']==[Q(1,2),Q(1,6),Q(1,6),Q(1,6)]
    assert r['mean']==Q(1,2) and r['variance']==Q(1,4)
    assert isclose(r['entropy'],log(2)+log(3)/2)
    cases=0
    for q in (Q(1,10),Q(1,3),Q(1,2),Q(9,10)):
        for levels,g in [([0,1],[1,3]),([0,0],[1,3]),([0,1,2],[2,1,4])]:
            a=grouped(levels,g,q)
            # Expand levels first, normalize each explicit state independently of grouped weights.
            energies=[e for e,n in zip(levels,g) for _ in range(n)]
            weights=[q**e for e in energies];z=sum(weights);p=[w/z for w in weights]
            assert p==a['micro'] and z==a['z']
            assert sum(v*e for v,e in zip(p,energies))==a['mean']
            assert sum(v*(e-a['mean'])**2 for v,e in zip(p,energies))==a['variance']
            assert isclose(a['entropy']-a['label_entropy'],sum(float(v)*log(n) for v,n in zip(a['p'],g)),abs_tol=1e-12)
            b=grouped([e+3 for e in levels],g,q)
            assert b['p']==a['p'] and b['variance']==a['variance'] and b['mean']==a['mean']+3
            assert b['z']==q**3*a['z']
            cases+=1
    for args in [([0],[True],Q(1,2)),([0],[0],Q(1,2)),([0,1],[1],Q(1,2)),([0],[1],0.5),([0],[1],1)]:
        try:grouped(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('Caso q=1/3:',r)
    print('Agrupamento, expansão e deslocamento conferidos em',cases,'cenários.')
