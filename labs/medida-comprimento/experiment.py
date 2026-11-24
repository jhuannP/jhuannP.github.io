"""Barra ideal em movimento inercial: eventos em unidades ct/L0,x/L0."""
from math import sqrt,isfinite

def real(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v):raise ValueError('Número real finito.')
    return v

def boost(tau,u,beta):
    real(tau);real(u);real(beta)
    if abs(beta)>=1:raise ValueError('Boost subluminal.')
    gamma=1/sqrt(1-beta*beta)
    out=[gamma*(tau-beta*u),gamma*(u-beta*tau)]
    if not all(isfinite(v) for v in out):raise ValueError('Transformação fora do alcance numérico.')
    return out

def model(beta=.6,length=2,mode=0):
    real(beta);real(length)
    if abs(beta)>.8 or not .5<=length<=4 or type(mode) is not int or mode not in (0,1):raise ValueError('β−0,8..0,8, L0=0,5..4m, par0/1.')
    gamma=1/sqrt(1-beta*beta);a=[0.,0.]
    b=[0.,1/gamma] if mode==0 else boost(0.,1.,-beta)
    ap=boost(*a,beta);bp=boost(*b,beta)
    dtau=b[0]-a[0];du=b[1]-a[1];dtaup=bp[0]-ap[0];dup=bp[1]-ap[1]
    return dict(beta=beta,length=length,mode=mode,gamma=gamma,a=a,b=b,ap=ap,bp=bp,
                lab_length=length/gamma,lab_span=length*du,rest_span=length*dup,
                delta_ct=length*dtau,delta_ct_prime=length*dtaup,
                simultaneous_lab=mode==0 or beta==0,simultaneous_rest=mode==1 or beta==0,
                invariant_lab=length*length*(dtau*dtau-du*du),invariant_rest=length*length*(dtaup*dtaup-dup*dup))

if __name__=='__main__':
    for mode in (0,1):print(model(mode=mode))
