"""Momentos exatos de passeio absorvente; não amostra Browniano."""
from fractions import Fraction as Q

def positive(x):
    if type(x) not in (int,Q) or x<=0:raise ValueError('Inteiro ou Fraction positivo')
    return Q(x)

def solve(rhs):
    # Thomas: diagonal2,sub/superdiagonais−1,Dirichlet zero.
    diagonal=[];r=[]
    for i,b in enumerate(rhs):
        factor=Q(0) if i==0 else -1/diagonal[i-1]
        diagonal.append(2+factor);r.append(b if i==0 else b-factor*r[i-1])
    out=[Q(0)]*len(r)
    for i in range(len(r)-1,-1,-1):out[i]=(r[i]+(out[i+1] if i+1<len(r) else 0))/diagonal[i]
    return out

def moments(length,D,intervals):
    length=positive(length);D=positive(D)
    if type(intervals) is not int or not 2<=intervals<=40:raise ValueError('De 2 a 40 intervalos')
    h=length/intervals;dt=h*h/(2*D)
    interior=solve([2*dt]*(intervals-1));mean=[Q(0)]+interior+[Q(0)]
    second=[Q(0)]+solve([4*dt*t-2*dt*dt for t in interior])+[Q(0)]
    prob_rhs=[Q(0)]*(intervals-1);prob_rhs[-1]=Q(1)
    probability=[Q(0)]+solve(prob_rhs)+[Q(1)]
    return dict(dt=dt,mean=mean,second=second,variance=[s-t*t for s,t in zip(second,mean)],right=probability)

def continuous(x,length,D):
    length=positive(length);D=positive(D)
    if type(x) not in (int,Q) or not 0<=x<=length:raise ValueError('Posição racional no intervalo')
    x=Q(x);mean=x*(length-x)/(2*D)
    second=(x**4-2*length*x**3+length**3*x)/(12*D*D)
    return dict(mean=mean,second=second,variance=second-mean*mean,right=x/length)

if __name__=='__main__':
    print('Contínuo:',continuous(1,2,Q(1,2)))
    for m in (2,4,8):
        s=moments(2,Q(1,2),m);print(m,'média',s['mean'][m//2],'variância',s['variance'][m//2])
