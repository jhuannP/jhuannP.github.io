"""Filtra famílias periódicas fornecidas, em múltiplos racionais de pi."""
from fractions import Fraction as Q
from math import ceil,floor


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float.')
    return Q(x)


def solve(a,b,bases,period,lo,hi,closed_upper=False):
    # u=x/pi e argumento/pi = a*u+b; bases/period também em unidades de pi.
    a,b,period,lo,hi=map(rational,(a,b,period,lo,hi))
    if period<=0 or lo>=hi or type(closed_upper) is not bool:
        raise ValueError('Período positivo, intervalo lo<hi e extremo booleano.')
    if type(bases) not in (list,tuple) or not 1<=len(bases)<=8:
        raise ValueError('Forneça uma a oito bases canônicas.')
    roots=tuple(map(rational,bases))
    if any(not 0<=r<period for r in roots):raise ValueError('Bases em [0,period).')
    if a==0:
        matches=any(((b-r)/period).denominator==1 for r in roots)
        return {'kind':'interval','bounds':(lo,hi),'closed_upper':closed_upper} if matches else {'kind':'finite','values':[]}
    low,high=sorted((a*lo+b,a*hi+b))
    answer=set()
    for r in roots:
        start=ceil((low-r)/period);end=floor((high-r)/period)
        if end-start+1>10000:raise ValueError('Mais de 10000 candidatos por família.')
        for k in range(start,end+1):
            u=(r+k*period-b)/a
            if lo<=u<hi or (closed_upper and u==hi):answer.add(u)
    return {'kind':'finite','values':sorted(answer)}


if __name__=='__main__':
    bases=(Q(1,6),Q(5,6)) # sin(theta)=1/2; famílias deduzidas antes.
    print('sin(2x-pi/6)=1/2,0<=x<2pi:')
    print(solve(2,Q(-1,6),bases,2,0,2))
    print('Os números retornados multiplicam pi, em radianos.')
    print('cos x=1 em [0,2pi):',solve(1,0,(0,),2,0,2))
    print('cos x=1 em [0,2pi]:',solve(1,0,(0,),2,0,2,True))
    print('O código recebe famílias; não deduz identidades ou arcos inversos.')
