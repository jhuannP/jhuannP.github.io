"""Contagem exata e análise de sensibilidade de um modelo didático.
Não fornece raios/energias tabelados de átomos polieletrônicos.
"""
from fractions import Fraction as Q

def electrons(Z,charge):
    if any(isinstance(v,bool) or not isinstance(v,int) for v in (Z,charge)):
        raise ValueError("Z e carga precisam ser inteiros")
    if Z<1 or Z-charge<0:raise ValueError("Contagem inválida")
    return Z-charge

def scales(n,Z,S):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:raise ValueError("n inteiro positivo")
    if any(isinstance(v,bool) or not isinstance(v,(int,Q)) for v in (Z,S)):
        raise ValueError("Parâmetros racionais")
    if Z<=0 or S<0 or Z<=S:raise ValueError("Exige Z>S>=0")
    eff=Q(Z)-S
    return Q(n*n)/eff,eff*eff/(n*n)

def verify():
    # A conservação de carga é independente do modelo de escalas.
    for Z in range(1,31):
        for q in range(-3,min(Z,4)+1):
            N=electrons(Z,q);assert Z-N==q
    assert [electrons(z,z-10) for z in (8,9,10,11,12,13)]==[10]*6
    count=0
    for n in (1,2,3,4):
        for Z in (4,8,12):
            for S in (0,1,2):
                r,b=scales(n,Z,S)
                r2,b2=scales(n,Z+1,S)
                assert r2<r and b2>b
                rn,bn=scales(2*n,Z,S)
                assert rn==4*r and bn==b/4
                rs,bs=scales(n,Z,Q(S)+Q(1,2))
                assert rs>r and bs<b
                count+=1
    r1,b1=scales(2,8,5);r2,b2=scales(2,10,5)
    assert (r1,b1,r2,b2)==(Q(4,3),Q(9,4),Q(4,5),Q(25,4))
    assert r2/r1==Q(3,5) and b2/b1==Q(25,9)
    for args in ((0,8,5),(2,5,5),(2,4,5),(True,8,5),(2,8,-1)):
        try:scales(*args)
        except ValueError:pass
        else:raise AssertionError("contrato")
    print(f"{count} configurações de escalas, contagens de carga, razões e contratos conferidos")
    print("Parâmetros fictícios I/II: r*, B* =",(r1,b1),(r2,b2))

if __name__=='__main__':verify()
