"""Modelo estático de três regiões; pesos e taxas sintéticos, sem ajuste."""
from fractions import Fraction as Q

def rational(x,lo,hi):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or not lo<=x<=hi:
        raise ValueError('Use int/Fraction dentro do intervalo documentado')
    return Q(x)

def contrast(left,center,right):
    left=rational(left,0,2);center=rational(center,0,2);right=rational(right,0,2)
    return center-(left+right)/2

def rates(left,center,right,baseline=10,gain=10):
    baseline=rational(baseline,0,100);gain=rational(gain,0,100)
    c=contrast(left,center,right)
    return {'contrast':c,'on':max(Q(0),baseline+gain*c),
            'off':max(Q(0),baseline-gain*c)}

if __name__=='__main__':
    for name,stim in [('uniforme',(1,1,1)),('centro',(Q(1,2),2,Q(1,2))),
                      ('vizinhos',(Q(3,2),0,Q(3,2)))]:
        print(name,stim,rates(*stim))
    assert rates(Q(1,2),2,Q(1,2))['on']==25
