import contextlib,io,itertools,json,tempfile,unittest
from pathlib import Path
try:
    from .experiment import crosses,wilson,ensemble,main,CRITICAL
except ImportError:
    from experiment import crosses,wilson,ensemble,main,CRITICAL

def independent_union(grid):
    h,w=len(grid),len(grid[0]);top,bottom=h*w,h*w+1;parent=list(range(h*w+2))
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    def join(a,b):parent[find(a)]=find(b)
    for i in range(h):
        for j in range(w):
            if not grid[i][j]:continue
            node=i*w+j
            if i==0:join(node,top)
            if i==h-1:join(node,bottom)
            if i+1<h and grid[i+1][j]:join(node,(i+1)*w+j)
            if j+1<w and grid[i][j+1]:join(node,i*w+j+1)
    return find(top)==find(bottom)

class PercolationEnsembleTests(unittest.TestCase):
    def test_all_small_grids_independent_oracle(self):
        for h in range(1,4):
            for w in range(1,4):
                for cells in itertools.product((0,1),repeat=h*w):
                    grid=[cells[i*w:(i+1)*w] for i in range(h)]
                    self.assertEqual(crosses(grid),independent_union(grid))

    def test_exact_two_by_two_probability(self):
        for p in (0,.2,.5,.8,1):
            exact=0
            for bits in itertools.product((0,1),repeat=4):
                if crosses((bits[:2],bits[2:])):
                    count=sum(bits);exact+=p**count*(1-p)**(4-count)
            self.assertAlmostEqual(exact,2*p*p-p**4)

    def test_wilson_edges_and_symmetry(self):
        z=CRITICAL;lo,hi=wilson(0,100)
        self.assertAlmostEqual(lo,0);self.assertAlmostEqual(hi,z*z/(100+z*z))
        a=wilson(100,100);self.assertAlmostEqual(a[1],1)
        for k in (0,10,50,100):
            a=wilson(k,100);b=wilson(100-k,100)
            self.assertAlmostEqual(a[0],1-b[1]);self.assertAlmostEqual(a[1],1-b[0])
            self.assertLessEqual(a[0],k/100);self.assertGreaterEqual(a[1],k/100)

    def test_endpoints_and_reproduction(self):
        self.assertEqual(ensemble(8,20,0,42)['successes'],0)
        self.assertEqual(ensemble(8,20,1,42)['successes'],20)
        self.assertEqual(ensemble(4,50,.6,42),ensemble(4,50,.6,42))
        self.assertAlmostEqual(ensemble(2,20,.5,1)['exact_if_2x2'],.4375)

    def test_invalid_parameters(self):
        for args in ((0,20,.5,42),(2,0,.5,42),(2,20,float('nan'),42),(2,20,2,42),(2,20,.5,True)):
            with self.assertRaises(ValueError):ensemble(*args)
        for grid in ([],[[]],[[1],[1,0]],[['false']]):
            with self.assertRaises(ValueError):crosses(grid)

    def test_cli_and_preserve_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            output=Path(tmp)/'run.json';args=['--size','2','--samples','20','--p','0.5','--seed','1','--output',str(output)]
            self.assertEqual(main(args),0);data=json.loads(output.read_text())
            self.assertEqual(data['config']['occupation_p'],.5)
            self.assertEqual(data['result']['exact_if_2x2'],.4375)
            before=output.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()):self.assertEqual(main(args),2)
            self.assertEqual(before,output.read_bytes())

if __name__=='__main__':unittest.main()
