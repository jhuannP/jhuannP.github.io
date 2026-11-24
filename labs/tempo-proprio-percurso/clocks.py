"""Trechos inerciais em unidades c=1: tempo em anos, x em anos-luz no exemplo."""
from fractions import Fraction as Q
from math import sqrt,fsum


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float.')
    return Q(x)


def speed(beta):
    beta=rational(beta)
    if abs(beta)>=1:raise ValueError('Relógio material requer |beta|<1.')
    return beta


def journey(segments):
    if type(segments) not in (list,tuple) or not 1<=len(segments)<=64:
        raise ValueError('Forneça de um a 64 trechos.')
    t=x=Q(0);taus=[];events=[{'t':t,'x':x,'tau':0.0}];intervals=[]
    for segment in segments:
        if type(segment) is not tuple or len(segment)!=2:
            raise ValueError('Trecho é tupla(delta_t,beta).')
        dt,beta=segment;dt=rational(dt);beta=speed(beta)
        if not 0<=dt<=10**6:raise ValueError('Delta t entre0 e10^6 no código.')
        dx=beta*dt;proper2=dt*dt-dx*dx
        square_float=float(proper2)
        if proper2 and not square_float:raise ValueError('Intervalo abaixo da resolução float.')
        tau=sqrt(square_float)
        t+=dt;x+=dx;taus.append(tau)
        intervals.append({'dt':dt,'dx':dx,'proper_squared':proper2,'proper':tau})
        events.append({'t':t,'x':x,'tau':fsum(taus)})
    return {'events':events,'segments':intervals,'elapsed':t,
            'displacement':x,'proper':fsum(taus)}


def earth_simultaneous(t,x,beta):
    # Terra em x=0; plano de simultaneidade do referencial instantâneo escolhido.
    t,x=map(rational,(t,x));beta=speed(beta)
    return t-beta*x


if __name__=='__main__':
    r=journey([(5,Q(3,5)),(5,Q(-3,5))])
    print('Eventos:',r['events'])
    print('Terra:',r['elapsed'],'anos; viajante:',r['proper'],'anos')
    for beta in (Q(3,5),Q(-3,5)):
        print('Tempo terrestre simultâneo com a virada, beta=',beta,
              earth_simultaneous(5,3,beta),'anos')
    print('Virada instantânea ideal; relógio local não salta, atribuição distante muda.')
