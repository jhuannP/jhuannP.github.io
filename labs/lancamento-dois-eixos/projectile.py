"""Voo racional: origem0, componentes positivas, mesma altura, sem arrasto.
Entradas SI. Estado em T é limite anterior ao impacto; não modela contato.
"""
from fractions import Fraction as Q

def positive(v):
    if type(v) not in (int,Q) or v<=0:raise ValueError('int/Fraction positivo sem bool')
    return Q(v)

def landmarks(vx,vy,g):
    vx,vy,g=map(positive,(vx,vy,g))
    return dict(top_time=vy/g,flight=2*vy/g,height=vy*vy/(2*g),range=2*vx*vy/g)

def state(t,vx,vy,g):
    vx,vy,g=map(positive,(vx,vy,g))
    if type(t) not in (int,Q) or not 0<=t<=2*vy/g:raise ValueError('tempo racional no intervalo de voo')
    t=Q(t)
    return dict(x=vx*t,y=vy*t-g*t*t/2,vx=vx,vy=vy-g*t,ax=Q(0),ay=-g)

if __name__=='__main__':
    r=landmarks(6,8,10);assert r==dict(top_time=Q(4,5),flight=Q(8,5),height=Q(16,5),range=Q(48,5))
    assert state(1,6,8,10)['y']==3 and state(1,6,8,10)['vy']==-2
    cases=0
    for vx in (Q(2),Q(6),Q(10)):
        for vy in (Q(1),Q(4),Q(8)):
            for g in (Q(5),Q(10)):
                r=landmarks(vx,vy,g);top=state(r['top_time'],vx,vy,g)
                assert top['vy']==0 and top['y']==r['height'] and top['ay']==-g
                assert state(r['flight'],vx,vy,g)['y']==0
                assert r['range']<=(vx*vx+vy*vy)/g
                for j in range(21):
                    t=r['flight']*Q(j,20);s=state(t,vx,vy,g);rev=state(r['flight']-t,vx,vy,g)
                    assert s['y']>=0
                    assert (s['vx']**2+s['vy']**2)/2+g*s['y']==(vx*vx+vy*vy)/2
                    assert rev['y']==s['y'] and rev['vy']==-s['vy'] and rev['x']==r['range']-s['x']
                    assert s['y']==vy*s['x']/vx-g*s['x']**2/(2*vx*vx)
                    cases+=1
    for call in (lambda:state(2,6,8,10),lambda:state(-1,6,8,10),lambda:landmarks(True,8,10),lambda:landmarks(6,0,10),lambda:state(.5,6,8,10)):
        try:call()
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('Exemplo:',landmarks(6,8,10),'estado em1s:',state(1,6,8,10))
    print('Energia, simetria e trajetória conferidas em',cases,'estados de18cenários.')
