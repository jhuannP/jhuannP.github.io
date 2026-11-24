"""Execute e explique os exemplos antes de alterar os valores.
Python3, somente biblioteca padrão; sem entrada externa, eval ou arquivos de dados.
Os assert são referências didáticas, não validação de qualquer programa do usuário.
"""
from math import isclose,isfinite
from fractions import Fraction
import sys

print("Python",sys.version.split()[0])

# Atribuir um resultado não mantém uma ligação algébrica reativa.
tempo_min=2
tempo_s=tempo_min*60
states=[(tempo_min,tempo_s)]
tempo_min=3
states.append((tempo_min,tempo_s))
tempo_s=tempo_min*60
states.append((tempo_min,tempo_s))
assert states==[(2,120),(3,120),(3,180)]
print("Estados (min,s):",states)

# Reatribuição de número versus mutação de um objeto compartilhado.
a=2;b=a;a=a+1
assert (a,b)==(3,2)
items=[1,2];same=items
same.append(3)
assert items is same and items==[1,2,3]
same=same+[4]
assert items==[1,2,3] and same==[1,2,3,4] and items is not same
print("Lista anterior e nova:",items,same)

# Expressões fixas, escritas explicitamente: não executamos texto recebido.
cases=[
    ("8 / 2",8/2,4.0,float),
    ("8 // 3",8//3,2,int),
    ("8.0 // 3",8.0//3,2.0,float),
    ("-7 // 3",-7//3,-3,int),
    ("-7 % 3",-7%3,2,int),
    ("2 + 3 * 4",2+3*4,14,int),
    ("(2 + 3) * 4",(2+3)*4,20,int),
    ("-2**2",-2**2,-4,int),
    ("(-2)**2",(-2)**2,4,int),
    ('"3" + "4"',"3"+"4","34",str),
    ('"3" * 4',"3"*4,"3333",str),
    ('int("12") + 3',int("12")+3,15,int),
]
for expression,value,expected,kind in cases:
    assert value==expected and type(value) is kind
    print(expression,"->",repr(value),type(value).__name__)
assert -7==3*(-7//3)+(-7%3)

try:
    "3"+4
except TypeError:
    print('"3" + 4 -> TypeError esperado')
else:
    raise AssertionError("mistura de texto e número aceita inesperadamente")
try:
    int("3.5")
except ValueError:
    print('int("3.5") -> ValueError esperado')
else:
    raise AssertionError("texto decimal convertido diretamente para int")

assert type(True) is bool and isinstance(True,int) and True+1==2
assert 3==3.0 and type(3) is not type(3.0)
assert "3"!=3

# Esta demonstração de representação pressupõe o float binário usual.
assert sys.float_info.radix==2
assert .1+.2!=.3
assert isclose(.1+.2,.3,rel_tol=1e-12,abs_tol=0)
assert not isclose(1e-12,0,rel_tol=1e-9,abs_tol=0)
assert isclose(1e-12,0,rel_tol=0,abs_tol=1e-11)
assert Fraction(1,10)+Fraction(2,10)==Fraction(3,10)
assert not isfinite(float("nan")) and not isfinite(float("inf"))
print("Float:",repr(.1+.2),"isclose:",isclose(.1+.2,.3,rel_tol=1e-12))

velocidade_m_s=3
tempo_min=2
tempo_s=tempo_min*60
deslocamento_m=velocidade_m_s*tempo_s
assert deslocamento_m==360 and tempo_min==2 and tempo_s==120
print("Movimento uniforme:",deslocamento_m,"m em",tempo_s,"s")
print("Referências dos exemplos conferidas. Agora explique cada etapa sem executar.")
