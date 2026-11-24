"""Uma retirada sem reposição observada por sensor binário, com taxas conhecidas."""
from fractions import Fraction as Q
from .urn import infer


def infer_report(n, weights, sensitivity, false_positive, report=1):
    """report: 1=informa vermelho, 0=informa azul; cor real permanece latente.

    O sensor depende apenas da cor retirada, não da hipótese nem da próxima bola.
    Taxas são parâmetros do modelo, não estimativas feitas pelo programa.
    """
    infer(n, weights)  # contratos de população e pesos
    if any(type(v) not in (int, Q) or not 0 <= v <= 1 for v in (sensitivity, false_positive)):
        raise ValueError('Taxas devem ser int/Fraction em [0,1]')
    if type(report) is not int or report not in (0, 1):
        raise ValueError('Relato deve ser inteiro 0 ou 1')
    total = sum(weights.values(), Q(0))
    joints = {}
    for k, weight in weights.items():
        for actual in (0, 1):
            color_mass = Q(k if actual else n-k, n)
            rate = Q(sensitivity if actual else false_positive)
            likelihood = rate if report else 1-rate
            joints[k, actual] = Q(weight)/total * color_mass * likelihood
    evidence = sum(joints.values(), Q(0))
    if not evidence:
        return dict(evidence=Q(0), joint_posterior=None, posterior=None, removed_red=None, next_red=None)
    joint = {state: mass/evidence for state, mass in joints.items()}
    posterior = {k: sum((p for (r, c), p in joint.items() if r == k), Q(0)) for k in weights}
    removed_red = sum((p*c for (k, c), p in joint.items()), Q(0))
    next_red = None if n == 1 else sum((p*Q(k-c, n-1) for (k, c), p in joint.items() if p), Q(0))
    return dict(evidence=evidence, joint_posterior=joint, posterior=posterior, removed_red=removed_red, next_red=next_red)


if __name__ == '__main__':
    result = infer_report(3, {1:1, 2:1}, Q(4,5), Q(1,5))
    assert result['posterior'][2] == Q(3,5)
    assert result['removed_red'] == Q(4,5)
    assert result['next_red'] == Q(2,5)
    print(result)
