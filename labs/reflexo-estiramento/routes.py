"""Caminhos simples num esquema assinado; não calcula resposta fisiológica."""
from math import prod

EDGES=(("Ia","alfa_hom",1),("Ia","inter",1),("inter","alfa_ant",-1))

def routes(edges,start,target):
    edges=tuple(edges)
    if len(edges)>16: raise ValueError("esquema didático: até 16 conexões")
    if any(len(e)!=3 or not isinstance(e[0],str) or not isinstance(e[1],str)
           or type(e[2]) is not int or e[2] not in (-1,1) for e in edges):
        raise ValueError("conexões precisam de dois nomes e sinal +1 ou -1")
    if len({(a,b) for a,b,_ in edges})!=len(edges): raise ValueError("conexão duplicada")
    nodes={n for a,b,_ in edges for n in (a,b)}
    if len(nodes)>8 or start not in nodes or target not in nodes or start==target:
        raise ValueError("até oito nós; origem e destino distintos e presentes")
    found=[]
    def walk(node,path,signs):
        if node==target:
            found.append({"path":path,"synapses":len(signs),"sign":prod(signs)})
            return
        for a,b,s in edges:
            if a==node and b not in path: walk(b,path+(b,),signs+(s,))
    walk(start,(start,),())
    return found

if __name__=="__main__":
    for target in ("alfa_hom","alfa_ant"):
        print(routes(EDGES,"Ia",target))
    print("Contagem central do desenho; sem tempos, ganhos ou inferência de movimento.")
