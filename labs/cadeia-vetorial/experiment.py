"""Composição polinomial original R²→R³→R²; coordenadas adimensionais."""
from math import hypot,isfinite

def F(u,v):return (u*u,v,u*v)
def G(x,y,z):return (x+y*z,z*z-y)
def H(u,v):return (u*u+u*v*v,u*u*v*v-v)
def matmul(A,B):
    if not A or not B or not A[0] or not B[0] or any(len(r)!=len(A[0]) for r in A) or any(len(r)!=len(B[0]) for r in B) or len(A[0])!=len(B):
        raise ValueError('Matrizes retangulares de dimensões compatíveis')
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def jacobians(u,v):
    x,y,z=F(u,v)
    A=[[2*u,0],[0,1],[v,u]]
    B=[[1,z,y],[0,-1,2*z]]
    return A,B,matmul(B,A)
def remainder(u,v,a,b):
    return (a*a+u*b*b+2*v*a*b+a*b*b,
            u*u*b*b+4*u*v*a*b+2*u*a*b*b+a*a*v*v+2*v*a*a*b+a*a*b*b)
def model(u=1,v=2,direction=2,k=4):
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not -2<=x<=2 for x in (u,v)) or type(direction) is not int or direction not in (0,1,2) or type(k) is not int or not 1<=k<=8:
        raise ValueError('Base no quadrado[-2,2]²; direção0..2; refinamento1..8')
    w=((1,0),(0,1),(1,1))[direction];eps=2.**(-k);h=(eps*w[0],eps*w[1])
    A,B,C=jacobians(u,v)
    jv=[row[0]*w[0]+row[1]*w[1] for row in C]
    linear=[eps*x for x in jv];actual=[a-b for a,b in zip(H(u+h[0],v+h[1]),H(u,v))]
    rem=remainder(u,v,*h)
    return {'u':u,'v':v,'direction':direction,'k':k,'eps':eps,'h':h,'w':w,'A':A,'B':B,'C':C,
            'jv':jv,'linear':linear,'actual':actual,'remainder':rem,
            'secant':[x/eps for x in actual],'relative_remainder':hypot(*rem)/hypot(*h),
            'bound':34*hypot(*h)}

# Exemplo escalar anterior preservado.
d=lambda t:2*t+4*t**3
if __name__=='__main__':
    assert d(1)==6
    m=model();assert m['C']==[[6,4],[8,3]] and m['jv']==[10,11]
    print(m)
