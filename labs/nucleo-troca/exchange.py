"""Balanço ideal de carga entre dois compartimentos; não implementa Ran."""
from fractions import Fraction as Q


def rational(value, zero=False):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise ValueError('Use int ou Fraction')
    value=Q(value)
    if value < 0 or (value == 0 and not zero):
        raise ValueError('Valor positivo exigido')
    return value


def stationary(total, a, b, vc=1, vn=1):
    total=rational(total,zero=True)
    a,b,vc,vn=map(rational,(a,b,vc,vn))
    nuclear=total*a/(a+b); cytosolic=total-nuclear
    return dict(nuclear=nuclear,cytosolic=cytosolic,
                cn=nuclear/vn,cc=cytosolic/vc,
                ratio=None if total==0 else (nuclear/vn)/(cytosolic/vc),
                inward=a*cytosolic,outward=b*nuclear,
                tau=1/(a+b))


def derivative(nuclear,total,a,b):
    nuclear=rational(nuclear,zero=True);total=rational(total,zero=True)
    a,b=map(rational,(a,b))
    if nuclear > total:
        raise ValueError('Carga nuclear fora do total')
    return a*(total-nuclear)-b*nuclear


if __name__=='__main__':
    r=stationary(12,3,1,3,1)
    assert r['nuclear']==9 and r['ratio']==9
    assert r['inward']==r['outward']==9 and r['tau']==Q(1,4)
    slow=stationary(12,Q(3,10),Q(1,10),3,1)
    assert slow['nuclear']==9 and slow['tau']==Q(5,2)
    print('Rápido:',r,'Lento:',slow)
