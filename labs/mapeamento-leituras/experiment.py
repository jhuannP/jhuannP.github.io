"""Mapeamento exato didático: dados sintéticos, sem variantes ou erros."""
REFERENCES=('ATGCCGTACGATTCAGGCTAACGT','ACGTTAGCTGCAACGTTAGCTGCA')
STARTS=(0,4,8,12,16)

def dna(s):
    if not isinstance(s,str) or not s or any(c not in 'ACGT' for c in s):
        raise ValueError('DNA não vazio, maiúsculo, somente ACGT.')
    return s

def revcomp(s):
    return dna(s).translate(str.maketrans('ACGT','TGCA'))[::-1]

def locate(reference,query):
    dna(reference);dna(query)
    rc=revcomp(query);hits=[]
    for start in range(len(reference)-len(query)+1):
        fragment=reference[start:start+len(query)]
        strands=[]
        if fragment==query:strands.append('+')
        if fragment==rc:strands.append('-')
        if strands:hits.append(dict(start=start,end=start+len(query),strands=strands))
    return hits

def coverage(intervals,n):
    out=[0]*n
    for a,b in intervals:
        if type(a) is not int or type(b) is not int or not 0<=a<b<=n:raise ValueError('Intervalo inválido.')
        for i in range(a,b):out[i]+=1
    return out

def model(genome=1,length=6,read=3):
    if type(genome) is not int or genome not in (0,1) or type(length) is not int or not 4<=length<=8 or type(read) is not int or not 1<=read<=5:
        raise ValueError('Referência 0/1, comprimento 4..8, leitura 1..5.')
    reference=REFERENCES[genome];rows=[]
    for i,start in enumerate(STARTS):
        fragment=reference[start:start+length];strand='+' if i%2==0 else '-'
        query=fragment if strand=='+' else revcomp(fragment)
        # locate recebe só referência e letras, sem origem conhecida.
        hits=locate(reference,query)
        rows.append(dict(read=i+1,query=query,origin=start,origin_strand=strand,hits=hits,unique=len(hits)==1))
    truth=coverage([(s,s+length) for s in STARTS],len(reference))
    unique=[r['hits'][0] for r in rows if r['unique']]
    retained=coverage([(h['start'],h['end']) for h in unique],len(reference))
    return dict(genome=genome,length=length,read=read,reference=reference,rows=rows,selected=rows[read-1],truth=truth,retained=retained,
                unique_count=len(unique),ambiguous_count=5-len(unique),mean_truth=sum(truth)/len(reference),mean_retained=sum(retained)/len(reference))

if __name__=='__main__':
    s=model();print(s['selected']);print('Cobertura gerada/retida:',s['mean_truth'],s['mean_retained'])
    assert len(locate('ATAT','ATAT'))==1
