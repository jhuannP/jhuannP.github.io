"""Seis polinômios na origem; cortes não substituem a prova do extremo."""
from fractions import Fraction as Q

COEFFICIENTS=((1,-1,0),(1,1,0),(-1,-1,0),(1,0,1),(1,0,-1),(1,0,0))
TRUTH=('saddle','strict-min','strict-max','strict-min','saddle','nonstrict-min')

def value(mode,x,y):
    if isinstance(mode,bool) or not isinstance(mode,int) or not 0<=mode<=5:
        raise ValueError('Modo inteiro0..5')
    a,b,c=COEFFICIENTS[mode]
    return a*x*x+b*y*y+c*y**4

def inspect(mode=3,direction=2,radius_step=10):
    if any(isinstance(x,bool) or not isinstance(x,int) for x in (mode,direction,radius_step)) or not 0<=mode<=5 or not 0<=direction<=2 or not 1<=radius_step<=10:
        raise ValueError('Modo0..5,direção0..2,raio em décimos1..10')
    a,b,c=COEFFICIENTS[mode]
    u2,v2=((Q(1),Q(0)),(Q(1,2),Q(1,2)),(Q(0),Q(1)))[direction]
    coefficient=a*u2+b*v2
    radius=Q(radius_step,10)
    times=[-radius,-radius/2,Q(0),radius/2,radius]
    values=[coefficient*t*t+c*v2*v2*t**4 for t in times]
    quadratic=[coefficient*t*t for t in times]
    determinant=4*a*b
    test='saddle' if determinant<0 else ('min' if a>0 else 'max') if determinant>0 else 'inconclusive'
    return dict(hessian=[[2*a,0],[0,2*b]],determinant=determinant,test=test,truth=TRUTH[mode],radius=radius,times=times,values=values,quadratic=quadratic)

if __name__=='__main__':
    assert inspect(3)['hessian']==inspect(4)['hessian']==inspect(5)['hessian']
    assert inspect(3)['values'][-1]==1 and inspect(4)['values'][-1]==-1
    print(inspect())
