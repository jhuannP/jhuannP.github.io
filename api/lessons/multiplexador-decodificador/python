def bit(x):
    if type(x) is not int or x not in (0,1):
        raise ValueError('Use int 0 ou 1')
    return x

def mux(a,b,s):
    a,b,s=map(bit,(a,b,s))
    return ((1-s)&a)|(s&b)

def decodificar_endereco(endereco,en=1):
    if type(endereco) is not int or not 0<=endereco<4:
        raise ValueError('Endereço inteiro de 0 a 3')
    en=bit(en)
    s1,s0=endereco//2,endereco%2
    return [en&(1-s1)&(1-s0),en&(1-s1)&s0,
            en&s1&(1-s0),en&s1&s0]

assert mux(1,0,1)==0 and mux(1,0,0)==1
assert decodificar_endereco(2)==[0,0,1,0]
assert decodificar_endereco(2,0)==[0,0,0,0]
print(mux(1,0,1),decodificar_endereco(2))
