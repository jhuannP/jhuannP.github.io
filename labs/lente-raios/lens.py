"""Lente fina paraxial em meios iguais; identidades racionais."""
from fractions import Fraction as F

def rat(x):
    if type(x) not in (int,F):raise TypeError('Use int ou Fraction')
    return F(x)

def image(f,p):
    f,p=map(rat,(f,p))
    if not f or p<=0:raise ValueError('Foco não nulo e objeto real p>0')
    if p==f:return {'kind':'collimated','q':None,'m':None}
    q=f*p/(p-f)
    return {'kind':'real' if q>0 else 'virtual','q':q,'m':-q/p}

def ray(f,p,h,y_lens,z):
    image(f,p) # shared parameter contract
    f,p,h,y,z=map(rat,(f,p,h,y_lens,z))
    slope_in=(y-h)/p
    slope_out=slope_in-y/f
    return y+z*slope_out,slope_out

if __name__=='__main__':
    for f,p in [(10,30),(10,5),(-10,30),(10,10)]:print(f,p,image(f,p))
