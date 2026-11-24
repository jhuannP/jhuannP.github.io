"""Partícula sobre apoio horizontal ideal, sem atrito. SI; g=10 m/s²."""
import math

def model(m=3,right=12,left=6,v0=-2,t=2):
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) for x in (m,right,left,v0,t)) or m<=0 or right<0 or left<0 or t<0:
        raise ValueError('Massa positiva; módulos e tempo não negativos; números finitos')
    force=right-left;a=force/m;v=v0+a*t;x=v0*t+a*t*t/2
    return dict(m=m,right=right,left=left,v0=v0,t=t,force=force,a=a,v=v,x=x,normal=10*m,weight=10*m,impulse=force*t,work=force*x,delta_k=m*(v*v-v0*v0)/2,turn=-v0/a if v0*a<0 else None)

if __name__=='__main__':
    s=model();assert s['a']==2 and s['v']==2 and s['x']==0
    print(s)
