# Água, interações e osmose ideal

16/10/2026. Rascunho didático para revisão de Jhuann.

## Uma molécula neutra pode ser polar

A distribuição de elétrons na água é desigual: o oxigênio tem carga parcial negativa e os hidrogênios, positiva. Essas cargas parciais não tornam cada molécula um íon. A geometria molecular permite um dipolo permanente.

## Distinguir ligações ajuda a interpretar um desenho

As ligações O–H dentro da molécula são covalentes polares. Uma ligação de hidrogênio entre moléculas envolve um hidrogênio ligado a um doador e um aceitador. Desenhe esses dois tipos de conexão com convenções distintas.

## A rede de interações é dinâmica

Na água líquida, ligações de hidrogênio se formam e se desfazem. A organização coletiva contribui para propriedades do líquido. Uma imagem estática não representa uma rede rígida permanente.

## O solvente participa da organização

Íons e grupos polares interagem com a água. Regiões apolares têm comportamento diferente; sua associação pode reduzir a exposição à água. Isso ajuda a estudar membranas e proteínas, sem supor que toda substância polar tenha a mesma solubilidade.

## Osmose exige especificar uma membrana

Considere água pura e uma solução separadas por uma membrana permeável somente à água. O soluto fica retido. A pressão osmótica Π é o excesso de pressão sobre a solução necessário para manter equilíbrio osmótico. Equilíbrio significa ausência de fluxo líquido, não imobilidade molecular.

## Um primeiro modelo conta partículas de soluto

Para uma solução ideal diluída, Π=cRT, com c em mol/m³ e T em kelvin. Aqui adotamos um soluto neutro sem dissociação ou associação. A fórmula descreve equilíbrio; não calcula a velocidade da água atravessando a membrana.

## A unidade de concentração muda o cálculo

A concentração mol/L precisa ser multiplicada por 1000 antes de usar R=8,314462618 J mol⁻¹ K⁻¹. Como J/m³=Pa, Π=1000 c_L R T em pascals. Usar o número em mol/L diretamente subestima o resultado por um fator 1000.

## A proporcionalidade permite verificar a conta

No modelo, dobrar c mantendo T dobra Π; dobrar T mantendo c também dobra Π. Isso é uma comparação matemática: alterar muito T pode mudar fases, propriedades do solvente e a validade das hipóteses. Os controles usam apenas 280 a 320 K.

## A pressão compensa a tendência osmótica

Sem o excesso de pressão, o solvente tende a entrar na solução neste sistema ideal. Aplicar Π estabelece a condição de equilíbrio descrita. A fórmula não fornece o volume final: seriam necessários volumes iniciais, geometria, conservação de soluto e uma relação mecânica para a pressão.

## O exemplo torna a conversão auditável

Para c=0,010 mol/L e T=300 K, primeiro obtenha 10 mol/m³. Então Π=10×8,314462618×300=24943,387854 Pa, aproximadamente 24,9434 kPa. As casas extras ajudam a conferir o código; não expressam precisão de uma medição real.

## A ponte com equilíbrios tem limites claros

A pressão osmótica está ligada à condição de equilíbrio do solvente; não é uma contagem de ligações de hidrogênio. Soluções reais exigem atividades e podem desviar do modelo ideal. pH, protonação e tampões serão desenvolvidos em outra aula; a concentração usada aqui não é a de H⁺.

## Investigue uma previsão antes de interpretar biologia

Varie concentração e temperatura, confira proporcionalidades e unidades e escreva as hipóteses. Depois pergunte quais dados faltariam para estudar uma célula: permeabilidades, solutos presentes, volume e propriedades mecânicas. Este laboratório é computacional, sem observação de células ou preparação de soluções.

## Resoluções

Quanto vale 0,010 mol/L em mol/m³?

Multiplique por 1000: 10 mol/m³.

Para c=0,010 mol/L e T=300 K, qual Π em kPa? Use R=8,314462618 e arredonde a 4 casas.

10×R×300 Pa = 24,943387854 kPa.

Por qual fator muda Π ao dobrar c com T fixa?

Π é linear em c no modelo ideal.

Para c=0, qual Π neste modelo, em Pa?

Sem soluto, Π=0; isso não significa pressão absoluta nula.

Em quantas vezes a conta fica menor se você usar mol/L diretamente como mol/m³?

Falta o fator 1000 de conversão.

Qual conexão está dentro de uma molécula de água?

O–H intramolecular é covalente polar; não confundir com a interação entre moléculas.

Π=cRT fornece diretamente qual resultado?

Vazão e volume final precisam de outros modelos e parâmetros.

A membrana deste modelo deixa passar o soluto?

A hipótese é permeabilidade somente ao solvente.

A água ser polar significa que cada molécula possui carga total diferente de zero?

Uma molécula neutra pode ter distribuição desigual de carga e momento de dipolo.

Concentração de soluto neutro nesta conta determina o pH?

pH exige tratar atividade de H⁺ e equilíbrios ácido-base; não é a concentração total de soluto neutro.

## Fontes, roteiro e pendências

[Alberts e colaboradores, componentes químicos da célula](https://www.ncbi.nlm.nih.gov/books/NBK26883/): apoio sobre polaridade, ligações e solvente, consultado em trechos indexados em 16/10/2026; abertura direta apresentou verificação de navegador. [IUPAC, pressão osmótica O04344](https://goldbook.iupac.org/terms/view/O04344): definição e expressão ideal diluída consultadas no resultado indexado; abertura direta indisponível. Escopo: [CCM0111](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0111), mapa curricular previamente conferido em 16/10. Texto, exercícios e laboratório originais.

Pré-requisitos: moléculas, concentração, proporcionalidade e unidades. Roteiro: desenhar O–H e uma interação intermolecular com convenções distintas; explicitar membrana/soluto; prever efeito de duplicar c; calcular e comparar; apontar parâmetros ausentes para calcular vazão. Produto: conta comentada e crítica às hipóteses. Não houve medição ou experimento biológico.

Pendentes: propriedades térmicas da água, atividades e dedução termodinâmica completa, soluções não ideais, transporte com permeabilidade, ácido-base/pH/tampões e modelos específicos de células. O valor de R é arredondado no código; a exibição numérica não representa incerteza experimental.
