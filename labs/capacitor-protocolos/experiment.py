"""Estados inicial/final de capacitor linear com dielétrico ideal.
C em microfarad, V em volt, Q em microcoulomb, energias/trabalho em microjoule.
"""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):raise ValueError("Use int/Fraction, sem bool")
    return Q(x)

def protocol(C0,V0,kappa,mode):
    C0,V0,kappa=map(scalar,(C0,V0,kappa))
    if C0<=0 or kappa<1:raise ValueError("C0 positivo e kappa>=1")
    if mode not in ("charge","voltage"):raise ValueError("Modo charge ou voltage")
    Q0=C0*V0;U0=C0*V0*V0/2;C=kappa*C0
    if mode=="charge":
        charge=Q0;voltage=charge/C
    else:
        voltage=V0;charge=C*voltage
    U=charge*voltage/2
    battery=Q(0) if mode=="charge" else -V0*(charge-Q0)
    delta=U-U0
    return dict(C=C,Q=charge,V=voltage,U=U,Q0=Q0,U0=U0,
                deltaU=delta,batteryEnergy=battery,externalWork=delta+battery)

if __name__=="__main__":
    a=protocol(2,3,3,"charge");b=protocol(2,3,3,"voltage")
    assert (a["Q"],a["V"],a["U"],a["externalWork"])==(6,1,3,-6)
    assert (b["Q"],b["V"],b["U"],b["batteryEnergy"],b["externalWork"])==(18,3,27,-36,-18)
    print("Carga fixa:",a)
    print("Tensão fixa:",b)
