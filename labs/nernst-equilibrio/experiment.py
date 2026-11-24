"""Nernst ideal de um íon; voltagem interior menos exterior, sem dinâmica."""
from math import log,isfinite
R,F=8.314,96485.0  # J/(mol K), C/mol; valores arredondados

def finite(x):return not isinstance(x,bool) and isinstance(x,(int,float)) and isfinite(x)

def energy(ci,co,V_mV,z=1,T=310.):
    if any(not finite(x) or x<=0 for x in (ci,co,T)) or not finite(V_mV) or type(z) is not int or z==0:
        raise ValueError("Concentrações/T positivas finitas, V finito e z inteiro não nulo")
    chemical=R*T*log(ci/co)
    electrical=z*F*V_mV/1000
    return dict(E_mV=-1000*chemical/(z*F),chemical=chemical,electrical=electrical,
                total=chemical+electrical)

def model(kind=0,q=1,V=0):
    if type(kind) is not int or kind not in (0,1) or type(q) is not int or q not in range(-2,3) or not finite(V) or not -150<=V<=150:
        raise ValueError("Tipo0/1, q−2..2 inteiros; V em[−150,150]mV")
    z=(1,-1)[kind];a=energy(10.**q,1.,V,z)
    return dict(kind=kind,q=q,V=V,z=z,ratio=10.**q,**a)

if __name__=="__main__":
    a=model();eq=energy(10,1,a["E_mV"])
    assert abs(eq["total"])<1e-9
    print(a);print("No equilíbrio:",eq)
