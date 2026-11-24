"""Duas superfícies esféricas ideais, sem energia, transporte ou dinâmica."""
from math import pi
from fractions import Fraction as F

def model(radius=20,thickness=4):
    if isinstance(radius,bool) or not isinstance(radius,int) or radius not in range(10,101,10):
        raise ValueError('Raio inteiro 10–100 em passos de 10 nm')
    if isinstance(thickness,bool) or not isinstance(thickness,int) or thickness not in (2,4,6):
        raise ValueError('Separação 2, 4 ou 6 nm')
    outer=radius+thickness
    ratio=F(outer*outer,radius*radius)
    return dict(radius=radius,thickness=thickness,outer=outer,
                inner_area=4*pi*radius**2,outer_area=4*pi*outer**2,
                lumen_volume=4*pi*radius**3/3,shell_volume=4*pi*(outer**3-radius**3)/3,
                ratio=float(ratio),relative_excess=float(ratio-1),
                outer_fraction=float(F(outer*outer,outer*outer+radius*radius)))

if __name__=='__main__':
    for r in (10,20,100):
        m=model(r,4)
        print('r=',r,'d=4 nm; Aexterna/Ainterna=',m['ratio'])
    assert F(14**2,10**2)==F(49,25)
