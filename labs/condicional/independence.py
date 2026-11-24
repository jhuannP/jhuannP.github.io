"""Independência dentro de um evento com massa positiva; aritmética exata."""
from .weighted import condition

def audit(weights, event_a, event_b, given):
    A, B, C = set(event_a), set(event_b), set(given)
    pa = condition(weights, A, C)
    pb = condition(weights, B, C)
    joint = condition(weights, A & B, C)
    # A primeira e a segunda chamadas validam todos os eventos e pesos.
    if pa is None:
        return dict(a=None, b=None, joint=None, product=None, independent=None)
    product = pa * pb
    return dict(a=pa, b=pb, joint=joint, product=product,
                independent=(joint == product))

if __name__ == "__main__":
    w = dict.fromkeys(["00", "01", "10", "11"], 1)
    A, B, C = {"10", "11"}, {"01", "11"}, {"00", "11"}
    print("Sem restrição:", audit(w, A, B, set(w)))
    print("Sabendo igualdade:", audit(w, A, B, C))
