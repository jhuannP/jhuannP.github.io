# Complexação 1:1 — notas de aula

Rascunho original, 22/10/2026; revisão pessoal pendente.

## A pergunta é quanto se forma

Considere uma solução fechada a temperatura e volume constantes, com um metal hidratado M, um ligante L e apenas o complexo ML. A escrita M+L⇌ML é abreviada: moléculas de solvente deslocadas e cargas ficam omitidas, sem afirmar que as espécies reais sejam neutras. A pergunta é a distribuição entre espécies livres e ligadas após o equilíbrio. Não estamos calculando a velocidade de chegada a esse estado.

M + L ⇌ ML

## Atividade e concentração têm papéis diferentes

A constante termodinâmica é β°=aML/(aM aL), adimensional. Usando aᵢ≈[i]/c° em uma solução ideal, obtemos β°≈c°[ML]/([M][L]). Definimos Kc=[ML]/([M][L]), que tem unidade inversa de concentração. Com c°=1 mol/L, Kc=500 L/mol corresponde numericamente a β°=500 nesta aproximação. β° e Kc não são a mesma grandeza, apesar dessa igualdade numérica na unidade escolhida.

β°≈c°Kc

## Fixar os totais antes de usar a constante

Cada ML contém um metal e um ligante. Os balanços são CM=[M]+[ML] e CL=[L]+[ML]. Escreva x=[ML], dando [M]=CM−x e [L]=CL−x. A conservação exige 0≤x≤min(CM,CL). Não é válido substituir sempre as concentrações livres pelos totais: essa aproximação precisa de uma justificativa de depleção pequena.

CM=[M]+x; CL=[L]+x

## A equação de especiação

Substituindo os balanços na expressão de Kc, obtemos x=Kc(CM−x)(CL−x). Cada fator à direita representa uma concentração livre, não um estoque inicial. A expressão tem unidade de concentração porque Kc carrega sua unidade própria. Em comparação, formar o quociente com totais em lugar das espécies livres deixa de impor o equilíbrio deste sistema fechado.

x=Kc(CM−x)(CL−x)

## Por que existe uma única raiz física

Defina F(x)=Kc(CM−x)(CL−x)−x. Para CM, CL e Kc positivos, F(0)>0 e F(min(CM,CL))<0. No intervalo físico, F′(x)=−Kc[(CM−x)+(CL−x)]−1<0. A continuidade garante uma raiz e a derivada negativa garante unicidade. A outra raiz que a equação quadrática possa fornecer está fora do domínio físico. Com total zero não há complexo; Kc=0 é tratado no código apenas como limite de ligação ausente.

F′(x)=−Kc(CM+CL−2x)−1<0

## Exemplo resolvido com concentrações em milimol

Escolha CM=2 mmol/L, CL=3 mmol/L e Kc=0,5 L/mmol. São parâmetros sintéticos, sem metal identificado. A equação fica x=0,5(2−x)(3−x), se os valores das concentrações forem expressos em mmol/L. Rearranjando, x²−7x+6=0; as raízes numéricas são 1 e 6. Só x=1 mmol/L pertence ao intervalo de 0 a 2. Assim [M]=1 e [L]=2 mmol/L; a fração do metal complexada é x/CM=1/2.

x=1 mmol/L; [M]=1 mmol/L; [L]=2 mmol/L

## Conferir o quociente e os estoques

No exemplo, x/[(CM−x)(CL−x)]=1/(1×2)=0,5 L/mmol. Os estoques fecham: 1+1=2 para metal e 2+1=3 para ligante. A raiz 6 produziria concentrações livres −4 e −3 mmol/L; mesmo que satisfaça o polinômio, não descreve uma solução física. Conferir apenas o resíduo algébrico não basta.



## Trocar de unidade muda o número de Kc

Como 1 mmol/L=0,001 mol/L, o mesmo exemplo usa CM=0,002 mol/L, CL=0,003 mol/L e Kc=500 L/mol. A concentração de ML é 0,001 mol/L, o mesmo estado físico. Manter o número 0,5 enquanto troca apenas as concentrações mudaria o modelo. Já β° continua adimensional e usa o estado padrão declarado.

0,5 L/mmol = 500 L/mol

## Quando podemos tratar o ligante como reservatório

Se x for pequeno em comparação com CL, podemos aproximar [L]≈CL. Então x≈CM Kc CL/(1+Kc CL). No exemplo, isso daria x≈1,2 mmol/L, 20% acima do valor correto 1 mmol/L. Aqui o consumo de ligante não é desprezível: 1 dos 3 mmol/L está ligado. Ter mais ligante total que metal total, por si só, não garante precisão. O critério relevante é comparar o ligante consumido com seu estoque.

x≈CM Kc CL/(1+Kc CL), somente se x≪CL

## A constante não muda quando adicionamos ligante

Dentro deste modelo ideal a temperatura fixa, aumentar CL mantendo CM e Kc aumenta a raiz física e a fração complexada. Isso altera a composição, não a constante de equilíbrio. Mesmo Kc grande não elimina o limite x≤CL: com ligante insuficiente, nem todo metal pode formar ML. Em soluções reais, mudança de força iônica, pH ou solvente pode alterar a relação por concentrações; esse efeito não está modelado aqui.



## Estabilidade termodinâmica não é inércia cinética

A constante compara estados de equilíbrio. Um complexo favorecido no equilíbrio pode trocar ligantes rapidamente; outro pode reagir lentamente mesmo quando uma transformação é termodinamicamente favorável. As palavras lábil e inerte se referem à cinética. Este laboratório não fornece mecanismo, barreira, tempo de relaxação ou constante de velocidade. Também não infere energia de uma ligação isolada diretamente de Kc.



## Resolver por intervalos preserva a raiz física

O código começa com o intervalo [0,min(CM,CL)] e calcula F no ponto médio. Se F>0, a raiz está à direita; se F<0, está à esquerda. A cada passo o intervalo se reduz pela metade. Frações racionais evitam arredondamento nos sinais para as entradas aceitas. O resultado devolve limites e o ponto médio, não uma alegação de raiz racional exata. A biblioteca padrão basta; o método também conecta esta aula a análise numérica.



## O que o sistema reduzido deixa de fora

Não há ML₂, polinucleares, protonação do ligante, hidrólise do metal, precipitação, competição de outros ligantes ou coeficientes de atividade. Ele também não determina geometria, spin, espectro, quelato, solvatação ou potencial redox. Para íons reais, são necessários balanço de carga e equilíbrios adicionais; aqui as cargas e contraíons são implicitamente externos ao recorte. Resultados não devem ser atribuídos a um complexo real sem essa ampliação.



## O que demonstrar na revisão pessoal

Reconstrua a equação a partir dos balanços, recuse a raiz fora do intervalo, converta unidades e avalie o erro de excesso de ligante antes de aceitar uma aproximação. O arquivo Python pode ser usado para variar os totais e comparar intervalos. A aula é rascunho assistido por IA; só a revisão, explicação e execução pessoal poderão se tornar evidência de competência no portfólio.



## Exercícios e resoluções

- No exemplo CM=2 mmol/L, CL=3 mmol/L e Kc=0,5 L/mmol, qual é [ML] em mmol/L? **Resolução:** As raízes são 1 e 6; apenas 1 está em [0,2].
- No mesmo exemplo, quanto é [M] livre em mmol/L? **Resolução:** CM−x=2−1=1.
- No mesmo exemplo, quanto é [L] livre em mmol/L? **Resolução:** CL−x=3−1=2.
- Qual é a fração de metal complexada no mesmo exemplo? **Resolução:** x/CM=1/2.
- Quanto é 0,5 L/mmol expresso em L/mol? **Resolução:** Há 1000 mmol por mol; o valor é 500 L/mol.
- Se CM=2 e CL=0,3 mmol/L, qual é o limite superior estequiométrico de [ML], em mmol/L? **Resolução:** Cada ML consome um L; x≤min(2,0,3)=0,3.
- No exemplo principal, qual [ML] em mmol/L a aproximação [L]≈CL fornece? **Resolução:** 2×0,5×3/(1+0,5×3)=1,2.
- No exemplo principal, qual é o erro relativo da aproximação 1,2 em relação ao valor correto 1? **Resolução:** (1,2−1)/1=0,2, isto é, 20%.
- A raiz 6 do exemplo deve ser aceita por zerar o polinômio? **Resolução:** Ela viola os estoques e produz concentrações livres negativas.
- Uma constante de formação grande determina uma reação rápida? **Resolução:** Equilíbrio e cinética são perguntas diferentes.
- A constante termodinâmica β° tem unidade L/mol? **Resolução:** β° é formada por atividades adimensionais; Kc carrega a unidade inversa de concentração.
- Adicionar ligante, sem mudar temperatura nem as hipóteses ideais, exige mudar Kc? **Resolução:** Muda a composição de equilíbrio, mantendo a constante do modelo.

## Fontes e reprodução

Miessler, Fischer e Tarr, Química Inorgânica, quinta edição brasileira Pearson 2014, §10.1.1, p.349/PDF364, leitura textual parcial sobre constantes de formação. Não se usaram os metais, valores, tabelas ou figuras da obra no exemplo. As atividades, unidades explícitas, balanços, prova de raiz única e algoritmo são desenvolvimento didático próprio. Programa CCM0214: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214, consulta em 22/10/2026, ativação exibida 15/07/2024; a extração web informa captura de dois meses antes, não é evidência da versão efetivamente ministrada.

Execute na raiz do site: python3 -m labs.complexacao-um-um.experiment e python3 -m unittest discover -s labs/complexacao-um-um -t . . Apenas biblioteca padrão. Entradas em mmol/L e L/mmol; mudar conjuntamente as unidades, como nos testes, mantém o estado físico. Intervalo após 80 passos tem largura no máximo min(CM,CL)/2^80; ponto médio não é proclamado exato. Para compartilhar o laboratório, conserve a pasta e a estrutura de módulos.

Próxima revisão pessoal: obter x=1 mmol/L sem olhar, testar os dois estoques e explicar por que 1,2 mmol/L é uma aproximação inadequada para esse exemplo. Revisão do material da turma e atividades reais pendentes.

Navegador: resposta 1/2 aceita na questão 4; diagrama carregado e inspecionado a 390 px, sem transbordamento horizontal observado. Prévia complexacao-um-um-mobile.jpg. Catálogo atual: 498 aulas/2884 exercícios em rascunho. Saldo semanal 95%; parada operacional em 65%.
