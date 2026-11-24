"""Arrhenius a Ea constante: comparação e inversão de dois pontos, SI explícito."""
import math
R=8.314462618  # J mol^-1 K^-1, valor arredondado adotado

def real(value, name, positive=False):
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise TypeError(name+": use int ou float finito")
    try:value=float(value)
    except OverflowError:raise ValueError(name+": fora do intervalo float") from None
    if not math.isfinite(value) or (positive and value<=0):
        raise ValueError(name+": valor inválido")
    return value

def log_ratio(ea_j_mol,t1_k,t2_k):
    ea=real(ea_j_mol,'Ea');t1=real(t1_k,'T1',True);t2=real(t2_k,'T2',True)
    # k2/k1 é adimensional; Ea pode ser aparente e negativa.
    result=(ea/R)*((t2-t1)/t1/t2)
    if not math.isfinite(result):raise ValueError('Logaritmo fora do intervalo float')
    return result

def rate_ratio(ea_j_mol,t1_k,t2_k):
    logarithm=log_ratio(ea_j_mol,t1_k,t2_k)
    try:result=math.exp(logarithm)
    except OverflowError:raise ValueError('Razão excede float; use log_ratio') from None
    if not math.isfinite(result) or result==0:
        raise ValueError('Razão não representável; use log_ratio')
    return result

def infer_ea(t1_k,k1,t2_k,k2):
    """Retorna J/mol. k1 e k2 devem ser da mesma lei e unidade, declaradas pelo usuário."""
    t1=real(t1_k,'T1',True);t2=real(t2_k,'T2',True)
    k1=real(k1,'k1',True);k2=real(k2,'k2',True)
    if t1==t2:raise ValueError('Temperaturas devem ser distintas')
    delta=(t2-t1)/t1/t2
    if delta==0:raise ValueError('Diferença recíproca não representável')
    # Diferença de logs evita transbordar k2/k1. Mesma unidade para ambos.
    result=R*(math.log(k2)-math.log(k1))/delta
    if not math.isfinite(result):raise ValueError('Ea fora do intervalo float')
    return result
