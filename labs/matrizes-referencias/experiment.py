"""Matrizes racionais retangulares; sem alterar os dados de entrada."""
from fractions import Fraction as Q

def shape(A):
    if type(A) is not list or not A or any(type(row) is not list or not row for row in A):
        raise ValueError("Lista não vazia de linhas não vazias")
    n = len(A[0])
    if any(len(row) != n for row in A):
        raise ValueError("Linhas devem ter o mesmo tamanho")
    if any(type(x) not in (int, Q) for row in A for x in row):
        raise ValueError("Use int ou Fraction, sem bool")
    return len(A), n

def copy_rows(A):
    shape(A)
    return [row.copy() for row in A]

def column_means(A):
    m, n = shape(A)
    return [sum((Q(A[i][j]) for i in range(m)), Q(0))/m for j in range(n)]

def center_columns(A):
    means = column_means(A)
    return [[Q(x)-means[j] for j, x in enumerate(row)] for row in A]

if __name__ == "__main__":
    A = [[2,10],[4,14],[6,12]]
    B = center_columns(A)
    assert B == [[-2,-2],[0,2],[2,0]]
    assert A == [[2,10],[4,14],[6,12]]
    print("Entrada:", A)
    print("Médias por coluna:", column_means(A))
    print("Centralizada:", B)
    bad = [[0,0]]*2
    good = [[0,0] for _ in range(2)]
    bad[0][1] = 7
    good[0][1] = 7
    assert bad == [[0,7],[0,7]] and good == [[0,7],[0,0]]
    print("Linhas compartilhadas:", bad)
    print("Linhas independentes:", good)
