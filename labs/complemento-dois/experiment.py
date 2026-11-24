"""Somador didático de quatro bits: entradas são padrões 0..15."""
def model(a=7,b=1):
    if any(type(x) is not int or not 0<=x<16 for x in (a,b)):
        raise ValueError("Padrões inteiros de quatro bits:0..15")
    signed=lambda u:u if u<8 else u-16
    carries=[0];bits=[]
    for i in range(4):
        total=((a>>i)&1)+((b>>i)&1)+carries[-1]
        bits.append(total&1);carries.append(total>>1)
    result=sum(bit<<i for i,bit in enumerate(bits))
    exact=signed(a)+signed(b)
    return dict(a=a,b=b,a_signed=signed(a),b_signed=signed(b),
                result=result,result_signed=signed(result),exact=exact,
                carry=carries[4],overflow=not -8<=exact<=7,carries=carries)

if __name__=='__main__':
    for pair in ((7,1),(15,1),(8,8),(1,1)):print(model(*pair))
