"""Contagem formal em NO3- e CO3(2-); não é cálculo quântico."""
from itertools import product

def inspect(species=0,orders=(2,1,1)):
    if isinstance(species,bool) or species not in (0,1) or not isinstance(species,int):
        raise ValueError('Espécie0 nitrato ou1 carbonato')
    if not isinstance(orders,(tuple,list)) or len(orders)!=3 or any(isinstance(x,bool) or not isinstance(x,int) or not 1<=x<=3 for x in orders):
        raise ValueError('Três ordens inteiras de1 a3')
    valence=5 if species==0 else 4
    charge=-1 if species==0 else -2
    bond_sum=sum(orders)
    lone=[8-2*b for b in orders]
    formal=[valence-bond_sum]+[6-n-b for n,b in zip(lone,orders)]
    return dict(symbol='N' if species==0 else 'C',charge=charge,
                total_electrons=2*bond_sum+sum(lone),lone=lone,
                shells=[2*bond_sum]+[8]*3,formal=formal,
                octets=bond_sum==4)

def contributors(species=0):
    return [b for b in product(range(1,4),repeat=3) if inspect(species,b)['octets']]

if __name__=='__main__':
    z=inspect()
    assert z['total_electrons']==24 and z['formal']==[1,0,-1,-1]
    assert len(contributors())==3
    print(z)
