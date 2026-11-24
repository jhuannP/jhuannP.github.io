"""Uma banda, magnitudes calibradas e tela sintética de extinção; sem dados de catálogo."""
from math import log10,isfinite

def photometry(m,absolute,extinction=0):
    if not all(isfinite(x) for x in (m,absolute,extinction)) or extinction<0:
        raise ValueError('Magnitudes finitas e extinção não negativa são necessárias.')
    modulus=m-absolute-extinction
    distance=10**((modulus+5)/5)
    naive=10**((m-absolute+5)/5)
    return dict(modulus=modulus,distance=distance,naive=naive,
                bias=10**(extinction/5),transmission=10**(-.4*extinction))

def apparent(absolute,distance_pc,extinction=0):
    if not all(isfinite(x) for x in (absolute,distance_pc,extinction)) or distance_pc<=0 or extinction<0:
        raise ValueError('Distância positiva e dados finitos; extinção não negativa.')
    return absolute+5*log10(distance_pc/10)+extinction

if __name__=='__main__':
    print(photometry(15,4,1))
    print('Conferência: magnitude observada =',apparent(4,1000,1))
