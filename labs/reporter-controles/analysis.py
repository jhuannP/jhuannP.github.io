"""Balanço didático de fluorescência, sem inferência causal automática."""
from fractions import Fraction as F

def value(x):
    if type(x) not in (int,F):raise TypeError('Use inteiro ou Fraction')
    return F(x)

def per_cell(raw,blank,cells):
    """Modelo F=N*q+B; células comparáveis e branco compatível assumidos."""
    raw,blank,cells=map(value,(raw,blank,cells))
    if raw<0 or blank<0 or cells<=0:raise ValueError('Sinais não negativos e células positivas')
    return (raw-blank)/cells

def fold(test,reference):
    """Sem razão interpretável se referência não positiva ou teste negativo."""
    test,reference=map(value,(test,reference))
    return None if reference<=0 or test<0 else test/reference

if __name__=='__main__':
    intact=per_cell(220,20,100)
    deleted=per_cell(70,20,50)
    print('Por célula:',intact,deleted)
    print('Razão intacto/deletado:',fold(intact,deleted))
