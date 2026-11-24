"""Traços didáticos próprios, sem introspecção do interpretador."""


def natural(n):
    if not isinstance(n,int) or isinstance(n,bool) or n<0:
        raise ValueError('Use inteiro não negativo')


def fatorial(n):
    natural(n)
    if n==0:return 1
    return n*fatorial(n-1)


def potencia(base,n):
    natural(n)
    if not isinstance(base,int) or isinstance(base,bool):raise ValueError('Base inteira')
    if n==0:return 1
    q=potencia(base,n//2)
    square=q*q
    return square*base if n%2 else square


def soma_recursiva(n):
    natural(n)
    if n==0:return 0
    return n+soma_recursiva(n-1)


def trace(kind=0,n=4):
    natural(n)
    if kind not in (0,1) or n>10:raise ValueError('Modo 0/1 e n de 0 a 10 no traço')
    events=[];stack=[];calls=0;mults=0;peak=0
    def record(event,arg,value=None):
        events.append(dict(event=event,arg=arg,value=value,stack=[dict(f) for f in stack],calls=calls,mults=mults,peak=peak))
    def visit(m):
        nonlocal calls,mults,peak
        calls+=1;stack.append(dict(n=m,state='executando'));peak=max(peak,len(stack));record('entrada',m)
        if m==0:value=1
        else:
            stack[-1]['state']='aguardando'
            q=visit(m-1 if kind==0 else m//2)
            if kind==0:value=m*q;mults+=1
            else:
                value=q*q;mults+=1
                if m%2:value*=2;mults+=1
        stack[-1]['state']='devolvendo';record('retorno',m,value);stack.pop()
        return value
    result=visit(n);record('fim',n,result)
    return dict(kind=kind,n=n,result=result,events=events,calls=calls,mults=mults,peak=peak)


if __name__=='__main__':
    assert fatorial(0)==1 and fatorial(5)==120
    assert potencia(3,5)==243 and soma_recursiva(4)==10
    for kind in (0,1):
        t=trace(kind,4)
        for e in t['events']:print(e)
