"""Duas reações sintéticas; atividades adimensionais, T=300 K."""
from math import log, exp
RT=.008314*300  # kJ/mol; R arredondado.

def model(log_q=0):
    if type(log_q) is not int or not -3<=log_q<=3:
        raise ValueError("log10 Q inteiro de -3 a 3")
    q=10.**log_q
    correction=RT*log(q)
    target=12+correction;donor=-20
    net=target+donor
    return dict(log_q=log_q,q=q,target=target,donor=donor,net=net,
                equilibrium_q=exp(8/RT))

if __name__=='__main__':
    for exponent in range(-3,4):print(model(exponent))
