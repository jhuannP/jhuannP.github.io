"""Modelo termodinâmico didático. SI; sem taxa, rendimento ou dados medidos."""
from math import isfinite, log

R = 8.314       # J/(mol K), constante arredondada para o exemplo
F = 96485.0     # C/mol, constante arredondada para o exemplo


def finite(value):
    if type(value) not in (int,float):
        raise ValueError('Use int/float finito, sem booleanos.')
    try:
        result=float(value)
    except OverflowError:
        raise ValueError('Fora da escala float.') from None
    if not isfinite(result):
        raise ValueError('Valor finito necessário.')
    return result


def transfer(pH_from,pH_to,psi_from,psi_to,T=300):
    """Δμ por mol de H+ da origem ao destino, em J/mol; psi em V, T em K."""
    a,b,c,d,T=map(finite,(pH_from,pH_to,psi_from,psi_to,T))
    if T<=0:
        raise ValueError('Temperatura absoluta positiva necessária.')
    chemical=finite(-R*T*log(10)*(b-a))
    electric=finite(F*(d-c))
    return dict(chemical=chemical,electric=electric,total=finite(chemical+electric))


def coupled(dg_proton,protons,dg_atp):
    """Ciclo hipotético: m prótons por ATP, síntese endergônica dada, em J/mol ATP."""
    dg_proton,dg_atp=finite(dg_proton),finite(dg_atp)
    if type(protons) is not int or protons<=0 or dg_atp<=0:
        raise ValueError('Exige m inteiro positivo e ΔG de síntese positivo.')
    return finite(dg_atp+protons*dg_proton)


if __name__=='__main__':
    inbound=transfer(7,8,0,-.15)
    print('Retorno P→N: pH 7→8, psi 0→−0.15 V, T=300 K.')
    print('Contribuições em kJ/mol H+:',{k:v/1000 for k,v in inbound.items()})
    print('Bombeamento N→P, kJ/mol H+:',transfer(8,7,-.15,0)['total']/1000)
    for m in (2,3):
        print('Ciclo hipotético, m=',m,'ΔG ATP=50 kJ/mol; ΔG ciclo kJ/mol:',
              coupled(inbound['total'],m,50000)/1000)
    print('Sinal favorável não determina taxa, acoplamento real ou rendimento de ATP.')
