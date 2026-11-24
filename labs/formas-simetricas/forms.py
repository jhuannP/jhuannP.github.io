"""Formas quadráticas simétricas reais 2x2; exemplos racionais exatos."""
from fractions import Fraction as Q
from dataclasses import dataclass

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):
        raise TypeError("Use int ou Fraction; bool e float não aceitos.")
    return Q(v)

def vector(v):
    if not isinstance(v,(tuple,list)) or len(v)!=2:raise ValueError("Vetor com duas componentes.")
    return tuple(map(rational,v))

@dataclass(frozen=True)
class Symmetric2:
    # Matriz [[a,b],[b,c]]: simetria é parte do tipo, não inferida por amostra.
    a:Q
    b:Q
    c:Q
    def __post_init__(self):
        for name in ('a','b','c'):object.__setattr__(self,name,rational(getattr(self,name)))
    def apply(self,v):
        x,y=vector(v)
        return self.a*x+self.b*y,self.b*x+self.c*y
    def quadratic(self,v):
        x,y=vector(v)
        return self.a*x*x+2*self.b*x*y+self.c*y*y
    @property
    def determinant(self):return self.a*self.c-self.b*self.b
    def classify(self):
        det=self.determinant
        if self.a>0 and det>0:return 'positiva definida'
        if self.a<0 and det>0:return 'negativa definida'
        if self.a==self.b==self.c==0:return 'nula'
        if self.a>=0 and self.c>=0 and det>=0:return 'positiva semidefinida'
        if self.a<=0 and self.c<=0 and det>=0:return 'negativa semidefinida'
        return 'indefinida'
    def completed_square(self,v):
        """Decomposição por a: válida só se a != 0; não é prova de positividade sozinha."""
        if self.a==0:raise ValueError("Pivô a nulo: esta decomposição não se aplica.")
        x,y=vector(v)
        return self.a*(x+self.b*y/self.a)**2+self.determinant*y*y/self.a
    def energy(self,v,force):
        v,force=vector(v),vector(force)
        return self.quadratic(v)/2-sum(x*f for x,f in zip(v,force))
    def minimizer(self,force):
        force=vector(force)
        if self.classify()!='positiva definida':
            raise ValueError("Método restrito a energia positiva definida.")
        f,g=force
        return ((self.c*f-self.b*g)/self.determinant,
                (self.a*g-self.b*f)/self.determinant)

def family(t):return Symmetric2(2,rational(t),2)

def principal_value(t,v):
    """Coordenadas não normalizadas r=x+y, s=x-y, sem aproximar raiz de 2."""
    t=rational(t);x,y=vector(v)
    return (2+t)*(x+y)**2/2+(2-t)*(x-y)**2/2

if __name__=='__main__':
    a=family(1)
    assert a.minimizer((1,0))==(Q(2,3),Q(-1,3))
    assert a.energy(a.minimizer((1,0)),(1,0))==Q(-1,3)
    for t in (1,2,3):print(t,family(t).classify())
