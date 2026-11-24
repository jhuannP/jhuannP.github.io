# RMN de¹H: posição e área são perguntas distintas

Notas originais assistidas por IA em rascunho para revisão de Jhuann. Os dados e retângulos são artificiais, sem molécula atribuída, aquisição de RMN, experiência experimental ou certificação de domínio.

## Fontes e correspondência curricular —26/10/2026

O [programa CCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214), ativação publicada15/07/2024, inclui no item4 fundamentos de RMN e espectrometria de massas. A página foi recuperada nesta data; a ferramenta informa captura de dois meses antes. A compatibilidade com2024/2 não demonstra qual versão foi efetivamente ministrada. O registro de aprovação vem do panorama anterior dos históricos, sem nova inspeção de PDF escolar.

Consulta parcial às fontes primárias:

- [McMurry/OpenStax, Organic Chemistry, §13.1](https://openstax.org/books/organic-chemistry/pages/13-1-nuclear-magnetic-resonance-spectroscopy): núcleo, campo e ressonância. A analogia clássica de núcleo girando não foi adotada como explicação literal do spin.
- [§13.3](https://openstax.org/books/organic-chemistry/pages/13-3-chemical-shifts): posição relativa e conversão ppm/Hz, orientação usual de apresentação.
- [§13.5](https://openstax.org/books/organic-chemistry/pages/13-5-integration-of-1h-nmr-absorptions-proton-counting): áreas relativas e número relativo de prótons, sob hipóteses quantitativas explicitadas nestas notas.

Sem leitura integral do capítulo. Pavia é referência oficial do programa; o inventário anterior identificou versões distintas sem confirmar a edição brasileira citada. O corpo desses exemplares não foi consultado neste bloco; não se presume equivalência de paginação. A busca também localizou a definição IUPAC de deslocamento, mas a abertura direta devolveu403; ela não é apresentada como nova leitura integral. Exemplos, exercícios, figura e código são próprios, não transcrições das fontes.

## Converter antes de interpretar

δ_ppm=10⁶(ν_amostra−ν_ref)/ν_ref, com frequências na mesma unidade. Exemplo escolhido:400000800Hz versus400000000Hz→Δν800Hz→2ppm. Referência600MHz com a mesma posição2ppm dáΔν1200Hz. A relação prática Δν(Hz)=δ_ppm×ν_ref(MHz) decorre dos fatores de10⁶. O laboratório não calcula a referência a partir de campo/blindagem nem prevê deslocamentos de substâncias.

O eixo da figura decresce de4 a0ppm, da esquerda para a direita. Retângulos são apenas funções artificiais a integrar; não são formas de linha de RMN. A: centro3ppm, largura2/5ppm, altura15/2u.a./ppm, área3u.a. B: centro1ppm, largura4/5ppm, altura5/2u.a./ppm, área2u.a. Razão de alturas3:1, de áreas3:2. Integrar só3–3,2ppm recupera1,5u.a. de A, não3.

As frações de área são3/5 e2/5. Se o total de cinco prótons for conhecido por outra evidência e se todos forem representados com a mesma resposta quantitativa, isso corresponde a3 e2. Com total dez,6 e4 também cabem. Se for imposto total seis, a conta produz3,6 e2,4; o código não arredonda nem atribui molécula. Em dados reais seria preciso avaliar incerteza, aquisição, linha de base, sobreposição e outras evidências. Não há calibração de equipamento aqui.

## Executar

Na raiz do site:

```sh
python3 -m labs.rmn-deslocamento-area.nmr
python3 -m unittest discover -s labs/rmn-deslocamento-area -t .
```

Funções aceitam apenas int/Fraction, não bool/float. Frequências absolutas e referência em MHz são positivas; deslocamentos/diferenças podem ser assinados. Os limites de integração são crescentes internamente, independentemente do eixo gráfico; limites iguais dão área zero. Cada componente fornece centro, largura positiva e área não negativa. Componentes sobrepostas são somadas, sem deconvolução. Normalizar exige soma de áreas positiva. O parâmetro total_h deve ser inteiro positivo informado externamente.

Cinco testes: conversões e35 viagens de ida/volta em escalas distintas; oráculo de soma por40 intervalos de0,1ppm, alinhados às bordas; aditividade em41 cortes, sobreposição e translação/largura; normalização/escala e contagens sem arredondamento; contratos. A correspondência dos retângulos é exata por construção; isso não valida respostas de núcleos reais ou uma atribuição estrutural.

## Revisão pessoal e lacunas

Em20min, reconstrua800Hz→2ppm e integre as duas janelas. Depois explique por que as alturas falham e qual informação externa permite usar o total de cinco prótons. Não registrar domínio ou estudo concluído automaticamente.

Ainda faltam acoplamentos e multiplicidades, equivalência química/magnética, troca, processamento/relaxação, espectros reais e identificação com massas/IV. Este recorte muda o grupo de RMN de Lacuna para Parcial; não completa o item4, que também inclui massas, nem a disciplina.
