# Mistura enzimática fechada e aproximações

Rascunho original para revisão de Jhuann. Simulação sintética, sem medições ou resultados da IC atribuídos a ele.

## Fontes consultadas em 16/10/2026

- Lehninger/Nelson/Cox, sexta edição: trechos de 6.3, páginas impressas 201–202 (PDF 231–232), janela inicial e formação do complexo. Leitura parcial, sem figura/exercício/PDF reproduzido.
- [Eilertsen e Schnell, arXiv:1911.03445v3](https://arxiv.org/abs/1911.03445): introdução e seção 2.1, páginas numeradas 5–7 do PDF, EDOs, inventários e escalas. Não leitura integral das 51 páginas ou reprodução da análise/figuras. O acesso inicial ao PMC exigiu verificação de navegador; a versão aberta dos autores foi consultada no arXiv.

Presets, código, gráficos e exercícios próprios. Não se usa o artigo para afirmar que um ε finito arbitrário garante precisão em todo horizonte.

## Sistemas comparados

Frasco: s' = −(Eₜ−c)s+c, c'=(Eₜ−c)s−2c, p'=c, com k1=1 μM⁻¹s⁻¹ e k−1=kcat=1 s⁻¹, s(0)=S₀, c(0)=p(0)=0. Enzima livre Eₜ−c; inventário s+c+p=S₀. As três espécies são integradas separadamente, sem reconstruir p ou cortar valores para esconder violações.

Redução escalar: S*' = −EₜS*/(2+S*), P*=S₀−S*. Resolve-se a relação integrada monotônica por bisseção em ln(S*/S₀), sem segundo RK4. S* não é o substrato livre exato quando o complexo retém quantidade importante.

Reservatório: mantém s=S₀; seu produto pode superar o inventário do frasco porque há alimentação. O relatório não o trata como previsão fechada válida. ε=Eₜ/(KM+S₀) e 1/[k1(S₀+KM)] são diagnósticos iniciais de escala, sem classificação automática por um limite arbitrário.

Três presets (S₀,Eₜ) em μM: (2;0,02), (2;2), (0,2;2). Janela rápida de 2 s ou prolongada de 40/8/8 s. O gráfico usa frações de S₀; o erro entre produtos também é normalizado por S₀, não por p perto de zero.

## Verificação e reprodução

Na raiz: `python3 -m unittest discover -s labs/enzima-fechada -t .`.

Quatro testes: inventário, monotonicidade de produto e limites físicos nas seis janelas; solução exata de ligação sem catálise em doze casos; refinamento e nove referências independentes de Taylor para o mecanismo completo; derivada de inventário e domínio. Dezoito configurações JS/Python estão em `reference.json`.

`verify_taylor.py` integra por séries polinomiais com Decimal de 60 dígitos. Ordens 18 e 20 concordam abaixo de 1e−30 nos nove pontos escolhidos antes de emitir `taylor_reference.json`. O passo da referência foi reduzido para atingir essa concordância; esse controle não é uma prova geral de erro. O RK4 é comparado com tolerância absoluta 3e−9 nesses pontos e 2e−8 entre duas malhas nas seis janelas. A referência é um algoritmo diferente do RK4, e o limite kcat=0 tem solução analítica de Riccati. Nenhuma instalação externa é necessária.

O passo interno é escolhido por uma escala de taxa dos presets; sua fórmula não é um teorema de estabilidade para toda rede química. A malha refinada, os inventários e as referências conferem estes exemplos. Erro de redução não desaparece ao refinar a integração completa.

## Pendências

Solvers adaptativos/rígidos gerais, redução total, prova de erro, reação inversa de produto, inibição, transporte e incerteza experimental. Depois deste bloco, alternar áreas; Biologia I continua parcial e aguarda revisão pessoal.
