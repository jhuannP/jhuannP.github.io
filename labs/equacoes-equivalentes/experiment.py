"""Equações afins curadas; cada etapa conserva o conjunto solução real."""
import math

# Etapa: texto, a,b,c,d representando ax+b=cx+d.
CASES=[
 [('3x+2=14',3,2,0,14),('3x=12',3,0,0,12),('x=4',1,0,0,4),('3x+2=14 (conferência)',3,2,0,14)],
 [('2(x−3)=x+1',2,-6,1,1),('2x−6=x+1',2,-6,1,1),('x−6=1',1,-6,0,1),('x=7',1,0,0,7)],
 [('2x+1=2x+3',2,1,2,3),('1=3',0,1,0,3),('0=2',0,0,0,2),('0=2 (classificação)',0,0,0,2)],
 [('3(x+2)=3x+6',3,6,3,6),('3x+6=3x+6',3,6,3,6),('6=6',0,6,0,6),('0=0',0,0,0,0)],
 [('(x−1)/2=3/4',.5,-.5,0,.75),('2(x−1)=3',2,-2,0,3),('2x=5',2,0,0,5),('x=5/2',1,0,0,2.5)]
]
OPERATIONS=[
 ['Equação original','Subtrair 2 dos dois lados','Dividir os dois lados por 3','Substituir o candidato na original'],
 ['Equação original','Aplicar a distributiva','Subtrair x dos dois lados','Somar 6 aos dois lados'],
 ['Equação original','Subtrair 2x dos dois lados','Subtrair 1 dos dois lados','Reconhecer contradição, sem dividir por zero'],
 ['Equação original','Aplicar a distributiva','Subtrair 3x dos dois lados','Subtrair 6 dos dois lados'],
 ['Equação original','Multiplicar os dois lados por 4','Distribuir e somar 2 aos dois lados','Dividir os dois lados por 2']
]


def classify(a,b,c,d):
    coefficient=a-c; target=d-b
    if coefficient == 0:
        return ('all' if target == 0 else 'none'), None
    return 'unique', target/coefficient


def model(case=0,step=0,candidate=4):
    if case not in range(5) or step not in range(4) or not math.isfinite(candidate) or not -2<=candidate<=8:
        raise ValueError('Caso 0–4, etapa 0–3 e candidato na janela −2 a 8')
    text,a,b,c,d=CASES[case][step]
    kind,root=classify(a,b,c,d)
    left=a*candidate+b;right=c*candidate+d
    original=CASES[case][0]
    original_left=original[1]*candidate+original[2]
    original_right=original[3]*candidate+original[4]
    return dict(case=case,step=step,candidate=candidate,text=text,operation=OPERATIONS[case][step],
                coefficients=[a,b,c,d],kind=kind,root=root,left=left,right=right,
                difference=left-right,satisfies=left==right,
                original_left=original_left,original_right=original_right)


if __name__=='__main__':
    for case in range(5):
        r=model(case,3)
        print(r['text'],r['kind'],r['root'])
    assert model(0,0,4)['satisfies']
    assert model(4,3,2.5)['satisfies']
