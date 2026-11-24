"""Médias em tabela e incerteza de um sinal constante sorteado por trajetória."""
from fractions import Fraction as Q

def averages(paths):
    rows=tuple(tuple(row) for row in paths)
    if not rows or not rows[0] or any(len(row)!=len(rows[0]) for row in rows):
        raise ValueError("Tabela retangular não vazia")
    if any(type(x) not in (int,Q) for row in rows for x in row):
        raise ValueError("Entradas int ou Fraction, sem bool")
    M,N=len(rows),len(rows[0])
    ensemble=tuple(sum((row[n] for row in rows),Q(0))/M for n in range(N))
    temporal=tuple(sum(row,Q(0))/N for row in rows)
    return ensemble,temporal

def variance_of_mean(covariance):
    C=tuple(tuple(row) for row in covariance)
    N=len(C)
    if not N or any(len(row)!=N for row in C):raise ValueError("Matriz quadrada não vazia")
    if any(type(x) not in (int,Q) for row in C for x in row):raise ValueError("Use int ou Fraction")
    if any(C[i][j]!=C[j][i] for i in range(N) for j in range(N)):
        raise ValueError("Covariância deve ser simétrica")
    # Rotina algébrica: não certifica semidefinição positiva nem estima C de dados.
    return sum((x for row in C for x in row),Q(0))/(N*N)

if __name__ == "__main__":
    print("Conjunto completo, duas trajetórias equiprováveis:",averages([[-1]*4,[1]*4]))
    print("Var(média temporal):",variance_of_mean([[1]*4 for _ in range(4)]))
