"""Mistura binária de dois modelos produto: cálculo racional, sem amostragem."""
from fractions import Fraction as F

def probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, F)) or not 0 <= value <= 1:
        raise ValueError('Use int ou Fraction no intervalo [0,1]')
    return F(value)

def independent_mixture(weight, p0, q0, p1, q1):
    """weight=P(G=1), pi=P(A|G=i), qi=P(B|G=i) nos grupos de massa positiva.

    Cada componente é uma distribuição produto por hipótese. Parâmetros de
    componente de peso zero não são probabilidades condicionais identificáveis.
    Células em ordem (A,B)=(0,0),(0,1),(1,0),(1,1).
    """
    w,p0,q0,p1,q1=map(probability,(weight,p0,q0,p1,q1))
    cells=[]
    for a,b in ((0,0),(0,1),(1,0),(1,1)):
        cell0=(p0 if a else 1-p0)*(q0 if b else 1-q0)
        cell1=(p1 if a else 1-p1)*(q1 if b else 1-q1)
        cells.append((1-w)*cell0+w*cell1)
    pa=cells[2]+cells[3];pb=cells[1]+cells[3];joint=cells[3]
    return dict(cells=tuple(cells),a=pa,b=pb,joint=joint,
                gap=joint-pa*pb,independent=joint==pa*pb,
                a_given_b=None if pb==0 else joint/pb,
                a_given_group=(None if w==1 else p0,None if w==0 else p1))

if __name__=='__main__':
    result=independent_mixture(F(1,2),F(1,4),F(1,4),F(3,4),F(3,4))
    assert result['cells']==(F(5,16),F(3,16),F(3,16),F(5,16))
    assert result['joint']==F(5,16) and result['gap']==F(1,16)
    assert result['a_given_b']==F(5,8)
    print(result)
