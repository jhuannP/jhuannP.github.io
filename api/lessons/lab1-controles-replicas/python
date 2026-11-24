"""Réplicas aninhadas: dados sintéticos, sem protocolo de bancada."""
from fractions import Fraction as Q
from math import sqrt, isfinite
from statistics import mean, variance


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise ValueError('Use inteiro ou Fraction para componentes exatos.')
    return Q(x)


def planning(n=4, r=3, tau=2, sigma=1):
    for x in (n, r):
        if isinstance(x, bool) or not isinstance(x, int) or not 1 <= x <= 10000:
            raise ValueError('Contagens inteiras entre 1 e 10000.')
    tau, sigma = map(rational, (tau, sigma))
    if min(tau, sigma) < 0:
        raise ValueError('Desvios padrão não negativos.')
    between, within = tau*tau, sigma*sigma
    correct = 2*(between/Q(n)+within/Q(n*r))
    naive = 2*(between+within)/Q(n*r)
    return dict(correct_variance=correct, naive_variance=naive,
                correct_se=sqrt(float(correct)), naive_se=sqrt(float(naive)),
                icc=between/(between+within) if between+within else None,
                design_effect=correct/naive if naive else None)


def summarize(control, treated):
    """Médias por unidade; grupos independentes, sem teste/intervalo causal."""
    def group(units):
        if len(units) < 2 or any(len(readings) == 0 for readings in units):
            raise ValueError('Pelo menos duas unidades por grupo e uma leitura por unidade.')
        for readings in units:
            for x in readings:
                if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
                    raise ValueError('Leituras numéricas finitas.')
        values=[mean(readings) for readings in units]
        return dict(unit_means=values, n=len(values), mean=mean(values),
                    variance_of_mean=variance(values)/len(values))
    c, t=group(control), group(treated)
    v=c['variance_of_mean']+t['variance_of_mean']
    return dict(control=c, treated=t, difference=t['mean']-c['mean'],
                estimated_variance=v, estimated_se=sqrt(v))


if __name__ == '__main__':
    print('Planejamento com componentes conhecidos:', planning())
    print('Resumo do conjunto sintético:', summarize([[8,10],[12,14]], [[12,14],[14,16]]))
    print('Componentes de planejamento não foram estimados do conjunto sintético.')
    print('Sem teste de hipótese, poder, intervalo de confiança ou efeito causal certificado.')
