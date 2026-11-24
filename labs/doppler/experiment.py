"""Som clássico 1D: fonte à esquerda, observador à direita, meio em repouso."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction.')
    return Q(x)


def doppler(c,frequency,source_v,observer_v):
    c,frequency,source_v,observer_v=map(rational,(c,frequency,source_v,observer_v))
    if c<=0 or frequency<=0 or abs(source_v)>=c or abs(observer_v)>=c:
        raise ValueError('c e frequência positivos; velocidades estritamente subsônicas.')
    wavelength=(c-source_v)/frequency
    received=(c-observer_v)/wavelength
    return dict(wavelength=wavelength,frequency=received,period=1/received)


def arrival(n,distance,c,frequency,source_v,observer_v):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=100:
        raise ValueError('Índice inteiro entre 0 e 100 neste experimento.')
    distance,c,frequency,source_v,observer_v=map(rational,(distance,c,frequency,source_v,observer_v))
    doppler(c,frequency,source_v,observer_v)
    emission=Q(n)/frequency
    if distance<=0 or distance+(observer_v-source_v)*emission<=0:
        raise ValueError('Observador deve permanecer à direita da fonte na emissão.')
    received=(distance+(c-source_v)*emission)/(c-observer_v)
    return dict(emission=emission,arrival=received,source_x=source_v*emission,
                observer_x=distance+observer_v*received)


if __name__=='__main__':
    print('c=340 m/s, f=100 Hz, fonte +34 m/s, observador −34 m/s:')
    print(doppler(340,100,34,-34))
    events=[arrival(n,340,340,100,34,-34) for n in range(6)]
    for event in events:print(event)
    print('Intervalos de recepção:',[b['arrival']-a['arrival'] for a,b in zip(events,events[1:])])
    print('Os sinais são referidos ao meio; fórmula válida antes do cruzamento.')
