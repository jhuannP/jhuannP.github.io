"""Tipo-valor original: snapshot de leituras racionais, sem conversão de unidades."""
from dataclasses import dataclass
from fractions import Fraction as Q


def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise ValueError('Leituras devem ser int ou Fraction, não bool/float.')
    return Q(value)


@dataclass(frozen=True,slots=True,init=False)
class Leituras:
    unidade: str
    valores: tuple[Q,...]

    def __init__(self,unidade: str,valores: list[int|Q] | tuple[int|Q,...]):
        if not isinstance(unidade,str) or unidade not in ('m','s'):
            raise ValueError('Unidade deve ser m ou s, sem conversão implícita.')
        if not isinstance(valores,(tuple,list)) or not valores:
            raise ValueError('Forneça lista/tupla não vazia.')
        snapshot=tuple(rational(x) for x in valores)
        object.__setattr__(self,'unidade',unidade)
        object.__setattr__(self,'valores',snapshot)

    @property
    def media(self):
        return sum(self.valores,Q(0))/len(self.valores)

    @property
    def desvios(self):
        mean=self.media
        return tuple(x-mean for x in self.valores)

    def com_acrescimo(self,value):
        return Leituras(self.unidade,self.valores+(rational(value),))

    def juntar(self,outra):
        if type(outra) is not Leituras:
            raise TypeError('juntar exige outro valor Leituras deste contrato.')
        if self.unidade!=outra.unidade:
            raise ValueError('Unidades distintas; não convertemos m em s.')
        return Leituras(self.unidade,self.valores+outra.valores)


if __name__=='__main__':
    origem=[1,2,3];a=Leituras('m',origem);origem[0]=100
    b=a.com_acrescimo(6)
    print('Origem mutável:',origem)
    print('Snapshot a:',a,'média:',a.media)
    print('Novo valor b:',b,'média:',b.media,'desvios:',b.desvios)
    print('a==outro snapshot igual:',a==Leituras('m',[1,2,3]))
