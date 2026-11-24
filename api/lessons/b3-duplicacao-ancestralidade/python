"""Classifica pares numa árvore binária com eventos fornecidos, sem inferi-los."""
from itertools import combinations


def index_tree(tree):
    events, leaves = {}, {}
    def visit(node, path=()):
        if type(node) is not tuple or len(node) != 3:
            raise ValueError('Nó deve ser tupla (tipo, nome, conteúdo).')
        kind, name, data = node
        if type(kind) is not str or kind not in ('gene','D','S'):
            raise ValueError('Tipo esperado: gene, D ou S.')
        if type(name) is not str or not name or name in events:
            raise ValueError('Nomes não vazios e únicos.')
        if len(events) >= 63:
            raise ValueError('Limite didático de 63 nós.')
        events[name] = kind
        path = path + (name,)
        if kind == 'gene':
            if type(data) is not str or not data:
                raise ValueError('Folha precisa de espécie não vazia.')
            leaves[name] = {'species': data, 'path': path}
        else:
            if type(data) is not tuple or len(data) != 2:
                raise ValueError('Evento precisa de dois descendentes.')
            for child in data: visit(child, path)
    visit(tree)
    return events, leaves


def relation(tree, a, b):
    events, leaves = index_tree(tree)
    if type(a) is not str or type(b) is not str or a == b:
        raise ValueError('Indique dois genes distintos.')
    if a not in leaves or b not in leaves:
        raise ValueError('Gene ausente da árvore.')
    common = []
    for u,v in zip(leaves[a]['path'],leaves[b]['path']):
        if u != v: break
        common.append(u)
    ancestor = common[-1]
    event = events[ancestor]
    return {'ancestor': ancestor, 'event': event,
            'relation': 'ortólogos' if event == 'S' else 'parálogos'}


# Duplicação depois da separação A/B: ortologia um-para-muitos.
AFTER = ('S','s0',(
    ('D','dA',(('gene','A1','A'),('gene','A2','A'))),
    ('gene','B1','B')))
# Duplicação antes da separação A/B: parálogos entre espécies também.
BEFORE = ('D','d0',(
    ('S','sx',(('gene','Ax','A'),('gene','Bx','B'))),
    ('S','sy',(('gene','Ay','A'),('gene','By','B')))))


if __name__ == '__main__':
    for title,tree in [('depois',AFTER),('antes',BEFORE)]:
        _, leaves = index_tree(tree)
        print('Duplicação',title,'da especiação')
        for a,b in combinations(leaves,2):print(a,b,relation(tree,a,b))
    print('Eventos fornecidos; sem alinhamento, inferência filogenética ou função medida.')
