"""Diagnósticos racionais de modelos de erro; não certificam convergência."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int ou Fraction, sem bool/float')
    return Q(x)


def positive_integer(x):
    if type(x) is not int or x<1:raise ValueError('Ordem inteira positiva')
    return x


def diagnostics(iterates,target,p=1):
    p=positive_integer(p)
    if not isinstance(iterates,(list,tuple)) or len(iterates)<2:
        raise ValueError('Forneça pelo menos duas iteradas racionais')
    xs=tuple(map(rational,iterates));target=rational(target)
    errors=tuple(abs(x-target) for x in xs)
    ratios=tuple(b/a**p if a else None for a,b in zip(errors,errors[1:]))
    steps=tuple(abs(b-a) for a,b in zip(xs,xs[1:]))
    return dict(errors=errors,ratios=ratios,steps=steps)


def power_errors(e0,factor,p,steps):
    e0,factor=map(rational,(e0,factor));p=positive_integer(p)
    if e0<=0 or factor<=0:raise ValueError('Erro inicial e fator positivos')
    if type(steps) is not int or steps<0:raise ValueError('Número de passos inteiro não negativo')
    values=[e0]
    for _ in range(steps):values.append(factor*values[-1]**p)
    return tuple(values)


def mesh_comparison(h,p=2,coefficient=1,floor=0):
    h,coefficient,floor=map(rational,(h,coefficient,floor));p=positive_integer(p)
    if h<=0 or coefficient<=0 or floor<0:raise ValueError('h,C positivos e piso não negativo')
    coarse=coefficient*h**p+floor
    fine=coefficient*(h/2)**p+floor
    return dict(coarse=coarse,fine=fine,ratio=coarse/fine)


if __name__=='__main__':
    linear=power_errors(Q(1,2),Q(1,2),1,4)
    quadratic=power_errors(Q(1,2),1,2,4)
    assert diagnostics(linear,0,1)['ratios']==(Q(1,2),)*4
    assert diagnostics(quadratic,0,2)['ratios']==(Q(1),)*4
    print('Linear:',linear,'Quadrática:',quadratic)
    print('Malha com piso:',mesh_comparison(Q(1,32),floor=Q(1,1024)))
