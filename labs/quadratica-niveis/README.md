# Função quadrática: vértice, raízes e alturas

22/10/2026. Rascunho para revisão e preparação de aulas. Aprofunda `em-quadratica`, preservando título, dois IDs antigos, exemplo mínimo−1 e desafio de quadrado completo. Python continua opcional; não se exige programação para teoria/exercícios.

## Fonte e autoria

[OpenStax, College Algebra2e, §5.1 Quadratic Functions](https://openstax.org/books/college-algebra-2e/pages/5-1-quadratic-functions), consulta direta parcial em22/10/2026: formas geral/de vértice, equivalência por expansão, extremos, domínio/imagem. Não lida integralmente a seção, nem reproduzidos exemplos, problemas, fotografias ou figuras. Demonstrações aplicadas, enunciados, traçados e código próprios. Complemento escolar de reforço, sem alegar disciplina do histórico, matriz de exame ou material já testado com alunos.

## Ideias e provas

Para a≠0, completar o quadrado produz f=a(x−h)²+k, h=−b/(2a), k=c−b²/(4a). O sinal do quadrado prova extremo global e imagem no domínioℝ, sem derivadas. f(h+d)=f(h−d), enquanto f(0)=c. Entradas, saídas, eixo, vértice e interceptos não são intercambiáveis.

f(x)=L equivale a(x−h)²=L−k e ao polinômio ax²+bx+(c−L)=0. Δ_L=b²−4a(c−L)=Δ+4aL=4a²[(L−k)/a]. Para a≠0, classificam-se0/1/2entradas reais distintas. Raiz dupla significa uma entrada com multiplicidade2. O marcador “V=raiz” só aparece quando L=0 e k=0; se L=k≠0, usa “V na reta”, porque a interseção não é zero de f.

Com a0/bnão nulo, resolver a equação afim; com a=b=0, para L=c todos os reais e para L≠c nenhum. Não atribuir vértice único de parábola ou aplicar Δ=0 como “raiz dupla” a uma identidade constante. Imagem da constante{c}; imagem da afim não constanteℝ. A constante tem mínimo/máximo de mesmo valorc, mas não um vértice único.

Exemplo preservado: x²−4x+3=(x−1)(x−3)=(x−2)²−1. Raízes1 e3, vértice(2,−1); L−1 → uma entrada2, L−2 → nenhuma; L0 → duas. No domínio[0,1], a função decresce até o extremo permitido x1 e o mínimo é0; não é−1. A prova no intervalo usa monotonicidade, não a amostragem numérica dos testes.

## Painel e compatibilidade

Identificador `quadraticShape` preservado e controles a/b/c anteriores mantidos; acrescentado nível L, padrão0. Entrada renderizada sem L continua interpretada como L0. A definição antiga do painel foi removida de `schoolmath-models.js`; a nova está em `quadratic-level-models.js`, sem duas definições competindo. O helper exportado `SchoolMathModels.quadratic` foi preservado para compatibilidade, mas o painel novo usa seu próprio solver e distingue número de raízes distintas.

Curva azul, reta L tracejada, círculos de interseção e losango do vértice. A janela quadrática tem x=h±3; casos afim/constante usam[−4,4]. Todos têm domínioℝ. Contagem global usa álgebra, não o número de marcadores visíveis; raízes fora da janela são indicadas. Eixo vertical adaptado a extremos da curva, nível e zero, com marcas legíveis. Vértice adicionado aos pontos da curva para que um toque na reta não se perca pela discretização. Isso melhora o desenho, não transforma uma grade em prova.

## Executar e verificar

```sh
python3 labs/quadratica-niveis/experiment.py
python3 -m unittest discover -s labs/quadratica-niveis -t .
```

Quatro testes: identidade de quadrado completo/simetria/extremo em252parábolas e21pontos racionais; classificação de2835configurações a/b/c/L por raio² racional independente, substituição das raízes e Viète; casos de degeneração/janela/exemplo; contratos e apoio ao exemplo restrito.72estados cruzam JS/Python, incluindo constantezero, afim, nenhum resultado, raiz dupla, negativos e vérticezero sem “−0”. Os testes não provam cobertura geral sozinhos; as justificativas estão no texto.

Código deliberadamente limitado às faixas pequenas do painel (a−2..2,b−4..4,c−3..3,L−4..4), sem prometer solver numericamente estável para coeficientes arbitrários ou raízes complexas. Frações usadas no Python para vértice/identidades; raízes não racionais aproximadas e indicadas por números decimais no painel.

## Continuidade

Revisão pessoal, diagnóstico de aluno e planos de aula pendentes. Construção de modelos, inequações quadráticas, intervalos de sinal, funções por partes e problemas com domínio físico precisam de recortes próprios. Não declarar curso completo ou pronto para oferta por estes testes.
