"""Coordenadas transformadas de tabelas sintéticas; não ajusta nem valida modelos."""
import math

def positive(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<=0:
        raise ValueError("valor positivo finito necessário")
    return x

def log_ratio(value, reference=1.0, base=math.e):
    positive(value); positive(reference); positive(base)
    if base==1: raise ValueError("base deve diferir de 1")
    # Diferença evita overflow da divisão de dois valores finitos.
    return (math.log(value)-math.log(reference))/math.log(base)

def coordinates(points, mode, xref=1.0, yref=1.0, base=math.e):
    if mode not in ("linear","monolog","dilog"): raise ValueError("escala desconhecida")
    positive(xref); positive(yref); positive(base)
    if base==1: raise ValueError("base inválida")
    out=[]
    for x,y in points:
        if any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) for v in (x,y)):
            raise ValueError("coordenada finita necessária")
        X=log_ratio(x,xref,base) if mode=="dilog" else x
        Y=log_ratio(y,yref,base) if mode!="linear" else y
        out.append((X,Y))
    return out

def secants(points):
    if len(points)<2: raise ValueError("ao menos dois pontos")
    slopes=[]
    for (x0,y0),(x1,y1) in zip(points,points[1:]):
        if x1==x0: raise ValueError("abscissas consecutivas distintas")
        slopes.append((y1-y0)/(x1-x0))
    return slopes

if __name__=="__main__":
    exp=[(t,64*2**(-t/2)) for t in (0,2,4,6)]
    power=[(x,3*x*x) for x in (1,2,4,8)]
    background=[(t,y+5) for t,y in exp]
    for name,points,mode in (("exponencial",exp,"monolog"),("potência",power,"dilog"),("com fundo",background,"monolog")):
        print(name, points, secants(coordinates(points,mode)))
