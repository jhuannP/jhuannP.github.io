"""Modelo de ocupação leve: Z=1..18, 0..18 elétrons; sem energias/estabilidade.
Diagramas representantes de Pauli/Hund; não função de onda multieletrônica exata.
"""
ORDER=(('1s',1),('2s',1),('2p',3),('3s',1),('3p',3))

def integer(v):
    if type(v) is not int:raise TypeError("Inteiro sem bool necessário.")
    return v

def boxes(count,orbitals):
    count,orbitals=integer(count),integer(orbitals)
    if orbitals not in (1,3) or not 0<=count<=2*orbitals:
        raise ValueError("Subnível s/p com ocupação dentro da capacidade.")
    return tuple((int(i<min(count,orbitals)),int(i<max(0,count-orbitals))) for i in range(orbitals))

def configuration(z,charge=0):
    z,charge=integer(z),integer(charge)
    n=z-charge
    if not 1<=z<=18 or not 0<=n<=18:
        raise ValueError("Z=1..18, contagem eletrônica 0..18.")
    remaining=n;result=[]
    for label,orbitals in ORDER:
        occupied=min(remaining,2*orbitals)
        if occupied:result.append((label,boxes(occupied,orbitals)))
        remaining-=occupied
    return tuple(result)

def counts(config):
    return tuple((label,sum(up+down for up,down in occupied)) for label,occupied in config)

def unpaired(config):
    return sum(up+down==1 for _,occupied in config for up,down in occupied)

if __name__=='__main__':
    oxygen=configuration(8)
    print(counts(oxygen),'desemparelhados:',unpaired(oxygen))
    print('Na+ e F−:',counts(configuration(11,1)),counts(configuration(9,-1)))
