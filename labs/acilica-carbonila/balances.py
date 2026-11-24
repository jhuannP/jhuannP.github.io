"""Contabilidade fornecida, sem predição de reação ou estrutura."""
from fractions import Fraction as Q
# C,H,O,carga; fórmulas declaradas manualmente.
species={'ester':(5,10,2,0),'oh':(0,1,1,-1),'tetra':(5,11,3,-1),'acid':(3,6,2,0),'ethoxide':(2,5,1,-1),'carboxylate':(3,5,2,-1),'ethanol':(2,6,1,0)}
def total(side):
    return tuple(sum(species[name][j]*count for name,count in side.items()) for j in range(4))
if __name__=='__main__':
    steps=[({'ester':1,'oh':1},{'tetra':1}),({'tetra':1},{'acid':1,'ethoxide':1}),({'acid':1,'ethoxide':1},{'carboxylate':1,'ethanol':1})]
    for left,right in steps:assert total(left)==total(right)
    assert total({'ester':1,'oh':1})==total({'carboxylate':1,'ethanol':1})==(5,11,3,-1)
    # Forma neutra isolada, sem transferir H ao etóxido, não fecha o balanço líquido.
    assert total({'acid':1,'ethanol':1})!=total({'ester':1,'oh':1})
    ester,oh=Q(4,100),Q(3,100);extent=min(ester,oh)
    assert (extent,ester-extent,oh-extent)==(Q(3,100),Q(1,100),0)
    initial=total({'ester':ester,'oh':oh})
    final=total({'ester':ester-extent,'carboxylate':extent,'ethanol':extent})
    assert initial==final
    print('Três etapas, balanço líquido, contraexemplo e estoque em mols conferidos; não é prova de mecanismo.')
