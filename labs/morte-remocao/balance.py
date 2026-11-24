"""Contagens sintéticas por intervalo; não prediz mecanismo ou morte celular."""
from dataclasses import dataclass

@dataclass(frozen=True)
class State:
    alive: int
    awaiting: int

def count(value,name):
    if type(value) is not int:raise TypeError(name+': inteiro, sem bool')
    if value<0:raise ValueError(name+': não negativo')
    return value

def step(state,*,born,died,cleared):
    """Mortes entre vivos iniciais, entradas vivas, remoção de mortos disponíveis.

    born = acréscimo líquido de unidades vivas por produção no intervalo;
    não é a contagem de todas as células-filhas de mitoses.
    Sem migração, outras perdas ou fragmentação. Cada morto é uma unidade.
    """
    if not isinstance(state,State):raise TypeError('Use State')
    n=count(state.alive,'alive');c=count(state.awaiting,'awaiting')
    born=count(born,'born');died=count(died,'died');cleared=count(cleared,'cleared')
    if died>n:raise ValueError('Mortes limitadas aos vivos iniciais neste modelo')
    if cleared>c+died:raise ValueError('Remoção excede mortos disponíveis')
    return State(n+born-died,c+died-cleared)
