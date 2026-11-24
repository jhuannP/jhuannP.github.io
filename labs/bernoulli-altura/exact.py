"""Duas seções de um modelo ideal, uniforme em cada seção, com SI racional."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction; sem float/bool")
    return Q(x)

def sections(*,A1,A2,v1,rho,g,z1,z2,p1):
    A1,A2,v1,rho,g,z1,z2,p1=map(rational,(A1,A2,v1,rho,g,z1,z2,p1))
    if min(A1,A2,rho,g)<=0 or v1<0:
        raise ValueError("Áreas, densidade e g positivos; rapidez inicial não negativa")
    flow=A1*v1;v2=flow/A2
    kinetic=rho*(v1*v1-v2*v2)/2
    height=rho*g*(z1-z2)
    dp=kinetic+height;p2=p1+dp
    return dict(flow=flow,v2=v2,dp_kinetic=kinetic,dp_height=height,dp=dp,p2=p2,
                B1=p1+rho*v1*v1/2+rho*g*z1,
                B2=p2+rho*v2*v2/2+rho*g*z2)

if __name__=="__main__":
    result=sections(A1=Q(4,10000),A2=Q(1,10000),v1=1,rho=1000,g=10,z1=0,z2=1,p1=200000)
    for name,value in result.items():print(name,"=",value)
