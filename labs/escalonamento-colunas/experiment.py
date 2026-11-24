"""Padronização didática por coluna, sem NaN, pesos ou dependências externas."""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class ScaleState:
    mean: tuple
    variance: tuple
    scale: tuple
    n: int

def finite(x):
    if type(x) not in (int,float) or not math.isfinite(x):raise ValueError("Real finito necessário")
    return float(x)

def rows(data,width=None):
    if not isinstance(data,(list,tuple)):raise ValueError("Matriz em lista ou tupla necessária")
    result=[]
    for row in data:
        if not isinstance(row,(list,tuple)) or not row:raise ValueError("Linha não vazia necessária")
        if width is None:width=len(row)
        if len(row)!=width:raise ValueError("Número de colunas incompatível")
        result.append(tuple(map(finite,row)))
    return result

def fit(data):
    data=rows(data)
    if not data:raise ValueError("Treino vazio")
    n=len(data);d=len(data[0])
    mean=tuple(math.fsum(row[j] for row in data)/n for j in range(d))
    variance=tuple(math.fsum((row[j]-mean[j])**2 for row in data)/n for j in range(d))
    scale=tuple(math.sqrt(v) if v>0 else 1. for v in variance)
    if not all(math.isfinite(v) for v in mean+variance+scale):raise ValueError("Estatística fora da faixa numérica")
    return ScaleState(mean,variance,scale,n)

def transform(data,state):
    if not isinstance(state,ScaleState):raise ValueError("Estado retornado por fit necessário")
    data=rows(data,len(state.mean))
    return [tuple((x-m)/s for x,m,s in zip(row,state.mean,state.scale)) for row in data]

def inverse(data,state):
    if not isinstance(state,ScaleState):raise ValueError("Estado retornado por fit necessário")
    data=rows(data,len(state.mean))
    return [tuple(z*s+m for z,m,s in zip(row,state.mean,state.scale)) for row in data]

if __name__=="__main__":
    train=[(0,100),(2,300)];test=[(4,500)]
    state=fit(train)
    print("Estado de treino:",state)
    print("Treino transformado:",transform(train,state))
    print("Teste transformado:",transform(test,state))
    print("Estado indevido com teste incluído:",fit(train+test))
