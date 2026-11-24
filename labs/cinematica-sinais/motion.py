"""Cinemática 1D com aceleração constante; números racionais, unidades do chamador."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int, Q):
        raise ValueError('Use inteiro ou Fraction; bool e float excluídos')
    return Q(x)


def state(t, x0=0, v0=2, a=1):
    t, x0, v0, a = map(rational,(t,x0,v0,a))
    if t<0:raise ValueError('Tempo desde t=0 não negativo')
    return dict(x=x0+v0*t+a*t*t/2, v=v0+a*t, a=a)


def interval(t0, t1, x0=0, v0=2, a=1):
    """Distância divide o intervalo apenas se v muda de sinal no interior.

    Não há barreiras, colisões, parada controlada ou arrasto neste modelo.
    """
    t0,t1,x0,v0,a=map(rational,(t0,t1,x0,v0,a))
    if not 0<=t0<t1:raise ValueError('Exija 0 <= t0 < t1')
    start,end=state(t0,x0,v0,a),state(t1,x0,v0,a)
    times=[t0,t1]
    if a:
        turn=-v0/a
        if t0<turn<t1:times.insert(1,turn)
    distance=sum((abs(state(right,x0,v0,a)['x']-state(left,x0,v0,a)['x'])
                  for left,right in zip(times,times[1:])),Q(0))
    displacement=end['x']-start['x']
    return dict(displacement=displacement, distance=distance,
                mean_velocity=displacement/(t1-t0), mean_speed=distance/(t1-t0))


if __name__=='__main__':
    print(state(3))
    result=interval(0,6,v0=6,a=-2)
    assert result==dict(displacement=Q(0),distance=Q(18),mean_velocity=Q(0),mean_speed=Q(3))
    print(result)
