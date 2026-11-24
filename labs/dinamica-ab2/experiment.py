"""AB2 angular harmônico próprio: nove coordenadas, três deformações lineares."""
import math
from fractions import Fraction as F
POSITIONS=((0,0,0),(1,0,1),(-1,0,1))
J=((-1,0,-1,1,0,1,0,0,0),
   (1,0,-1,0,0,0,-1,0,1),
   (0,0,-1,-F(1,2),0,F(1,2),F(1,2),0,F(1,2)))

def matrices(mass=2,kappa=F(1)):
    weights=(mass,)*3+(1,)*6
    h=[[sum(F(k)*J[r][i]*J[r][j] for r,k in enumerate((1,1,kappa))) for j in range(9)] for i in range(9)]
    d=[[float(h[i][j])/math.sqrt(weights[i]*weights[j]) for j in range(9)] for i in range(9)]
    return weights,h,d

def modes(mass=2,bend=4):
    if type(mass) is not int or not 1<=mass<=8 or type(bend) is not int or not 0<=bend<=8:
        raise ValueError('Massa central inteira 1..8, rigidez angular em quartos 0..8')
    k=bend/4;a=2+2/mass;b=1/mass;c=1+1/mass
    weights,h,d=matrices(mass,F(bend,4))
    def lift(g,scale):
        v=[sum(float(J[r][i])*g[r] for r in range(3))/weights[i]/scale for i in range(9)]
        # Fase definida pelas combinações internas; v e -v são o mesmo modo.
        return tuple(v)
    asymmetric=lift((1/math.sqrt(2),-1/math.sqrt(2),0),math.sqrt(a))
    if k==0:
        det=a*c-2*b*b;g=(-b/det,-b/det,a/det)
        lower=tuple(-v for v in lift(g,math.sqrt(a/det)))
        upper=lift((1/math.sqrt(2),1/math.sqrt(2),0),math.sqrt(a))
        lambdas=(0.,a,a)
    else:
        coupling=math.sqrt(2*k)*b
        delta=math.sqrt((a-k*c)**2+4*coupling**2)
        lambdas=((a+k*c-delta)/2,a,(a+k*c+delta)/2)
        def eigenvector(lam):
            s,t=coupling,lam-a;norm=math.hypot(s,t);s/=norm;t/=norm
            return lift((s/math.sqrt(2),s/math.sqrt(2),math.sqrt(k)*t),math.sqrt(lam))
        lower=eigenvector(lambdas[0]);upper=eigenvector(lambdas[2])
    result=[]
    for i,(lam,vector,irrep) in enumerate(zip(lambdas,(lower,asymmetric,upper),('A1','B1','A1'))):
        residual=max(abs(sum(float(h[row][col])*vector[col] for col in range(9))-lam*weights[row]*vector[row]) for row in range(9))
        result.append(dict(index=i,eigenvalue=lam,omega=math.sqrt(max(0,lam)),vector=vector,irrep=irrep,
                           mass_norm=sum(w*v*v for w,v in zip(weights,vector)),residual=residual,
                           floppy=k==0 and i==0))
    return result

def model(mass=2,bend=4,mode=0,amplitude=1):
    if type(mode) is not int or mode not in (0,1,2):raise ValueError('Modo 0..2')
    if isinstance(amplitude,bool) or not isinstance(amplitude,(int,float)) or not math.isfinite(amplitude) or not -1<=amplitude<=1:
        raise ValueError('Fator visual finito entre -1 e 1')
    rows=modes(mass,bend);selected=rows[mode];v=selected['vector'];maximum=max(abs(x) for x in v)
    display=tuple(amplitude*.25*x/maximum for x in v)
    return dict(mass=mass,kappa=bend/4,mode=mode,amplitude=amplitude,rows=rows,selected=selected,
                displacement=display,positions=tuple(tuple(p[a]+display[3*i+a] for a in range(3)) for i,p in enumerate(POSITIONS)),
                rigid_zeros=6,internal_zeros=int(bend==0))

if __name__=='__main__':
    r=model();assert abs(r['selected']['eigenvalue']-(9-math.sqrt(17))/4)<1e-12
    assert model(bend=0)['selected']['floppy']
    print([(x['irrep'],x['eigenvalue'],x['omega']) for x in r['rows']])
