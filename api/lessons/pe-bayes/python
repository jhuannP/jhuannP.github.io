"""Probabilidades racionais em modelos sintéticos; condicionamento zero explícito."""
from fractions import Fraction as Q

def probability(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or not 0<=x<=1:
        raise ValueError('Use int ou Fraction entre 0 e 1')
    return Q(x)

def given(intersection,conditioning):
    joint,base=probability(intersection),probability(conditioning)
    if joint>base:raise ValueError('A interseção não pode superar o evento condicionado')
    return None if base==0 else joint/base

def detector(prior,sensitivity,false_positive):
    p,s,f=map(probability,(prior,sensitivity,false_positive))
    true_positive=p*s;false_alarm=(1-p)*f;positive=true_positive+false_alarm
    true_negative=(1-p)*(1-f);missed=p*(1-s);negative=true_negative+missed
    return dict(joint_defect_positive=true_positive,joint_good_positive=false_alarm,
                positive=positive,negative=negative,defect_given_positive=given(true_positive,positive),
                defect_given_negative=given(missed,negative),
                expected_table_1000=[[1000*true_positive,1000*missed],[1000*false_alarm,1000*true_negative]])

if __name__=='__main__':
    result=detector(Q(1,10),Q(4,5),Q(1,5))
    assert result['defect_given_positive']==Q(4,13)
    assert result['expected_table_1000']==[[80,20],[180,720]]
    print('Posterior no modelo:',result['defect_given_positive'])
    print('Contagens esperadas em 1000, não observações:',result['expected_table_1000'])
    assert detector(0,0,0)['defect_given_positive'] is None
    assert detector(Q(1,2),Q(4,5),Q(1,5))['defect_given_positive']==Q(4,5)
