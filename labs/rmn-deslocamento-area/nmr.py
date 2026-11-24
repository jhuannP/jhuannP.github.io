"""Conversões racionais e integração de janelas retangulares artificiais."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float')
    return Q(x)


def chemical_shift(sample_hz,reference_hz):
    sample_hz,reference_hz=map(rational,(sample_hz,reference_hz))
    if min(sample_hz,reference_hz)<=0:raise ValueError('Frequências positivas em Hz')
    return (sample_hz-reference_hz)/reference_hz*10**6


def offset_hz(shift_ppm,reference_mhz):
    shift_ppm,reference_mhz=map(rational,(shift_ppm,reference_mhz))
    if reference_mhz<=0:raise ValueError('Referência positiva em MHz')
    return shift_ppm*reference_mhz


def rectangle(center,width,area):
    center,width,area=map(rational,(center,width,area))
    if width<=0 or area<0:raise ValueError('Largura positiva e área não negativa')
    return center-width/2,center+width/2,area/width


def integrate(components,lower,upper):
    """Componentes (centro, largura, área). Limites crescentes em ppm.

    Área em unidade arbitrária; altura em unidade de área por ppm.
    Não resolve FID, formas de linha, ruído ou aquisição quantitativa.
    """
    lower,upper=map(rational,(lower,upper))
    if upper<lower:raise ValueError('Limites crescentes')
    if not isinstance(components,(list,tuple)):raise ValueError('Lista/tupla de componentes')
    result=Q(0)
    for component in components:
        if not isinstance(component,(list,tuple)) or len(component)!=3:raise ValueError('Componente centro/largura/área')
        left,right,height=rectangle(*component)
        result+=height*max(Q(0),min(right,upper)-max(left,lower))
    return result


def fractions(areas):
    if not isinstance(areas,(list,tuple)) or not areas:raise ValueError('Áreas não vazias')
    areas=tuple(map(rational,areas));total=sum(areas,Q(0))
    if any(x<0 for x in areas) or total<=0:raise ValueError('Áreas não negativas, soma positiva')
    return tuple(x/total for x in areas)


def counts(areas,total_h):
    """Inferência condicional: total conhecido e resposta quantitativa igual assumidos.

    Resultados não inteiros são mantidos, sem arredondar para uma estrutura.
    """
    if type(total_h) is not int or total_h<=0:raise ValueError('Total de H inteiro positivo conhecido')
    return tuple(total_h*x for x in fractions(areas))


if __name__=='__main__':
    artificial=[(3,Q(2,5),3),(1,Q(4,5),2)]
    assert chemical_shift(400000800,400000000)==2
    assert offset_hz(2,600)==1200
    assert integrate(artificial,2,4)==3 and integrate(artificial,0,2)==2
    assert counts((3,2),5)==(3,2)
    print('Áreas:',integrate(artificial,2,4),integrate(artificial,0,2),'frações:',fractions((3,2)))
