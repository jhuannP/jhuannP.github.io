# Condicionamento contínuo — faixa, densidade e versão

27/10/2026. Notas de aula originais com apoio de IA, em rascunho. Revisão pessoal de Jhuann pendente. Trilha complementar; não é uma disciplina formal concluída nem prova de domínio.

## Pergunta e hipóteses

Variáveis adimensionais X,Y; densidade conjunta conhecida f(x,y)=(6/5)(x²+y) no quadrado unitário, zero fora. Não foi estimada de dados. Pré-requisitos: condicionamento por eventos, densidades e integral definida. A aula oferece texto, exemplo resolvido, 16 exercícios e figura original; Python é opcional para estudar as contas.

A massa total é (6/5)(1/3+1/2)=1. Marginais:

- fX(x)=(6/5)(x²+1/2), 0≤x≤1;
- fY(y)=(6/5)(1/3+y), 0≤y≤1;
- zero fora dos respectivos intervalos.

Uma versão contínua da condicional é fY|X(y|x)=(x²+y)/(x²+1/2), 0≤y≤1, para x no intervalo. Ela integra 1. O valor de uma densidade não é a probabilidade de um ponto. A conjunta tem altura máxima 12/5 e massa total 1; P(X=x)=0 mesmo com fX(x)>0.

Para t entre 0 e 1:

P(Y>t|X=x)=[x²(1−t)+(1−t²)/2]/[x²+1/2].

A acumulada entre 0 e 1 é [x²t+t²/2]/[x²+1/2]; prolongar com 0 e 1 fora. A razão usa densidades, nunca a divisão por P(X=x)=0. As condicionais são determinadas apenas a menos de conjuntos de peso marginal zero: alterar um único x não muda a conjunta. Usamos explicitamente a versão contínua, incluindo a extensão aos extremos; não uma atribuição universal para qualquer evento nulo.

## Faixa de largura positiva

P(a≤X≤b,c≤Y≤d)=(6/5){[(b³−a³)/3](d−c)+(b−a)(d²−c²)/2}.

A probabilidade condicionada à faixa é essa massa dividida pela mesma expressão com c=0,d=1, desde que a<b. Faixa degenerada tem massa zero e `band_interval` retorna `None`, inclusive se o numerador for zero. Isso não retorna uma posterior zero e não implementa a convenção de atribuição arbitrária para eventos nulos citada nos livros.

Em x₀=1/2 e meia largura 0<h≤1/2, a média de x² na integral em dx é 1/4+h²/3. Logo a cauda acima de 1/2 na faixa centrada é

p(h)=(1/2+h²/6)/(3/4+h²/3).

A diferença exata até 2/3 é (h²/18)/(3/4+h²/3)>0, tendendo a zero. A expressão simplificada admite extensão em h=0, mas a razão original de eventos não admite divisão 0/0. O limite é justificado aqui pela continuidade e pela marginal positiva, não afirmado para toda distribuição.

| Informação sobre X | P(Y>1/2 | informação) |
|---|---|
| Nenhuma, faixa completa | 13/20 |
| [1/4,3/4], h=1/4 | 49/74 |
| [3/8,5/8], h=1/8 | 193/290 |
| X=1/2, versão contínua escolhida | 2/3 |

Para a faixa [1/4,3/4], massa de X=37/80 e conjunta com Y>1/2=49/160; o quociente é 49/74. A faixa representa observação ideal de intervalo, não intervalo de confiança. Ruído de medida exige um modelo próprio.

A lei da probabilidade total usa o peso fX(x)dx. O integrando para a cauda é (6/5)(x²/2+3/8); sua integral recupera 13/20. Não é média uniforme das condicionais. As caudas condicionais variam continuamente com x, de 3/4 a 7/12, estabelecendo dependência neste exemplo; não causalidade.

## Fontes e alcance da consulta

Reconferência textual parcial em 27/10/2026 nas extrações dos exemplares privados autorizados:

- Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, pp.54–55 (PDF69–70): razão por eventos, restrição e produto.
- Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §3.2, pp.128–133 (PDF69–71, páginas duplas): definição3.6, razão por densidades, interpretação por faixas, mistura e independência.

A extração de PVA intercala colunas. Não houve nova conferência visual nem leitura integral desses capítulos. Usamos fundamentos das fontes; a densidade polinomial, integrais específicas, números, figura, exercícios e código são próprios. Não se reproduzem exemplos ou exercícios dos livros; PDFs privados não distribuídos. A escolha de uma versão por densidades é distinguida da convenção arbitrária de probabilidade em evento nulo nos textos.

## Exercícios e conferência

1. k=6/5: integral sem k é5/6.
2. fX(1/2)=9/10, uma altura.
3. P(X=1/2)=0, uma massa.
4. Cauda marginal13/20.
5. Cauda na versão em x=1/2:2/3.
6. Massa da faixa [1/4,3/4]:37/80.
7. Cauda nessa faixa49/74.
8. Cauda na faixa [3/8,5/8]:193/290.
9. P(Y=1/2|X=1/2)=0 na versão adotada.
10. Probabilidade total integra com fX(x)dx.
11. Faixa degenerada:None; função pontual usa outra construção.
12. Versões podem diferir em conjunto de peso marginal zero.

## Laboratório e limites

`density.py` usa apenas Python padrão e Fraction. Entradas `int` ou `Fraction`, sem bool ou float. Os intervalos precisam estar ordenados dentro de [0,1]. Retângulos degenerados retornam massa zero; faixa condicionante degenerada retorna None. A função pontual só aceita x no suporte e representa a versão escolhida; fora dele gera erro. `joint` e `marginal_x` retornam zero fora do suporte.

Rodar da raiz do protótipo:

```sh
python3 -m unittest discover -s labs/condicional-continua -t .
```

Cinco testes iniciais cobrem: 225 retângulos contra quadratura numérica separada das primitivas; normalização, partições e probabilidade total; limites das faixas e identidade exata do erro; densidade versus massa e dependência; contratos. A quadratura é uma verificação numérica para este polinômio, não prova geral. Os testes não validam observações reais, ruído instrumental ou aprendizagem.

## Próxima revisão pessoal

Dois blocos sugeridos de20min: primeiro normalização e marginais; depois faixa, versão e limite. Registro de dúvidas e compreensão deixado em branco. Pendentes: distribuições com suporte não retangular, modelos mistos/singulares, condicionamento formal mais geral e inferência de densidades a partir de dados. Não ampliar esses assuntos antes de revisar os denominadores desta aula.

## Extensão: Bayes ao observar um evento em Y — 27/10/2026

Cinco seções e quatro exercícios adicionados à mesma aula (19 seções/16 exercícios). As 14 seções e os 12 exercícios anteriores permanecem. Apoio: mesmos trechos de Magalhães e Lima, Noções 7ª ed. §2.2 pp.54–55/PDF69–70, e Magalhães, PVA 2ª ed. §3.2 pp.128–133/PDF69–71. Reconferência textual parcial; a definição3.6 p.128/PDF69 trata explicitamente X condicionado em um evento de Y de massa positiva. Nenhum capítulo integral foi lido ou copiado. Deduções, números e exercícios abaixo são próprios.

A observação é A={Y>1/2}, não o valor Y=1/2. Sua massa é13/20. Integrar a conjunta apenas em A dá g(x)=(6/5)(x²/2+3/8). Para qualquer intervalo I, P(X∈I,A)=∫I g(x)dx; dividir por13/20 identifica fX|A(x)=(12x²+9)/13 no suporte, zero fora. Integral(4+9)/13=1. O fator de normalização20/13 é maior que1 porque não é uma probabilidade. A verossimilhança L(x)=P(A|X=x) também não é densidade em x.

B={X≤1/2} tem massa7/20. A interseção com A tem massa1/4. Logo P(A|B)=5/7, P(B|A)=5/13. Bayes em eventos fornece (5/7)(7/20)/(13/20)=5/13, e a integral da posterior fornece o mesmo resultado. Não inverter condicionais preservando o denominador.

Média anterior: (6/5)∫(x³+x/2)dx=3/5. Média posterior: ∫x(12x²+9)/13 dx=15/26. Diferença−3/130. Ambas as densidades são crescentes, mas a chance de A decresce com x, favorecendo relativamente valores menores. Não é efeito causal de observar Y sobre X.

Resoluções dos novos exercícios13–16: fator20/13; prior7/20; posterior5/13; média15/26. Proposta de revisão20min: reconstruir as três razões e as duas integrais antes de usar código; dúvidas e avaliação pessoal permanecem em branco.

Novas funções `posterior_x_density(x,c,d)` e `posterior_x_interval(a,b,c,d)` condicionam no evento c≤Y≤d. Intervalo condicionante degenerado retorna None; densidade retorna zero fora do suporte apenas quando a condição tem massa positiva. Contratos de entradas racionais e intervalos são mantidos. Não são estimadores nem ferramentas para qualquer distribuição.

Quatro testes novos em `test_bayes.py`:150 combinações de intervalos comparadas à quadratura racional aninhada independente das primitivas; normalização; fatoração de Bayes em pontos e eventos; médias e atualização específica; contratos, faixa nula e observação de todo o suporte. Quadratura de Simpson é exata aqui para os polinômios até grau3, não uma garantia para funções gerais. Nove testes locais e14 de catálogo aprovados;694 estruturas MathML conferidas. No navegador390px, exercício15 rejeitou5/7 e aceitou5/13 pelo Enter; documento390px sem transbordamento horizontal. Revisão pessoal e teste com leitor de tela/Windows real não realizados.
