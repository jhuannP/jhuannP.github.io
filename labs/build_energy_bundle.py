"""Reconstrói um pacote de fontes explícitas, sem PDFs, caches ou caminhos privados."""
from io import BytesIO
from pathlib import Path
import hashlib
import importlib
import json
import sys
from zipfile import ZipFile,ZipInfo,ZIP_STORED
ROOT=Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
env=importlib.import_module("labs.contratos-energia.environment")
INTRO="""# Laboratório de energia: começar aqui

Extraia o ZIP inteiro em uma pasta. Abra terminal nesta raiz, que contém labs/ e MANIFEST.json.
É necessário um Python 3 já disponível. Sem dependências externas; nenhuma instalação é executada.
Verificado no Mac com CPython 3.14.5; execução em Windows e outras versões ainda pendente.

Comando de referência no Mac:

    python3 -m labs.contratos-energia.environment
    python3 -m labs.contratos-energia.environment --verify
    python3 -m unittest discover -s labs/contratos-energia -t .
    python3 -m labs.contratos-energia.pipeline labs/contratos-energia/measurements.json

No Windows, use python ou py -3 no lugar de python3, conforme o executável configurado.
Resultados de referência: energias [24.0,400.0,0.0] J. Confira valores e testes, sem exigir texto de ambiente igual.
BUILD_ENVIRONMENT.json registra o ambiente observado na construção; não comprova execução no dispositivo de destino.

MANIFEST.json lista SHA-256 dos arquivos incluídos, exceto ele mesmo. --verify confere esses arquivos;
não audita arquivos extras nem é assinatura de autoria ou prova de correção científica.
Não copie um ambiente .venv de um sistema para outro; recrie-o localmente se precisar de isolamento.
Este laboratório não necessita criar .venv, instalar pacotes ou mudar configurações.

Mais hipóteses e limites em labs/contratos-energia/README.md. Material próprio assistido por IA em rascunho para revisão.
"""

def build_bytes():
    files={name:(ROOT/name).read_bytes() for name in env.SOURCE_FILES}
    files["LEIA-ME.md"]=INTRO.encode("utf-8")
    files["BUILD_ENVIRONMENT.json"]=(json.dumps(env.report(),ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode("utf-8")
    manifest={name:hashlib.sha256(data).hexdigest() for name,data in sorted(files.items())}
    files["MANIFEST.json"]=(json.dumps(manifest,sort_keys=True,indent=2)+"\n").encode("utf-8")
    stream=BytesIO()
    with ZipFile(stream,"w",compression=ZIP_STORED) as archive:
        for name,data in sorted(files.items()):
            info=ZipInfo(name,date_time=(2000,1,1,0,0,0));info.compress_type=ZIP_STORED
            info.create_system=3;info.external_attr=0o100644<<16
            archive.writestr(info,data)
    return stream.getvalue()

if __name__=="__main__":
    target=ROOT/"labs/contratos-energia.zip"
    target.write_bytes(build_bytes())
    print("Pacote reconstruído:",target.name)
