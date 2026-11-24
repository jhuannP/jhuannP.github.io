"""Sequências de cores, retiradas uniformes sem reposição; exemplo original."""
from fractions import Fraction as F

def sequence_probability(red, blue, pattern):
    if any(isinstance(v, bool) or not isinstance(v, int) or v < 0 for v in (red, blue)):
        raise ValueError('Quantidades inteiras não negativas')
    if not isinstance(pattern, str) or any(c not in 'RB' for c in pattern):
        raise ValueError('Use uma string de R (vermelha) e B (azul)')
    if len(pattern) > red + blue:
        raise ValueError('Não há objetos suficientes para essas retiradas')
    remaining = {'R': red, 'B': blue}
    probability = F(1)
    for i, color in enumerate(pattern):
        if remaining[color] == 0:
            return F(0)  # sequência impossível; não condicionar depois num prefixo nulo
        probability *= F(remaining[color], red + blue - i)
        remaining[color] -= 1
    return probability

if __name__ == '__main__':
    rr = sequence_probability(3, 2, 'RR')
    r = sequence_probability(3, 2, 'R')
    assert rr == F(3, 10) and rr/r == F(1, 2)
    print('P(R1 e R2)=', rr, '; P(R2|R1)=', rr/r)
