"""Modelo original: limiar aleatório independente de X uniforme [0,1]."""
from fractions import Fraction as Q
A = (Q(1,4), Q(1,2))
PRIOR = (Q(1,2), Q(1,2))

def zero():
    evidence = sum(p*a for p,a in zip(PRIOR,A))
    weights = tuple(p*a/evidence for p,a in zip(PRIOR,A))
    mean = sum(w*a/2 for w,a in zip(weights,A))
    second = sum(w*a*a/3 for w,a in zip(weights,A))
    return evidence, weights, mean, second-mean*mean

def positive(y):
    # As fronteiras marginalmente nulas não são definidas por esta função.
    if isinstance(y,bool) or not isinstance(y,(int,Q)):
        raise TypeError("Use um racional exato")
    if not 0 < y < Q(3,4) or y == Q(1,2):
        raise ValueError("Use um ponto interior de um dos dois ramos")
    mass = tuple(p if y < 1-a else Q(0) for p,a in zip(PRIOR,A))
    density = sum(mass)
    weights = tuple(m/density for m in mass)
    mean = sum(w*(y+a) for w,a in zip(weights,A))
    variance = sum(w*(y+a-mean)**2 for w,a in zip(weights,A))
    return density,weights,mean,variance

def simpson(f,lo,hi):
    # Exato para os polinômios de grau <=3 usados aqui.
    return (hi-lo)*(f(lo)+4*f((lo+hi)/2)+f(hi))/6

def verify():
    evidence,w,mu,var=zero()
    assert (evidence,w,mu,var)==(Q(3,8),(Q(1,3),Q(2,3)),Q(5,24),Q(11,576))
    assert positive(Q(1,8))==(1,(Q(1,2),Q(1,2)),Q(1,2),Q(1,64))
    assert positive(Q(5,8))==(Q(1,2),(1,0),Q(7,8),0)
    # Probabilidades por pré-imagens de pequenas faixas: independentes da razão de densidades.
    count=0; eps=Q(1,1024)
    for i in range(1,96):
        y=Q(i,128)
        if y==Q(1,2): continue
        lengths=[max(Q(0),min(1,y+eps+a)-max(a,y-eps+a)) for a in A]
        masses=[p*t for p,t in zip(PRIOR,lengths)]
        posterior=tuple(m/sum(masses) for m in masses)
        assert posterior==positive(y)[1]
        count+=1
    # Risco integrado no espaço de origem (A,X), sem integrar a fórmula de Var(X|Y).
    risk=Q(0); predicted_mean=Q(0)
    for a,p in zip(A,PRIOR):
        pieces=[(Q(0),a,lambda x:mu),
                (a,min(Q(1),a+Q(1,2)),lambda x,a=a:x-a+Q(3,8))]
        if a+Q(1,2)<1:
            pieces.append((a+Q(1,2),Q(1),lambda x,a=a:x-a+Q(1,4)))
        for lo,hi,m in pieces:
            risk+=p*simpson(lambda x:(x-m(x))**2,lo,hi)
            predicted_mean+=p*simpson(m,lo,hi)
    assert evidence+Q(1,2)+Q(1,8)==1
    assert predicted_mean==Q(1,2)
    assert risk==Q(23,1536)==evidence*var+Q(1,2)*Q(1,64)
    known=sum(p*a**3/12 for a,p in zip(A,PRIOR))
    assert known==Q(3,512) and risk-known==Q(7,768)
    for bad in (Q(0),Q(1,2),Q(3,4),Q(-1)):
        try: positive(bad)
        except ValueError: pass
        else: raise AssertionError("fronteira aceita")
    print(f"{count} faixas interiores, momentos, normalização, risco e fronteiras conferidos")
    print("Zero:",zero(),"; leitura 1/8:",positive(Q(1,8)))

if __name__=='__main__': verify()
