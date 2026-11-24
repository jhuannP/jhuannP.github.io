"""Contabilidade racional de carga; não prevê reações ou controle da célula."""
from fractions import Fraction as Q

def number(x,lo,hi):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or not lo<=x<=hi:
        raise ValueError('Use int/Fraction no intervalo documentado')
    return Q(x)

def charge(segments):
    if not isinstance(segments,(list,tuple)) or not 1<=len(segments)<=100:
        raise ValueError('Forneça de 1 a 100 trechos')
    total=Q(0)
    for pair in segments:
        if not isinstance(pair,(list,tuple)) or len(pair)!=2: raise ValueError('Use (I_A,t_s)')
        current=number(pair[0],0,1000);time=number(pair[1],0,86400)
        total+=current*time
    if total>10**9: raise ValueError('Carga excede orçamento de 10**9 C')
    return total

def deposition(coulombs,molar_mass,z,eta=1,faraday=96500,available=None):
    coulombs=number(coulombs,0,10**9);molar_mass=number(molar_mass,Q(1,10),1000)
    faraday=number(faraday,1000,10**6);eta=number(eta,0,1)
    if isinstance(z,bool) or not isinstance(z,int) or not 1<=z<=8:
        raise ValueError('z inteiro de 1 a 8')
    product=eta*coulombs/(z*faraday)
    if available is not None and product>number(available,0,10**6):
        raise ValueError('Modelo com eta constante excede o inventário fornecido')
    return {'electron_mol':coulombs/faraday,'product_mol':product,
            'mass_g':product*molar_mass,'target_C':eta*coulombs,
            'other_C':(1-eta)*coulombs}

def required_charge(mass,molar_mass,z,eta=1,faraday=96500):
    mass=number(mass,0,10**6);molar_mass=number(molar_mass,Q(1,10),1000)
    eta=number(eta,Q(1,10**6),1);faraday=number(faraday,1000,10**6)
    if isinstance(z,bool) or not isinstance(z,int) or not 1<=z<=8:raise ValueError('z inteiro1..8')
    result=mass*z*faraday/(eta*molar_mass)
    return number(result,0,10**9)

if __name__=='__main__':
    q=charge([(1,1930)])
    result=deposition(q,Q(127,2),2,Q(4,5))
    assert result['mass_g']==Q(127,250)
    print('Q_C=',q,result)
    print('tempo a1A para1,27g:',required_charge(Q(127,100),Q(127,2),2,Q(4,5)),'s')
