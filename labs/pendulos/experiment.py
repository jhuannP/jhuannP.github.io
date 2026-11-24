"""Pêndulos conservativos: período por média aritmético-geométrica."""
import math


def positive(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<=0:
        raise ValueError('Use grandeza finita positiva.')
    return float(x)


def period_ratio(theta0):
    if isinstance(theta0,bool) or not isinstance(theta0,(int,float)) or not math.isfinite(theta0) or not 0<=theta0<math.pi:
        raise ValueError('Amplitude em radianos: 0≤theta0<pi.')
    a,b=1.0,math.cos(theta0/2)
    for _ in range(60):
        new_a=(a+b)/2
        b=math.sqrt(a*b);a=new_a
        if abs(a-b)<=1e-15*a:return 1/a
    raise ArithmeticError('AGM não convergiu no limite de iteração.')


def period(length,g,theta0):
    length,g=map(positive,(length,g))
    t0=2*math.pi*math.sqrt(length/g)
    ratio=period_ratio(theta0)
    return dict(linear=t0,nonlinear=t0*ratio,ratio=ratio,excess_percent=100*(ratio-1))


def physical_length(inertia,mass,distance):
    inertia,mass,distance=map(positive,(inertia,mass,distance))
    return inertia/(mass*distance)


if __name__=='__main__':
    for degrees in (0,10,30,90,150):
        print(degrees,'graus:',period(1,10,math.radians(degrees)))
    print('Haste uniforme de 1,5 m presa na ponta; massa 2 kg:')
    print('Comprimento equivalente=',physical_length(2*1.5**2/3,2,1.5/2),'m')
    print('Amplitude zero é limite de período: um corpo parado não completa ciclos.')
