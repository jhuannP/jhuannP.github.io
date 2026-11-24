import unittest
from itertools import product
from .experiment import CATALOG,carbon_state,states,transition

class OrganicRedoxTests(unittest.TestCase):
    def test_reference_local_states(self):
        expected={"ethanol":(-3,-1),"ethanal":(-3,1),"ethanoic_acid":(-3,3),
                  "propan_2_ol":(-3,0,-3),"propanone":(-3,2,-3)}
        for name,answer in expected.items():self.assertEqual(states(name),answer)
        self.assertEqual(transition("ethanol","ethanoic_acid")["electron_equivalents"],4)

    def test_neutral_formula_and_local_valence(self):
        for name,data in CATALOG.items():
            C,H,O=data["formula"]
            self.assertEqual(C,len(data["carbons"]))
            self.assertEqual(sum(states(name))+H-2*O,0)
            for h,o,c in data["carbons"]:
                self.assertEqual(h+o+c,4)
                self.assertEqual(carbon_state(h,o,c),o-h)

    def test_all_same_family_half_reactions_balance(self):
        for start,end in product(CATALOG,repeat=2):
            if CATALOG[start]["family"]!=CATALOG[end]["family"]:continue
            r=transition(start,end)
            ca,ha,oa=CATALOG[start]["formula"];cb,hb,ob=CATALOG[end]["formula"]
            self.assertEqual(ca,cb)
            self.assertEqual(oa+r["water_left"],ob)
            self.assertEqual(ha+2*r["water_left"],hb+r["protons_right"])
            self.assertEqual(r["protons_right"]-r["electrons_right"],0)
            self.assertEqual(sum(r["delta"]),r["electrons_right"])

    def test_reverse_and_additive_bookkeeping(self):
        a=transition("ethanol","ethanal");b=transition("ethanal","ethanoic_acid")
        full=transition("ethanol","ethanoic_acid")
        reverse=transition("ethanal","ethanol")
        for field in ("water_left","protons_right","electrons_right","electron_equivalents"):
            self.assertEqual(a[field]+b[field],full[field])
            self.assertEqual(reverse[field],-a[field])
        self.assertEqual(a["water_left"],0)
        self.assertEqual(b["water_left"],1)

    def test_contracts_and_mapping_limit(self):
        for args in ((True,1,2),(-1,1,4),(1.,1,2),(0,2,1)):
            with self.assertRaises(ValueError):carbon_state(*args)
        for pair in (("ethanol","propanone"),("unknown","ethanal"),(True,"ethanol")):
            with self.assertRaises(ValueError):transition(*pair)
