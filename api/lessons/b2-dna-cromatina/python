"""Cadeia finita idealizada: N cernes e N-1 linkers, sem caudas externas."""
RISE_NM=0.34
CORE_BP=147


def reverse_complement(seq):
    if not isinstance(seq,str) or not seq or any(b not in 'ACGT' for b in seq):
        raise ValueError('Sequência não vazia, letras maiúsculas ACGT')
    return seq.translate(str.maketrans('ACGT','TGCA'))[::-1]


def model(cores=4,linker=40,selected=2):
    if any(not isinstance(v,int) or isinstance(v,bool) for v in (cores,linker,selected)) or not 1<=cores<=8 or not 0<=linker<=80 or not 1<=selected<=8:
        raise ValueError('Cernes 1..8, linker 0..80 pb, seleção 1..8')
    selected=min(selected,cores)
    segments=[];cursor=0
    for i in range(cores):
        segments.append(dict(kind='core',index=i+1,start=cursor,stop=cursor+CORE_BP))
        cursor+=CORE_BP
        if i<cores-1:
            segments.append(dict(kind='linker',index=i+1,start=cursor,stop=cursor+linker))
            cursor+=linker
    wrapped=CORE_BP*cores;link_bp=linker*(cores-1)
    return dict(cores=cores,linker=linker,selected=selected,segments=segments,
                wrapped=wrapped,link_bp=link_bp,total_bp=cursor,nucleotides=2*cursor,
                histones=8*cores,each_histone=2*cores,
                contour_nm=RISE_NM*cursor,wrapped_fraction=wrapped/cursor,
                internal_repeat=CORE_BP+linker if cores>1 else None)


if __name__=='__main__':
    a=model()
    assert a['total_bp']==708 and a['histones']==32
    assert reverse_complement('AATG')=='CATT'
    print(a)
