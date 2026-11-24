"""Probabilidade exata em categorias com quantidades inteiras fornecidas."""
from fractions import Fraction as F

def probability(counts,event,given=None):
    if not isinstance(counts,dict) or not 1<=len(counts)<=100:raise ValueError('Use 1 a100 categorias')
    if any(type(k) is not str or not k for k in counts):raise TypeError('Categorias textuais necessárias')
    if any(type(v) is not int or v<0 for v in counts.values()):raise TypeError('Contagens inteiras não negativas')
    if isinstance(event,str) or isinstance(given,str):raise TypeError('Use conjuntos de categorias')
    event=set(event);given=set(counts) if given is None else set(given)
    if not event<=counts.keys() or not given<=counts.keys():raise ValueError('Categoria desconhecida')
    denominator=sum(counts[k] for k in given)
    if denominator==0:raise ValueError('Não condicionamos em massa zero neste laboratório')
    return F(sum(counts[k] for k in event&given),denominator)

COUNTS={'circle_blue':24,'circle_red':6,'square_blue':14,'square_red':56}
CIRCLE={'circle_blue','circle_red'}
BLUE={'circle_blue','square_blue'}
if __name__=='__main__':
    print('P(círculo|azul):',probability(COUNTS,CIRCLE,BLUE))
    print('P(azul|círculo):',probability(COUNTS,BLUE,CIRCLE))
