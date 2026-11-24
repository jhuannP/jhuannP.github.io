"""Auditar o forward da MLP existente; executar como módulo na raiz."""
import dense_net as net

def numeric(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)):
        raise ValueError('use int ou float finito; sem conversão de texto')
    return net.real(x)

def trace(model,x):
    """Cópia numérica local; não altera parâmetros nem calcula gradientes."""
    params={'W':[[numeric(v) for v in row] for row in model['W']],
            'b':[numeric(v) for v in model['b']],
            'v':[numeric(v) for v in model['v']], 'c':numeric(model['c'])}
    net.validate(params); values=[numeric(v) for v in x]
    result=net.forward(params,values)
    pre=[net.real(sum(w*a for w,a in zip(row,values))+b)
         for row,b in zip(params['W'],params['b'])]
    return {'preactivation':pre,**result,'parameter_count':4*len(params['W'])+1}

def decision(probability,threshold=.5):
    p,t=map(numeric,(probability,threshold))
    if not 0<=p<=1 or not 0<t<1:raise ValueError('p em[0,1],limiar em(0,1)')
    return int(p>=t)

def fixture():
    return {'W':[[1.,0.],[-1.,0.]],'b':[0.,0.], 'v':[2.,-2.],'c':0.}

if __name__=='__main__':
    from math import log
    r=trace(fixture(),[log(3)/2,1.])
    print(r)
    print('limiar .5:',decision(r['probability']), 'limiar .9:',decision(r['probability'],.9))
