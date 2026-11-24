"""Contagem original de rótulos: strip -> casefold -> NFC; vazios descartados."""
from unicodedata import normalize
from itertools import product
import unittest


def canonical(label):
    if type(label) is not str: raise TypeError('Rótulo precisa ser string')
    return normalize('NFC', label.strip().casefold())


def count_labels(labels):
    if type(labels) not in (list, tuple): raise TypeError('Use lista ou tupla de rótulos')
    frequencies={}; skipped=0
    for label in labels:
        key=canonical(label)
        if not key:
            skipped += 1
            continue
        frequencies[key]=frequencies.get(key,0)+1
    return {'counts':frequencies,'accepted':sum(frequencies.values()),'skipped':skipped}


def ranked(result):
    return sorted(result['counts'].items(), key=lambda item:(-item[1],item[0]))


EXAMPLE=[' FÍSICA ', 'fi'+chr(0x301)+'sica', 'Física,', 'fisica', ' ', 'CÓDIGO']


class Checks(unittest.TestCase):
    def test_unicode_and_policy(self):
        self.assertEqual(canonical(' FÍSICA '), canonical('fi'+chr(0x301)+'sica'))
        self.assertNotEqual(canonical('física'),canonical('fisica'))
        self.assertNotEqual(canonical('física,'),canonical('física'))
        self.assertEqual(canonical('Straße'),canonical('STRASSE'))
        self.assertEqual(canonical('  '),'')
        self.assertEqual(canonical('a  b'),'a  b')
        for label in EXAMPLE:
            self.assertEqual(canonical(canonical(label)),canonical(label))

    def test_example_and_no_mutation(self):
        before=EXAMPLE.copy(); actual=count_labels(EXAMPLE)
        self.assertEqual(EXAMPLE,before)
        self.assertEqual(actual,{'counts':{'física':2,'física,':1,'fisica':1,'código':1},'accepted':5,'skipped':1})
        self.assertEqual(ranked(actual),[('física',2),('código',1),('fisica',1),('física,',1)])
        self.assertEqual(list(actual['counts']),['física','física,','fisica','código'])
        self.assertEqual(count_labels([]),{'counts':{},'accepted':0,'skipped':0})

    def test_enumeration_against_list_count(self):
        alphabet=(' A ','a','B','b,','','é','e'+chr(0x301))
        configurations=0
        for n in range(5):
            for values in product(alphabet,repeat=n):
                result=count_labels(values)
                keys=[canonical(x) for x in values if canonical(x)]
                # Referência por contagem em lista, sem atualização incremental de dict.
                reference={key:keys.count(key) for key in set(keys)}
                self.assertEqual(result['counts'],reference)
                self.assertEqual(result['accepted'],len(keys))
                self.assertEqual(result['accepted']+result['skipped'],len(values))
                self.assertTrue(all(v>0 for v in result['counts'].values()))
                self.assertEqual(result['counts'],count_labels(tuple(reversed(values)))['counts'])
                self.assertEqual(ranked(result),ranked(count_labels(tuple(reversed(values)))))
                configurations+=1
        self.assertEqual(configurations,2801)
        print('Entradas enumeradas:',configurations)

    def test_batches_and_insertion_are_distinct(self):
        all_counts=count_labels(EXAMPLE)
        left=count_labels(EXAMPLE[:3]); right=count_labels(EXAMPLE[3:])
        keys=set(left['counts'])|set(right['counts'])
        merged={k:left['counts'].get(k,0)+right['counts'].get(k,0) for k in keys}
        self.assertEqual(merged,all_counts['counts'])
        self.assertEqual(left['accepted']+right['accepted'],all_counts['accepted'])
        self.assertEqual(left['skipped']+right['skipped'],all_counts['skipped'])
        reversed_counts=count_labels(list(reversed(EXAMPLE)))
        self.assertNotEqual(list(all_counts['counts']),list(reversed_counts['counts']))
        missing={}
        self.assertEqual(missing.get('x',0),0)
        self.assertEqual(len(missing),0)

    def test_contracts(self):
        for labels in ('abc',None,42,{'a':2}):
            with self.assertRaises(TypeError):count_labels(labels)
        for label in (None,1,True,[],1.0):
            with self.assertRaises(TypeError):count_labels(['válido',label])


if __name__=='__main__':
    print(count_labels(EXAMPLE))
    unittest.main()
