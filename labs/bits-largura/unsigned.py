"""Palavras sem sinal, w=1..16; bytes de 8 bits e ordem declarada."""
def integer(v):
    if type(v) is not int:raise TypeError("Inteiro sem bool necessário.")
    return v

def width(w):
    w=integer(w)
    if not 1<=w<=16:raise ValueError("Largura de 1 a 16 bits.")
    return w

def encode(n,w=8):
    n,w=integer(n),width(w)
    if not 0<=n<2**w:raise ValueError("Inteiro fora da faixa sem sinal.")
    bits=[]
    for _ in range(w):
        n,remainder=divmod(n,2);bits.append(str(remainder))
    return ''.join(reversed(bits))

def decode(bits):
    if type(bits) is not str:raise TypeError("Texto binário necessário.")
    if not 1<=len(bits)<=16 or any(c not in '01' for c in bits):raise ValueError("1..16 caracteres ASCII 0/1.")
    value=0
    for c in bits:value=2*value+int(c)
    return value

def wrap(n,w=8):
    return integer(n)%(2**width(w))

def byte_order(order):
    if order not in ('big','little'):raise ValueError("Ordem big ou little.")
    return order

def pack16(n,order='big'):
    n=integer(n);order=byte_order(order)
    if not 0<=n<65536:raise ValueError("Faixa sem sinal de 16 bits.")
    hi,lo=divmod(n,256)
    return bytes((hi,lo) if order=='big' else (lo,hi))

def unpack16(data,order='big'):
    order=byte_order(order)
    if type(data) is not bytes or len(data)!=2:raise ValueError("Exatamente dois bytes.")
    first,second=data
    return 256*first+second if order=='big' else first+256*second

if __name__=='__main__':
    print(encode(46),decode('00101110'),wrap(300))
    print(pack16(300,'big').hex(),pack16(300,'little').hex())
