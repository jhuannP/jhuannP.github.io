"""Original exact quadratic worksheet, not an Adam implementation."""
from fractions import Fraction as F


def vector(values):
    if not isinstance(values, (list, tuple)) or not values:
        raise ValueError('nonempty vector')
    if any(type(x) not in (int, F) for x in values):
        raise ValueError('exact int or Fraction required, no bool or float')
    return tuple(F(x) for x in values)


def scalar(x):
    return vector([x])[0]


def mask_for(mask, n):
    if not isinstance(mask, (list, tuple)) or len(mask) != n or any(type(x) is not bool for x in mask):
        raise ValueError('one boolean mask per coordinate')
    return tuple(mask)


def penalty(w, lam, mask):
    w = vector(w); lam = scalar(lam); mask = mask_for(mask, len(w))
    if lam < 0: raise ValueError('lambda >= 0')
    return lam * sum(x*x for x,m in zip(w,mask) if m) / 2


def quadratic(w, targets, curvature, lam, mask):
    w, targets, curvature = map(vector, (w,targets,curvature))
    if len(targets) != len(w) or len(curvature) != len(w) or min(curvature) <= 0:
        raise ValueError('matching positive curvature')
    return sum(a*(x-y)**2 for x,y,a in zip(w,targets,curvature)) / 2 + penalty(w,lam,mask)


def step(w, gradient, eta, lam, mask, preconditioner=None, decoupled=False):
    w, g = vector(w), vector(gradient)
    if len(w) != len(g) or type(decoupled) is not bool: raise ValueError('matching vectors and boolean mode')
    mask=mask_for(mask,len(w)); eta,lam=scalar(eta),scalar(lam)
    if eta<0 or lam<0: raise ValueError('nonnegative eta/lambda')
    p=vector(preconditioner) if preconditioner is not None else (F(1),)*len(w)
    if len(p)!=len(w) or min(p)<=0: raise ValueError('positive matching diagonal')
    if decoupled:
        return tuple(x-eta*a*v-eta*lam*x*m for x,v,a,m in zip(w,g,p,mask))
    return tuple(x-eta*a*(v+lam*x*m) for x,v,a,m in zip(w,g,p,mask))


if __name__ == '__main__':
    args=((2,-1,3),(1,2,-4),F(1,10),F(1,5),(True,True,False))
    print('Coupled fixed diagonal:',step(*args,preconditioner=(1,F(1,4),2)))
    print('Decoupled fixed diagonal:',step(*args,preconditioner=(1,F(1,4),2),decoupled=True))
    print('No training benchmark, no Adam state, no measured generalization.')
