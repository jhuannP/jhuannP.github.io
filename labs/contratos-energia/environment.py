"""Registro restrito de ambiente e conferência dos arquivos de um pacote extraído."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys

SOURCE_FILES=("labs/__init__.py","labs/build_energy_bundle.py")+tuple("labs/contratos-energia/"+name for name in (
    "__init__.py","energy.py","pipeline.py","environment.py","measurements.json",
    "test_energy.py","test_pipeline.py","test_environment.py","README.md"))

def report():
    return {"schema_version":1,"python":platform.python_version(),
            "implementation":platform.python_implementation(),"system":platform.system(),
            "machine":platform.machine(),"external_dependencies":[],
            "float":{"radix":sys.float_info.radix,"mant_dig":sys.float_info.mant_dig,
                     "max_exp":sys.float_info.max_exp,"min_exp":sys.float_info.min_exp}}

def verify_manifest(root):
    root=Path(root)
    manifest=json.loads((root/"MANIFEST.json").read_text(encoding="utf-8"))
    expected=set(SOURCE_FILES)|{"LEIA-ME.md","BUILD_ENVIRONMENT.json"}
    if type(manifest) is not dict or set(manifest)!=expected:
        raise ValueError("Manifesto com conjunto de arquivos inesperado")
    mismatches=[]
    for name in sorted(expected):
        digest=manifest[name]
        if type(digest) is not str or len(digest)!=64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError("Digest inválido no manifesto")
        path=root/name
        try:actual=hashlib.sha256(path.read_bytes()).hexdigest()
        except OSError:mismatches.append(name);continue
        if actual!=digest:mismatches.append(name)
    return mismatches

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify",action="store_true",help="Conferir manifesto na raiz do pacote extraído")
    args=parser.parse_args(argv)
    try:
        if args.verify:
            differences=verify_manifest(Path(__file__).resolve().parents[2])
            print(json.dumps({"listed_files_match":not differences,"differences":differences},ensure_ascii=False,sort_keys=True))
            return 1 if differences else 0
        print(json.dumps(report(),ensure_ascii=False,sort_keys=True,indent=2))
    except (OSError,ValueError) as error:
        print("Erro: "+str(error),file=sys.stderr);return 2
    return 0

if __name__=="__main__":raise SystemExit(main())
