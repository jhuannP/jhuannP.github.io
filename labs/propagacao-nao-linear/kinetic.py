"""K=mV²/2, massa exata, V uniforme em [v0-a,v0+a], SI."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float/texto')
    return Q(x)

def energy_moments(mass_kg,velocity_center,velocity_half_width):
    m,v,a=map(rational,(mass_kg,velocity_center,velocity_half_width))
    if m<=0 or a<0:raise ValueError('Massa positiva e semilargura não negativa')
    input_variance=a*a/3
    plug_in=m*v*v/2
    linear_variance=m*m*v*v*input_variance
    curvature_variance=m*m*a**4/45
    return dict(plug_in=plug_in,mean=plug_in+m*input_variance/2,
                input_variance=input_variance,linear_variance=linear_variance,
                curvature_variance=curvature_variance,
                exact_variance=linear_variance+curvature_variance,
                extra_over_linear=curvature_variance/linear_variance if linear_variance else None)

if __name__=='__main__':
    for v in (2,0):
        print('v0 =',v,'m/s:',energy_moments(2,v,Q(1,5)))
    assert energy_moments(2,0,Q(1,5))['exact_variance']==Q(4,28125)
