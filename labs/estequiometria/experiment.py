"""Balanço estequiométrico ideal: 2 H2 + O2 -> 2 H2O; quantidades em mol."""
from fractions import Fraction as Q


def amount(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or x<0:
        raise ValueError('Quantidade não negativa em inteiro ou Fraction.')
    return Q(x)


def balanced(hydrogen,oxygen,water):
    if any(isinstance(x,bool) or not isinstance(x,int) or x<=0 for x in (hydrogen,oxygen,water)):
        raise ValueError('Coeficientes inteiros positivos.')
    return 2*hydrogen==2*water and 2*oxygen==water


def reaction(h2,o2):
    h2,o2=map(amount,(h2,o2))
    extent=min(h2/2,o2)
    final={'H2':h2-2*extent,'O2':o2-extent,'H2O':2*extent}
    exhausted=[name for name in ('H2','O2') if final[name]==0]
    return dict(extent=extent,initial={'H2':h2,'O2':o2,'H2O':Q(0)},final=final,
                exhausted=exhausted,H_atoms_initial=2*h2,O_atoms_initial=2*o2,
                H_atoms_final=2*final['H2']+2*final['H2O'],
                O_atoms_final=2*final['O2']+final['H2O'])


if __name__=='__main__':
    print('Coeficientes 2,1,2 balanceiam H e O:',balanced(2,1,2))
    for h2,o2 in ((3,2),(4,2),(6,2),(0,2)):
        print('Balanço para H2/O2 iniciais:',h2,o2,reaction(h2,o2))
    print('Modelo de conversão completa, não previsão de cinética ou equilíbrio.')
