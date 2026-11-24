import unittest
from itertools import product
from .balance import State,step

class BalanceTests(unittest.TestCase):
    def test_example_and_same_death_different_visibility(self):
        self.assertEqual(step(State(100,4),born=10,died=10,cleared=12),State(100,2))
        self.assertEqual(step(State(100,0),born=10,died=10,cleared=10),State(100,0))
        self.assertEqual(step(State(100,0),born=10,died=10,cleared=2),State(100,8))

    def test_independent_identified_objects_and_conservation(self):
        # Build distinct cells, then remove explicit identifiers; no recurrence as oracle.
        for n,c,b in product(range(5),repeat=3):
            for deaths in range(n+1):
                for removals in range(c+deaths+1):
                    living=[('initial',i) for i in range(n)]
                    dead=[('old-dead',i) for i in range(c)]
                    dead.extend(living[:deaths]);living=living[deaths:]
                    living.extend(('new',i) for i in range(b))
                    removed=dead[:removals];dead=dead[removals:]
                    actual=step(State(n,c),born=b,died=deaths,cleared=removals)
                    self.assertEqual((actual.alive,actual.awaiting),(len(living),len(dead)))
                    self.assertEqual(actual.alive+actual.awaiting+len(removed),n+c+b)

    def test_multiple_intervals_track_cumulative_removal(self):
        state=State(100,4);removed=0;born=0
        for b,d,c in ((10,10,12),(5,8,4),(3,0,2)):
            state=step(state,born=b,died=d,cleared=c);removed+=c;born+=b
            self.assertEqual(state.alive+state.awaiting+removed,104+born)
        self.assertEqual(state,State(100,4))

    def test_contracts_and_input_preservation(self):
        initial=State(5,2)
        for field in ('born','died','cleared'):
            for value in (True,1.5,'1'):
                kwargs=dict(born=0,died=0,cleared=0);kwargs[field]=value
                with self.assertRaises(TypeError):step(initial,**kwargs)
            kwargs=dict(born=0,died=0,cleared=0);kwargs[field]=-1
            with self.assertRaises(ValueError):step(initial,**kwargs)
        with self.assertRaises(ValueError):step(initial,born=10,died=6,cleared=0)
        with self.assertRaises(ValueError):step(initial,born=0,died=1,cleared=4)
        self.assertEqual(initial,State(5,2))

if __name__=='__main__':unittest.main()
