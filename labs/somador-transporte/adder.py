"""Portas/encadeamento ideais. Não mede tempo, potência ou circuito físico."""
def bit(x):
    if type(x) is not int or x not in (0,1):raise ValueError("Bit inteiro0/1 necessário.")
    return x

def width_value(width):
    if type(width) is not int or not 1<=width<=16:raise ValueError("Largura inteira1..16 necessária.")
    return width

def word(x,width):
    width=width_value(width)
    if type(x) is not int or not 0<=x<1<<width:raise ValueError("Palavra fora da largura.")
    return x

def full_adder(a,b,carry):
    a,b,carry=map(bit,(a,b,carry));propagate=a^b;generate=a&b
    return propagate^carry,generate|(propagate&carry)

def decode_signed(value,width):
    value=word(value,width)
    return value if value<(1<<(width-1)) else value-(1<<width)

def ripple(a,b,width,carry_in=0):
    width=width_value(width);a,b=word(a,width),word(b,width);carry=bit(carry_in)
    result=0;trace=[]
    for i in range(width):
        ai,bi=(a>>i)&1,(b>>i)&1;before=carry
        si,carry=full_adder(ai,bi,before);result|=si<<i
        trace.append(dict(index=i,a=ai,b=bi,carry_in=before,sum=si,carry_out=carry,
                          prefix=result))
    overflow=trace[-1]['carry_in']^carry
    return dict(low=result,carry=carry,overflow=overflow,trace=trace)

if __name__=='__main__':
    for a,b in [(15,1),(7,1),(5,6)]:print(a,b,ripple(a,b,4))
