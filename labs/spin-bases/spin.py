"""Spin1/2 ideal, bases x/y/z, Born e atualização projetiva assumidas.
Amplitudes complexas em float; não modela aparelho, dinâmica espacial ou ruído.
"""
from math import sqrt,isfinite,isclose
ROOT=sqrt(2)
BASES={'z':((1+0j,0j),(0j,1+0j)),
       'x':((1/ROOT,1/ROOT),(1/ROOT,-1/ROOT)),
       'y':((1/ROOT,1j/ROOT),(1/ROOT,-1j/ROOT))}

def state(values):
    raw=tuple(values)
    if len(raw)!=2 or any(isinstance(v,bool) for v in raw):raise ValueError("Duas amplitudes complexas necessárias.")
    try:values=tuple(complex(v) for v in raw)
    except (TypeError,ValueError,OverflowError):raise ValueError("Amplitudes finitas necessárias.") from None
    if not all(isfinite(v.real) and isfinite(v.imag) for v in values):raise ValueError("Amplitudes finitas necessárias.")
    try:norm=sum(abs(v)**2 for v in values)
    except OverflowError:raise ValueError("Norma fora da resolução numérica.") from None
    if not isclose(norm,1,rel_tol=0,abs_tol=1e-12):raise ValueError("Estado deve estar normalizado.")
    return values

def basis(axis):
    if not isinstance(axis,str) or axis not in BASES:raise ValueError("Eixo x,y,z necessário.")
    return BASES[axis]

def inner(u,v):return sum(a.conjugate()*b for a,b in zip(u,v))

def amplitudes(psi,axis):
    psi=state(psi)
    return tuple(inner(v,psi) for v in basis(axis))

def probabilities(psi,axis):return tuple(abs(a)**2 for a in amplitudes(psi,axis))

def project(psi,axis,outcome):
    if type(outcome) is not int or outcome not in (0,1):raise ValueError("Resultado0(+) ou1(-) necessário.")
    amp=amplitudes(psi,axis)[outcome];p=abs(amp)**2
    if p==0:return p,None
    vector=basis(axis)[outcome]
    post=tuple(v*amp/sqrt(p) for v in vector)
    return p,state(post)

def nonselective_probability(psi,first_axis,last_axis):
    total=[0.,0.]
    for outcome in (0,1):
        p,post=project(psi,first_axis,outcome)
        if post is None:continue
        for j,v in enumerate(probabilities(post,last_axis)):total[j]+=p*v
    return tuple(total)

if __name__=='__main__':
    psi=(sqrt(3)/2,.5j)
    for axis in 'xyz':print(axis,probabilities(psi,axis))
    print(nonselective_probability((1,0),'x','z'))
