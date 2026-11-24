"""p-valores normais e covariância racional, sem dados reais."""
from fractions import Fraction as Q
from math import erfc, sqrt, isfinite


def normal_pvalue(z, side='two-sided'):
    if isinstance(z, bool) or not isinstance(z, (int, float)) or not isfinite(z):
        raise ValueError('z real finito')
    if side == 'two-sided': return erfc(abs(z)/sqrt(2))
    if side == 'right': return .5*erfc(z/sqrt(2))
    if side == 'left': return .5*erfc(-z/sqrt(2))
    raise ValueError('Use two-sided, right ou left')


def joint_moments(xs, ys, weights):
    if not len(xs) == len(ys) == len(weights) or not 1 <= len(xs) <= 1000:
        raise ValueError('Listas de mesmo tamanho entre 1 e 1000')
    if any(isinstance(x, bool) or not isinstance(x, (int, Q)) for x in list(xs)+list(ys)+list(weights)):
        raise ValueError('Use int ou Fraction')
    xs, ys, weights = list(map(Q,xs)), list(map(Q,ys)), list(map(Q,weights))
    if any(w<0 for w in weights) or sum(weights)!=1:
        raise ValueError('Pesos não negativos com soma 1')
    mx = sum(x*w for x,w in zip(xs,weights)); my = sum(y*w for y,w in zip(ys,weights))
    vx = sum((x-mx)**2*w for x,w in zip(xs,weights))
    vy = sum((y-my)**2*w for y,w in zip(ys,weights))
    cov = sum((x-mx)*(y-my)*w for x,y,w in zip(xs,ys,weights))
    rho = None if vx==0 or vy==0 else float(cov)/sqrt(float(vx*vy))
    return dict(mean_x=mx, mean_y=my, variance_x=vx, variance_y=vy,covariance=cov,correlation=rho)


if __name__ == '__main__':
    assert normal_pvalue(0)==1 and normal_pvalue(0,'right')==.5
    assert abs(normal_pvalue(2)-.04550026389635842)<1e-12
    print('z=2: p bilateral=',normal_pvalue(2),'p à direita=',normal_pvalue(2,'right'))
    xs=[-2,-1,0,1,2]; ys=[x*x for x in xs]; weights=[Q(1,5)]*5
    r=joint_moments(xs,ys,weights)
    assert r['covariance']==0 and r['correlation']==0
    assert Q(1,5)!=Q(1,5)*Q(1,5)  # P(X=0,Y=0) não é P(X=0)P(Y=0).
    print('Y=X²: covariância zero com dependência:',r)
    constant=joint_moments(xs,[3]*5,weights)
    assert constant['correlation'] is None
    print('Y constante: correlação indefinida, não zero:',constant)
