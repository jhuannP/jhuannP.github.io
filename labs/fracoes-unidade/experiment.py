"""Soma exata de duas frações não negativas na mesma unidade."""
from math import gcd

def model(p=1,q=3,r=1,s=4):
    if any(isinstance(x,bool) or not isinstance(x,int) for x in (p,q,r,s)) or not(0<=p<=6 and 0<=r<=6 and 1<=q<=6 and 1<=s<=6):
        raise ValueError('Numeradores inteiros 0–6; denominadores inteiros 1–6')
    common=q*s//gcd(q,s);a=p*(common//q);b=r*(common//s);n=a+b;g=gcd(n,common)
    return dict(p=p,q=q,r=r,s=s,common=common,a=a,b=b,n=n,numerator=n//g,denominator=common//g,extent=max(1,(n+common-1)//common))

if __name__=='__main__':
    s=model();assert (s['n'],s['common'])==(7,12)
    print(s)
