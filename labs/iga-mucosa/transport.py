"""Contabilidade didática de leituras sintéticas; não simula transporte de IgA."""
from fractions import Fraction as Q

def _q(value, positive=False):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise ValueError('Use inteiro ou Fraction na unidade declarada.')
    value=Q(value)
    if value<0 or (positive and value==0):
        raise ValueError('Grandeza negativa ou denominador não positivo.')
    return value

def apical_readout(measured_ug_ml,blank_ug_ml,volume_ml,area_cm2,hours):
    c,b=map(_q,(measured_ug_ml,blank_ug_ml))
    v,a,t=(_q(x,positive=True) for x in (volume_ml,area_cm2,hours))
    if c<b:raise ValueError('Leitura abaixo do branco; rever dados, não truncar.')
    mass=(c-b)*v
    return {'mass_ug':mass,'apparent_rate_ug_cm2_h':mass/(a*t)}

def recovery(initial_ug,donor_ug,apical_ug,cell_ug):
    initial=_q(initial_ug,positive=True)
    total=sum((_q(x) for x in (donor_ug,apical_ug,cell_ug)),Q(0))
    return {'fraction':total/initial,'unaccounted_ug':initial-total,'over_recovery':total>initial}

if __name__=='__main__':
    for label,c,v in [('A',12,Q(1,2)),('B',7,Q(1,2)),('B_volume',7,Q(1))]:
        print(label,apical_readout(c,2,v,1,2))
    print('Balanço:',recovery(20,12,5,1))
