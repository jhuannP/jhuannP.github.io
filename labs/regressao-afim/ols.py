"""Mínimos quadrados afins de uma variável, racionais exatos e intercepto livre."""
from fractions import Fraction as Q
from dataclasses import dataclass

def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError('Use int/Fraction, sem bool/float')
    return Q(x)

def points(values):
    if not isinstance(values,(list,tuple)) or not values:raise ValueError('Pontos não vazios')
    if any(not isinstance(v,(list,tuple)) or len(v)!=2 for v in values):raise ValueError('Pares (x,y)')
    return tuple((number(x),number(y)) for x,y in values)

@dataclass(frozen=True)
class Line:
    slope: Q
    intercept: Q
    def predict(self,x):return self.slope*number(x)+self.intercept

def fit(values):
    values=points(values);n=len(values)
    mx=sum((x for x,y in values),Q(0))/n;my=sum((y for x,y in values),Q(0))/n
    sxx=sum(((x-mx)**2 for x,y in values),Q(0))
    if sxx==0:raise ValueError('Inclinação não identificável: x constante')
    sxy=sum(((x-mx)*(y-my) for x,y in values),Q(0))
    w=sxy/sxx
    return Line(w,my-w*mx)

def mse(line,values):
    values=points(values)
    return sum(((line.predict(x)-y)**2 for x,y in values),Q(0))/len(values)
