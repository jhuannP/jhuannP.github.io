# Separáveis: o intervalo pertence à solução

22/10/2026. Rascunho original assistido por IA, pendente de revisão de Jhuann. Nenhum dado ou resultado de pesquisa pessoal.

## Dois PVIs, hipóteses explícitas

Caso0: y′=2y, y(0)=y₀; fórmula y₀exp(2t), intervaloℝ. Caso1: y′=y²; fórmula y₀/(1−y₀t) no componente conectado que contém zero; se y₀=0, equilíbrio zero emℝ. Para y₀>0, intervalo(−∞,1/y₀); para y₀<0,(1/y₀,+∞).

O contrato do painel restringe consulta t/y₀ a[−2,2], sem transformar isso em limite do intervalo matemático. Valor no polo ou fora do componente do PVI retornaNone/null com motivos distintos. Não calcula o ramo do outro lado e não liga segmentos através do polo. Trechos fora da janela vertical[−6,6] são omitidos; valor finito válido permanece no relatório. No padrão y₀1/t0,5: valor2, derivada4, polo1. Em t1 não há valor finito; em t1,5 a expressão do outro intervalo não é prolongamento.

Variáveis adimensionais, modelos exatos, sem integrador, cinética física ou calibração. A prova da separação usa regra da cadeia no domínio onde a divisão faz sentido. A aula preserva o exemplo exponencial antigo, a API y(t,y0), os dois IDs de exercício e o desafio exponencial.

Um argumento por fator integrante prova unicidade no intervalo comum dos dois modelos. Isso não é teoria geral. O contraexemplo adicional y′=2√y em y≥0 tem funções com espera, verificadas diretamente; não é terceiro caso do painel.

## Fonte consultada parcialmente

Apostol, *Calculus*, VolumeI, segunda edição, Wiley1967, exemplar privado autorizado. §8.23, pp.345–346/PDF365–366 lidas; p.345 visualmente inspecionada. Localização confirmada no corpo, não presumida pelo sumário. Trecho introdutório de§8.20/pp.339–340(PDF359–360) consultado; exercícios que aparecem nas páginas vizinhas não foram usados. Não alegar leitura do capítulo inteiro, campos de direção ou teoria geral.

Redação, exemplos, curvas e exercícios próprios. Não copiados enunciados, figuras, tabelas ou soluções do livro. PDF e imagem da fonte não são distribuídos. O programa CCM0123 disponível tem ativação2025 posterior à turma2024, conforme auditoria; não confirma o conteúdo ministrado.

## Verificação

Na raiz:

```sh
python3 labs/separaveis-dominio/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes:561estados racionais contra Fraction e identidade implícita; condição inicial/derivadas locais e exponencial por outra identidade; vizinhos nextafter dos polos, zero e família com espera; domínio. Setenta estados cruzados Python/JS incluem polos, consultas no outro componente, valores negativos e zero. Diferenças finitas são verificação local, não prova de igualdade funcional. Os argumentos da aula são necessários além dos testes.

## Composição e interação

Tese visual: uma curva delimitada e um intervalo escrito tornam visível a restrição que a fórmula sozinha esconde. Plano: definição→divisão→prova→exemplos→domínio→verificação/prática. Controles alternam equação, valor inicial e consulta; polo aparece apenas quando existe; ponto de consulta desaparece quando inválido ou fora da janela. Sem animação que sugira atravessar a singularidade.

## Pendências

Revisão pessoal, fator integrante de equações lineares com coeficientes variáveis, teoria geral de existência/unicidade, métodos numéricos e demais tipos de EDO. Este recorte não conclui o grupo curricular.
