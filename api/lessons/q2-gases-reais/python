"""Van der Waals reduzido: x=b/Vm, theta=RTb/a. Não ajusta substância real."""
import math


def eos(theta,x):
    if not math.isfinite(theta) or theta<=0 or not math.isfinite(x) or not 0<=x<1:
        raise ValueError('theta>0, 0<=x<1')
    pressure=theta*x/(1-x)-x*x
    ideal=theta*x
    repulsive=theta*x/(1-x)
    z=1/(1-x)-x/theta
    slope=theta/(1-x)**2-2*x
    second=2*theta/(1-x)**3-2
    pkappa=pressure/(x*slope) if x and slope>0 else 1 if x==0 else None
    return dict(theta=theta,x=x,pressure=pressure,ideal=ideal,repulsive=repulsive,
                z=z,slope=slope,second=second,pkappa=pkappa,
                volume_ratio=1/x if x else None,virial=1+(1-1/theta)*x,
                volume_correction=x/(1-x),attraction=-x/theta,
                b2_ratio=1-1/theta,temperature_ratio=27*theta/8)


def model(theta=.6,x=.2,view=0):
    if not math.isfinite(theta) or not .4<=theta<=2 or not math.isfinite(x) or not 0<=x<=.6 or view not in (0,1):
        raise ValueError('theta .4..2, x 0...6, vista 0/1')
    return dict(eos(theta,x),view=view)


if __name__=='__main__':
    s=model(.6,.4)
    assert abs(s['z']-1)<1e-14
    assert abs(s['pkappa']-9/13)<1e-14
    print(s)
