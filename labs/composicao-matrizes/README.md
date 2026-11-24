# Composição: notas de aula

Rascunho original assistido por IA, revisão pessoal pendente. Material não comprova domínio ou formação concluída.

## Derivações e exemplos

B:U→V, A:V→W, composição u→A(Bu). Linearidade vem da aplicação sucessiva das duas linearidades. Nas bases compatíveis, a coluna j de AB é A aplicado à coluna j de B; o elemento(i,j) é Σₖaᵢₖbₖⱼ. Assim tamanho m×n vezes n×p produz m×p. Associatividade vem de A(B(Cx)) em qualquer agrupamento, sem permutar.

Original preservado: A=diag(2,1), B=[[1,1],[0,1]]. AB=[[2,2],[0,1]], BA=[[2,1],[0,1]]. Em(0,1) dão(2,1) e(1,1); em(1,0) coincidem, sem serem a mesma aplicação. Igualdade em uma base inteira, com mesmos espaços, implica igualdade por linearidade.

Novo retangular: B(x,y)=(x,y,x+y), A(u,v,w)=(u+w,v−w). AB(x,y)=(2x+y,−x); BA(u,v,w)=(u+w,v−w,u+v). Produtos2×2 e3×3 atuam em espaços diferentes. Em(1,2), AB dá(4,−1).

Cancelamento: A=diag(1,0), B=I, C=diag(1,2) dão AB=AC e B≠C. Se A é injetiva, A(Bx)=A(Cx) força Bx=Cx para todo x. Inversa de AB, quando ambas existem, é B⁻¹A⁻¹; conferir produtos dos dois lados.

Bases: P converte W→V no espaço intermediário. A_W=A_VP e B_W=P⁻¹B_V, logo A_WB_W=A_VB_V. Dimensões compatíveis não bastam sem coordenadas compatíveis. Não representa automaticamente translações ou mudanças não lineares. Conexão com cadeia exige pontos e restos próprios, não só produto formal.

## Respostas

Preservadas duas questões: primeira coordenada2; não há comutatividade geral. Novas:1;2;4;−1;4 colunas;sim para igualdade em base;associatividade não permuta;cancelamento sem hipótese não vale;inversaB⁻¹A⁻¹;converter bases intermediárias. Mantidos exemplo, Python e desafio originais.

## Laboratório

`exact.py` aceita matrizes list/tuple retangulares não vazias, entradas int/Fraction sem bool/float; retorna tuplas de frações sem alterar a entrada. `apply` recebe vetor coluna list/tuple. Não modela dimensão zero ou erro numérico.

Na raiz do protótipo:

```sh
python3 -m unittest discover -s labs/composicao-matrizes -t .
```

Cinco testes: mapas2D em49vetores;caso retangular em49vetores e125triplas com fórmulas diretas;6561pares de matrizes2×2 ternárias contra reconstrução por imagens da base;conversão intermediária e contraexemplo;contratos. Testes corroboram implementação; provas algébricas nas notas sustentam os resultados gerais.

## Referências e limites

ProgramaCCM0213 item2, reaberto27/10/2026: https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0213 . Ativação15/07/2024 compatível com2024/2 não comprova programa ministrado.

Lima, Álgebra Linear, IMPA2014, §8 pp.83–88/PDF94–99 parcialmente consultados em27/10; p.87/PDF98 visualmente conferida para o teorema de composição. Mudança de bases p.89/PDF100 lida parcialmente. Referência complementar, não uma das referências oficiais localizadas. Leitura parcial não implica capítulo integral; exemplos numéricos, figura, código e texto próprios. PDF privado não distribuído, exercícios não reproduzidos.

Permanecem inversas gerais, mapas em espaços de funções, adjuntos, interpretação física detalhada e estabilidade numérica. O programa oficial abrange muito mais que este recorte. Sem resultado de pesquisa, autoria independente ou revisão pessoal presumida.

## Registro pessoal

Data: ____ · derivação reconstruída: ____ · dúvida: ____
