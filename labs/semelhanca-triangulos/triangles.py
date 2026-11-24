"""Geometria racional exata de triângulos rotulados; sem reconhecimento de imagem."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError('int ou Fraction requerido')
    return Q(x)

def point(p):
    if not isinstance(p,(tuple,list)) or len(p)!=2:raise ValueError('ponto plano com duas coordenadas')
    return tuple(rational(x) for x in p)

def cross(u,v):return u[0]*v[1]-u[1]*v[0]
def sub(u,v):return tuple(x-y for x,y in zip(u,v))
def area(tri):
    A,B,C=triangle(tri)
    return abs(cross(sub(B,A),sub(C,A)))/2

def triangle(tri):
    if not isinstance(tri,(tuple,list)) or len(tri)!=3:raise ValueError('três pontos requeridos')
    A,B,C=map(point,tri)
    if cross(sub(B,A),sub(C,A))==0:raise ValueError('triângulo não degenerado requerido')
    return A,B,C

def sides2(tri):
    A,B,C=triangle(tri)
    return tuple(sum(x*x for x in sub(V,U)) for U,V in [(A,B),(A,C),(B,C)])

def similarity_ratio2(first,second):
    """Correspondência A↔A′,B↔B′,C↔C′ dada pela ordem; retorna k² ou None."""
    x,y=sides2(first),sides2(second)
    ratios=tuple(b/a for a,b in zip(x,y))
    return ratios[0] if len(set(ratios))==1 else None

def parallel_cut(tri,k):
    A,B,C=triangle(tri);k=rational(k)
    if not 0<k<1:raise ValueError('recorte interno 0<k<1')
    def cut(V):return tuple(a+k*(v-a) for a,v in zip(A,V))
    return A,cut(B),cut(C)

def transform(tri,k,quarter_turns=0,reflected=False,offset=(0,0)):
    k=rational(k);off=point(offset)
    if k<=0:raise ValueError('escala positiva requerida')
    if type(quarter_turns) is not int or quarter_turns not in range(4):raise ValueError('quartos de volta0..3')
    if type(reflected) is not bool:raise TypeError('reflected booleano')
    out=[]
    for x,y in triangle(tri):
        if reflected:x=-x
        for _ in range(quarter_turns):x,y=-y,x
        out.append((off[0]+k*x,off[1]+k*y))
    return tuple(out)

def shadow_height(reference_height,reference_shadow,target_shadow):
    h,s,S=map(rational,(reference_height,reference_shadow,target_shadow))
    if min(h,s,S)<=0:raise ValueError('comprimentos positivos na mesma unidade')
    return h*S/s
