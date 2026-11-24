# Limite central: lei exata e aproximação normal

Laboratório original, com apoio de IA e revisão pessoal pendente. Leis e eventos prescritos; não usa amostras, dados de pesquisa ou gerador aleatório.

## Resultado e hipóteses

Na versão clássica, Xᵢ são IID, com média μ e 0<σ²<∞, mantendo a lei ao crescer n. Zₙ=(Sₙ−nμ)/(σ√n) converge em distribuição para uma normal padrão. A lei dos grandes números e o TCL respondem a perguntas diferentes: concentração de X̄ em μ versus distribuição de suas flutuações padronizadas.

A aula apresenta um esboço por funções características, φ_Y(u)=1−u²/2+o(u²), e [φ_Y(t/√n)]ⁿ→e^(−t²/2), invocando o teorema de continuidade de Lévy. Não prova esse teorema auxiliar, versões de dependência ou taxas universais de convergência.

## Comparação equilibrada

K~Binomial(16,1/2), evento 6≤K≤10. Média 8, variância 4 e desvio 2:

| Cálculo | Probabilidade |
|---|---:|
| Binomial exata | 25883/32768 ≈ 0,789886475 |
| Normal, limites 6 e 10 | 0,682689492 |
| Normal corrigida, limites 5,5 e 10,5 | 0,788700453 |

Os erros absolutos são ≈0,107196982 e ≈0,001186022, respectivamente. São valores desse evento, não uma cota ou promessa para qualquer aplicação. Na figura, as barras são massas exatas e a linha liga áreas normais em células de largura um; não compara uma massa com uma densidade sem especificar a área.

P(K=8)=6435/32768 é positivo, mas uma normal contínua atribui massa zero ao ponto 8. A correção de continuidade explicita um evento contínuo aproximador. O código não renormaliza as áreas normais para somarem um no suporte discreto.

## Contagem rara

K~Binomial(100,1/100): P(K=0)=P(K≤0)=(99/100)¹⁰⁰≈0,366032341. A normal com média 1 e variância 0,99 fornece, com correção na cauda, Φ((0,5−1)/√0,99)≈0,307651278. Erro absoluto ≈0,058381063, apesar de n=100. Não há corte universal em n=30; a lei, o evento e a precisão desejada importam.

p permanece fixo em cada aplicação do TCL clássico. Mudar p com n introduz outra sequência e exige análise adicional; não é feito para afirmar um limite normal neste laboratório.

## Implementação e contrato

`masses` calcula probabilidades com int/Fraction e fórmula binomial, 1≤n≤256, p∈[0,1], denominador≤1000. Inclui leis degeneradas p=0 ou1. A aproximação normal as rejeita por variância zero. Não aceita bool/float para n/p.

`exact` e `approximate` recebem limites inteiros inclusivos, com None para uma cauda infinita. A correção afasta a fronteira inferior por 1/2 e a superior por 1/2; None mantém infinito. O exemplo raro usa limite inferior None, não uma célula finita em torno de zero. Como a normal tem suporte real, aproximar descrições diferentes de um evento discreto pode envolver escolhas de fronteira distintas; a chamada efetiva fica explícita. Não há truncamento ou correção automática de caudas.

A integração normal usa erf/erfc em floats, sem prometer precisão relativa em caudas extremas; o helper de área pressupõe limites ordenados. O script é uma comparação de eventos, não um solver geral de inferência.

## Executar

Da raiz:

```sh
python3 labs/limite-central-binomial/binomial.py
python3 -B -m unittest discover -s labs/limite-central-binomial -t .
```

Seis métodos de teste: marcos dos dois eventos; 80 leis por convolução independente e momentos; seis quartos momentos da soma simétrica contra contagem de pares, E[Zₙ⁴]=3−2/n; células e probabilidade pontual; cinco integrais de densidade normal por Simpson independentes de erf/erfc; contratos. O snippet e desafio anteriores da aula foram preservados.

## Fontes — 29/10/2026

Magalhães/Lima, *Noções de Probabilidade e Estatística*, 7ª edição2010, primeira reimpressão2011/Edusp, §7.3 pp.238–239/PDF253–254. Recortes do enunciado e discussão consultados parcialmente; p.238 visualmente inspecionada. Nenhum exemplo ou histograma da fonte foi reproduzido.

Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição2006/Edusp, §6.4, Teorema6.16 e demonstração pp.338–339; recortes de aproximação/correção pp.340–341. PDF174–175 contém duas páginas impressas por scan; estas páginas foram inspecionadas visualmente. Tabela e exemplos numéricos da fonte não incorporados. Perfil, figura e testes próprios; livros privados não servidos.

Não certifica domínio pessoal, versão efetivamente ministrada de CCM0226 ou calibração de uma inferência real. É um apoio complementar da biblioteca, com revisão pessoal pendente.
