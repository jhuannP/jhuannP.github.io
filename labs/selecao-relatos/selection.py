"""Modelo finito: estado H, relato R e registro S. Taxas conhecidas, não estimadas."""
from fractions import Fraction as Q
from itertools import product

def probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise TypeError("Use int ou Fraction, sem bool ou float")
    value = Q(value)
    if not 0 <= value <= 1:
        raise ValueError("Probabilidade fora de [0,1]")
    return value

def joint(prior, positive_h, positive_not_h, retention):
    """retention[(h,r)] = P(S=True | H=h, R=r); exatamente quatro chaves bool."""
    prior, positive_h, positive_not_h = map(probability, (prior, positive_h, positive_not_h))
    if not isinstance(retention, dict) or len(retention) != 4 or any(
        not isinstance(k, tuple) or len(k) != 2 or any(type(x) is not bool for x in k)
        for k in retention
    ):
        raise ValueError("Forneça as quatro chaves (bool,bool)")
    rates = {key: probability(value) for key, value in retention.items()}
    result = {}
    for h,r,s in product((False,True), repeat=3):
        ph = prior if h else 1-prior
        pr = positive_h if h else positive_not_h
        pr = pr if r else 1-pr
        ps = rates[h,r] if s else 1-rates[h,r]
        result[h,r,s] = ph*pr*ps
    return result

def condition(table, *, report=None, recorded=None):
    """P(H=True | informação fornecida). None omite o evento; massa zero -> None."""
    if any(x is not None and type(x) is not bool for x in (report,recorded)):
        raise TypeError("Filtros devem ser bool ou None")
    selected = [(h,mass) for (h,r,s),mass in table.items()
                if (report is None or r is report) and (recorded is None or s is recorded)]
    evidence = sum((mass for _,mass in selected), Q(0))
    return None if evidence == 0 else sum((mass for h,mass in selected if h),Q(0))/evidence
