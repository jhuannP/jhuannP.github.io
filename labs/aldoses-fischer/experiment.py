"""Fischer de aldo-hexoses abertas; 0=OH à esquerda, 1=OH à direita."""
from itertools import product
REFERENCE=(1,0,1,1) # D-glicose, C2 a C5

def pattern(bits):
    if not isinstance(bits,(tuple,list)) or len(bits)!=4 or any(isinstance(x,bool) or not isinstance(x,int) or x not in (0,1) for x in bits):
        raise ValueError('Quatro inteiros0/1, em C2,C3,C4,C5')
    return tuple(bits)

def relation(first,second):
    first,second=pattern(first),pattern(second)
    changed=[i+2 for i,(a,b) in enumerate(zip(first,second)) if a!=b]
    n=len(changed)
    return dict(changed=changed,relation='identical' if n==0 else 'epimer' if n==1 else 'enantiomer' if n==4 else 'diastereomer')

def inspect(bits=REFERENCE):
    bits=pattern(bits)
    names={(1,0,1,1):'D-glicose',(0,0,1,1):'D-manose',(1,0,0,1):'D-galactose',(0,1,0,0):'L-glicose'}
    return dict(bits=list(bits),series='D' if bits[-1] else 'L',name=names.get(bits,'Outra aldo-hexose do recorte'),**relation(REFERENCE,bits))

if __name__=='__main__':
    assert inspect((0,0,1,1))['changed']==[2]
    assert inspect((0,1,0,0))['relation']=='enantiomer'
    print(inspect((0,0,1,1)))
