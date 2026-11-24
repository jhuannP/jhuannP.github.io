"""Classificação algébrica de um modelo por partes; não inferida de amostras."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction')
    return Q(x)


def piece(x,left=-1,right=1,value=0):
    x,left,right,value=map(rational,(x,left,right,value))
    return left+x if x<0 else right-x if x>0 else value


def classify(left=-1,right=1,value=0):
    left,right,value=map(rational,(left,right,value))
    bilateral=left if left==right else None
    category='salto' if bilateral is None else 'continua' if value==bilateral else 'removivel'
    return dict(left_limit=left,right_limit=right,value=value,bilateral=bilateral,category=category)


def hole_extension(x,value=4):
    x,value=map(rational,(x,value))
    return value if x==2 else x+2


if __name__=='__main__':
    for left,right,value in [(-1,1,0),(1,1,9),(1,1,1)]:
        print('Junção:',classify(left,right,value))
        for h in (Q(1,10),Q(1,100),Q(1,1000)):
            assert piece(-h,left,right,value)==left-h
            assert piece(h,left,right,value)==right-h
            print('h=',h,'ramos=',piece(-h,left,right,value),piece(h,left,right,value))
    # Junção contínua com canto: quocientes de diferença laterais distintos.
    for h in (Q(1,10),Q(1,100)):
        assert (piece(-h,0,0,0)-piece(0,0,0,0))/(-h)==1
        assert (piece(h,0,0,0)-piece(0,0,0,0))/h==-1
    assert hole_extension(2)==4 and hole_extension(2,9)==9
