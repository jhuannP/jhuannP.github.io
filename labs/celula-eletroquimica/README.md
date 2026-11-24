# Célula eletroquímica: meia-reações, Gibbs e Nernst

Rascunho didático original · 27/10/2026 · revisão pessoal pendente.

## Uma reação pode transferir energia por um circuito

Em uma reação de oxirredução, uma espécie perde elétrons e outra os recebe. Separar os dois processos em compartimentos, conectando eletrodos por um circuito e mantendo transporte iônico entre as soluções, permite transferir energia elétrica ao meio. A célula não cria energia: converte parte da diminuição de energia de Gibbs da reação em trabalho. Neste primeiro recorte usamos uma célula reversível idealizada; não calculamos corrente, velocidade ou potência.

## Meia-reações: conservar átomos e carga

Considere os metais hipotéticos M e N. Na direção escolhida, M(s)→M²⁺(aq)+2e⁻ é oxidação, e N²⁺(aq)+2e⁻→N(s) é redução. Somar elimina os dois elétrons: M(s)+N²⁺(aq)→M²⁺(aq)+N(s). Há um átomo de cada metal em cada lado e carga total +2 em ambos. O número eletrônico n=2 é positivo e adimensional para a reação tal como escrita; por mol de avanço, a carga transferida tem magnitude nF. M e N são rótulos de um modelo, sem tabela de uma substância real.

## Ânodo e cátodo são definidos pelo processo

Oxidação ocorre no ânodo; redução no cátodo. Esses nomes não dependem do sinal elétrico. Na descarga galvânica desenhada, o ânodo é negativo e o cátodo positivo, e os elétrons no circuito externo vão do ânodo ao cátodo. A corrente convencional nesse circuito tem sentido oposto ao dos elétrons. Na operação eletrolítica, uma fonte externa sustenta uma direção não espontânea, e os sinais dos eletrodos diferem do caso galvânico; não memorize “ânodo negativo” como definição geral.

## A ponte salina transporta íons, não elétrons

No compartimento de M, a oxidação aumenta a quantidade de cátions metálicos; ânions do eletrólito podem compensar essa carga. No de N, a redução consome cátions; cátions do eletrólito podem compensar a carga que resta. Essa descrição pressupõe eletrólito compatível, sem reação relevante com as espécies. Elétrons percorrem o circuito metálico; o transporte nas soluções é iônico. Uma ponte real pode introduzir potencial de junção e outras limitações que omitimos no modelo.

## Força eletromotriz tem unidade de tensão

A força eletromotriz, FEM, é uma diferença de potencial no limite de corrente zero, em volts: 1 V=1 J/C. Apesar do nome, não é força mecânica em newtons. Em uma célula reversível, essa FEM se relaciona ao trabalho elétrico máximo. A tensão nos terminais sob carga pode diferir por resistência interna, polarização e transporte. Portanto não use a equação termodinâmica para prever diretamente a tensão e a potência de uma bateria em uso.

## Potenciais de redução compartilham uma referência

Um potencial de eletrodo é referido a outro eletrodo, por convenção; valores tabulados usuais são potenciais de redução. Para a reação de descarga escolhida, E°célula=E°redução,cátodo−E°redução,ânodo. Defina dados sintéticos E°redução,N=+0,20 V e E°redução,M=−0,40 V: resulta E°=+0,60 V. Não mude o sinal duas vezes: usando dois potenciais de redução, faça a subtração. Nenhum desses números é medição atribuída a um metal real.

E° = 0,20 − (−0,40) = 0,60 V

## Gibbs por mol de avanço, tensão por carga

A temperatura e pressão fixas, a energia de Gibbs de reação ΔᵣG é dada por mol de avanço da reação. Na conversão reversível ideal, ΔᵣG=−nFE. O sinal negativo indica que uma direção com E>0 tem ΔᵣG<0 e pode fornecer trabalho; a quantidade máxima de trabalho elétrico entregue por mol de avanço é nFE. Em um avanço finito, E pode variar com a composição, e o trabalho total requer integrar nF E dξ: não mantenha a tensão inicial constante sem justificar.

ΔᵣG = −nFE

## Dobrar a reação não dobra a tensão

Ao multiplicar todos os coeficientes por 2, n passa de 2 para 4 e ΔᵣG também dobra. Como E=−ΔᵣG/(nF), a tensão permanece a mesma. Potenciais não são somados ou multiplicados como energias extensivas. Inverter a reação muda o sinal de ΔᵣG e de E, mantendo n como magnitude positiva do número eletrônico. Identifique a direção da reação antes de interpretar espontaneidade.

## As atividades formam um quociente sem unidade

Para a reação M+N²⁺→M²⁺+N, Q=a(M²⁺)/a(N²⁺) quando os metais são sólidos puros nas fases consideradas, com atividade 1. Q não contém elétrons livres, que se cancelam na reação química. Atividades são adimensionais e dependem da referência. Substituir atividade por concentração dividida por uma concentração padrão é uma aproximação ideal, que exige hipótese de diluição e coeficientes de atividade adequados. Um sólido em liga não recebe automaticamente atividade 1.

Q = a(M²⁺)/a(N²⁺)

## Derivar Nernst fixa os sinais

Parta de ΔᵣG=ΔᵣG°+RT ln Q e substitua ΔᵣG=−nFE e ΔᵣG°=−nFE°. Dividir por −nF fornece E=E°−(RT/nF)ln Q. R é a constante dos gases em J/(mol·K), T a temperatura absoluta em K e F a constante de Faraday em C/mol. O logaritmo é natural. Se usar logaritmo decimal, aparece o fator ln 10; o coeficiente numérico depende de T e de n, não é universal.

E = E° − (RT/nF) ln Q

## Exemplo resolvido fora do estado padrão

Use E°=0,60 V, n=2, T=300 K, R=8,314462618 J/(mol·K) e F=96485,33212 C/mol como constantes arredondadas. Escolha atividades sintéticas a(M²⁺)=0,10 e a(N²⁺)=0,001: Q=100 e ln Q≈4,60517. A correção (RT/2F)ln 100 é aproximadamente 0,05953 V; portanto E≈0,54047 V e ΔᵣG≈−104,30 kJ/mol de avanço. Aumentar a atividade do produto relativamente ao reagente diminui a força motriz para a reação escolhida. Os valores não são dados de uma solução experimental.

## Equilíbrio químico da reação não é apenas circuito aberto

No equilíbrio químico da reação global, ΔᵣG=0 e Q=K, portanto E=0. Das relações padrão vem ln K=nFE°/(RT). Entretanto uma célula reversível em circuito aberto pode ter equilíbrios eletroquímicos nas interfaces e E não nulo: a ausência de caminho externo para os elétrons impede o avanço macroscópico. Assim “não passa corrente” não prova Q=K. O laboratório retorna ln K, evitando gerar K por exponenciação quando o número é muito grande.

ln K = nFE°/(RT)

## Padrão não significa sempre 298 kelvin

O sobrescrito ° indica uma escolha de estados padrão, à temperatura declarada. Não fixa T em 298 K. E° geralmente varia com a temperatura; o exemplo fornece E° em 300 K. Alterar T no programa mantendo E° fixo é um cenário paramétrico com esse valor fornecido, não uma previsão térmica de uma célula real. A escala de atividade e a temperatura devem acompanhar qualquer dado tabulado.

## O que o código confere e o que permanece fora

O laboratório recebe E°, n, T e ln Q. Para a reação M/N, uma função calcula ln Q como ln a(M²⁺)−ln a(N²⁺), evitando formar uma razão que pode estourar a faixa numérica. Os testes usam uma rota independente por ΔᵣG químico com Decimal, inversão e reescala de reação, sinal perto de Q=K e contratos. O cálculo não faz balanceamento automático, não estima atividades, não descreve eletrodos reais nem prevê corrente, corrosão, sobrepotencial ou rendimento.

## Uma revisão de vinte minutos

Escreva as duas meia-reações, confira átomos e carga, derive Nernst a partir de Gibbs e explique por que multiplicar a reação mantém E. Refaça a conta para Q=1 e Q=100, identificando unidades e direção. Por fim, explique como uma célula pode ter tensão em circuito aberto. Esta primeira aula muda a lacuna para cobertura parcial; tipos de eletrodos, eletrólise quantitativa, junções e aplicações experimentais continuam pendentes. Revisão pessoal de Jhuann não foi realizada pelo agente.

## Exercícios e resoluções

1. Quantos elétrons são transferidos na reação M+N²⁺→M²⁺+N, como escrita?

   Resolução: M perde dois elétrons e N²⁺ recebe dois; n=2.

2. Com potenciais de redução N=+0,20 V e M=−0,40 V, qual E° da direção M+N²⁺→M²⁺+N, em V?

   Resolução: 0,20−(−0,40)=0,60 V.

3. Para atividades a(M²⁺)=0,10 e a(N²⁺)=0,001, quanto vale Q?

   Resolução: 0,10/0,001=100, adimensional.

4. Com E°=0,60 V, n=2, T=300 K e Q=100, qual E em volts? Use R=8,314462618 e F=96485,33212.

   Resolução: E=0,60−(RT/2F)ln 100≈0,54047 V.

5. Com E=0,60 V, n=2 e F=96485,33212 C/mol, quanto é ΔᵣG em kJ/mol de avanço?

   Resolução: −2×96485,33212×0,60/1000≈−115,7824 kJ/mol.

6. Se a reação e seu n forem multiplicados por 2, qual será E° em volts, partindo de E°=0,60 V?

   Resolução: ΔᵣG° e n dobram; a razão E° permanece 0,60 V.

7. No equilíbrio químico da reação global, quanto vale E em volts?

   Resolução: Q=K e ΔᵣG=0; logo E=0.

8. Qual processo define o ânodo?

   Resolução: Ânodo é o eletrodo onde ocorre oxidação, independentemente do sinal.

9. Quem transporta carga no eletrólito da ponte salina deste modelo?

   Resolução: O circuito metálico transporta elétrons; a ponte transporta íons.

10. Uma corrente externa zero prova que Q=K para a reação química global?

   Resolução: O circuito aberto pode impedir avanço macroscópico mesmo com FEM não nula.

11. O sobrescrito padrão em E° obriga T=298 K?

   Resolução: O estado padrão é definido à temperatura declarada; E° pode variar com T.

12. Este modelo termodinâmico prevê a corrente de descarga da célula?

   Resolução: Faltam cinética, transporte, resistência e circuito.

## Fontes e limites da consulta

Programa CCM0124, item 7: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0124 . Reconferido em 27/10/2026; ativação 01/01/2025, posterior à turma de 2024/1. Versão ministrada não recuperada.

Levine, Physical Chemistry, sexta edição, 2009, exemplar privado autorizado: §13.4 pp.403–404/PDF421–422 e §13.6 pp.412–414/PDF430–432, leitura textual parcial em 27/10. P.414/PDF432 renderizada e inspecionada visualmente: equações 13.40–13.44, sinais e distinção entre equilíbrio eletroquímico e químico. Extração omite símbolos; imagem usada para conferir relações. Página PDF contada a partir de 1. Nome do arquivo indica 2008, mas páginas editoriais previamente conferidas indicam 2009. Sem leitura integral ou distribuição do livro.

Apoios públicos, consulta parcial em 27/10/2026:
- https://openstax.org/books/chemistry-2e/pages/17-2-galvanic-cells — organização das meia-células e caminhos da carga.
- https://openstax.org/books/chemistry-2e/pages/17-3-electrode-and-cell-potentials — referência de redução e diferença de potenciais. Não se adotou a simplificação de estado padrão como temperatura obrigatória de 298 K ou atividade universalmente igual à concentração 1 M.
- https://openstax.org/books/chemistry-2e/pages/17-4-potential-free-energy-and-equilibrium — relações entre Gibbs, potencial e equilíbrio.

M/N, potenciais, atividades, exercícios, figura e código são um modelo original hipotético. Não são dados de substâncias reais nem gabarito de exercício dos autores. Constantes R=8,314462618 e F=96485,33212 são entradas arredondadas declaradas; nenhuma precisão experimental reivindicada.

## Laboratório

`cell.py` recebe ln Q, evitando razões e exponenciações desnecessárias. A função auxiliar `log_quotient` vale especificamente para M+N²⁺→M²⁺+N com sólidos puros. A função geral `state` pressupõe reação balanceada; não confere n ou estequiometria contra uma fórmula química. Retorna E em V, ΔᵣG em J/mol e ln K. T em K deve ser positiva; n inteiro positivo, sem bool; atividades positivas e finitas. Não calcula potenciais de junção, corrente, cinética, sobrepotencial, queda ôhmica ou incerteza.

```sh
python3 labs/celula-eletroquimica/cell.py
python3 -m unittest discover -s labs/celula-eletroquimica -t .
```

Testes usam rota química independente por ΔᵣG°+RT ln Q com Decimal e logaritmo de alta precisão, além de inversão e reescala da reação, equilíbrio, sinais, atividades extremas sem formar a razão e contratos. Não validam um dispositivo real.

## Registro pessoal — preencher ao estudar

- Data:
- Como conferi os sinais:
- Como interpretei circuito aberto:
- Dúvida sobre atividades ou unidades:

Primeiro recorte parcial. Eletrodos de referência em detalhe, eletrólise quantitativa, junções, células de concentração e aplicações experimentais permanecem pendentes. Nenhum domínio pessoal certificado.
