"""Escalas de uma onda progressiva harmônica ideal, com fase racional exata."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool ou float')
    return Q(x)


def positive(x):
    x=rational(x)
    if x<=0:raise ValueError('Grandeza positiva exigida')
    return x


def parameters(frequency,wavelength):
    frequency,wavelength=map(positive,(frequency,wavelength))
    return dict(frequency=frequency,wavelength=wavelength,period=1/frequency,speed=frequency*wavelength)


def phase_cycles(x,t,frequency=5,wavelength=2):
    """Fase módulo um de sin[2π(x/λ−ft)]; fase não é deslocamento material."""
    x,t=map(rational,(x,t));p=parameters(frequency,wavelength)
    if t<0:raise ValueError('Tempo não negativo')
    return (x/p['wavelength']-p['frequency']*t)%1


def phase_marker(index,t,frequency=5,wavelength=2):
    """Posição da fase1/4+index; corresponde a uma crista quando A>0."""
    if type(index) is not int:raise ValueError('Índice inteiro, sem bool')
    t=rational(t);p=parameters(frequency,wavelength)
    if t<0:raise ValueError('Tempo não negativo')
    return p['wavelength']*(Q(1,4)+index+p['frequency']*t)


def interface(frequency,speed_before,speed_after):
    """Hipótese externa: interface fixa, meios em repouso e resposta linear estacionária.

    Não calcula reflexão, amplitudes, energia transmitida ou efeito Doppler.
    """
    frequency,speed_before,speed_after=map(positive,(frequency,speed_before,speed_after))
    return dict(frequency=frequency,period=1/frequency,
                wavelength_before=speed_before/frequency,wavelength_after=speed_after/frequency)


def pressure_intensity_ratio(initial,final):
    """Amplitudes de pressão; mesmo meio e onda sonora progressiva linear."""
    initial=positive(initial);final=rational(final)
    if final<0:raise ValueError('Amplitude final não negativa')
    return (final/initial)**2


if __name__=='__main__':
    assert parameters(5,2)==dict(frequency=Q(5),wavelength=Q(2),period=Q(1,5),speed=Q(10))
    assert phase_marker(0,Q(1,20))-phase_marker(0,0)==Q(1,2)
    print(parameters(5,2),interface(5,10,20))
