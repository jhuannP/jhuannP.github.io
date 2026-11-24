from pathlib import Path
points_f=[];points_g=[]
for i in range(801):
 x=-8+16*i/800;f=(2*x*x+1)/(x*x+3);g=2+x/(x*x+1)
 points_f.append(f'{60+25*(x+8):.3f},{330-80*f:.3f}')
 points_g.append(f'{60+25*(x+8):.3f},{330-80*g:.3f}')
svg='''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="510" viewBox="0 0 520 510" role="img" aria-labelledby="title desc"><title id="title">Mesma assíntota, comportamentos distintos</title><desc id="desc">Duas curvas na janela de menos oito a oito. f igual a dois x ao quadrado mais um sobre x ao quadrado mais três fica sempre abaixo de dois. g igual a dois mais x sobre x ao quadrado mais um cruza a reta horizontal y dois em x zero. A reta y dois é assíntota de ambas nos dois extremos; a janela finita não prova esses limites.</desc><rect width="520" height="510" fill="#f7f4eb"/>
<g fill="#182e38" font-family="sans-serif" font-size="21"><text x="20" y="35" font-size="25">Assíntota horizontal não é barreira</text><text x="20" y="71">Mesmos eixos; janela −8 ≤ x ≤ 8</text></g>
<g stroke="#d4dbd3" stroke-width="1"><path d="M60 90V330 M160 90V330 M260 90V330 M360 90V330 M460 90V330 M60 90H460 M60 250H460"/></g>
<path d="M60 330H480 M260 90V345" stroke="#758279" stroke-width="1.5" fill="none"/>
<path d="M60 170H460" stroke="#758279" stroke-width="2" stroke-dasharray="3 5"/>
'''+f'<polyline points="{" ".join(points_f)}" stroke="#176153" stroke-width="3" fill="none"/><polyline points="{" ".join(points_g)}" stroke="#182e38" stroke-width="2.5" stroke-dasharray="8 5" fill="none"/>'+'''
<circle cx="260" cy="170" r="4" fill="#182e38"/>
<g fill="#182e38" font-family="sans-serif" font-size="20"><text x="26" y="97">3</text><text x="26" y="177">2</text><text x="26" y="257">1</text><text x="26" y="337">0</text><text x="46" y="365">−8</text><text x="146" y="365">−4</text><text x="253" y="365">0</text><text x="354" y="365">4</text><text x="454" y="365">8</text><text x="481" y="337">x</text><text x="18" y="127">y</text><text x="282" y="153">g(0) = 2</text><text x="20" y="412" fill="#176153">f, linha contínua: (2x²+1)/(x²+3)</text><text x="20" y="449">g, tracejada: 2 + x/(x²+1)</text><text x="20" y="486">Pontilhada: y = 2 · limite provado no texto</text></g></svg>'''
Path(__file__).with_name('comparacao.svg').write_text(svg)
