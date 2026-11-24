"""Balanço adiabático com duas capacidades e recipiente opcional.
Capacidades em kJ/K, temperaturas em graus Celsius, transferências em kJ.
"""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction; sem bool")
    return Q(x)

def mix(C1,C2,T1,T2,Ccal=0,Tcal=20):
    C1,C2,T1,T2,Ccal,Tcal=map(scalar,(C1,C2,T1,T2,Ccal,Tcal))
    if C1<=0 or C2<=0 or Ccal<0:raise ValueError("Capacidades dos corpos positivas; recipiente não negativo")
    if min(T1,T2,Tcal)<Q(-27315,100):raise ValueError("Temperatura abaixo do zero absoluto")
    Tf=(C1*T1+C2*T2+Ccal*Tcal)/(C1+C2+Ccal)
    return dict(Tf=Tf,Q1=C1*(Tf-T1),Q2=C2*(Tf-T2),Qcal=Ccal*(Tf-Tcal))

if __name__=="__main__":
    r=mix(1,2,80,20,1,20)
    assert r==dict(Tf=35,Q1=-45,Q2=30,Qcal=15)
    assert sum(r[k] for k in ("Q1","Q2","Qcal"))==0
    print("Com recipiente:",r)
    print("Recipiente desprezado:",mix(1,2,80,20))
