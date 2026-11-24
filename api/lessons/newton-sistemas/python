"""Newton completo para F=(x²+y²-1, x-y), adimensional.
Sistema linear 2x2 com pivotamento parcial; sem inversa explícita.
"""
from math import isfinite


def system(x,y):return (x*x+y*y-1,x-y)
def jacobian(x,y):return [[2*x,2*y],[1.,-1.]]
def norm(values):return max(map(abs,values))


def solve2(A,b):
    m=[list(map(float,row))+[float(rhs)] for row,rhs in zip(A,b)]
    threshold=1e-12*max(1.,max(abs(v) for row in A for v in row))
    if abs(m[1][0])>abs(m[0][0]):m[0],m[1]=m[1],m[0]
    if abs(m[0][0])<=threshold:raise ArithmeticError('Pivô pequeno.')
    ratio=m[1][0]/m[0][0]
    for j in (1,2):m[1][j]-=ratio*m[0][j]
    if abs(m[1][1])<=threshold:raise ArithmeticError('Pivô pequeno.')
    y=m[1][2]/m[1][1];x=(m[0][2]-m[0][1]*y)/m[0][0]
    return x,y


def newton(x,y,max_steps=6,ftol=1e-10,steptol=1e-14):
    for value in (x,y,ftol,steptol):
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not isfinite(value):
            raise ValueError('Entradas numéricas finitas.')
    if norm((x,y))>1e6 or min(ftol,steptol)<0:
        raise ValueError('Coordenadas até 1e6 e tolerâncias não negativas.')
    if isinstance(max_steps,bool) or not isinstance(max_steps,int) or not 0<=max_steps<=12:
        raise ValueError('De 0 a 12 passos neste laboratório.')
    def frame(x,y):return dict(x=x,y=y,residual=norm(system(x,y)))
    trace=[frame(x,y)]
    if trace[-1]['residual']<=ftol:return dict(trace=trace,status='residual')
    for _ in range(max_steps):
        try:dx,dy=solve2(jacobian(x,y),[-v for v in system(x,y)])
        except ArithmeticError:return dict(trace=trace,status='pivot')
        u,v=x+dx,y+dy
        if not all(isfinite(z) for z in (u,v)) or norm((u,v))>1e6:
            return dict(trace=trace,status='bound')
        trace.append(frame(u,v));x,y=u,v
        if trace[-1]['residual']<=ftol:return dict(trace=trace,status='residual')
        if norm((dx,dy))<=steptol*(1+norm((x,y))):
            return dict(trace=trace,status='smallStep')
    return dict(trace=trace,status='limit')


if __name__=='__main__':
    for start in ((1,0),(-1,0),(0,0)):
        result=newton(*start)
        print('Inicial:',start,'parada:',result['status'])
        for k,row in enumerate(result['trace']):print(k,row)
