"""Original tensile, axial, quasistatic linear bars; SI rational inputs."""
from fractions import Fraction as F


def real(x):
    if type(x) not in (int,F):raise ValueError('int/Fraction required')
    return F(x)


def element(length,area,young):
    length,area,young=map(real,(length,area,young))
    if min(length,area,young)<=0:raise ValueError('L,A,E>0')
    return (length,area,young)


def elements(values):
    if not isinstance(values,(tuple,list)) or not 1<=len(values)<=64:raise ValueError('1..64 elements')
    result=[]
    for item in values:
        if not isinstance(item,(tuple,list)) or len(item)!=3:raise ValueError('each element is (L,A,E)')
        result.append(element(*item))
    return result


def bar(force,length,area,young):
    force=real(force);length,area,young=element(length,area,young)
    if force<0:raise ValueError('tensile force>=0; buckling/compression not modelled')
    stress=force/area;strain=stress/young;extension=strain*length;stiffness=young*area/length
    return dict(stress=stress,strain=strain,extension=extension,stiffness=stiffness,energy=force*extension/2)


def series(force,parts):
    parts=elements(parts);items=[bar(force,*item) for item in parts]
    compliance=sum(L/(A*E) for L,A,E in parts)
    extension=sum(x['extension'] for x in items)
    return dict(extension=extension,stiffness=1/compliance,energy=sum(x['energy'] for x in items),elements=items)


def parallel(force,parts):
    force=real(force);parts=elements(parts)
    if force<0:raise ValueError('tensile force>=0')
    ks=[A*E/L for L,A,E in parts];stiffness=sum(ks);extension=force/stiffness
    forces=tuple(k*extension for k in ks)
    return dict(extension=extension,stiffness=stiffness,forces=forces,energy=sum(k*extension*extension/2 for k in ks))


if __name__=='__main__':
    E=40*10**9;parts=[(1,F(2,10**6),E),(1,F(4,10**6),E)]
    print('Prescribed E=40GPa; F=120N. Series:',series(120,parts))
    print('Same segments, parallel:',parallel(120,parts))
    print('No measured material, yield limit or real structural design is inferred.')
