"""Fixed, deliberately small teaching experiment; no source-code mutation."""
from fractions import Fraction as Q
from itertools import combinations

def inputs(m,v):
    if any(isinstance(x,bool) or not isinstance(x,(int,Q)) for x in (m,v)):
        raise ValueError('int/Fraction required')
    return Q(m),Q(v)

def implementation(name,m,v):
    m,v=inputs(m,v)
    if name=='zero_rejected':
        if m<=0:raise ValueError('mass must be positive: deliberate bug')
    elif name!='negative_accepted' and m<0:raise ValueError('negative mass')
    if name=='no_half':return m*v*v
    if name=='no_square':return m*v/2
    if name=='mass_squared':return m*m*v*v/2
    if name=='equivalent_abs':return m*abs(v)**2/2
    if name in ('correct','negative_accepted','zero_rejected'):return m*v*v/2
    raise ValueError('unknown implementation')

# Expected values are hand-derived, not computed by the function under test.
CASES={'rest':(1,0,Q(0)),'general':(2,3,Q(9)),'zero_mass':(0,3,Q(0)),'negative_velocity':(2,-3,Q(9)),'invalid_mass':(-1,3,ValueError)}
BUGS=('no_half','no_square','mass_squared','negative_accepted','zero_rejected')
NAMES=('correct',*BUGS,'equivalent_abs')

def passes(name,case):
    m,v,expected=CASES[case]
    try:got=implementation(name,m,v)
    except ValueError:return expected is ValueError
    return expected is not ValueError and got==expected

def detected(case):return frozenset(name for name in BUGS if not passes(name,case))

def minimal_suites():
    names=tuple(CASES)
    for size in range(len(names)+1):
        winners=[group for group in combinations(names,size) if frozenset().union(*(detected(c) for c in group))==frozenset(BUGS)]
        if winners:return winners
    return []

if __name__=='__main__':
    for case in CASES:print(case,'detecta',','.join(sorted(detected(case))) or 'nenhum dos cinco erros')
    print('Menores conjuntos para ESTES cinco erros:',minimal_suites())
