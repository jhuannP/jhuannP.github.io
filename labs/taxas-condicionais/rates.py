"""Taxas de sucesso por estrato; contagens sintéticas, aritmética racional."""
from fractions import Fraction as Q

EXAMPLE_A = ((9, 10), (18, 30))
EXAMPLE_B = ((24, 30), (5, 10))

def audit(cells, common_weights):
    """Cada célula é (sucessos,total), total>0; pesos comuns somam 1.

    Retorna taxas condicionais, pesos observados, taxa bruta e padronizada.
    Não estima efeito causal nem incerteza de uma população.
    """
    cells = tuple(cells)
    if not cells:
        raise ValueError('informe ao menos um estrato')
    for s, n in cells:
        if type(s) is not int or type(n) is not int:
            raise TypeError('contagens devem ser inteiros, sem bool')
        if n <= 0 or not 0 <= s <= n:
            raise ValueError('exige 0 <= sucessos <= total e total > 0')
    weights = tuple(common_weights)
    if len(weights) != len(cells):
        raise ValueError('um peso por estrato')
    if any(type(w) not in (int, Q) for w in weights):
        raise TypeError('pesos devem ser int ou Fraction, sem float/bool')
    weights = tuple(Q(w) for w in weights)
    if any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError('pesos não negativos devem somar 1')
    total = sum(n for _, n in cells)
    rates = tuple(Q(s, n) for s, n in cells)
    observed = tuple(Q(n, total) for _, n in cells)
    return {'rates': rates, 'observed_weights': observed,
            'raw': sum(p*w for p, w in zip(rates, observed)),
            'standardized': sum(p*w for p, w in zip(rates, weights))}

if __name__ == '__main__':
    a, b = (audit(c, (Q(1, 2), Q(1, 2))) for c in (EXAMPLE_A, EXAMPLE_B))
    assert a['raw'] == Q(27, 40) < b['raw'] == Q(29, 40)
    assert a['standardized'] == Q(3, 4) > b['standardized'] == Q(13, 20)
    print('Brutas:', a['raw'], b['raw'])
    print('Com pesos iguais:', a['standardized'], b['standardized'])
