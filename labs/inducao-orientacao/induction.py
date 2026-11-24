"""SI, campo uniforme imposto, área vetorial fixa e regime resistivo sem autoindução."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float')
    return Q(x)


def vector(v):
    if not isinstance(v,(list,tuple)) or len(v)!=3:raise ValueError('Vetor de três componentes')
    return tuple(map(rational,v))


def dot(a,b):
    a,b=map(vector,(a,b));return sum((x*y for x,y in zip(a,b)),Q(0))


def force(charge,velocity,field):
    charge=rational(charge);v=vector(velocity);b=vector(field)
    return tuple(charge*x for x in (v[1]*b[2]-v[2]*b[1],v[2]*b[0]-v[0]*b[2],v[0]*b[1]-v[1]*b[0]))


def turns_count(turns):
    if type(turns) is not int or turns<1:raise ValueError('Número inteiro positivo de espiras')
    return turns


def mean_emf(initial_flux,final_flux,seconds,turns=1):
    initial_flux,final_flux,seconds=map(rational,(initial_flux,final_flux,seconds))
    turns=turns_count(turns)
    if seconds<=0:raise ValueError('Intervalo positivo')
    return -turns*(final_flux-initial_flux)/seconds


def fixed_loop(area_vector,field0,field_rate,resistance,time=0,turns=1):
    """B(t)=field0+field_rate*t; fluxo por espira, R total.

    Normal e contorno positivo ligados pela mão direita. Corrente=emf/R
    aproxima resposta puramente resistiva, sem autoindução/realimentação.
    """
    a,b0,rate=map(vector,(area_vector,field0,field_rate))
    resistance,time=map(rational,(resistance,time));turns=turns_count(turns)
    if dot(a,a)==0 or resistance<=0 or time<0:raise ValueError('Área não nula, R positiva, tempo não negativo')
    field=tuple(b+r*time for b,r in zip(b0,rate))
    flux=dot(field,a);flux_rate=dot(rate,a);emf=-turns*flux_rate
    current=emf/resistance
    return dict(flux=flux,flux_rate=flux_rate,emf=emf,current=current,power=current**2*resistance)


if __name__=='__main__':
    assert force(1,(2,0,0),(0,0,3))==(0,-6,0)
    assert mean_emf(0,6,3)==-2
    r=fixed_loop((0,0,Q(1,5)),(0,0,1),(0,0,2),4)
    assert r['emf']==Q(-2,5) and r['current']==Q(-1,10) and r['power']==Q(1,25)
    print(r)
