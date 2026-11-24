"""Duas informações em uma medida finita; resultados exatos, sem independência."""
from fractions import Fraction as Q
from .weighted import condition

def update(weights, event, first, second):
    A, B, C = set(event), set(first), set(second)
    # Estas chamadas também validam pesos e pertencimento de todos os eventos.
    initial = condition(weights, A, B)
    second_given_first = condition(weights, C, B)
    joint_given_first = condition(weights, A & C, B)
    final = condition(weights, A, B & C)
    staged = (None if second_given_first in (None, 0)
              else joint_given_first / second_given_first)
    return dict(initial=initial, second_given_first=second_given_first,
                joint_given_first=joint_given_first, staged=staged, final=final)

if __name__ == "__main__":
    result = update(dict(a=1,b=2,c=3,d=4,e=5), set("ce"), set("abcd"), set("bce"))
    assert result["initial"] == Q(3,10)
    assert result["staged"] == result["final"] == Q(3,5)
    print(result)
