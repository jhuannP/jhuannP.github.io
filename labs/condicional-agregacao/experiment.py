"""Comparações condicionais em uma população finita sintética, sem inferência causal."""
from fractions import Fraction as F


def compare(rows, weight=F(1, 2)):
    """Cada linha é (sucessos_A, total_A, sucessos_B, total_B); dois grupos."""
    if not isinstance(rows, (list, tuple)) or len(rows) != 2:
        raise ValueError('Forneça exatamente dois grupos')
    if isinstance(weight, bool) or not isinstance(weight, (int, F)) or not 0 <= weight <= 1:
        raise ValueError('Peso racional entre zero e um')
    for row in rows:
        if not isinstance(row, (list, tuple)) or len(row) != 4:
            raise ValueError('Quatro contagens por grupo')
        if any(isinstance(x, bool) or not isinstance(x, int) for x in row):
            raise ValueError('Contagens inteiras')
        a, na, b, nb = row
        if na <= 0 or nb <= 0 or not 0 <= a <= na or not 0 <= b <= nb:
            raise ValueError('Totais positivos e sucessos dentro dos totais')
    rates_a = tuple(F(r[0], r[1]) for r in rows)
    rates_b = tuple(F(r[2], r[3]) for r in rows)
    na = sum(r[1] for r in rows); nb = sum(r[3] for r in rows)
    pooled_a = F(sum(r[0] for r in rows), na)
    pooled_b = F(sum(r[2] for r in rows), nb)
    weights_a = tuple(F(r[1], na) for r in rows)
    weights_b = tuple(F(r[3], nb) for r in rows)
    common_a = weight*rates_a[0] + (1-weight)*rates_a[1]
    common_b = weight*rates_b[0] + (1-weight)*rates_b[1]
    reversal = all(a > b for a, b in zip(rates_a, rates_b)) and pooled_a < pooled_b
    return dict(rates_a=rates_a, rates_b=rates_b, weights_a=weights_a,
                weights_b=weights_b, pooled_a=pooled_a, pooled_b=pooled_b,
                common_a=common_a, common_b=common_b, reversal=reversal)


if __name__ == '__main__':
    result = compare(((9, 10, 72, 90), (27, 90, 2, 10)))
    assert result['pooled_a'] == F(9, 25)
    assert result['pooled_b'] == F(37, 50)
    assert result['common_a'] == F(3, 5) and result['common_b'] == F(1, 2)
    assert result['reversal']
    for name, value in result.items():
        print(name, value)
