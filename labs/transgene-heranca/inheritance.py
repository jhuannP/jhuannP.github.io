"""Herança e observação em modelo sintético, sem protocolo experimental."""
from fractions import Fraction as Q
from math import comb

def prob(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or not 0<=x<=1:
        raise ValueError('Probabilidade inteira/Fraction em [0,1]')
    return Q(x)

def cross(a,b):
    """a,b=0,1,2 homólogos com T num único locus diploide autossômico.
    Não é contagem de cópias moleculares de um transgene.
    Saída: probabilidades de +/+, T/+, T/T na concepção.
    """
    if any(isinstance(x,bool) or type(x) is not int or x not in (0,1,2) for x in (a,b)):
        raise ValueError('Dose de locus inteira 0,1,2')
    pa=Q(a,2);pb=Q(b,2)
    return ((1-pa)*(1-pb),pa*(1-pb)+(1-pa)*pb,pa*pb)

def viable(distribution,survival):
    """Condiciona à sobrevivência; não altera a distribuição na concepção."""
    distribution=tuple(prob(v) for v in distribution)
    survival=tuple(prob(v) for v in survival)
    if len(distribution)!=3 or len(survival)!=3 or sum(distribution)!=1:
        raise ValueError('Três genótipos, distribuição normalizada')
    weights=tuple(p*s for p,s in zip(distribution,survival));total=sum(weights)
    if not total:raise ValueError('Evento condicionante de probabilidade zero')
    return tuple(w/total for w in weights)

def any_independent(probabilities):
    ps=tuple(prob(x) for x in probabilities)
    if not 1<=len(ps)<=8:raise ValueError('Use 1..8 loci independentes')
    absent=Q(1)
    for x in ps:absent*=1-x
    return 1-absent

def observed(carrier,sensitivity,false_positive=0):
    p=prob(carrier);s=prob(sensitivity);f=prob(false_positive)
    return p*s+(1-p)*f

def binomial(n,k,p):
    if any(isinstance(x,bool) or type(x) is not int for x in (n,k)) or not 0<=k<=n<=20:
        raise ValueError('Inteiros 0<=k<=n<=20')
    p=prob(p)
    return comb(n,k)*p**k*(1-p)**(n-k)

if __name__=='__main__':
    print('T/+ x +/+: ',cross(1,0))
    print('T/+ x T/+: ',cross(1,1))
    print('Sobreviventes sem T/T:',viable(cross(1,1),(1,1,0)))
    print('P(6 positivos em8), p=1/2:',binomial(8,6,Q(1,2)))
    print('Detecção com sensibilidade3/4:',observed(Q(1,2),Q(3,4)))
