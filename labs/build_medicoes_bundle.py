"""Reconstrua o pacote didático depois de editar suas fontes."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
ROOT=Path(__file__).resolve().parent
FILES=('README.md','analyze.py','starter.py','measurements.csv','test_analysis.py','example-output.json','__init__.py')
if __name__=='__main__':
    with ZipFile(ROOT/'medicoes.zip','w',compression=ZIP_DEFLATED) as archive:
        for name in FILES:archive.write(ROOT/'medicoes'/name,arcname='medicoes/'+name)
    print('Pacote reconstruído:',ROOT/'medicoes.zip')
