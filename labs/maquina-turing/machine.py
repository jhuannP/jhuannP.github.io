"""Interpretador didático de tabelas determinísticas finitas.

Convenção: escrever, mover -1/0/+1, mudar estado; então conferir parada.
Fita indexada por inteiros; '_' branco. Não executa código fornecido na tabela.
"""
BLANK='_'


def name(x):
    if type(x) is not str or not x:raise ValueError('Estado deve ser texto não vazio')
    return x


def symbol(x):
    if type(x) is not str or len(x)!=1:raise ValueError('Símbolo deve ser um caractere')
    return x


def run(program,tape,*,state='buscar',head=0,accept='aceita',reject='rejeita',max_steps=100):
    state,accept,reject=map(name,(state,accept,reject))
    if accept==reject:raise ValueError('Estados de aceitação e rejeição devem diferir')
    if type(head) is not int or type(max_steps) is not int or max_steps<0:
        raise ValueError('Cabeça inteira e orçamento inteiro não negativo')
    if not isinstance(program,dict) or not isinstance(tape,dict):
        raise ValueError('Tabela e fita devem ser dicionários')
    for key,value in program.items():
        if not isinstance(key,tuple) or len(key)!=2 or not isinstance(value,tuple) or len(value)!=3:
            raise ValueError('Regra: (estado,símbolo):(novo,escrita,movimento)')
        name(key[0]);symbol(key[1]);name(value[0]);symbol(value[1])
        if type(value[2]) is not int or value[2] not in (-1,0,1):raise ValueError('Movimento -1,0 ou1')
    cells={}
    for position,char in tape.items():
        if type(position) is not int:raise ValueError('Posição inteira, sem bool')
        if symbol(char)!=BLANK:cells[position]=char
    steps=0;history=[]
    while True:
        history.append(dict(state=state,head=head,tape=cells.copy(),steps=steps))
        if state==accept:status='aceita';break
        if state==reject:status='rejeita';break
        if steps==max_steps:status='limite';break
        instruction=program.get((state,cells.get(head,BLANK)))
        if instruction is None:status='sem_regra';break
        next_state,write,move=instruction
        if write==BLANK:cells.pop(head,None)
        else:cells[head]=write
        head+=move;state=next_state;steps+=1
    return dict(status=status,state=state,head=head,tape=cells.copy(),steps=steps,history=tuple(history))


def unary_tape(n):
    if type(n) is not int or n<0:raise ValueError('n inteiro não negativo')
    return {i:'1' for i in range(n)}


def binary_tape(word):
    if type(word) is not str or any(c not in '01' for c in word):raise ValueError('Palavra binária exigida')
    return dict(enumerate(word))


UNARY={('buscar','1'):('buscar','1',1),('buscar',BLANK):('aceita','1',1)}
PARITY={('par','0'):('par','0',1),('par','1'):('impar','1',1),
        ('impar','0'):('impar','0',1),('impar','1'):('par','1',1),
        ('par',BLANK):('aceita',BLANK,1),('impar',BLANK):('rejeita',BLANK,1)}

if __name__=='__main__':
    r=run(UNARY,unary_tape(3),max_steps=4)
    assert r['status']=='aceita' and r['steps']==4 and r['head']==4
    print('Traço:',r['history'])
    print('Paridade de101:',run(PARITY,binary_tape('101'),state='par')['status'])
