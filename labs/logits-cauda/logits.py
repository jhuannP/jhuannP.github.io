"""BCE escalar para rótulos inteiros0/1. Sem framework ou autodiff."""
from math import exp,log1p,log,isfinite,isclose
from decimal import Decimal,localcontext

def checked(z,y):
    if type(y) is not int or y not in (0,1) or isinstance(z,bool):raise ValueError('logit finito e rótulo inteiro0/1 necessários')
    try:z=float(z)
    except (TypeError,ValueError,OverflowError):raise ValueError('logit finito necessário') from None
    if not isfinite(z):raise ValueError('logit finito necessário')
    return z

def sigmoid(z):
    if z>=0:return 1/(1+exp(-z))
    q=exp(z);return q/(1+q)

def loss(z,y):
    z=checked(z,y)
    return (max(z,0)-y*z)+log1p(exp(-abs(z)))

def gradient(z,y):
    z=checked(z,y)
    return sigmoid(z) if y==0 else -sigmoid(-z)

if __name__=='__main__':
    cases=0
    with localcontext() as ctx:
        ctx.prec=500
        for z in (-1000,-50,-10,-1,0,1,10,50,1000):
            for y in (0,1):
                dz=Decimal(z);prob=1/(1+(-dz).exp())
                ref=-(prob.ln() if y else (1-prob).ln())
                gref=prob-Decimal(y)
                assert isclose(loss(z,y),float(ref),rel_tol=1e-14,abs_tol=0.)
                assert isclose(gradient(z,y),float(gref),rel_tol=1e-14,abs_tol=0.)
                cases+=1
    for z in (-3,-1,0,1,3):
        for y in (0,1):
            h=1e-5;finite_diff=(loss(z+h,y)-loss(z-h,y))/(2*h)
            assert isclose(finite_diff,gradient(z,y),rel_tol=1e-8,abs_tol=1e-9)
    r=log1p(exp(-50))
    assert (50+r)-50==0 and loss(50,1)==r>0
    assert gradient(50,1)<0 and sigmoid(50)-1==0
    assert loss(1000,1)==0 and loss(1000,0)==1000
    mean=(loss(0,1)+loss(0,0))/2
    assert mean==log(2) and (gradient(0,1)/2,gradient(0,0)/2)==(-.25,.25)
    for z,y in [(True,1),(0,True),(0,.5),(float('inf'),1),(0,2)]:
        try:loss(z,y)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print(cases,'valores/gradientes versus Decimal500;10 diferenças finitas;cancelamento,underflow,batch e contratos aprovados.')
