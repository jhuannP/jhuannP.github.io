"""Geometria de um traçado sintético, não um modelo de atividade neural."""
from math import hypot, isfinite

def measure(points, scale):
    if isinstance(scale, bool) or not isinstance(scale, (int,float)) or not isfinite(scale) or scale <= 0:
        raise ValueError('Calibração positiva e finita, em micrometros por pixel')
    points = list(points)
    if len(points) < 2: raise ValueError('Ao menos dois pontos')
    for point in points:
        if not isinstance(point,(tuple,list)) or len(point)!=2 or any(isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) for x in point):
            raise ValueError('Pontos 2D finitos')
    length = scale*sum(hypot(b[0]-a[0],b[1]-a[1]) for a,b in zip(points, points[1:]))
    distance = scale*hypot(points[-1][0]-points[0][0],points[-1][1]-points[0][1])
    if not isfinite(length) or not isfinite(distance): raise ValueError('Fora do alcance numérico')
    return {'length':length, 'distance':distance, 'ratio':length/distance if distance else None}

def model(height=160, scale=.1, coarse=0):
    if isinstance(height,bool) or not isinstance(height,(int,float)) or not isfinite(height) or not 0<=height<=160 or type(coarse) is not int or coarse not in (0,1):
        raise ValueError('Altura entre zero e160; modo zero ou um')
    if isinstance(scale,bool) or not isinstance(scale,(int,float)) or not isfinite(scale) or not .1<=scale<=1:
        raise ValueError('Calibração do painel entre0,1 e1')
    full = [(0,0),(120,height),(240,0)]
    used = [full[0],full[-1]] if coarse else full
    result = measure(used,scale)
    result['full_length'] = measure(full,scale)['length']
    return result

if __name__ == '__main__':
    m=model();assert m['length']==40 and m['distance']==24
    print(m)
    print('Amostragem só nas pontas:', model(coarse=1))
