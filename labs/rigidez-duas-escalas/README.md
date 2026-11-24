# Rigidez — duas escalas, estabilidade e precisão

Modelo diagonal u′=−u,v′=−100v,ambos iniciando1, taxas inversas à unidade de tempo escolhida. Convenção da aula λ>0 emy′=−λy, distinta do teste assinado y′=μy da referência(μ=−λ). Exemplo/código/painel/desafio/IDs re1/re2 antigos preservados.

FNC de Driscoll/Braun, consulta textual parcial em27/10/2026: §11.3 eq11.3.3–7, definição de estabilidade e fator de Euler, https://fncbook.com/absstab-diffusion/ ; §11.4 abertura sobre restrição por estabilidade versus precisão, https://fncbook.com/python/stiffness/ . Sem copiar códigos, exemplos ou figuras. Burden10 permanece referência temática, sem nova leitura neste bloco. Sistema de duas escalas, números, figura e derivações adicionais próprios.

Na raiz: `python3 labs/rigidez-duas-escalas/decay.py`. Biblioteca padrão,Fraction para taxas/passos e fatores; n inteiro0..1000. Método explícito/implícito escalar separado; não resolve sistemas gerais. Script confere fronteira−1,caso de fator0,12 combinações taxa/passo, monotonia implícita e fatores; compara erros das duas fórmulas em T1,N20/40/80 com exponencial float, razões compatíveis com ordem1. Não é prova de convergência geral nem precisão garantida para todas as escalas.

Comh0,1,modo rápido tem fator explícito−9,implícito1/11 e exato exp(−10). O implícito é estável e ainda representa mal a queda no primeiro passo. hλ=2 produz alternância limitada, sem decaimento; hλ<2 é a condição estrita. Análise fixa de longa duração não é o mesmo limite que h→0 emT fixo. Escolha de passo depende da grandeza de interesse e tolerâncias.

Próxima revisão20min: reconstruir fatores, separar fronteira/decadência e comparar com exp(−10). Sistemas acoplados, EDOs não lineares, solução iterativa por passo, fontes de perturbação e revisão pessoal pendentes. Sem dado ou resultado experimental/IC.


## 27/10/2026 — rigidez com duas escalas e precisão do transiente

`rigidez-estabilidade` ampliada de3 seções/2 exercícios para12/12. Preservados exemploλ10/h0,3,Python,desafio,painel e IDs re1/re2. Derivação dos fatores, fronteira limitada−1 versus decaimento estrito, modo zerado artificialmente e sistema diagonal de taxas1/100. h0,1 dá fatores explícitos0,9/−9 e implícitos10/11,1/11. O implícito não explode no teste, mas não resolve a queda rápida exp(−10) com precisão nesse primeiro passo. Limites de refinamentoT fixo versus longa duração, tolerâncias/custo e sistema implícito geral explicitados. Sem modificar integradores gerais nesta continuação.

Fontes públicas parcialmente consultadas em27/10/2026: Driscoll/Braun,FNC§11.3 eq11.3.3–7, https://fncbook.com/absstab-diffusion/ ;§11.4 abertura de rigidez/precisão, https://fncbook.com/python/stiffness/ . Convenção da fonteμ assinado versusλ>0 da aula distinguida. Sistema,numeração,figura e derivações adicionais próprios; sem copiar exemplos/código/tabelas. Burden10 referência temática, sem nova leitura neste bloco.

Verificação:14 testes de catálogo aprovados;833 estruturas MathML conferidas. Script racional executado com12 combinações taxa/passo, fronteiras−1/0, monotonia implícita, potências de fatores, contratos e referência. Erros no tempo1 comN20/40/80 foram comparados à exponencial float, com razões compatíveis com primeira ordem para ambos os métodos. Não é prova geral de ordem ou precisão de sistemas acoplados/não lineares. No navegador390px, exercício4 rejeitou1/11 e aceitou−9 pelo Enter; figura inspecionada em `rigidez-duas-escalas-mobile.jpg`, documento390/390px e console sem erros observados. Windows real/leitor de tela não testados; revisão pessoal pendente.

ComputaçãoIV:30 aulas próprias/217 exercícios,15 introduções curtas e dez grupos oficiais parciais. Global51 trilhas,554 aulas/4593 exercícios,182 introduções curtas. Sem curso completo ou domínio individual certificado. Próxima revisão20min: reconstruir fatores e explicar a diferença entre estabilidade e resolução da queda rápida. Próxima elaboração global: conferir introdução de CálculoI e sua fonte antes de ampliar, mantendo alternância. Saldo semanal77%; parada65% mantida.
