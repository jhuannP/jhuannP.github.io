"""Transferência HA+B <=> A-+BH+, única reação ideal; não calcula pH ou cinética."""
import math


def equilibrium(delta=2.,ratio=1.):
    if not all(math.isfinite(v) for v in (delta,ratio)) or not -12<=delta<=12 or ratio<=0 or ratio>10:
        raise ValueError('Delta entre -12 e 12 e razão positiva até 10')
    # u=x/C_A; positive quadratic root without cancellation at K=1.
    K=10**delta
    return 2*ratio/(1+ratio+math.sqrt((1-ratio)**2+4*ratio/K))


def quotient(u,ratio):
    if not math.isfinite(ratio) or ratio<=0 or not math.isfinite(u) or not 0<u<min(1,ratio):
        raise ValueError('Composição estritamente interior')
    return 2*math.log10(u)-math.log10(1-u)-math.log10(ratio-u)


def gibbs(u,ratio,delta):
    """G/(RT*n_A,total), a menos de constantes, para comparar composições nos mesmos totais."""
    def xlogx(x):return 0 if x==0 else x*math.log(x)
    if not 0<=u<=min(1,ratio):raise ValueError('Composição admissível')
    return xlogx(1-u)+xlogx(ratio-u)+2*xlogx(u)-u*delta*math.log(10)


def model(delta=2.,ratio=1.,concentration=.01,fraction=.25):
    if not all(math.isfinite(v) for v in (delta,ratio,concentration,fraction)) or not -6<=delta<=6 or not .25<=ratio<=4 or not .001<=concentration<=.02 or not 0<=fraction<=1:
        raise ValueError('Domínio didático: delta ±6, razão .25..4, C .001...02, f 0..1')
    limit=min(1,ratio);u=limit*fraction;ueq=equilibrium(delta,ratio)
    current=[concentration*(1-u),concentration*(ratio-u),concentration*u,concentration*u]
    final=[concentration*(1-ueq),concentration*(ratio-ueq),concentration*ueq,concentration*ueq]
    logQ=quotient(u,ratio) if 0<fraction<1 else None
    dg_rt=(logQ-delta)*math.log(10) if logQ is not None else None
    direction='direto' if fraction==0 else 'inverso' if fraction==1 else ('equilíbrio' if abs(logQ-delta)<1e-10 else 'direto' if logQ<delta else 'inverso')
    return dict(delta=delta,ratio=ratio,concentration=concentration,fraction=fraction,
                K=10**delta,u=u,ueq=ueq,eq_fraction=ueq/limit,current=current,final=final,
                logQ=logQ,dg_rt=dg_rt,direction=direction)


if __name__=='__main__':
    for delta in (-2,0,2):
        s=model(delta=delta)
        print('delta=',delta,'f_eq=',s['eq_fraction'],'sentido=',s['direction'])
    assert abs(equilibrium(2,1)-10/11)<1e-14
