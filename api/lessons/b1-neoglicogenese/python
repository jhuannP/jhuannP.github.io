"""Inventário reduzido em mol. Não é balanço completo de átomos/carga ou taxa."""
from fractions import Fraction as Q


def amount(value):
    if type(value) not in (int,Q) or value<0:
        raise ValueError('Use quantidade não negativa em int/Fraction, em mol.')
    return Q(value)


def inventory(glucose,precursor='pyruvate'):
    g=amount(glucose)
    if precursor not in ('pyruvate','lactate'):
        raise ValueError('Precursor fora deste recorte.')
    generated=2*g if precursor=='lactate' else Q(0)
    return dict(glucose=g,precursor=2*g,ATP_carboxylase=2*g,ATP_PGK=2*g,
                ATP_total=4*g,GTP=2*g,NADH_used=2*g,NADH_from_lactate=generated,
                NADH_net_used=2*g-generated,carbon_input=6*g,carbon_glucose=6*g,
                carbon_temporarily_added=2*g,carbon_released=2*g)


def limit_from_pyruvate(pyruvate,ATP,GTP,NADH):
    """Teto estequiométrico com estoques finitos e sem regeneração de cofatores."""
    available=dict(zip(('pyruvate','ATP','GTP','NADH'),map(amount,(pyruvate,ATP,GTP,NADH))))
    required=dict(pyruvate=Q(2),ATP=Q(4),GTP=Q(2),NADH=Q(2))
    ceiling=min(available[k]/required[k] for k in required)
    remaining={k:available[k]-required[k]*ceiling for k in required}
    return dict(ceiling=ceiling,remaining=remaining,
                limiting=[k for k in required if remaining[k]==0])


if __name__=='__main__':
    for precursor in ('pyruvate','lactate'):
        print('Para 3 mmol de glicose, a partir de',precursor)
        print({k:1000*v for k,v in inventory(Q(3,1000),precursor).items()})
        print('Quantidade em mmol; linhas de carbono em mmol de átomos C.')
    print('Estoques em mol: 2 piruvato,4 ATP,1 GTP,2 NADH:')
    print(limit_from_pyruvate(2,4,1,2))
    print('Teto de um modelo de estoques, não previsão de conversão celular.')
