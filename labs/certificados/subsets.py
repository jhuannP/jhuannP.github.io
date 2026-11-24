"""Soma de subconjunto com vazio permitido; inteiros exatos de Python.
Busca exaustiva e DP têm orçamentos didáticos: exceder não significa resposta não.
"""
class BudgetExceeded(RuntimeError):
    pass


def instance(values,target):
    if not isinstance(values,(list,tuple)) or any(type(v) is not int for v in values):
        raise TypeError("Valores devem ser lista/tupla de int, sem bool.")
    if type(target) is not int:raise TypeError("Alvo deve ser int, sem bool.")
    return tuple(values),target


def positive_budget(value):
    if type(value) is not int or value<1:raise ValueError("Orçamento deve ser inteiro positivo.")
    return value


def verify(values,target,indices):
    values,target=instance(values,target)
    if not isinstance(indices,(list,tuple)) or len(indices)>len(values):return False
    seen=[False]*len(values);total=0
    for i in indices:
        if type(i) is not int or not 0<=i<len(values):return False
        if seen[i]:return False
        seen[i]=True;total+=values[i]
    return total==target


def search(values,target,max_candidates=65536):
    values,target=instance(values,target);positive_budget(max_candidates)
    for mask in range(1<<len(values)):
        if mask>=max_candidates:
            raise BudgetExceeded("Busca interrompida; existência ainda não decidida.")
        indices=[i for i in range(len(values)) if mask & (1<<i)]
        if verify(values,target,indices):return indices
    return None


def dp_decide(values,target,max_work=100000):
    """Só não negativos; (T+1)*max(1,n) é orçamento superior didático."""
    values,target=instance(values,target);positive_budget(max_work)
    if target<0 or any(v<0 for v in values):
        raise ValueError("Esta DP requer valores e alvo não negativos.")
    if (target+1)*max(1,len(values))>max_work:
        raise BudgetExceeded("Tabela não iniciada: orçamento excedido, sem conclusão.")
    reachable=[False]*(target+1);reachable[0]=True
    for value in values:
        for total in range(target,value-1,-1):
            reachable[total]=reachable[total] or reachable[total-value]
    return reachable[target]


if __name__=="__main__":
    values=[2,5,9];target=11
    cert=search(values,target)
    print("certificado",cert,"confere",verify(values,target,cert),"DP",dp_decide(values,target))
