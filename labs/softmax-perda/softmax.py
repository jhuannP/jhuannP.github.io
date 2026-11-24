"""Softmax e CE simples: vetores pequenos, alvo inteiro, Python padrão.
Perda calculada por logits; sem pesos, smoothing, máscaras na CE ou treino.
"""
from math import exp,log1p,isfinite

def real(x):
    if isinstance(x,bool):raise ValueError('Real finito necessário')
    try:y=float(x)
    except (TypeError,ValueError,OverflowError):raise ValueError('Real finito necessário') from None
    if not isfinite(y):raise ValueError('Real finito necessário')
    return y

def softmax(logits,mask=None):
    z=[real(v) for v in logits]
    keep=[True]*len(z) if mask is None else list(mask)
    if not z or len(keep)!=len(z) or any(not isinstance(v,bool) for v in keep) or not any(keep):raise ValueError('Máscara precisa permitir pelo menos um logit')
    top=max(v for v,k in zip(z,keep) if k);w=[exp(v-top) if k else 0 for v,k in zip(z,keep)];total=sum(w)
    return [v/total for v in w]

def cross_entropy(logits,target):
    z=[real(v) for v in logits]
    if not z or isinstance(target,bool) or not isinstance(target,int) or not 0<=target<len(z):raise ValueError('Classe alvo inválida')
    top=max(z)
    peak=z.index(top)
    tail=sum(exp(v-top) for i,v in enumerate(z) if i!=peak)
    return real((top-z[target])+log1p(tail))


def loss_gradient(logits,target):
    z=list(logits)
    loss=cross_entropy(z,target)
    probabilities=softmax(z)
    return loss,[v-int(i==target) for i,v in enumerate(probabilities)]

def batch_loss_gradient(rows,targets,reduction='mean'):
    rows=[list(row) for row in rows];targets=list(targets)
    if not rows or len(rows)!=len(targets) or not rows[0] or any(len(r)!=len(rows[0]) for r in rows):
        raise ValueError("Batch retangular não vazio e um alvo por linha.")
    if reduction not in ('mean','sum'):raise ValueError("Redução mean ou sum.")
    values=[loss_gradient(row,t) for row,t in zip(rows,targets)]
    scale=1/len(rows) if reduction=='mean' else 1
    loss=real(sum(v[0] for v in values)*scale)
    return loss,[[g*scale for g in grad] for _,grad in values]

if __name__=='__main__':
    from math import log
    print(loss_gradient([log(2),0,0],0))
    print('logits iguais 1e20:',cross_entropy([1e20]*3,1))
    print('alvo com probabilidade arredondada a zero:',cross_entropy([1000,0,-1000],2))
