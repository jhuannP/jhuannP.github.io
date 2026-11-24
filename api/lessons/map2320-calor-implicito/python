"""Calor 1D sintético: Euler implícito/FTCS, Dirichlet e referências modais."""
from math import sin, pi, exp, isfinite


def integer(x, lo, hi):
    if isinstance(x,bool) or not isinstance(x,int) or not lo<=x<=hi:
        raise ValueError('Inteiro fora do intervalo permitido.')
    return x


def finite(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x):
        raise ValueError('Escalar real finito, sem booleanos.')
    return float(x)


def step(u,r,method='implicit',left=0,right=0):
    """Avança estados interiores. Bordas são dados do novo tempo no implícito."""
    values=[finite(x) for x in u];r,left,right=map(finite,(r,left,right))
    if not values or r<0 or not isfinite(1+2*r):raise ValueError('Interior não vazio e coeficientes finitos com r não negativo.')
    if method=='explicit':
        old=[left]+values+[right]
        return [finite(v+r*(old[i]-2*v+old[i+2])) for i,v in enumerate(values)]
    if method!='implicit':raise ValueError('Método implicit ou explicit.')
    # A=tridiag(-r,1+2r,-r); Thomas, sem inversão explícita da matriz.
    m=len(values);diag=[1+2*r]*m;rhs=values[:]
    rhs[0]+=r*left;rhs[-1]+=r*right
    for i in range(1,m):
        factor=-r/diag[i-1]
        diag[i]-=factor*(-r);rhs[i]-=factor*rhs[i-1]
    out=[0.]*m;out[-1]=finite(rhs[-1]/diag[-1])
    for i in range(m-2,-1,-1):out[i]=finite((rhs[i]+r*out[i+1])/diag[i])
    return out


def heat(n=8,nt=16,method='implicit',high=True):
    """u_t=u_xx em [0,1], T=.2, bordas zero; modo 1 + .1 modo n-1 opcional."""
    n=integer(n,4,64);nt=integer(nt,1,4096)
    if method not in ('implicit','explicit') or not isinstance(high,bool):raise ValueError('Método ou opção inválida.')
    T=.2;dt=T/nt;r=dt*n*n
    modes=[(1,1.)]+([(n-1,.1)] if high else [])
    profile=lambda rates:[0.]+[sum(a*sin(k*pi*j/n)*exp(-rate*T) for (k,a),rate in zip(modes,rates)) for j in range(1,n)]+[0.]
    continuum=profile([(k*pi)**2 for k,a in modes])
    lambdas=[4*n*n*sin(k*pi/(2*n))**2 for k,a in modes]
    semi=profile(lambdas)
    u=[sum(a*sin(k*pi*j/n) for k,a in modes) for j in range(1,n)]
    for _ in range(nt):u=step(u,r,method)
    numerical=[0.]+u+[0.]
    temporal=max(abs(a-b) for a,b in zip(numerical,semi))
    spatial=max(abs(a-b) for a,b in zip(semi,continuum))
    total=max(abs(a-b) for a,b in zip(numerical,continuum))
    factors=[1/(1+4*r*sin(k*pi/(2*n))**2) if method=='implicit' else 1-4*r*sin(k*pi/(2*n))**2 for k in range(1,n)]
    return dict(numerical=numerical,semi=semi,continuum=continuum,r=r,radius=max(map(abs,factors)),temporal=temporal,spatial=spatial,total=total)


if __name__=='__main__':
    for nt in (20,40,80):
        q=heat(16,nt,high=False)
        print('nt=',nt,'erro temporal=',q['temporal'],'erro espacial=',q['spatial'])
    for method in ('implicit','explicit'):
        q=heat(8,16,method)
        print(method,'r=',q['r'],'raio=',q['radius'],'erro total=',q['total'])
    print('Malha espacial fixa isola erro temporal contra referência semidiscreta.')
