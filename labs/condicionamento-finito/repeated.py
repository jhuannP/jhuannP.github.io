"""Dois sinais binários com mesmas marginais; modelo sintético exato."""
from fractions import Fraction as F

def probability(value):
    if isinstance(value, bool) or not isinstance(value, (int, F)) or not 0 <= value <= 1:
        raise ValueError('Use inteiros ou Fraction entre zero e um')
    return F(value)

def pair_table(rate, joint):
    t, j = probability(rate), probability(joint)
    if not max(F(0), 2*t-1) <= j <= t:
        raise ValueError('Interseção incompatível com as marginais')
    return {(1,1): j, (1,0): t-j, (0,1): t-j, (0,0): 1-2*t+j}

def evidence(prior, rate_h, rate_n, joint_h, joint_n):
    p = probability(prior)
    h, n = pair_table(rate_h, joint_h), pair_table(rate_n, joint_n)
    atoms = {(truth, x, y): weight*table[x,y]
             for truth, weight, table in ((1,p,h), (0,1-p,n))
             for x,y in table}
    first = p*F(rate_h)+(1-p)*F(rate_n)
    both = p*h[1,1]+(1-p)*n[1,1]
    return {'atoms': atoms, 'first_mass': first, 'both_mass': both,
            'after_first': p*F(rate_h)/first if first else None,
            'after_both': p*h[1,1]/both if both else None}

if __name__ == '__main__':
    for name, jh, jn in [('independentes dado H', F(16,25), F(1,25)),
                         ('cópia do primeiro', F(4,5), F(1,5)),
                         ('interseções mínimas', F(3,5), F(0))]:
        r = evidence(F(1,10), F(4,5), F(1,5), jh, jn)
        print(name, r['after_first'], r['after_both'])
