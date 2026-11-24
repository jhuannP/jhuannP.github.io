"""Rede sintética M,ML,MS; reservatórios de L/S,sem previsão de composto."""
from fractions import Fraction as Q

def val(x,lo=0,hi=12):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or not lo<=x<=hi:
        raise ValueError('Use int/Fraction no intervalo documentado')
    return Q(x)

def stationary(L=2,S=3,total=Q(1,1000)):
    L,S=val(L),val(S);total=val(total,Q(1,10**6),1)
    # kL=1,k-L=1,kS=2,k-S=2,kcat=4,com unidades no README.
    free=total/(1+L+S/3);ml=L*free;ms=S*free/3
    return (free,ml,ms)

def drift(state,L=2,S=3):
    if not isinstance(state,(list,tuple)) or len(state)!=3:raise ValueError('Estado(M,ML,MS)')
    f,ml,ms=(val(x,0,1) for x in state);L,S=val(L),val(S)
    if f+ml+ms>1:raise ValueError('Inventário total de até1 mol/L')
    return (-(L+2*S)*f+ml+6*ms,L*f-ml,2*S*f-6*ms)

def flux(state):
    drift(state) # validação de forma/faixa
    return 4*Q(state[2])

def step(state,h,L=2,S=3):
    L,S=val(L),val(S);h=val(h,Q(1,10**6),1)
    if h*max(L+2*S,Q(1),Q(6))>1:
        raise ValueError('Passo não preserva positividade pela cota escolhida')
    derivative=drift(state,L,S)
    return tuple(Q(x)+h*dx for x,dx in zip(state,derivative))

if __name__=='__main__':
    state=stationary();rate=flux(state);total=sum(state)
    assert drift(state)==(0,0,0)
    print('M,ML,MS em mol/L:',state,'v em mol/L/s:',rate,'v/Mtotal em1/s:',rate/total)
    y=(Q(0),total,Q(0))
    for _ in range(80):y=step(y,Q(1,8))
    print('erro máximo após10s:',float(max(abs(a-b) for a,b in zip(y,state))))
