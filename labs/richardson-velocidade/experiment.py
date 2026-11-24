"""Richardson com referência racional. Modelo didático, sem dados medidos."""
from fractions import Fraction as Q


def rational(value):
    if type(value) not in (int, Q):
        raise ValueError('Use int ou Fraction; float e bool não são referência exata.')
    return Q(value)


def combine(coarse, fine, p=2):
    if type(p) is not int or not 1 <= p <= 20:
        raise ValueError('Ordem inteira entre 1 e 20 necessária neste laboratório.')
    coarse, fine = rational(coarse), rational(fine)
    factor = 2**p
    return (factor*fine-coarse)/(factor-1)


def central(f, x, h):
    x, h = rational(x), rational(h)
    if h <= 0:
        raise ValueError('Passo positivo necessário.')
    return (rational(f(x+h))-rational(f(x-h)))/(2*h)


def extrapolate(f, x, h, p=2):
    return combine(central(f,x,h),central(f,x,rational(h)/2),p)


def position(t):
    t = rational(t)
    return 2*t+t**3+t**5


def perturbed(h, errors):
    """Quatro erros: pontos -h, -h/2, +h/2, +h relativos a t=1."""
    h = rational(h)
    if h <= 0:
        raise ValueError('Passo positivo necessário.')
    if len(errors) != 4:
        raise ValueError('Quatro erros necessários.')
    values=[position(1+offset*h)+rational(error)
            for offset,error in zip((Q(-1),Q(-1,2),Q(1,2),Q(1)),errors)]
    return (values[0]-8*values[1]+8*values[2]-values[3])/(6*h)


def experiment():
    print('Trajetória sintética em SI; v(1)=10 m/s.')
    print('h(s), D(h), D(h/2), R(h), erro R(m/s)')
    for h in (Q(1,2),Q(1,4),Q(1,8)):
        r=extrapolate(position,1,h)
        print(h,central(position,1,h),central(position,1,h/2),r,r-10)
    delta=Q(1,4000); h=Q(1,20)
    ideal=extrapolate(position,1,h)
    noisy=perturbed(h,(delta,-delta,delta,-delta))
    print('Efeito construído dos erros (m/s):',noisy-ideal,'= 3delta/h =',3*delta/h)
    wrong=combine(Q(3)+Q(1,2)**2,Q(3)+Q(1,4)**2,p=1)
    print('Ordem errada p=1 no exemplo cúbico:',wrong,'em vez de 3.')


if __name__=='__main__': experiment()
