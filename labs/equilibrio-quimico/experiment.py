"""A <-> B ideal 1:1; K sintético, sem previsão cinética ou reação real."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def equilibrium(a0,b0,K):
    a0,b0,K=map(rational,(a0,b0,K))
    if min(a0,b0)<0 or a0+b0<=0 or K<=0:
        raise ValueError('Quantidades não negativas, total positivo e K positivo.')
    extent=(K*a0-b0)/(1+K)
    A=a0-extent;B=b0+extent
    direction='direta' if extent>0 else 'inversa' if extent<0 else 'já em equilíbrio'
    return dict(A=A,B=B,extent=extent,K=K,Qinitial=b0/a0 if a0 else None,
                fraction_B=B/(A+B),direction=direction)


if __name__=='__main__':
    for initial in ((3,1),(0,4),(2,2)):
        print('Inicial:',initial,'K=1:',equilibrium(*initial,1))
    print('Com total 1 mol e K=4:',equilibrium(1,0,4))
    print('None em Qinitial indica A ausente: razão de atividades não finita.')
    print('Estado final não fornece tempo de relaxação nem caminho da reação.')
