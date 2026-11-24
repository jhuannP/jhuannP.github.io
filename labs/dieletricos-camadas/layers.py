"""Capacitor plano de duas camadas: grandezas normalizadas, não dados de material."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise ValueError('Use inteiro ou Fraction; não bool ou float.')
    return Q(x)


def solve(k1, k2, d1, d2, voltage, sheet=0):
    """z crescente, phi(0)=voltage e phi(d1+d2)=0; folha livre em z=d1.

    E em Eref; z em lref; phi em Eref*lref; D/P/sigma em epsilon0*Eref;
    C em epsilon0*A/lref; Q em epsilon0*A*Eref; U em epsilon0*A*lref*Eref**2.
    Sem campo exterior, bordas, perdas, anisotropia ou dinâmica.
    """
    k1, k2, d1, d2, voltage, sheet = map(rational, (k1,k2,d1,d2,voltage,sheet))
    if min(k1,k2,d1,d2) <= 0:
        raise ValueError('kappa e espessuras devem ser positivos.')
    inverse_capacity = d1/k1 + d2/k2
    D1 = (voltage - sheet*d2/k2)/inverse_capacity
    D2 = D1 + sheet
    E1, E2 = D1/k1, D2/k2
    P1, P2 = (k1-1)*E1, (k2-1)*E2
    phi_interface = E2*d2
    return dict(k1=k1,k2=k2,d1=d1,d2=d2,voltage=voltage,sheet=sheet,
                E1=E1,E2=E2,D1=D1,D2=D2,P1=P1,P2=P2,
                phi_interface=phi_interface,capacity=1/inverse_capacity,
                free_bottom=D1,free_top=-D2,
                bound_bottom=-P1,bound_interface=P1-P2,bound_top=P2,
                energy=(k1*E1**2*d1+k2*E2**2*d2)/2)


def potential(state, z):
    """Potencial contínuo no intervalo fechado entre as placas."""
    z = rational(z)
    if not 0 <= z <= state['d1']+state['d2']:
        raise ValueError('z fora do capacitor idealizado.')
    if z <= state['d1']:
        return state['voltage']-state['E1']*z
    return state['E2']*(state['d1']+state['d2']-z)


if __name__ == '__main__':
    for sheet in [0,1]:
        print('Entradas prescritas, normalizadas; folha livre =',sheet)
        print(solve(2,5,1,2,Q(9,5),sheet))
