"""Synthetic coverage audits; standard library only, no research data."""
from fractions import Fraction as F
from math import comb, erf, isfinite, sqrt


def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,float,F)) or not isfinite(x):
        raise ValueError('finite real required')
    return float(x)


def count(n,limit):
    if type(n) is not int or not 1<=n<=limit:
        raise ValueError('integer sample size outside educational limit')
    return n


def known_sigma(mean,sigma,n,critical=1.96):
    mean=number(mean);sigma=number(sigma);critical=number(critical);count(n,10**7)
    if sigma<=0 or critical<=0:raise ValueError('positive sigma and critical required')
    se=sigma/sqrt(n);margin=critical*se
    if not all(isfinite(t) for t in (se,margin,mean-margin,mean+margin)):
        raise ValueError('floating point range exceeded')
    return dict(se=se,margin=margin,lower=mean-margin,upper=mean+margin)


def normal_coverage(critical=1.96,standardized_bias=0,scale=1):
    """Actual standardized error is bias + scale*Z; Z standard normal."""
    critical=number(critical);bias=number(standardized_bias);scale=number(scale)
    if critical<=0 or scale<=0:raise ValueError('positive critical and scale required')
    lo=(-critical-bias)/scale;hi=(critical-bias)/scale
    return (erf(hi/sqrt(2))-erf(lo/sqrt(2)))/2


def rademacher(n,critical=F(49,25)):
    """All count masses, no simulated draws; Xi iid, P(Xi=+-1)=1/2."""
    count(n,128)
    if isinstance(critical,bool) or not isinstance(critical,(int,F)) or critical<=0:
        raise ValueError('positive exact rational critical required')
    critical=F(critical);rows=[]
    for k in range(n+1):
        total=2*k-n
        covered=F(total*total)<=critical*critical*n
        rows.append(dict(k=k,mean=F(total,n),mass=F(comb(n,k),2**n),covered=covered))
    coverage=sum((r['mass'] for r in rows if r['covered']),F(0))
    return dict(rows=rows,coverage=coverage)


def repeated_rademacher(n,critical=F(49,25)):
    """Countermodel: one Rademacher value copied n times, still claiming se=1/sqrt(n)."""
    count(n,128)
    if isinstance(critical,bool) or not isinstance(critical,(int,F)) or critical<=0:
        raise ValueError('positive exact rational critical required')
    return F(int(F(critical)**2>=n))


if __name__=='__main__':
    print('Preserved normal example:',known_sigma(10,2,100))
    print('Normal actual coverage, c=1.96:',normal_coverage())
    print('Four iid +/-1 values:',rademacher(4))
    print('One value repeated four times:',repeated_rademacher(4))
    print('Normal bias=5 claimed standard errors:',normal_coverage(standardized_bias=5))
    print('Synthetic models only; coverage is not posterior probability or evidence of personal mastery.')
