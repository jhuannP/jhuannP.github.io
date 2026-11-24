"""Corpo rígido de 1 L; fluido 1000 kg/m³; g=10 m/s²; posição imposta."""
from fractions import Fraction as F


def inspect(rho=400,percent=40):
    if type(rho) is not int or not 200<=rho<=1400:
        raise ValueError('Densidade inteira de 200 a 1400 kg/m³')
    if type(percent) is not int or not 0<=percent<=100:
        raise ValueError('Fração submersa inteira em porcentagem')
    volume=F(percent,100000)
    mass=F(rho,1000);weight=mass*10;buoyancy=F(percent,10)
    return dict(volume=volume,mass=mass,weight=weight,buoyancy=buoyancy,
                net=buoyancy-weight,balanced=10*percent==rho,
                equilibrium_fraction=F(rho,1000) if rho<=1000 else None,
                regime='parcial' if rho<1000 else 'neutro' if rho==1000 else 'sem equilíbrio por empuxo')


if __name__=='__main__':
    assert inspect()['weight']==4 and inspect()['buoyancy']==4
    assert inspect(1200,100)['net']==-2
    print(inspect())
