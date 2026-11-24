"""Linearização: referências racionais e erros assinados."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def square(a,h):
    a,h=rational(a),rational(h)
    exact=(a+h)**2
    linear=a*a+2*a*h
    error=exact-linear
    return dict(exact=exact,linear=linear,error=error,absolute=abs(error),
                relative=None if exact==0 else abs(error/exact))


def reciprocal(a,h):
    a,h=rational(a),rational(h)
    if not a or not a+h:raise ValueError('Centro e ponto final devem estar no domínio x≠0.')
    exact=1/(a+h)
    linear=1/a-h/a**2
    return dict(exact=exact,linear=linear,error=exact-linear)


def nonquadratic(t):
    # f(h)=|h|^(3/2) em a=0. Escolhemos h=t² e t>0.
    t=rational(t)
    if t<=0:raise ValueError('Parâmetro estritamente positivo.')
    h=t*t
    return dict(h=h,remainder=t**3,over_h=t,over_h_squared=1/t)


def curvature_bound(M,h):
    M,h=rational(M),rational(h)
    if M<0:raise ValueError('Cota da curvatura não negativa.')
    return M*h*h/2


if __name__=='__main__':
    for h in (Q(1,10),Q(-1,10),Q(1,20)):
        print('Quadrado em a=2:',h,square(2,h))
        print('Inverso em a=1:',h,reciprocal(1,h))
    print('Erro relativo em valor exato zero:',square(1,-1)['relative'])
    for t in (Q(1,2),Q(1,10),Q(1,100)):
        print('Diferenciável, sem resto O(h²):',nonquadratic(t))
    print('A cota M h²/2 exige hipótese sobre f″ no segmento; não apenas f′(a).')
