from math import isfinite, sqrt, pi, cos, sin, exp, e, fsum

def _real(value):
    try:
        if isinstance(value,bool): raise ValueError
        result=float(value)
    except (TypeError,ValueError,OverflowError):
        raise ValueError('Valor real finito necessário') from None
    if not isfinite(result): raise ValueError('Valor real finito necessário')
    return result

def _params(tol,max_iter):
    tol=_real(tol)
    if tol<=0 or isinstance(max_iter,bool) or not isinstance(max_iter,int) or max_iter<=0:
        raise ValueError('Tolerância positiva e orçamento inteiro positivo necessários')
    return tol

def _eval(f,x):
    return _real(f(x))

def ponto_fixo(g,x0,tol=1e-10,max_iter=100):
    tol=_params(tol,max_iter);x=_real(x0)
    for _ in range(max_iter):
        novo=_eval(g,x)
        if abs(novo-x)<=tol*(1+abs(novo)):return novo
        x=novo
    raise RuntimeError('Orçamento atingido sem cumprir o critério de passo')

x=ponto_fixo(lambda x:x/2+1,0)
assert abs(x-2)<1e-9
print(x)

# Critério de passo pode aceitar uma aproximação distante.
s=1-1e-12
candidato=ponto_fixo(lambda x:s*x+2*(1-s),0)
assert abs(candidato-2)>1.9
print('Passo pequeno, mas erro de posição grande:',candidato)
