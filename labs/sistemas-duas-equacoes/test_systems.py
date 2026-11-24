import itertools,unittest
from fractions import Fraction as Q
from .systems import solve,satisfies,combine,scale_row

# RREF independente da fórmula dos determinantes usada no módulo.
def by_elimination(values):
    mat=[list(map(Q,row)) for row in values];rank=0;pivots=[]
    for col in range(2):
        pos=next((i for i in range(rank,2) if mat[i][col]),None)
        if pos is None:continue
        mat[rank],mat[pos]=mat[pos],mat[rank]
        pivot=mat[rank][col];mat[rank]=[v/pivot for v in mat[rank]]
        for i in range(2):
            if i!=rank:
                factor=mat[i][col]
                mat[i]=[v-factor*u for v,u in zip(mat[i],mat[rank])]
        pivots.append(col);rank+=1
    if any(row[:2]==[0,0] and row[2] for row in mat):return 'nenhuma',None
    if rank<2:return 'infinitas',None
    return 'unica',(mat[0][2],mat[1][2])

class SchoolSystemTests(unittest.TestCase):
    def test_exhaustive_against_elimination(self):
        count=0
        for values in itertools.product([-1,0,1],repeat=6):
            model=[values[:3],values[3:]]
            result=solve(model)
            self.assertEqual(result,by_elimination(model))
            if result[0]=='unica':self.assertTrue(satisfies(model,result[1]))
            count+=1
        self.assertEqual(count,729)

    def test_original_models_and_context(self):
        model=[(3,2,94),(2,3,86)]
        self.assertEqual(solve(model),('unica',(22,14)))
        self.assertTrue(satisfies(model,[22,14]))
        self.assertFalse(satisfies(model,[24,11])) # Apenas a primeira conta.
        self.assertEqual(solve([(3,2,94),(6,4,188)])[0],'infinitas')
        self.assertEqual(solve([(3,2,94),(6,4,190)])[0],'nenhuma')
        status,point=solve([(1,1,1),(1,-1,3)])
        self.assertEqual((status,point),('unica',(2,-1)))
        self.assertFalse(all(v>=0 and v.denominator==1 for v in point))
        self.assertEqual(solve([(1,1,1),(1,-1,0)]),('unica',(Q(1,2),Q(1,2))))

    def test_reversible_row_operations(self):
        for model in [[(3,2,94),(2,3,86)],[(1,2,3),(2,4,6)],[(1,2,3),(2,4,7)],[(0,0,0),(0,0,0)]]:
            expected=solve(model)
            for m in [Q(-3,2),0,2]:
                changed=combine(model,m)
                self.assertEqual(solve(changed),expected)
                self.assertEqual(combine(changed,-m),tuple(tuple(Q(v) for v in row) for row in model))
            for i in (0,1):
                for m in [Q(-2),Q(1,3),3]:self.assertEqual(solve(scale_row(model,i,m)),expected)
        # Trocar todo o sistema apenas por sua soma perde informação.
        self.assertTrue(5*Q(18)+5*Q(18)==180)
        self.assertFalse(satisfies([(3,2,94),(2,3,86)],[18,18]))

    def test_scaling_and_graph(self):
        base=[(3,2,94),(2,3,86)]
        cents=[(3,2,9400),(2,3,8600)]
        self.assertEqual(solve(cents),('unica',(2200,1400)))
        # Leitura do gráfico por duas funções afins, sem chamar solve.
        x=Q(22);first=(94-3*x)/2;second=(86-2*x)/3
        self.assertEqual(first,second);self.assertEqual(first,14)
        self.assertEqual(solve([(1,0,2),(0,1,3)]),('unica',(2,3)))
        self.assertEqual(solve([(0,0,0),(0,0,1)]),('nenhuma',None))

    def test_contracts(self):
        for model in [[],[(1,2,3)],[(1,2),(3,4)],[(1,2,3,4),(1,2,3)]]:
            with self.assertRaises(ValueError):solve(model)
        for value in [True,.5,'1']:
            with self.assertRaises(TypeError):solve([(value,1,2),(1,1,3)])
        with self.assertRaises(ValueError):scale_row([(1,1,2),(1,-1,0)],0,0)
        with self.assertRaises(ValueError):scale_row([(1,1,2),(1,-1,0)],True,2)
        with self.assertRaises(ValueError):satisfies([(1,1,2),(1,-1,0)],[1])

if __name__=='__main__':unittest.main()
