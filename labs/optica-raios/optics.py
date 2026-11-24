"""Óptica geométrica ideal: seno racional e lente fina para objeto real."""
from fractions import Fraction as Q
from math import asin,degrees


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float')
    return Q(x)


def indices(n1,n2):
    n1,n2=map(rational,(n1,n2))
    if n1<=0 or n2<=0:raise ValueError('Índices reais positivos exigidos')
    return n1,n2


def snell(n1,n2,sine_incident):
    n1,n2=indices(n1,n2);sine_incident=rational(sine_incident)
    if not 0<=sine_incident<1:raise ValueError('Incidência entre0° inclusive e90° exclusive')
    required=n1*sine_incident/n2
    regime='total' if required>1 else 'rasante' if required==1 else 'propagante'
    return dict(regime=regime,sine_incident=sine_incident,sine_reflected=sine_incident,
                required_sine=required,sine_transmitted=None if required>1 else required)


def critical_sine(n1,n2):
    n1,n2=indices(n1,n2)
    return n2/n1 if n1>n2 else None


def angle_degrees(sine):
    """Aproximação de exibição. Não é usada para classificar o regime."""
    sine=rational(sine)
    if not 0<=sine<=1:raise ValueError('Seno entre0 e1')
    return degrees(asin(float(sine)))


def thin_lens(f,p):
    """Mesmo meio nos dois lados; p>0 objeto real à esquerda, luz para direita.

    f>0 convergente; q>0 imagem real à direita; q<0 virtual à esquerda.
    Não resolve lente espessa, aberrações ou p<=0 (objeto virtual).
    """
    f,p=map(rational,(f,p))
    if f==0 or p<=0:raise ValueError('Foco não nulo e distância de objeto positiva')
    inverse_q=1/f-1/p
    if not inverse_q:return dict(kind='sem_imagem_finita',q=None,magnification=None)
    q=1/inverse_q
    return dict(kind='real' if q>0 else 'virtual',q=q,magnification=-q/p)


if __name__=='__main__':
    r=snell(1,Q(3,2),Q(1,2))
    assert r['sine_transmitted']==Q(1,3)
    print(r,angle_degrees(r['sine_transmitted']))
    assert thin_lens(2,4)==dict(kind='real',q=Q(4),magnification=Q(-1))
    print(thin_lens(2,1),thin_lens(2,2))
