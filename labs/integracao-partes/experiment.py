"""I(b)=integral de 0 a b de x exp(x), b em décimos de [-2,2]."""
from math import exp,expm1


def inspect(tenths=10):
    if isinstance(tenths,bool) or not isinstance(tenths,int) or not -20<=tenths<=20:
        raise ValueError('Limite em décimos inteiros de -20 a 20')
    b=tenths/10
    boundary=b*exp(b)
    remainder=expm1(b)
    integral=(b-1)*exp(b)+1 if tenths else 0.0
    return dict(b=b,boundary=boundary,remainder=remainder,integral=integral)


if __name__=='__main__':
    assert inspect(10)['integral']==1
    assert inspect(0)['integral']==0
    print(inspect(-10))
