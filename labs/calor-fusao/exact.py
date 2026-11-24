"""Mistura ideal: gelo a 0°C, água/recipiente na mesma temperatura inicial."""
from fractions import Fraction as Q

def solve(*,ice,water,Tw,c,L,Ccal=0):
    values=(ice,water,Tw,c,L,Ccal)
    if any(type(x) not in (int,Q) for x in values):raise ValueError("Use int/Fraction; sem float/bool")
    ice,water,Tw,c,L,Ccal=map(Q,values)
    if ice<0 or water<=0 or not 0<=Tw<100 or min(c,L)<=0 or Ccal<0:
        raise ValueError("Domínio: gelo>=0, água>0, 0<=Tw<100, c,L>0, Ccal>=0")
    available=(water*c+Ccal)*Tw;needed=ice*L
    if available<needed:
        melted=available/L;Tf=Q(0);regime="ice_and_water"
    else:
        melted=ice;Tf=(available-needed)/((water+ice)*c+Ccal)
        regime="liquid_at_zero" if Tf==0 else "liquid_above_zero"
    remaining=ice-melted;liquid=water+melted
    # Enthalpy datum: solid ice at 0°C is zero; liquid at 0°C has L per kg.
    initial=water*(L+c*Tw)+Ccal*Tw
    final=liquid*(L+c*Tf)+Ccal*Tf
    return dict(Tf=Tf,melted=melted,ice_remaining=remaining,liquid=liquid,
                available=available,needed=needed,regime=regime,
                H_initial=initial,H_final=final)

if __name__=="__main__":
    for Tw in (20,40,60):
        r=solve(ice=Q(1,10),water=Q(1,5),Tw=Tw,c=4200,L=336000)
        print("Água inicial",Tw,"°C:",r['regime'],"Tf =",r['Tf'],"°C; gelo restante =",r['ice_remaining'],"kg")
