# Regra da cadeia vetorial — composição e resto

22/10/2026. Aprofundamento da aula existente `c3-cadeia`: 15 seções e 12 exercícios originais; dois exercícios e exemplo escalar anteriores preservados. Pendente de revisão pessoal de Jhuann.

## Fonte consultada

Apostol, Cálculo, volume2, tradução portuguesa Reverté1996/reimpressão2004, original identificado como segunda edição. Exemplar privado e sumário reconferidos no bloco anterior. Corpo lido agora: §8.15 nas páginas impressas296–297(PDF311–312); §§8.18–8.21 nas pp.303–307(PDF318–322), incluindo derivada de campo vetorial, representação por Jacobiana, continuidade e regra da composição. Página306/PDF321renderizada e inspecionada visualmente. Não é leitura integral do capítulo; exemplos/exercícios/figuras dos livros não foram reproduzidos. Paginação da tradução não foi transferida ao inglês.

O apoio diferencial corresponde ao mapa de MatemáticaIII/CCM0213; ApostolIIé referência complementar nessa disciplina e oficial em MatemáticaIV/CCM0223. Esta aula não aumenta cobertura dos cinco grupos integrais/especiais deIV. Programa público não comprova a extensão efetivamente ministrada ou domínio pessoal.

## Justificativa original com os restos

Para F diferenciável em a, escreva F(a+h)=F(a)+Ah+rF(h), com rF=o(||h||). Para G diferenciável em b=F(a), G(b+k)=G(b)+Bk+rG(k), com rG=o(||k||). A composição é definida numa vizinhança. O incremento interno k=Ah+rF(h)é O(||h||), pois aplicações lineares em dimensão finita são limitadas. Substituir a primeira expansão na segunda dá ΔH=BAh+B rF(h)+rG(k). Os dois restos finais são o(||h||); para k=0, rG(0)=0e não se usa uma razão0/0. Assim DH(a)=DG(F(a))DF(a), com ordem e ponto definidos pela composição.

Existência de parciais não substitui a hipótese de diferenciabilidade. Conferir dimensões também não garante que o ponto de avaliação esteja correto. No exemplo, o produto invertido existe, mas tem3×3, enquanto DHtem2×2; a outra composição requer outro ponto de avaliação.

## Exemplo polinomial e limite uniforme

F(u,v)=(u²,v,uv), G(x,y,z)=(x+yz,z²−y), H=G∘F=(u²+uv²,u²v²−v). Coordenadas adimensionais. Jacobianas:

- DF tem linhas (2u,0),(0,1),(v,u), portanto3×2.
- DG(F(u,v)) tem linhas (1,uv,v),(0,−1,2uv), portanto2×3.
- DH tem linhas (2u+v²,2uv),(2uv²,2u²v−1), portanto2×2.

Em(1,2), DH=((6,4),(8,3)), e DH(1,1)=(10,11), onde o segundo par é o vetor-direção, não outro ponto-base. O código usa nomes separados para evitar essa ambiguidade: jv=DH(p)w.

Se h=(α,β), o resto exato após retirar DH(p)h é:

r₁=α²+uβ²+2vαβ+αβ²,

r₂=u²β²+4uvαβ+2uαβ²+α²v²+2vα²β+α²β².

Para |u|,|v|≤2e ||h||≤1, use |α|,|β|≤||h||. Cada monômio de grau pelo menos2é limitado por seu coeficiente em módulo vezes||h||². Isso dá |r₁|≤(1+2+4+1)||h||²=8||h||² e |r₂|≤(4+16+4+4+4+1)||h||²=33||h||². Portanto ||r||≤√1153||h||²<34||h||². A constante não é ótima, mas controla todas as direções, e ||r||/||h||≤34||h||→0.

Essa é a prova uniforme para a família no domínio declarado. Testar três direções numericamente não seria suficiente para demonstrar o limite em todas as direções. A prova geral da cadeia usa as hipóteses de diferenciabilidade, não esta constante particular.

## Interface e interpretação

Base p=(u,v)em[-2,2]²; w é (1,0),(0,1)ou(1,1); ε=2⁻ᵏ,k1..8,h=εw. Logo ||h||≤1. O gráfico mostra vetores de saída q: quadrado azul em DH(p)w e círculo preto em ΔH/ε. Não é superfície/traçado de H nem gráfico no espaço de entrada. Os eixos têm mesma escala entre si, adaptada aos controles. Quando marcadores quase coincidem, a tabela preserva os valores. Para w=(1,1), a direção não é unitária; a norma do incremento usa√2ε.

A tabela mostra DF,DG,produto e vetores completos. O relatório apresenta o quociente do resto e o limite uniforme. Resto por expansão polinomial evita usar cancelamento de ponto flutuante como evidência de uma prova. No domínio discreto do painel, bases inteiras e passos diádicos permitem conferências particularmente limpas.

Tese visual: um plano de vetores de saída e matrizes rotuladas, para acompanhar a composição. Conteúdo: espaços/hipóteses, demonstração, exemplo, exploração e exercícios. Interação: mudar ponto/direção/refinamento com atualização imediata, preservando teclado; sem animação decorativa.

## Execução e verificações

Na raiz:

```sh
python3 labs/cadeia-vetorial/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes novos: composição e Jacobiana por derivação direta; expansão independente em frações para600estados; limite uniforme/refinamento e concordância do resto; dimensões/contratos.36estados de referência Python/JScom matrizes e vetores completos. Testes finitos verificam implementação, não substituem as demonstrações.

## Lacunas e sequência

Autodiferenciação, aplicação física com unidades, funções implícitas, Hessianas e outros usos continuam para recortes futuros. Notas/Samsung Notes e resolução pessoal não importadas. Nenhuma reivindicação de pesquisa ou domínio baseada nesta produção assistida por IA.

Próxima alternância global: auditar QuímicaIII antes de escolher assunto. A integração de MatemáticaIVcontinua parcial e não foi ampliada por esta aula diferencial.


Verificação final:574testes Python,241demonstrações/723cenários,330MathML e36estados de referência aprovados. Notação científica preservada para resto pequeno; refinamento, derivada nula, matriz e resposta6conferidos. Desktop/390px sem transbordamento ou erros observados no console; viewport restaurado. Catálogo462/2054, revisão pessoal pendente. Saldo90%,parada65%.
