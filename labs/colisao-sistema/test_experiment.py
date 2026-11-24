from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import stick

class StickingCollisionTests(unittest.TestCase):
    def test_known_examples_and_opposite_impulses(self):
        r=stick(1,1,4,0)
        self.assertEqual(r,dict(v=Q(2),p_before=Q(4),p_after=Q(4),
            k_before=Q(8),k_after=Q(4),loss=Q(4),impulse1=Q(-2),impulse2=Q(2)))
        r=stick(1,1,3,-3)
        self.assertEqual((r["v"],r["p_before"],r["loss"]),(0,0,9))
    def test_grid_against_center_frame_energy(self):
        for m1,m2 in product([Q(1,2),Q(1),Q(3),Q(5,2)],repeat=2):
            for u1,u2 in product(range(-4,5),repeat=2):
                r=stick(m1,m2,u1,u2)
                self.assertEqual(r["p_before"],r["p_after"])
                self.assertEqual(r["impulse1"]+r["impulse2"],0)
                # Avaliação independente na referência que se move com a velocidade comum.
                center_energy=(m1*(u1-r["v"])**2+m2*(u2-r["v"])**2)/2
                self.assertEqual(r["loss"],center_energy)
                self.assertGreaterEqual(r["loss"],0)
                self.assertEqual(r["loss"]==0,u1==u2)
    def test_boost_mass_scale_and_label_exchange(self):
        for m1,m2,u1,u2 in product((1,2,3),repeat=4):
            r=stick(m1,m2,u1,u2)
            s=stick(m2,m1,u2,u1)
            for key in ("v","loss","p_before","p_after","k_before","k_after"):
                self.assertEqual(r[key],s[key])
            self.assertEqual(r["impulse1"],s["impulse2"])
            for boost in (-7,0,5):
                b=stick(m1,m2,u1+boost,u2+boost)
                self.assertEqual(b["v"],r["v"]+boost)
                self.assertEqual(b["loss"],r["loss"])
                self.assertEqual(b["impulse1"],r["impulse1"])
                self.assertEqual(b["p_before"],r["p_before"]+(m1+m2)*boost)
            for scale in (Q(1,2),3):
                s=stick(scale*m1,scale*m2,u1,u2)
                self.assertEqual(s["v"],r["v"])
                for key in ("loss","p_before","p_after","k_before","k_after","impulse1","impulse2"):
                    self.assertEqual(s[key],scale*r[key])
    def test_recover_momentum_from_supplied_impulse_and_duration(self):
        r=stick(2,1,3,-1)
        dt=Q(1,10)
        f1=r["impulse1"]/dt;f2=r["impulse2"]/dt
        self.assertEqual(3+f1*dt/2,r["v"])
        self.assertEqual(-1+f2*dt,r["v"])
        # Forças médias dependem de duração fornecida, não deduzida dos estados finais.
        self.assertEqual(r["impulse1"]/(2*dt),f1/2)
    def test_contracts_and_same_velocity_limit(self):
        self.assertEqual(stick(2,3,-2,-2)["loss"],0)
        for values in [(0,1,2,0),(-1,1,2,0),(True,1,2,0),(1,1,.5,0),(1,1,0,float("nan"))]:
            with self.assertRaises(ValueError):stick(*values)
