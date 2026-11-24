"""Lateral cilíndrica em um quadrado: derivadas e quadratura didática."""
from math import sin,cos,pi,sqrt,isfinite

def _real(x,low,high):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not low<=x<=high:
        raise ValueError('Parâmetro fora do domínio didático.')
    return float(x)

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def chart(u,v,radius=2,height=3,twist=0,turns=1,direction=1):
    u,v=(_real(x,0,1) for x in (u,v))
    r,h=(_real(x,1e-6,1e4) for x in (radius,height))
    b=_real(twist,-100,100)
    if isinstance(turns,bool) or not isinstance(turns,int) or not 1<=turns<=8:
        raise ValueError('Uma a oito voltas inteiras.')
    if isinstance(direction,bool) or direction not in (-1,1):raise ValueError('Sentido ±1.')
    omega=direction*2*pi*turns
    theta=omega*u+b*v
    point=(r*cos(theta),r*sin(theta),h*v)
    du=(-omega*r*sin(theta),omega*r*cos(theta),0)
    dv=(-b*r*sin(theta),b*r*cos(theta),h)
    return point,du,dv

def integrate(radius=2,height=3,twist=0,turns=1,direction=1,kappa=1,n=12):
    k=_real(kappa,-1e4,1e4)
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=128:raise ValueError('Malha1–128.')
    area=flux=0.
    for i in range(n):
        for j in range(n):
            point,du,dv=chart((i+.5)/n,(j+.5)/n,radius,height,twist,turns,direction)
            normal=cross(du,dv)
            area+=sqrt(sum(x*x for x in normal))/n**2
            field=(k*point[0],k*point[1],0)
            flux+=sum(a*b for a,b in zip(field,normal))/n**2
    return dict(parameter_area_m2=area,induced_flux_m3_s=flux)

if __name__=='__main__':
    for turns,direction in [(1,1),(1,-1),(2,1)]:
        print(turns,direction,integrate(twist=5,turns=turns,direction=direction))
