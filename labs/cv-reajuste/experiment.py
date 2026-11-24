"""CV didática com aritmética racional; sem avaliação externa ou pacote de ML."""
from fractions import Fraction as Q
DATA=((-3,-5),(-2,-3),(-1,-1),(1,3),(2,5),(3,11))
FOLDS=((0,5),(1,4),(2,3))

def dataset(rows):
    if not isinstance(rows,(tuple,list)) or len(rows)<2:raise ValueError("Ao menos dois registros")
    out=[]
    for row in rows:
        if not isinstance(row,(tuple,list)) or len(row)!=2 or any(type(x) not in (int,Q) for x in row):
            raise ValueError("Pares (x,y) int/Fraction")
        out.append(tuple(map(Q,row)))
    return out

def fit(rows,lam=0):
    rows=dataset(rows)
    if type(lam) not in (int,Q) or lam<0:raise ValueError("Penalidade racional não negativa")
    n=len(rows);mx=sum(x for x,y in rows)/n;my=sum(y for x,y in rows)/n
    den=sum((x-mx)**2 for x,y in rows)+lam
    if den==0:raise ValueError("Inclinação não identificável sem penalidade")
    b=sum((x-mx)*(y-my) for x,y in rows)/den
    return dict(a=my-b*mx,b=b)

def crossvalidate(rows,folds,lam=0):
    rows=dataset(rows);n=len(rows)
    if not isinstance(folds,(tuple,list)) or len(folds)<2 or any(not isinstance(f,(tuple,list)) or not f for f in folds):
        raise ValueError("Ao menos dois blocos não vazios")
    ids=[i for f in folds for i in f]
    if any(type(i) is not int for i in ids) or sorted(ids)!=list(range(n)):
        raise ValueError("Cada índice deve validar exatamente uma vez")
    results=[];errors=[]
    for k,validation in enumerate(folds):
        train=[i for i in range(n) if i not in validation]
        f=fit([rows[i] for i in train],lam)
        preds=[f['a']+f['b']*rows[i][0] for i in validation]
        error2=[(pred-rows[i][1])**2 for i,pred in zip(validation,preds)]
        errors.extend(error2)
        results.append(dict(fold=k,train=train,validation=list(validation),fit=f,predictions=preds,error2=error2,mse=sum(error2)/len(error2)))
    return dict(folds=results,mse=sum(errors)/n,fold_mean=sum(z['mse'] for z in results)/len(results))

def choose(rows,folds,candidates=(0,1,4,16)):
    if not isinstance(candidates,(tuple,list)) or not candidates:raise ValueError("Candidatos não vazios")
    scores=[(lam,crossvalidate(rows,folds,lam)['mse']) for lam in candidates]
    lam,score=min(scores,key=lambda item:(item[1],item[0]))
    return dict(lam=lam,selection_mse=score,refit=fit(rows,lam),scores=scores)

if __name__=='__main__':
    s=crossvalidate(DATA,FOLDS)
    assert s['mse']==Q(49234,12675)
    assert choose(DATA,FOLDS)['lam']==0
    print(s);print(choose(DATA,FOLDS))
