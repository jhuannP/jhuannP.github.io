# Integral de Itô: somas e informação

Notas e laboratório originais assistidos por IA para revisão pessoal. Browniano padrão W0=0, malhas determinísticas, integrandas previsíveis simples com energia média finita. O exemplo não certifica pesquisa ou domínio.

Para H_i mensurável no início, E[H_i ΔW_i]=0 e E[I²]=ΣE[H_i²]h_i. Os cruzados zeram por condicionamento no início do incremento posterior, não por suposta independência entre integranda e toda trajetória. Construção geral por aproximação fica pendente.

Para H=W: L=(W_T²−Q)/2, R=(W_T²+Q)/2 e A=(L+R)/2=W_T²/2, Q=ΣΔW². A usa média dos valores nas extremidades. Isso NÃO é o valor amostrado no instante médio da trajetória browniana na malha finita. O roteiro não generaliza a identidade trapezoidal a toda integranda. I=(W_T²−T)/2 em L² e E[(L−I)²]=Σh_i²/2; malha uniforme T²/(2n), RMSE=T/√(2n). E[I]=0 e E[I²]=T²/2. Não é alegação de convergência quase certa por consequência automática.

Fixture racional adimensional: Δw=(1/2,−1/4,3/4), w0=0. Q=7/8,final1,L1/16,A1/2,R15/16. Não é evidência de lei browniana ou tempo observado; passos temporais entram separadamente na fórmula teórica do MSE. Soma usa int/Fraction e até256incrementos; zeros finais não são informação sobre refinamento contínuo.

O modelo discreto complementar tem ξ1,ξ2 independentes±1, H0=a,H1=b+cξ1. Enumera4estados e confirma média0, segundo momento a²+b²+c². Antecipar H0=ξ1 produz média1 em ξ1²+ξ1ξ2. Incrementos são Rademacher, não normais; o cálculo finito ilustra previsibilidade/isometria e não constrói Browniano.

```
python3 -m unittest discover -s labs/ito-somas -t .
python3 labs/ito-somas/sums.py
```
Quatro testes:1875identidades de malha,fixture/erro teórico,125integrandas discretas e contraexemplo,contratos. Snippet gaussiano anterior permanece na aula; uma realização não demonstra convergência de ensemble. Unidades: se tempo em segundos, Browniano padrão tem unidade√s; WdW e Q têm unidade s. Nos números do fixture não se impõe escala física.

## Fontes consultadas parcialmente em 28/10/2026

Pavliotis, Stochastic Processes and Applications, exemplar privado autorizado: §3.2 pp.58–61/PDF71–74; definição/adaptação, convenções de avaliação, isometria e martingale (eqs.3.11–3.20). Consulta textual parcial, sem nova inspeção visual ou leitura integral. Página editorial: https://link.springer.com/book/10.1007/978-1-4939-1323-7 . PDF não servido. A fórmula de MSE e exemplos/figura/código deste roteiro são deduções próprias. Chorin–Hald cap.5 segue referência temática anterior, não relido neste bloco.

MIT18.642 Stochastic Processes II, https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec14_1.pdf : reaberto e consultado parcialmente para incrementos brownianos; busca textual por isometry sem resultado. Não foi usado como fonte da isometria; conferida em Pavliotis.

Percurso próprio complementar, não disciplina cursada nem equivalência administrativa. Pendente: espaços previsíveis gerais, extensão da integral, martingais locais e outras integrandas/convenções; revisão pessoal.
