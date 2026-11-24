# Lei de Gauss para duas fontes esféricas

Material original em rascunho para revisão de Jhuann. Distribuições prescritas e normalizadas, sem experimento ou resultado da IC.

## Fontes consultadas em 16/10/2026

- [OpenStax University Physics II 6.2](https://openstax.org/books/university-physics-volume-2/pages/6-2-explaining-gausss-law): fluxo orientado, carga interna e campo total.
- [OpenStax 6.3](https://openstax.org/books/university-physics-volume-2/pages/6-3-applying-gausss-law): trechos de simetria esférica e esfera volumétrica, não toda a seção.
- [Feynman Lectures II, capítulo 4](https://www.feynmanlectures.caltech.edu/II_04.html): trechos 4–6/4–7, lei de Gauss, forma diferencial e campo externo esférico. Edição oficial online; não se inferiu paginação do PDF português do acervo.

Exemplos, exercícios, código e gráficos próprios. Nenhuma figura, lista protegida ou PDF privado reproduzido. A bibliografia oficial e os exemplares identificados do acervo continuam no mapa de Física III; este bloco usa as fontes online indicadas.

## Modelo

Vácuo, R=1 e ε₀=1 em unidades normalizadas. Q com sinal. Perfil 0: volume uniforme, Q interna=Q min(r³,1), Eᵣ=Q interna/(4πr²) para r>0. Perfil 1: casca superficial uniforme, campo zero dentro e Q/(4πr²) fora. Na camada não nula r=1, o painel apresenta apenas limites, sem um valor único. Para Q=0 não há camada carregada nem salto.

No centro o campo é zero por simetria; fluxo em r=0 significa limite, não uma superfície regular de área zero. Uma esfera com excesso de carga condutora em equilíbrio não é o perfil volumétrico uniforme. Nenhuma fonte externa ou polarização incluída.

O gráfico alterna 4πEᵣ e Φ; a tabela usa Eᵣ sem esse fator. Não compare números de eixos diferentes sem conversão. A casca é desenhada em dois trechos, sem ligar o salto; a marca em r=R mostra a fronteira da fonte.

## Verificação independente

Na raiz: `python3 -m unittest discover -s labs/gauss-esferico -t .`.

Quatro testes: integração radial de densidade e escalas de volume/área; quadratura angular independente da integral de Coulomb para casca (18 configurações, erro absoluto <2e−10); continuidade da esfera, salto da casca, centro, carga nula e exterior comum; exemplo de fluxo nulo com campo uniforme e validação de domínio. `reference.json` contém trinta configurações JS/Python, incluindo superfície e carga zero.

A quadratura usa Simpson com 4000 painéis, evita r=1 e não demonstra o teorema geral. A integral de Coulomb para casca de raio um é Q/(8πε₀) vezes ∫ de −1 a 1 de (r−u)/(r²+1−2ru)^(3/2) du. Não há cálculo numérico singular na camada.

## Pendências

Densidades radiais gerais, geometrias cilíndricas/planas, campos externos, materiais, redistribuição condutora, potenciais, energia e condições de contorno mais gerais. O curso continua parcial e não certifica domínio pessoal.
