"""Medidas racionais em células e invariantes de elipses; não é integrador geral."""
from fractions import Fraction as Q

def rational(x,allow_zero=False):
    if type(x) not in (int,Q) or (x<0 if allow_zero else x<=0):
        raise ValueError("Use int ou Fraction positivo (zero só quando indicado)")
    return Q(x)

def sector_cell(radius,dr,dtheta):
    """Integral de r na célula; aberturas >2π contam a cobertura com multiplicidade."""
    radius=rational(radius,True);dr=rational(dr);dtheta=rational(dtheta)
    return dict(exact=(radius*dr+dr*dr/2)*dtheta,
                lower_left=radius*dr*dtheta,error=dr*dr*dtheta/2)

def ellipse(a,b,orientation=1):
    a=rational(a);b=rational(b)
    if type(orientation) is not int or orientation not in (-1,1):
        raise ValueError("Orientação deve ser +1 ou -1")
    return dict(area_over_pi=a*b,moment_over_pi=a*b*(a*a+b*b)/4,
                mean_radius_squared=(a*a+b*b)/4,jacobian_over_r=orientation*a*b)

if __name__=="__main__":
    e=ellipse(2,1)
    assert e["area_over_pi"]==2 and e["moment_over_pi"]==Q(5,2)
    c=sector_cell(2,Q(1,10),Q(1,5))
    assert c["exact"]==Q(41,1000) and c["error"]==Q(1,1000)
    print(e);print(c)
