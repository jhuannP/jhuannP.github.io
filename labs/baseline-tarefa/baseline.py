"""Referências constantes racionais; dados sintéticos,sem biblioteca de ML."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction.')
    return Q(x)


def targets(values):
    ys=tuple(map(rational,values))
    if not 1<=len(ys)<=1000:raise ValueError('1..1000 alvos.')
    return ys


def fit_constant(train,kind='mean'):
    ys=targets(train)
    if kind=='mean':return sum(ys)/len(ys)
    if kind=='median':return sorted(ys)[(len(ys)-1)//2]
    raise ValueError('kind mean ou median;em npar,mediana inferior.')


def score_constant(c,observed):
    c=rational(c);ys=targets(observed)
    return dict(mse=sum((c-y)**2 for y in ys)/len(ys),
                mae=sum(abs(c-y) for y in ys)/len(ys))


if __name__=='__main__':
    train=(2,2,8);test=(5,7)
    for kind in ('mean','median'):
        c=fit_constant(train,kind)
        print(kind,'constante=',c,'treino=',score_constant(c,train),'teste=',score_constant(c,test))
    leaked=fit_constant(test)
    print('DemonstraçãoINVÁLIDA como avaliação fora do treino:')
    print('ajuste nos próprios alvos de teste:',leaked,score_constant(leaked,test))
    print('A API não detecta procedência de dados sozinha;protocolo precisa ser documentado.')
