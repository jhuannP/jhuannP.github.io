# Integral tripla: primeiro a região, depois massa e momentos

Notas de aula originais em rascunho. Apoio parcial a integrais múltiplas de MatemáticaIV, sem equivalência integral entre a trilha Cálculo3 e uma disciplina. Pré-requisitos: integrais duplas, integração por etapas e unidades. Não comprova estudo realizado ou domínio pessoal de Jhuann.

## Medida de volume não é densidade

A soma de valores de f multiplicados pelos pequenos volumesΔxΔyΔz leva à integral tripla quando o limite existe. Nos exemplos de funções contínuas em caixas e tetraedros compactos, trabalhamos com integrais bem definidas. Integrar1 dá volume; integrarρ≥0 em kg/m³ dá massa. Um integrando adimensional1 e uma densidade numericamente1kg/m³ têm interpretações diferentes, mesmo se os valores numéricos coincidirem em unidades escolhidas.

No cubo normalizado[0,1]³, a densidade adimensional escolhida é x+y+z. Cada termo integra1/2, dando massa normalizada3/2. Para um cubo físico de lado L, tomeρ=ρ₀(x/L+y/L+z/L). A substituição x=Lu,y=Lv,z=Lw tem JacobianoL³, logo M=(3/2)ρ₀L³. O primeiro momento em x é(5/6)ρ₀L⁴, pois a integral normalizada de x(x+y+z) é1/3+1/4+1/4=5/6. Portanto x̄=5L/9; idem nas outras coordenadas.

Permutar eixos preserva região e densidade, justificando coordenadas iguais. Refletir x→L−x não preserva essa densidade; não justifica x̄=L/2. Para densidade uniforme, as reflexões permitiriam o centro geométrico.

## Tetraedro: os limites são parte do problema

O sólido D={x,y,z≥0;x+y+z≤1} tem projeção triangular0≤x≤1,0≤y≤1−x. Sobre cada ponto,0≤z≤1−x−y. Para f=1, a integral interna é1−x−y; a seguinte,(1−x)²/2; a última,1/6. Trocar todos os limites por[0,1] daria o cubo, outro sólido.

Para f=x+y+z:

1. A integral em z é[(x+y)z+z²/2]₀^(1−x−y)=[1−(x+y)²]/2.
2. Integrar em y entre0 e1−x dá1/3−x/2+x³/6.
3. Integrar em x entre0 e1 dá1/3−1/4+1/24=1/8.

Os momentos básicos são∭x²=1/60 e∭xy=∭xz=1/120, então o primeiro momento para f é1/30 e a coordenada de centro de massa é(1/30)/(1/8)=4/15. Para conferir os momentos diretamente, uma integração sucessiva de x^a y^b z^c neste tetraedro, com a,b,c inteiros não negativos, fornece a!b!c!/(a+b+c+3)!. Isso resulta de integrar z e usar repetidamente a integral de potência vezes(1−x)^n, ou integração por partes. No código essa referência é confrontada com outra mudança de variáveis e uma quadratura exata para os graus usados.

Uma ordem alternativa válida é0≤z≤1,0≤y≤1−z,0≤x≤1−y−z. As hipóteses de continuidade nos sólidos regulares do recorte permitem a troca; não se permutam diferenciais mantendo limites com dependências erradas. Casos impróprios e domínios gerais não estão encerrados.

## Esfera: convenção e Jacobiano

Use r≥0,φ polar a partir de z,0≤φ≤π,θ azimutal0≤θ<2π. O mapa é x=r senφcosθ,y=r senφsenθ,z=r cosφ. O módulo do Jacobiano é r²senφ. Localmente, as três direções coordenadas ortogonais têm fatores1,r,r senφ. Os conjuntos onde a parametrização degenera são bordas de volume nulo neste exemplo; não se somam cópias extras por causa deles.

Na bola, o volume é(R³/3)×2×2π=4πR³/3. Com densidade uniformeρ₀, multiplique pela densidade para obter massa; reflexões preservam ambos os objetos e dão centro na origem. Omitir o Jacobiano produziria2π²R: escala de comprimento, incompatível com volume. O laboratório só confere f=1 no exemplo esférico separável, não um integrador geral de esféricas.

## Código: outra rota para os momentos

Execute `python3 labs/triplas-regiao-massa/moments.py`. Em uma caixa, usa regra de Boole nos três eixos, com nós0,1/4,1/2,3/4,1 e pesos(7,32,12,32,7)/90. As seis identidades para monômios de graus0–5 conferem, por linearidade, sua exatidão para polinômios até grau5 em cada variável.

Para o tetraedro, o código mapeia o cubo: x=u,y=(1−u)v,z=(1−u)(1−v)w, com0≤u,v,w≤1. A matriz derivada é triangular na ordem usada, com diagonal1,1−u,(1−u)(1−v), e determinante(1−u)²(1−v). O interior é mapeado sem repetição; bordas colapsadas têm volume nulo. Multiplicar pelo determinante é indispensável. Para x^a y^b z^c com grau total até3, o integrando transformado tem graus no máximo5 em u,4 em v,3 em w; Boole é exata nesses casos. Não se afirma exatidão para uma função arbitrária entregue à rotina.

Seis testes:20 monômios em cada sólido, confrontados com antiderivadas independentes; massas/momentos/centros conhecidos;32 combinações de domínio/L/ρ₀ para escala; esfera por integração de sinφ com Simpson e refinamento; medida/domínio/exatidão de Boole; contratos. No exemplo esférico, parte radial e azimutal são analíticas e apenas o fator angular é aproximado. O erro relativo em32 subintervalos ficou abaixo de10⁻⁶ nos raios escolhidos; não é limite geral de erro para outros integrandos.

Comρ₀=0, a massa é zero e o código devolve center=None, sem fazer0/0. Com massa positiva, normalizarρ/M produz uma densidade de probabilidade em volume; a densidade de massa original não precisa integrar1. O código é específico destes exemplos, sem dados reais ou certificação automática de integrabilidade.

## Referências consultadas

- Apostol, *Cálculo*,volume2, tradução Reverté1996/reimpressão2004, original indicado como segunda edição: §11.31 pp.455–457/PDF468–470, consulta textual parcial em27/10/2026, extensão dimensional e integrações repetidas. Extração contém ruído; sem nova inspeção visual, leitura integral, cópia de exercícios ou distribuição do exemplar. Paginação não transferida ao inglês da referência oficial. O início de§11.32 aparece na última página consultada, sem alegar leitura integral da seção.
- [OpenStax CalculusVolume3 §5.4](https://openstax.org/books/calculus-volume-3/pages/5-4-triple-integrals), consulta parcial em27/10/2026 para integrais triplas e ordem.
- [OpenStax CalculusVolume3 §5.5](https://openstax.org/books/calculus-volume-3/pages/5-5-triple-integrals-in-cylindrical-and-spherical-coordinates), consulta parcial em27/10/2026 para convenção esférica e medida de volume.

Exemplos, figura, deduções e laboratório preparados para estas notas; modelos e regras clássicos não são descobertas próprias. Revisão conceitual e didática pessoal pendente.

## Próxima revisão — vinte minutos

Desenhe a projeção do tetraedro, reconstrua volume1/6 e massa1/8 e explique por que5/9 e4/15 exigem momentos. Depois restaure as unidades deρ₀,L e verifique por que o centro é indefinido com massa zero.
