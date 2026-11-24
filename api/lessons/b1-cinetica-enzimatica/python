"""Mecanismo E+S <-> ES -> E+P; S livre imposto por reservatório."""
import math
K_ON=1.0  # μM^-1 s^-1
K_OFF=1.0  # s^-1


def delayed_time(tau):
    # tau-(1-exp(-tau)); série evita cancelamento perto de zero.
    return tau*tau*(.5-tau/6+tau*tau/24-tau**3/120) if tau<1e-3 else tau+math.expm1(-tau)


def model(substrate=2,enzyme=.02,kcat=1,tau=3):
    if not all(math.isfinite(x) for x in [substrate,enzyme,kcat,tau]) or substrate<0 or enzyme<=0 or kcat<=0 or tau<0:
        raise ValueError('S e tempo não negativos; enzima e kcat positivos')
    km=(K_OFF+kcat)/K_ON;kd=K_OFF/K_ON;vmax=kcat*enzyme
    fraction=substrate/(km+substrate)
    steady_complex=enzyme*fraction
    relaxation=K_ON*substrate+K_OFF+kcat
    time=tau/relaxation
    buildup=-math.expm1(-tau)
    complex_now=steady_complex*buildup
    steady_rate=kcat*steady_complex
    product=steady_rate/relaxation*delayed_time(tau)
    return dict(substrate=substrate,enzyme=enzyme,kcat=kcat,tau=tau,km=km,kd=kd,vmax=vmax,
                fraction=fraction,steady_complex=steady_complex,steady_free=enzyme-steady_complex,
                relaxation=relaxation,time=time,complex_now=complex_now,free_now=enzyme-complex_now,
                steady_rate=steady_rate,rate_now=kcat*complex_now,product=product,
                equilibrium_guess=vmax*substrate/(kd+substrate))


if __name__=='__main__':
    r=model()
    print('KM/μM',r['km'],'Vmax/(μM/s)',r['vmax'],'v estacionária',r['steady_rate'])
    print('tempo/s',r['time'],'ES/μM',r['complex_now'],'P/μM',r['product'])
    assert r['fraction']==.5 and r['steady_rate']==.01
