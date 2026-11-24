import unittest
from fractions import Fraction as Q
from math import pi,isclose,cos,sin
from .experiment import ellipse,sector_cell

class AreaJacobianTests(unittest.TestCase):
    def test_ellipse_against_cartesian_midpoint_grid(self):
        # Integração em caixas cartesianas, sem Jacobiano polar ou fórmula da elipse.
        n=400
        cells=[(i,j) for i in range(-n+1,n,2) for j in range(-n+1,n,2) if i*i+j*j<=n*n]
        for a,b in ((1,1),(2,1),(1,3),(Q(3,2),Q(2,3))):
            q=ellipse(a,b);area=float(4*a*b)*len(cells)/(n*n)
            moment=float(4*a*b)*sum(float(a*a)*i*i+float(b*b)*j*j for i,j in cells)/(n**4)
            self.assertTrue(isclose(area,float(q["area_over_pi"])*pi,rel_tol=.002))
            self.assertTrue(isclose(moment,float(q["moment_over_pi"])*pi,rel_tol=.003))
    def test_orientation_against_derivative_columns(self):
        for sign in (-1,1):
            for theta in (0,.3,1.2,3.,5.):
                for radius in (.2,.7,1.):
                    # Derivadas diretas de (sign*a*r*cosθ,b*r*sinθ).
                    a,b=2,3
                    xu=sign*a*cos(theta);xv=-sign*a*radius*sin(theta)
                    yu=b*sin(theta);yv=b*radius*cos(theta)
                    det=xu*yv-xv*yu
                    self.assertAlmostEqual(det,float(ellipse(a,b,sign)["jacobian_over_r"])*radius)
            self.assertEqual(ellipse(2,3,sign)["area_over_pi"],6)
    def test_cells_by_radial_integral_splitting_and_refinement(self):
        for radius in (0,1,2,Q(3,2)):
            for dr in (Q(1,10),Q(1,4),1):
                c=sector_cell(radius,dr,Q(1,5))
                # Integral de r: diferença de primitivas, calculada independentemente.
                exact=((radius+dr)**2-radius**2)*Q(1,10)
                self.assertEqual(c["exact"],exact)
                self.assertEqual(c["exact"]-c["lower_left"],c["error"])
                half=Q(dr)/2
                parts=sector_cell(radius,half,Q(1,5))["exact"]+sector_cell(radius+half,half,Q(1,5))["exact"]
                self.assertEqual(parts,exact)
                self.assertEqual(sector_cell(radius,Q(dr)/2,Q(1,5))["error"],c["error"]/4)
    def test_contracts_and_scaling(self):
        for a,b in ((1,2),(Q(2,3),Q(3,4))):
            q=ellipse(a,b);d=ellipse(2*a,2*b)
            self.assertEqual(d["area_over_pi"],4*q["area_over_pi"])
            self.assertEqual(d["moment_over_pi"],16*q["moment_over_pi"])
        for bad in (0,-1,True,.5,'1'):
            with self.assertRaises(ValueError):ellipse(bad,1)
        for bad in (0,2,True,1.):
            with self.assertRaises(ValueError):ellipse(1,1,bad)
        self.assertEqual(sector_cell(0,1,1)["lower_left"],0)
        self.assertEqual(sector_cell(0,1,1)["exact"],Q(1,2))
