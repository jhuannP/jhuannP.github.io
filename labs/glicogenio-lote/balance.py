"""Lote de produtos já liberados: G1P e glicose até lactato, modelo clássico."""

def count(v):
    if isinstance(v,bool) or not isinstance(v,int) or not 0<=v<=1000000:
        raise ValueError('Contagem inteira de 0 a 1.000.000, sem bool')
    return v

def balance(g1p,glucose):
    g1p,glucose=map(count,(g1p,glucose));units=g1p+glucose
    gross=4*units;pfk=units;hexokinase=glucose
    return dict(glucose_units=units,lactate=2*units,carbon_in=6*units,
                carbon_out=3*(2*units),atp_gross=gross,
                atp_pfk=pfk,atp_hexokinase=hexokinase,
                atp_net=gross-pfk-hexokinase,
                atp_net_if_all_free=2*units,saving_vs_free=g1p,
                nadh_produced=2*units,nadh_used=2*units,nadh_net=0)

if __name__=='__main__':
    a=balance(4,1)
    assert a['atp_net']==14 and a['lactate']==10
    print(a)
