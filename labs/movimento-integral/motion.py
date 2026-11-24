"""Dois modelos 1D fixos: t em segundos; v em m/s; posição em m.

Coeficientes são os valores numéricos nas unidades SI declaradas na aula.
Não é um localizador geral de raízes nem um integrador de dados medidos.
"""
from fractions import Fraction as Q


def rational(t):
    if type(t) not in (int,Q):
        raise ValueError('use int ou Fraction, sem bool/float')
    return Q(t)


def velocity(t, model='linear'):
    t=rational(t)
    if model=='linear':return 2*t-2
    if model=='cubic':return (t-1)**2*(t-3)
    raise ValueError('modelo linear ou cubic')


def primitive(t, model='linear'):
    t=rational(t)
    if model=='linear':return t*t-2*t
    if model=='cubic':return t**4/4-Q(5,3)*t**3+Q(7,2)*t*t-3*t
    raise ValueError('modelo linear ou cubic')


def travel(start,end,model='linear'):
    """Intervalo físico 0<=start<=end. Médias None se duração zero.

    Raízes conhecidas dos dois modelos são inseridas apenas no interior.
    Somar módulos das variações por trechos de sinal fixo dá a distância.
    """
    start,end=rational(start),rational(end)
    if not 0<=start<=end:raise ValueError('exige 0<=início<=fim')
    if model not in ('linear','cubic'):raise ValueError('modelo linear ou cubic')
    roots=(Q(1),) if model=='linear' else (Q(1),Q(3))
    cuts=(start,)+tuple(t for t in roots if start<t<end)+(end,)
    changes=tuple(primitive(b,model)-primitive(a,model) for a,b in zip(cuts,cuts[1:]))
    displacement=primitive(end,model)-primitive(start,model)
    distance=sum(map(abs,changes),Q(0))
    duration=end-start
    return {'cuts':cuts,'changes':changes,'displacement':displacement,
            'distance':distance,
            'average_velocity':displacement/duration if duration else None,
            'average_speed':distance/duration if duration else None}

if __name__=='__main__':
    assert travel(0,2)['displacement']==0
    assert travel(0,2)['distance']==2
    cubic=travel(0,4,'cubic')
    assert cubic['displacement']==Q(4,3)
    assert cubic['distance']==Q(35,6)
    print('Cúbico: deslocamento',cubic['displacement'],'m; distância',cubic['distance'],'m')
