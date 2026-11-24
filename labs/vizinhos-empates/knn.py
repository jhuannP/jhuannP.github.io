"""kNN binário 1D exato: empate de distância por índice, de votos por classe0."""
from fractions import Fraction as Q

def rational(v):
    if type(v) not in (int,Q):raise ValueError('use int/Fraction sem bool')
    return Q(v)

def predict(x,y,query,k):
    if not isinstance(x,(list,tuple)) or not isinstance(y,(list,tuple)) or not x or len(x)!=len(y):raise ValueError('dados pareados não vazios')
    if any(type(v) is not int or v not in (0,1) for v in y):raise ValueError('rótulos inteiros0/1')
    if type(k) is not int or not 1<=k<=len(x):raise ValueError('1<=k<=N')
    x=[rational(v) for v in x];query=rational(query)
    ids=sorted(range(len(x)),key=lambda i:(abs(x[i]-query),i))[:k]
    ones=sum(y[i] for i in ids)
    return dict(indices=ids,distances=[abs(x[i]-query) for i in ids],ones=ones,fraction_one=Q(ones,k),label=int(2*ones>k))

if __name__=='__main__':
    from itertools import permutations
    x=[0,2,3,5,8];y=[0,0,1,1,0]
    r=predict(x,y,4,3);assert r['indices']==[2,3,1] and r['label']==1 and r['fraction_one']==Q(2,3)
    assert predict(x,y,4,5)['label']==0
    assert predict(x,y,Q(13,2),1)['label']==1
    assert predict([0,2,3,8,5],[0,0,1,0,1],Q(13,2),1)['label']==0
    # Independent rank via pairwise comparisons, not sorting the same key.
    for q in (Q(-1),Q(1),Q(4),Q(13,2),Q(100)):
        for k in range(1,6):
            result=predict(x,y,q,k)
            ranks={i:sum((abs(x[j]-q),j)<(abs(x[i]-q),i) for j in range(5)) for i in range(5)}
            selected={i for i,rank in ranks.items() if rank<k}
            assert set(result['indices'])==selected
            assert result['ones']==sum(y[i] for i in selected)
    # Away from a tied cutoff, permutations preserve the selected points and vote.
    for ids in permutations(range(5)):
        assert predict([x[i] for i in ids],[y[i] for i in ids],4,3)['label']==1
    for shift in range(-4,5):
        for scale in (Q(1,10),Q(1),Q(2),Q(100)):
            assert predict([scale*v+shift for v in x],y,scale*4+shift,3)['indices']==r['indices']
    assert all(predict(x,y,q,1)['label']==label for q,label in zip(x,y))
    assert predict(x,y,100,3)['distances'][0]==92
    assert 2**2+100**2>4**2+1**2
    assert Q(2)**2+Q(100,100)**2<Q(4)**2+Q(1,100)**2
    for args in [([],[],0,1),(x,y,4,0),(x,y,4,True),(x,[True]*5,4,3),(x,y,4.0,3)]:
        try:predict(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('q=4,k=3:',r)
    print('25 rankings,120 permutações e36 mudanças afins positivas conferidos.')
