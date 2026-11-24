"""Exhaustive conditional bootstrap of a previously verified regression stump."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec

_spec=spec_from_file_location("portfolio_regression_stump",Path(__file__).resolve().parents[1]/"stump-regressao"/"stump.py")
_stump=module_from_spec(_spec);_spec.loader.exec_module(_stump)
fit,predict=_stump.fit,_stump.predict

def rational(x):
    if type(x) not in (int,Q):raise ValueError("use int or Fraction")
    return Q(x)

def bootstrap_models(x,y):
    x=tuple(map(rational,x));y=tuple(map(rational,y))
    if len(x)!=len(y) or not 1<=len(x)<=4:
        raise ValueError("1..4 matched training pairs in this exhaustive routine")
    n=len(x)
    return tuple((ids,fit([x[i] for i in ids],[y[i] for i in ids]))
                 for ids in product(range(n),repeat=n))

def distribution(models,query):
    query=rational(query)
    return Counter(predict(model,query) for ids,model in models)

def mean_variance(counts):
    total=sum(counts.values())
    if total<=0:raise ValueError("nonempty empirical distribution required")
    mean=sum((rational(x)*w for x,w in counts.items()),Q(0))/total
    var=sum((w*(rational(x)-mean)**2 for x,w in counts.items()),Q(0))/total
    return mean,var

def oob_predictions(models,x):
    """Per original training index: (mean_prediction or None, eligible_models)."""
    result=[]
    for i,value in enumerate(x):
        value=rational(value)
        predictions=[predict(m,value) for ids,m in models if i not in ids]
        result.append((sum(predictions,Q(0))/len(predictions) if predictions else None,len(predictions)))
    return tuple(result)

def variance_factor(size,rho):
    """Exchangeable equal-variance predictors; illustrative nonnegative correlation."""
    if type(size) is not int or size<1:raise ValueError("positive integer ensemble size")
    rho=rational(rho)
    if not 0<=rho<=1:raise ValueError("this illustration assumes 0<=rho<=1")
    return rho+(1-rho)/size

if __name__=='__main__':
    x=(0,1,2);y=(0,2,0);models=bootstrap_models(x,y)
    counts=distribution(models,1)
    print("conditional bootstrap distribution",sorted(counts.items()))
    print("conditional mean / variance",mean_variance(counts))
    print("OOB means and counts",oob_predictions(models,x))
    oob=oob_predictions(models,x)
    print("OOB MSE",sum((pred-Q(target))**2 for (pred,n),target in zip(oob,y))/len(y))
