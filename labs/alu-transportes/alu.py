"""ALU combinacional didática de quatro bits, sem relógio ou estado."""
OPS = ('ADD', 'AND', 'OR', 'XOR')


def word(value):
    if type(value) is not int or not 0 <= value < 16:
        raise ValueError('Palavra deve ser int de 0 a 15, sem bool.')
    return value


def signed(value):
    word(value)
    return value if value < 8 else value - 16


def evaluate(a, b, op):
    word(a)
    word(b)
    if type(op) is not str or op not in OPS:
        raise ValueError('Operação: ADD, AND, OR ou XOR.')
    # Todos os blocos combinacionais recebem os mesmos operandos.
    carry = [0]
    sums = []
    for i in range(4):
        x, y, c = (a >> i) & 1, (b >> i) & 1, carry[-1]
        sums.append(x ^ y ^ c)
        carry.append((x & y) | (x & c) | (y & c))
    candidates = {
        'ADD': sum(bit << i for i, bit in enumerate(sums)),
        'AND': a & b, 'OR': a | b, 'XOR': a ^ b,
    }
    result = candidates[op]
    return {'result': result, 'z': int(result == 0),
            'c': carry[4] if op == 'ADD' else 0,
            'v': (carry[3] ^ carry[4]) if op == 'ADD' else 0,
            'carries': tuple(carry)}


if __name__ == '__main__':
    for a, b in [(7, 1), (15, 1), (8, 8), (2, 3)]:
        print(a, b, evaluate(a, b, 'ADD'))
