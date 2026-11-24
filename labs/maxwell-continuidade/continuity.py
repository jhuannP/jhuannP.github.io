"""Modelos didáticos racionais; não é um resolvedor de campos de Maxwell."""
from fractions import Fraction as Q
from itertools import product
import unittest


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction')
    return Q(x)


def cube_flux(rate,L):
    rate,L=map(rational,(rate,L))
    if L<=0:
        raise ValueError('Semilado positivo')
    # J_i=-rate*x_i/3 on each face. Each normal is explicitly signed.
    flux=Q(0)
    for axis in range(3):
        for side in (-1,1):
            position=side*L
            current_component=-rate*position/3
            flux+=current_component*side*(2*L)**2
    return flux


def capacitor(current,r,R):
    """Returns I_D(r) and B(r)/B(R); latter only defined for current!=0."""
    current,r,R=map(rational,(current,r,R))
    if R<=0 or r<0:
        raise ValueError('R>0 e r>=0')
    fraction=min((r/R)**2,Q(1))
    ratio=r/R if r<=R else R/r
    return current*fraction, ratio if current else None


class Checks(unittest.TestCase):
    def test_cube_charge_balance(self):
        # rho=a+b*t+c*t²; explicit face currents vs derivative of rho*volume.
        for a,b,c,t,L in product((Q(-1),Q(0),Q(2)),
                                  (Q(-2),Q(0),Q(3)),(Q(0),Q(1,2)),
                                  (Q(0),Q(1,3),Q(2)),(Q(1,2),Q(1),Q(3))):
            rate=b+2*c*t
            charge_derivative=(2*L)**3*rate
            self.assertEqual(cube_flux(rate,L),-charge_derivative)
        self.assertEqual(cube_flux(2,1),-16)

    def test_local_equations(self):
        # Exact pointwise cancellation of conduction and displacement currents.
        for rate,eps,xyz in product((Q(-2),Q(0),Q(3)),(Q(1),Q(2,3)),
                                    product((Q(-1),Q(0),Q(2)),repeat=3)):
            J=tuple(-rate*x/3 for x in xyz)
            dE=tuple(rate*x/(3*eps) for x in xyz)
            self.assertEqual(tuple(j+eps*e for j,e in zip(J,dE)),(0,0,0))
            # Spatial derivatives of E_i=rho*x_i/(3eps) give rho/eps.
            rho=Q(5,7)
            self.assertEqual(sum(rho/(3*eps) for _ in range(3)),rho/eps)
            self.assertEqual(sum(-rate/3 for _ in range(3)),-rate)

    def test_capacitor_geometry(self):
        for current,R,radius_ratio in product((Q(-2),Q(0),Q(3)),
                                              (Q(1,2),Q(2)),
                                              (Q(0),Q(1,4),Q(1,2),Q(1),Q(2),Q(4))):
            r=R*radius_ratio
            displacement,ratio=capacitor(current,r,R)
            self.assertEqual(displacement,current*min(radius_ratio**2,Q(1)))
            if current:
                # 2πr B/μ0 = enclosed I; divide by B(R)=μ0 I/(2πR).
                self.assertEqual(radius_ratio*ratio,displacement/current)
            else:
                self.assertIsNone(ratio)
        self.assertEqual(capacitor(2,Q(1,2),1),(Q(1,2),Q(1,2)))
        self.assertEqual(capacitor(2,1,1),(Q(2),Q(1)))
        self.assertEqual(capacitor(2,2,1),(Q(2),Q(1,2)))

    def test_contracts(self):
        for L in (0,-1,True,.5):
            with self.assertRaises(ValueError):cube_flux(2,L)
        for args in ((1,-1,1),(1,1,0),(True,1,1),(.5,1,1)):
            with self.assertRaises(ValueError):capacitor(*args)


if __name__=='__main__':
    unittest.main()
