"""Integral de t entre fronteiras móveis; referências exatas didáticas."""

def integral(a,b):return (b*b-a*a)/2

def boundaries(mode,x):
    if isinstance(mode,bool) or not isinstance(mode,int) or mode not in (0,1,2):
        raise ValueError('Modo 0, 1 ou 2')
    if mode==0:return 0,x,0,1
    if mode==1:return 0,x*x,0,2*x
    return x,2*x,1,2

def accumulation(mode,x):
    lower,upper,_,_=boundaries(mode,x)
    return integral(lower,upper)

def rate(mode,x):
    lower,upper,lower_rate,upper_rate=boundaries(mode,x)
    return upper*upper_rate-lower*lower_rate

if __name__=='__main__':
    for mode in range(3):
        for x in [-1,0,1,2]:
            print('modo,x:',mode,x,'fronteiras:',boundaries(mode,x)[:2],
                  'acumulação:',accumulation(mode,x),'taxa:',rate(mode,x))
