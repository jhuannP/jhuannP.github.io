"""Busca exaustiva sem gaps, quatro letras, qualidades homogêneas hipotéticas."""
from fractions import Fraction as F
REFERENCE='ACGTTACGAT'
READS=('CGTT','GGTT','CGCT','CCCC','ACGT')

def dna(s):
    if not isinstance(s,str) or not 1<=len(s)<=256 or any(c not in 'ACGT' for c in s):
        raise ValueError('Use DNA ACGT maiúsculo, comprimento 1..256')
    return s

def revcomp(s):
    return dna(s).translate(str.maketrans('ACGT','TGCA'))[::-1]

def search(reference,query,limit=1,q=20):
    dna(reference);dna(query)
    if type(limit) is not int or not 0<=limit<=len(query): raise ValueError('Limite inteiro entre 0 e comprimento da leitura')
    if type(q) is not int or q not in (10,20,30,40): raise ValueError('Q deve ser 10,20,30 ou 40')
    p=F(1,10**(q//10));rows=[]
    for start in range(len(reference)-len(query)+1):
        fragment=reference[start:start+len(query)]
        for strand,oriented in (('+',query),('-',revcomp(query))):
            differences=tuple(j for j,(a,b) in enumerate(zip(fragment,oriented)) if a!=b)
            d=len(differences)
            likelihood=(1-p)**(len(query)-d)*(p/3)**d
            rows.append(dict(start=start,end=start+len(query),strand=strand,query=oriented,
                             fragment=fragment,differences=differences,cost=d,likelihood=likelihood,accepted=d<=limit))
    minimum=min((r['cost'] for r in rows),default=None)
    accepted=[r for r in rows if r['accepted']]
    best=[r for r in accepted if r['cost']==minimum]
    intervals=sorted({(r['start'],r['end']) for r in best})
    return dict(rows=rows,accepted=accepted,best=best,minimum=minimum,
                interval_count=len(intervals),oriented_count=len(best),p=p,
                expected_errors=len(query)*p)

def model(kind=1,limit=1,q=20):
    if type(kind) is not int or kind not in range(5):raise ValueError('Leitura 0..4')
    return dict(reference=REFERENCE,read=READS[kind],**search(REFERENCE,READS[kind],limit,q))

if __name__=='__main__':
    r=model();assert r['minimum']==1 and r['interval_count']==1
    assert r['best'][0]['start']==1 and r['best'][0]['strand']=='+'
    assert r['best'][0]['likelihood']==F(323433,100000000)
    print('Leitura',r['read'],'melhor custo',r['minimum'],'intervalos',r['interval_count'])
    print('Verossimilhança hipotética:',r['best'][0]['likelihood'])
