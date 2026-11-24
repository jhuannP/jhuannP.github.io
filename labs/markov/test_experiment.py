import contextlib,io,json,tempfile,unittest
from pathlib import Path
try:
    from .experiment import matrix,distributions,simulate,draw_state,main
except ImportError:
    from experiment import matrix,distributions,simulate,draw_state,main

P=[[.8,.2],[.4,.6]]
class MarkovLabTests(unittest.TestCase):
    def test_closed_form_and_mass(self):
        trace=distributions(P,0,20)
        for t,row in enumerate(trace):
            self.assertAlmostEqual(row[0],2/3+(.4**t)/3)
            self.assertAlmostEqual(sum(row),1)
            self.assertTrue(all(0<=x<=1 for x in row))
        self.assertAlmostEqual(trace[2][0],.72)

    def test_stationary_does_not_imply_convergence(self):
        flip=[[0,1],[1,0]]
        trace=distributions(flip,0,4)
        self.assertEqual(trace,[[1,0],[0,1],[1,0],[0,1],[1,0]])
        stationary=[.5,.5]
        self.assertEqual([sum(stationary[i]*flip[i][j] for i in range(2)) for j in range(2)],stationary)
        self.assertEqual(simulate(flip,0,4,20,42)['frequencies'],trace)

    def test_generic_cycle_and_identity(self):
        P3=[[0,1,0],[0,0,1],[1,0,0]]
        self.assertEqual(distributions(P3,0,3)[-1],[1,0,0])
        self.assertEqual(simulate(P3,0,3,5,42)['counts'][-1],[5,0,0])
        self.assertEqual(distributions([[1,0],[0,1]],1,3),[[0,1]]*4)
        self.assertEqual(draw_state((.8,.2),.79),0)
        self.assertEqual(draw_state((.8,.2),.8),1)

    def test_repetition_and_counts(self):
        a=simulate(P,0,10,100,42);b=simulate(P,0,10,100,42)
        self.assertEqual(a,b)
        self.assertEqual(a['counts'][0],[100,0])
        for row in a['counts']:self.assertEqual(sum(row),100)

    def test_invalid_and_rounding_contract(self):
        for Pbad in ([],[[.5,.5]],[[1.1,-.1],[0,1]],[[.2,.2],[0,1]],[[True,0],[0,1]]):
            with self.assertRaises((ValueError,TypeError)):matrix(Pbad)
        normalized=matrix([[.5,.5+1e-13],[0,1]])
        self.assertAlmostEqual(sum(normalized[0]),1)
        with self.assertRaises(ValueError):simulate(P,0,3,0,42)
        with self.assertRaises(ValueError):simulate(P,True,3,10,42)

    def test_cli_report_and_preserve_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);source=root/'matrix.json';output=root/'run.json';source.write_text(json.dumps(P))
            args=['--matrix',str(source),'--steps','2','--samples','20','--output',str(output)]
            self.assertEqual(main(args),0);record=json.loads(output.read_text())
            self.assertAlmostEqual(record['result']['distribution_trace'][2][0],.72)
            self.assertEqual(record['input']['name'],'matrix.json')
            before=output.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()):self.assertEqual(main(args),2)
            self.assertEqual(before,output.read_bytes())

if __name__=='__main__':unittest.main()
