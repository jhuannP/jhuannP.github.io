"""Cinco clones fictícios; reconhecimento e condição de ativação são entradas, não previsões."""
MATCHES=((1,0,0),(0,1,0),(1,0,0),(0,0,0),(0,0,1))
INITIAL=(10,10,10,10,10)

def grow(initial,target,g,signal):
    if len(initial)!=5 or any(not isinstance(n,int) or n<0 for n in initial) or sum(initial)==0:
        raise ValueError('Cinco contagens inteiras não negativas e total positivo.')
    if not isinstance(target,int) or not 0<=target<3 or not isinstance(g,int) or not 0<=g<=20 or signal not in (0,1):
        raise ValueError('Alvo 0..2, divisões inteiras 0..20 e sinal 0/1.')
    return [n*(2**g if MATCHES[i][target] and signal else 1) for i,n in enumerate(initial)]

def summary(target,g,signal):
    final=grow(INITIAL,target,g,signal)
    recognized=[bool(row[target]) for row in MATCHES]
    active=[bool(r and signal) for r in recognized]
    total=sum(final)
    return dict(final=final,recognized=recognized,active=active,total=total,
                added=total-sum(INITIAL),selected_fraction=sum(n for n,r in zip(final,recognized) if r)/total)

if __name__=='__main__':
    print('Alvo A, 3 divisões, condição presente:',summary(0,3,1))
    print('Mesmo reconhecimento, condição ausente:',summary(0,3,0))
