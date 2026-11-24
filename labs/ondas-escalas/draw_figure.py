from pathlib import Path
import math
path=[]
for i in range(241):
 x=4*i/240;path.append(f'{60+105*x:.3f},{200-50*math.sin(math.pi*x):.3f}')
time=[]
for i in range(241):
 t=.4*i/240;time.append(f'{60+1050*t:.3f},{470-50*math.cos(10*math.pi*t):.3f}')
parts=['''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="600" viewBox="0 0 520 600" role="img" aria-labelledby="title desc"><title id="title">Espaço e tempo da mesma onda</title><desc id="desc">O perfil espacial em t zero tem duas cristas separadas por dois metros. A oscilação no ponto fixo x igual a meio metro tem máximos separados por zero vírgula dois segundo. Ambos usam amplitude zero vírgula zero cinco metro.</desc><rect width="520" height="600" fill="#f6f3eb"/><g font-family="sans-serif" fill="#172845" font-size="21"><text x="20" y="34" font-size="27" font-weight="bold">Mesmo padrão: duas leituras</text><text x="20" y="67" font-size="22">A=0,05 m; f=5 Hz; λ=2 m</text><text x="60" y="102" font-size="24">Perfil y(x,0)</text><text x="60" y="363" font-size="24">Ponto fixo: y(0,5 m,t)</text><g stroke="#172845" stroke-width="1.3" fill="none"><path d="M60 140V255 M60 200H480 M60 410V525 M60 470H480"/></g>''',f'<polyline points="{" ".join(path)}" fill="none" stroke="#264bb5" stroke-width="3"/>',f'<polyline points="{" ".join(time)}" fill="none" stroke="#264bb5" stroke-width="3"/>']
for yy in [200,470]:
 for val,dy in [('0,05',-50),('0',0),('−0,05',50)]:parts.append(f'<text x="51" y="{yy+dy+7}" text-anchor="end">{val}</text>')
for i in range(5):parts.append(f'<text x="{60+105*i}" y="281" text-anchor="middle">{i}</text>')
for i in range(5):parts.append(f'<text x="{60+105*i}" y="554" text-anchor="middle">{str(i/10).replace(".",",")}</text>')
parts.append('''<g stroke="#264bb5" stroke-width="2"><path d="M112.5 126H322.5 M112.5 121V131 M322.5 121V131 M60 399H270 M60 394V404 M270 394V404"/></g><text x="217.5" y="121" text-anchor="middle" fill="#264bb5">λ=2 m</text><text x="165" y="394" text-anchor="middle" fill="#264bb5">T=0,2 s</text><text x="400" y="310">x (m)</text><text x="400" y="586">t (s)</text><text x="8" y="130">y (m)</text><text x="8" y="400">y (m)</text></g></svg>''')
Path(__file__).with_name('espaco-tempo.svg').write_text(''.join(parts))
