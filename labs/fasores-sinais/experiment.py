"""Convenção x(t)=Re[Z exp(i omega t)], com omega>0 e amplitudes de pico."""
import math

def checked_phasor(z):
    if type(z) not in (int,float,complex):
        raise ValueError("Use amplitude complexa numérica finita")
    z = complex(z)
    if not math.isfinite(z.real) or not math.isfinite(z.imag):
        raise ValueError("Amplitude deve ser finita")
    return z

def real_parameter(x):
    if type(x) not in (int,float) or not math.isfinite(x):
        raise ValueError("Parâmetro real finito necessário")
    return float(x)

def polar(z):
    z = checked_phasor(z)
    amplitude = abs(z)
    if not math.isfinite(amplitude):
        raise ValueError("Módulo fora da faixa numérica")
    return amplitude, None if z == 0 else math.atan2(z.imag,z.real)

def signal(z,omega,t):
    z=checked_phasor(z); omega=real_parameter(omega); t=real_parameter(t)
    if omega <= 0 or not math.isfinite(omega*t):
        raise ValueError("omega deve ser positiva e omega*t finito")
    angle=omega*t
    result=z.real*math.cos(angle)-z.imag*math.sin(angle)
    if not math.isfinite(result):
        raise ValueError("Resultado fora da faixa numérica")
    return result

def derivative(z,omega,t):
    z=checked_phasor(z); omega=real_parameter(omega)
    return signal(1j*omega*z,omega,t)

if __name__ == "__main__":
    first,second=3+4j,-3+4j
    total=first+second
    print("Soma, amplitude e fase:",total,polar(total))
    print("x(0), x'(0) para omega=2:",signal(total,2,0),derivative(total,2,0))
    print("Cancelamento:",polar(1+(-1)))
