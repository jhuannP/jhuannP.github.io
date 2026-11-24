"""Área orientada 2D em uma família controlada, sem diagnóstico geral de posto."""
import math


def det2(a):
    value=a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return 0 if value == 0 else value


def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def signed_polygon_area(vertices):
    return sum(vertices[i][0]*vertices[(i+1)%len(vertices)][1]-vertices[(i+1)%len(vertices)][0]*vertices[i][1] for i in range(len(vertices)))/2


def model(scale=1, shear=.5, height=1, swap=0):
    if not all(math.isfinite(x) for x in [scale,shear,height]) or not (.25<=scale<=2 and -2<=shear<=2 and -2<=height<=2) or swap not in (0,1):
        raise ValueError('Parâmetros finitos nas faixas do painel; troca 0/1')
    a=[[scale,scale*shear],[0,scale*height]]
    if swap: a=[[row[1],row[0]] for row in a]
    u=[a[0][0],a[1][0]];v=[a[0][1],a[1][1]]
    vertices=[[0,0],u,[u[0]+v[0],u[1]+v[1]],v]
    determinant=det2(a)
    return dict(scale=scale,shear=shear,height=height,swap=swap,matrix=a,u=u,v=v,
                vertices=vertices,determinant=determinant,area=abs(determinant),
                polygon_area=signed_polygon_area(vertices),
                orientation=1 if determinant>0 else -1 if determinant<0 else 0)


if __name__=='__main__':
    for height in [1,0,-1]:
        r=model(height=height)
        print(r['matrix'],'det =',r['determinant'],'área =',r['area'])
    assert det2([[2,1],[0,3]])==6
