"""Parâmetros manuais e cinco dados fictícios de inspeção; não há treino/teste final."""
import math
X=(-2.,-1.,0.,1.,2.)
Y=(0,1,0,1,1)

def probability(z):
    if not math.isfinite(z):raise ValueError('Logit finito necessário.')
    if z>=0:return 1/(1+math.exp(-z))
    e=math.exp(z);return e/(1+e)

def binary_loss(z,y):
    if not math.isfinite(z) or y not in (0,1):raise ValueError('Logit finito e y binário.')
    return max(z if y==0 else -z,0)+math.log1p(math.exp(-abs(z)))

def decide(z,threshold):
    if not math.isfinite(z) or not math.isfinite(threshold) or not 0<=threshold<=1:raise ValueError('Limiar 0..1 e logit finito.')
    if threshold==0:return 1
    if threshold==1:return 0
    return int(z>=math.log(threshold)-math.log1p(-threshold))

def inspect(w=1.,b=0.,x=0.,threshold=.5):
    if not all(math.isfinite(t) for t in (w,b,x,threshold)) or not -4<=w<=4 or not -3<=b<=3 or not -2<=x<=2 or not 0<=threshold<=1:
        raise ValueError('Parâmetros fora da janela didática.')
    rows=[];counts=dict(TN=0,FP=0,FN=0,TP=0);errors=[]
    for a,y in zip(X,Y):
        z=w*a+b;p=probability(z);decision=decide(z,threshold)
        counts[('TN','FP','FN','TP')[2*y+decision]]+=1
        rows.append(dict(x=a,y=y,z=z,p=p,decision=decision))
        errors.append(p if y==0 else -probability(-z))
    boundary=(math.log(threshold)-math.log1p(-threshold)-b)/w if w and 0<threshold<1 else None
    return dict(w=w,b=b,x=x,threshold=threshold,z=w*x+b,p=probability(w*x+b),decision=decide(w*x+b,threshold),rows=rows,
                counts=counts,precision=counts['TP']/(counts['TP']+counts['FP']) if counts['TP']+counts['FP'] else None,
                recall=counts['TP']/sum(Y),accuracy=(counts['TP']+counts['TN'])/len(Y),
                loss=sum(binary_loss(row['z'],row['y']) for row in rows)/len(rows),
                gradient=[sum(e*a for e,a in zip(errors,X))/len(X),sum(errors)/len(X)],boundary=boundary)

if __name__=='__main__':
    s=inspect();assert s['counts']==dict(TN=1,FP=1,FN=1,TP=2)
    print(s)
