"""Critério de entropia de propostas cíclicas e expansão livre ideal."""
from fractions import Fraction as Q
from math import isfinite,log

def candidate(*,TH,TC,QH,QC):
    if any(type(x) not in (int,Q) for x in (TH,TC,QH,QC)):raise ValueError("Use int/Fraction, sem bool")
    TH,TC,QH,QC=map(Q,(TH,TC,QH,QC))
    if not TH>TC>0 or QH<=0 or not 0<=QC<=QH:
        raise ValueError("TH>TC>0 K; QH>0 e 0<=QC<=QH em J")
    work=QH-QC;eta=work/QH;limit=1-TC/TH
    ds_hot=-QH/TH;ds_cold=QC/TC;ds_total=ds_hot+ds_cold
    return dict(work=work,eta=eta,carnot_limit=limit,ds_hot=ds_hot,ds_cold=ds_cold,
                ds_total=ds_total,not_excluded_by_entropy=ds_total>=0)

def free_entropy(nR,ratio):
    if any(type(x) not in (int,float) for x in (nR,ratio)):raise ValueError("Use int/float sem bool")
    try:nR,ratio=map(float,(nR,ratio))
    except OverflowError:raise ValueError("Entrada não representável") from None
    if not isfinite(nR) or not isfinite(ratio) or nR<=0 or ratio<1:
        raise ValueError("nR positivo e razão de expansão >=1, finitos")
    ds=nR*log(ratio)
    if not isfinite(ds) or (ratio>1 and ds==0):raise ArithmeticError("Entropia fora da representação finita")
    return ds

if __name__=="__main__":
    for QC in (600,800,400):print(QC,candidate(TH=600,TC=300,QH=1200,QC=QC))
    print("Expansão livre, nR=2 J/K e r=2: ΔS =",free_entropy(2,2),"J/K")
