"""Solenoide infinito preenchido por meio linear isotrópico: valores racionais em SI."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float.')
    return Q(x)


def solenoid(turns_per_m,current,chi):
    n,I,chi=map(rational,(turns_per_m,current,chi))
    if n<0 or chi<=-1:raise ValueError('n>=0 e chi>-1 necessários neste modelo.')
    H=n*I;M=chi*H
    return dict(H=H,M=M,B_over_mu0=H+M,mu_relative=1+chi,
                free_sheet=n*I,bound_sheet=M)


if __name__=='__main__':
    for chi in (Q(1,1000),Q(0),Q(-1,1000)):
        print('chi=',chi,solenoid(1000,2,chi))
    print('H,M,K em A/m; B/mu0 também em A/m. Multiplicar por mu0 para B em tesla.')
    print('Sem bordas, desmagnetização finita, histerese ou modelo microscópico.')
