"""Balanço de um fóton; fluxo/corrente apenas com rendimento estipulado."""
import math
H=6.62607015e-34
E=1.602176634e-19
C=299792458
AREA=1e-6  # m²: 1 mm²
YIELD=.2  # hipótese do exemplo, não propriedade medida


def model(ratio=1.5,work_ev=2,irradiance=2):
    if not all(math.isfinite(x) for x in [ratio,work_ev,irradiance]) or ratio<=0 or work_ev<=0 or irradiance<0:
        raise ValueError('Razão e função trabalho positivas, irradiância não negativa')
    photon_ev=ratio*work_ev
    threshold_hz=work_ev*E/H
    frequency_hz=ratio*threshold_hz
    state='below' if ratio<1 else 'threshold' if ratio==1 else 'above'
    kinetic_ev=None if state=='below' else (ratio-1)*work_ev
    photon_rate=irradiance*AREA/(photon_ev*E)
    emitted_rate=0 if irradiance==0 or state=='below' else None if state=='threshold' else YIELD*photon_rate
    current_a=None if emitted_rate is None else E*emitted_rate
    return dict(ratio=ratio,work_ev=work_ev,irradiance=irradiance,photon_ev=photon_ev,
                threshold_hz=threshold_hz,frequency_hz=frequency_hz,wavelength_nm=C/frequency_hz*1e9,
                state=state,kinetic_ev=kinetic_ev,stopping_v=kinetic_ev,
                photon_rate=photon_rate,emitted_rate=emitted_rate,current_a=current_a)


if __name__=='__main__':
    for ratio in [.5,1,1.5]:
        r=model(ratio)
        print(r['state'], 'Kmax/eV=',r['kinetic_ev'],'f/THz=',r['frequency_hz']/1e12)
    assert model(.5)['kinetic_ev'] is None
    assert model(1.5)['kinetic_ev']==1
