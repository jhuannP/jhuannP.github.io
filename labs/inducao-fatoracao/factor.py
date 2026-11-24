"""Divisão tentativa: exemplo didático limitado, sem bibliotecas externas."""
def factor(n):
    if type(n) is not int or not 2 <= n <= 1000000:
        raise ValueError("inteiro entre 2 e 1000000")
    remaining, divisor, factors, trace = n, 2, [], []
    while divisor*divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            remaining //= divisor
            trace.append((tuple(factors), remaining))
        else:
            divisor += 1
    if remaining > 1:
        factors.append(remaining)
        remaining = 1
        trace.append((tuple(factors), remaining))
    return tuple(factors), tuple(trace)

if __name__ == '__main__':
    for n in (2, 72, 97, 1000000):
        factors, trace = factor(n)
        print(n, factors, trace)
