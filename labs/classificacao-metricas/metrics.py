"""Métricas binárias exatas para exemplos sintéticos; não calibra scores."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def labels(values):
    values=tuple(values)
    if not values or any(type(v) is not int or v not in (0,1) for v in values):raise ValueError("Classes inteiras 0/1 não vazias necessárias.")
    return values

def ratio(a,b):return Q(a,b) if b else None

def metrics(y,pred):
    y,pred=labels(y),labels(pred)
    if len(y)!=len(pred):raise ValueError("Tamanhos iguais necessários.")
    counts={key:0 for key in ('TP','FP','FN','TN')}
    for actual,decision in zip(y,pred):
        key=('TP' if decision else 'FN') if actual else ('FP' if decision else 'TN')
        counts[key]+=1
    tp,fp,fn,tn=(counts[k] for k in ('TP','FP','FN','TN'))
    recall=ratio(tp,tp+fn);specificity=ratio(tn,tn+fp)
    return dict(counts,accuracy=Q(tp+tn,len(y)),precision=ratio(tp,tp+fp),recall=recall,
                specificity=specificity,f1=ratio(2*tp,2*tp+fp+fn),
                balanced_accuracy=None if recall is None or specificity is None else (recall+specificity)/2)

def threshold(y,scores,t):
    y=labels(y);scores=tuple(map(rational,scores));t=rational(t)
    if len(y)!=len(scores):raise ValueError("Tamanhos iguais necessários.")
    if any(not 0<=s<=1 for s in scores):raise ValueError("Scores didáticos em [0,1] necessários.")
    return metrics(y,[int(s>=t) for s in scores])

def empirical_cost(result,c_fp,c_fn):
    c_fp,c_fn=map(rational,(c_fp,c_fn))
    if min(c_fp,c_fn)<0:raise ValueError("Custos não negativos necessários.")
    if not isinstance(result,dict) or any(type(result.get(k)) is not int or result[k]<0 for k in ('TP','FP','FN','TN')):raise ValueError("Contagens necessárias.")
    return c_fp*result['FP']+c_fn*result['FN']

def predictive_precision(prevalence,tpr,fpr):
    prevalence,tpr,fpr=map(rational,(prevalence,tpr,fpr))
    if any(not 0<=v<=1 for v in (prevalence,tpr,fpr)):raise ValueError("Probabilidades em [0,1] necessárias.")
    numerator=prevalence*tpr;denominator=numerator+(1-prevalence)*fpr
    return numerator/denominator if denominator else None

if __name__=='__main__':
    y=[1,0,1,0,1,0,0,0];s=[Q(i,10) for i in [9,8,7,6,4,3,2,1]]
    for t in [Q(9,10),Q(7,10),Q(1,2),Q(2,5)]:
        r=threshold(y,s,t);print(t,r,empirical_cost(r,1,4))
