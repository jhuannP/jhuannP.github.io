"""Rótulo gregoriano UT1 -> JD(UT1); não converte UTC ou fuso."""
from datetime import date
from fractions import Fraction as Q

ANCHOR = date(2000, 1, 1)
JD_ANCHOR_MIDNIGHT = Q(4903089, 2)  # 2451544.5, 2000-01-01 00h UT1

def jd_ut1(year, month, day, seconds_ut1=0):
    """1901..2099; segundos da leitura UT1 em [0,86400), int/Fraction."""
    if any(type(x) is not int for x in (year, month, day)):
        raise ValueError('Ano, mês e dia exigem int, sem bool')
    if not 1901 <= year <= 2099:
        raise ValueError('Recorte didático: anos 1901..2099')
    if type(seconds_ut1) not in (int, Q):
        raise ValueError('Segundos UT1 exigem int/Fraction, sem bool/float/texto')
    t = Q(seconds_ut1)
    if not 0 <= t < 86400:
        raise ValueError('Leitura UT1 dentro do dia: 0 <= segundos < 86400')
    current = date(year, month, day)  # valida o calendário gregoriano
    return JD_ANCHOR_MIDNIGHT + (current - ANCHOR).days + t / 86400

if __name__ == '__main__':
    for h in (0, 6, 12, 18):
        print('2000-01-01', h, 'h UT1: JD =', jd_ut1(2000, 1, 1, h*3600))
    assert jd_ut1(1978, 7, 21, 15*3600) == Q(19549689, 8)
