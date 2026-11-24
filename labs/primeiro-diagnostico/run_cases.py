"""Executa apenas os exemplos didáticos fixos locais. Não é avaliador web de código."""
from pathlib import Path
import json,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parent

def observe(source):
    with tempfile.TemporaryDirectory(prefix='primeiro-diagnostico-') as name:
        path=Path(name)/'exemplo.py';path.write_text(source,encoding='utf-8')
        result=subprocess.run([sys.executable,str(path)],capture_output=True,text=True,encoding='utf-8',timeout=3)
    return dict(returncode=result.returncode,stdout=result.stdout,stderr=result.stderr)

if __name__=='__main__':
    examples=json.loads((ROOT/'cases.json').read_text(encoding='utf-8'))
    examples['correto']=(ROOT/'viagem.py').read_text(encoding='utf-8')
    for label,source in examples.items():
        print(label,json.dumps(observe(source),ensure_ascii=False))
