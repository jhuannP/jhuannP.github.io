"""Contagens sintéticas exatas: a=AB,b=A Bc,c=Ac B,d=Ac Bc."""
from fractions import Fraction as F

def inspect(a=2,b=1,c=1,d=2):
    counts=(a,b,c,d)
    if any(isinstance(v,bool) or not isinstance(v,int) or v<0 for v in counts):
        raise ValueError('Contagens inteiras não negativas')
    n=sum(counts)
    if n==0:return dict(counts=counts,n=0,pA=None,pB=None,joint=None,a_given_b=None,b_given_a=None,independent=None)
    return dict(counts=counts,n=n,pA=F(a+b,n),pB=F(a+c,n),joint=F(a,n),a_given_b=F(a,a+c) if a+c else None,b_given_a=F(a,a+b) if a+b else None,independent=a*n==(a+b)*(a+c))

if __name__=='__main__':
    s=inspect();assert s['a_given_b']==F(2,3)
    print(s)
