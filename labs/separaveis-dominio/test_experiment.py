import unittest
from math import nextafter,exp
from fractions import Fraction as F
from .experiment import model

class SeparableTests(unittest.TestCase):
    def test_rational_identity_and_interval(self):
        for y0 in (F(i,4) for i in range(-8,9)):
            for t in (F(j,8) for j in range(-16,17)):
                s=model(1,float(y0),float(t));d=1-y0*t
                self.assertEqual(s['defined'],d>0)
                self.assertEqual(s['reason'],'polo' if d==0 else 'outro-intervalo' if d<0 else 'valida')
                if d>0:
                    self.assertAlmostEqual(s['value'],float(y0/d),places=12)
                    # Verificação implícita sem dividir por y0, incluindo zero.
                    self.assertAlmostEqual(s['value']*(1-float(y0*t)),float(y0),places=12)
                    self.assertAlmostEqual(s['derivative'],float(y0*y0/(d*d)),places=10)
                else:self.assertIsNone(s['value']);self.assertIsNone(s['derivative'])

    def test_reference_and_derivatives(self):
        for kind in (0,1):
            for y0 in (-2,-1,0,.5,1,2):self.assertEqual(model(kind,y0,0)['value'],y0)
        for t in (-2,-1,0,.5,2):
            s=model(0,1,t);self.assertAlmostEqual(s['value'],exp(t)**2,places=12)
        for kind,y0,t in ((0,1,.2),(0,-1,-.5),(1,1,.3),(1,-1,.5)):
            h=.00001;diff=(model(kind,y0,t+h)['value']-model(kind,y0,t-h)['value'])/(2*h)
            self.assertAlmostEqual(diff,model(kind,y0,t)['derivative'],places=7)

    def test_pole_neighbors_and_zero(self):
        self.assertTrue(model(1,1,nextafter(1,0))['defined'])
        self.assertFalse(model(1,1,1)['defined']);self.assertFalse(model(1,1,nextafter(1,2))['defined'])
        self.assertTrue(model(1,-1,nextafter(-1,0))['defined'])
        self.assertFalse(model(1,-1,-1)['defined']);self.assertFalse(model(1,-1,nextafter(-1,-2))['defined'])
        self.assertEqual(model(1,-1,0)['lower'],-1);self.assertEqual(model(1,1,0)['upper'],1)
        for t in (-2,0,2):
            s=model(1,0,t);self.assertIsNone(s['pole']);self.assertEqual(s['value'],0)
        # Família com espera para outra EDO: y'=2sqrt(y), y(0)=0, domínio y>=0.
        for wait in (0,1,2):
            for t in (-1,0,1,2,3):
                y=max(t-wait,0)**2;dy=2*max(t-wait,0)
                self.assertEqual(dy*dy,4*y)

    def test_invalid_controls(self):
        for args in ((2,0,0),(True,0,0),(0,3,0),(1,0,3),(0,True,0),(1,float('nan'),0)):
            with self.assertRaises(ValueError):model(*args)
