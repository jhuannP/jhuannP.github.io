import unittest,itertools
try:
    from .tree import construir,inserir,caminho,em_ordem,altura,report
except ImportError:
    from tree import construir,inserir,caminho,em_ordem,altura,report

class TreeTests(unittest.TestCase):
    def assert_global_order(self,root,low=None,high=None):
        if root is None:return
        if low is not None:self.assertGreater(root.chave,low)
        if high is not None:self.assertLess(root.chave,high)
        self.assert_global_order(root.esq,low,root.chave)
        self.assert_global_order(root.dir,root.chave,high)

    def test_all_small_orders(self):
        for order in itertools.permutations(range(1,6)):
            root=construir(order)
            self.assert_global_order(root)
            self.assertEqual(em_ordem(root),list(range(1,6)))
            for target in range(7):
                result=caminho(root,target)
                self.assertEqual(result['encontrada'],target in order)
                self.assertLessEqual(len(result['visitados']),altura(root))
                if result['encontrada']:self.assertEqual(result['visitados'][-1],target)

    def test_known_shapes_paths_and_duplicate(self):
        self.assertEqual(report(0,7,7),dict(altura=7,em_ordem=list(range(1,8)),encontrada=True,visitados=list(range(1,8))))
        self.assertEqual(report(2,7,7)['visitados'],[4,6,7])
        self.assertEqual(report(2,7,7)['altura'],3)
        self.assertEqual(report(2,7,0)['visitados'],[4,2,1])
        root=construir([4,2,6,1,3,5,7]);before=em_ordem(root)
        self.assertIs(inserir(root,4),root);self.assertEqual(em_ordem(root),before)
        self.assertEqual(altura(root),3)

    def test_empty_and_long_chain(self):
        self.assertEqual(em_ordem(None),[]);self.assertEqual(altura(None),0)
        self.assertEqual(caminho(None,1),{'encontrada':False,'visitados':[]})
        root=construir(range(1200))
        self.assertEqual(altura(root),1200)
        self.assertEqual(em_ordem(root),list(range(1200)))
        self.assertEqual(len(caminho(root,1199)['visitados']),1200)

    def test_invalid_keys_and_controls(self):
        for key in [True,'1',1.5,None]:
            with self.assertRaises(TypeError):inserir(None,key)
            with self.assertRaises(TypeError):caminho(None,key)
        for mode,count in [(3,7),(-1,7),(True,7),(0,8),(0,True)]:
            with self.assertRaises(ValueError):report(mode,count,1)

if __name__=='__main__':unittest.main()
