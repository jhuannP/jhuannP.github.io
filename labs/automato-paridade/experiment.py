"""AFD de paridade; estados 0=par e 1=ímpar; leitura sem voltar."""
def trace(word):
    if not isinstance(word,str) or any(c not in '01' for c in word):
        raise ValueError('Palavra sobre o alfabeto {0,1}')
    state=0;states=[0];rows=[]
    for i,c in enumerate(word):
        before=state;state=(state+int(c))%2;states.append(state)
        rows.append(dict(index=i+1,symbol=c,before=before,after=state))
    return dict(word=word,states=states,rows=rows,accepted=state==0)

def inspect(word=11,step=2):
    if any(isinstance(v,bool) or not isinstance(v,int) for v in (word,step)) or not 0<=word<=15 or not 0<=step<=4:
        raise ValueError('Palavra codificada 0–15; passo 0–4')
    text=format(word,'04b');s=trace(text)
    return dict(word=word,step=step,text=text,prefix=text[:step],suffix=text[step:],state=s['states'][step],states=s['states'],rows=s['rows'],complete=step==4,accepted=s['accepted'])

if __name__=='__main__':
    assert trace('')['accepted'] and trace('1100')['accepted']
    assert not trace('1011')['accepted']
    print(inspect())
