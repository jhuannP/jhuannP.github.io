"""Dois corpos rígidos com capacidades térmicas totais iguais e constantes."""
from math import sqrt,log,isfinite

def parameters(hot,cold,capacity):
    values=[]
    for x in (hot,cold,capacity):
        if isinstance(x,bool) or not isinstance(x,(int,float)):
            raise ValueError('Real finito, sem bool')
        try: value=float(x)
        except OverflowError: raise ValueError('Real finito necessário') from None
        if not isfinite(value):raise ValueError('Real finito necessário')
        values.append(value)
    hot,cold,capacity=values
    if not 50<=cold<=hot<=2000 or not .01<=capacity<=10000:
        raise ValueError('Recorte: 50<=Tc<=Th<=2000 K; 0.01<=C<=10000 J/K')
    return hot,cold,capacity

def compare(hot,cold,capacity):
    h,c,C=parameters(hot,cold,capacity)
    tr=sqrt(h*c);ta=(h+c)/2
    # Forma equivalente evita subtrair duas grandes energias quase iguais.
    work=C*((h-c)/(sqrt(h)+sqrt(c)))**2
    return {'reversible_k':tr,'contact_k':ta,'maximum_j':work,
            'heat_hot_j':C*(h-tr),'heat_cold_j':C*(tr-c),
            'entropy_contact_jk':C*(log(ta/h)+log(ta/c)),
            'efficiency_initial':1-c/h}

def path(hot,cold,capacity,steps):
    h,c,C=parameters(hot,cold,capacity)
    if isinstance(steps,bool) or type(steps) is not int or not 1<=steps<=200:
        raise ValueError('Inteiro 1..200')
    end=sqrt(h*c)
    # Estados da trajetória reversível analítica, não ciclos discretos físicos.
    return tuple((H,h*c/H)for H in (h+(end-h)*j/steps for j in range(steps+1)))

if __name__=='__main__':
    print(compare(400,100,2))
