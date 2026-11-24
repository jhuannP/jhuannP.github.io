"""Momentos de um modelo finito ponderado; não é estimador amostral."""
from fractions import Fraction as Q

def moments(rows, weights):
    rows=tuple(tuple(row) for row in rows);weights=tuple(weights)
    if not rows or not rows[0] or len(weights)!=len(rows) or any(len(row)!=len(rows[0]) for row in rows):
        raise ValueError("Resultados retangulares não vazios e um peso por resultado")
    if any(type(x) not in (int,Q) for row in rows for x in row):raise ValueError("Valores racionais, sem bool")
    if any(type(w) not in (int,Q) or w<0 for w in weights) or sum(weights)<=0:
        raise ValueError("Pesos racionais não negativos, massa total positiva")
    p=tuple(Q(w)/sum(weights) for w in weights);d=len(rows[0])
    mu=tuple(sum((w*row[j] for row,w in zip(rows,p)),Q(0)) for j in range(d))
    C=tuple(tuple(sum((w*(row[i]-mu[i])*(row[j]-mu[j]) for row,w in zip(rows,p)),Q(0))
                  for j in range(d)) for i in range(d))
    return mu,C

if __name__ == "__main__":
    print("Dois tempos afins:",moments([(9,1),(10,3),(11,5)],[1,1,1]))
    print("Não linear:",moments([(-1,1),(0,0),(1,1)],[1,1,1]))
