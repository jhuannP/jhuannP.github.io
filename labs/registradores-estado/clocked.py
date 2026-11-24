"""Dois registradores ideais na mesma borda; não simula eletrônica."""
def bit(x):
    if type(x) is not int or x not in (0,1):raise ValueError('Bit inteiro0 ou1 necessário')
    return x

def step(state,d,enable=(1,1),reset=0):
    if type(state) is not tuple or len(state)!=2:raise ValueError('Estado tupla de dois bits')
    if type(enable) is not tuple or len(enable)!=2:raise ValueError('Habilitações tupla de dois bits')
    a,b=map(bit,state);ea,eb=map(bit,enable);d=bit(d);reset=bit(reset)
    if reset:return (0,0) # synchronous reset, highest priority at this event
    return (d if ea else a,a if eb else b) # B reads old A

if __name__=='__main__':
    state=(0,0)
    for d in (1,0,1):
        state=step(state,d);print(state)
