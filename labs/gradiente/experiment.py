"""Duas funções analíticas selecionadas; classificação não é teste geral de diferenciabilidade."""
import math


def value(kind,x,y):
    if kind==0:return x*x+2*y*y
    if kind!=1:raise ValueError('Função 0/1')
    r2=x*x+y*y
    return x*x*x/r2 if r2 else 0


def partials(kind,x,y):
    if kind==0:return (2*x,4*y)
    if kind!=1:raise ValueError('Função 0/1')
    if x==0:return (0,0) if y else (1,0)
    r2=x*x+y*y
    return (x*x*(x*x+3*y*y)/(r2*r2),-2*x*x*x*y/(r2*r2)) if r2 else (1,0)


def gradiente(x,y):
    return partials(0,x,y)


def direction(angle):
    special={0:(1.,0.),90:(0.,1.),180:(-1.,0.),270:(0.,-1.),360:(1.,0.)}
    return special.get(angle,(math.cos(math.radians(angle)),math.sin(math.radians(angle))))


def model(kind=0,x=1.,y=2.,angle=45.,refinements=2):
    if kind not in (0,1) or not all(math.isfinite(v) for v in (x,y,angle)) or abs(x)>2 or abs(y)>2 or not 0<=angle<=360 or not isinstance(refinements,int) or not 0<=refinements<=6:
        raise ValueError('Função 0/1, x/y ±2, ângulo 0..360 e refinamentos 0..6')
    h=2.**(-refinements);u=direction(angle);g=partials(kind,x,y);norm=math.hypot(*g)
    differentiable=not (kind==1 and x==0 and y==0)
    dot=sum(a*b for a,b in zip(g,u))
    derivative=dot if differentiable else u[0]**3
    end=(x+h*u[0],y+h*u[1]);base=value(kind,x,y);final=value(kind,*end)
    secant=(final-base)/h
    remainder=final-base-h*dot
    normal_available=differentiable and norm>0
    return dict(kind=kind,x=x,y=y,angle=angle,refinements=refinements,h=h,u=u,g=g,norm=norm,
                base=base,end=end,final=final,dot=dot,derivative=derivative,secant=secant,
                remainder=remainder,scaled_remainder=abs(remainder)/h,
                differentiable=differentiable,normal_available=normal_available,
                max_growth=norm if differentiable else None)


if __name__=='__main__':
    for kind in (0,1):
        for n in (0,3,6):
            s=model(kind,0,0,45,n)
            print(kind,n,s['derivative'],s['dot'],s['scaled_remainder'])
    assert gradiente(1,2)==(2,8)
