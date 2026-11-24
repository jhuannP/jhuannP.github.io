"""KMP por função de prefixos, índices Python e todas as ocorrências."""
def pattern_input(pattern):
    if not isinstance(pattern,str) or not 1<=len(pattern)<=64:
        raise ValueError('Padrão str não vazio, até64 pontos de código')
    return pattern

def _prefix(pattern):
    pi=[0]*len(pattern);compares=0
    for i in range(1,len(pattern)):
        j=pi[i-1]
        while True:
            compares+=1
            if pattern[i]==pattern[j]:
                j+=1;pi[i]=j;break
            if j==0:break
            j=pi[j-1]
    return tuple(pi),compares

def prefix(pattern):
    return _prefix(pattern_input(pattern))[0]

def search(text,pattern):
    pattern=pattern_input(pattern)
    if not isinstance(text,str) or len(text)>512:
        raise ValueError('Texto str com até512 pontos de código')
    pi,preprocessing=_prefix(pattern)
    matches=[];j=0;compares=0
    for i,char in enumerate(text):
        while True:
            compares+=1
            if char==pattern[j]:
                j+=1
                if j==len(pattern):
                    matches.append(i-len(pattern)+1)
                    j=pi[j-1] # Preserva ocorrência sobreposta.
                break
            if j==0:break
            j=pi[j-1]
    return {'matches':tuple(matches),'prefix':pi,
            'pattern_compares':preprocessing,'text_compares':compares}

if __name__=='__main__':
    print(search('ababababa','ababa'))
