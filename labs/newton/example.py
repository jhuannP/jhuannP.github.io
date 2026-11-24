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

def newton(f,df,x0,xtol=1e-10,ftol=1e-10,max_iter=50):
    xtol=_params(xtol,max_iter);ftol=_real(ftol)
    if ftol<=0:raise ValueError('Tolerância de resíduo deve ser positiva')
    x=_real(x0);fx=_eval(f,x)
    if fx==0:return x
    for _ in range(max_iter):
        derivada=_eval(df,x)
        if derivada==0:raise ArithmeticError('Derivada zero: próximo passo indefinido')
        novo=_real(x-fx/derivada);fn=_eval(f,novo)
        if fn==0 or (abs(novo-x)<=xtol*(1+abs(novo)) and abs(fn)<=ftol):return novo
        x,fx=novo,fn
    raise RuntimeError('Orçamento atingido sem cumprir passo e resíduo')

raiz=newton(lambda x:x*x-2,lambda x:2*x,1.5)
assert abs(raiz-sqrt(2))<1e-10
print(raiz)

# Contraexemplo: ciclo apesar das derivadas válidas nos pontos visitados.
try:newton(lambda x:x**3-2*x+2,lambda x:3*x*x-2,0,max_iter=10)
except RuntimeError:print('Ciclo 0↔1: orçamento atingido, sem convergência.')
else:raise AssertionError('O ciclo não deveria cumprir os critérios')
for x in [.5,1.,2.]:assert x-x*x/(2*x)==x/2
