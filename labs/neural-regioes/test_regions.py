import unittest
from .regions import ancestry, descendants, cavities_below, PARENT, PRIMARY, SECONDARY, NODES


class RegionTests(unittest.TestCase):
    def test_nine_literal_regional_paths(self):
        rows = [('cortex','prosencefalo','telencefalo'),
                ('bulbo_olfatorio','prosencefalo','telencefalo'),
                ('talamo','prosencefalo','diencefalo'),
                ('hipotalamo','prosencefalo','diencefalo'),
                ('teto','mesencefalo_primario','mesencefalo'),
                ('tegmento','mesencefalo_primario','mesencefalo'),
                ('ponte','rombencefalo','metencefalo'),
                ('cerebelo','rombencefalo','metencefalo'),
                ('bulbo','rombencefalo','mielencefalo')]
        for adult, primary, secondary in rows:
            self.assertEqual(ancestry(adult), ('tubo_rostral', primary, secondary, adult))

    def test_primary_secondary_partition_and_acyclicity(self):
        self.assertEqual(len(PRIMARY), 3)
        self.assertEqual(len(SECONDARY), 5)
        self.assertEqual(len(NODES), 18)
        for node in NODES:
            path = ancestry(node)
            self.assertEqual(len(path), len(set(path)))
            self.assertEqual(path[0], 'tubo_rostral')
        self.assertEqual({PARENT[s] for s in SECONDARY}, set(PRIMARY))

    def test_cavities_are_spaces_not_duplicate_regions(self):
        self.assertEqual(cavities_below('prosencefalo'), {'ventriculos_laterais', 'terceiro_ventriculo'})
        self.assertEqual(cavities_below('mesencefalo_primario'), {'aqueduto'})
        self.assertEqual(cavities_below('rombencefalo'), {'quarto_ventriculo'})
        self.assertEqual(cavities_below('metencefalo'), cavities_below('mielencefalo'))
        self.assertEqual(len(cavities_below('tubo_rostral')), 4)

    def test_similar_names_and_non_connection_meaning(self):
        self.assertNotEqual(ancestry('bulbo'), ancestry('bulbo_olfatorio'))
        self.assertNotIn('talamo', descendants('cortex'))
        self.assertIn('cerebelo', descendants('rombencefalo'))
        self.assertNotIn('cortex', descendants('rombencefalo'))
        self.assertEqual(cavities_below('cortex'), frozenset())
        # Vazio significa que o mapa não atribui uma cavidade a este nó.
        # Não afirma ausência de relação anatômica com ventrículos.

    def test_reject_unknown_or_wrong_kind(self):
        for node in ['quarto_ventriculo', 'retina', 'medula', 'SNP', '', None, True, []]:
            with self.assertRaises(ValueError): ancestry(node)
            with self.assertRaises(ValueError): cavities_below(node)
