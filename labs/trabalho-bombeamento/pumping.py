"""Cone ideal: raio(y)=c*y, vértice no fundo, y medido em metros.
Retorna fatores de pi: volume m³, peso N, trabalho J. Densidade/peso uniformes.
Não modela bomba real, perda de carga ou potência de equipamento.
"""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def layer(height,c,outlet,y0,y1,weight_density=10000):
    height,c,outlet,y0,y1,weight_density=map(rational,(height,c,outlet,y0,y1,weight_density))
    if height<=0 or c<=0 or weight_density<=0 or not 0<=y0<=y1<=height or outlet<height:raise ValueError("Domínio geométrico inválido.")
    volume=c*c*(y1**3-y0**3)/3
    first_moment=c*c*(y1**4-y0**4)/4
    work=weight_density*(outlet*volume-first_moment)
    return dict(volume_pi=volume,weight_pi=weight_density*volume,
                centroid=None if volume==0 else first_moment/volume,work_pi=work)

def full_riemann(n):
    # Apenas o exemplo H4,c1/2,outlet6,gamma10000; f crescente nesse intervalo.
    if type(n) is not int or not 1<=n<=4096:raise ValueError("Inteiro1..4096 necessário.")
    step=Q(4,n)
    f=lambda y:2500*y*y*(6-y)
    lower=step*sum((f(i*step) for i in range(n)),Q(0))
    upper=step*sum((f(i*step) for i in range(1,n+1)),Q(0))
    return lower,upper

if __name__=='__main__':
    print(layer(4,Q(1,2),6,0,4));print(layer(4,Q(1,2),6,2,4));print(full_riemann(4))
