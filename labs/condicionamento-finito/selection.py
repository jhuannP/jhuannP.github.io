"""Seleção determinística em quatro átomos binários; massas exatas, exemplo sintético."""
from fractions import Fraction as F

def selected_table(weights, selected):
    """Ordem (0,0), (0,1), (1,0), (1,1). None indica condição nula."""
    if not isinstance(weights, (list, tuple)) or len(weights) != 4:
        raise ValueError('Quatro pesos inteiros não negativos')
    if any(isinstance(w, bool) or not isinstance(w, int) or w < 0 for w in weights):
        raise ValueError('Quatro pesos inteiros não negativos')
    if not isinstance(selected, (list, tuple)) or len(selected) != 4 or any(type(s) is not bool for s in selected):
        raise ValueError('Quatro indicadores booleanos de seleção')
    if sum(weights) == 0:
        raise ValueError('O modelo original precisa de massa positiva')
    kept = [w if s else 0 for w, s in zip(weights, selected)]
    mass = sum(kept)
    if mass == 0:
        return None
    p_a = F(kept[2] + kept[3], mass)
    p_b = F(kept[1] + kept[3], mass)
    joint = F(kept[3], mass)
    return dict(selection=F(mass, sum(weights)), a=p_a, b=p_b, joint=joint,
                independent=joint == p_a * p_b,
                a_given_b=None if p_b == 0 else joint / p_b,
                cells=tuple(F(w, mass) for w in kept))

if __name__ == '__main__':
    weights = (1, 1, 1, 1)
    original = selected_table(weights, (True, True, True, True))
    filtered = selected_table(weights, (False, True, True, True))
    assert original['independent'] and not filtered['independent']
    assert filtered['joint'] == F(1, 3)
    assert filtered['a'] * filtered['b'] == F(4, 9)
    assert filtered['a_given_b'] == F(1, 2)
    print('Original:', original)
    print('Pelo menos um 1:', filtered)
