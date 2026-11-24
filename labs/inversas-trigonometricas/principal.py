"""Inversas principais aproximadas e direção orientada em [-pi,pi)."""
import math

def finite_number(value):
    if type(value) not in (int,float):raise ValueError('Use int/float finito, sem bool/texto')
    try:value=float(value)
    except OverflowError as exc:raise ValueError('Fora da faixa de float') from exc
    if not math.isfinite(value):raise ValueError('Valor não finito')
    return value

def inverse(kind,value):
    functions={'asin':math.asin,'acos':math.acos,'atan':math.atan}
    if type(kind) is not str or kind not in functions:raise ValueError('Escolha asin, acos ou atan')
    x=finite_number(value)
    if kind in ('asin','acos') and not -1<=x<=1:
        raise ValueError('Domínio real: -1<=x<=1, sem ajuste silencioso')
    return functions[kind](x)

def direction_angle(x,y):
    x,y=map(finite_number,(x,y))
    if x==0 and y==0:raise ValueError('A origem não define uma direção')
    angle=math.atan2(y,x)
    if angle==math.pi:angle=-math.pi
    return 0.0 if angle==0 else angle  # unifica +0/-0 na saída

if __name__=='__main__':
    print('arctan(y/x):',inverse('atan',-1))
    print('Direção de (-1,+1):',direction_angle(-1,1))
    assert math.isclose(direction_angle(-1,1),3*math.pi/4)
