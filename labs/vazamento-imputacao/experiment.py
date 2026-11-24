"""Imputação finita em protocolo indutivo; regra de decisão fixada, sem treinamento."""
from fractions import Fraction as F


def inspect(q=8,missing_y=1):
    if type(q) is not int or not 0<=q<=10:
        raise ValueError('Atributo observado do teste inteiro de 0 a 10')
    if type(missing_y) is not int or missing_y not in (0,1):
        raise ValueError('Rótulo sintético 0 ou 1')
    train=[0,2]
    test=[q,None]
    mean_train=F(sum(train),len(train))
    observed=train+[x for x in test if x is not None]
    mean_all=F(sum(observed),len(observed))
    predict=lambda x:int(x>=2) # Regra definida antes; não é classificador treinado.
    proper=[predict(q),predict(mean_train)]
    leaked=[predict(q),predict(mean_all)]
    truth=[predict(q),missing_y]
    accuracy=lambda pred:F(sum(p==y for p,y in zip(pred,truth)),len(truth))
    return dict(mean_train=mean_train,mean_all=mean_all,
                proper_prediction=proper[1],leaked_prediction=leaked[1],
                proper_accuracy=accuracy(proper),leaked_accuracy=accuracy(leaked))


if __name__=='__main__':
    s=inspect()
    assert s['mean_train']==1 and s['mean_all']==F(10,3)
    assert s['proper_accuracy']==F(1,2) and s['leaked_accuracy']==1
    assert inspect(8,0)['leaked_accuracy']==F(1,2)
    print(s)
