"""Modelos prescritos de massa invariante constante; sem gravitação."""
import math

def finite(x):
    if isinstance(x,bool) or not isinstance(x,(float,int)) or not math.isfinite(x):
        raise ValueError("número finito necessário")
    return x

def trajectory(q):
    finite(q)
    if not 0<=q<=10000: raise ValueError("q no intervalo didático [0,10000]")
    g=math.hypot(1,q)
    return {"q":q,"gamma":g,"beta":q/g,"X":q*q/(g+1),"A":1/g**3}

def acceleration(beta,force,mass):
    # beta=v/c; force e mass em unidades coerentes. Retorno em force/mass.
    finite(mass)
    if mass<=0 or len(beta)!=3 or len(force)!=3: raise ValueError("massa positiva e vetores 3D")
    for x in (*beta,*force): finite(x)
    b2=sum(x*x for x in beta)
    if b2>=1: raise ValueError("velocidade subluminal necessária")
    g=1/math.sqrt(1-b2);dot=sum(x*y for x,y in zip(beta,force))
    return tuple((f-dot*b)/(g*mass) for f,b in zip(force,beta))

if __name__=="__main__":
    for q in (0,3/4,4/3): print(trajectory(q))
    print("Com beta=(0.6,0,0), F=(1,1,0), m=1:", acceleration((0.6,0,0),(1,1,0),1))
    print("q=Ft/(mc); X=Fx/(mc²); A=ma/F. Números são do modelo, não medições.")
