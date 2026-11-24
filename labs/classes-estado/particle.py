"""MRU didático em uma dimensão; posições em m e tempos em s."""
import math


def finite_float(value):
    if type(value) not in (int, float):
        raise ValueError('Use int ou float, sem bool ou texto')
    try:
        number = float(value)
    except (OverflowError, ValueError):
        raise ValueError('Valor fora do alcance de float') from None
    if not math.isfinite(number):
        raise ValueError('Valor deve ser finito')
    return number


class ParticulaMRU:
    def __init__(self, x, v):
        x, v = finite_float(x), finite_float(v)
        self.x = x
        self.v = v

    def avancar(self, dt):
        dt = finite_float(dt)
        if dt < 0:
            raise ValueError('Passo deve ser não negativo')
        candidate = self.x + self.v * dt
        if not math.isfinite(candidate):
            raise ValueError('Resultado não finito; estado preservado')
        self.x = candidate
        # Sem return explícito: a chamada retorna None.


if __name__ == '__main__':
    p = ParticulaMRU(1, 2)
    q = ParticulaMRU(0, -1)
    r = p
    result = p.avancar(3)
    assert p.x == r.x == 7 and q.x == 0
    assert r is p and q is not p and result is None
    print('p, r e q:', p.x, r.x, q.x)
