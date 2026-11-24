"""Auditoria de átomos e carga; não prevê reações, produtos ou equilíbrio."""
from fractions import Fraction as Q

# Cadastro explícito, não um interpretador geral de fórmulas químicas.
SPECIES = {
    'MnO4-': {'Mn':1, 'O':4, 'charge':-1},
    'Mn2+': {'Mn':1, 'charge':2},
    'Fe2+': {'Fe':1, 'charge':2},
    'Fe3+': {'Fe':1, 'charge':3},
    'H+': {'H':1, 'charge':1},
    'H2O': {'H':2, 'O':1, 'charge':0},
    'OH-': {'O':1, 'H':1, 'charge':-1},
    'O2': {'O':2, 'charge':0},
    'e-': {'charge':-1},
}
FIELDS = ('Mn', 'Fe', 'O', 'H', 'charge')


def coefficient(value):
    if type(value) not in (int, Q) or value < 0:
        raise ValueError('Coeficiente não negativo em int ou Fraction.')
    return Q(value)


def total(side):
    if not isinstance(side, dict) or not side:
        raise ValueError('Forneça um dicionário de espécies e coeficientes.')
    result = dict.fromkeys(FIELDS, Q(0))
    positive = False
    for name, value in side.items():
        if name not in SPECIES:
            raise ValueError('Espécie não cadastrada: '+str(name))
        value = coefficient(value)
        positive = positive or value > 0
        for field in FIELDS:
            result[field] += value*SPECIES[name].get(field, 0)
    if not positive:
        raise ValueError('Um lado inteiramente nulo não representa a reação proposta.')
    return result


def residuals(left, right):
    """Produtos menos reagentes, por campo. Charge em múltiplos de |e|."""
    a, b = total(left), total(right)
    return {field:b[field]-a[field] for field in FIELDS}


def balanced(left, right):
    return all(value == 0 for value in residuals(left, right).values())


ACID_LEFT = {'MnO4-':1, 'Fe2+':5, 'H+':8}
ACID_RIGHT = {'Mn2+':1, 'Fe3+':5, 'H2O':4}


if __name__ == '__main__':
    print('Balanço iônico em meio ácido, produtos especificados:')
    print('Reagentes:',total(ACID_LEFT))
    print('Produtos:',total(ACID_RIGHT))
    print('Resíduos:',residuals(ACID_LEFT,ACID_RIGHT))
    wrong_left={'MnO4-':1,'Fe2+':4,'H+':8}
    wrong_right={'Mn2+':1,'Fe3+':4,'H2O':4}
    print('Com quatro Fe de cada lado, resíduos:',residuals(wrong_left,wrong_right))
    print('Conservar átomos e carga não prevê conversão, mecanismo ou velocidade.')
