import unittest
from fractions import Fraction as Q
from itertools import product
from math import sqrt,pi
from decimal import Decimal,localcontext
from .cells import basis,closed_points,weighted_count,nearest,geometry,density

class CellTests(unittest.TestCase):
    def test_boundary_categories(self):
        expected={'SC':{3:8},'BCC':{3:8,0:1},'FCC':{3:8,1:6}}
        for kind,categories in expected.items():
            points=closed_points(kind);actual={}
            for p in points:
                n=sum(x in (0,1) for x in p);actual[n]=actual.get(n,0)+1
            self.assertEqual(actual,categories)
            self.assertEqual(weighted_count(kind),{'SC':1,'BCC':2,'FCC':4}[kind])
            self.assertEqual(len(basis(kind)),weighted_count(kind))

    def test_neighbors_against_periodic_supercell(self):
        # Enumeração independente por paridade em malha de meio passo.
        for kind in ['SC','BCC','FCC']:
            for size in [3,4,5]:
                sites=[]
                for v in product(range(2*size),repeat=3):
                    odd=sum(x%2 for x in v)
                    if (kind=='SC' and odd==0) or (kind=='BCC' and odd in (0,3)) or (kind=='FCC' and odd in (0,2)):
                        sites.append(v)
                self.assertEqual(len(sites),{'SC':1,'BCC':2,'FCC':4}[kind]*size**3)
                ds=[Q(sum(min(x,2*size-x)**2 for x in v),4) for v in sites if any(v)]
                dmin=min(ds)
                g=geometry(kind)
                self.assertEqual(dmin,g['distance_squared_over_a2'])
                self.assertEqual(ds.count(dmin),g['coordination'])

    def test_geometry_literal_and_nonoverlap(self):
        for kind,atom,z,d2,phi in [('SC',1,6,Q(1),pi/6),('BCC',2,8,Q(3,4),sqrt(3)*pi/8),('FCC',4,12,Q(1,2),pi/(3*sqrt(2)))]:
            g=geometry(kind)
            self.assertEqual((g['atoms'],g['coordination'],g['distance_squared_over_a2']),(atom,z,d2))
            self.assertAlmostEqual(g['packing'],phi,places=14)
            self.assertAlmostEqual(4*g['radius_over_a']**2,float(d2),places=14)
            # Todas as distâncias no bloco ampliado são >= diâmetro de contato.
            for b in basis(kind):
                for shift in product(range(-2,3),repeat=3):
                    d=sum((b[i]+shift[i])**2 for i in range(3))
                    if d:self.assertGreaterEqual(d,d2)

    def test_density_decimal_and_replicas(self):
        with localcontext() as ctx:
            ctx.prec=50
            ref=Decimal(240)/(Decimal('6.02214076e23')*Decimal('4e-8')**3)
        self.assertAlmostEqual(density('FCC',60,400),float(ref),places=13)
        for kind in ['SC','BCC','FCC']:
            rho=density(kind,60,400)
            for N in [1,2,3,7]:
                # Massa e volume de N³ células, calculados diretamente.
                mass=N**3*len(basis(kind))*60/6.02214076e23
                volume=(N*400e-10)**3
                self.assertAlmostEqual(mass/volume,rho,places=12)

    def test_scaling_and_partial_occupation(self):
        for kind in ['SC','BCC','FCC']:
            rho=density(kind,60,400)
            self.assertAlmostEqual(density(kind,120,400),2*rho)
            self.assertAlmostEqual(density(kind,60,800),rho/8)
            self.assertAlmostEqual(density(kind,60,400,Q(9,10)),.9*rho)
            self.assertEqual(density(kind,60,400,0),0)
        # A igual: FCC/BCC=2; r igual é outra comparação.
        self.assertAlmostEqual(density('FCC',60,400)/density('BCC',60,400),2)
        r=100
        ratio=density('FCC',60,2*sqrt(2)*r)/density('BCC',60,4*r/sqrt(3))
        self.assertAlmostEqual(ratio,4*sqrt(6)/9)

    def test_contracts(self):
        for kind in ['HCP','fcc','',None]:
            with self.assertRaises(ValueError):geometry(kind)
        for args in [('SC',0,400),('FCC',60,0),('BCC',60,400,-.1),('FCC',60,400,1.1),('SC',float('nan'),400)]:
            with self.assertRaises(ValueError):density(*args)
        for args in [('SC',True,400),('SC','60',400),('SC',60,False)]:
            with self.assertRaises(TypeError):density(*args)
