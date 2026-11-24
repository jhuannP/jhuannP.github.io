"""Mesma parábola, parametrizações diferentes; referências racionais."""
from fractions import Fraction as Q


def state(mode,t):
    if isinstance(mode,bool) or mode not in (0,1,2):raise ValueError('Modo 0, 1 ou 2.')
    if isinstance(t,bool) or not isinstance(t,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    t=Q(t)
    if mode==0:s,ds,dds=t,Q(1),Q(0)
    elif mode==1:s,ds,dds=t**3,3*t*t,6*t
    else:s,ds,dds=-t,Q(-1),Q(0)
    position=(s,s*s,Q(0))
    velocity=(ds,2*s*ds,Q(0))
    acceleration=(dds,2*ds*ds+2*s*dds,Q(0))
    return dict(position=position,velocity=velocity,acceleration=acceleration,
                speed_squared=sum(v*v for v in velocity),regular=any(velocity))


if __name__=='__main__':
    for mode in range(3):
        for t in (Q(0),Q(1,2),Q(1)):
            print('Modo',mode,'parâmetro',t,state(mode,t))
    print('O caminho y=x², z=0 é o mesmo para t em [-1,1].')
    print('No modo t³, derivada zero em t=0 impede normalizar o vetor tangente ali.')
    print('Isso não elimina a tangente geométrica da parábola, obtida por outra parametrização.')
