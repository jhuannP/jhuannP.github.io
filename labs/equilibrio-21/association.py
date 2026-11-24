"""2A <-> B ideal hipotético. Quantidades e v=V*c° em mol; K adimensional."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise ValueError('Use inteiro ou Fraction, sem bool/float.')
    return Q(x)


def bracket(a0, b0, v, K, steps=40):
    a0, b0, v, K = map(rational, (a0, b0, v, K))
    if min(a0, b0) < 0 or a0 + 2*b0 <= 0 or min(v, K) <= 0:
        raise ValueError('Estoque não negativo, total positivo, v e K positivos.')
    if isinstance(steps, bool) or not isinstance(steps, int) or not 0 <= steps <= 200:
        raise ValueError('steps inteiro entre 0 e 200.')
    lo, hi = -b0, a0/2
    def residual(x):
        return v*(b0+x) - K*(a0-2*x)**2
    for _ in range(steps):
        mid = (lo+hi)/2
        r = residual(mid)
        if r == 0:
            lo = hi = mid
            break
        if r < 0:
            lo = mid
        else:
            hi = mid
    mid = (lo+hi)/2
    return dict(lo=lo, hi=hi, extent=mid, error_bound=(hi-lo)/2,
                A=a0-2*mid, B=b0+mid)


if __name__ == '__main__':
    for v in (1, 8):
        r=bracket(3, 0, v, 1)
        print('v=',v,'mol; intervalo de extensão=',r['lo'],r['hi'])
        print('A, B (aproximados se intervalo aberto):',r['A'],r['B'])
    print('Tempo de reação e idealidade de substâncias reais não modelados.')
