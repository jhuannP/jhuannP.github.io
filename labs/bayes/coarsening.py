"""Registros agrupados: aplicação original de probabilidade total e Bayes.
Executar deste diretório ou pelo caminho do arquivo; apenas biblioteca padrão.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import unittest
from stopping import table, posterior


def summarize(joint, records):
    """Retorna (massa do resumo, posterior, pesos dos registros).

    joint é a tabela exata produzida por stopping.table; zero evidência
    retorna posterior None e nenhum peso normalizado. Duplicatas não
    representam uma partição e são rejeitadas.
    """
    records = tuple(records)
    if len(set(records)) != len(records) or not set(records) <= joint.keys():
        raise ValueError('Use registros distintos que existam na tabela')
    masses = [sum((joint[r][h] for r in records), Q(0)) for h in (0, 1)]
    evidence = sum(masses)
    weights = {r: sum(joint[r])/evidence for r in records} if evidence else {}
    return evidence, posterior(masses), weights


class Checks(unittest.TestCase):
    def test_weighted_example(self):
        t = table()
        mass, p, weights = summarize(t, ('1', '01', '001'))
        self.assertEqual(mass, Q(25,32))
        self.assertEqual(weights, {'1':Q(16,25), '01':Q(6,25), '001':Q(3,25)})
        self.assertEqual(p, Q(63,100))
        self.assertEqual(sum(posterior(t[r]) for r in weights)/3, Q(1,2))
        self.assertNotEqual(p, Q(1,2))

    def test_all_groupings(self):
        # 125 modelos e 16 subconjuntos de registros. A identidade geral
        # é demonstrada nas notas; a grade finita verifica a implementação.
        for prior, a, b in product((Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)), repeat=3):
            t = table(prior,a,b)
            for n in range(5):
                for records in combinations(t,n):
                    mass, p, weights = summarize(t,records)
                    # Expressão independente via verossimilhanças dos prefixos.
                    lh = [sum(((1-q)**3 if r=='000' else (1-q)**(len(r)-1)*q
                               for r in records),Q(0)) for q in (a,b)]
                    expected_mass = prior*lh[0]+(1-prior)*lh[1]
                    self.assertEqual(mass,expected_mass)
                    if mass:
                        self.assertEqual(p,prior*lh[0]/mass)
                        self.assertEqual(sum(weights.values()),1)
                        self.assertEqual(p,sum(weights[r]*posterior(t[r])
                                               for r in records if sum(t[r])))
                    else:
                        self.assertIsNone(p)
                        self.assertEqual(weights,{})
            self.assertEqual(summarize(t,t)[1],prior)

    def test_partition_contract(self):
        for records in [('1','1'),('invalid',)]:
            with self.assertRaises(ValueError): summarize(table(),records)
        self.assertEqual(summarize(table(),()),(0,None,{}))


if __name__ == '__main__':
    print('Resumo sucesso:', summarize(table(),('1','01','001')))
    unittest.main()
