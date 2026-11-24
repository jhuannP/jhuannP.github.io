"""Zeros de polinômios: coeficientes crescentes e diagnósticos explícitos.
Não é um solver geral de todas as raízes. Modelo adimensional.
"""
import math

def checked(coeff):
    c=list(coeff)
    if not c or any(isinstance(x,bool) or not math.isfinite(float(x)) for x in c):
        raise ValueError('Coeficientes reais finitos e lista não vazia')
    if len(c)>1 and c[-1]==0: raise ValueError('Declare o grau sem zeros finais')
    return c

def value_derivative(coeff,x):
    c=checked(coeff)
    if not math.isfinite(float(x)): raise ValueError('x finito')
    p=c[-1];dp=0
    for a in reversed(c[:-1]):dp=dp*x+p;p=p*x+a
    return p,dp

def divide_linear(coeff,r):
    c=checked(coeff)
    if len(c)<2 or not math.isfinite(float(r)):raise ValueError('Grau >=1 e divisor finito')
    q=[0]*(len(c)-1);q[-1]=c[-1]
    for j in range(len(q)-2,-1,-1):q[j]=c[j+1]+r*q[j+1]
    return q,c[0]+r*q[0]

def cauchy_bound(coeff):
    c=checked(coeff)
    if len(c)<2:raise ValueError('Grau >=1')
    return 1+max(abs(a/c[-1]) for a in c[:-1])

def family(m):
    if m not in (1,2):raise ValueError('m=1 ou m=2')
    return [-2,1,1] if m==1 else [2,-3,0,1]

def newton(coeff,x0,steps=3,multiplier=1):
    c=checked(coeff)
    if not math.isfinite(float(x0)) or not isinstance(steps,int) or isinstance(steps,bool) or not 0<=steps<=8:
        raise ValueError('x inicial finito e 0 a 8 passos')
    if multiplier not in (1,2):raise ValueError('Multiplicador 1 ou 2 neste roteiro')
    x=float(x0);trace=[]
    for k in range(steps+1):
        p,dp=value_derivative(c,x)
        if not math.isfinite(p) or not math.isfinite(dp):return {'trace':trace,'status':'nonfinite'}
        trace.append({'x':x,'p':p,'dp':dp})
        if p==0:return {'trace':trace,'status':'computedZero'}
        if k==steps:return {'trace':trace,'status':'limit'}
        if dp==0:return {'trace':trace,'status':'derivativeZero'}
        y=x-multiplier*p/dp
        if not math.isfinite(y):return {'trace':trace,'status':'nonfinite'}
        if y==x:return {'trace':trace,'status':'stagnation'}
        x=y

if __name__=='__main__':
    for m in (1,2):
        for factor in (1,m):print(m,factor,newton(family(m),2,3,factor))
