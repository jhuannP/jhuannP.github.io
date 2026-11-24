"""Inferência sem reposição a partir da contagem, não da ordem das cores."""
from fractions import Fraction as Q
from math import comb
from .urn import infer


def infer_count(n, weights, draws, red):
    """Mesmo protocolo de urn.infer; observação: red vermelhas em draws bolas.

    evidence é P(X=red), não a probabilidade de uma sequência específica.
    """
    # Reuse input contracts for n and prior; do not use sequential likelihoods.
    infer(n, weights)
    if type(draws) is not int or not 0 <= draws <= n:
        raise ValueError('Número de retiradas inteiro entre 0 e n')
    if type(red) is not int or not 0 <= red <= draws:
        raise ValueError('Contagem vermelha inteira entre 0 e draws')
    mass = sum(weights.values(), Q(0))
    joint = {}
    for r, w in weights.items():
        feasible = red <= r and draws-red <= n-r
        likelihood = Q(comb(r, red)*comb(n-r, draws-red), comb(n, draws)) if feasible else Q(0)
        joint[r] = w/mass * likelihood
    evidence = sum(joint.values(), Q(0))
    if not evidence:
        return dict(evidence=Q(0), posterior=None, next_red=None)
    posterior = {r:j/evidence for r,j in joint.items()}
    predictive = None if draws == n else sum((p*Q(r-red, n-draws) for r,p in posterior.items() if p), Q(0))
    return dict(evidence=evidence, posterior=posterior, next_red=predictive)
