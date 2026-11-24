"""-u''=f em [0,1], malha uniforme; solução racional para estudo."""
from fractions import Fraction as F

def rational(x):
    if type(x) is int:return F(x)
    if isinstance(x,F):return x
    raise ValueError("use int ou Fraction")

def solve(rhs,left=0,right=0):
    # rhs contém h² f_i, antes de somar os valores das bordas.
    b=list(map(rational,rhs));left,right=map(rational,(left,right));m=len(b)
    if not 1<=m<=255:raise ValueError("de1 a255 pontos interiores")
    b[0]+=left;b[-1]+=right
    diag=[F(2)]*m
    for i in range(1,m):
        diag[i]-=1/diag[i-1]
        b[i]+=b[i-1]/diag[i-1]
    y=[F(0)]*m;y[-1]=b[-1]/diag[-1]
    for i in range(m-2,-1,-1):y[i]=(b[i]+y[i+1])/diag[i]
    return [left]+y+[right]

def residual(values,source):
    u=list(map(rational,values));f=list(map(rational,source));n=len(u)-1
    if n<2 or len(f)!=n-1:raise ValueError("valores de bordas e fonte interior compatíveis")
    return [f[i-1]-n*n*(2*u[i]-u[i-1]-u[i+1]) for i in range(1,n)]

def quartic(n):
    if type(n) is not int or not 2<=n<=256:raise ValueError("n inteiro2..256")
    xs=[F(i,n) for i in range(n+1)]
    f=[-2+12*x-12*x*x for x in xs[1:-1]]
    U=solve([v/(n*n) for v in f]);ref=[x*x*(1-x)**2 for x in xs]
    return xs,f,U,ref

if __name__=="__main__":
    for n in (4,8,16):
        x,f,U,ref=quartic(n);err=max(abs(a-b) for a,b in zip(U,ref))
        print("n=",n,"erro nodal=",err,"resíduo algébrico=",max(map(abs,residual(U,f))))
