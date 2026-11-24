"""Frasco fechado: ação das massas e redução escalar de Michaelis–Menten."""
import math
PRESETS=[(2.,.02,40.),(2.,2.,8.),(.2,2.,8.)] # S0, Etotal, horizonte longo


def rhs(y,enzyme,kcat=1.):
    s,c,p=y
    association=(enzyme-c)*s  # k1=1 μM^-1 s^-1
    release=c                # k-1=1 s^-1
    catalysis=kcat*c
    return (-association+release,association-release-catalysis,catalysis)


def solve(s0,enzyme,end,kcat=1.,frames=120,refinement=1):
    if not all(math.isfinite(x) for x in [s0,enzyme,end,kcat]) or min(s0,enzyme,end,kcat)<0:
        raise ValueError('Concentrações, tempo e catálise finitos não negativos')
    if not isinstance(frames,int) or frames<1 or not isinstance(refinement,int) or refinement<1:
        raise ValueError('Quadros/refinamento inteiros positivos')
    interval=end/frames
    substeps=max(1,math.ceil(interval*(s0+enzyme+1+kcat)/.05))*refinement
    h=interval/substeps
    y=(s0,0.,0.);history=[dict(t=0.,s=s0,c=0.,p=0.)]
    for frame in range(1,frames+1):
        for _ in range(substeps):
            a=rhs(y,enzyme,kcat)
            b=rhs(tuple(z+h*d/2 for z,d in zip(y,a)),enzyme,kcat)
            c=rhs(tuple(z+h*d/2 for z,d in zip(y,b)),enzyme,kcat)
            d=rhs(tuple(z+h*w for z,w in zip(y,c)),enzyme,kcat)
            y=tuple(z+h*(aa+2*bb+2*cc+dd)/6 for z,aa,bb,cc,dd in zip(y,a,b,c,d))
        history.append(dict(t=end*frame/frames,s=y[0],c=y[1],p=y[2]))
    # Nenhuma projeção ou truncamento para impor conservação/positividade.
    return dict(history=history,h=h,steps=frames*substeps)


def reduced_product(s0,enzyme,t,kcat=1.):
    if s0==0 or enzyme*kcat*t==0:return 0.
    km=1+kcat;vmax=kcat*enzyme
    # S*+KM ln(S*/S0)=S0-Vmax*t; z=ln(S*/S0).
    lo=-vmax*t/km;hi=0.
    for _ in range(70):
        z=(lo+hi)/2
        if s0*math.exp(z)+km*z>s0-vmax*t:hi=z
        else:lo=z
    return s0*(-math.expm1((lo+hi)/2))


def delay(tau):
    return tau*tau*(.5-tau/6+tau*tau/24-tau**3/120) if tau<1e-3 else tau+math.expm1(-tau)


def experiment(case=0,window=0,fraction=.5,refinement=1):
    if case not in range(3) or window not in (0,1) or not math.isfinite(fraction) or not 0<=fraction<=1:
        raise ValueError('Caso 0–2, janela 0/1 e fração 0–1')
    s0,enzyme,long=PRESETS[case];end=2. if window==0 else long
    result=solve(s0,enzyme,end,refinement=refinement)
    km=2.;vmax=enzyme;v0=vmax*s0/(km+s0);lam=s0+km
    for row in result['history']:
        row['qssa_p']=reduced_product(s0,enzyme,row['t'])
        row['clamp_p']=v0/lam*delay(lam*row['t'])
        row['v']=row['c'];row['mm_at_free_s']=vmax*row['s']/(km+row['s'])
    selected=result['history'][int(math.floor(fraction*120+.5))]
    return dict(case=case,window=window,fraction=fraction,s0=s0,enzyme=enzyme,end=end,
                epsilon=enzyme/(km+s0),fast_time=1/lam,selected=selected,
                max_mass_error=max(abs(r['s']+r['c']+r['p']-s0) for r in result['history']),
                max_model_gap=max(abs(r['p']-r['qssa_p'])/s0 for r in result['history']),**result)


def exact_binding_complex(s0,enzyme,t):
    """Limite kcat=0, k1=k-1=1: solução de Riccati independente do RK4."""
    b=s0+enzyme+1
    delta=math.sqrt(b*b-4*s0*enzyme)
    upper=(b+delta)/2
    lower=2*s0*enzyme/(b+delta)
    decay=math.exp(-delta*t)
    return lower*(-math.expm1(-delta*t))/(1-(lower/upper)*decay)


if __name__=='__main__':
    for case in range(3):
        r=experiment(case)
        print(case,r['selected'],'erro inventário',r['max_mass_error'])
