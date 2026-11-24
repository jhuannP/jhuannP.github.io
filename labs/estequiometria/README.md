# Estequiometria — notas originais

16/10/2026. Rascunho para revisão de Jhuann.

## Uma equação representa espécies e proporções

A escrita H₂ significa uma molécula com dois átomos de H; H₂O contém dois H e um O. O índice faz parte da identidade química. O coeficiente na frente multiplica o número de entidades daquela espécie. Alterar um índice para balancear a equação mudaria a substância representada.

## Balancear conserva os átomos de cada elemento

Na transformação formal H₂+O₂→H₂O, a contagem de O não coincide. Escreva aH₂+bO₂→cH₂O. O balanço de H dá 2a=2c e o de O dá 2b=c. Escolhendo os menores inteiros positivos, a=2, b=1 e c=2. A equação balanceada é 2H₂+O₂→2H₂O. Reações iônicas também exigem conservar carga, tema não incluído neste exemplo neutro.

## Coeficientes não são razões de massa

A proporção 2:1:2 vale para entidades e para quantidades de matéria em mol. Não significa 2 g de H₂ para 1 g de O₂. Para converter massa m em quantidade n, use n=m/M, com massa molar M em g/mol se m estiver em gramas. Declarar a entidade contada evita confundir mol de moléculas e mol de átomos.

## Um avanço comum liga todas as quantidades

Defina extensão de reação ξ, em mol. Para uma única reação, n_i=n_i,0+ν_iξ, com ν negativo para reagentes e positivo para produtos. Aqui ν=(−2,−1,+2). Se a água começa ausente, n_H₂=h−2ξ, n_O₂=o−ξ e n_H₂O=2ξ. Uma unidade de ξ consome duas unidades de H₂ e uma de O₂, mantendo as proporções.

## A não negatividade impõe um limite

Como quantidades não podem ser negativas, ξ≤h/2 e ξ≤o para avanço direto. Portanto ξ_max=min(h/2,o). Comparar quantidades iniciais sem dividir pelos coeficientes pode escolher o reagente errado. Este é um limite estequiométrico; atingir o limite requer uma hipótese adicional sobre conversão, não decorre do balanceamento.

## Reagente limitante e excesso dependem das quantidades

Com h=3 mol e o=2 mol, os limites individuais são 1,5 mol e 2 mol de extensão. H₂ limita o avanço. Em ξ=1,5 mol, formam-se 3 mol de H₂O e sobra 0,5 mol de O₂. Não sobram 0,5 mol de H₂: esse reagente foi consumido na extensão máxima.

## Uma proporção exata pode esgotar ambos

Com h=4 mol e o=2 mol, ambos os limites são 2 mol; na conversão completa ambos os reagentes chegam a zero. Não há necessidade de escolher arbitrariamente um único limitante. Se h=0, a extensão máxima é zero, ainda que haja O₂. O código informa quais reagentes ficam esgotados no limite calculado, incluindo esses casos de fronteira.

## Contar átomos antes e depois fornece uma conferência independente

No caso h=3, o=2, há inicialmente 6 mol de átomos de H e 4 mol de átomos de O. Ao final, a água contém 6 mol de H e 3 mol de O; o oxigênio restante contém 1 mol de O. A soma conserva os dois elementos. Contar mol de moléculas totais não é uma lei de conservação: o número total de entidades moleculares pode mudar.

## Massas molares aproximadas precisam ser identificadas

Para uma conta didática, adote M(H₂)=2 g/mol, M(O₂)=32 g/mol e M(H₂O)=18 g/mol. O exemplo começa com 6+64=70 g e termina com 54+16=70 g. Esses números são aproximações coerentes de massas molares, não valores precisos para qualquer composição isotópica. A conservação dos átomos é conferida exatamente por aritmética racional no laboratório.

## Conversão completa não é cinética nem equilíbrio

O modelo da tabela usa ξ=ξ_max e ignora reações paralelas. A equação balanceada sozinha não demonstra que a transformação ocorrerá, sua rapidez ou seu rendimento. Uma conversão menor pode respeitar o mesmo balanço; equilíbrio e evidências experimentais precisam de análise própria. As quantidades do exemplo são abstratas, sem montagem ou execução de reação real.

## Um laboratório computacional deve expor seus contratos

O programa aceita inteiros ou frações não negativas em mol, conserva H/O e rejeita entradas inválidas. A demonstração varia apenas quantidades iniciais e calcula o máximo estequiométrico para a equação fixa. Não analisa fórmulas químicas arbitrárias nem balanceia redox. O próximo passo é relacionar reação, evidência e equilíbrio, preservando essa distinção entre contagem e previsão.

## Resoluções

Na equação H₂+O₂→H₂O ainda não balanceada, qual o menor coeficiente inteiro positivo de H₂?

A conservação de H/O dá coeficientes 2:1:2.

Com 3 mol de H₂ e 2 mol de O₂, qual ξ_max em mol?

min(3/2,2)=3/2 mol.

Nesse exemplo, quantos mol de O₂ sobram? Aceita fração.

2−3/2=1/2 mol.

Nesse exemplo, quantos mol de H₂O se formam?

2ξ=3 mol.

Com 18 g de água e M=18 g/mol, quantos mol há?

n=m/M=18/18=1 mol.

Para balancear, pode-se alterar H₂O para outra fórmula sem mudar a espécie?

Índices definem a espécie; coeficientes multiplicam entidades.

Razão estequiométrica 2:1 significa necessariamente razão de massa 2:1?

A razão vale para entidades/mol; massas dependem de M.

A equação balanceada prova que a conversão será completa?

Conversão depende de cinética, equilíbrio e condições.

Com 4 mol de H₂ e 2 mol de O₂, ambos podem se esgotar no limite?

As quantidades estão na proporção 2:1.

## Roteiro didático e evidência

Começar distinguindo índice e coeficiente; montar balanços de cada elemento; converter massa e mol; só então calcular o mínimo de n/coeficiente. Pedir ao aluno que confira um caso de empate e explique por que a conservação de átomos não garante conversão completa. Produto de compreensão: balanço comentado com excesso e unidades. O laboratório é contabilidade computacional, sem execução de reação real.

## Fonte e pendências

Escopo: [CCM0114 no Júpiter](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0114), consulta 16/10/2026, ativação 2024 posterior à turma. Referências e diferenças de edição registradas na página do curso. Texto, problemas e código próprios, sem transcrição de livros. Pendentes: equações iônicas, redox, rendimento e equilíbrio, além dos eixos estruturais ainda não preparados.
