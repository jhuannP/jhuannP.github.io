"""Inspect existing MLP gradients and idealized Xavier variance, no new trainer."""
from fractions import Fraction as Q
from dense_net import gradients,update,forward,initialize


def variance_factors(fan_in,fan_out):
    for n in (fan_in,fan_out):
        if type(n) is not int or not 1<=n<=1000:raise ValueError('Fan dimensions must be int 1..1000')
    var=Q(2,fan_in+fan_out)
    return dict(weight_variance=var,amplitude_squared=3*var,
                forward_factor=fan_in*var,backward_factor=fan_out*var)


def paired(outgoing=(1.,1.)):
    """Two identical incoming units; outgoing weights are explicit experimental controls."""
    if not isinstance(outgoing,(list,tuple)) or len(outgoing)!=2:raise ValueError('Two finite output weights')
    from math import isfinite
    if any(type(v) not in (int,float) or not isfinite(v) for v in outgoing):raise ValueError('Two finite output weights')
    return dict(W=[[0.,0.],[0.,0.]],b=[0.,0.],v=list(outgoing),c=0.)


if __name__=='__main__':
    for v in [(1.,1.),(1.,2.),(0.,0.)]:
        m=paired(v);g=gradients(m,[[1.,0.]],[1.]);n=update(m,g,.1)
        print('outgoing',v,'gradient W',g['W'],'next W',n['W'],'next c',n['c'])
    print('2 to 4',variance_factors(2,4))
    print('4 to 1',variance_factors(4,1))
    print('seed42 reproducible',initialize(4,42)==initialize(4,42))
