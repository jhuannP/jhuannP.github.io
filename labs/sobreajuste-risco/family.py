"""Família sintética f_a=x²+a(x³−x), riscos e seleção prescritos."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError('use int ou Fraction')
    return Q(x)

def predict(x,a):
    x,a=map(rational,(x,a))
    return x*x+a*(x*x*x-x)

def mse(a,samples):
    a=rational(a); samples=tuple(samples)
    if not 1<=len(samples)<=1000: raise ValueError('1..1000 pontos')
    losses=[]
    for row in samples:
        if len(row)!=2: raise ValueError('par x,y')
        x,y=map(rational,row)
        losses.append((predict(x,a)-y)**2)
    return sum(losses)/len(losses)

def select(candidates,validation):
    """Menor MSE de validação; primeiro candidato em empate.
    Não confere a procedência dos dados nem os congela por conta própria.
    """
    candidates=tuple(map(rational,candidates)); validation=tuple(validation)
    if not 1<=len(candidates)<=1000:raise ValueError('1..1000 candidatos')
    return min(candidates,key=lambda a:mse(a,validation))

def uniform_risk(a,truth_b=0):
    """Risco exato para X uniforme[-1,1],Y=f_b(X), sem ruído.
    Referência oracular conhecida neste modelo, não estimativa de teste.
    """
    delta=rational(a)-rational(truth_b)
    return delta**2 * (Q(1,7)-Q(2,5)+Q(1,3))

if __name__=='__main__':
    train=tuple((Q(x),Q(x*x)) for x in (-1,0,1))
    validation=tuple((x,x*x) for x in (Q(-1,2),Q(1,2)))
    for a in (0,2,4):
        print('a=',a,'treino=',mse(a,train),'validação=',mse(a,validation),
              'risco uniforme=',uniform_risk(a))
    print('escolha validação=',select((0,2,4),validation))
