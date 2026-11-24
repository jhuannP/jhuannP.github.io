"""Bayes exato para uma composição fixa desconhecida e retiradas uniformes."""
from fractions import Fraction as Q


def infer(n, weights, observed=(), *, replacement=False):
    """Cores: 1=vermelha, 0=azul. Pesos prévios sobre número de vermelhas.

    evidence é a probabilidade da sequência ordenada. None representa
    posterior indefinida ou inexistência de próxima bola, conforme o campo.
    """
    if type(n) is not int or n < 1 or type(replacement) is not bool:
        raise ValueError('n inteiro positivo e replacement booleano')
    if not isinstance(weights, dict) or not weights:
        raise ValueError('Forneça pesos prévios não vazios')
    if any(type(r) is not int or not 0 <= r <= n for r in weights):
        raise ValueError('Cada hipótese deve ter um inteiro entre 0 e n vermelhas')
    if any(type(w) not in (int, Q) or w < 0 for w in weights.values()):
        raise ValueError('Pesos inteiros/Fraction não negativos; bool excluído')
    total = sum(weights.values(), Q(0))
    if not total:
        raise ValueError('Massa prévia positiva exigida')
    if not isinstance(observed, (tuple, list)) or any(type(c) is not int or c not in (0, 1) for c in observed):
        raise ValueError('Observações devem ser lista/tupla de inteiros 0 ou 1')
    if not replacement and len(observed) > n:
        raise ValueError('Mais retiradas do que bolas sem reposição')
    joint = {}
    for r, w in weights.items():
        likelihood = Q(1)
        remaining = [n-r, r]
        for i, color in enumerate(observed):
            available = remaining[color]
            likelihood *= Q(available, n if replacement else n-i)
            if not likelihood:
                break
            if not replacement:
                remaining[color] -= 1
        joint[r] = w / total * likelihood
    evidence = sum(joint.values(), Q(0))
    if not evidence:
        return dict(evidence=Q(0), posterior=None, next_red=None)
    posterior = {r: j/evidence for r, j in joint.items()}
    if not replacement and len(observed) == n:
        next_red = None
    else:
        red_seen = sum(observed)
        # Ignore hypotheses with zero posterior: their inventory may be incompatible.
        next_red = sum((p * Q(r if replacement else r-red_seen,
                                   n if replacement else n-len(observed))
                        for r, p in posterior.items() if p), Q(0))
    return dict(evidence=evidence, posterior=posterior, next_red=next_red)


if __name__ == '__main__':
    result = infer(3, {1: 1, 2: 1}, (1,))
    assert result == dict(evidence=Q(1,2), posterior={1: Q(1,3), 2: Q(2,3)}, next_red=Q(1,3))
    print(result)
