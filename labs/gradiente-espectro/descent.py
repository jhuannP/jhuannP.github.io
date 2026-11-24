"""Exact rational diagnostics for Phi=(x*x+4*y*y)/2, not a general optimizer."""
from fractions import Fraction as Q


def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError('Use int/Fraction without bool/float')
    return Q(x)


def point(v):
    if not isinstance(v,(list,tuple)) or len(v)!=2:raise ValueError('Two coordinates required')
    return tuple(map(number,v))


def inspect(v):
    x,y=point(v)
    return dict(point=(x,y),objective=(x*x+4*y*y)/2,gradient=(x,4*y),gradient_norm_squared=x*x+16*y*y)


def history(eta,steps,initial=(1,1)):
    eta=number(eta);x,y=point(initial)
    if not 0<=eta<=2:raise ValueError('Didactic step range 0..2')
    if type(steps) is not int or not 0<=steps<=200:raise ValueError('Integer steps 0..200')
    rows=[inspect((x,y))]
    for _ in range(steps):
        x,y=x-eta*x,y-eta*4*y
        rows.append(inspect((x,y)))
    return tuple(rows)


def contraction(eta):
    eta=number(eta)
    return max(abs(1-eta),abs(1-4*eta))


def exact_line_step(v):
    x,y=point(v)
    denominator=x*x+64*y*y
    return (x*x+16*y*y)/denominator if denominator else None


if __name__=='__main__':
    for eta in (Q(1,4),Q(2,5),Q(1,2)):
        print('eta',eta,'q',contraction(eta),'first',history(eta,1)[-1])
    a,b=history(Q(1,2),11)[10:]
    print('boundary cost change',a['objective']-b['objective'],'gradient²',a['gradient_norm_squared'])
    eta=exact_line_step((1,1));print('exact one-step line search',eta,history(eta,1)[-1])
