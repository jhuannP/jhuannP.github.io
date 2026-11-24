"""Ramos, traçado e duas somas finitas; exemplos próprios."""
n=3
soma=0
for i in range(1,n+1):
    soma+=i
    print(i,soma)
assert soma==6
contador=1
soma_enquanto=0
while contador<=n:
    soma_enquanto+=contador
    contador+=1
assert soma_enquanto==6
# Os exemplos abaixo usam funções; def/return são aprofundados na próxima aula.


def classify_temperature(value):
    if value<0:return 'negativa'
    elif value==0:return 'zero'
    else:return 'positiva'

def checked_n(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=1000:
        raise ValueError('Inteiro entre 0 e 1000 neste exemplo')
    return n

def sum_for(n):
    checked_n(n);total=0;trace=[]
    for i in range(1,n+1):
        before=total;total+=i
        trace.append((i,before,total))
    return total,trace

def sum_while(n):
    checked_n(n);i=1;total=0
    while i<=n:
        total+=i;i+=1
    return total

assert classify_temperature(-1)=='negativa'
assert classify_temperature(0)=='zero'
assert classify_temperature(2)=='positiva'
assert list(range(2,7))==[2,3,4,5,6]
assert list(range(5,0,-2))==[5,3,1]
for n in [0,1,4,5,20]:
    total,_=sum_for(n)
    assert total==sum_while(n)==n*(n+1)//2
assert sum_for(3)[1]==[(1,0,1),(2,1,3),(3,3,6)]
# continue pula o restante daquela iteração; break encerra o laço.
total=0
for i in range(1,6):
    if i==3:continue
    if i==5:break
    total+=i
assert total==7
print('Traçado (i, soma antes, soma depois):',sum_for(3)[1])
print('Soma de 1 a 5:',sum_while(5))
