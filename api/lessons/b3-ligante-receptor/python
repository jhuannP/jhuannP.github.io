"""Ligação reversível 1:1 em volume fechado; concentrações sintéticas em nM."""
import math


def binding(total=2.,receptors=2.,kd=1.):
    if not all(math.isfinite(v) for v in (total,receptors,kd)) or total<0 or receptors<=0 or kd<=0:
        raise ValueError('Ligante total não negativo, receptores e Kd positivos')
    S=total+receptors+kd
    disc=(receptors-total)**2+2*kd*(receptors+total)+kd*kd
    complex_=2*receptors*total/(S+math.sqrt(disc))
    free_ligand=total-complex_;free_receptor=receptors-complex_
    return dict(total=total,receptors=receptors,kd=kd,complex=complex_,
                free_ligand=free_ligand,free_receptor=free_receptor,
                fraction=complex_/receptors,approximation=total/(kd+total),
                depletion=complex_/total if total else None,half_total=kd+receptors/2)


def model(total=2.,receptors=2.,kd=1.):
    if not all(math.isfinite(v) for v in (total,receptors,kd)) or not 0<=total<=10 or not .5<=receptors<=5 or not .5<=kd<=4:
        raise ValueError('Ltotal 0..10, Rtotal .5..5 e Kd .5..4 nM')
    return binding(total,receptors,kd)


if __name__=='__main__':
    s=model()
    assert s['complex']==1 and s['fraction']==.5 and s['free_ligand']==1
    print(s)
