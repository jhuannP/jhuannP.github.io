"""Paralaxe sintética: unidades, inversão e imagem de uma faixa, sem inferência de catálogo."""
from math import pi, tan, isfinite

def summary(p_mas, sigma_mas):
    if not all(isfinite(x) for x in (p_mas,sigma_mas)) or p_mas<=0 or sigma_mas<0:
        raise ValueError('Esta inversão didática exige p positivo e sigma não negativo, ambos finitos.')
    distance=1000/p_mas
    return dict(distance=distance, relative=sigma_mas/p_mas,
                linear=1000*sigma_mas/p_mas**2,
                lower=1000/(p_mas+sigma_mas),
                upper=1000/(p_mas-sigma_mas) if p_mas>sigma_mas else None)

def geometric_distance_au(p_arcsec):
    """Triângulo ideal com cateto transversal de 1 au; p é um ângulo geométrico."""
    if not isfinite(p_arcsec) or not 0<p_arcsec<324000:
        raise ValueError('Ângulo geométrico deve estar entre 0 e 90 graus.')
    return 1/tan(p_arcsec*pi/648000)

if __name__=='__main__':
    print('p=10 mas, faixa p±2 mas:',summary(10,2))
    print('p=10 mas, faixa toca zero:',summary(10,10))
    print('Teste geométrico: p=45 graus, distância em au:',geometric_distance_au(162000))
