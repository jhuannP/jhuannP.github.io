"""Linguagem inteira retilínea ADD/SUB/MUL por constantes; sem eval ou saltos."""
import json


def integer(value):
    if type(value) is not int:raise ValueError('Inteiro exigido, sem bool/float')
    return value


def normalize(program):
    if not isinstance(program,(list,tuple)):raise ValueError('Programa deve ser lista/tupla')
    result=[]
    for instruction in program:
        if not isinstance(instruction,(list,tuple)) or len(instruction)!=2:
            raise ValueError('Instrução deve conter operação e constante')
        op,value=instruction
        if type(op) is not str or op not in ('ADD','SUB','MUL'):
            raise ValueError('Operação desconhecida')
        result.append((op,integer(value)))
    return tuple(result)


def execute(program,x=0):
    program=normalize(program);acc=integer(x);trace=[acc]
    for op,value in program:
        if op=='ADD':acc+=value
        elif op=='SUB':acc-=value
        else:acc*=value
        trace.append(acc)
    return dict(result=acc,steps=len(program),trace=tuple(trace))


def compile_affine(program):
    """Invariante de prefixo: acumulador = a*x+b."""
    a,b=1,0
    for op,value in normalize(program):
        if op=='ADD':b+=value
        elif op=='SUB':b-=value
        else:a*=value;b*=value
    return a,b


def compose(first,second):
    """Primeiro execute first; depois second sobre sua saída."""
    a1,b1=compile_affine(first);a2,b2=compile_affine(second)
    return a2*a1,a2*b1+b2


def encode(program):
    return json.dumps(normalize(program),separators=(',',':'))


def decode(text):
    if type(text) is not str:raise ValueError('Descrição JSON deve ser texto')
    def reject_constant(value):raise ValueError('Constante JSON não finita não admitida')
    return normalize(json.loads(text,parse_constant=reject_constant))


if __name__=='__main__':
    program=(('ADD',3),('MUL',2))
    description=encode(program)
    assert execute(decode(description),0)['result']==6
    assert compile_affine(program)==(2,6)
    print(description,execute(program),compile_affine(program))
