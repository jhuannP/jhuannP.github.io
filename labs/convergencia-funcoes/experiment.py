"""Convergência de funções: cotas e testemunhas racionais."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def index(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=100:
        raise ValueError('n inteiro de 1 a 100 neste experimento.')
    return n


def power_witness(n):
    n=index(n)
    x=1-Q(1,2*n)
    return dict(x=x,value=x**n,limit=Q(0))


def restricted_error(n,b):
    n=index(n);b=rational(b)
    if not 0<=b<1:raise ValueError('0≤b<1 para a restrição uniforme.')
    return b**n


def uniform_linear_index(epsilon):
    epsilon=rational(epsilon)
    if epsilon<=0:raise ValueError('Tolerância positiva.')
    return int(1/epsilon)+1  # 1/N < epsilon, inclusive em tolerâncias recíprocas.


def spike(n,x):
    n=index(n);x=rational(x)
    if n<2:raise ValueError('Triângulo no intervalo [0,1] exige n≥2.')
    return max(Q(0),n*(1-n*abs(x-Q(1,n))))


if __name__=='__main__':
    for n in (1,4,20):
        print('Testemunha móvel para x^n:',n,power_witness(n))
        print('Erro uniforme em [0,1/2]:',restricted_error(n,Q(1,2)))
    print('Para x/n em [0,1], epsilon=1/10: N=',uniform_linear_index(Q(1,10)))
    print('Pico triangular n=4:',[(x,spike(4,x)) for x in (Q(0),Q(1,4),Q(1,2))])
    print('A integral desse triângulo é 1; o limite pontual é zero. Provas no texto.')
