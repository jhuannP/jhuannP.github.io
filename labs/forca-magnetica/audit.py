"""Analytic helix and audit of existing Euler; fixed synthetic SI example."""
from math import sin,cos
from numerics4 import integrate

def helix(t):
    # m=1 kg, q=2 C, Bz=4 T, r(0)=0 and v(0)=(3,0,4) m/s.
    return ((3/8*sin(8*t),3/8*(cos(8*t)-1),4*t),
            (3*cos(8*t),-3*sin(8*t),4.))

def euler_orbit():
    def rhs(t,y):
        vx,vy,vz=y[3:]
        return [vx,vy,vz,8*vy,-8*vx,0]
    # Four steps h=1/8; the physical K is 25/2 J at all times.
    return integrate(rhs,0,.5,[0,0,0,3,0,4],4,'euler')

if __name__ == "__main__":
    for t,state in euler_orbit():
        speed2=sum(x*x for x in state[3:])
        print("t, Euler kinetic energy, physical reference:",t,speed2/2,25/2)
