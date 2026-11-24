"""E/Z em desenho plano, prioridades decididas por números atômicos distintos."""
from fractions import Fraction as F

def scalar(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)): raise TypeError('Use int ou Fraction.')
    if abs(x)>10**6: raise ValueError('Magnitude didática até um milhão.')
    return F(x)

def point(p):
    if not isinstance(p,(list,tuple)) or len(p)!=2: raise ValueError('Duas coordenadas.')
    return tuple(map(scalar,p))

def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def sub(a,b):return tuple(x-y for x,y in zip(a,b))

def side(atom,origin,axis):return cross(axis,sub(atom,origin))

def priority(z0,z1):
    for z in (z0,z1):
        if isinstance(z,bool) or not isinstance(z,int):raise TypeError('Número atômico inteiro.')
        if not 1<=z<=118:raise ValueError('Número atômico de 1 a 118.')
    if z0==z1:raise ValueError('Empate: este recorte não resolve CIP recursivo ou isótopos.')
    return 0 if z0>z1 else 1

def classify(a,b,left,right):
    """left/right: dois pares (Z, posição do substituinte) por carbono."""
    a,b=point(a),point(b);v=sub(b,a)
    if v==(0,0):raise ValueError('Eixo de dupla ligação não nulo.')
    signs=[];high=[]
    for origin,pair in ((a,left),(b,right)):
        if not isinstance(pair,(list,tuple)) or len(pair)!=2:raise ValueError('Dois substituintes por carbono.')
        if any(not isinstance(x,(list,tuple)) or len(x)!=2 for x in pair):raise ValueError('Pares (Z, posição).')
        index=priority(pair[0][0],pair[1][0])
        points=tuple(point(x[1]) for x in pair)
        areas=tuple(side(x,origin,v) for x in points)
        if areas[0]*areas[1]>=0:raise ValueError('Desenhe os dois substituintes em lados opostos e fora do eixo.')
        high.append(index);signs.append(areas[index])
    return {'configuration':'Z' if signs[0]*signs[1]>0 else 'E',
            'higher_indices':tuple(high),'signed_areas':tuple(signs)}

A=(0,0);B=(2,0)
LEFT=((17,(-1,1)),(9,(-1,-1)))
RIGHT_E=((35,(3,1)),(53,(3,-1)))
RIGHT_Z=((53,(3,1)),(35,(3,-1)))

if __name__=='__main__':
    print('Cl/F à esquerda, Br/I à direita:',classify(A,B,LEFT,RIGHT_E))
    print('Trocando Br e I:',classify(A,B,LEFT,RIGHT_Z))
    assert classify(A,B,LEFT,RIGHT_E)['configuration']=='E'
    assert classify(A,B,LEFT,RIGHT_Z)['configuration']=='Z'
    print('Coordenadas são desenho; não são estrutura molecular otimizada ou energia.')
