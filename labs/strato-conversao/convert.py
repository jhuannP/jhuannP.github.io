"""Conversão escalar e expoentes do modelo linear; sem simular Browniano."""
from fractions import Fraction as Q
from importlib import import_module
# Apoio existente: não duplicar suas identidades finitas ou momentos gaussianos.
base=import_module('labs.ito-variacao.ito')

def conversion(a_s,b,derivative_b):
    """Valores pontuais: a_I=a_S+b*b'/2; entradas racionais."""
    a_s,b,derivative_b=map(base.q,(a_s,b,derivative_b))
    return a_s+b*derivative_b/2

def linear_exponent(alpha,sigma,time,w,convention):
    """Log(X_T/X0) para X0>0; alpha é coeficiente de X na deriva.
    Retorna expoente exato, não X nem exponencial racional.
    """
    alpha,sigma,time,w=map(base.q,(alpha,sigma,time,w))
    if time<0:raise ValueError('tempo não negativo')
    if convention=='ito':return (alpha-sigma*sigma/2)*time+sigma*w
    if convention=='stratonovich':return alpha*time+sigma*w
    raise ValueError('convenção ito ou stratonovich')

def compare(increments):
    result=base.square_sums(increments)
    return {'final':result['final'],'left':result['left'],
            'symmetric':result['midpoint'],'qv':result['qv']}

if __name__=='__main__':
    for dx in ((Q(1,2),Q(-1,2),Q(1,2),Q(1,2)),(Q(1,4),)*4):print(compare(dx))
    print('coeficiente Itô,alphaS0,sigma2=',conversion(0,2,2))
    print('expoente convertido=',linear_exponent(2,2,2,0,'ito'))
