"""Anel de quatro vizinhos com adição de atalhos, não religação de arestas."""
from collections import deque
from itertools import combinations

def integer(x,low,high):
    if isinstance(x,bool) or not isinstance(x,int) or not low<=x<=high:
        raise ValueError(f'Inteiro entre {low} e {high}')
    return x

def validate(graph):
    n=len(graph);integer(n,2,40)
    out=[set(row) for row in graph]
    for u,row in enumerate(out):
        for v in row:
            integer(v,0,n-1)
            if u==v or u not in out[v]:raise ValueError('Grafo simples não dirigido: sem laços e simétrico')
    return out

def bfs(graph,source):
    graph=validate(graph);integer(source,0,len(graph)-1)
    distances={source:0};queue=deque([source])
    while queue:
        u=queue.popleft()
        for v in sorted(graph[u]):
            if v not in distances:distances[v]=distances[u]+1;queue.append(v)
    return distances

def metrics(graph):
    graph=validate(graph);n=len(graph)
    distances=[bfs(graph,u) for u in range(n)]
    connected=all(len(row)==n for row in distances)
    mean=sum(sum(row.values()) for row in distances)/(n*(n-1)) if connected else None
    local=[]
    for neighbors in graph:
        possible=len(neighbors)*(len(neighbors)-1)//2
        triangles=sum(v in graph[u] for u,v in combinations(sorted(neighbors),2))
        local.append(triangles/possible if possible else 0.)
    return dict(connected=connected,mean_distance=mean,mean_clustering=sum(local)/n,
                local_clustering=local,edges=sum(map(len,graph))//2)

def ring(n):
    integer(n,8,40)
    return [{(u+d)%n for d in [-2,-1,1,2]} for u in range(n)]

def network(n,extra,seed):
    graph=ring(n)
    candidates=[(u,v) for u in range(n) for v in range(u+1,n) if v not in graph[u]]
    integer(extra,0,len(candidates));integer(seed,0,2**32-1)
    state=seed
    for i in range(len(candidates)-1,0,-1):
        state=(1664525*state+1013904223)%(2**32)
        j=int((state/(2**32))*(i+1))
        candidates[i],candidates[j]=candidates[j],candidates[i]
    added=candidates[:extra]
    for u,v in added:graph[u].add(v);graph[v].add(u)
    return graph,added

if __name__=='__main__':
    for extra in [0,2,4,8,12]:
        graph,added=network(12,extra,42)
        print('Atalhos:',extra,'arestas:',added,'métricas:',metrics(graph))
