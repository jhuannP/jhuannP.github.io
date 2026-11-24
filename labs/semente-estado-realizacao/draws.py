"""Execução pseudoaleatória local e referência matemática finita original."""
from random import Random
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from pathlib import Path
from hashlib import sha256
import random
import platform
import sys
import json
import unittest


def count(n):
    if type(n) is not int or n <= 0: raise ValueError('Quantidade inteira positiva')
    return n


def block(rng, n):
    count(n)
    if type(rng) is not Random: raise TypeError('Este exemplo exige random.Random')
    return tuple(rng.randrange(1, 7) for _ in range(n))


def realization(seed, n):
    if type(seed) is not int or seed < 0: raise ValueError('Semente inteira não negativa')
    return block(Random(seed), n)


def mean(values):
    values=tuple(values)
    if not values or any(type(x) is not int or not 1 <= x <= 6 for x in values):
        raise ValueError('Lista não vazia de resultados inteiros1..6')
    return Q(sum(values), len(values))


def exact_distribution(n):
    count(n)
    if n > 4: raise ValueError('Enumeração limitada a N≤4 neste laboratório')
    counts=Counter(mean(values) for values in product(range(1, 7), repeat=n))
    return {value: Q(frequency, 6**n) for value, frequency in counts.items()}


def report(seed=42, n=12):
    values=realization(seed, n)
    return {'schema':1,'seed':seed,'draws':n,'generator':'random.Random / Mersenne Twister',
            'sampler':'randrange(1, 7), uma chamada por dado',
            'schedule':'sequencial; uma instância criada antes do lote',
            'python_implementation':platform.python_implementation(),
            'python_version':platform.python_version(),'platform':sys.platform,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'values':list(values),'mean_fraction':str(mean(values)),
            'scope':'realização sintética; sem validação empírica do gerador ou do modelo'}


class Checks(unittest.TestCase):
    def test_local_repeat_and_global_isolation(self):
        before=random.getstate()
        a=realization(42, 12)
        random_other=Random(99)
        for _ in range(20): random_other.random()
        self.assertEqual(a, realization(42, 12))
        self.assertEqual(before, random.getstate())
        rng=Random(42)
        self.assertEqual(block(rng, 4)+block(rng, 8), a)

    def test_checkpoint_restores_continuation(self):
        rng=Random(42)
        prefix=block(rng, 5)
        saved=rng.getstate()
        tail=block(rng, 7)
        rng.setstate(saved)
        self.assertEqual(block(rng, 7), tail)
        self.assertEqual(prefix+tail, realization(42, 12))

    def test_exact_moments_from_all_tuples(self):
        total=0
        for n in range(1, 5):
            distribution=exact_distribution(n)
            self.assertEqual(sum(distribution.values()), 1)
            expected=sum(x*p for x,p in distribution.items())
            variance=sum((x-expected)**2*p for x,p in distribution.items())
            self.assertEqual(expected, Q(7, 2))
            self.assertEqual(variance, Q(35, 12*n))
            self.assertEqual(distribution[Q(6)], Q(1, 6**n))
            total += 6**n
        self.assertEqual(total, 1554)
        print('Tuplas enumeradas:', total)

    def test_reinitialization_is_not_replication_of_model(self):
        copies=[mean(realization(42, 4)) for _ in range(20)]
        average=sum(copies)/len(copies)
        empirical=sum((x-average)**2 for x in copies)/len(copies)
        self.assertEqual(len(set(copies)), 1)
        self.assertEqual(empirical, 0)
        self.assertNotEqual(empirical, Q(35, 48))
        r=report()
        self.assertEqual(r, report())
        self.assertEqual(r['mean_fraction'], str(mean(r['values'])))
        self.assertEqual(len(r['source_sha256']), 64)

    def test_contracts(self):
        for n in (0,-1,True,1.5):
            with self.assertRaises(ValueError): realization(42,n)
        for seed in (-1,True,.5,'42'):
            with self.assertRaises(ValueError): realization(seed,4)
        with self.assertRaises(TypeError): block(None,4)
        for values in ([],[True],[0],[7],[1.0]):
            with self.assertRaises(ValueError): mean(values)
        with self.assertRaises(ValueError): exact_distribution(5)


if __name__ == '__main__':
    if sys.argv[1:] == ['--report']:
        print(json.dumps(report(), ensure_ascii=False, indent=2))
    else:
        unittest.main()
