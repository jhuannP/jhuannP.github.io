"""Duas cadeiras tetraédricas ideais; rastreia um substituinte R sem calcular energia."""
from math import pi,cos,sin,sqrt

def model(chair=0,site=1,up=1):
    for value,allowed in ((chair,(0,1)),(site,range(1,7)),(up,(0,1))):
        if isinstance(value,bool) or not isinstance(value,int) or value not in allowed:
            raise ValueError('Cadeira/face 0 ou 1; carbono inteiro 1 a 6')
    rho=sqrt(8/9)
    carbons=[];axial=[];equatorial=[]
    for i in range(6):
        a=i*pi/3;s=(-1)**(i+chair)
        carbons.append([rho*cos(a),rho*sin(a),s/6])
        axial.append([0,0,s])
        equatorial.append([rho*cos(a),rho*sin(a),-s/3])
    index=site-1;wanted=1 if up else -1
    kind='axial' if axial[index][2]==wanted else 'equatorial'
    direction=(axial if kind=='axial' else equatorial)[index]
    return dict(chair=chair,site=site,up=up,carbons=carbons,axial=axial,equatorial=equatorial,
                kind=kind,direction=direction,other_kind='equatorial' if kind=='axial' else 'axial',
                axial_up=[i+1 for i,v in enumerate(axial) if v[2]>0])

if __name__=='__main__':
    for chair in (0,1):
        m=model(chair,1,1)
        print('Cadeira',chair,'R em C1 acima:',m['kind'],'axiais acima:',m['axial_up'])
    assert model(0,1,1)['kind']=='axial'
    assert model(1,1,1)['kind']=='equatorial'
