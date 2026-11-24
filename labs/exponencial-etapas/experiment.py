"""Sequência geométrica didática com frações exatas e etapas inteiras."""
from fractions import Fraction as Q

def sequence(initial,factor,steps):
    if type(initial) not in (int,Q) or initial<0:
        raise ValueError("Quantidade inicial inteira ou Fraction não negativa.")
    if type(factor) not in (int,Q) or factor<=0:
        raise ValueError("Fator inteiro ou Fraction estritamente positivo.")
    if type(steps) is not int or not 0<=steps<=256:
        raise ValueError("Etapas inteiras de 0 a 256.")
    initial,factor=Q(initial),Q(factor)
    rows=[]
    for n in range(steps+1):
        value=initial*factor**n
        delta=None if n==0 else value-rows[-1]["value"]
        rows.append(dict(n=n,value=value,delta=delta))
    return rows

if __name__=="__main__":
    for row in sequence(80,Q(3,2),3):
        print(row["n"],row["value"],"variação:",row["delta"])
