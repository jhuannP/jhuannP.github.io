import unittest
from fractions import Fraction as Q
from .ice import equilibrium,CI,CW,LF

class LatentHeatTests(unittest.TestCase):
    def test_original_examples(self):
        mixed=equilibrium(100,-10,200,40)
        self.assertEqual(mixed.state,'mistura');self.assertEqual(mixed.temperature,0)
        self.assertEqual(mixed.ice,Q(950,167))
        self.assertEqual(mixed.liquid,300-Q(950,167))
        self.assertEqual(200*CW*40,33600)
        self.assertEqual(100*CI*10+100*LF,35500)
        warm=equilibrium(100,-10,200,60)
        self.assertEqual(warm.state,'agua');self.assertEqual(warm.temperature,Q(745,63))
        frozen=equilibrium(100,-20,10,5)
        self.assertEqual(frozen.state,'gelo');self.assertEqual(frozen.temperature,Q(-650,231))

    def test_balance_by_initial_and_final_subsystems(self):
        # Via independente: energia cedida/recebida, por fase inicial e final.
        count=0
        for mi in [10,100,200]:
            for mw in [10,100,200]:
                for ti in [-40,-10,0]:
                    for tw in [0,20,60,90]:
                        result=equilibrium(mi,ti,mw,tw);t=result.temperature
                        self.assertEqual(result.ice+result.liquid,mi+mw)
                        self.assertGreaterEqual(result.ice,0);self.assertGreaterEqual(result.liquid,0)
                        self.assertTrue(min(ti,0)<=t<=max(tw,0))
                        if result.state=='agua':
                            received=mi*(CI*(-ti)+LF+CW*t)
                            released=mw*CW*(tw-t)
                        elif result.state=='gelo':
                            received=mi*CI*(t-ti)
                            released=mw*(CW*tw+LF+CI*(-t))
                        else:
                            melted=result.liquid-mw
                            # melted pode ser negativo: parte da água congela.
                            received=mi*CI*(-ti)+melted*LF
                            released=mw*CW*tw
                        self.assertEqual(received,released)
                        count+=1
        self.assertEqual(count,108)

    def test_thresholds_and_plateau(self):
        # Gelo já em 0°C, água em 40°C: cada g de água cede 168 J.
        mw=Q(334,168)
        r=equilibrium(1,0,mw,40)
        self.assertEqual(r.state,'agua');self.assertEqual(r.temperature,0)
        below=equilibrium(1,0,mw-Q(1,1000),40)
        above=equilibrium(1,0,mw+Q(1,1000),40)
        self.assertEqual(below.state,'mistura');self.assertEqual(below.temperature,0)
        self.assertEqual(above.state,'agua');self.assertGreater(above.temperature,0)
        # Limite de congelamento completo: H=0.
        cold=Q(334,42)
        r=equilibrium(cold,-20,1,0)
        self.assertEqual(r.state,'gelo');self.assertEqual(r.temperature,0)

    def test_mass_scaling_and_simple_limits(self):
        base=equilibrium(100,-10,200,40)
        for scale in [Q(1,1000),2,1000]:
            r=equilibrium(100*scale,-10,200*scale,40)
            self.assertEqual(r.temperature,base.temperature)
            self.assertEqual(r.ice,base.ice*scale)
            self.assertEqual(r.thermal_reference,base.thermal_reference*scale)
        self.assertEqual(equilibrium(1,-10,0,0).temperature,-10)
        self.assertEqual(equilibrium(0,0,1,40).temperature,40)
        self.assertEqual(equilibrium(1,0,1,0).liquid,1)

    def test_contracts(self):
        for args in [(0,0,0,0),(-1,0,1,0),(1,-41,1,0),(1,1,1,0),(1,0,1,-1),(1,0,1,91)]:
            with self.assertRaises(ValueError):equilibrium(*args)
        for bad in [True,1.0,'1']:
            with self.assertRaises(TypeError):equilibrium(bad,0,1,0)

if __name__=='__main__':unittest.main()
