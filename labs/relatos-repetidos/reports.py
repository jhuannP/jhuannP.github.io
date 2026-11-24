"""Toy likelihoods, not an empirical sensor calibration. Exact arithmetic only."""
from fractions import Fraction as Q
from itertools import product

MODES = ("independente", "copia", "misto")

def likelihood(h, first, second, mode):
    """P(first,second | h), with h and reports literal bools."""
    if any(type(x) is not bool for x in (h, first, second)):
        raise TypeError("h and reports must be bool")
    if mode not in MODES:
        raise ValueError("unknown observation mechanism")
    positive = Q(3, 4) if h else Q(1, 4)
    p1 = positive if first else 1 - positive
    p2 = positive if second else 1 - positive
    independent = p1 * p2
    copied = p1 if first == second else Q(0)
    if mode == "independente":
        return independent
    if mode == "copia":
        return copied
    return (independent + copied) / 2

def update(first, second, mode, prior=Q(1, 2)):
    """Return (P(reports), P(h|reports)); None for zero evidence."""
    if type(prior) not in (int, Q):
        raise TypeError("prior must be int or Fraction, not float/bool")
    if not 0 <= prior <= 1:
        raise ValueError("prior outside [0,1]")
    yes = prior * likelihood(True, first, second, mode)
    no = (1 - prior) * likelihood(False, first, second, mode)
    evidence = yes + no
    return evidence, yes / evidence if evidence else None

if __name__ == "__main__":
    for mode in MODES:
        print(mode, update(True, True, mode))
