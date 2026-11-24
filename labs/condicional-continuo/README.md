# Condicionamento contínuo: faixa e densidade

22/10/2026. Rascunho próprio, pendente de revisão pessoal de Jhuann. Pré-requisitos: condicionamento em eventos positivos, densidade e integral definida. A aula `condicional-continuo` é complemento de estudo no percurso probabilístico de Computação IV, sem atribuir este recorte à ementa cursada ou a domínio comprovado.

## Referências consultadas

- Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição, §6.1, pp. 179–181 (PDF 194–196): densidade como área, normalização e probabilidade zero em valores individuais. Recorte extraído e lido parcialmente; exemplos e exercícios do livro não reproduzidos.
- Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição, §3.2, pp. 128–131 (PDF 69–70, páginas duplas): distribuição condicional, relação conjunta/marginal, interpretação por faixas e identidades integrais. Recorte lido parcialmente; o exemplo contínuo do livro não é o exemplo criado aqui.

O tratamento do limite por faixas é delimitado ao modelo abaixo, com demonstração explícita, sem afirmar convergência em todo ponto de qualquer distribuição. Uma versão da distribuição condicional é determinada apenas quase certamente sob a lei da variável condicionante; identidades integrais não identificam alterações em conjuntos nulos. O material não constitui construção geral de condicionais regulares. A convenção dos livros para condicionamento de eventos de massa zero não é substituta automática da versão por densidades. Arquivos privados e imagens dos livros permanecem fora do site.

## Modelo original

Densidade conjunta f(x,y)=2 no triângulo 0<x<y<1, zero fora. Área 1/2; massa total um. Marginal fY(y)=2y no interior. A versão escolhida para X|Y=y é uniforme em (0,y): acumulada C(a|y)=max(0,min(1,a/y)), para 0<y<1.

Faixa B=[l,u], com l=max(0,y−h), u=min(1,y+h): massa u²−l². Para 0≤a≤1, conjunta com X≤a:

- a≤l: 2a(u−l);
- l<a<u: 2au−a²−l²;
- a≥u: u²−l².

Dividir pela massa fornece a acumulada na faixa. Em y=a=1/2 e h=1/5: massa da faixa 2/5, conjunta 9/25, razão 9/10; a versão no ponto vale um, e a marginal sem informação vale 3/4. Para a=y e faixa simétrica interior, a razão é 1−h/(4y). Para a<y, h suficientemente pequeno torna a razão exatamente a/y. Assim o limite é demonstrado neste modelo. Extremos do suporte não são controles de centro no painel.

Probabilidade total recupera P(X≤a)=2a−a²: integra-se C(a|y)2y em y. Não se divide por P(Y=y), que é zero. Densidade positiva não implica massa positiva em um ponto. Densidades podem exceder um; probabilidades calculadas permanecem em [0,1].

## Implementação e verificação

Python: biblioteca padrão, `Fraction`, sem floats nos parâmetros. `inspect(y,half_width,threshold)` retorna massas, acumuladas e diferença exatas. `cdf(x,y)` calcula a versão escolhida e admite limiares fora do suporte. Parâmetros do painel: centro em décimos de 0,1 a 0,9; meia largura em centésimos de 0,01 a 0,20; limiar em décimos de 0 a 1. JavaScript calcula massas em unidades inteiras de 1/10000 antes das razões. Gráfico com faixa tracejada preta e versão no ponto em azul contínuo, em escala comum 0–1; o ponto azul marca o limiar do controle. Não são curvas estimadas ou frequências de simulação.

Quatro testes Python novos: recorte racional de polígonos e área shoelace em 396 estados, independente das fórmulas de antiderivada; limite por faixas e suporte; probabilidade total por trapézios exatos para integrando linear por partes, monotonicidade de acumuladas; contratos e faixas recortadas. `reference.json` contém esses 396 estados racionais convertidos para comparação numérica com o navegador. Testes JavaScript conferem os estados, valores das curvas, monotonicidade, normalização e contratos.

Próximo passo: revisão de Jhuann das três perguntas e uma solução própria com suporte diferente. Não há ruído de medição, densidade estimada, mistura com átomos, dado físico real ou aplicação à IC neste modelo. Densidades condicionais mais gerais, versões, Bayes contínuo e inferência seguem pendentes.
