from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import unittest
from .orbit import circular,specific_energy,surface_change

class GravityTests(unittest.TestCase):
    def test_reference(self):
        c=circular(8,2)
        self.assertEqual(c,{'v2':4,'k':2,'u':-4,'energy':-2,'angular2':16,'period2_over_4pi2':1,'escape2':8})
        self.assertEqual(circular(8,8)['energy'],Q(-1,2))
        self.assertEqual(surface_change(8,2,Q(1,5)),{'exact':Q(4,11),'linear':Q(2,5),'relative':Q(1,10)})
    def test_dynamics_and_scale(self):
        for mu,r in product((Q(1),Q(8),Q(3,2)),(Q(1),Q(2),Q(5))):
            c=circular(mu,r)
            self.assertEqual(c['v2']/r,mu/r**2)
            self.assertEqual(2*c['k']+c['u'],0)
            self.assertEqual(c['k']+c['u'],c['energy'])
            self.assertEqual(c['angular2'],r*r*c['v2'])
            large=circular(mu,4*r)
            self.assertEqual(large['v2'],c['v2']/4)
            self.assertEqual(large['period2_over_4pi2'],64*c['period2_over_4pi2'])
    def test_energy_is_not_circle_certificate(self):
        # Estado circular r2,vt2 versus outro estado ligado r2,vt1.
        self.assertEqual(specific_energy(8,2,0,2),-2)
        self.assertEqual(specific_energy(8,2,0,1),Q(-7,2))
        self.assertNotEqual(Q(1,2),Q(8,4)) # vt²/r difere de mu/r².
        # Estado com energia de escape: vr2,vt2 dá v²8, sem raiz irracional.
        self.assertEqual(specific_energy(8,2,2,2),0)
        self.assertEqual(specific_energy(8,2,3,0),Q(1,2))
    def test_surface_approximation(self):
        for mu,R,z in product((1,8),(1,2),(Q(1,5),1,2)):
            got=surface_change(mu,R,z)
            # Referência independente da subtração de potenciais da implementação.
            self.assertEqual(got['exact'],Q(mu)*z/(R*(R+z)))
            self.assertEqual(got['relative'],Q(z)/R)
        self.assertEqual(surface_change(8,2,0),{'exact':0,'linear':0,'relative':None})
        self.assertEqual(surface_change(8,2,2)['relative'],1)
    def test_preserved_material(self):
        ls=json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text())
        l=next(x for x in ls if x['id']=='f1-gravitacao')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
    def test_contracts(self):
        for bad in (True,1.0,'1'):
            with self.assertRaises(TypeError):circular(bad,2)
        for bad in (0,-1):
            with self.assertRaises(ValueError):circular(8,bad)
        with self.assertRaises(ValueError):surface_change(8,2,-1)
if __name__=='__main__':unittest.main()
