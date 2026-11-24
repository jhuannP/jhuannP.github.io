"""Campos afins2D: derivadas e integrais exatas no quadrado."""
from fractions import Fraction as Q

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):
        raise TypeError('use int ou Fraction')
    return Q(v)

class Affine:
    def __init__(self, matrix, offset=(0,0)):
        if len(matrix)!=2 or any(len(row)!=2 for row in matrix) or len(offset)!=2:
            raise ValueError('matriz2x2 e offset2')
        self.A=tuple(tuple(rational(v) for v in row) for row in matrix)
        self.b=tuple(rational(v) for v in offset)
    def at(self, point):
        if len(point)!=2: raise ValueError('ponto2D')
        x,y=map(rational,point)
        return tuple(row[0]*x+row[1]*y+b for row,b in zip(self.A,self.b))
    def operators(self):
        return self.A[0][0]+self.A[1][1], self.A[1][0]-self.A[0][1]
    def square(self, origin, side):
        """Retorna fluxo externo, circulação anti-horária por quatro arestas.
        Ponto médio é exato aqui porque cada restrição é afim.
        """
        if len(origin)!=2: raise ValueError('origem2D')
        x,y=map(rational,origin); L=rational(side)
        if L<=0: raise ValueError('lado positivo')
        bottom=self.at((x+L/2,y));right=self.at((x+L,y+L/2))
        top=self.at((x+L/2,y+L));left=self.at((x,y+L/2))
        flux=L*(-bottom[1]+right[0]+top[1]-left[0])
        circulation=L*(bottom[0]+right[1]-top[0]-left[1])
        return flux,circulation

def quadratic_gradient(a,b,c,point):
    """Gradiente de a*x²+b*x*y+c*y², sem termos lineares."""
    a,b,c=map(rational,(a,b,c))
    return Affine(((2*a,b),(b,2*c))).at(point)

def vortex(point):
    """(-y/r²,x/r²), domínio plano sem origem."""
    if len(point)!=2: raise ValueError('ponto2D')
    x,y=map(rational,point); r2=x*x+y*y
    if not r2: raise ValueError('origem excluída')
    return -y/r2,x/r2

if __name__=='__main__':
    f=Affine(((2,-3),(1,-1)),(1,2))
    print('F(1,2)=',f.at((1,2)),'div,curlz=',f.operators())
    print('fluxo,circulação=',f.square((0,0),2))
    print('grad phi=',quadratic_gradient(1,0,1,(1,2)))
