"""Mapa C-alfa de 1CRN, cadeia A. Proximidade definida, não ligação química."""
from math import sqrt

# PDB 1CRN, acesso22/10/2026, CC0; coordenadas inteiras em0.001 angstrom.
ROWS = ((1, 'THR', 16967, 12784, 4338), (2, 'THR', 13856, 11469, 6066), (3, 'CYS', 13660, 10707, 9787), (4, 'CYS', 10646, 8991, 11408), (5, 'PRO', 9448, 9034, 15012), (6, 'SER', 8673, 5314, 15279), (7, 'ILE', 8912, 2083, 13258), (8, 'VAL', 5145, 2209, 12453), (9, 'ALA', 5598, 5767, 11082), (10, 'ARG', 8496, 4609, 8837), (11, 'SER', 6500, 1584, 7565), (12, 'ASN', 3545, 3935, 6751), (13, 'PHE', 5929, 6358, 5055), (14, 'ASN', 7331, 3607, 2791), (15, 'VAL', 3782, 2599, 1742), (16, 'CYS', 2890, 6285, 1126), (17, 'ARG', 5895, 6489, -1213), (18, 'LEU', 4933, 3431, -3326), (19, 'PRO', 2792, 5376, -5797), (20, 'GLY', 5366, 8191, -6018), (21, 'THR', 3767, 10609, -3513), (22, 'PRO', 6143, 13513, -2696), (23, 'GLU', 8114, 13103, 500), (24, 'ALA', 6614, 16317, 1913), (25, 'ILE', 3074, 14894, 1756), (26, 'CYS', 4180, 11549, 3187), (27, 'ALA', 5879, 13502, 6026), (28, 'THR', 2691, 15221, 7194), (29, 'TYR', 715, 12045, 6657), (30, 'THR', 2986, 9994, 8950), (31, 'GLY', 4769, 12336, 11360), (32, 'CYS', 8140, 11694, 9635), (33, 'ILE', 10280, 14760, 8823), (34, 'ILE', 12552, 15877, 6036), (35, 'ILE', 15930, 17454, 6941), (36, 'PRO', 18635, 18861, 4738), (37, 'GLY', 21452, 16969, 6513), (38, 'ALA', 22019, 13242, 7020), (39, 'THR', 21936, 12911, 10809), (40, 'CYS', 18504, 12312, 12298), (41, 'PRO', 17924, 13421, 15877), (42, 'GLY', 17334, 10956, 18691), (43, 'ASP', 13564, 11573, 18836), (44, 'TYR', 13257, 10745, 15081), (45, 'ALA', 15445, 7667, 15246), (46, 'ASN', 13512, 5395, 12878))

def squared_distance(a,b):
    return sum((x-y)**2 for x,y in zip(a,b))

def model(cutoff=16,separation=3,selected=4):
    """cutoff em meios angstrom; separação mínima por índice da sequência."""
    if any(isinstance(v,bool) or not isinstance(v,int) for v in (cutoff,separation,selected)):
        raise ValueError('Controles inteiros')
    if not 8<=cutoff<=24 or not 1<=separation<=10 or not 1<=selected<=46:
        raise ValueError('Controle fora do domínio')
    threshold=(500*cutoff)**2
    pairs=[];degree=[0]*46
    for i,a in enumerate(ROWS):
        for j in range(i+separation,46):
            b=ROWS[j];d2=squared_distance(a[2:],b[2:])
            if d2<=threshold:
                pairs.append((i+1,j+1,d2));degree[i]+=1;degree[j]+=1
    neighbors=[(j if i==selected else i,d2) for i,j,d2 in pairs if selected in (i,j)]
    return dict(pairs=pairs,degree=degree,neighbors=neighbors,count=len(pairs),
                eligible=(46-separation)*(47-separation)//2)

if __name__=='__main__':
    result=model(10,10,4)  #5 angstrom e |i-j|>=10
    print('Contatos do resíduo4:',[(i,round(sqrt(d2)/1000,6)) for i,d2 in result['neighbors']])
    print('Pares únicos:',result['count'],'; candidatos:',result['eligible'])
