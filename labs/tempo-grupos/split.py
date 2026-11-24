"""Divisões didáticas e memorizador por grupo; não é API scikit-learn."""
from fractions import Fraction as Q

def integer(x):
    if isinstance(x,bool) or not isinstance(x,int):raise ValueError('Inteiro necessário')
    return x

def data(groups,values):
    groups=list(groups);values=list(values)
    if not 1<=len(groups)<=100 or len(groups)!=len(values):raise ValueError('Dados pareados1..100 necessários')
    if any(not isinstance(g,str) or not g or len(g)>30 for g in groups):raise ValueError('Grupos textuais necessários')
    if any(isinstance(y,bool) or not isinstance(y,(int,Q)) for y in values):raise ValueError('Valores int/Fraction necessários')
    return groups,[Q(y) for y in values]

def memorize(groups,values,train,test):
    groups,values=data(groups,values);train=list(train);test=list(test)
    for part in (train,test):
        if not part or any(not 0<=integer(i)<len(groups) for i in part) or len(set(part))!=len(part):
            raise ValueError('Índices únicos não vazios no domínio necessários')
    if set(train)&set(test):raise ValueError('Linhas sobrepostas')
    fallback=sum(values[i] for i in train)/len(train)
    means={g:sum(values[i] for i in train if groups[i]==g)/sum(groups[i]==g for i in train)
           for g in {groups[i] for i in train}}
    pred=[means.get(groups[i],fallback) for i in test]
    sse=sum((a-values[i])**2 for a,i in zip(pred,test))
    return dict(predictions=pred,fallback=fallback,sse=sse,mse=sse/len(test))

def leave_group_out(groups):
    groups,_=data(groups,[0]*len(groups))
    names=sorted(set(groups))
    if len(names)<2:raise ValueError('Dois grupos distintos necessários')
    return [(tuple(i for i,g in enumerate(groups) if g!=name),
             tuple(i for i,g in enumerate(groups) if g==name)) for name in names]

def temporal(n,cut,horizon,size):
    """Origens unitárias0..n-1; alvo da linha t disponível em t+horizon.
    Ajuste em cut após observações de cut. Previsões emitidas em cada origem.
    """
    n,cut,horizon,size=map(integer,(n,cut,horizon,size))
    if not 2<=n<=100 or not 1<=horizon<=20 or not 1<=size<=n or not 0<cut<n or cut+size>n:
        raise ValueError('Tamanhos/tempos fora do contrato')
    train=tuple(t for t in range(cut) if t+horizon<=cut)
    purge=tuple(t for t in range(cut) if t+horizon>cut)
    test=tuple(range(cut,cut+size))
    if not train:raise ValueError('Treino sem rótulos disponíveis')
    return train,purge,test

if __name__=='__main__':
    g=['A','A','B','B','C','C'];y=[0,2,8,10,16,18]
    known=memorize(g,y,[0,2,4],[1,3,5]);print('Mesmo grupo:',known['mse'])
    folds=[memorize(g,y,tr,te) for tr,te in leave_group_out(g)]
    combined=sum(r['sse'] for r in folds)/len(y)
    assert known['mse']==4 and combined==97
    print('Grupo novo, OOF:',combined)
    print('Tempo:',temporal(10,8,2,2))
