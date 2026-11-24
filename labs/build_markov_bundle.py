"""Reconstrua o pacote após editar fontes ou relatório."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
ROOT=Path(__file__).resolve().parent
FILES=('README.md','experiment.py','starter.py','transition.json','test_experiment.py','example-output.json','__init__.py')
if __name__=='__main__':
    with ZipFile(ROOT/'markov.zip','w',compression=ZIP_DEFLATED) as archive:
        for name in FILES:archive.write(ROOT/'markov'/name,arcname='markov/'+name)
    print('Pacote reconstruído:',ROOT/'markov.zip')
