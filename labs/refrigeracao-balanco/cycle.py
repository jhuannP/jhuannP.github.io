"""Two-reservoir cyclic refrigerator ledger. Prescribed energy proposals, not equipment."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError("use int or Fraction")
    return Q(x)

def proposal(tc,th,qc,work):
    """K, K, J/cycle, J/cycle. Work=0 allowed to diagnose a forbidden proposal."""
    tc,th,qc,work=map(rational,(tc,th,qc,work))
    if not 0<tc<th or qc<=0 or work<0:raise ValueError("requires 0<Tc<Th, Qc>0, work>=0")
    qh=qc+work
    entropy=qh/th-qc/tc
    work_min=qc*(th-tc)/tc
    return dict(tc=tc,th=th,qc=qc,qh=qh,work=work,sgen=entropy,
                work_min=work_min,excess_work=work-work_min,
                cop_r=qc/work if work else None,cop_h=qh/work if work else None,
                cop_r_bound=tc/(th-tc),cop_h_bound=th/(th-tc),
                compatible=entropy>=0)

def rates(ledger,duration):
    """Mean rates for one cycle of positive duration; no dynamic/power-limit model."""
    duration=rational(duration)
    if duration<=0:raise ValueError("positive seconds required")
    return {name:ledger[name]/duration for name in ('qc','qh','work','sgen')}

if __name__=='__main__':
    for work in (0,80,120,140):
        print(proposal(280,320,840,work))
    print("mean rates over 2s:",rates(proposal(280,320,840,140),2))
