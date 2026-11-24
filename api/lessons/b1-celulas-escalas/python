"""Comparação geométrica de esferas; não é modelo de divisão celular."""
from fractions import Fraction as Q


def geometry(radius,k=1):
    if isinstance(radius,bool) or not isinstance(radius,(int,Q)) or radius<=0:
        raise ValueError('Raio positivo em inteiro ou Fraction, em micrômetros.')
    if isinstance(k,bool) or not isinstance(k,int) or not 1<=k<=10:
        raise ValueError('Fator inteiro entre 1 e 10 neste laboratório.')
    radius=Q(radius);small=radius/k;count=k**3
    area_pi=4*radius**2;volume_pi=Q(4,3)*radius**3
    return dict(radius=radius,k=k,count=count,small_radius=small,
                single_area_pi=area_pi,volume_pi=volume_pi,
                total_area_pi=count*4*small**2,
                total_volume_pi=count*Q(4,3)*small**3,
                single_ratio=3/radius,total_ratio=3*k/radius)


if __name__=='__main__':
    for k in (1,2,3):print(geometry(4,k))
    print('area_pi e volume_pi são coeficientes: multiplique por pi.')
    print('Raio em micrômetros; áreas em micrômetros quadrados; volumes cúbicos.')
    print('O volume total é igual; área cresce com k. Não há previsão biológica universal.')
