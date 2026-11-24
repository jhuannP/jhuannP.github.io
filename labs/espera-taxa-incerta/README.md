# Esperar também informa — notas de aula

Extensão original de `pe-exponencial`, em rascunho para revisão de Jhuann. Pré-requisitos: condicionamento, Bayes e sobrevivência exponencial. Não é dado ou resultado de pesquisa.

Escolhemos uma classe H uma vez: lenta L ou rápida R, cada uma com probabilidade 1/2. Condicionado à classe, T é exponencial com taxa ln(2)/dia ou 2ln(2)/dia. O estado permanece fixo durante a espera; não se trata de sortear uma nova taxa a cada instante.

## Da informação à previsão

Escrevendo t como o número de dias, S_L(t)=2^(−t), S_R(t)=4^(−t). Pela probabilidade total, S(t)=[2^(−t)+4^(−t)]/2. Assim S(1)=3/8 e S(2)=5/32. A mistura das densidades integra 1, porque cada densidade de classe integra 1 e os pesos somam 1.

| Objeto | Classe lenta | Classe rápida |
|---|---:|---:|
| Peso inicial | 1/2 | 1/2 |
| Sobreviver um dia dado H | 1/2 | 1/4 |
| Massa conjunta com T>1 | 1/4 | 1/8 |
| Peso posterior dado T>1 | 2/3 | 1/3 |

Dividir as massas pela evidência 3/8 é Bayes. A nova previsão de mais um dia é (2/3)(1/2)+(1/3)(1/4)=5/12, também obtida por S(2)/S(1). É diferente de S(1)=3/8: falta de memória em cada classe não implica falta de memória na mistura. Após dois dias, os pesos são 4/5 e 1/5. Em etapas, use a sobrevivência do intervalo adicional; os eventos T>1 e T>2 são encaixados e não constituem evidências independentes.

## Taxa instantânea e tempo restante

Defina w_i(t)=p_i exp(−λ_i t)/S(t). A densidade da mistura é Σ p_i λ_i exp(−λ_i t), então h=f/S=Σw_iλ_i. Diferenciando a razão, w_i′=w_i(h−λ_i). Portanto h′=h²−Σw_iλ_i²=−Var(λ_H|T>t). Para tempos finitos e ambas as classes com peso positivo e taxas distintas, a variância é positiva e a derivada é estritamente negativa. Isso descreve seleção entre classes, sem modificar a taxa individual. A unidade de h é dia⁻¹, a de h′ é dia⁻².

A média restante é Σw_i/λ_i, por esperança condicional e falta de memória em cada classe. Inicialmente ela é 3/(4ln(2)) dias. Após um dia sem ocorrência, é 5/(6ln(2)) dias. O tempo total condicionado soma o dia já decorrido. Não confundir E[1/λ_H|T>t] com 1/E[λ_H|T>t].

Se as taxas forem iguais ou apenas uma classe tiver peso positivo, a mistura volta a uma única exponencial e recupera a falta de memória. Os parâmetros sintéticos não identificam um fenômeno físico, nem demonstram ajuste ou adequação a observações.

## Código e verificação

Execute `python3 labs/espera-taxa-incerta/mixture.py` a partir da pasta do protótipo. O código usa q_i=exp(−λ_i×1 dia) racional e tempos inteiros, não implementa tempos reais arbitrários ou ajuste de taxas. As deduções acima usam tempos reais não negativos.

Seis testes: exemplo; 525 combinações de pesos, sobrevivências e tempos confrontadas com somas de células de uma tabela conjunta de floor(T/dia), incluindo uma cauda agregada; atualizações em etapas; limites de uma única taxa; normalização e média por integração de densidades com Simpson e cauda analítica em três tempos; derivada da taxa por diferença central em quatro tempos; contratos. Quadratura e diferenças finitas são aproximações numéricas com tolerâncias declaradas; não substituem as deduções. Nenhum gerador aleatório é testado. O painel já existente na aula continua mostrando uma única exponencial.

## Referências efetivamente consultadas

Em 27/10/2026, reconferência textual parcial nos exemplares privados autorizados:

- Magalhães e Lima, **Noções de Probabilidade e Estatística**, 7ª ed., §2.2 pp.54–55 e59 (PDF69–70 e74): condicionamento, produto e Bayes; §6.2, definição6.5, pp.192–193 (PDF207–208): modelo exponencial. Símbolos de algumas equações não são recuperados integralmente pela extração.
- Magalhães, **Probabilidade e Variáveis Aleatórias**, 2ª ed., §1.3 pp.28–30 (PDF19–20); §2.4 pp.96–99 (PDF53–54), definição2.14 e proposição2.4: exponencial e falta de memória. PDF com páginas duplas e trechos intercalados na extração.

Sem leitura integral, nova inspeção visual ou distribuição dos livros. Apoiam os fundamentos; não se atribui a eles este exemplo de duas taxas, figura ou exercícios. Complemento público de nomenclatura: [Boost.Math — Hyperexponential Distribution](https://www.boost.org/latest/libs/math/doc/html/math_toolkit/dist_ref/dists/hyperexponential_dist.html), definição de mistura de exponenciais, consulta parcial em 27/10/2026. Nenhum código C++ foi instalado ou executado.

## Próxima revisão pessoal — vinte minutos

Sem abrir soluções, obtenha 3/8, 2/3 e 5/12. Explique o denominador de cada conta e por que a taxa individual constante é compatível com uma taxa agregada decrescente. Depois compare com taxas iguais. Demonstrações não comprovam domínio pessoal: revisão de Jhuann pendente.


## 27/10/2026 — condicional: o registro da ocorrência define a informação

Aula `pe-exponencial` ampliada de 20 seções/15 exercícios para 25/19, preservando a mistura anterior e seu painel de taxa conhecida. Mesmo modelo hipotético, com classe fixa, pesos iniciais iguais e taxas ln(2) e 2ln(2) por dia. Para o registro 1<T≤2, massas conjuntas 1/8 e3/32, evidência7/32 e posterior lenta4/7. Atualização em etapas: pesos após T>1 iguais a2/3 e1/3, chances de ocorrer no próximo dia1/2 e3/4; evidência condicional7/12, posterior novamente4/7. Comparação com sobrevivência T>2, posterior4/5, e versão contínua por densidades em t=2, posterior2/3. Derivado o limite de faixas pela continuidade das densidades; não se divide por probabilidade pontual zero. Não há seleção adicional de registros no modelo. Sem dados reais, estimação de taxas ou validação experimental.

Referências parcialmente reconferidas por extração textual: Magalhães e Lima, Noções de Probabilidade e Estatística,7ª ed.,§2.2 pp.54–55 e59/PDF69–70 e74,§6.2 pp.192–193/PDF207–208; Magalhães, Probabilidade e Variáveis Aleatórias,2ª ed.,§1.3 pp.28–30/PDF19–20,§2.4 pp.96–99/PDF53–54 e§3.2 pp.128–131/PDF69–70. PVA tem páginas duplas e texto intercalado; fórmulas de Noções parcialmente ausentes na extração. Sem leitura integral ou nova inspeção visual dos livros. Exemplo, cálculos, figura e exercícios originais.

Verificações: quatro testes novos em `labs/espera-taxa-incerta/observed_interval.py`, incluindo360 configurações exatas comparadas a somas de células e atualização em etapas; integração independente de densidades em quatro intervalos; aproximação por faixas decrescentes em quatro instantes; exemplos e contratos. Os seis testes anteriores da mistura continuam aprovados.14 testes de catálogo e847 estruturas MathML conferidos. Interface390px: exercício do intervalo rejeitou4/5 e aceitou4/7 pelo Enter; documento390/390px, console sem erros observados. Figura e texto inspecionados em `condicional-ocorrencia-mobile.jpg`. Revisão pessoal, Windows real e leitor de tela pendentes.

