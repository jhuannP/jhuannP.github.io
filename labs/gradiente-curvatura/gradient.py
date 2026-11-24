"""MSE linear: gradiente, passo simultâneo e escala, com frações exatas."""
from fractions import Fraction as Q
from itertools import product

def data(x,y):
    if not x or len(x)!=len(y):raise ValueError("Pares não vazios de mesmo tamanho")
    if any(isinstance(t,bool) or not isinstance(t,(int,Q)) for t in [*x,*y]):
        raise ValueError("Entradas racionais")
    return tuple(map(Q,x)),tuple(map(Q,y))

def loss(x,y,w,b):
    x,y=data(x,y)
    return sum((w*a+b-t)**2 for a,t in zip(x,y))/len(x)

def gradient(x,y,w,b):
    x,y=data(x,y);err=[w*a+b-t for a,t in zip(x,y)]
    return 2*sum(e*a for e,a in zip(err,x))/len(x),2*sum(err)/len(x)

def step(x,y,w,b,eta_w,eta_b=None):
    eta_b=eta_w if eta_b is None else eta_b
    if any(isinstance(v,bool) or not isinstance(v,(int,Q)) or v<0 for v in (eta_w,eta_b)):
        raise ValueError("Passos racionais não negativos")
    dw,db=gradient(x,y,w,b)
    return w-eta_w*dw,b-eta_b*db

def verify():
    datasets=[([-1,0,1],[-1,1,3]),([0,1,3],[1,3,7]),([1],[2])]
    checks=0
    for x,y in datasets:
        for w,b in product(range(-2,3),repeat=2):
            dw,db=gradient(x,y,w,b)
            for eps in (Q(1,10),Q(1,100)):
                # Exato para esta quadrática: não usa a expressão do gradiente.
                assert (loss(x,y,w+eps,b)-loss(x,y,w-eps,b))/(2*eps)==dw
                assert (loss(x,y,w,b+eps)-loss(x,y,w,b-eps))/(2*eps)==db
                checks+=1
    x,y=datasets[0];states=0
    for eta in (Q(1,10),Q(3,4),Q(1),Q(11,10)):
        w=b=Q(0)
        for n in range(13):
            assert w==2-2*(1-4*eta/3)**n
            assert b==1-(1-2*eta)**n
            assert loss(x,y,w,b)==Q(2,3)*(w-2)**2+(b-1)**2
            w,b=step(x,y,w,b,eta);states+=1
    assert step(x,y,0,0,Q(1,10))==(Q(4,15),Q(1,5))
    # Atualização sequencial muda o esquema em dados não centrados.
    w,b=step([1],[2],0,0,Q(1,10));assert (w,b)==(Q(2,5),Q(2,5))
    sequential_b=-Q(1,10)*gradient([1],[2],w,0)[1]
    assert sequential_b==Q(8,25)!=b
    # Um ponto não identifica os dois parâmetros.
    assert loss([1],[2],2,0)==loss([1],[2],1,1)==0
    # Reparametrização x'=10x. Passo de w'/100 mantém a trajetória correspondente.
    xp=[10*a for a in x];w=b=wp=bp=Q(0)
    for _ in range(12):
        w,b=step(x,y,w,b,Q(1,10))
        wp,bp=step(xp,y,wp,bp,Q(1,1000),Q(1,10))
        assert wp==w/10 and bp==b
        assert loss(x,y,w,b)==loss(xp,y,wp,bp)
    # Com o mesmo passo0,1, o coeficiente de erro de w' é -37/3.
    assert 1-Q(1,10)*Q(400,3)==-Q(37,3)
    for args in (([],[]),([1],[1,2]),([True],[2])):
        try:data(*args)
        except ValueError:pass
        else:raise AssertionError("contrato")
    print(f"{checks} diferenças centrais exatas (dois parâmetros), {states} estados e 12 reparametrizações conferidos")
    print("Primeiro passo centrado:",step(x,y,0,0,Q(1,10)))

if __name__=='__main__':verify()
