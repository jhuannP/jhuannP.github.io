# Bayes em chances — rascunho para revisão

Pré-requisitos: condicionamento em eventos de massa positiva e partição binária. Aula `bayes-chances`, complemento próprio em Computação IV; não é um novo item oficial do programa cursado.

## Fontes e autoria

Consulta parcial em 22/10/2026 ao acervo autorizado: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª ed., §2.2, pp.54–59 (PDF 69–74), definição, produto, partições e Bayes; Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª ed., §1.3, pp.34–35 (PDF 22, páginas duplas), inversão e independência condicional. Extração textual consultada; sem declaração de leitura integral. Alguns fluxos do PDF de Noções geraram avisos de extração; fórmulas desta aula foram derivadas e verificadas independentemente. Nenhum PDF ou imagem privada foi copiado.

A apresentação em chances e os exemplos/limiares são desenvolvimento original a partir das identidades dos livros, sem atribuir este recorte específico aos autores. Não há dados de pesquisa, calibração, recomendação financeira ou prova de domínio pessoal.

## Explorar e justificar

1. Derive O(H|S)=O(H) a/b cancelando a massa do sinal. Declare p interior e a,b positivos.
2. Compare L=4 com o limiar L=9 para prior 1/10 e posterior alvo 1/2.
3. Compare sinal ausente, cópia e segundo sinal independente dentro de cada hipótese. Reutilizar taxas sem essa hipótese pode duplicar informação.
4. Use as massas nos extremos. `posterior=None` indica sinal impossível; razões têm `kind` finite/infinite/undefined para distinguir denominador zero.

O código usa int ou Fraction em [0,1], rejeita floats e bools. Frações exatas não corrigem hipóteses inadequadas. Taxas fornecidas para uma hipótese de prior zero são parâmetros do modelo, não condicionais identificadas a partir desse evento.

## Experiência de leitura

Tese visual: manter a composição editorial calma e o azul do site, com fórmulas curtas e texto em coluna legível. Sequência: pergunta inversa → derivação → exemplo → limiar → limites → prática. Preservar navegação e revelação das soluções por teclado; não acrescentar movimentos decorativos. O painel de sinais repetidos permanece na aula anterior, com seu contrato original.

## Verificar

`python3 -m unittest discover -s labs/bayes-chances -t .`

Quatro testes: enumeração de 16 átomos em 125 configurações; total/complemento/troca de hipóteses em 216 configurações; limiares por comparação direta de posteriores e atualização sequencial; contratos, massa zero e razões infinitas. Os testes apoiam a revisão conceitual, sem substituí-la.

Próxima ação pessoal: explicar por que favorecer H não equivale a torná-la majoritária e resolver os exercícios sem consultar soluções. Inferência de taxas a partir de dados e análise de sensibilidade real permanecem pendentes.


## Continuação: sensibilidade — 22/10/2026

A aula agora tem 14 seções/12 exercícios. O painel `bayesSensitivity` usa três parâmetros percentuais inteiros, controles em passos de 5%, com curva de posterior versus prior em escala 0–1 e tabela das massas. O prior selecionado só marca um ponto; não move as taxas nem simula observações. A grade da curva tem passos de um ponto percentual. Casos de massa zero são omitidos e declarados; não são preenchidos por continuidade. Com ambas as taxas zero não há curva.

O fundamento permanece Bayes nas consultas parciais aos dois livros já registradas. Derivadas e limites do retângulo são desenvolvimento original independente: D=pa+(1−p)b; derivadas ab/D², p(1−p)b/D², −p(1−p)a/D² no interior positivo. Retângulo escolhido p∈[.05,.20], a∈[.70,.90], b∈[.10,.30] dá [7/64,9/13]. Não se trata de intervalo de confiança ou credibilidade, nem de taxas estimadas a partir de dados.

Três testes Python adicionais verificam monotonicidade nas três direções, sinais, 7056 combinações do retângulo e singularidades com limites distintos do valor indefinido. `sensitivity-reference.json` contém 225 estados calculados com Fraction e usados na comparação JavaScript, incluindo extremos e taxas de 1%. O código fornecido anteriormente é preservado.

Próximo passo pessoal: prever o efeito de cada controle antes de movê-lo e justificar por que o retângulo não tem nível de confiança. Estimação e calibração a partir de dados, escolhas de prior fundamentadas e Bayes contínuo permanecem pendentes. Após este complemento, retomar o roteiro global de Física do Ensino Médio para equilibrar as disciplinas.
