"""Verifica candidatos de exemplos específicos; não calcula log real geral."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float/texto')
    return Q(x)

def matches_integer_log(base,argument,exponent):
    b,x=map(rational,(base,argument))
    if b<=0 or b==1 or x<=0:raise ValueError('Base positiva diferente de 1 e argumento positivo')
    if type(exponent) is not int:raise ValueError('Este verificador exige expoente int')
    return b**exponent==x

def equation_candidate(x):
    """log2(x-1)+log2(x+1)=3, com domínio antes da multiplicação."""
    x=rational(x)
    return x>1 and (x-1)*(x+1)==8

if __name__=='__main__':
    assert matches_integer_log(2,Q(1,4),-2)
    assert matches_integer_log(Q(1,2),4,-2)
    assert equation_candidate(3) and not equation_candidate(-3)
    print('3 satisfaz a equação; -3 é eliminado pelo domínio.')
