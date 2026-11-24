"""Reconstrua o pacote depois de editar fontes ou relatório de exemplo."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
ROOT=Path(__file__).resolve().parent
FILES=('README.md','experiment.py','starter.py','test_experiment.py','example-output.json','__init__.py')
if __name__=='__main__':
    with ZipFile(ROOT/'percolacao.zip','w',compression=ZIP_DEFLATED) as archive:
        for name in FILES:archive.write(ROOT/'percolacao'/name,arcname='percolacao/'+name)
    print('Pacote reconstruído:',ROOT/'percolacao.zip')
