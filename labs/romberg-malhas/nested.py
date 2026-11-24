"""Rational Romberg with nested dyadic evaluations. Not an error certificate."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise TypeError("use int or Fraction")
    return Q(x)

def trapezoid_column(f,a,b,levels=5):
    a=rational(a);b=rational(b)
    if a>=b:raise ValueError("increasing interval required")
    if type(levels) is not int:raise TypeError("integer levels required")
    if not 1<=levels<=10:raise ValueError("1..10 levels in this teaching routine")
    t=(b-a)*(rational(f(a))+rational(f(b)))/2
    column=[t]
    for k in range(1,levels):
        n=2**k;h=(b-a)/n
        new=sum((rational(f(a+i*h)) for i in range(1,n,2)),Q(0))
        t=t/2+h*new
        column.append(t)
    return tuple(column)

def extrapolate(column):
    if type(column) not in (tuple,list) or not column:raise TypeError("nonempty tuple/list required")
    table=[]
    for k,t in enumerate(column):
        row=[rational(t)]
        for j in range(1,k+1):
            row.append(row[-1]+(row[-1]-table[k-1][j-1])/(4**j-1))
        table.append(tuple(row))
    return tuple(table)

def romberg(f,a,b,levels=5):return extrapolate(trapezoid_column(f,a,b,levels))

def cosine_coarse_samples(x):
    """Exact cos(16*pi*x) ONLY on dyadic grids through n=16 on [0,1].
    Partial sample oracle, NOT a continuous callable cosine implementation.
    """
    x=rational(x);phase=16*x
    if not 0<=x<=1 or phase.denominator!=1:
        raise ValueError("sample is outside the declared coarse grids")
    return Q((-1)**phase.numerator)

if __name__=='__main__':
    for name,f,exact,levels in [('x^4',lambda x:x**4,Q(1,5),4),
                                ('abs(x-1/5)',lambda x:abs(x-Q(1,5)),Q(17,50),5),
                                ('cosine coarse sample oracle',cosine_coarse_samples,Q(0),5)]:
        rows=romberg(f,0,1,levels)
        print(name,"exact integral",exact)
        for k,row in enumerate(rows):print(k,row,"diagonal error",row[-1]-exact)
