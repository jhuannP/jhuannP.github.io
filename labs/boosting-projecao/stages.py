"""Auditoria racional de boosting quadrático, reutilizando o stump existente."""
from fractions import Fraction as Q
from importlib import import_module
STUMP=import_module('labs.stump-regressao.stump')

def fit(x,y,rounds=5,eta=Q(1,2)):
    x=tuple(map(STUMP.rational,x));y=tuple(map(STUMP.rational,y))
    eta=STUMP.rational(eta)
    if not x or len(x)!=len(y) or len(x)>100:raise ValueError('De 1 a 100 pares necessários')
    if type(rounds) is not int or not 0<=rounds<=50:raise ValueError('De 0 a 50 rodadas')
    if not 0<eta<=1:raise ValueError('Passo entre 0 exclusivo e 1 inclusivo')
    base=sum(y,Q(0))/len(y);pred=(base,)*len(y);trees=[];history=[]
    def record():
        r=tuple(a-b for a,b in zip(y,pred))
        history.append(dict(pred=pred,residual=r,mse=sum(v*v for v in r)/len(r)))
    record()
    for _ in range(rounds):
        tree=STUMP.fit(x,history[-1]['residual']);trees.append(tree)
        correction=tuple(STUMP.predict(tree,v) for v in x)
        pred=tuple(a+eta*b for a,b in zip(pred,correction));record()
    return dict(base=base,eta=eta,trees=trees,history=history)

def predict(model,x,rounds=None):
    x=STUMP.rational(x)
    if rounds is None:rounds=len(model['trees'])
    if type(rounds) is not int or not 0<=rounds<=len(model['trees']):raise ValueError('Rodada inexistente')
    return model['base']+model['eta']*sum((STUMP.predict(t,x) for t in model['trees'][:rounds]),Q(0))

if __name__=='__main__':
    m=fit([0,1,2,3],[0,0,2,2])
    for k,state in enumerate(m['history']):
        print(k,'MSE treino:',state['mse'],'erro no ponto reservado:',(predict(m,Q(3,2),k)-1)**2)
