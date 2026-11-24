"""Seis orientações de Newman no butano ideal; contagens geométricas, sem energia."""
from math import pi,cos,sin,sqrt

def model(phi=180):
    if isinstance(phi,bool) or not isinstance(phi,int) or phi not in range(0,361,60):
        raise ValueError('Ângulo inteiro múltiplo de 60, entre 0 e 360')
    angle=phi%360
    rho=sqrt(8/9)
    def vectors(turn,z):
        return [[rho*cos(pi/2+2*pi*k/3+turn),rho*sin(pi/2+2*pi*k/3+turn),z] for k in range(3)]
    front=vectors(0,-1/3);back=vectors(angle*pi/180,1/3)
    # Índice 0 é CH3; índices 1 e 2 são H em cada carbono central.
    counts={'HH':0,'MH':0,'MM':0}
    for i in range(3):
        for j in range(3):
            if (120*i-(angle+120*j))%360==0:
                kind='MM' if i==j==0 else ('HH' if i and j else 'MH')
                counts[kind]+=1
    kind='anti' if angle==180 else ('gauche' if angle in (60,300) else 'eclipsada')
    return dict(phi=phi,angle=angle,kind=kind,front=front,back=back,eclipsed=counts,
                methyl_separation=min(angle,360-angle))

if __name__=='__main__':
    for phi in range(0,361,60):
        m=model(phi)
        print(phi,m['kind'],'separação CH3:',m['methyl_separation'],'pares eclipsados:',m['eclipsed'])
