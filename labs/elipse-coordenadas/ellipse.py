"""Equação A*x²+B*x*y+C*y²+D*x+E*y+F=0; coordenadas racionais."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float')
    return Q(x)


def coefficients(values):
    if not isinstance(values,(list,tuple)) or len(values)!=6:raise ValueError('Seis coeficientes A,B,C,D,E,F')
    return tuple(map(rational,values))


def evaluate(values,x,y):
    a,b,c,d,e,f=coefficients(values);x,y=map(rational,(x,y))
    return a*x*x+b*x*y+c*y*y+d*x+e*y+f


def reduce_definite(values):
    values=coefficients(values);a,b,c,d,e,f=values
    delta=4*a*c-b*b
    if delta<=0 or a==0:raise ValueError('Somente parte quadrática definida, sem caso singular/indefinido')
    if a<0:
        values=tuple(-x for x in values);a,b,c,d,e,f=values
    h=(b*e-2*c*d)/delta;k=(b*d-2*a*e)/delta
    rhs=-evaluate(values,h,k)
    kind='elipse' if rhs>0 else 'ponto' if rhs==0 else 'vazio'
    return dict(center=(h,k),rhs=rhs,kind=kind,normalized_coefficients=values)


def rotation(cosine,sine):
    cosine,sine=map(rational,(cosine,sine))
    if cosine*cosine+sine*sine!=1:raise ValueError('c²+s² deve ser exatamente1')
    return cosine,sine


def to_world(center,cosine,sine,u,v):
    if not isinstance(center,(tuple,list)) or len(center)!=2:raise ValueError('Centro com duas coordenadas')
    h,k=map(rational,center);c,s=rotation(cosine,sine);u,v=map(rational,(u,v))
    return h+c*u-s*v,k+s*u+c*v


def to_local(center,cosine,sine,x,y):
    if not isinstance(center,(tuple,list)) or len(center)!=2:raise ValueError('Centro com duas coordenadas')
    h,k=map(rational,center);c,s=rotation(cosine,sine);x,y=map(rational,(x,y))
    return c*(x-h)+s*(y-k),-s*(x-h)+c*(y-k)


if __name__=='__main__':
    values=(36,-24,29,-120,140,20)
    r=reduce_definite(values)
    assert r['center']==(1,-2) and r['rhs']==180
    point=to_world((1,-2),Q(3,5),Q(4,5),3,0)
    assert point==(Q(14,5),Q(2,5)) and evaluate(values,*point)==0
    print(r,point)
