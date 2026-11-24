"""Mapa regional didático; setas não são migração celular, circuito ou tempo."""
PARENT = {
    'prosencefalo': 'tubo_rostral', 'mesencefalo_primario': 'tubo_rostral',
    'rombencefalo': 'tubo_rostral',
    'telencefalo': 'prosencefalo', 'diencefalo': 'prosencefalo',
    'mesencefalo': 'mesencefalo_primario',
    'metencefalo': 'rombencefalo', 'mielencefalo': 'rombencefalo',
    'cortex': 'telencefalo', 'bulbo_olfatorio': 'telencefalo',
    'talamo': 'diencefalo', 'hipotalamo': 'diencefalo',
    'teto': 'mesencefalo', 'tegmento': 'mesencefalo',
    'ponte': 'metencefalo', 'cerebelo': 'metencefalo', 'bulbo': 'mielencefalo',
}
CAVITY = {'telencefalo': 'ventriculos_laterais', 'diencefalo': 'terceiro_ventriculo',
          'mesencefalo': 'aqueduto', 'metencefalo': 'quarto_ventriculo',
          'mielencefalo': 'quarto_ventriculo'}
PRIMARY = ('prosencefalo', 'mesencefalo_primario', 'rombencefalo')
SECONDARY = tuple(CAVITY)
NODES = frozenset(PARENT) | {'tubo_rostral'}


def ancestry(node):
    if type(node) is not str or node not in NODES:
        raise ValueError('Use uma região do mapa, não uma cavidade.')
    path = [node]
    while path[-1] in PARENT:
        parent = PARENT[path[-1]]
        if parent in path:
            raise ValueError('Ciclo inválido no mapa regional.')
        path.append(parent)
    return tuple(reversed(path))


def descendants(node):
    ancestry(node)
    return frozenset(n for n in NODES if node in ancestry(n))


def cavities_below(node):
    # União de rótulos de espaços; não soma de caminhos ou volume.
    return frozenset(CAVITY[n] for n in descendants(node) if n in CAVITY)


if __name__ == '__main__':
    for node in ['cortex', 'cerebelo', 'bulbo_olfatorio', 'bulbo']:
        print(node, '←', ' / '.join(ancestry(node)))
    for node in PRIMARY:
        print('espaços associados a', node, sorted(cavities_below(node)))
