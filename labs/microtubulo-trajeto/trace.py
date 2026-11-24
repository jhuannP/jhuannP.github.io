"""Trajetória fornecida, não simulador de capa de GTP ou inferência biológica."""
from fractions import Fraction as Q

def rational(v,positive=False):
    if type(v) not in (int,Q):raise ValueError('Inteiro ou Fraction necessário')
    v=Q(v)
    if v<0 or (positive and v==0):raise ValueError('Valor fora do domínio')
    return v

def trace(initial,segments,growth=Q(1,5),shrink=Q(1,2)):
    length=rational(initial,True);growth=rational(growth,True);shrink=rational(shrink,True)
    segments=tuple(segments)
    if not 1<=len(segments)<=100:raise ValueError('De 1 a 100 trechos')
    time=Q(0);exposure={'G':Q(0),'S':Q(0)};events={'G':0,'S':0};points=[(time,length)];previous=None
    for i,(state,duration) in enumerate(segments):
        if state not in exposure or state==previous:raise ValueError('Estados G/S alternados necessários')
        duration=rational(duration,True)
        if previous is not None:events[previous]+=1
        next_length=length+(growth if state=='G' else -shrink)*duration
        if next_length<0 or (next_length==0 and i!=len(segments)-1):raise ValueError('Trajeto atravessa a fronteira zero')
        time+=duration;length=next_length;exposure[state]+=duration;points.append((time,length));previous=state
    return dict(points=points,exposure=exposure,catastrophes=events['G'],rescues=events['S'],
                catastrophe_rate=None if not exposure['G'] else Q(events['G'])/exposure['G'],
                rescue_rate=None if not exposure['S'] else Q(events['S'])/exposure['S'])

if __name__=='__main__':
    print(trace(3,[('G',10),('S',4),('G',5)]))
