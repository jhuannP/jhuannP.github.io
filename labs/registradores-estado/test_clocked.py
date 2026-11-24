import itertools
import unittest
from .clocked import step
class RegisterTests(unittest.TestCase):
    def test_trace_and_sequential_counterexample(self):
        q=(0,0);trace=[]
        for d in (1,0,1):q=step(q,d);trace.append(q)
        self.assertEqual(trace,[(1,0),(0,1),(1,0)])
        a,b=0,0;a=1;b=a # intentionally incorrect update
        self.assertEqual((a,b),(1,1));self.assertNotEqual((a,b),step((0,0),1))

    def test_exhaustive_enable_reset_and_immutable_input(self):
        for a,b,d,ea,eb,rst in itertools.product((0,1),repeat=6):
            old=(a,b);new=step(old,d,(ea,eb),rst)
            if rst:self.assertEqual(new,(0,0))
            else:
                # Written component equals its pre-edge source; disabled one is preserved.
                self.assertEqual(new[0],d if ea==1 else old[0])
                self.assertEqual(new[1],old[0] if eb==1 else old[1])
            self.assertEqual(old,(a,b))

    def test_two_stage_delay_and_no_implicit_reset(self):
        for seq in itertools.product((0,1),repeat=6):
            q=(0,0)
            for i,d in enumerate(seq):
                q=step(q,d)
                self.assertEqual(q,(d,seq[i-1] if i else 0))
        self.assertEqual(step((1,1),0,(0,0)),(1,1))
        self.assertEqual(step((1,1),1,(0,0),1),(0,0))
        self.assertEqual(step((1,0),0,(0,1)),(1,1))

    def test_contracts(self):
        for args in [([0,0],1),((0,),1),((0,False),1),((0,0),True),((0,0),2)]:
            with self.assertRaises(ValueError):step(*args)
        with self.assertRaises(ValueError):step((0,0),1,(1,2))
if __name__=='__main__':unittest.main()
