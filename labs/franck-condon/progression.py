"""Pesos de Franck–Condon: um modo, curvaturas iguais, estado inicial v=0."""
from math import exp, isfinite, fsum


def progression(S, last=12):
    if type(S) not in (int, float) or not isfinite(S) or not 0 <= S <= 20:
        raise ValueError('Use S finito entre 0 e 20, sem bool.')
    if type(last) is not int or not 0 <= last <= 200:
        raise ValueError('Índice final inteiro entre 0 e 200.')
    weights = [exp(-S)]
    for n in range(last):
        weights.append(weights[-1] * S / (n + 1))
    return {'weights': weights, 'sum': fsum(weights),
            'omitted': 1 - fsum(weights)}


def lines(S, E00, quantum, last=12):
    for value in (E00, quantum):
        if type(value) not in (int, float) or not isfinite(value):
            raise ValueError('Energias finitas, sem bool.')
    if E00 <= 0 or quantum <= 0:
        raise ValueError('Energias positivas na mesma unidade.')
    r = progression(S, last)
    return [(n, E00 + n * quantum, w) for n, w in enumerate(r['weights'])]


if __name__ == '__main__':
    for n, energy, weight in lines(1.5, 2.0, 0.1, 4):
        print(n, f'{energy:.2f} eV', f'F={weight:.9f}')
    print('Soma até n=4:', progression(1.5, 4)['sum'])
    print('Peso omitido, sem renormalizar:', progression(1.5, 4)['omitted'])
    print('Pesos de sobreposição; não são intensidades instrumentais completas.')
