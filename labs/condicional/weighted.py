"""Medida condicional finita, com pesos racionais não negativos."""
from fractions import Fraction as Q

def condition(weights, event, given):
    if not isinstance(weights, dict) or not weights:
        raise ValueError("Forneça um mapa não vazio de pesos")
    if any(type(w) not in (int, Q) or w < 0 for w in weights.values()):
        raise ValueError("Use inteiros ou Fraction não negativos; bool não é peso")
    total = sum(weights.values(), Q(0))
    if total == 0:
        raise ValueError("Massa total deve ser positiva")
    A, B = set(event), set(given)
    if not A <= weights.keys() or not B <= weights.keys():
        raise ValueError("Eventos devem pertencer ao espaço")
    denominator = sum((weights[x] for x in B), Q(0))
    if denominator == 0:
        return None
    return sum((weights[x] for x in A & B), Q(0)) / denominator

if __name__ == "__main__":
    weights = dict(a=1, b=2, c=3, d=4)
    A, B = {"a", "c"}, {"b", "c"}
    assert condition(weights, A, B) == Q(3, 5)
    assert condition(weights, B, A) == Q(3, 4)
    print("P(A|B) =", condition(weights, A, B))
