"""Memória didática 4×8: leitura combinacional e transição por evento."""
def integer(value, low, high, name):
    if type(value) is not int or not low <= value <= high:
        raise ValueError(name)
    return value


def state_check(state):
    if type(state) is not tuple or len(state) != 4:
        raise ValueError('Estado: tupla de quatro bytes.')
    for value in state:
        integer(value, 0, 255, 'Byte inválido.')


def decoder(address):
    integer(address, 0, 3, 'Endereço: 0..3.')
    a0, a1 = address & 1, (address >> 1) & 1
    return ((1-a1) & (1-a0), (1-a1) & a0,
            a1 & (1-a0), a1 & a0)


def read(state, address):
    state_check(state)
    selected = decoder(address)
    result = 0
    for bit in range(8):
        out = 0
        for index in range(4):
            out |= selected[index] & ((state[index] >> bit) & 1)
        result |= out << bit
    return result


def transition(state, address, data, we, event):
    state_check(state)
    selected = decoder(address)
    integer(data, 0, 255, 'Dado: 0..255.')
    integer(we, 0, 1, 'we: int 0 ou 1.')
    integer(event, 0, 1, 'event: int 0 ou 1.')
    updated = []
    for index in range(4):
        enable = selected[index] & we & event
        value = 0
        for bit in range(8):
            old, new = (state[index] >> bit) & 1, (data >> bit) & 1
            value |= (((1-enable) & old) | (enable & new)) << bit
        updated.append(value)
    return tuple(updated)


TRACE = ((2, 9, 1, 0), (2, 9, 1, 1), (2, 7, 0, 1),
         (1, 200, 1, 1), (2, 13, 1, 1), (2, 13, 1, 1))

if __name__ == '__main__':
    state = (3, 85, 170, 240)
    for inputs in TRACE:
        address, data, we, event = inputs
        before = read(state, address)
        updated = transition(state, *inputs)
        print(inputs, 'antes=', before, 'depois=', read(updated, address), updated)
        state = updated
