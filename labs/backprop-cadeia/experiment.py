"""Decompor o gradiente da rede própria; executar como módulo na raiz do protótipo."""
from fractions import Fraction as Q
import dense_net as net

def two_paths(u):
    if type(u) not in (int,Q):raise ValueError("u inteiro ou Fraction")
    return dict(r=u*u,s=3*u,z=u*u+3*u,dz_du=2*u+3)

def breakdown(model,X,y,lam=0):
    H=net.validate(model);X,y=net.data(X,y);lam=net.real(lam)
    if lam<0:raise ValueError("Penalidade não negativa")
    N=len(y);records=[]
    g=dict(W=[[0.]*2 for _ in range(H)],b=[0.]*H,v=[0.]*H,c=0.)
    for x,target in zip(X,y):
        forward=net.forward(model,x);h=forward['hidden']
        delta=(forward['probability']-target)/N
        local=[delta*model['v'][j]*(1-h[j]*h[j]) for j in range(H)]
        dW=[[local[j]*x[k] for k in range(2)] for j in range(H)]
        dv=[delta*h[j] for j in range(H)]
        records.append(dict(x=x,y=target,forward=forward,delta=delta,local=local,dW=dW,dv=dv))
        g['c']+=delta
        for j in range(H):
            g['b'][j]+=local[j];g['v'][j]+=dv[j]
            for k in range(2):g['W'][j][k]+=dW[j][k]
    # A penalidade pertence ao objetivo do batch, somada uma vez.
    for j in range(H):
        g['v'][j]+=lam*model['v'][j]
        for k in range(2):g['W'][j][k]+=lam*model['W'][j][k]
    return dict(records=records,gradient=g)

def fixture():
    return dict(W=[[0.,0.],[0.,0.]],b=[0.,0.],v=[2.,-1.],c=0.)

if __name__=='__main__':
    result=breakdown(fixture(),[[1,2],[-1,1]],[1,0])
    assert result['gradient']['W']==[[-1.,-.5],[.5,.25]]
    assert two_paths(2)['dz_du']==7
    print(result)
