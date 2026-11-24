"""Parede retangular vertical desde a superfície; SI, g=10 m/s²."""
from math import isfinite

def model(rho=1000,height=2,width=1,p0=100,probe=1):
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) for x in (rho,height,width,p0,probe)) or not (500<=rho<=1500 and 0<=height<=4 and .5<=width<=3 and 80<=p0<=120 and 0<=probe<=1):
        raise ValueError('Parâmetros fora do painel')
    z=probe*height;dp=rho*10*z;area=width*height;net=rho*10*width*height**2/2
    return dict(rho=rho,height=height,width=width,p0=p0,probe=probe,z=z,dp=dp,absolute=1000*p0+dp,area=area,net=net,one_side=1000*p0*area+net,center=2*height/3 if height else None)

if __name__=='__main__':
    s=model();assert s['dp']==20000 and s['net']==20000
    print(s)
