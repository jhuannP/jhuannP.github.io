from decimal import Decimal,localcontext
from fractions import Fraction
from pathlib import Path
import tempfile
import unittest
from .model import solve
from .record import EXAMPLE,encode,decode,identity,known_sources,build,verify,replay,write_bundle

ENV={'python':'test-fixture','implementation':'test-fixture','system':'test-fixture'}


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.sources=known_sources();self.bundle=build(encode(EXAMPLE),self.sources,ENV)

    def test_reference_replay_and_accuracy(self):
        self.assertEqual(verify(self.bundle),[]);self.assertEqual(replay(self.bundle,self.sources),[])
        endpoint=decode(self.bundle['result.json'])['endpoint']
        self.assertEqual(endpoint,dict(numerator=81,denominator=256))
        self.assertEqual(solve({**EXAMPLE,'steps':2}),Fraction(1,4))
        with localcontext() as c:
            c.prec=60
            error=Decimal(81)/256-(-Decimal(1)).exp()
            self.assertTrue(Decimal('-.052')<error<Decimal('-.051'))
        other_env={**ENV,'system':'different-test-system'}
        other=build(encode(EXAMPLE),self.sources,other_env)
        self.assertNotEqual(other['manifest.json'],self.bundle['manifest.json'])
        self.assertEqual(other['result.json'],self.bundle['result.json'])

    def test_bytes_and_meaning_differ(self):
        spaced=b'{ "steps": 4, "initial": "1", "duration_s": "1", "rate_s_inv": "1" }\n'
        other=build(spaced,self.sources,ENV)
        self.assertEqual(decode(spaced),decode(self.bundle['config.json']))
        self.assertNotEqual(identity(spaced),identity(self.bundle['config.json']))
        self.assertEqual(other['result.json'],self.bundle['result.json'])
        tampered=dict(self.bundle);tampered['config.json']+=b' '
        self.assertIn('config.json identity differs',verify(tampered))

    def test_rehashed_wrong_result(self):
        altered=dict(self.bundle)
        altered['result.json']=encode({'endpoint':{'numerator':1,'denominator':1},'unit':'U'})
        manifest=decode(altered['manifest.json']);manifest['artifacts']['result.json']=identity(altered['result.json'])
        altered['manifest.json']=encode(manifest)
        self.assertEqual(verify(altered),[]) # An unsigned manifest can be rewritten.
        self.assertEqual(replay(altered,self.sources),['result differs on known-model replay'])

    def test_source_is_not_executed_from_bundle(self):
        altered=dict(self.bundle);altered['model.py']=b'raise RuntimeError("This is data, not executable replay")\n'
        manifest=decode(altered['manifest.json']);manifest['artifacts']['model.py']=identity(altered['model.py'])
        altered['manifest.json']=encode(manifest)
        self.assertEqual(verify(altered),[])
        self.assertEqual(replay(altered,self.sources),['source differs from known local implementation'])

    def test_write_and_refuse_existing_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            out=Path(temp)/'example';write_bundle(self.bundle,out)
            reread={p.name:p.read_bytes() for p in out.iterdir()}
            self.assertEqual(reread,self.bundle);self.assertEqual(replay(reread,self.sources),[])
            with self.assertRaises(FileExistsError):write_bundle(self.bundle,out)
            self.assertEqual({p.name:p.read_bytes() for p in out.iterdir()},reread)

    def test_contracts(self):
        for raw in [b'{"x":1,"x":2}',b'{"x":NaN}',b'{"x":Infinity}',b'\xff',b' '*16385]:
            with self.assertRaises((ValueError,UnicodeError)):decode(raw)
        for config in [{**EXAMPLE,'steps':True},{**EXAMPLE,'steps':0},{**EXAMPLE,'steps':129},
                       {**EXAMPLE,'rate_s_inv':'-1'},{**EXAMPLE,'duration_s':'0'},
                       {**EXAMPLE,'rate_s_inv':'NaN'},{**EXAMPLE,'initial':1.0},
                       {**EXAMPLE,'rate_s_inv':'5'},{**EXAMPLE,'extra':1}]:
            with self.assertRaises(ValueError):solve(config)
        missing=dict(self.bundle);del missing['model.py'];self.assertTrue(verify(missing))
        with self.assertRaises(ValueError):encode({'x':float('nan')})

if __name__=='__main__':unittest.main()
