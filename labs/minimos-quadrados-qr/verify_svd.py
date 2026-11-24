"""Validação opcional independente; requer NumPy já disponível."""
from pathlib import Path
import runpy
import numpy as np

ns=runpy.run_path(str(Path(__file__).with_name('experiment.py')))
max_prediction_error=0.
cases=0
for mode in (0,1,2):
    for delta in (-1,0,1):
        for level in ((0,1,2,3) if mode==2 else (1,)):
            d=ns['dataset'](mode,delta,level)
            r=ns['qr_fit'](d['A'],d['y'])
            A=np.array(d['A']);y=np.array(d['y'])
            beta,_,rank,_=np.linalg.lstsq(A,y,rcond=1e-12)
            if r['status']=='ok':
                error=float(np.max(np.abs(A@beta-np.array(r['pred']))))
                max_prediction_error=max(max_prediction_error,error)
                assert error<2e-7 and rank==A.shape[1]
            else:
                assert rank<A.shape[1]
            cases+=1
print({'independent_svd_cases':cases,'max_prediction_difference':max_prediction_error})
