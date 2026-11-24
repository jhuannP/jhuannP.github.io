"""HA/NaA com adição idealizada de HCl (q<0) ou NaOH (q>0).
Quantidades por volume final fixo, normalizadas por c°=1 mol/L.
Sem ajuste de atividades, volume de titulante ou dados medidos.
"""
from math import sqrt,log10,log,isfinite
KW=1e-14

def positive_water_root(b,Kw):
    d=sqrt(b*b+4*Kw)
    return 2*Kw/(b+d) if b>=0 else (-b+d)/2

def solve(Ca,Cs,q=0.,Ka=1e-5,Kw=KW):
    if not all(isfinite(v) for v in (Ca,Cs,q,Ka,Kw)) or min(Ca,Cs)<0 or min(Ka,Kw)<=0:
        raise ValueError('Concentrações não negativas e constantes positivas, valores finitos')
    C=Ca+Cs;Na=Cs+max(q,0);Cl=max(-q,0);S=Cs+q
    lo=positive_water_root(S,Kw);hi=positive_water_root(S-C,Kw)
    if C==0:h=lo
    else:
        lo,hi=log10(lo),log10(hi)
        for _ in range(100):
            mid=(lo+hi)/2;z=10**mid
            if z+S-Kw/z-C*Ka/(Ka+z)>0:hi=mid
            else:lo=mid
        h=10**((lo+hi)/2)
    a=C*Ka/(Ka+h);u=C*h/(Ka+h);o=Kw/h
    base_pre=Cs+q;acid_pre=Ca-q
    hh=-log10(Ka)+log10(base_pre/acid_pre) if C and min(base_pre,acid_pre)>1e-12*C else None
    beta=log(10)*(h+o+C*Ka*h/(Ka+h)**2)
    return dict(h=h,anion=a,acid=u,oh=o,sodium=Na,chloride=Cl,pH=-log10(h),
                hh=hh,beta=beta,charge=h+Na-a-o-Cl,mass=a+u-C,
                acid_pre=acid_pre,base_pre=base_pre)

if __name__=='__main__':
    for q in (-.006,0,.001,.006):print(q,solve(.005,.005,q))
