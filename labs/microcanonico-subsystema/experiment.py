"""Sítios distinguíveis de dois níveis, energia total exata e pesos uniformes."""
from fractions import Fraction as Q
from math import comb, log

def validate(N,q,a):
    if any(type(x) is not int for x in (N,q,a)) or N<1 or not 0<=q<=N or not 0<=a<=N:
        raise ValueError("N>=1; q e a inteiros em 0..N; bool não é contagem")

def subsystem(N,q,a):
    validate(N,q,a)
    omega=comb(N,q)
    counts=tuple(comb(a,k)*comb(N-a,q-k)
                 if 0<=q-k<=N-a else 0 for k in range(a+1))
    return dict(omega=omega,counts=counts,probabilities=tuple(Q(c,omega) for c in counts))

def pattern_probability(N,q,bits):
    bits=tuple(bits)
    validate(N,q,len(bits))
    if any(type(x) is not int or x not in (0,1) for x in bits):
        raise ValueError("Padrão deve conter apenas os inteiros 0 e 1")
    remaining=q-sum(bits)
    return Q(comb(N-len(bits),remaining),comb(N,q)) if 0<=remaining<=N-len(bits) else Q(0)

if __name__=="__main__":
    r=subsystem(8,3,3)
    assert r["omega"]==56 and r["counts"]==(10,30,15,1)
    p=r["probabilities"]
    mean=sum(k*pk for k,pk in enumerate(p))
    variance=sum((k-mean)**2*pk for k,pk in enumerate(p))
    assert mean==Q(9,8) and variance==Q(225,448)
    print("Multiplicidade global:",r["omega"])
    print("Contagens por X:",r["counts"])
    print("Probabilidades por X:",p)
    print("E[X] e Var(X):",mean,variance)
    print("S_total/kB:",log(r["omega"]))
