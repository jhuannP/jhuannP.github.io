# AB2 — derivadas guardadas, início e dois modos

Recorte original de Adams–Bashforth de dois passos, malha uniforme. Laboratório escalar racional com t0=0 e y1 fornecido; integrador vetorial existente mantém inícioRK4. RHS pura, sem estado dependente da contagem de chamadas. Grandezas: h é tempo, λ inverso do tempo, z=hλ adimensional.

## Fontes parcialmente consultadas —27/10/2026

Burden, Faires e Burden, *Análise Numérica*, tradução da10ª edição (3ª brasileira2016): §5.6, início pp.331–333/PDF345–347 e recortes pp.335–336/PDF349–350 inspecionados visualmente. Incluem definição multipasso, início, construção por interpolação/integração e erro; os exemplos de AB4/AB3 e a tabela5.12 não foram reproduzidos. Sumário p.xiv/PDF12 usado apenas para localização. Sem leitura integral ou distribuição dos PDFs privados.

[Driscoll/Braun, FNC §6.8](https://fncbook.com/zerostability/): critério de raízes, exemplo de Adams e teorema de convergência, consulta parcial. [FNC §11.3](https://fncbook.com/absstab-diffusion/): teste escalar e definição de estabilidade absoluta por limitação, consulta parcial. A análise específica do polinômio AB2 no eixo real e as deduções/exemplos são próprios. A primeira URL curta /absstab não abriu; a URL válida acima foi recuperada por busca e lida. Não se afirma leitura dos exercícios ou prova integral de Dahlquist.

## Correção concreta

`numerics4.adams_bashforth2` recalculava a derivada anterior. Agora a guarda, com resultados iguais para a mesma f pura. Os dois blocos completos na aula também foram atualizados. Para N passos, N+4 chamadas totais com inícioRK4:4 estágios+1 f0 armazenada+N−1 avaliações atuais. O histórico retornado usa O(N) memória; o avanço guarda uma derivada anterior. Funções com efeitos dependentes das chamadas estão fora do contrato matemático.

## Limites e verificação

`integrate` usa int/Fraction e y1 dado; N entre1 e1000, h>0. `heun_start` fornece um início opcional. `test_sequence` usa passo unitário e λ=z para estudar a recorrência, não simular um fenômeno medido. Não altera o integrador de passo variável ou implementa Adams adaptativo.

Na raiz: `python3 -m unittest discover -s labs/ab2-historia -t .` e `python3 -m unittest test_numerics4`.

Casos:0,815; solução1+t² e erro de um inícioEuler; contagem de avaliações; fronteira com forma fechada; estabilidade e crescimento; comparação independente com a rotina que recalculava; contratos. Precisão de uma malha e estabilidade não são equivalentes. Para−1<z<0 há decaimento; em z=−1 uma componente de raiz−1 pode persistir, mesmo com sequência limitada. Passo variável, rigidez geral, região complexa e revisão pessoal pendentes.

Conferência em27/10/2026:27 testes selecionados aprovados (14 catálogo+8 integrador+5 locais),812 estruturas MathML globais. Navegador390px: contagem rejeitou42 e aceitou24 pelo Enter; alternativa sobre raiz−1 aceita. Figura inspecionada, largura390px e console sem erros; captura na raiz `ab2-historia-mobile.jpg`. Saldo79%, parada65%.
