"""BFS de múltiplas origens; caminho mínimo em número de arestas."""
from collections import deque

def validate(grid):
    if not isinstance(grid,(list,tuple)) or not 1<=len(grid)<=30:
        raise ValueError('De 1 a 30 linhas')
    if any(not isinstance(row,(list,tuple)) for row in grid):raise ValueError('Linhas devem ser listas ou tuplas')
    width=len(grid[0])
    if not 1<=width<=30 or any(len(row)!=width for row in grid):raise ValueError('Grade retangular com 1 a 30 colunas')
    if any(not (isinstance(x,bool) or type(x) is int and x in (0,1)) for row in grid for x in row):
        raise ValueError('Sítios bool ou inteiros 0/1')
    return tuple(tuple(row) for row in grid)

def shortest_crossing(grid):
    grid=validate(grid);height,width=len(grid),len(grid[0]);queue=deque();parent={};distance={}
    for j in range(width):
        if grid[0][j]:
            source=(0,j);queue.append(source);parent[source]=None;distance[source]=0
    expanded=0
    while queue:
        cell=queue.popleft();expanded+=1;i,j=cell
        if i==height-1:
            path=[];current=cell
            while current is not None:path.append(current);current=parent[current]
            return dict(path=tuple(reversed(path)),distance=distance[cell],
                        discovered=len(parent),expanded=expanded)
        for a,b in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            neighbor=(a,b)
            if 0<=a<height and 0<=b<width and grid[a][b] and neighbor not in parent:
                parent[neighbor]=cell;distance[neighbor]=distance[cell]+1;queue.append(neighbor)
    return dict(path=None,distance=None,discovered=len(parent),expanded=expanded)

if __name__=='__main__':
    grid=[[1,0,0],[1,1,0],[0,1,1]]
    result=shortest_crossing(grid)
    assert result['path']==((0,0),(1,0),(1,1),(2,1))
    print(result)
