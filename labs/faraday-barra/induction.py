"""Modelos ideais SI: barra móvel e E azimutal de fluxo cilíndrico imposto.
Sem autoindutância, radiação, franja ou ajuste de dados reais.
"""
from math import pi,isfinite

def number(x):
    if isinstance(x,bool):raise ValueError("Real finito necessário.")
    try:x=float(x)
    except (ValueError,TypeError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(x):raise ValueError("Real finito necessário.")
    return x

def rod(b,length,velocity,resistance):
    b,length,velocity,resistance=map(number,(b,length,velocity,resistance))
    if length<=0 or resistance<=0:raise ValueError("Comprimento e resistência positivos necessários.")
    emf=number(-b*length*velocity);current=number(emf/resistance)
    force=number(current*length*b);external=number(-force)
    heat=number(current*current*resistance);power=number(external*velocity)
    return dict(emf=emf,current=current,magnetic_force_x=force,external_force_x=external,
                joule_power=heat,external_power=power)

def circular_e(radius,field_radius,b_rate):
    radius,field_radius,b_rate=map(number,(radius,field_radius,b_rate))
    if radius<0 or field_radius<=0:raise ValueError("r>=0 e a>0 necessários.")
    if radius==0:return dict(e_phi=0.,emf=0.,flux_rate=0.)
    area=number(pi*min(radius,field_radius)**2)
    rate=number(area*b_rate);emf=number(-rate);e=number(emf/(2*pi*radius))
    return dict(e_phi=e,emf=emf,flux_rate=rate)

if __name__=='__main__':
    print(rod(.5,.2,3,2))
    for r in [.05,.1,.2]:print(r,circular_e(r,.1,.2))
