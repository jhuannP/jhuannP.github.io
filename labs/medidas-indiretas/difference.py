"""Diferença orientada e variância; entradas racionais na mesma unidade."""
from fractions import Fraction as Q

def rational(value):
    if type(value) not in (int,Q):
        raise ValueError('Use int/Fraction, sem bool/float/texto')
    return Q(value)

def difference(x1,x2,variance1,variance2,covariance12):
    x1,x2,v1,v2,cov=map(rational,(x1,x2,variance1,variance2,covariance12))
    if v1<0 or v2<0 or cov*cov>v1*v2:
        raise ValueError('Matriz de covariância 2x2 deve ser semidefinida positiva')
    return dict(value=x2-x1,variance=v1+v2-2*cov)

if __name__=='__main__':
    shared=difference(20,70,Q(1,25),Q(1,25),Q(3,100))
    independent=difference(20,70,Q(1,25),Q(1,25),0)
    assert shared==dict(value=Q(50),variance=Q(1,50))
    assert independent['variance']==Q(2,25)
    print('Com componente comum:',shared)
    print('Covariância nula:',independent)
