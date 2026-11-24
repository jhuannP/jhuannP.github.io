"""Funções: contrato, retorno, escopo e objetos compartilhados."""

def energia_cinetica(massa_kg,velocidade_m_s):
    # Faixas didáticas limitam a implementação, não a lei física.
    if isinstance(massa_kg,bool) or not isinstance(massa_kg,(int,float)) or not 0<massa_kg<=1e6:
        raise ValueError('Massa positiva até 10^6 kg')
    if isinstance(velocidade_m_s,bool) or not isinstance(velocidade_m_s,(int,float)) or not -1e6<=velocidade_m_s<=1e6:
        raise ValueError('Velocidade finita em [-10^6,10^6] m/s')
    return .5*massa_kg*velocidade_m_s**2

def mostrar_energia(massa_kg,velocidade_m_s):
    print(energia_cinetica(massa_kg,velocidade_m_s))

def dobrar(valor):return 2*valor

def reatribuir(lista):
    lista=[9] # Muda apenas o nome local.
    return lista

def acrescentar(lista,item):
    lista.append(item) # Muda o objeto compartilhado.

def criar_lista(item,lista=None):
    # Nenhuma lista mutável é criada como argumento padrão.
    if lista is None:lista=[]
    lista.append(item)
    return lista

assert energia_cinetica(2,3)==9
assert energia_cinetica(2,-3)==9
assert energia_cinetica(2,0)==0
assert energia_cinetica(4,2)==8
for mass,speed in [(0,1),(-1,1),(True,2),(2,float('nan'))]:
    try:energia_cinetica(mass,speed)
    except ValueError:pass
    else:raise AssertionError('Entrada inválida deve falhar')
valor=10
assert dobrar(3)==6 and valor==10
original=[1,2]
assert reatribuir(original)==[9] and original==[1,2]
assert acrescentar(original,3) is None and original==[1,2,3]
assert criar_lista('A')==['A'] and criar_lista('B')==['B']
resultado=mostrar_energia(2,3)
assert resultado is None # Imprimir 9 não retorna 9.
print('Valor retornado pela função que só imprime:',resultado)
