"""Two spins, ONE bond, exact odds a=exp(2J/T), b=exp(2h/T)."""
from fractions import Fraction as Q
STATES=((1,1),(1,-1),(-1,1),(-1,-1))


def positive(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError('Use int/Fraction without bool/float')
    x=Q(x)
    if x<=0:raise ValueError('Positive value required')
    return x


def distribution(a,b=1):
    a,b=map(positive,(a,b));weights=(a*b*b,b,b,a);z=sum(weights)
    return tuple(w/z for w in weights)


def moments(a,b=1):
    p=distribution(a,b)
    local=tuple(sum(prob*s[j] for prob,s in zip(p,STATES)) for j in range(2))
    product_mean=sum(prob*s[0]*s[1] for prob,s in zip(p,STATES))
    covariance=product_mean-local[0]*local[1]
    M=sum(local)
    variance=sum(prob*(sum(s)-M)**2 for prob,s in zip(p,STATES))
    return dict(probabilities=p,local_means=local,mean=M,product_mean=product_mean,
                covariance=covariance,local_variances=tuple(1-v*v for v in local),variance=variance)


def response(a,b,temperature):
    t=positive(temperature);r=moments(a,b)
    return dict(total=r['variance']/t,per_spin=r['variance']/(2*t),
                off_diagonal=r['covariance']/t)


if __name__=='__main__':
    for a in (Q(1,3),Q(1),Q(3)):
        print('a',a,'b1',moments(a),'T2',response(a,1,2))
