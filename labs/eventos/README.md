# Eventos: conjuntos e regra da união

13/10/2026. Conteúdo original com apoio de IA, em rascunho para revisão de Jhuann.

## Objetivos

- Definir resultados, eventos e pesos de um modelo finito.
- Calcular união, interseção, complemento e diferença.
- Justificar inclusão-exclusão por uma partição, evitando dupla contagem.
- Ler uma tabela conjunta e reconhecer limites válidos das probabilidades.

## Resultado não é o mesmo que evento

O espaço amostral Ω reúne os resultados possíveis do modelo. Um resultado é um elemento; um evento é um subconjunto. Para um dado, Ω={1,2,3,4,5,6}; o evento par é A={2,4,6}. O espaço depende do experimento: duas moedas pedem pares de resultados, não uma lista com apenas cara e coroa. Antes de contar, escreva exatamente o que cada resultado representa.

ω∈Ω; A⊆Ω

## Os pesos fazem parte do modelo

Em um modelo finito, associe a cada resultado ω um peso não negativo w(ω), com soma 1. A probabilidade de um evento é a soma dos pesos de seus elementos. A regra |A|/|Ω| só vale quando todos os resultados têm o mesmo peso. Em Ω={1,2,3}, com pesos 1/10, 2/10 e 7/10, P({1,2})=3/10, e não 2/3.

P(A)=Σω∈A w(ω); Σω∈Ω w(ω)=1

## União, interseção e complemento

A∪B ocorre quando pelo menos um dos eventos ocorre, inclusive quando ambos ocorrem. A∩B exige os dois. Aᶜ contém os resultados de Ω que não pertencem a A. A diferença A\B reúne os resultados de A fora de B. O complemento só faz sentido em relação ao espaço escolhido.

A\B=A∩Bᶜ

## Três partes disjuntas explicam a união

Divida A∪B em A\B, A∩B e B\A. Essas três partes são disjuntas. Somar P(A)+P(B) inclui A∩B duas vezes; subtrair uma cópia corrige a duplicação. A demonstração usa aditividade em partes disjuntas e não exige pesos uniformes.

P(A∪B)=P(A)+P(B)−P(A∩B)

## Complementos, diferença e monotonicidade

A e Aᶜ particionam Ω, por isso P(Aᶜ)=1−P(A). Também A é a união disjunta de A\B e A∩B, então P(A\B)=P(A)−P(A∩B). Se A⊆B, temos B=A∪(B\A), de onde P(A)≤P(B). Essas relações são úteis para conferir resultados negativos ou maiores que 1.

P(Aᶜ)=1−P(A)

## Leis de De Morgan: traduza a frase

Não ocorrer A nem B significa estar fora da união: (A∪B)ᶜ=Aᶜ∩Bᶜ. Não ocorrerem ambos significa estar fora da interseção: (A∩B)ᶜ=Aᶜ∪Bᶜ. As duas frases são distintas; desenhe ou enumere os resultados para evitar trocar uma pela outra.

(A∪B)ᶜ=Aᶜ∩Bᶜ; (A∩B)ᶜ=Aᶜ∪Bᶜ

## Uma tabela conjunta determina as marginais

Organize quatro massas: r=P(A∩B), p−r=P(A∩Bᶜ), q−r=P(Aᶜ∩B) e 1−p−q+r=P(Aᶜ∩Bᶜ), onde p=P(A) e q=P(B). As linhas somam p e 1−p; as colunas somam q e 1−q. A união é 1 menos a célula onde nenhum ocorre. Essas massas não são obrigadas a ser iguais.

P(A∪B)=1−P(Aᶜ∩Bᶜ)

## Os limites da interseção vêm de massas não negativas

As quatro células impõem r≥0, r≤p, r≤q e r≥p+q−1. Logo max(0,p+q−1)≤r≤min(p,q). Se p=q=0,8, a interseção não pode ser zero: ela precisa ter pelo menos 0,6. Na demonstração, a posição escolhida interpola entre esses limites; ela não é uma nova probabilidade de evento.

max(0,p+q−1)≤r≤min(p,q)

## Para três eventos, corrija a correção

Ao somar três marginais, cada resultado em duas partes é contado duas vezes e cada resultado na interseção tripla é contado três vezes. Subtraia as três interseções aos pares e adicione de volta a interseção tripla. Essa extensão não autoriza omitir interseções quando os eventos se sobrepõem.

P(A∪B∪C)=P(A)+P(B)+P(C)−P(A∩B)−P(A∩C)−P(B∩C)+P(A∩B∩C)

## Modelo, amostra e revisão

As contas desta aula pertencem a distribuições sintéticas. A frequência em uma amostra é outro objeto, e seu uso para estimar probabilidades exige esclarecer a coleta. Evento vazio tem probabilidade zero; a recíproca não é geral, pois um modelo pode atribuir peso zero a resultados. Conferir soma 1 não valida a escolha dos pesos para um fenômeno real.

## Exemplo resolvido

No dado justo, quanto vale “par ou pelo menos quatro”?

1. A={2,4,6} e B={4,5,6}; cada resultado tem peso 1/6.
2. A\B={2}, A∩B={4,6} e B\A={5} são disjuntos.
3. P(A)=P(B)=1/2 e P(A∩B)=1/3.
4. P(A∪B)=1/2+1/2−1/3=2/3.
5. O complemento da união é {1,3}, com probabilidade 1/3.
6. As condicionais e a independência são perguntas adicionais; a regra da união não precisa delas.

## Exercícios e resoluções

### No dado justo, A={2,4,6} e B={4,5,6}. Qual P(A∪B)?

4/6=2/3.

### A regra da união sempre pode omitir a interseção?

Sim
Não

Só quando os eventos são disjuntos.

### No mesmo dado e mesmos eventos, qual P((A∪B)ᶜ)?

Ω\(A∪B)={1,3}; 2/6=1/3.

### No mesmo dado, qual P(A\B)?

A\B={2}; probabilidade 1/6.

### Ω={1,2,3}, pesos 0,1; 0,2; 0,7. Qual P({1,2})?

Some os pesos 0,1+0,2=0,3; contagem simples não vale aqui.

### Se P(A)=P(B)=0,8, qual o menor P(A∩B) possível?

A célula fora de ambos exige 1−0,8−0,8+r≥0; logo r≥0,6.

### P(A)=P(B)=P(C)=0,4; cada interseção aos pares vale 0,15 e a tripla 0,05. Qual P(A∪B∪C)?

3×0,4−3×0,15+0,05=0,8.

### “Não ocorreu A nem B” corresponde a:

Aᶜ∩Bᶜ
Aᶜ∪Bᶜ

É o complemento da união: ambos os eventos estão ausentes.

### A regra geral da união exige equiprobabilidade?

Sim
Não

Aditividade em partes disjuntas basta; equiprobabilidade é necessária para contar por razão simples.

## Experimento e código

Baixe finite.py e execute `python3 finite.py`. Usa apenas a biblioteca padrão, probabilidades racionais e modelos finitos sintéticos. A tabela do navegador usa ponto flutuante. Não há leitura de dados privados ou escrita em arquivos.

## Proposta de condução da aula

Comece enumerando os resultados com o aluno; peça previsão antes de alterar a tabela; resolva um exercício por definição e outro por identidade; encerre com um contraexemplo. A sequência e a duração precisam de revisão didática de Jhuann.

## Hipóteses e limites

- Eventos são subconjuntos de um mesmo espaço amostral finito.
- Pesos não negativos com soma exatamente 1 no código racional.
- Contagens simples apenas no modelo uniforme.
- Tabelas são probabilidades sintéticas, sem dados observados.
