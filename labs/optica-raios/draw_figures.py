"""Figuras originais; executar na raiz do site com Python padrão."""
from pathlib import Path
from math import sqrt
out=Path(__file__).parent
common='''<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="context-stroke"/></marker></defs>'''
yin=240-100*sqrt(3);xt=260+170/3;yt=240+170*sqrt(8)/3
interface=f'''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="480" viewBox="0 0 520 480" role="img" aria-labelledby="title desc"><title id="title">Ângulos medidos pela normal</title><desc id="desc">Raio incidente a trinta graus da normal em n1 igual a um. O refletido também faz trinta graus. Em n2 igual a três meios, o refratado faz aproximadamente dezenove vírgula quarenta e sete graus, aproximando-se da normal.</desc>{common}
<rect width="520" height="480" fill="#f7f4eb"/><rect y="240" width="520" height="240" fill="#e5efed"/>
<path d="M20 240H500" stroke="#182e38" stroke-width="2"/><path d="M260 60V425" stroke="#667770" stroke-width="1.5" stroke-dasharray="7 6"/>
<g stroke-width="3" fill="none" marker-end="url(#arrow)"><path d="M160 {yin}L260 240" stroke="#3547a0"/><path d="M260 240L360 {yin}" stroke="#827449"/><path d="M260 240L{xt} {yt}" stroke="#176153"/></g>
<g stroke="#52675e" stroke-width="1.3" fill="none"><path d="M236 198.43A48 48 0 0 1 260 192"/><path d="M260 180A60 60 0 0 1 290 188.04"/><path d="M260 310A70 70 0 0 0 283.33 306"/></g>
<g fill="#182e38" font-family="sans-serif" font-size="22"><text x="20" y="34" font-size="26">Uma normal, três raios</text><text x="275" y="83">normal</text><text x="20" y="114">incidente</text><text x="380" y="114">refletido</text><text x="170" y="195">30°</text><text x="302" y="185">30°</text><text x="20" y="222">n₁ = 1</text><text x="20" y="280">n₂ = 3/2</text><text x="337" y="351">≈ 19,47°</text><text x="337" y="383">refratado</text><text x="20" y="454">Snell: sin θ₂ = (1 ÷ 3/2) × 1/2 = 1/3</text></g></svg>'''
(out/'interface.svg').write_text(interface)
lens=f'''<svg xmlns="http://www.w3.org/2000/svg" width="520" height="420" viewBox="0 0 520 420" role="img" aria-labelledby="title desc"><title id="title">Objeto e imagem em dois focos</title><desc id="desc">Lente fina convergente com f dois centímetros, objeto real a quatro centímetros e imagem real a quatro centímetros, invertida e do mesmo tamanho. Um raio paralelo passa pelo foco imagem; outro atravessa o centro sem desvio no modelo fino. Alturas são ampliadas no desenho.</desc>{common}
<rect width="520" height="420" fill="#f7f4eb"/>
<g fill="#182e38" font-family="sans-serif" font-size="21"><text x="20" y="34" font-size="25">p = q = 4 cm · f = 2 cm</text><text x="20" y="69">Alturas ampliadas para visualizar os raios</text></g>
<path d="M20 190H500" stroke="#68766e" stroke-width="1.5"/>
<path d="M260 98V287 M253 108L260 98L267 108 M253 277L260 287L267 277" fill="none" stroke="#68766e" stroke-width="2"/>
<g fill="none" stroke-width="2" marker-end="url(#arrow)"><path d="M60 140H260L460 240" stroke="#176153"/><path d="M60 140L460 240" stroke="#3547a0"/></g>
<g stroke="#182e38" stroke-width="3" marker-end="url(#arrow)"><path d="M60 190V140"/><path d="M460 190V240"/></g>
<g fill="#182e38" font-family="sans-serif" font-size="21"><text x="25" y="116">+0,2 cm</text><text x="385" y="280">−0,2 cm</text><text x="144" y="248">F</text><text x="351" y="248">F′</text><text x="230" y="315">lente</text><text x="126" y="364">p = 4 cm</text><text x="329" y="364">q = 4 cm</text><text x="20" y="403">Imagem real invertida: m = −q/p = −1</text></g>
<g stroke="#68766e" stroke-width="1.5"><path d="M160 184V196 M360 184V196 M60 332H260 M260 332H460 M60 326V338 M260 326V338 M460 326V338"/></g></svg>'''
(out/'lens-2f.svg').write_text(lens)
