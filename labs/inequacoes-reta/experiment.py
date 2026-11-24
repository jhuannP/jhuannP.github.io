"""Inequação linear real: solução simbólica com racionais; Python opcional."""
from fractions import Fraction as F
OPS=('<','<=','>','>=')
FLIP={'<':'>','<=':'>=','>':'<','>=':'<='}

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError('Use int ou Fraction')
    return F(x)

def compare(left,right,op):
    if op not in OPS:raise ValueError('Operador inválido')
    return {'<':left<right,'<=':left<=right,'>':left>right,'>=':left>=right}[op]

def solve(a,b,c,op='<'):
    a,b,c=map(rational,(a,b,c))
    if op not in OPS:raise ValueError('Operador inválido')
    if a==0:
        return dict(kind='all' if compare(b,c,op) else 'none',boundary=None,operator=None,closed=False)
    return dict(kind='ray',boundary=(c-b)/a,operator=op if a>0 else FLIP[op],closed=op in ('<=','>='))

def contains(solution,x):
    x=rational(x)
    if solution['kind']=='all':return True
    if solution['kind']=='none':return False
    return compare(x,solution['boundary'],solution['operator'])

if __name__=='__main__':
    s=solve(-2,0,6)
    assert s['boundary']==-3 and s['operator']=='>'
    for x in (F(-4),F(-3),F(-5,2),F(0)):
        assert contains(s,x)==(-2*x<6)
    print('Solução:',s)
    print('A grade confere casos; a equivalência algébrica justifica o conjunto real.')
