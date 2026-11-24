# Integral de linha: massa, trabalho e multiplicidade

27/10/2026. Ampliação da aula existente para16 seções/12 exercícios, com apoio de IA, em rascunho. Três seções, dois exercícios, segmento resolvido, Python e desafio anteriores preservados. Revisão pessoal de Jhuann pendente. Fio, campo, figura e números próprios; sem experimento ou resultado de IC.

## Duas medidas

Curva regular por partes r(t), campos contínuos integráveis. Integral escalar ∫f ds=∫f(r(t))‖r′(t)‖dt. Integral vetorial ∫F·dr=∫F(r(t))·r′(t)dt. Massa exige densidade linear λ≥0, em kg/m; trabalho de força tem unidade N m=J. O parâmetro não precisa ser o tempo. Exemplo matemático anterior F=(y,x),r=(t,t) é adimensional; se interpretado fisicamente, requer coeficientes e escalas com unidades. Integral de trabalho do exemplo1, integral escalar de f=1 no segmento√2.

Regra da cadeia em r(φ(u)): r′(φ(u))φ′(u). A norma produz |φ′|, o produto vetorial preserva o sinal. Mudança monótona regular de uma passagem conserva massa e, se mantiver sentido, trabalho. Reversão mantém massa e troca sinal do trabalho. A mesma imagem percorrida duas vezes tem multiplicidade diferente; massa do fio físico exige cobri-lo uma vez.

## Exemplo semicircular original

Fio fino no semicírculo superior R=2 m, r(θ)=(Rcosθ,Rsinθ),0≤θ≤π, direita→esquerda. λ=λ0[1+(x/R)²],λ0=3 kg/m. No topo3, nos extremos6 kg/m. Norma de r′=R, portanto ds=Rdθ.

ComprimentoπR=2π m. Massa:

M=λ0R∫₀π(1+cos²θ)dθ=(3π/2)λ0R=9π kg.

Densidade média M/comprimento=9/2 kg/m. Simetria dá xCM=0. Momento em y:

∫yλds=λ0R²∫₀πsinθ(1+cos²θ)dθ=(8/3)λ0R².

Substituição z=cosθ dá∫₋₁¹(1+z²)dz=8/3. Logo yCM=16R/(9π)=32/(9π) m≈1,13177 m. Fio homogêneo no mesmo arco tem yCM=2R/π; nossa densidade maior nas pontas abaixa o centro. O centro pode ficar no interior do semidisco, sem material naquele ponto; não é uma partícula extra.

Campo F=k(−y,x),k=1 N/m. Produto com r′ é kR², portanto W=kπR²=4π J. Não se deduziu F da massa; é campo prescrito para comparar integrais. Inversão W=−4π J, M=9π kg. Reparametrização θ=π(u+u²)/2 tem derivadaπ(1+2u)/2>0 e conserva os dois valores. Ida e volta conta2M=18π kg na integral do percurso e W=0; não representa massa física duplicada do fio original.

Trocar o arco pelo diâmetro cria outro objeto: M=3∫₋₂²(1+x²/4)dx=16 kg. Extremos iguais não tornam integrais independentes do caminho. Potenciais e hipóteses de independência ficam para sua aula própria, ainda introdutória.

## Quadratura e contratos

`wire.py` usa Simpson composto para este fio e este campo. Entradas numéricas reais finitas int/float, sem bool; R eλ0 positivos, k pode ter qualquer sinal. Número par de painéis2..100000 (limite operacional). Modos: forward,reverse,nonlinear eout-and-back. O último soma duas integrais separadas, uma em cada sentido, preservando as derivadas laterais do percurso; não é só uma mudança de velocidade numa cobertura simples.

A densidade é avaliada na posição, velocidade paramétrica entra pela norma ou produto escalar. Retorno imutável: comprimento,massa,centro x/y e trabalho. Quadratura trigonométrica é aproximada em float; limites numéricos extremos podem produzir erro ou falha. Não há certificado de erro geral, implementação de curvas arbitrárias ou tratamento automático de auto-interseções. A rotina Simpson de apoio é exercitada nos intervalos parametrizados deste modelo.

Da raiz: `python3 -m unittest discover -s labs/linha-massa-trabalho -t .`.

Cinco testes:18 combinações de R,λ0 eparametrização contra fórmulas analíticas de comprimento,massa ecentro; orientação e passagem dupla; escalas e independência dos campos; Simpson em polinômios de grau≤3 e refinamento da parametrização não linear; contratos. As fórmulas analíticas são referências independentes da quadratura, não derivadas de um teste numérico. Amostras e teste de refinamento não substituem as provas por regra da cadeia ou integrais.

## Referência e edição

Tom M. Apostol,Cálculo volume2, tradução Reverté1996,reimpressão2004 do original2ª edição, metadados/sumário reconferidos. Consulta parcial em27/10/2026: §§10.2–10.4 pp.364–366/PDF377–379 e §§10.7–10.8 pp.370–371/PDF383–384. p.370/PDF383 inspecionada visualmente. Extração avisou sobre blocos comprimidos de algumas páginas; texto pertinente e imagem puderam ser conferidos, sem reparar ou alterar o PDF privado. Sem leitura integral. Não transferir paginação à edição inglesa.

MatemáticaIV CCM0223: aprovação2025/1 e ativação2025 vêm do mapa existente; programa e histórico não reabertos neste bloco. Parte diferencial da trilha Cálculo3 apoia MatemáticaIII; esta aula de integração apoia item1 de MatemáticaIV. O programa não comprova nível de domínio pessoal ou extensão ministrada. Não distribuímos PDF ou captura privada; a matriz de exemplo do texto, figura, redação e laboratório são próprios.

## Exercícios e revisão pessoal

Respostas dos12 itens:1; não;2π;9;9/2;0;32/(9π);4;−4; comprimento ds; dupla contagem; derivada da mudança de parâmetro. Dicas e resoluções completas na aula.

Duas sessões sugeridas de20min: massa/centro e trabalho; depois mudança de sentido, velocidade e multiplicidade. Dúvidas e avaliação pessoal em branco. Teoria geral de comprimento, potenciais, Green/Stokes, campos e curvas mais gerais e revisão por Jhuann pendentes.

Conferência de entrega: cinco testes locais e14 do catálogo aprovados;729 estruturas MathML verificadas. Em390px, exercício11 rejeitou cancelamento de massa por orientação e aceitou dupla contagem pelo Enter; figura inspecionada, sem transbordamento e sem erros de console. Revisão pessoal, leitor de tela e Windows real pendentes.
