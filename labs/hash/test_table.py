import unittest,itertools
from random import Random
try:
    from .table import HashTable,raw_hash,trace
except ImportError:
    from table import HashTable,raw_hash,trace

class HashTests(unittest.TestCase):
    def test_collisions_updates_and_delete(self):
        t=HashTable();t.put('ab',1);t.put('ba',2);t.put('ad',None)
        before=t.snapshot();t.put('ab',9)
        self.assertEqual(len(t),3);self.assertEqual(t.capacity,4)
        self.assertEqual(t.migrated,before['migrated'])
        self.assertEqual(t.get('ab'),9);self.assertEqual(t.get('ba'),2);self.assertIsNone(t.get('ad'))
        self.assertEqual(t.delete('ba'),2);self.assertEqual(t.get('ab'),9)
        before=t.snapshot()
        for method in [t.get,t.delete]:
            with self.assertRaises(KeyError):method('missing')
            self.assertEqual(t.snapshot(),before)
        self.assertTrue(t.invariant())

    def test_growth_recomputes_indices(self):
        t=HashTable();t.put('ab',1);t.put('ba',2);t.put('ad',3)
        self.assertEqual(t.index('ad'),1)
        t.put('x',4)
        self.assertEqual(t.capacity,8);self.assertEqual(t.migrated,3)
        self.assertEqual(t.index('ad'),5);self.assertEqual(t.get('ad'),3)
        self.assertEqual(t.index('ab'),t.index('ba')) # Colisão persistente.
        self.assertTrue(t.invariant())

    def test_against_dict(self):
        keys=['','ab','ba','ad','x','y','😀','á']
        for mode in ['sum','poly','constant']:
            for limit in [.5,.75,2]:
                t=HashTable(2,limit,mode);reference={};rng=Random(42)
                for i in range(1000):
                    key=rng.choice(keys);operation=rng.randrange(3)
                    if operation==0:t.put(key,i);reference[key]=i
                    elif operation==1:
                        if key in reference:self.assertEqual(t.delete(key),reference.pop(key))
                        else:
                            with self.assertRaises(KeyError):t.delete(key)
                    else:
                        if key in reference:self.assertEqual(t.get(key),reference[key])
                        else:
                            with self.assertRaises(KeyError):t.get(key)
                    self.assertEqual(len(t),len(reference));self.assertTrue(t.invariant())
                    self.assertEqual(dict(pair for bucket in t.snapshot()['buckets'] for pair in bucket),reference)

    def test_adversarial_and_permutations(self):
        keys=[''.join(x) for x in itertools.permutations('abcd')]
        t=HashTable(mode='sum')
        for i,key in enumerate(keys):t.put(key,i)
        self.assertEqual(t.snapshot()['longest'],24)
        self.assertEqual(len({t.index(k) for k in keys}),1)
        self.assertTrue(t.invariant()) # Carga controlada não garante dispersão.
        for i,key in enumerate(keys):self.assertEqual(t.get(key),i)
        self.assertNotEqual(raw_hash('ab','poly'),raw_hash('ba','poly'))

    def test_contracts_and_snapshots(self):
        for capacity in [0,1,True,2.5]:
            with self.assertRaises(ValueError):HashTable(capacity)
        for load in [True,0,float('nan'),3]:
            with self.assertRaises(ValueError):HashTable(max_load=load)
        with self.assertRaises(ValueError):HashTable(mode='unknown')
        t=HashTable()
        for method in [t.get,t.delete,t.index]:
            with self.assertRaises(TypeError):method(3)
        t.put('x',1);s=t.snapshot();s['buckets'][t.index('x')].clear()
        self.assertEqual(t.get('x'),1)
        self.assertEqual(trace()[4]['migrated'],3)

if __name__=='__main__':unittest.main()
