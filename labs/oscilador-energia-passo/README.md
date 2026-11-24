# Oscilador: estado completo, energia e passo numérico

Notas de aula originais em rascunho. Apoio à aplicação de sistemas de EDOs em ComputaçãoIV; não é uma validação de sistema físico ou domínio pessoal de Jhuann. Pré-requisitos: EDO, vetores, derivação e métodos Euler/Heun/RK4.

## Converter o modelo sem mudar o significado

De q″=−ω²q, ω>0, defina p=q′. O sistema é q′=p, p′=−ω²q. O nome p foi preservado do código anterior e representa **velocidade**, não momento canônico. Se q está em metro e t em segundo, p tem m/s eω tem s⁻¹. E=(p²+ω²q²)/2 é energia específica, em J/kg; multiplicar pela massa fornece joules. Os exemplos numéricos são normalizados, com massa1.

Para dados q₀,p₀, a referência é q=q₀cos(ωt)+(p₀/ω)sen(ωt), p=−ωq₀sen(ωt)+p₀cos(ωt). Derivação e substituição conferem a equação e o início. Diferenciar E dá E′=pp′+ω²qq′=0. Sem atrito ou força externa, conservar energia é propriedade do modelo contínuo.

Reescale u=ωq,v=p e w=(u,v). Então w′=ωJw, J=[[0,1],[−1,0]], J²=−I. A solução é uma rotação e E=||w||²/2. O passo relevante é z=ωh, adimensional.

## Três matrizes, três fatores de energia

Se um passo tiver matriz aI+bJ, seu quadrado de norma é multiplicado por a²+b², pois J é antissimétrica e JᵀJ=I. Assim:

| Método | a | b | E_(n+1)/E_n, para E_n>0 |
|---|---|---|---|
| Euler explícito | 1 | z | 1+z² |
| Heun, trapézio explícito/RK2 | 1−z²/2 | z | 1+z⁴/4 |
| RK4 clássico | 1−z²/2+z⁴/24 | z−z³/6 | 1−z⁶/72+z⁸/576 |

As identidades valem em aritmética exata para este sistema linear, não para qualquer EDO. Euler e Heun aumentam a energia em todo passo não nulo e estado não nulo. Para RK4, o fator é1−z⁶(8−z²)/576: menor que1 em0<z<√8, igual a1 na fronteira√8 e maior que1 acima dela. Isso descreve amplitude/energia; não garante fase correta ou boa precisão dentro da região estável.

Comω=h=1 e início(q,p)=(1,0), Euler dá(1,−1) e fator2; Heun dá(1/2,−1) e fator5/4; RK4 dá(13/24,−5/6) e fator569/576. Para RK4 com z=2, o fator5/9 mostra perda considerável de energia por passo, embora o método ainda não amplifique a amplitude. O gráfico compara esses fatores, sem resultados medidos.

Os estágios vetoriais devem usar estados coerentes. Aqui k₁,k₂,k₃,k₄ são **derivadas**, e h entra nas combinações; o Burden apresenta a convenção de incrementos já multiplicados por h. As formas são equivalentes quando usadas consistentemente. Atualizar uma componente e reaproveitá-la antes da outra pode mudar o método. O código anterior e seu desafio de dimensão foram preservados.

## Três verificações complementares

1. Estado: compare posição e velocidade com a referência no mesmo instante.
2. Energia: acompanhe E e seu defeito, lembrando que E correto não identifica uma solução. No instanteπ/2, a referência(0,−1) e o estado errado(0,+1) têm ambos E=1/2.
3. Refinamento: mantenha dados, equação e instante final e reduza h. Energia relativa só é definida para E₀>0; estado nulo exige erro absoluto.

Euler pode convergir em tempo final fixo apesar da amplificação a h fixo. Para T=Nh, E_N/E₀=(1+ω²h²)^(T/h). Seu logaritmo está entre0 eω²Th porque ln(1+x)≤x, logo tende a0 quando h→0 mantendo T. Já N→∞ com h fixo produz crescimento sem limite. Os dois limites são diferentes.

Se o modelo for q″+2γq′+ω²q=0, comγ≥0, a derivada física da energia é−2γp². Essa é uma equação diferente. Não se pode estimarγ apenas pela perda numérica de energia do RK4 aplicado ao modelo sem atrito.

## Laboratório e limites da evidência

Execute `python3 labs/oscilador-energia-passo/oscillator.py`. Seis testes:

- 1323 comparações racionais da energia calculada por estágios reais com o fator analítico, variando49 estados, três frequências, três passos e três métodos; inclui estado zero sem divisão por E.
- Primeiros vetores/fatores exatos, inclusive RK4 em z=2 e z=3.
- Refinamento em T=1 com8/16/32/64 passos, erro do estado reescalado; razões observadas próximas de2,4,16 para Euler/Heun/RK4. Verifica também energia acumulada de Euler por iteração direta.
- Referência de energia e exemplo de fase errada; identidade de dissipação no modelo com atrito; contratos e preservação de entrada.

As razões observadas não são prova da ordem para qualquer problema; a teoria exige hipóteses pertinentes. O código guarda traço de um sistema normalizado pequeno, com limite didático de100000 passos. Não é integrador adaptativo, detector de rigidez ou certificação em tempo longo. Não se implementou método simplético neste bloco; sua aula continua introdutória.

## Referências consultadas

- Burden, Faires e Burden, *Análise Numérica*,10ª ed., §5.9 pp.363–364/PDF377–378, inspeção visual parcial em27/10/2026 do acervo privado autorizado. Sistemas de primeira ordem, condições iniciais e extensão vetorial de RK4. A página363 começa com o fim de uma seção anterior; somente o recorte de§5.9 serve como fundamento aqui. Edição escolhida difere da7ª oficial; sem equivalência de páginas, leitura integral, cópia de exercícios ou distribuição do PDF/imagens.
- [Georgii Oblapenko, MSSD/RWTH — Lecture05, §§6.1–6.3](https://rwth-acom.pages.git.nrw/teaching/mssd/lectures/05-notes.html), consulta parcial em27/10/2026 para oscilador, energia e amplificação de Euler. Apoio público; não se copiaram os scripts ou gráficos da página. As matrizes e identidades de Heun/RK4 foram derivadas nestas notas e confrontadas por aritmética racional.
- [USP — CCM0226](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0226): mapa anterior do programa padrão preservado. Nova tentativa direta retornou timeout; não é tratada como confirmação da versão ministrada. A sondagem inicial deCCM0224 não foi usada como fonte desta disciplina. Tentativa de um PDF público de física computacional também falhou e não é contada como leitura.

Exemplos, deduções, gráfico, código e exercícios preparados para estas notas, assistidos por IA. Não são resultados da IC ou evidência de domínio pessoal.

## Próxima revisão — vinte minutos

Converta o sistema, derive E′=0 e refaça os três fatores em z=1. Explique por que o estado de energia correta pode estar errado e por que perda numérica não mede atrito físico. Registre dúvidas antes de passar à integração simplética.
