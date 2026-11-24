"""Phred+33 em registros sintéticos de quatro linhas. Não é leitor FASTQ geral."""
from math import isfinite, log10, prod, fsum
PROFILES=((20,)*6,(40,40,40,40,10,10),(30,)*6)
SEQUENCE='ACGTAC'

def qualities(qs):
    if not isinstance(qs,(list,tuple)) or not qs or any(type(q) is not int or not 0<=q<=40 for q in qs):
        raise ValueError('Qualidades inteiras entre 0 e 40, não vazias.')
    return list(qs)

def encode(qs):
    return ''.join(chr(q+33) for q in qualities(qs))

def decode(text):
    if not isinstance(text,str) or not text or any(not 33<=ord(c)<=73 for c in text):
        raise ValueError('Recorte Phred+33: caracteres ASCII 33..73, sem espaços.')
    return [ord(c)-33 for c in text]

def parse_record(text):
    if not isinstance(text,str):raise ValueError('Texto esperado.')
    lines=text.splitlines()
    if len(lines)!=4:raise ValueError('Exatamente quatro linhas por registro neste recorte.')
    header,sequence,separator,quality=lines
    if not header.startswith('@') or not header[1:].strip():raise ValueError('Identificador ausente.')
    if separator!='+':raise ValueError('Separador deve ser + sem repetição de identificador neste recorte.')
    if not sequence or any(c not in 'ACGTN' for c in sequence):raise ValueError('Somente ACGTN maiúsculo neste recorte.')
    qs=decode(quality)
    if len(sequence)!=len(qs):raise ValueError('Uma qualidade por base.')
    return dict(id=header[1:],sequence=sequence,qualities=qs)

def summarize(qs):
    qs=qualities(qs);ps=[10**(-q/10) for q in qs];expected=fsum(ps)
    return dict(qs=qs,ps=ps,mean_q=fsum(qs)/len(qs),expected=expected,mean_p=expected/len(qs),
                effective_q=-10*log10(expected/len(qs)),lower=max(ps),upper=min(1.,expected),
                any_independent=1-prod(1-p for p in ps),encoded=encode(qs))

def model(case=1,shift=0,cutoff=.1):
    if type(case) is not int or not 0<=case<=2 or type(shift) is not int or not -10<=shift<=0:
        raise ValueError('Caso 0..2 e deslocamento inteiro -10..0.')
    if isinstance(cutoff,bool) or not isinstance(cutoff,(int,float)) or not isfinite(cutoff) or not 0<=cutoff<=3:
        raise ValueError('Limite entre 0 e 3 erros esperados.')
    rows=[dict(case=i,**summarize([q+shift for q in base])) for i,base in enumerate(PROFILES)]
    for row in rows:row['retained']=row['expected']<=cutoff
    return dict(case=case,shift=shift,cutoff=cutoff,rows=rows,selected=rows[case],retained_count=sum(r['retained'] for r in rows))

if __name__=='__main__':
    for r in model()['rows']:print(r['case'],r['mean_q'],r['expected'],r['retained'])
