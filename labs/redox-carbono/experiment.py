"""Inventário formal C/H/O neutro em catálogo fixo.
Não prediz mecanismo, reagentes, rendimento ou viabilidade de síntese.
Cada carbono: (H ligados, soma das ordens C-O, soma das ordens C-C).
"""
CATALOG={
 "ethanol":dict(family="C2",formula=(2,6,1),carbons=((3,0,1),(2,1,1))),
 "ethanal":dict(family="C2",formula=(2,4,1),carbons=((3,0,1),(1,2,1))),
 "ethanoic_acid":dict(family="C2",formula=(2,4,2),carbons=((3,0,1),(0,3,1))),
 "propan_2_ol":dict(family="C3",formula=(3,8,1),carbons=((3,0,1),(1,1,2),(3,0,1))),
 "propanone":dict(family="C3",formula=(3,6,1),carbons=((3,0,1),(0,2,2),(3,0,1))),
}

def carbon_state(h,oxygen_order,carbon_order):
    if any(type(v) is not int or v<0 for v in (h,oxygen_order,carbon_order)) or h+oxygen_order+carbon_order!=4:
        raise ValueError("Carbono neutro tetravalente: inteiros não negativos com soma quatro.")
    return oxygen_order-h

def states(name):
    if not isinstance(name,str) or name not in CATALOG:
        raise ValueError("Escolha uma espécie do catálogo fixo.")
    return tuple(carbon_state(*c) for c in CATALOG[name]["carbons"])

def transition(start,end):
    before,after=states(start),states(end)
    A,B=CATALOG[start],CATALOG[end]
    if A["family"]!=B["family"]:
        raise ValueError("Apenas esqueletos e mapeamentos da mesma família fixa.")
    delta=tuple(b-a for a,b in zip(before,after))
    water=B["formula"][2]-A["formula"][2]
    protons=A["formula"][1]+2*water-B["formula"][1]
    return dict(before=before,after=after,delta=delta,electron_equivalents=sum(delta),
                water_left=water,protons_right=protons,electrons_right=protons)

if __name__=="__main__":
    for pair in (("ethanol","ethanal"),("ethanal","ethanoic_acid"),("propan_2_ol","propanone")):
        print(pair,transition(*pair))
