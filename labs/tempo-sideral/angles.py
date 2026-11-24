"""Relações angulares exatas; não converte data civil em tempo sideral."""
from fractions import Fraction as Q

def rational(value):
    if type(value) not in (int,Q):raise ValueError("Use int ou Fraction, sem bool/float/texto")
    return Q(value)

def wrap24(hours):
    return rational(hours)%24

def hours_to_degrees(hours):
    return 15*rational(hours)

def clock_hours(value):
    x=rational(value)
    if not 0<=x<24:raise ValueError("Ângulo em horas exige 0<=h<24")
    return x

def local_sidereal_hours(greenwich_hours,longitude_east_deg):
    gst=clock_hours(greenwich_hours);lon=rational(longitude_east_deg)
    if not -180<=lon<=180:raise ValueError("Longitude leste positiva entre -180 e 180 graus")
    return wrap24(gst+lon/15)

def hour_angle_hours(local_sidereal,ra_hours):
    lst,ra=map(clock_hours,(local_sidereal,ra_hours))
    return (lst-ra+12)%24-12  # ramo [-12h,+12h)

if __name__=="__main__":
    for gst,lon,ra in ((22,30,Q(47,2)),(2,-45,1)):
        lst=local_sidereal_hours(gst,lon);H=hour_angle_hours(lst,ra)
        print("GST =",gst,"h; longitude leste =",lon,"°; α =",ra,"h")
        print("TSL =",lst,"h; H =",H,"h =",hours_to_degrees(H),"°")
