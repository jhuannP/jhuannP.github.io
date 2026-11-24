"""Declared physical representation and availability; not inferred provenance."""
from fractions import Fraction as Q
from importlib import import_module
OLS=import_module('labs.regressao-afim.ols')
MASS={'kg':Q(1),'g':Q(1,1000)}
SPEED={'m/s':Q(1),'cm/s':Q(1,100),'km/h':Q(5,18)}


def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError('Use int/Fraction without bool/float')
    return Q(x)


def feature(mass,speed,mass_unit='kg',speed_unit='m/s'):
    """Return m*v**2 in kg*m**2/s**2, for a signed 1D velocity component."""
    mass,speed=number(mass),number(speed)
    if mass<=0:raise ValueError('Positive mass required')
    if mass_unit not in MASS or speed_unit not in SPEED:raise ValueError('Unsupported units')
    return mass*MASS[mass_unit]*(speed*SPEED[speed_unit])**2


def feature_at(mass,speed,mass_known_at,speed_known_at,predict_at):
    """Inputs in SI; timestamps share an arbitrary common time coordinate."""
    tm,tv,tp=map(number,(mass_known_at,speed_known_at,predict_at))
    if max(tm,tv)>tp:raise ValueError('Input declared unavailable at prediction time')
    return feature(mass,speed)


def dimensionless(mass,speed,m0,v0):
    mass,speed,m0,v0=map(number,(mass,speed,m0,v0))
    if min(mass,m0,v0)<=0:raise ValueError('Positive mass and reference scales required')
    return (mass/m0)*(speed/v0)**2


# Prescribed synthetic training: mass kg, signed velocity m/s, target kinetic energy J.
TRAIN=((1,2,2),(2,2,4),(1,4,8))


def comparison():
    good=[(feature(m,v),Q(y)) for m,v,y in TRAIN]
    lost=[(Q(v*v),Q(y)) for m,v,y in TRAIN]
    return OLS.fit(good), OLS.fit(lost), good, lost


if __name__=='__main__':
    good,lost,good_data,lost_data=comparison()
    print('m*v²',good,'training MSE',OLS.mse(good,good_data))
    print('v² only',lost,'training MSE',OLS.mse(lost,lost_data))
    print('unit conversion',feature(1000,200,'g','cm/s'))
    print('new prescribed state m2,v3',good.predict(feature(2,3)))
    print('dimensionless m2,v3,m0=2,v0=3',dimensionless(2,3,2,3))
