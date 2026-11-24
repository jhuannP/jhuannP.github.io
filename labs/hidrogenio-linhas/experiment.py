"""Recorte didático de Balmer, constantes arredondadas: E0=13,6 eV, hc=1240 eV nm."""
from fractions import Fraction as Q

def model(n=6):
    if type(n) is not int or not 3<=n<=8:
        raise ValueError("n inteiro de 3 a 8, emissão para n=2")
    initial=-Q(68,5*n*n);final=-Q(17,5)
    photon=initial-final
    return dict(n=n,initial=initial,final=final,atom_change=final-initial,
                photon=photon,wavelength=Q(1240)/photon)

if __name__=='__main__':
    for n in range(3,9):print(model(n))
