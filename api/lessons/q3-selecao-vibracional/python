"""Permissão por simetria em C2v; sem derivadas físicas, intensidades ou frequências."""
OPS=((1,1,1),(-1,-1,1),(1,-1,1),(-1,1,1))
NAMES=('A1','A2','B1','B2')
CHARACTERS=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
CHANNELS=(('x',(1,0,0)),('y',(0,1,0)),('z',(0,0,1)),
          ('xx',(2,0,0)),('yy',(0,2,0)),('zz',(0,0,2)),
          ('xy',(1,1,0)),('xz',(1,0,1)),('yz',(0,1,1)))
AB2=(2,0,1,0)

def character(exponents):
    return tuple(s[0]**exponents[0]*s[1]**exponents[1]*s[2]**exponents[2] for s in OPS)

def model(irrep=0,channel=2):
    if type(irrep) is not int or not 0<=irrep<4 or type(channel) is not int or not 0<=channel<9:
        raise ValueError('Classe 0..3 e canal 0..8 inteiros')
    mode=CHARACTERS[irrep];operator=character(CHANNELS[channel][1])
    product=tuple(a*b for a,b in zip(mode,operator));projection=sum(product)//4
    assert sum(product) in (0,4)
    compatible=[name for name,exp in CHANNELS if character(exp)==mode]
    return dict(irrep=NAMES[irrep],operator=CHANNELS[channel][0],kind='IR' if channel<3 else 'Raman',
                mode_character=mode,operator_character=operator,product_character=product,
                product_irrep=NAMES[CHARACTERS.index(product)],a1_multiplicity=projection,allowed=projection==1,
                ir_components=tuple(x for x in compatible if len(x)==1),
                raman_components=tuple(x for x in compatible if len(x)==2),ab2_multiplicity=AB2[irrep])

if __name__=='__main__':
    a=model(0,2);b=model(0,0)
    assert a['allowed'] and not b['allowed']
    assert model(1,6)['allowed'] and model(1,6)['ab2_multiplicity']==0
    print('A1 com z:',a['product_character'],'A1 incluída:',a['a1_multiplicity'])
    print('A1 com x:',b['product_character'],'A1 incluída:',b['a1_multiplicity'])
