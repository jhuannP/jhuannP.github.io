from fractions import Fraction as F
from itertools import product
import unittest
from .experiment import update

class BayesChances(unittest.TestCase):
    def test_independent_atom_enumeration(self):
        # 4 identidades de hipótese × 4 resultados auxiliares equiprováveis.
        for p,a,b in product(range(5), repeat=3):
            atoms=[(i<p, j<(a if i<p else b)) for i in range(4) for j in range(4)]
            signals=[h for h,s in atoms if s]
            r=update(F(p,4),F(a,4),F(b,4))
            self.assertEqual(r['mass'],F(len(signals),16))
            self.assertEqual(r['posterior'],F(sum(signals),len(signals)) if signals else None)
            if 0<p<4 and b>0:
                self.assertEqual(r['posterior_odds']['value'],r['prior_odds']['value']*r['likelihood_ratio']['value'])

    def test_total_probability_and_complement(self):
        for p,a,b in product([F(i,5) for i in range(6)],repeat=3):
            pos=update(p,a,b);neg=update(p,1-a,1-b)
            self.assertEqual(pos['mass']+neg['mass'],1)
            recovered=sum(r['mass']*r['posterior'] for r in (pos,neg) if r['mass'])
            self.assertEqual(recovered,p)
            swap=update(1-p,b,a)
            if pos['mass']:self.assertEqual(swap['posterior'],1-pos['posterior'])

    def test_threshold_and_sequential_evidence(self):
        p=F(1,10);a=F(4,5);b=F(1,5)
        first=update(p,a,b)['posterior']
        second=update(first,a,b)['posterior']
        self.assertEqual(second,F(16,25)) # independência em cada hipótese
        self.assertEqual(update(first,1,1)['posterior'],first) # cópia conhecida
        for i in range(1,20):
            for j in range(1,20):
                p=F(i,20); target=F(j,20)
                bound=target*(1-p)/((1-target)*p)
                for a,b in [(F(4,5),F(1,5)),(F(1,5),F(4,5)),(F(1,2),F(1,2))]:
                    self.assertEqual(update(p,a,b)['posterior']>=target,a/b>=bound)

    def test_zero_masses_and_contracts(self):
        self.assertIsNone(update(F(1,2),0,0)['posterior'])
        self.assertEqual(update(F(1,2),1,0)['posterior_odds']['kind'],'infinite')
        self.assertEqual(update(0,1,0)['posterior_odds']['kind'],'undefined')
        self.assertEqual(update(1,1,0)['posterior'],1)
        for value in [True,0.5,'1/2',F(-1,2),F(3,2),None]:
            for k in range(3):
                args=[F(1,2)]*3;args[k]=value
                with self.assertRaises(ValueError):update(*args)
