"""Família triangular A=[[a,b],[0,a]]; solução fechada, sem algoritmo geral expm."""
import math


def bounded(x,low,high):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or not low<=x<=high:
        raise ValueError('Parâmetro fora da faixa finita deste laboratório.')
    return float(x)


def evolution(a,b,t):
    a=bounded(a,-2,2);b=bounded(b,-4,4);t=bounded(t,-4,4)
    scale=math.exp(a*t)
    return ((scale,scale*b*t),(0.0,scale))


def state(a,b,t,x0=0,y0=1):
    x0=bounded(x0,-4,4);y0=bounded(y0,-4,4)
    E=evolution(a,b,t)
    x=E[0][0]*x0+E[0][1]*y0;y=E[1][1]*y0
    return dict(x=x,y=y,dx=a*x+b*y,dy=a*y,
                eigenspace_dimension=2 if b==0 else 1)


if __name__=='__main__':
    for a in (-1,0,1):
        for t in (0,1,2,4):print('a=',a,'b=2, t=',t,state(a,2,t))
    print('a=0, b=2, (x0,y0)=(1,3), t=2:',state(0,2,2,1,3))
    print('A solução é exata para esta família; números usam ponto flutuante.')
