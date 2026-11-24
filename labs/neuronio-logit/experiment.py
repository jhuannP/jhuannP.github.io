"""Uma unidade logística e uma atualização, sem framework ou avaliação externa."""
import math

def real(x):
    if type(x) not in (int,float) or not math.isfinite(x):raise ValueError("Real finito necessário")
    return float(x)

def sigmoid(z):
    z=real(z)
    if z>=0:return 1/(1+math.exp(-z))
    e=math.exp(z)
    return e/(1+e)

def bce_logit(z,y):
    z=real(z)
    if type(y) is not int or y not in (0,1):raise ValueError("Rótulo deve ser inteiro 0 ou 1")
    return max(z,0)-y*z+math.log1p(math.exp(-abs(z)))

def affine(x,w,b):
    if not isinstance(x,(list,tuple)) or not isinstance(w,(list,tuple)) or not x or len(x)!=len(w):
        raise ValueError("Vetores não vazios e de mesmo tamanho necessários")
    x=tuple(map(real,x));w=tuple(map(real,w));b=real(b)
    return real(sum(a*v for a,v in zip(x,w))+b)

def loss_and_grad(x,w,b,y):
    z=affine(x,w,b);loss=bce_logit(z,y);p=sigmoid(z);g=p-y
    return loss,p,tuple(real(g*v) for v in x),g

def step(x,w,b,y,eta):
    eta=real(eta)
    if eta<0:raise ValueError("Taxa deve ser não negativa")
    _,_,gw,gb=loss_and_grad(x,w,b,y)
    return tuple(real(v-eta*g) for v,g in zip(w,gw)),real(b-eta*gb)

if __name__ == "__main__":
    x,w,b,y=(2,1),(1,-1),-1,1
    print("Antes:",loss_and_grad(x,w,b,y))
    new_w,new_b=step(x,w,b,y,.2)
    print("Pesos e viés novos:",new_w,new_b)
    print("Depois:",loss_and_grad(x,new_w,new_b,y))
