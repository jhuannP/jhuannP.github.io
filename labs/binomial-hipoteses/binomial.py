"""PMFs exatas: independência é hipótese,não conclusão da soma."""
from fractions import Fraction as Q
from math import comb

def probability(p):
    if isinstance(p,bool) or not isinstance(p,(int,Q)) or not 0<=p<=1:
        raise ValueError('p int/Fraction entre0 e1')
    return Q(p)

def pmf(n,p):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=100:raise ValueError('n inteiro0..100')
    p=probability(p)
    if p==0:return (Q(1),)+(Q(0),)*n
    if p==1:return (Q(0),)*n+(Q(1),)
    return tuple(comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1))

def independent_sum(ps):
    if not isinstance(ps,(list,tuple)) or len(ps)>100:raise ValueError('Lista de até100 probabilidades')
    weights=(Q(1),)
    for p in ps:
        p=probability(p);new=[Q(0)]*(len(weights)+1)
        for k,w in enumerate(weights):
            new[k]+=(1-p)*w;new[k+1]+=p*w
        weights=tuple(new)
    return weights

def moments(weights):
    if not isinstance(weights,(list,tuple)) or not 1<=len(weights)<=101:
        raise ValueError('PMF de suporte0..n até100')
    weights=tuple(probability(w) for w in weights)
    if sum(weights)!=1:raise ValueError('PMF precisa somar1')
    mean=sum((k*w for k,w in enumerate(weights)),Q(0))
    variance=sum(((k-mean)**2*w for k,w in enumerate(weights)),Q(0))
    return mean,variance

if __name__=='__main__':
    weights=pmf(4,Q(1,4))
    assert weights==tuple(Q(k,256) for k in (81,108,54,12,1))
    print(weights,'média/variância',moments(weights),'P(S>=1)',1-weights[0])
    print('heterogêneos',independent_sum([Q(1,4),Q(3,4)]))
