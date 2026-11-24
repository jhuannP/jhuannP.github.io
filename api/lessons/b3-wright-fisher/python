"""Wright–Fisher neutro: distribuição finita, não amostragem de trajetórias."""
from math import comb, fsum
from functools import lru_cache


def integer(value, lo, hi):
    if isinstance(value, bool) or not isinstance(value, int) or not lo <= value <= hi:
        raise ValueError(f'Use inteiro entre {lo} e {hi}.')
    return value


@lru_cache(maxsize=20)
def kernel(individuals):
    N = integer(individuals, 1, 20)
    M = 2*N
    rows = []
    for i in range(M+1):
        if i in (0, M):
            rows.append(tuple(float(j == i) for j in range(M+1)))
        else:
            p = i/M
            rows.append(tuple(comb(M, j)*p**j*(1-p)**(M-j) for j in range(M+1)))
    return tuple(rows)


def distribution(individuals=10, initial_count=10, generations=10):
    N = integer(individuals, 1, 20)
    M = 2*N
    k = integer(initial_count, 0, M)
    t = integer(generations, 0, 100)
    matrix = kernel(N)
    q = [float(i == k) for i in range(M+1)]
    for _ in range(t):
        q = [fsum(q[i]*matrix[i][j] for i in range(M+1)) for j in range(M+1)]
    p0 = k/M
    mean = fsum(q[i]*i/M for i in range(M+1))
    variance = fsum(q[i]*(i/M-mean)**2 for i in range(M+1))
    heterozygosity = fsum(q[i]*2*(i/M)*(1-i/M) for i in range(M+1))
    decay = (1-1/M)**t
    return dict(distribution=q, mean=mean, variance=variance,
                heterozygosity=heterozygosity, mass=fsum(q), loss=q[0],
                fixation=q[M], coexistence=fsum(q[1:M]),
                analytic_variance=p0*(1-p0)*(1-decay),
                analytic_heterozygosity=2*p0*(1-p0)*decay)


if __name__ == '__main__':
    for t in (0, 1, 2):
        print('N=1, k0=1, geração', t, distribution(1, 1, t))
    q = distribution(10, 10, 10)
    print('N=10, 10 cópias A iniciais, t=10: média/variância', q['mean'], q['variance'])
    print('Hipóteses: 2N cópias, neutralidade, sem mutação/migração; dados sintéticos.')
    print('Estados absorventes no horizonte finito não são probabilidades finais de fixação.')
