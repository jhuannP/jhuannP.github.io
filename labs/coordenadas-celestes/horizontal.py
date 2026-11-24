"""Transformação geométrica local; sem tempo civil, catálogo ou refração."""
from math import atan2,cos,degrees,hypot,isfinite,radians,sin
AZ_HORIZONTAL_EPS=1e-12

def finite(value):
    if type(value) not in (int,float):raise ValueError("Use int/float, sem bool")
    try:x=float(value)
    except OverflowError:raise ValueError("Entrada não representável") from None
    if not isfinite(x):raise ValueError("Ângulo finito necessário")
    return x

def to_horizontal(latitude_deg,declination_deg,hour_angle_deg):
    lat,dec,H=map(finite,(latitude_deg,declination_deg,hour_angle_deg))
    if not -90<lat<90 or not -90<=dec<=90 or not -180<=H<=180:
        raise ValueError("Exija -90<latitude<90, -90<=declinação<=90 e -180<=H<=180 graus")
    phi,delta,H=map(radians,(lat,dec,H))
    a=cos(delta)*cos(H);b=-cos(delta)*sin(H);c=sin(delta)
    east=b;north=-sin(phi)*a+cos(phi)*c;up=cos(phi)*a+sin(phi)*c
    horizontal=hypot(east,north)
    altitude=degrees(atan2(up,horizontal))
    azimuth=None if horizontal<=AZ_HORIZONTAL_EPS else degrees(atan2(east,north))%360
    return dict(altitude_deg=altitude,azimuth_deg=azimuth,east=east,north=north,up=up)

if __name__=="__main__":
    for H in (-90,0,90,180):print("H =",H,"graus:",to_horizontal(-30,0,H))
