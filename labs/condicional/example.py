"""Dado justo: contar resultados sob informação e comparar condicionais."""
from fractions import Fraction as Q

def conditional_uniform(event,given_event,sample_space):
    space=set(sample_space);A=set(event);B=set(given_event)
    if not space or not A<=space or not B<=space:raise ValueError('Eventos devem estar no espaço não vazio')
    return None if not B else Q(len(A&B),len(B))

space=set(range(1,7));even={2,4,6};at_least_four={4,5,6}
assert conditional_uniform(even,at_least_four,space)==Q(2,3)
B={4,5}
assert conditional_uniform(even,B,space)==Q(1,2)
assert conditional_uniform(B,even,space)==Q(1,3)
assert conditional_uniform(even,set(),space) is None
# Partição de duas máquinas: probabilidade total de defeito.
prob_defect=Q(3,5)*Q(1,50)+Q(2,5)*Q(1,20)
assert prob_defect==Q(4,125)
print('P(par | resultado>=4):',conditional_uniform(even,at_least_four,space))
print('Total de defeito no modelo de máquinas:',prob_defect)
