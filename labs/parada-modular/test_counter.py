import unittest
from .counter import classify

class CounterTests(unittest.TestCase):
    def test_original_four_state_family(self):
        results=[classify(x,d,4) for x in range(4) for d in range(4)]
        self.assertEqual(sum(r.status=='parada' for r in results),11)
        self.assertEqual(classify(1,1,4).steps,3)
        self.assertEqual(classify(1,2,4).cycle_length,2)
        self.assertEqual(classify(1,0,4).cycle_length,1)

    def test_independent_explicit_state_enumeration(self):
        # Oracle uses only transitions, no gcd or modular inverse.
        for modulus in range(1,41):
            for initial in range(modulus):
                for increment in range(modulus):
                    state=initial;seen={};steps=0
                    while state!=0 and state not in seen:
                        seen[state]=steps
                        state=(state+increment)%modulus;steps+=1
                    result=classify(initial,increment,modulus)
                    if state==0:
                        self.assertEqual((result.status,result.steps,result.cycle_length),('parada',steps,None))
                    else:
                        self.assertEqual((result.status,result.steps,result.cycle_length),('ciclo',None,steps-seen[state]))

    def test_large_integer_case_without_trajectory(self):
        # Construct a known first hitting time k=12345 with d=1.
        modulus=10**100+1;initial=modulus-12345
        self.assertEqual(classify(initial,1,modulus).steps,12345)
        # Odd start stays odd with even increment and even modulus.
        result=classify(1,2,10**100)
        self.assertEqual(result.status,'ciclo')
        self.assertEqual(result.cycle_length,5*10**99)

    def test_contracts(self):
        for values in ((True,1,4),(1,1.0,4),(1,1,'4')):
            with self.assertRaises(TypeError):classify(*values)
        for values in ((0,0,0),(-1,1,4),(4,1,4),(1,-1,4),(1,4,4)):
            with self.assertRaises(ValueError):classify(*values)
        self.assertEqual(classify(0,0,1).steps,0)

if __name__=='__main__':unittest.main()
