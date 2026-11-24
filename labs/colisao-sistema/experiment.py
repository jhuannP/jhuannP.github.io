"""Balanço exato antes/depois de adesão 1D; sem simular contato ou duração."""
from fractions import Fraction as Q

def stick(m1,m2,u1,u2):
    values=(m1,m2,u1,u2)
    if any(type(x) not in (int,Q) for x in values) or m1<=0 or m2<=0:
        raise ValueError("Massas positivas e valores int/Fraction; bool não é valor")
    m1,m2,u1,u2=map(Q,values)
    mass=m1+m2
    momentum=m1*u1+m2*u2
    v=momentum/mass
    ki=(m1*u1*u1+m2*u2*u2)/2
    kf=mass*v*v/2
    return dict(v=v,p_before=momentum,p_after=mass*v,
                k_before=ki,k_after=kf,loss=ki-kf,
                impulse1=m1*(v-u1),impulse2=m2*(v-u2))

if __name__ == "__main__":
    r=stick(1,1,4,0)
    assert r["v"]==2 and r["loss"]==4
    print("Exemplo da aula:",r)
    print("Massas iguais e velocidades opostas:",stick(1,1,3,-3))
