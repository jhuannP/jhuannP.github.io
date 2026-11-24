"""Synthetic binary masks; geometry accounting, not image analysis or biology inference."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError("use int or Fraction")
    return Q(x)

def mask(points):
    if type(points) not in (list,tuple,set,frozenset):raise ValueError("explicit coordinate collection required")
    result=set()
    for point in points:
        if type(point) is not tuple or len(point)!=3 or any(type(i) is not int for i in point):
            raise ValueError("coordinates must be tuples of three integers")
        result.add(point)
    return frozenset(result)

def measure(microglia,signal,lysosome,spacing=(1,1,1)):
    m=mask(microglia);s=mask(signal);l=mask(lysosome)
    if not m:raise ValueError("nonempty cell mask required")
    if type(spacing) not in (tuple,list) or len(spacing)!=3:raise ValueError("three spacings required")
    dx,dy,dz=map(rational,spacing)
    if min(dx,dy,dz)<=0:raise ValueError("positive spacings required")
    voxel=dx*dy*dz
    inside=m&s;triple=inside&l
    return dict(cell_count=len(m),signal_count=len(s),inside_count=len(inside),lysosome_inside_count=len(triple),
                cell_volume=len(m)*voxel,inside_volume=len(inside)*voxel,
                occupancy=Q(len(inside),len(m)),
                signal_inside_fraction=Q(len(inside),len(s)) if s else None,
                lysosome_fraction=Q(len(triple),len(inside)) if inside else None)

def projection_xy_overlap(microglia,signal):
    m={(x,y) for x,y,z in mask(microglia)};s={(x,y) for x,y,z in mask(signal)}
    return len(m&s),len(s)

def threshold(field,cutoff):
    cutoff=rational(cutoff)
    if type(field) is not dict:raise ValueError("coordinate-to-intensity dictionary required")
    mask(list(field))
    values={point:rational(value) for point,value in field.items()}
    return frozenset(point for point,value in values.items() if value>=cutoff)

def cell_aggregates(counts):
    if type(counts) not in (list,tuple) or not counts:raise ValueError("nonempty list/tuple of counts")
    parsed=[]
    for item in counts:
        if type(item) not in (tuple,list) or len(item)!=2:raise ValueError("(cell_voxels,inside_voxels)")
        m,i=item
        if type(m) is not int or type(i) is not int or not 0<=i<=m or m<=0:raise ValueError("valid integer counts required")
        parsed.append((m,i))
    cell_mean=sum((Q(i,m) for m,i in parsed),Q(0))/len(parsed)
    pooled=Q(sum(i for m,i in parsed),sum(m for m,i in parsed))
    return cell_mean,pooled

CELL=frozenset((x,y,z) for x in (0,1) for y in (0,1) for z in (0,1,2))
FIELD={(0,0,1):20,(1,1,2):12,(0,1,4):18,(1,0,5):16,(2,2,1):30}
LYSOSOME=frozenset(((0,0,1),(0,1,0),(1,0,1)))

if __name__=='__main__':
    for cut in (10,15,25):
        signal=threshold(FIELD,cut)
        print("threshold",cut,measure(CELL,signal,LYSOSOME,(Q(1,2),Q(1,2),2)))
    print("xy overlap",projection_xy_overlap(CELL,threshold(FIELD,10)))
    print("cell mean / pooled",cell_aggregates([(10,2),(90,9)]))
