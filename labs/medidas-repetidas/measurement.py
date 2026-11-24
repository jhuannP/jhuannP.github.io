"""Momentos racionais e correção aditiva; hipóteses estatísticas externas."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int ou Fraction, sem bool/float/texto')
    return Q(x)

def summarize(readings):
    if type(readings) not in (list,tuple) or len(readings)<2:
        raise ValueError('Forneça lista/tupla com pelo menos duas leituras')
    x=tuple(map(rational,readings));n=len(x);mean=sum(x,Q(0))/n
    sample_variance=sum(((v-mean)**2 for v in x),Q(0))/(n-1)
    return dict(n=n,mean=mean,sample_variance=sample_variance,
                mean_variance=sample_variance/n)

def corrected(readings,bias_estimate,calibration_standard_uncertainty):
    """Modelo y=mean-b; cov(mean,b)=0 deve ser justificada fora do código."""
    s=summarize(readings);b=rational(bias_estimate)
    u=rational(calibration_standard_uncertainty)
    if u<0:raise ValueError('Incerteza padrão não pode ser negativa')
    return dict(s,corrected_mean=s['mean']-b,
                calibration_variance=u*u,combined_variance=s['mean_variance']+u*u)

def rectangular_variance(half_width):
    a=rational(half_width)
    if a<0:raise ValueError('Semilargura não negativa')
    return a*a/3

if __name__=='__main__':
    x=[Q(49,5),10,Q(51,5)]  # cm, dados sintéticos
    print(corrected(x,Q(3,10),Q(1,10)))
    assert corrected(x,Q(3,10),Q(1,10))['combined_variance']==Q(7,300)
