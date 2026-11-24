"""Conjunto de inteiros: inserção, busca e percursos iterativos."""

def chave_inteira(chave):
    if isinstance(chave,bool) or not isinstance(chave,int):
        raise TypeError('Esta versão usa chaves inteiras')
    return chave

class No:
    def __init__(self,chave):
        self.chave=chave_inteira(chave);self.esq=None;self.dir=None

def inserir(raiz,chave):
    chave_inteira(chave)
    if raiz is None:return No(chave)
    no=raiz
    while True:
        if chave==no.chave:return raiz
        lado='esq' if chave<no.chave else 'dir'
        proximo=getattr(no,lado)
        if proximo is None:
            setattr(no,lado,No(chave));return raiz
        no=proximo

def caminho(raiz,chave):
    chave_inteira(chave);visitados=[];no=raiz
    while no is not None:
        visitados.append(no.chave)
        if chave==no.chave:return dict(encontrada=True,visitados=visitados)
        no=no.esq if chave<no.chave else no.dir
    return dict(encontrada=False,visitados=visitados)

def contem(raiz,chave):return caminho(raiz,chave)['encontrada']

def em_ordem(raiz):
    resultado=[];pilha=[];no=raiz
    while pilha or no is not None:
        while no is not None:pilha.append(no);no=no.esq
        no=pilha.pop();resultado.append(no.chave);no=no.dir
    return resultado

def altura(raiz):
    # Altura em número de nós: vazia=0, raiz sozinha=1.
    if raiz is None:return 0
    pendentes=[(raiz,1)];maximo=0
    while pendentes:
        no,nivel=pendentes.pop();maximo=max(maximo,nivel)
        if no.esq is not None:pendentes.append((no.esq,nivel+1))
        if no.dir is not None:pendentes.append((no.dir,nivel+1))
    return maximo

def construir(chaves):
    raiz=None
    for chave in chaves:raiz=inserir(raiz,chave)
    return raiz

ORDENS=([1,2,3,4,5,6,7],[7,6,5,4,3,2,1],[4,2,6,1,3,5,7])

def report(ordem,quantidade,alvo):
    if isinstance(ordem,bool) or not isinstance(ordem,int) or not 0<=ordem<=2:raise ValueError('Ordem 0, 1 ou 2')
    if isinstance(quantidade,bool) or not isinstance(quantidade,int) or not 0<=quantidade<=7:raise ValueError('Quantidade entre 0 e 7')
    raiz=construir(ORDENS[ordem][:quantidade])
    return dict(altura=altura(raiz),em_ordem=em_ordem(raiz),**caminho(raiz,alvo))

if __name__=='__main__':
    for ordem in range(3):print(report(ordem,7,7))
    raiz=construir([4,2,6,1,3])
    assert em_ordem(raiz)==[1,2,3,4,6]
    assert caminho(raiz,3)['visitados']==[4,2,3]
