"""N corpos pontuais em 2D; Euler–Cromer e velocity Verlet, sem dependências."""
from math import cos, sin, sqrt, fsum, isfinite, hypot

def finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('Valores numéricos finitos, sem booleanos')
    return float(x)

def state(masses, positions, velocities):
    m=tuple(finite(x) for x in masses)
    if not 2<=len(m)<=20 or any(x<=0 for x in m):
        raise ValueError('De 2 a 20 massas positivas')
    def vectors(values):
        out=tuple(tuple(finite(x) for x in row) for row in values)
        if len(out)!=len(m) or any(len(row)!=2 for row in out):
            raise ValueError('Um vetor 2D por massa')
        return out
    return m, vectors(positions), vectors(velocities)

def acceleration(m, r):
    # Cada par é visitado uma vez: mesma geometria para ambas as forças.
    a=[[0.,0.] for _ in m]
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            d=[r[j][k]-r[i][k] for k in range(2)]
            radius=hypot(*d)
            if radius==0: raise ValueError('Colisão não resolvida')
            for k in range(2):
                field=d[k]/radius**3
                a[i][k]+=m[j]*field
                a[j][k]-=m[i]*field
    return a

def diagnostics(m,r,v):
    total=fsum(m)
    energy=fsum(.5*m[i]*fsum(x*x for x in v[i]) for i in range(len(m)))
    distances=[]
    for i in range(len(m)):
        for j in range(i+1,len(m)):
            radius=hypot(r[i][0]-r[j][0],r[i][1]-r[j][1])
            if radius==0: raise ValueError('Colisão não resolvida')
            energy-=m[i]*m[j]/radius
            distances.append(radius)
    return dict(energy=energy,
                momentum=[fsum(m[i]*v[i][k] for i in range(len(m))) for k in range(2)],
                center=[fsum(m[i]*r[i][k] for i in range(len(m)))/total for k in range(2)],
                angular=fsum(m[i]*(r[i][0]*v[i][1]-r[i][1]*v[i][0]) for i in range(len(m))),
                min_distance=min(distances))

def integrate(masses,positions,velocities,time,steps,method='verlet'):
    m,r,v=state(masses,positions,velocities)
    time=finite(time)
    if time<=0 or isinstance(steps,bool) or not isinstance(steps,int) or not 1<=steps<=10000:
        raise ValueError('Tempo positivo e de 1 a 10000 passos')
    if method not in ('cromer','verlet'):raise ValueError('Método cromer ou verlet')
    h=time/steps
    trace=[dict(time=0.,positions=r,velocities=v,**diagnostics(m,r,v))]
    a=acceleration(m,r)
    for n in range(steps):
        if method=='cromer':
            v=tuple(tuple(v[i][k]+h*a[i][k] for k in range(2)) for i in range(len(m)))
            r=tuple(tuple(r[i][k]+h*v[i][k] for k in range(2)) for i in range(len(m)))
            a=acceleration(m,r)
        else:
            new_r=tuple(tuple(r[i][k]+h*v[i][k]+.5*h*h*a[i][k] for k in range(2)) for i in range(len(m)))
            new_a=acceleration(m,new_r)
            v=tuple(tuple(v[i][k]+.5*h*(a[i][k]+new_a[i][k]) for k in range(2)) for i in range(len(m)))
            r,a=new_r,new_a
        diag=diagnostics(m,r,v)
        if not all(isfinite(x) for row in (*r,*v) for x in row) or not isfinite(diag['energy']):
            raise ValueError('Estado não finito; reveja escala e passo')
        trace.append(dict(time=(n+1)*h,positions=r,velocities=v,**diag))
    return trace

def binary():
    return [1.,1.],[[-.5,0.],[.5,0.]],[[0.,-1/sqrt(2)],[0.,1/sqrt(2)]]

def exact_binary(t):
    # Só vale para binary(), G=1, sem suavização.
    x,y=.5*cos(sqrt(2)*t),.5*sin(sqrt(2)*t)
    return [[-x,-y],[x,y]]

def position_error(trace):
    last=trace[-1]; exact=exact_binary(last['time'])
    return max(hypot(*(last['positions'][i][k]-exact[i][k] for k in range(2))) for i in range(2))

if __name__=='__main__':
    # Instante não periódico evita cancelamento acidental no estudo da ordem.
    for method in ('cromer','verlet'):
        for steps in (20,40,80,160):
            trace=integrate(*binary(),.7,steps,method)
            drift=max(abs(row['energy']-trace[0]['energy']) for row in trace)
            print(method,steps,'erro de posição:',position_error(trace),'máximo |ΔE|:',drift)
