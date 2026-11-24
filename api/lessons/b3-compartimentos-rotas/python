"""Roteiro discreto selecionado; não prediz destino a partir de sequência."""
NODES=('citosol','nucleo','re','golgi','exterior','matriz')
EDGES=(('citosol','nucleo','poro'),('citosol','re','translocacao'),('citosol','matriz','translocacao'),('re','golgi','vesicular'),('golgi','exterior','vesicular'))

def path(start,end):
    if start not in NODES or end not in NODES:raise ValueError('Compartimento não listado')
    queue=[(start,[])];seen={start}
    for node,steps in queue:
        if node==end:return steps
        for source,target,kind in EDGES:
            if source==node and target not in seen:
                seen.add(target);queue.append((target,steps+[(source,target,kind)]))
    return None

def model(case=0):
    if isinstance(case,bool) or not isinstance(case,int) or case not in range(4):raise ValueError('Caso inteiro 0–3')
    target=('nucleo','exterior','matriz','citosol')[case];steps=path('citosol',target)
    return dict(case=case,target=target,steps=steps,nodes=['citosol']+[t for _,t,_ in steps],crossings=sum(k=='translocacao' for _,_,k in steps),vesicles=sum(k=='vesicular' for _,_,k in steps))

if __name__=='__main__':
    assert model(1)['nodes']==['citosol','re','golgi','exterior']
    print(model(1))
