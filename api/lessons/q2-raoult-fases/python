"""Equilíbrio binário ideal a T,P: pressões de saturação prescritas, sem dados reais."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction, não float ou bool.')
    return Q(x)


def parameters(pA,pB):
    pA,pB=map(rational,(pA,pB))
    if not pA>pB>0:
        raise ValueError('Exige pA*>pB*>0; A é o mais volátil neste recorte.')
    return pA,pB


def bubble(pA,pB,x):
    pA,pB=parameters(pA,pB);x=rational(x)
    if not 0<=x<=1:raise ValueError('Composição fora de [0,1].')
    return x*pA+(1-x)*pB


def dew(pA,pB,y):
    pA,pB=parameters(pA,pB);y=rational(y)
    if not 0<=y<=1:raise ValueError('Composição fora de [0,1].')
    return 1/(y/pA+(1-y)/pB)


def split_at_tp(pA,pB,P,z,N=1):
    """p* e P na mesma unidade; N em mol; z fração global A, estritamente entre0 e1.

    Ideal líquido+gás, T fixa, sem reação; não resolve balanço de energia.
    x/y são frações molares A nas fases; beta=nV/N, diferente de y.
    Em bolha/orvalho, a composição da fase ausente é o limite incipiente.
    Fora da coexistência, a composição da fase ausente é None.
    """
    pA,pB=parameters(pA,pB);P,z,N=map(rational,(P,z,N))
    if P<=0 or N<=0 or not 0<z<1:
        raise ValueError('P,N positivos e 0<z<1; componentes puros fora deste solver.')
    pb,pd=bubble(pA,pB,z),dew(pA,pB,z)
    if P>pb:regime,beta,x,y='liquid',Q(0),z,None
    elif P<pd:regime,beta,x,y='vapor',Q(1),None,z
    else:
        x=(P-pB)/(pA-pB);y=x*pA/P
        beta=(z-x)/(y-x)
        regime='bubble' if P==pb else 'dew' if P==pd else 'two-phase'
    nV=N*beta;nL=N-nV
    liquid_A=nL*x if x is not None else Q(0)
    vapor_A=nV*y if y is not None else Q(0)
    return dict(pA=pA,pB=pB,P=P,z=z,N=N,regime=regime,bubble=pb,dew=pd,
                x=x,y=y,beta=beta,nL=nL,nV=nV,
                liquid_A=liquid_A,liquid_B=nL-liquid_A,
                vapor_A=vapor_A,vapor_B=nV-vapor_A)


def rr_bracket(pA,pB,P,z,steps=60):
    """Bisseção racional da equação de balanço; só estados estritamente bifásicos.

    Ki=pi*/P; f(beta)=sum zi(Ki-1)/(1+beta(Ki-1)).
    Retorna intervalo inclusivo com largura <=2**(-steps); não erro de modelo.
    """
    if isinstance(steps,bool) or not isinstance(steps,int) or not 1<=steps<=128:
        raise ValueError('steps inteiro entre1 e128.')
    a=split_at_tp(pA,pB,P,z)
    if a['regime']!='two-phase':raise ValueError('Use só interior bifásico.')
    K=(a['pA']/a['P'],a['pB']/a['P']);zi=(a['z'],1-a['z'])
    def f(b):return sum(v*(k-1)/(1+b*(k-1)) for v,k in zip(zi,K))
    lo,hi=Q(0),Q(1)
    for _ in range(steps):
        mid=(lo+hi)/2;value=f(mid)
        if value==0:return mid,mid
        if value>0:lo=mid
        else:hi=mid
    return lo,hi


if __name__=='__main__':
    print('Pressões prescritas em kPa, mesma T; N em mol, sem identidade química real.')
    print(split_at_tp(80,20,40,Q(2,5),5))
    print('Intervalo de beta por balanço numérico:',rr_bracket(80,20,40,Q(2,5)))
