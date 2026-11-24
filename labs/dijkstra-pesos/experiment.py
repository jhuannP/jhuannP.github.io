"""Dijkstra próprio com heap de candidatos e pesos racionais não negativos."""
from fractions import Fraction as Q
from heapq import heappush,heappop
from itertools import count

def validate(graph,source):
    if not isinstance(graph,dict) or not graph or any(type(v) is not str or not v for v in graph):
        raise ValueError("Grafo não vazio com vértices string não vazios")
    if type(source) is not str or source not in graph:raise ValueError("Origem deve ser um vértice")
    for edges in graph.values():
        if not isinstance(edges,(list,tuple)):raise ValueError("Adjacências em lista/tupla")
        for e in edges:
            if not isinstance(e,(list,tuple)) or len(e)!=2:raise ValueError("Aresta=(destino,peso)")
            v,w=e
            if type(v) is not str or v not in graph:raise ValueError("Destino deve estar no grafo")
            if type(w) not in (int,Q) or w<0:raise ValueError("Peso int/Fraction não negativo, sem bool")

def dijkstra(graph,source):
    validate(graph,source)
    dist={v:None for v in graph};pred={v:None for v in graph}
    dist[source]=Q(0);serial=count();heap=[(Q(0),next(serial),source)];settled=[]
    while heap:
        du,_,u=heappop(heap)
        if du!=dist[u]:continue # candidato substituído por um caminho melhor
        settled.append((u,du))
        for v,w in graph[u]:
            candidate=du+w
            if dist[v] is None or candidate<dist[v]:
                dist[v]=candidate;pred[v]=(u,Q(w))
                heappush(heap,(candidate,next(serial),v))
    return dict(source=source,dist=dist,pred=pred,settled=settled)

def path_to(result,target):
    if target not in result["dist"]:raise ValueError("Destino desconhecido")
    if result["dist"][target] is None:return None
    path=[];v=target
    while v!=result["source"]:
        path.append(v);v=result["pred"][v][0]
    return [result["source"]]+path[::-1]

def example():
    return dict(A=[("B",4),("C",1),("D",10)],B=[("D",1)],
                C=[("B",2),("D",5)],D=[],E=[])

if __name__=="__main__":
    r=dijkstra(example(),"A")
    assert r["dist"]["D"]==4 and path_to(r,"D")==["A","C","B","D"]
    assert r["dist"]["E"] is None
    print("Distâncias:",r["dist"])
    print("Caminho até D:",path_to(r,"D"))
    print("Vértices finalizados:",r["settled"])
