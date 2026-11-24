"""Equilíbrio planar ideal de bloco; entradas SI racionais, não teste estrutural."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction.')
    return Q(x)


def static_state(weight,width,height,mu,force):
    W,B,H,mu,P=map(rational,(weight,width,height,mu,force))
    if W<=0 or B<=0 or min(H,mu,P)<0:
        raise ValueError('Peso/largura positivos; altura,mu,força não negativos.')
    x=P*H/W
    left=W/2-P*H/B; right=W/2+P*H/B
    friction_margin=mu*W-P; edge_margin=B/2-x
    slide=mu*W
    tip=W*B/(2*H) if H else None
    if tip is None or slide<tip:
        first='deslizamento'; threshold=slide
    elif tip<slide:
        first='tombamento'; threshold=tip
    else:
        first='simultâneos'; threshold=slide
    return dict(normal=W,friction=-P,x=x,left=left,right=right,
                friction_margin=friction_margin,edge_margin=edge_margin,
                admissible=friction_margin>=0 and edge_margin>=0,
                slide_threshold=slide,tip_threshold=tip,
                first=first,threshold=threshold)


if __name__=='__main__':
    for mu in (Q(2,5),Q(1,5),Q(1,3)):
        r=static_state(300,Q(4,5),Q(6,5),mu,90)
        print('mu=',mu,'limiares(N)=',r['slide_threshold'],r['tip_threshold'])
        print('primeiro:',r['first'],'x(m)=',r['x'],'admissível:',r['admissible'])
    print('Contato limite não prevê movimento subsequente, vibração ou ruptura.')
