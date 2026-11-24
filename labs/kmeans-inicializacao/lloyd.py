"""Lloyd 1D racional didático: até 30 pontos, centros explícitos, sem tolerância."""
from fractions import Fraction as F

def values(seq):
    seq = list(seq)
    if not 1 <= len(seq) <= 30 or any(isinstance(v, bool) or not isinstance(v, (int, F)) for v in seq):
        raise ValueError("Use de 1 a 30 inteiros ou Fraction")
    return tuple(F(v) for v in seq)

def assign(x, centers):
    return tuple(min(range(len(centers)), key=lambda j: (xv-centers[j])**2) for xv in x)

def cost(x, labels, centers):
    return sum(((v-centers[j])**2 for v,j in zip(x, labels)), F(0))

def lloyd(points, initial, max_iter=100):
    x, centers = values(points), values(initial)
    if isinstance(max_iter, bool) or not isinstance(max_iter, int) or not 1 <= max_iter <= 1000:
        raise ValueError("Orçamento inteiro de 1 a 1000")
    trace = []
    for _ in range(max_iter):
        labels = assign(x, centers)
        before = cost(x, labels, centers)
        updated = tuple(sum((v for v,k in zip(x,labels) if k==j), F(0))/labels.count(j)
                        if j in labels else c for j,c in enumerate(centers))
        after_mean = cost(x, labels, updated)
        next_labels = assign(x, updated)
        after_assign = cost(x, next_labels, updated)
        trace.append(dict(centers=centers, labels=labels, updated=updated,
                          before=before, after_mean=after_mean, after_assign=after_assign))
        if updated == centers:
            return dict(centers=updated, labels=next_labels, inertia=after_assign, trace=trace)
        centers = updated
    raise RuntimeError("Orçamento atingido; não foi certificado um ponto fixo")

if __name__ == '__main__':
    for initial in [(0,3),(0,10)]:
        r = lloyd([0,2,3,5,10], initial)
        print(initial, r['centers'], r['inertia'])
