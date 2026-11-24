"""Rede combinacional ideal; níveis lógicos não são tempos físicos."""
from itertools import product

ARITY = {'NOT': 1, 'AND': 2, 'OR': 2, 'XOR': 2}


def evaluate(inputs, gates, outputs):
    """Portas: nome -> (operação, tupla de dependências); nomes são únicos."""
    if type(inputs) is not dict or type(gates) is not dict:
        raise ValueError('Entradas e portas devem ser dicionários.')
    names = list(inputs) + list(gates)
    if any(type(n) is not str or not n for n in names):
        raise ValueError('Nomes devem ser strings não vazias.')
    if len(set(names)) != len(names) or len(names) > 64:
        raise ValueError('Nomes distintos e no máximo 64 nós.')
    if any(type(v) is not int or v not in (0, 1) for v in inputs.values()):
        raise ValueError('Bits devem ser inteiros 0 ou 1, sem bool.')
    if type(outputs) is not tuple or not outputs:
        raise ValueError('Indique uma tupla não vazia de saídas.')
    if any(type(n) is not str or n not in names for n in outputs):
        raise ValueError('Saída inexistente.')
    for spec in gates.values():
        if type(spec) is not tuple or len(spec) != 2:
            raise ValueError('Porta deve ter operação e dependências.')
        op, args = spec
        if type(op) is not str or op not in ARITY:
            raise ValueError('Operação desconhecida.')
        if type(args) is not tuple or len(args) != ARITY[op]:
            raise ValueError('Aridade inválida.')
        if any(type(n) is not str or n not in names for n in args):
            raise ValueError('Dependência inexistente.')
    values = dict(inputs)
    depth = {n: 0 for n in inputs}
    pending = dict(gates)
    layers = []
    while pending:
        ready = [n for n, (_, args) in pending.items()
                 if all(a in values for a in args)]
        if not ready:
            raise ValueError('Ciclo: não há porta pronta; rede rejeitada.')
        layers.append(tuple(ready))
        for n in ready:
            op, args = pending.pop(n)
            x = [values[a] for a in args]
            if op == 'NOT': value = 1 - x[0]
            elif op == 'AND': value = x[0] & x[1]
            elif op == 'OR': value = x[0] | x[1]
            else: value = x[0] ^ x[1]
            values[n] = value
            depth[n] = 1 + max(depth[a] for a in args)
    return {'outputs': {n: values[n] for n in outputs},
            'values': values, 'depth': depth, 'layers': layers,
            'gate_count': len(gates),
            'output_depth': max(depth[n] for n in outputs)}


# Ordem declarada invertida de propósito: nome não é ordem de execução.
XOR_NETWORK = {'z': ('AND', ('u', 'w')),
               'w': ('NOT', ('v',)),
               'v': ('AND', ('A', 'B')),
               'u': ('OR', ('A', 'B'))}


if __name__ == '__main__':
    for a, b in product((0, 1), repeat=2):
        r = evaluate({'A': a, 'B': b}, XOR_NETWORK, ('z',))
        print(a, b, {n: r['values'][n] for n in ('u','v','w','z')})
    print('Portas:', r['gate_count'], 'profundidade de z:', r['output_depth'])
    print('Camadas:', r['layers'], '; não são ciclos de clock nem nanossegundos.')
