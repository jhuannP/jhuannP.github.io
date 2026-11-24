import math,unittest
from .experiment import fatorial,potencia,soma_recursiva,trace


class RecursionTests(unittest.TestCase):
    def test_independent_references(self):
        for n in range(121):
            self.assertEqual(fatorial(n),math.factorial(n))
            self.assertEqual(soma_recursiva(n),n*(n+1)//2)
            for base in (-3,-1,0,1,2,5):self.assertEqual(potencia(base,n),pow(base,n))

    def test_replay_stack_and_continuations(self):
        # Replay only the event stream with an independent explicit stack machine.
        for kind in (0,1):
            for n in range(11):
                t=trace(kind,n);stack=[];child=None;calls=mults=peak=0
                for e in t['events']:
                    if e['event']=='entrada':
                        m=e['arg']
                        if stack:self.assertEqual(m,stack[-1]-1 if kind==0 else stack[-1]//2)
                        stack.append(m);calls+=1;peak=max(peak,len(stack))
                        self.assertEqual([f['n'] for f in e['stack']],stack)
                    elif e['event']=='retorno':
                        m=stack[-1];self.assertEqual(m,e['arg'])
                        if m==0:expected=1
                        elif kind==0:expected=m*child;mults+=1
                        else:
                            expected=child*child;mults+=1
                            if m%2:expected*=2;mults+=1
                        self.assertEqual(e['value'],expected);child=expected
                        self.assertEqual([f['n'] for f in e['stack']],stack)
                        stack.pop()
                    else:self.assertEqual(stack,[]);self.assertEqual(e['value'],child)
                    self.assertEqual(e['calls'],calls);self.assertEqual(e['mults'],mults);self.assertEqual(e['peak'],peak)
                self.assertEqual(child,math.factorial(n) if kind==0 else 2**n)
                self.assertEqual(len(t['events']),2*calls+1)

    def test_costs_and_snapshot_independence(self):
        for n in range(11):
            f=trace(0,n);p=trace(1,n)
            self.assertEqual((f['calls'],f['peak'],f['mults']),(n+1,n+1,n))
            self.assertEqual((p['calls'],p['peak'],p['mults']),(n.bit_length()+1,n.bit_length()+1,n.bit_length()+n.bit_count()))
            self.assertEqual(f['events'][0]['stack'][0]['state'],'executando')
            if n:self.assertEqual(f['events'][1]['stack'][0]['state'],'aguardando')
            self.assertEqual(f['events'][-1]['stack'],[])

    def test_contract_and_zero(self):
        self.assertEqual(potencia(0,0),1) # Convention for the empty integer product.
        for bad in (-1,1.5,True,'4'):
            for func in (fatorial,soma_recursiva):
                with self.assertRaises(ValueError):func(bad)
            with self.assertRaises(ValueError):potencia(2,bad)
            with self.assertRaises(ValueError):trace(0,bad)
        with self.assertRaises(ValueError):trace(0,11)
        with self.assertRaises(ValueError):trace(2,4)
