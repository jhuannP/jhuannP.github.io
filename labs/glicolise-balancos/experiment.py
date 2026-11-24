"""Inventário estequiométrico reduzido da glicólise clássica.
Extensões em mol; omite H+, cargas, estados de protonação e complexos com Mg.
Não é simulação temporal, balanço atômico completo ou teste de viabilidade.
"""
from fractions import Fraction as Q
REACTIONS=(
 {"glucose":-1,"ATP":-1,"G6P":1,"ADP":1},
 {"G6P":-1,"F6P":1},
 {"F6P":-1,"ATP":-1,"FBP":1,"ADP":1},
 {"FBP":-1,"DHAP":1,"GAP":1},
 {"DHAP":-1,"GAP":1},
 {"GAP":-1,"Pi":-1,"NAD+":-1,"BPG":1,"NADH":1},
 {"BPG":-1,"ADP":-1,"PG3":1,"ATP":1},
 {"PG3":-1,"PG2":1},
 {"PG2":-1,"PEP":1,"water":1},
 {"PEP":-1,"ADP":-1,"pyruvate":1,"ATP":1},
)
UNIT_EXTENTS=(1,1,1,1,1,2,2,2,2,2)

def combine(extents):
    if not isinstance(extents,(list,tuple)) or len(extents)!=10:
        raise ValueError("Forneça dez extensões.")
    if any(type(x) not in (int,Q) or x<0 for x in extents):
        raise ValueError("Extensões int/Fraction não negativas; sem bool ou float.")
    net={s:Q(0) for r in REACTIONS for s in r}
    for extent,reaction in zip(extents,REACTIONS):
        for species,coefficient in reaction.items():net[species]+=extent*coefficient
    return net

def ledger(glucose):
    if type(glucose) not in (int,Q) or glucose<0:
        raise ValueError("Quantidade de glicose em mol, int/Fraction não negativa.")
    extents=tuple(Q(glucose)*n for n in UNIT_EXTENTS)
    net=combine(extents)
    used=sum((extent*(-r.get("ATP",0)) for extent,r in zip(extents,REACTIONS) if r.get("ATP",0)<0),Q(0))
    made=sum((extent*r.get("ATP",0) for extent,r in zip(extents,REACTIONS) if r.get("ATP",0)>0),Q(0))
    return dict(extents=extents,net=net,atp_used=used,atp_made=made,atp_net=made-used)

if __name__=="__main__":
    r=ledger(1)
    print("ATP gasto, produzido, líquido em mol:",r["atp_used"],r["atp_made"],r["atp_net"])
    print("Inventário líquido não nulo:",{k:v for k,v in r["net"].items() if v})
