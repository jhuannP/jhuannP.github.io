"""Naive Bayes Bernoulli finito; duas classes e frações exatas."""
from dataclasses import dataclass
from fractions import Fraction as Q

def bit(x):
    if type(x) is not int or x not in (0,1):
        raise ValueError("Use bits inteiros 0/1, sem bool")

@dataclass(frozen=True)
class Model:
    priors: tuple
    theta: tuple

def fit(rows, labels, alpha=Q(1)):
    if type(alpha) not in (int,Q) or alpha < 0:
        raise ValueError("alpha deve ser int/Fraction não negativo")
    if not isinstance(rows,(list,tuple)) or not rows or not isinstance(labels,(list,tuple)):
        raise ValueError("Forneça linhas e classes")
    if len(rows)!=len(labels):raise ValueError("Uma classe por linha")
    if any(not isinstance(r,(list,tuple)) or not r for r in rows):
        raise ValueError("Linhas não vazias")
    width=len(rows[0])
    if any(len(r)!=width for r in rows):raise ValueError("Matriz retangular")
    for r in rows:
        for x in r:bit(x)
    for y in labels:bit(y)
    counts=tuple(labels.count(c) for c in (0,1))
    if 0 in counts:raise ValueError("Ambas as classes devem aparecer no treino")
    theta=tuple(tuple(
        (sum(r[j] for r,y in zip(rows,labels) if y==c)+Q(alpha))/(counts[c]+2*Q(alpha))
        for j in range(width)) for c in (0,1))
    return Model(tuple(Q(n,len(rows)) for n in counts),theta)

def posterior(model, query):
    """Ordem classe 0, classe 1; None para evidência de massa nula."""
    if not isinstance(model,Model):raise ValueError("Use o modelo devolvido por fit")
    if not isinstance(query,(list,tuple)) or len(query)!=len(model.theta[0]):
        raise ValueError("Consulta deve ter a largura do treino")
    for x in query:bit(x)
    scores=[]
    for c in (0,1):
        score=model.priors[c]
        for x,p in zip(query,model.theta[c]):score*=p if x else 1-p
        scores.append(score)
    total=sum(scores)
    return None if total==0 else tuple(s/total for s in scores)

if __name__=="__main__":
    rows=[(1,1)]*4+[(0,0)]+[(1,1)]+[(0,0)]*4
    labels=[0]*5+[1]*5
    assert posterior(fit(rows,labels,0),(1,1))==(Q(16,17),Q(1,17))
    assert posterior(fit(rows,labels,1),(1,1))==(Q(25,29),Q(4,29))
    print("Sem suavizar:",posterior(fit(rows,labels,0),(1,1)))
    print("alpha=1:",posterior(fit(rows,labels,1),(1,1)))
