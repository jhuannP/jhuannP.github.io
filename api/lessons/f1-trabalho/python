"""Bloco já deslizando em +x, v0=2 m/s; massa constante e g=10 m/s²."""
from math import isfinite,sqrt

def number(x,low,high):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not low<=x<=high:
        raise ValueError(f'Número finito entre {low} e {high}')
    return float(x)

def ledger(mass,force,mu,distance):
    mass=number(mass,1e-6,1000);force=number(force,0,1000)
    mu=number(mu,0,5);distance=number(distance,0,1000)
    initial=2*mass # m v0²/2, com v0=2.
    friction=mu*mass*10;net=force-friction
    stop=initial/(-net) if net<0 else None
    travelled=min(distance,stop) if stop is not None else distance
    stopped=stop is not None and distance>=stop
    app=force*travelled;fric=-friction*travelled
    final=0. if stopped else initial+app+fric
    return dict(initial_energy=initial,final_energy=final,work_applied=app,work_friction=fric,
                work_net=app+fric,speed=sqrt(2*final/mass),requested=distance,
                travelled=travelled,reached=stop is None or distance<=stop,
                stopped=stopped,stop_distance=stop)

if __name__=='__main__':
    for config in [(2,10,.1,3),(2,0,.1,5),(2,0,0,3)]:print(config,ledger(*config))
