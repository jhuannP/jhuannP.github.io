"""Tabela sintética de movimento com força resultante constante; não experimento."""
from fractions import Fraction as F

def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):raise TypeError('Use inteiro ou Fraction.')
    x=F(x)
    if abs(x)>10**4:raise ValueError('Magnitude didática até dez mil.')
    return x

def table(mass,force,v0,dt=1,steps=3):
    mass,force,v0,dt=map(number,(mass,force,v0,dt))
    if mass<=0 or dt<=0:raise ValueError('Massa e intervalo positivos.')
    if isinstance(steps,bool) or not isinstance(steps,int):raise TypeError('Número inteiro de intervalos.')
    if not 0<=steps<=100:raise ValueError('Use 0–100 intervalos.')
    a=force/mass;rows=[]
    for k in range(steps+1):
        t=k*dt;v=v0+a*t;x=v0*t+a*t*t/2
        rows.append({'t_s':t,'x_m':x,'v_m_s':v,'a_m_s2':a})
    return tuple(rows)

if __name__=='__main__':
    for force in (0,2):
        print('DADOS SINTÉTICOS: massa2kg, força resultante horizontal',force,'N')
        for row in table(2,force,3):print(row)
    assert table(2,0,3)[-1]['x_m']==9
    assert table(2,2,3)[-1]['x_m']==F(27,2)
    print('Resultados calculados, não medidos. Não validam as leis usadas para gerá-los.')
