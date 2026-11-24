"""Balanço local de taxas médias em duas pontas; sem dinâmica de ATP ou nucleação."""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction; bool não é taxa")
    return Q(x)

def rates(c,kon_plus=3,koff_plus=3,kon_minus=1,koff_minus=5):
    c,kp,dp,km,dm=map(scalar,(c,kon_plus,koff_plus,kon_minus,koff_minus))
    if c<0 or kp<=0 or km<=0 or dp<0 or dm<0:
        raise ValueError("c e koff não negativos; kon positivos")
    vp=kp*c-dp;vm=km*c-dm
    return dict(c=c,critical_plus=dp/kp,critical_minus=dm/km,
                balance_c=(dp+dm)/(kp+km),v_plus=vp,v_minus=vm,net=vp+vm,
                stationary_flow=(vp+vm==0 and vp!=0),
                both_balanced=(vp==0 and vm==0))

if __name__=="__main__":
    for c in (0,1,2,3,5,6):
        print(rates(c))
    s=rates(2)
    assert (s["v_plus"],s["v_minus"],s["net"])==(3,-3,0)
    assert s["stationary_flow"] and not s["both_balanced"]
