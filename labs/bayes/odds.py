"""Bayes em razões: domínio estritamente interior, probabilidades exatas."""
from fractions import Fraction as Q

def odds_update(prior, sensitivity, false_positive):
    values = (prior, sensitivity, false_positive)
    if any(type(x) not in (int, Q) or not 0 < x < 1 for x in values):
        raise ValueError("Use Fraction estritamente entre zero e um")
    p, s, f = map(Q, values)
    prior_odds = p / (1 - p)
    likelihood_ratio = s / f
    posterior_odds = prior_odds * likelihood_ratio
    return dict(prior_odds=prior_odds, likelihood_ratio=likelihood_ratio,
                posterior_odds=posterior_odds,
                posterior=posterior_odds / (1 + posterior_odds),
                base_for_half=f / (s + f))

if __name__ == "__main__":
    r = odds_update(Q(1,10), Q(4,5), Q(1,5))
    assert r["prior_odds"] == Q(1,9)
    assert r["likelihood_ratio"] == 4
    assert r["posterior_odds"] == Q(4,9)
    assert r["posterior"] == Q(4,13)
    assert r["base_for_half"] == Q(1,5)
    print(r)
