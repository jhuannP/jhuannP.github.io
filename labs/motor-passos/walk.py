"""Passeio de passos e desligamento independentes; taxas NÃO ajustadas a motor real."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use int/Fraction')
    return Q(x)

def parameters(step,forward,backward,off):
    d,a,b,c=map(rational,(step,forward,backward,off))
    if not Q(1,100)<=d<=100 or not 0<=a<=1000 or not 0<=b<=1000 or a+b==0 or not Q(1,100)<=c<=1000:
        raise ValueError('d em[.01,100]nm,r± em[0,1000]/s com soma positiva,off em[.01,1000]/s')
    return d,a,b,c

def moments(step,forward,backward,time):
    d,a,b,_=parameters(step,forward,backward,1);t=rational(time)
    if not 0<=t<=10:raise ValueError('0<=t<=10s necessário')
    # Passeio não interrompido, ou condicionado à sobrevivência com relógio off independente.
    return dict(mean=d*(a-b)*t,variance=d*d*(a+b)*t)

def run_means(step,forward,backward,off):
    d,a,b,c=parameters(step,forward,backward,off);total=a+b+c
    return dict(lifetime=1/c,net=d*(a-b)/c,path=d*(a+b)/c,steps=(a+b)/c,
                probabilities=(a/total,b/total,c/total))

def trace(step,signs):
    d=rational(step);signs=list(signs)
    if not Q(1,100)<=d<=100 or len(signs)>100 or any(isinstance(s,bool) or not isinstance(s,int) or s not in (-1,1) for s in signs):
        raise ValueError('Passo positivo no contrato e até100 sinais+1/−1 necessários')
    return dict(net=d*sum(signs),path=d*len(signs),steps=len(signs))

if __name__=='__main__':
    print('Em1s sem interrupção:',moments(5,4,1,1))
    print('Até desligar:',run_means(5,4,1,Q(1,2)))
    print('Trajetória fornecida:',trace(5,[1,1,-1,1]))
    assert run_means(5,4,1,Q(1,2))['net']==30
