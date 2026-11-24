import math
import runpy
from pathlib import Path
import unittest
from fractions import Fraction as F
from .experiment import J,POSITIONS,matrices,modes,model

def jacobi_values(matrix):
    a=[row[:] for row in matrix];n=len(a)
    for _ in range(1500):
        p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda ij:abs(a[ij[0]][ij[1]]))
        if abs(a[p][q])<1e-13:break
        angle=.5*math.atan2(2*a[p][q],a[q][q]-a[p][p]);c=math.cos(angle);s=math.sin(angle)
        ap,aq,off=a[p][p],a[q][q],a[p][q]
        for k in range(n):
            if k not in (p,q):
                x,y=a[k][p],a[k][q];a[k][p]=a[p][k]=c*x-s*y;a[k][q]=a[q][k]=s*x+c*y
        a[p][p]=c*c*ap-2*s*c*off+s*s*aq;a[q][q]=s*s*ap+2*s*c*off+c*c*aq;a[p][q]=a[q][p]=0.
    else:raise AssertionError('Jacobi não convergiu')
    return sorted(a[i][i] for i in range(n))

class AB2DynamicsTests(unittest.TestCase):
    def test_full_hessian_independent_diagonalization(self):
        for mass in range(1,9):
            for bend in range(9):
                weights,h,d=matrices(mass,F(bend,4));rows=modes(mass,bend)
                values=jacobi_values(d)
                target=[0.]*6+[r['eigenvalue'] for r in rows]
                for got,want in zip(values,sorted(target)):self.assertAlmostEqual(got,want,delta=1e-10)
                for r in rows:
                    self.assertLess(r['residual'],1e-11)
                    self.assertAlmostEqual(r['mass_norm'],1)
                for i in range(3):
                    for j in range(i):self.assertAlmostEqual(sum(w*a*b for w,a,b in zip(weights,rows[i]['vector'],rows[j]['vector'])),0,delta=1e-11)
    def test_rigid_invariance_and_classification(self):
        build=runpy.run_path(str(Path(__file__).parents[1]/'deslocamentos-simetria'/'experiment.py'))['build']
        geometry=build('bent');rigid=geometry['translations']+geometry['rotations']
        expected={'A1':(1,1,1,1),'B1':(1,-1,1,-1)}
        for col in rigid:
            self.assertTrue(all(sum(j*v for j,v in zip(row,col))==0 for row in J))
        for mass in (1,2,8):
            for bend in (0,1,4,8):
                weights,_,_=matrices(mass,F(bend,4))
                for r in modes(mass,bend):
                    for col in rigid:self.assertAlmostEqual(sum(w*v*c for w,v,c in zip(weights,r['vector'],col)),0,delta=1e-11)
                    for operation,char in zip(geometry['matrices'].values(),expected[r['irrep']]):
                        transformed=[sum(a*b for a,b in zip(row,r['vector'])) for row in operation]
                        for a,b in zip(transformed,r['vector']):self.assertAlmostEqual(a,char*b,delta=1e-11)
    def test_quadratic_energy_hessian_by_finite_difference(self):
        # Energia avaliada diretamente nas três deformações lineares.
        for bend in (0,1,4,8):
            _,h,_=matrices(2,F(bend,4));step=F(1,100)
            def energy(v):
                q=[sum(a*b for a,b in zip(row,v)) for row in J]
                return (q[0]**2+q[1]**2+F(bend,4)*q[2]**2)/2
            for i in range(9):
                for j in range(9):
                    def point(si,sj):
                        v=[F(0)]*9;v[i]+=si*step;v[j]+=sj*step;return energy(v)
                    numerical=(point(1,1)-point(1,-1)-point(-1,1)+point(-1,-1))/(4*step*step)
                    self.assertEqual(numerical,h[i][j])
    def test_missing_bending_force_display_and_contract(self):
        rows=modes(2,0);self.assertTrue(rows[0]['floppy']);self.assertEqual(rows[0]['eigenvalue'],0)
        self.assertNotEqual(sum(j*v for j,v in zip(J[2],rows[0]['vector'])),0)
        for i in range(3):
            a=model(mode=i,amplitude=1);b=model(mode=i,amplitude=-1)
            self.assertAlmostEqual(max(abs(x) for x in a['displacement']),.25)
            for x,y in zip(a['displacement'],b['displacement']):self.assertAlmostEqual(x,-y)
            self.assertEqual(model(mode=i,amplitude=0)['positions'],POSITIONS)
        for args in [(0,4),(9,4),(True,4),(2,-1),(2,9),(2,.5)]:
            with self.assertRaises(ValueError):modes(*args)
        for amp in (-2,2,True,float('nan')):
            with self.assertRaises(ValueError):model(amplitude=amp)
