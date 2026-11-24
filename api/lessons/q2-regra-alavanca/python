"""Linha de coexistência hipotética binária: x_Bα=1/5, x_Bβ=4/5; base molar."""
from fractions import Fraction as F


def inspect(z=50,total=1):
    if type(z) is not int or not 0<=z<=100:
        raise ValueError('Composição global inteira em porcentagem de 0 a 100')
    if type(total) is not int or not 1<=total<=5:
        raise ValueError('Quantidade total inteira de 1 a 5 mol')
    x=F(z,100);inside=F(1,5)<=x<=F(4,5)
    fa=(F(4,5)-x)/F(3,5) if inside else None
    fb=(x-F(1,5))/F(3,5) if inside else None
    na=total*fa if inside else None;nb=total*fb if inside else None
    return dict(z=x,total=total,inside=inside,two_present=20<z<80,
                fa=fa,fb=fb,n_alpha=na,n_beta=nb,
                b_alpha=na/5 if inside else None,b_beta=nb*F(4,5) if inside else None,
                b_total=total*x)


if __name__=='__main__':
    s=inspect(50,5)
    assert s['fa']==F(1,2) and s['b_alpha']+s['b_beta']==s['b_total']
    assert inspect(10)['fa'] is None
    print(s)
