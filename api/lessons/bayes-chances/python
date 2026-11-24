"""Bayes binário exato; taxas sintéticas, não calibradas por dados."""
from fractions import Fraction as F

def probability(x):
    if isinstance(x, bool) or not isinstance(x, (int, F)) or not 0 <= x <= 1:
        raise ValueError('Use int ou Fraction em [0,1]')
    return F(x)

def ratio(a, b):
    if b == 0:
        return {'kind': 'undefined' if a == 0 else 'infinite', 'value': None}
    return {'kind': 'finite', 'value': a/b}

def update(prior, given_h, given_not_h):
    p, a, b = map(probability, (prior, given_h, given_not_h))
    joint_h = p*a
    joint_not_h = (1-p)*b
    mass = joint_h + joint_not_h
    return {'mass': mass, 'joint_h': joint_h, 'joint_not_h': joint_not_h,
            'posterior': joint_h/mass if mass else None,
            'prior_odds': ratio(p, 1-p),
            'likelihood_ratio': ratio(a, b),
            'posterior_odds': ratio(joint_h, joint_not_h)}

if __name__ == '__main__':
    r = update(F(1,10), F(4,5), F(1,5))
    assert r['posterior'] == F(4,13)
    assert r['posterior_odds']['value'] == F(4,9)
    print('P(H|S)=', r['posterior'], '; chances H:Hc = 4:9')
