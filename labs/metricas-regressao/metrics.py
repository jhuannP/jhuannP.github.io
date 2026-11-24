"""Métricas escalares racionais; sem treinamento ou API geral de biblioteca."""
from fractions import Fraction as Q
from itertools import product

def metrics(y,pred):
    if not isinstance(y,(list,tuple)) or not isinstance(pred,(list,tuple)) or not y or len(y)!=len(pred):raise ValueError('pares não vazios de mesmo tamanho necessários')
    if any(type(v) not in (int,Q) for v in list(y)+list(pred)):raise ValueError('valores racionais sem bool necessários')
    y=list(map(Q,y));pred=list(map(Q,pred));n=len(y)
    errors=[b-a for a,b in zip(y,pred)];mean=sum(y)/n
    sse=sum(e*e for e in errors);sst=sum((v-mean)**2 for v in y)
    return dict(MAE=sum(abs(e) for e in errors)/n,MSE=sse/n,R2=None if sst==0 else 1-sse/sst)

if __name__=='__main__':
    cases=0
    for n in range(1,4):
        vectors=list(product((-1,0,1),repeat=n))
        for y in vectors:
            for pred in vectors:
                r=metrics(y,pred);cases+=1
                assert r['MSE']>=r['MAE']**2
                # Pairwise identity for SST, independent of subtracting the mean.
                sst=sum(Q((y[i]-y[j])**2,n) for i in range(n) for j in range(i+1,n))
                sse=sum((a-b)**2 for a,b in zip(y,pred))
                assert r['R2']==(None if sst==0 else 1-sse/sst)
                for a,b in [(Q(2),Q(7)),(Q(-1,2),Q(-3))]:
                    changed=metrics([a*x+b for x in y],[a*x+b for x in pred])
                    assert changed['MAE']==abs(a)*r['MAE']
                    assert changed['MSE']==a*a*r['MSE']
                    assert changed['R2']==r['R2']
    A=metrics([1,2,3],[1,2,7]);B=metrics([1,2,3],[3,4,5])
    assert A['MAE']==Q(4,3) and A['MSE']==Q(16,3)
    assert A['MAE']<B['MAE'] and A['MSE']>B['MSE']
    assert metrics([0,2],[3,3])['R2']==-4
    assert metrics([0,0],[0,0])['R2'] is None
    assert metrics([0,0],[1,1])['R2'] is None
    assert metrics([0,0],[0,2])['MSE']==2
    for y,pred in [([],[]),([1],[1,2]),([True],[1]),([1.],[1])]:
        try:metrics(y,pred)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print(cases,'pares alvo/previsão: SST por pares,desigualdade e duas transformações afins; referências/contratos aprovados.')
