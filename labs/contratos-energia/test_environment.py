import importlib
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from zipfile import ZipFile
from .environment import report,verify_manifest,SOURCE_FILES

class EnvironmentTests(unittest.TestCase):
    def test_report_is_explicit_and_minimal(self):
        data=report()
        self.assertEqual(set(data),{'schema_version','python','implementation','system','machine','external_dependencies','float'})
        self.assertEqual(data['external_dependencies'],[])
        self.assertTrue(data['python'])
        self.assertEqual(set(data['float']),{'radix','mant_dig','max_exp','min_exp'})

    def test_bundle_extracts_and_runs_without_external_packages(self):
        builder=importlib.import_module('labs.build_energy_bundle')
        raw=builder.build_bytes()
        self.assertEqual(raw,builder.build_bytes())
        with TemporaryDirectory() as folder:
            root=Path(folder)
            with ZipFile(BytesIO(raw)) as archive:
                self.assertEqual(set(archive.namelist()),set(SOURCE_FILES)|{'LEIA-ME.md','BUILD_ENVIRONMENT.json','MANIFEST.json'})
                self.assertTrue(all(not name.startswith('/') and '..' not in Path(name).parts for name in archive.namelist()))
                archive.extractall(root)
            self.assertEqual(verify_manifest(root),[])
            result=subprocess.run([sys.executable,'-S','-m','labs.contratos-energia.pipeline','labs/contratos-energia/measurements.json'],cwd=root,text=True,capture_output=True)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(result.stdout)['energies'],[24,400,0])
            check=subprocess.run([sys.executable,'-S','-m','labs.contratos-energia.environment','--verify'],cwd=root,text=True,capture_output=True)
            self.assertEqual(check.returncode,0,check.stderr)
            self.assertTrue(json.loads(check.stdout)['listed_files_match'])
            # Tampering and missing source are detected without executing the altered file.
            source=root/'labs/contratos-energia/energy.py';source.write_bytes(source.read_bytes()+b'\n# modificado\n')
            self.assertEqual(verify_manifest(root),['labs/contratos-energia/energy.py'])
            source.unlink()
            self.assertEqual(verify_manifest(root),['labs/contratos-energia/energy.py'])

    def test_manifest_cannot_choose_arbitrary_paths(self):
        with TemporaryDirectory() as folder:
            root=Path(folder)
            for data in ({'../private':'0'*64},[],{}):
                (root/'MANIFEST.json').write_text(json.dumps(data))
                with self.assertRaises(ValueError):verify_manifest(root)
