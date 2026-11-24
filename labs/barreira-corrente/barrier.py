"""Espalhamento estacionário: forma fechada e casamento independente.
Unidades reduzidas V0=1 e 2m=hbar=1 no sistema linear.
"""
import math
import unittest
from itertools import product


def parameters(e,z):
    if any(type(x) not in (int,float) for x in (e,z)):
        raise ValueError('Use int/float nativos')
    try:e,z=float(e),float(z)
    except (ValueError,OverflowError):raise ValueError('Valores finitos') from None
    if not (math.isfinite(e) and math.isfinite(z) and
            1e-6 <= e <= 1-1e-6 and 0 <= z <= 20):
        raise ValueError('1e-6 <= e <= 1-1e-6 e 0 <= z <= 20')
    return e,z


def transmission(e,z):
    e,z=parameters(e,z)
    return 1/(1+math.sinh(z)**2/(4*e*(1-e)))


def solve(matrix,rhs):
    """Eliminação com pivô parcial complexo, independente da fórmula T."""
    a=[list(map(complex,row))+[complex(b)] for row,b in zip(matrix,rhs)]
    for j in range(len(a)):
        pivot=max(range(j,len(a)),key=lambda k:abs(a[k][j]))
        a[j],a[pivot]=a[pivot],a[j]
        v=a[j][j]
        if abs(v)<1e-14:raise ValueError('Pivô pequeno')
        a[j]=[x/v for x in a[j]]
        for k in range(len(a)):
            if k != j:
                v=a[k][j];a[k]=[x-v*y for x,y in zip(a[k],a[j])]
    return [row[-1] for row in a]


def matching(e,z):
    e,z=parameters(e,z)
    if z>5:raise ValueError('Sistema direto limitado a z <= 5')
    k,kap=math.sqrt(e),math.sqrt(1-e)
    ep,em=math.exp(z),math.exp(-z)
    # Unknowns r,C,D,t, with inside C exp(kap*x)+D exp(-kap*x).
    m=[[1,-1,-1,0],[-1j*k,-kap,kap,0],
       [0,ep,em,-1],[0,kap*ep,-kap*em,-1j*k]]
    return solve(m,[-1,-1j*k,0,0])


class Checks(unittest.TestCase):
    def test_matching_against_closed_form(self):
        for e,z in product((.01,.2,.5,.8,.99),(0,.25,1,3,5)):
            r,c,d,t=matching(e,z)
            self.assertAlmostEqual(abs(t)**2,transmission(e,z),places=11)
            self.assertAlmostEqual(abs(r)**2+abs(t)**2,1,places=11)

    def test_boundary_and_current(self):
        for e,z in product((.2,.5,.8),(.25,1,3,5)):
            r,c,d,t=matching(e,z);k,kap=math.sqrt(e),math.sqrt(1-e)
            self.assertLess(abs(1+r-c-d),1e-11)
            self.assertLess(abs(1j*k*(1-r)-kap*(c-d)),1e-11)
            for s in (0,.3,.7,1):
                # s=x/a; kap*x=s*z. Omit common hbar/m in all currents.
                psi=c*math.exp(s*z)+d*math.exp(-s*z)
                derivative=kap*(c*math.exp(s*z)-d*math.exp(-s*z))
                self.assertAlmostEqual((psi.conjugate()*derivative).imag,
                                       k*abs(t)**2,places=11)
            self.assertLess(abs(c*math.exp(z)+d*math.exp(-z)-t),1e-11)
            self.assertLess(abs(kap*(c*math.exp(z)-d*math.exp(-z))-1j*k*t),1e-11)

    def test_symmetric_and_thick(self):
        for z in (0,.1,1,3,5,10,20):
            self.assertAlmostEqual(transmission(.5,z),1/math.cosh(z)**2,places=14)
        exact=transmission(.5,3);approx=4*math.exp(-6)
        self.assertAlmostEqual(approx/exact-1,2*math.exp(-6)+math.exp(-12),places=13)
        self.assertGreater(4*math.exp(-2),transmission(.5,1))

    def test_zero_width_and_monotonicity(self):
        for e in (.01,.2,.5,.8,.99):
            self.assertEqual(transmission(e,0),1)
            values=[transmission(e,z/2) for z in range(41)]
            self.assertTrue(all(a>b>0 for a,b in zip(values,values[1:])))

    def test_contracts(self):
        for e,z in [(0,1),(1,1),(.5,-1),(.5,21),(True,1),(.5,'1'),
                    (float('nan'),1),(.5,float('inf')),(10**400,1)]:
            with self.assertRaises(ValueError):transmission(e,z)
        with self.assertRaises(ValueError):matching(.5,6)


if __name__=='__main__':
    for z in (1,3):
        exact=transmission(.5,z);approx=4*math.exp(-2*z)
        print(f'z={z}: T={exact:.12g}, exp={math.exp(-2*z):.12g}, '
              f'prefator={approx:.12g}, erro relativo={approx/exact-1:.12g}')
    unittest.main()
