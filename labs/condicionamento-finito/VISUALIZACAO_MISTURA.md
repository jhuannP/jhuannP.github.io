# Independência nos grupos e na mistura

22/10/2026. Material original em rascunho, pendente de revisão pessoal de Jhuann. Pré-requisito: aula `probabilidade-condicional`. A nova aula `mistura-independencia` desenvolve a visualização sem substituir o painel anterior de quatro regiões.

## Fontes e alcance

Referências temáticas locais reconferidas parcialmente no texto extraído: Magalhães e Lima, *Noções de Probabilidade e Estatística*, 7ª edição, §2.2, pp. 58–59 (PDF 73–74): partições, probabilidade total e Bayes; Magalhães, *Probabilidade e Variáveis Aleatórias*, 2ª edição, §1.3, p. 35 (PDF 22, página dupla): independência e independência condicional. São recortes, sem leitura integral nem reprodução de exercícios. A consulta utiliza PDFs privados do acervo autorizado; nenhum PDF ou imagem de suas páginas integra o site.

O exemplo de mistura, seus parâmetros, a fatoração aplicada e os exercícios são próprios. A hipótese de distribuição produto dentro de cada grupo precede o cálculo; não é uma conclusão obtida de observações. A fatoração Δ=λ(1−λ)(p₁−p₀)(q₁−q₀) decorre da expansão das marginais e da probabilidade total. Não se afirma que esse exemplo está nos livros.

## Exploração e referência exata

Todos os controles representam quartos. Estado padrão (k,p₀,q₀,p₁,q₁)=(2,1,1,3,3): pesos 1/2; marginais internas 1/4 e 3/4. Cada componente é uma tabela produto com denominador 16. A mistura tem denominador 64; há átomos duplicados em relação à apresentação de 32 átomos da aula, sem mudar as massas. Joint 5/16, produto 1/4, diferença 1/16, P(A|B)=5/8.

1. Reduza somente q₁ a zero: diferença −1/32.
2. Iguale p₁ a p₀: diferença zero, ainda que q varie.
3. Faça k=0 ou k=4: grupo ausente não admite condicional pela razão. Parâmetros desse grupo não afetam a mistura.
4. Faça q₀=q₁=0: P(B)=0, logo P(A|B) não definida no laboratório. Os livros adotam uma convenção extra para esse caso; ela não é resultado de 0/0.

As barras representam probabilidades, em escala compartilhada 0–1; azul contínuo indica conjunta, preto tracejado indica produto das marginais. Números exatos acompanham a codificação visual. Sem simulação aleatória, causalidade, erro amostral, dados pessoais, resultados físicos ou condicionais contínuas.

## Código e verificação

`mixture.py` permanece a referência racional Python, com testes existentes que enumeram 3125 configurações de 64 átomos. `mixture-reference.json` contém 245 estados gerados por essa rotina (3⁵ extremos/intermediários, mais dois exemplos de associação), usados na comparação com JavaScript. `mixture-conditioning-models.js` usa contagens inteiras: massa em 64 átomos; diferença em 4096 unidades. Independência é verificada sem tolerância flutuante. Testes JavaScript também enumeram 64 átomos independentemente em todas as 3125 configurações e verificam a fatoração.

Próximo passo didático: Jhuann explicar a fatoração e os grupos de massa zero, e resolver um exemplo sem consultar a visualização. Densidades condicionais e transição discreto–contínuo continuam pendentes.
