# Relatos repetidos: informação nova ou evidência duplicada?

Rascunho didático original · 27/10/2026 · revisão pessoal pendente.

## Antes de multiplicar, descreva as observações

Queremos avaliar uma hipótese H sobre um estado fixo. Dois relatos R₁ e R₂ indicam positivo ou negativo. Um segundo texto positivo pode vir de uma nova medição, de uma cópia ou de uma fonte compartilhada. A frase “dois resultados positivos” não determina uma probabilidade sem um modelo de como eles surgem. Todos os números desta aula são sintéticos; não descrevem um aparelho, uma pessoa ou um sistema de IA real.

## A primeira atualização usa uma tabela pequena

Adote P(H)=P(Hᶜ)=1/2. Para cada relato isolado, P(+|H)=3/4 e P(+|Hᶜ)=1/4. As massas de H com positivo e Hᶜ com positivo são 3/8 e 1/8. A soma é P(+)=1/2. Assim um positivo muda a probabilidade de H de 1/2 para (3/8)/(1/2)=3/4. A taxa 3/4 não é automaticamente a probabilidade posterior: isso acontece aqui por causa da escolha simétrica do prior e das taxas.

## A regra do produto sempre conserva a informação

Sem acrescentar independência, a chance dos dois positivos dado H é P(R₁+|H) vezes P(R₂+|R₁+∩H). O segundo fator ainda sabe o primeiro relato. Para obter a evidência, faça a mesma conta sob Hᶜ e misture usando P(H) e P(Hᶜ). Não apague R₁+ do segundo fator apenas porque os relatos têm nomes diferentes.

P(R₁+∩R₂+|H)=P(R₁+|H)P(R₂+|R₁+∩H)

## Quando é legítimo multiplicar as duas taxas

No primeiro mecanismo, os relatos são independentes condicionados ao estado: a fatoração vale tanto dentro de H quanto dentro de Hᶜ. Isso autoriza usar (3/4)²=9/16 sob H e (1/4)²=1/16 sob Hᶜ. Ter apenas as duas taxas marginais não demonstra essa hipótese; precisamos de uma justificativa do mecanismo. Para dois indicadores binários, a conjunta positiva e as marginais também determinam as outras três células.

## Dois positivos independentes dado o estado

Multiplique as verossimilhanças pelos pesos anteriores: P(H∩++)=(1/2)(9/16)=9/32 e P(Hᶜ∩++)=(1/2)(1/16)=1/32. Somar dá P(++)=10/32=5/16. Dividindo a primeira massa pelo total, P(H|++)=9/10. Essa é uma inferência dentro do modelo declarado, não uma garantia de que dois relatos reais atingem 90%.

P(H|++) = 9/10

## Atualizar em duas etapas dá a mesma resposta

Depois do primeiro positivo, os novos pesos são 3/4 e 1/4. Sob independência condicional, as taxas do segundo continuam 3/4 e 1/4. As contribuições são então 9/16 e 1/16, agora relativas ao espaço já condicionado no primeiro positivo. A razão é novamente 9/10. A chance do segundo positivo dado o primeiro é 5/8, e não 1/2: (3/4)(3/4)+(1/4)(1/4)=5/8.

## Independência condicional não é independência marginal

Cada relato tem P(+)=1/2, mas a conjunta é 5/16, diferente de (1/2)(1/2)=1/4. Os relatos compartilham o estado desconhecido H. Ao receber o primeiro positivo, aumentamos o peso do estado que também torna o segundo mais provável. Portanto os relatos podem ser independentes dentro de cada estado e dependentes quando misturamos os estados. Não troque uma hipótese pela outra.

## Uma cópia não é uma segunda medição

No segundo mecanismo, R₂=R₁ sempre. As taxas de cada relato isolado continuam 3/4 sob H e 1/4 sob Hᶜ. Entretanto P(++|H)=3/4 e P(++|Hᶜ)=1/4: repetir o mesmo evento não o transforma em seu quadrado. Logo P(H|++)=3/4. Uma sequência +,− é impossível neste modelo e a razão elementar retorna indefinida, representada por None no laboratório. Isso sinaliza incompatibilidade com o modelo, não posterior zero para H.

## Um mecanismo compartilhado pode ficar oculto

No terceiro modelo, antes de produzir os relatos sorteamos um modo: metade das vezes duas observações independentes dado o estado; metade uma observação copiada. O modo é independente de H e não é revelado. As taxas de cada relato isolado permanecem iguais às anteriores, mas as conjuntas mudam. Sob H: (1/2)(9/16)+(1/2)(3/4)=21/32. Sob Hᶜ: (1/2)(1/16)+(1/2)(1/4)=5/32.

## Misture massas antes de dividir

Com prior 1/2, as massas conjuntas de H e Hᶜ com dois positivos são 21/64 e 5/64. Portanto a evidência é 26/64=13/32 e a posterior é 21/26, cerca de 80,77%. Não tire a média simples das posteriores 9/10 e 3/4: depois de ++, os modos já não têm peso igual. O modo cópia tem posterior (1/2×1/2)/(13/32)=8/13; o independente tem 5/13. A média com esses pesos, (5/13)(9/10)+(8/13)(3/4), recupera 21/26.

P(H|++) = 21/26

## Relatos opostos também conferem o modelo

No mecanismo independente, P(+−|H)=(3/4)(1/4)=3/16 e P(+−|Hᶜ)=(1/4)(3/4)=3/16. Com pesos anteriores iguais, a posterior volta a 1/2; o evento continua possível, com massa 3/16. Na mistura, apenas o modo independente pode gerar relatos opostos, e a posterior de H também é 1/2. Na cópia exata, a evidência é zero. O mesmo par de palavras exige interpretações distintas conforme o modelo.

## O que este exemplo ensina para pesquisa e IA

Dois sistemas podem reutilizar o mesmo documento, treinamento ou medição. O exemplo mostra por que não se deve multiplicar suas taxas como se fossem novas evidências independentes sem justificar a hipótese. Ele não estima a dependência de agentes reais nem fornece uma correção universal. Uma aplicação exigiria definir estado, dados, protocolo, taxas e sua incerteza. Aqui verificamos apenas as consequências exatas de três mecanismos hipotéticos.

## Sua revisão: reconstrua as oito células

Em vinte minutos, escreva as oito massas P(H ou Hᶜ, R₁, R₂) para um dos mecanismos. Confira que somam 1, recupere as marginais de cada relato e calcule a posterior após ++ e +−. Depois explique por que a cópia não adiciona informação e por que não podemos usar pesos de modo iguais depois de observar ++. Deixe o registro pessoal em branco até estudar; testes do código não comprovam domínio pessoal.

## Exercícios e resoluções

1. No modelo da aula, qual é P(H|R₁+), após apenas um positivo?

   Resolução: (3/8)/(3/8+1/8)=3/4.

2. Com independência condicional e prior 1/2, qual é a evidência P(R₁+∩R₂+)?

   Resolução: (1/2)(9/16)+(1/2)(1/16)=5/16.

3. Com relatos independentes dado cada estado, qual é P(H|++)?

   Resolução: (9/32)/(10/32)=9/10.

4. No mecanismo independente dado o estado, quanto é P(R₂+|R₁+)?

   Resolução: (3/4)(3/4)+(1/4)(1/4)=5/8.

5. Se R₂ é uma cópia exata de R₁, qual é P(H|++)?

   Resolução: A informação ++ equivale a R₁+; posterior 3/4.

6. Na mistura com metade de cada modo antes dos relatos, qual é P(H|++)?

   Resolução: As massas são 21/64 e 5/64; a razão é 21/26.

7. No modelo misto, qual a probabilidade de o modo ter sido cópia depois de ++?

   Resolução: P(cópia∩++)=(1/2)(1/2)=1/4; divida por 13/32 para obter 8/13.

8. No mecanismo independente dado o estado, quanto é P(H|+−)?

   Resolução: As duas verossimilhanças são 3/16; pesos iniciais iguais dão 1/2.

9. Independência dos relatos dentro de H e Hᶜ garante independência sem conhecer H?

   Resolução: Não: P(++)=5/16, enquanto P(R₁+)P(R₂+)=1/4.

10. O modelo de cópia exata recebe +−. Como o laboratório trata a posterior?

   Resolução: Não há massa para esse relato; não se divide por zero.

11. Na mistura, podemos obter P(H|++) pela média simples de 9/10 e 3/4?

   Resolução: Depois de ++, os modos têm pesos 5/13 e 8/13.

12. Este exemplo permite atribuir 90% de confiança a dois agentes reais que concordam?

   Resolução: As probabilidades são sintéticas; não calibram agentes reais.

## Fontes e localização da leitura

Noções de Probabilidade e Estatística, Magalhães e Lima, 7ª edição: §2.2, definição p.54 (PDF69), regra do produto p.55 (PDF70), Bayes p.59 (PDF74). Probabilidade e Variáveis Aleatórias, Magalhães, 2ª edição: §1.3, definição/produto/total pp.28–29 (PDF19), Bayes p.30 (PDF20) e independência condicional p.35 (PDF22). PDF é contado a partir de 1; PVA traz duas páginas impressas por página de PDF nesses recortes.

Reconferência textual parcial em 27/10/2026 das extrações locais dos exemplares autorizados, previamente identificados. Noções pp.54–55/59 e PVA pp.28–29/35 reconferidos neste bloco; a localização de Bayes p.30 em PVA reutiliza o registro anterior. A extração de PVA intercala colunas. Não houve nova inspeção visual dos livros nem leitura integral. Os mecanismos, números, exercício, diagrama e código são próprios; não são exercícios atribuídos aos autores. Exemplares privados não distribuídos.

## Laboratório e contratos

`reports.py` calcula verossimilhanças com Fraction. `update` retorna (evidência, posterior); a posterior é None se a evidência for zero. O prior aceita apenas int/Fraction entre 0 e 1; exclui float/bool para não introduzir aproximações ou conversões silenciosas. Estados e relatos devem ser bool. Não estima parâmetros nem aceita séries arbitrárias ou dependência desconhecida.

Execução, a partir da raiz do protótipo:

```sh
python3 labs/relatos-repetidos/reports.py
python3 -m unittest discover -s labs/relatos-repetidos -t .
```

Os testes usam sorteios uniformes primitivos em {0,1,2,3}, enumerados independentemente das fórmulas de Bayes do programa. Conferem todas as células e pares de relatos, marginais iguais, conjuntas diferentes, simetria ao trocar H/Hᶜ e os sinais, extremos do prior e contratos. A prova da fatoração depende do mecanismo descrito, não da quantidade de testes.

## Registro pessoal — preencher ao estudar

- Data:
- Mecanismo cuja tabela reconstruí:
- Como distingui a marginal da conjunta:
- Dúvida que permaneceu:

Não há validação de medições ou agentes reais; aplicação exige dados, protocolo e análise de incerteza. Nenhum domínio pessoal registrado.
