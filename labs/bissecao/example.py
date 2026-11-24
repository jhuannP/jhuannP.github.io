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

def bissecao(f,a,b,tol=1e-8,max_iter=100):
    tol=_params(tol,max_iter);a,b=_real(a),_real(b)
    if not a<b: raise ValueError('Intervalo deve ter a<b')
    fa,fb=_eval(f,a),_eval(f,b)
    if fa==0:return a
    if fb==0:return b
    if (fa>0)==(fb>0):raise ValueError('Intervalo deve mudar o sinal')
    for _ in range(max_iter):
        meio=a/2+b/2;fm=_eval(f,meio)
        if fm==0 or b/2-a/2<=tol:return meio
        if meio==a or meio==b:raise ArithmeticError('Limite de resolução de ponto flutuante')
        if (fa>0)!=(fm>0):b=meio
        else:a,fa=meio,fm
    raise RuntimeError('Orçamento atingido sem cumprir o critério de parada')

from math import sqrt
raiz=bissecao(lambda x:x*x-2,1,2)
assert abs(raiz-sqrt(2))<=1e-8
print(raiz)

# Contraexemplo controlado: não há garantia sem continuidade.
def salto(x):return -1 if x<0 else 1
candidato=bissecao(salto,-1,1,tol=1e-6)
assert abs(salto(candidato))==1
print('Sem continuidade, candidato não é raiz:',candidato)
