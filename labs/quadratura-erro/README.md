# Quadratura composta: pesos, erro e regularidade

22/10/2026. Rascunho original para revisão de Jhuann. Aula proprietária em Computação III; apoio compartilhado de MAP2220, sem duplicação de conteúdo ou totais.

## Fonte efetivamente consultada

Burden/Faires/Burden, *Análise Numérica*, tradução da 10ª edição norte-americana, terceira edição brasileira, copyright Cengage 2016. §4.4, páginas impressas 224–228/PDF 238–242, inspecionadas visualmente: composição por blocos, termos de erro e hipóteses C²/C⁴. Não foi extraído texto útil desse exemplar; leitura realizada nas imagens temporárias. Não houve leitura integral da seção ou cópia de figuras, exemplos, exercícios e algoritmos. Os integrandos, derivação de pesos, código e gráficos da aula são próprios; figuras privadas não distribuídas.

## Convenções e escopo

No laboratório exato: [0,1], malha uniforme h=1/n e n positivo par, porque calculamos as duas regras conjuntamente. Trapézios isoladamente permite n ímpar, como no exemplo Python original da aula, que permanece preservado. Simpson aqui é a regra 1/3 composta, não todas as variantes de quadratura.

Erro assinado e=regra−I; isso é o oposto de convenções que usam I−regra. Limites de módulo: |eT|≤(b−a)h²M2/12 se f∈C², |eS|≤(b−a)h⁴M4/180 se f∈C⁴ e n par. São limites de truncamento em aritmética exata. M2 e M4 são máximos dos módulos das derivadas indicadas; não se assumem sem conhecer a função.

## Dois exemplos próprios

f=x⁴: I=1/5, M2=12, M4=24, eT=1/(3n²)−1/(30n⁴), eS=2/(15n⁴). A referência integral vem da primitiva, e os termos de erro são confrontados com somas das regras. Para Simpson, o limite clássico coincide com o erro nesse caso particular. A razão de erros ao dobrar n é 16 para Simpson; a razão de trapézios tende a 4 e não é exatamente 4 em malhas finitas.

g=|x−3/10|: I=[(3/10)²+(7/10)²]/2=29/100. Não satisfaz C²/C⁴ no intervalo; não aplicamos os limites suaves do painel. S2=3/10, eS2=1/100; S4=17/60, eS4=−1/150. A mudança de sinal não contradiz o teorema, e regra uniforme não deve ser confundida com divisão em trechos adaptada à quina.

## Figura e precisão

Azul: função; tracejado preto: interpolação linear de cada trapézio; roxo pontilhado: polinômio quadrático por bloco de dois subintervalos usado em Simpson. Gráfico dos integrandos/interpolantes, não do erro. Eixos adimensionais e escalas fixas. Tabela mostra valores com nove casas e erros pequenos em notação científica; isso evita apresentar truncamento pequeno como zero visual. Não se infere precisão universal de ponto flutuante.

## Executar e verificar

Na raiz do protótipo:

```sh
python3 labs/quadratura-erro/experiment.py
python3 -m unittest discover -s labs/quadratura-erro -t .
```

`rules` exige n positivo par e função retornando int/Fraction nos nós racionais; bool/float são rejeitados. `model` aceita family 0/1 e level 1…6 inteiros, n=2^level, até 64 subintervalos. O painel JS compara as mesmas 12 combinações usando ponto flutuante.

Quatro testes: exatidão polinomial de Simpson até grau 3 e trapézios até grau 1 para 16 malhas; identidades racionais de erro em 32 malhas e razão 16 de Simpson; integral por partes e mudança de sinal na quina; contratos inválidos. JSON com 12 referências geradas pela soma de painéis locais, separada da rotina de pesos compostos, confrontado com JS. Isso verifica essas funções/malhas; não prova estimador adaptativo ou erro para qualquer integrando.

Aula 14 seções/12 exercícios, preservando os anteriores, exemplo x², Python e desafio de cúbica. Demonstração anterior mantida como apoio adicional. Refinamento, regularidade, arredondamento e referência não são intercambiáveis; controle geral de precisão e quadraturas adaptativas seguem pendentes.


## Verificação final e continuidade

777 testes Python aprovados; suíte JavaScript com 282 demonstrações/846 cenários básicos e referências adicionais aprovada; 458 estruturas MathML conferidas. No navegador, x⁴ com 64 subintervalos mostrou erro de Simpson≈7,947×10⁻⁹ sem zero visual; quina com n=2/4 mudou o sinal de +0,01 para −0,006667. Exercício aceitou 29/100; tela 390 px sem transbordamento horizontal e sem erros de console observados. Linhas de estilos distintos, viewport restaurado; prévia `quadratura-erro-mobile.jpg`.

Computação III 33 aulas/137 exercícios: 24 introduções curtas e nove recortes desenvolvidos. MAP2220 continua com uma aula própria/10 exercícios e 19 apoios, agora 13 introduções e seis recortes desenvolvidos. Catálogo geral 487 aulas/2577 exercícios. Grupos curriculares continuam parciais e revisão pessoal pendente. Próxima alternância global: cobertura de Biologia III. Saldo semanal informado após o bloco: 99%; parada em 65%.
