"""Família sintética 2×2; diagnósticos analíticos separados de avaliação float."""
from math import isfinite,fsum

def model(exponent=3,s=1,direction=0,scale=0):
    if type(exponent) is not int or not 1<=exponent<=6 or type(direction) is not int or direction not in (0,1) or type(scale) is not int or not -3<=scale<=3:
        raise ValueError('Expoente1..6, direção0/1, escala inteira−3..3.')
    if isinstance(s,bool) or not isinstance(s,(int,float)) or not isfinite(s) or not -1<=s<=1:raise ValueError('s finito em[−1,1].')
    delta=10.**(-exponent);c=10.**scale
    A=[[c,c],[c,c*(1+delta)]];b=[2*c,c*(2+delta)];xhat=[1+s,1+(-s if direction==0 else s)]
    r=[0,c*delta*s] if direction==0 else [-2*c*s,-c*(2+delta)*s]
    norm_a=c*(2+delta);norm_inv=(2+delta)/(c*delta);kappa=(2+delta)**2/delta
    absolute=max(abs(v) for v in r);relative=absolute/(c*(2+delta));error=abs(s)
    rf=[bi-fsum(a*x for a,x in zip(row,xhat)) for row,bi in zip(A,b)]
    return dict(exponent=exponent,s=s,direction=direction,scale=scale,delta=delta,c=c,A=A,b=b,xhat=xhat,r=r,
                norm_a=norm_a,norm_inv=norm_inv,kappa=kappa,residual_abs=absolute,residual_relative=relative,
                error_relative=error,bound=kappa*relative,lower=relative/kappa,residual_float=rf,
                residual_float_norm=max(abs(v) for v in rf))

if __name__=='__main__':
    m=model();assert m['error_relative']==1;assert abs(m['residual_abs']-.001)<1e-12
    print(m)
