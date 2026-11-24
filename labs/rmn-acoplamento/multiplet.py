"""First-order prescribed spin-1/2 sticks, exact rational frequencies/areas."""
from fractions import Fraction as Q
from math import comb

def rational(value):
    if type(value) not in (int, Q):
        raise TypeError("use int or Fraction; floats/bools/text are not accepted")
    return Q(value)

def sticks(groups):
    """groups: list/tuple of (count, J_Hz), <=12 neighbours total.
    Returns sorted tuple (offset_Hz, fractional_area), merging exact coincidences.
    Independent equiprobable neighbour states; weak coupling assumed, not checked.
    """
    if type(groups) not in (list, tuple):
        raise TypeError("groups must be list or tuple")
    parsed=[]
    for group in groups:
        if type(group) not in (tuple, list) or len(group)!=2:
            raise TypeError("each group is (count, J_Hz)")
        n,j=group
        if type(n) is not int:raise TypeError("count must be int")
        if n < 1:raise ValueError("group count must be positive")
        parsed.append((n,rational(j)))
    if sum(n for n,j in parsed)>12:
        raise ValueError("at most 12 neighbours in this teaching model")
    result={Q(0):Q(1)}
    for n,j in parsed:
        branch=[(j*(Q(k)-Q(n,2)),Q(comb(n,k),2**n)) for k in range(n+1)]
        combined={}
        for x,w in result.items():
            for y,v in branch:
                combined[x+y]=combined.get(x+y,Q(0))+w*v
        result=combined
    return tuple(sorted(result.items()))

def positions_ppm(groups, center_ppm, reference_mhz):
    center=rational(center_ppm); ref=rational(reference_mhz)
    if ref<=0:raise ValueError("reference_mhz must be positive")
    return tuple((center+x/ref,w) for x,w in sticks(groups))

def moments(lines):
    """Moments of normalized discrete sticks, NOT broadened line-shape variance."""
    total=sum(w for x,w in lines)
    if total<=0:raise ValueError("positive total required")
    center=sum(x*w for x,w in lines)/total
    variance=sum(w*(x-center)**2 for x,w in lines)/total
    return total,center,variance

if __name__=='__main__':
    for groups in ([(2,6)],[(1,6),(1,2)],[(1,6),(1,6)],[(1,6),(1,3)]):
        print(groups, sticks(groups), moments(sticks(groups)))
    print("dd at 400MHz, 2ppm:", positions_ppm([(1,6),(1,2)],Q(2),400))
