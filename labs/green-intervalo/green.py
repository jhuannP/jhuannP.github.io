"""Green 1D por integração racional; modelo de contorno, não experimento."""
from fractions import Fraction as F

def rational(x):
    if type(x) is int:return F(x)
    if isinstance(x,F):return x
    raise ValueError("use int ou Fraction")

def domain(x,L):
    x,L=map(rational,(x,L))
    if L<=0 or not 0<=x<=L:raise ValueError("L>0 e x em [0,L]")
    return x,L

def green(x,s,L=1):
    x,L=domain(x,L);s,_=domain(s,L)
    return min(x,s)*(L-max(x,s))/L

def primitive(coeffs,a,b,shift=0):
    return sum((c*(b**(k+shift+1)-a**(k+shift+1))/(k+shift+1) for k,c in enumerate(coeffs)),F(0))

def solution(coeffs,x,L=1):
    x,L=domain(x,L);c=tuple(map(rational,coeffs))
    if not 1<=len(c)<=9:raise ValueError("polinômio de grau até oito")
    # Coeficientes crescentes: f(s)=c0+c1*s+...
    left=primitive(c,F(0),x,1)
    right=L*primitive(c,x,L)-primitive(c,x,L,1)
    return (L-x)*left/L+x*right/L

def uniform_patch(x,a,epsilon,Q=1,L=1):
    x,L=domain(x,L);a,_=domain(a,L);epsilon,Q=map(rational,(epsilon,Q))
    if epsilon<=0 or not 0<a-epsilon<a+epsilon<L:raise ValueError("suporte deve estar no interior")
    lo,hi=a-epsilon,a+epsilon
    # Integra a função linear por partes em s, somente no suporte da fonte.
    split=min(max(x,lo),hi)
    integral=(L-x)*(split*split-lo*lo)/(2*L)
    integral+=x*(L*(hi-split)-(hi*hi-split*split)/2)/L
    return Q*integral/(2*epsilon)

if __name__=="__main__":
    for x in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        print("x, fonte6x, ponto, faixa:",x,solution((0,6),x),green(x,F(1,2)),uniform_patch(x,F(1,2),F(1,8)))
