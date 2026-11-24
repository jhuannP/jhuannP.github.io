"""Audita anotações fornecidas; não prediz domínios ou função."""
from fractions import Fraction as Q
from collections import Counter

def report(length,hits):
    if isinstance(length,bool) or not isinstance(length,int) or not 1<=length<=10000:raise ValueError('Comprimento1–10000.')
    if not isinstance(hits,(list,tuple)) or len(hits)>64:raise ValueError('Até64anotações.')
    checked=[]
    for hit in hits:
        if not isinstance(hit,(list,tuple)) or len(hit)!=3:raise ValueError('Use rótulo,início,fim.')
        label,a,b=hit
        if not isinstance(label,str) or not 1<=len(label)<=32:raise ValueError('Rótulo textual1–32.')
        if any(isinstance(v,bool) or not isinstance(v,int) for v in (a,b)) or not 1<=a<=b<=length:raise ValueError('Limites inclusivos inválidos.')
        checked.append((label,a,b))
    checked.sort(key=lambda h:(h[1],h[2],h[0]))
    overlaps=[(i,j) for i in range(len(checked)) for j in range(i+1,len(checked)) if max(checked[i][1],checked[j][1])<=min(checked[i][2],checked[j][2])]
    merged=[]
    for label,a,b in checked:
        if merged and a<=merged[-1][1]+1:merged[-1]=(merged[-1][0],max(merged[-1][1],b))
        else:merged.append((a,b))
    covered=sum(b-a+1 for a,b in merged)
    return {'covered':covered,'fraction':Q(covered,length),'uncovered':length-covered,'union':merged,'overlapping_hits':overlaps,'ordered_labels':None if overlaps else [h[0] for h in checked],'annotation_counts':dict(Counter(h[0] for h in checked))}

EXAMPLES={'P':(180,[('A',11,60),('B',91,160)]),'Q':(220,[('A',11,60),('B',91,160),('B',171,210)]),'R':(180,[('B',11,80),('A',111,160)])}
if __name__=='__main__':
    for name,args in EXAMPLES.items():print(name,report(*args))
    print('Sobreposição:',report(120,[('A',20,80),('B',60,100)]))
