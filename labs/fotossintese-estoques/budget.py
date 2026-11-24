"""Inventário molar idealizado de trioses, sem cinética ou rendimento luminoso."""
from fractions import Fraction as F

def amount(value):
    if isinstance(value, bool) or not isinstance(value, (int, F)):
        raise TypeError("Use inteiros ou Fraction em mol; não use float.")
    value = F(value)
    if value < 0 or value > 10**6:
        raise ValueError("Estoque didático entre zero e um milhão de mol.")
    return value

def budget(co2, nadph, atp):
    """Teto contínuo em mol de equivalentes G3P; RuBP regenerada e sem perdas."""
    stocks = tuple(amount(x) for x in (co2, nadph, atp))
    costs = (F(3), F(6), F(9))
    capacities = tuple(s/c for s, c in zip(stocks, costs))
    output = min(capacities)
    used = tuple(c*output for c in costs)
    left = tuple(s-u for s, u in zip(stocks, used))
    labels = ('CO2', 'NADPH', 'ATP')
    return {'triose_mol': output, 'used_mol': used, 'left_mol': left,
            'limiting': tuple(k for k, cap in zip(labels, capacities) if cap == output),
            'fixed_carbon_mol': 3*output}

if __name__ == '__main__':
    result = budget(9, 18, 18)
    print(result)
    assert result['triose_mol'] == 2
    assert result['left_mol'] == (3, 6, 0)
