"""Duas molas passivas em série, em equilíbrio estático.
k:nN/um, deslocamento:um, força:nN, energia:nN um = fJ.
Analogia mecânica; não calcula sinalização, ocupação ou destino celular.
"""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def stiffness(k_matrix,k_cell):
    a,b=map(rational,(k_matrix,k_cell))
    if min(a,b)<=0:raise ValueError("Rigidezes positivas necessárias.")
    return a,b

def package(km,kc,force):
    xm,xc=force/km,force/kc
    return dict(force=force,matrix_extension=xm,cell_extension=xc,total_extension=xm+xc,
                matrix_energy=km*xm*xm/2,cell_energy=kc*xc*xc/2,
                total_energy=force*(xm+xc)/2,effective_stiffness=km*kc/(km+kc))

def fixed_displacement(k_matrix,k_cell,delta):
    km,kc=stiffness(k_matrix,k_cell);delta=rational(delta)
    if delta<0:raise ValueError("Deslocamento imposto não negativo necessário.")
    force=delta/(1/km+1/kc)
    return package(km,kc,force)

def fixed_force(k_matrix,k_cell,force):
    km,kc=stiffness(k_matrix,k_cell);force=rational(force)
    if force<0:raise ValueError("Força imposta não negativa necessária.")
    return package(km,kc,force)

if __name__=='__main__':
    print(fixed_displacement(2,2,2));print(fixed_displacement(8,2,2))
    print(fixed_force(8,2,2))
