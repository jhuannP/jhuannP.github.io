"""Small exact matrices for studying Laplace expansion, not a scalable solver."""
from fractions import Fraction as Q

def matrix(a):
    if not isinstance(a,(tuple,list)) or len(a)>6:raise ValueError('square matrix up to order six')
    n=len(a)
    if any(not isinstance(row,(tuple,list)) or len(row)!=n for row in a):raise ValueError('square matrix required')
    if any(isinstance(x,bool) or not isinstance(x,(int,Q)) for row in a for x in row):raise ValueError('int/Fraction entries required')
    return tuple(tuple(Q(x) for x in row) for row in a)

def minor(a,i,j):
    return tuple(tuple(x for k,x in enumerate(row) if k!=j) for h,row in enumerate(a) if h!=i)

def _det(a):
    if not a:return Q(1)
    return sum(((-1)**j*a[0][j]*_det(minor(a,0,j)) for j in range(len(a))),Q(0))

def determinant(a):return _det(matrix(a))

def expansion(a,row=0):
    """Individual signed contributions a_ij C_ij for a selected row."""
    a=matrix(a)
    if isinstance(row,bool) or not isinstance(row,int) or not 0<=row<len(a):raise ValueError('valid nonempty row required')
    return tuple(a[row][j]*(-1)**(row+j)*_det(minor(a,row,j)) for j in range(len(a)))

def adjugate(a):
    a=matrix(a);n=len(a)
    return tuple(tuple((-1)**(i+j)*_det(minor(a,j,i)) for j in range(n)) for i in range(n))

if __name__=='__main__':
    a=((2,1,0),(0,3,1),(1,0,2))
    print('contribuições primeira linha:',expansion(a))
    print('det:',determinant(a))
    print('adjunta clássica:',adjugate(a))
