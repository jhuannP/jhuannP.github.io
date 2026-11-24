"""Probabilidade finita ponderada com frações exatas; sem dados externos."""
from fractions import Fraction as Q


def rational_probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)) or not 0 <= value <= 1:
        raise ValueError('Use int ou Fraction entre 0 e 1')
    return Q(value)


def distribution(weights):
    if not isinstance(weights, dict) or not weights:
        raise ValueError('Informe um dicionário não vazio de pesos')
    result = {key: rational_probability(value) for key, value in weights.items()}
    if sum(result.values()) != 1:
        raise ValueError('Os pesos devem somar exatamente 1')
    return result


def event_probability(weights, event):
    model = distribution(weights)
    event = frozenset(event)
    if not event <= model.keys():
        raise ValueError('Evento contém resultado fora do espaço amostral')
    return sum((model[x] for x in event), Q(0))


def analyze(weights, a, b):
    model = distribution(weights)
    a, b = frozenset(a), frozenset(b)
    pa, pb = event_probability(model, a), event_probability(model, b)
    joint = event_probability(model, a & b)
    return dict(a=pa, b=pb, intersection=joint,
                union=event_probability(model, a | b),
                complement_a=event_probability(model, model.keys() - a),
                a_given_b=None if pb == 0 else joint / pb,
                independent=joint == pa * pb, difference=joint - pa * pb)


def binary_table(p, q, position):
    """Mantém marginais p,q; position interpola a conjunta entre limites válidos."""
    p, q, position = map(rational_probability, (p, q, position))
    lower, upper = max(Q(0), p + q - 1), min(p, q)
    r = lower + position * (upper - lower)
    return distribution({(1, 1): r, (1, 0): p - r,
                         (0, 1): q - r, (0, 0): 1 - p - q + r})


if __name__ == '__main__':
    die = {x: Q(1, 6) for x in range(1, 7)}
    r = analyze(die, {2, 4, 6}, {4, 5, 6})
    assert r['union'] == Q(2, 3)
    assert r['intersection'] == Q(1, 3)
    assert not r['independent']
    print('Dado justo:', r)

    # Mesmo espaço, pesos diferentes: contar resultados já não basta.
    biased = {1: Q(1, 10), 2: Q(2, 10), 3: Q(7, 10)}
    assert event_probability(biased, {1, 2}) == Q(3, 10)
    print('Evento {1,2} no modelo ponderado:', event_probability(biased, {1, 2}))

    coins = {(a, b): Q(1, 4) for a in (0, 1) for b in (0, 1)}
    a = {x for x in coins if x[0] == 1}
    b = {x for x in coins if x[1] == 1}
    c = {x for x in coins if x[0] == x[1]}
    assert all(analyze(coins, x, y)['independent'] for x, y in [(a, b), (a, c), (b, c)])
    assert event_probability(coins, a & b & c) == Q(1, 4)
    assert event_probability(coins, a) * event_probability(coins, b) * event_probability(coins, c) == Q(1, 8)
    print('Independência aos pares não garante independência mútua.')

    for position in [Q(0), Q(1, 2), Q(1)]:
        weights = binary_table(Q(1, 2), Q(1, 2), position)
        result = analyze(weights, a, b)
        assert result['independent'] == (position == Q(1, 2))
        print('Tabela binária; posição', position, result)
