"""Projeção em partições finitas; distribuição estipulada, não amostra."""
import math


def project(values, weights, groups):
    if not values or not (len(values) == len(weights) == len(groups)):
        raise ValueError('Vetores não vazios de mesmo tamanho')
    if any(not math.isfinite(x) for x in values + weights) or any(p < 0 for p in weights):
        raise ValueError('Valores finitos e probabilidades não negativas')
    if not math.isclose(sum(weights), 1, rel_tol=0, abs_tol=1e-12):
        raise ValueError('Probabilidades devem somar um')
    totals, masses = {}, {}
    for x, p, g in zip(values, weights, groups):
        totals[g] = totals.get(g, 0) + p*x
        masses[g] = masses.get(g, 0) + p
    means = {g: totals[g]/m for g, m in masses.items() if m > 0}
    # Grupo nulo: versão arbitrária zero, sem efeito nas esperanças.
    return [means.get(g, 0) for g in groups]


def model(info=1, noise=1, shift=0):
    if info not in (0, 1, 2) or not math.isfinite(noise) or noise < 0 or not math.isfinite(shift):
        raise ValueError('Informação 0/1/2, escala não negativa e deslocamento finito')
    ys = [-1, -1, 0, 0, 1, 1]
    zs = [-1, 1]*3
    weights = [1/8, 1/8, 1/4, 1/4, 1/8, 1/8]
    values = [y*y + noise*z for y, z in zip(ys, zs)]
    groups = [0]*6 if info == 0 else ys if info == 1 else list(range(6))
    means = project(values, weights, groups)
    predictions = [m + shift for m in means]
    residuals = [x-m for x, m in zip(values, means)]
    mean = sum(p*x for p, x in zip(weights, values))
    var_x = sum(p*(x-mean)**2 for p, x in zip(weights, values))
    optimal = sum(p*r*r for p, r in zip(weights, residuals))
    risk = sum(p*(x-g)**2 for p, x, g in zip(weights, values, predictions))
    explained = sum(p*(m-mean)**2 for p, m in zip(weights, means))
    rows = []
    for group in dict.fromkeys(groups):
        ids = [i for i, g in enumerate(groups) if g == group]
        rows.append({'group': group, 'probability': sum(weights[i] for i in ids),
                     'mean': means[ids[0]], 'prediction': predictions[ids[0]]})
    return dict(info=info, noise=noise, shift=shift, ys=ys, zs=zs, weights=weights,
                values=values, groups=groups, means=means, predictions=predictions,
                residuals=residuals, mean=mean, var_x=var_x, optimal=optimal,
                risk=risk, explained=explained, rows=rows)


if __name__ == '__main__':
    for information in range(3):
        r = model(information)
        print(information, 'm =', r['means'], 'EQM =', r['risk'])
