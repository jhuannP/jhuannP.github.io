# Módulo como distância na reta

Rascunho original para reforço escolar. Papel,reta numérica e álgebra bastam;Python é opcional. Execute `python3 intervals.py`,sem dependências adicionais.

## Deduções e condições

|x|=x para x≥0 e−x para x<0. A distância de x até a é|x−a|,não a diferença geral dos módulos. Para r>0,a igualdade seleciona a±r;em r0,um ponto;em r<0,nenhum.

Para r≥0,|x−a|≤r equivale a a−r≤x≤a+r. A versão estrita exige r>0 para um intervalo interno não vazio. |x−a|>r seleciona x<a−r ou x>a+r;é união,não interseção. Inclusão de extremos deve acompanhar o sinal da comparação.

Para A≠0,|Ax+B|=|A||x+B/A|. O centro é−B/A e o raio reduzido r/|A|,quando r≥0. A=0 requer uma comparação constante,verdadeira para todos os x ou para nenhum. r<0 e r0 recebem casos próprios,sem divisão indevida ou dois pontos artificiais.

Em |x−2|=x,exigir x≥0 e separar a expressão dá solução1. Em |x+2|=x,o quadrado produz candidata−1,que falha na condição de sinal e na equação original. Não se alega que toda transformação por quadrado é equivalente sem condições.

A desigualdade triangular real segue de somar−|u|≤u≤|u| e−|v|≤v≤|v|;logo|u+v|≤|u|+|v|. Uma cota pode ser maior que o valor realizado:para2 e−5,temos3≤7. Todas as deduções,casos,numeração,figura e exercícios são próprios.

## Laboratório opcional

solve(A,B,r,comparador) usa int/Fraction e retorna intervalos exatos,com flags de inclusão. None é limite ausente,não um número infinito usado em aritmética. Coeficiente zero,limite negativo,limite zero,igualdade e quatro desigualdades são separados. contains apenas confere pertinência ao conjunto devolvido;as deduções gerais não dependem de amostrar reais. Não resolve expressões variáveis no lado direito de forma geral,nem inequações não lineares.

## Fontes parciais —27/10/2026

- [OpenStax Algebra and Trigonometry2e,§2.6](https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-6-other-types-of-equations),trechos de equações de módulo e definição por partes.
- [OpenStax,§2.7](https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-7-linear-inequalities-and-absolute-value-inequalities),notação de intervalos e inequações de módulo.

Leituras parciais,sem copiar exercícios,figuras ou seus números. Nesta aula a contagem de soluções afins explicita A≠0 e trata A=0 separadamente. Nenhuma matriz curricular brasileira/prova específica consultada;sem alegar equivalência,domínio docente ou aula já ministrada. Mais funções modulares,gráficos e problemas integradores pendentes.

## Verificações e próxima ação

Cinco testes locais:1470 combinações de coeficientes/limites/comparadores,confrontadas com a expressão original em49 pontos racionais cada,72030comparações;fronteiras racionais−1 e1/3 e seus arredores;casos constantes/zero/negativo;1681pares racionais da desigualdade triangular e candidata falsa após quadrado;contratos. Grade finita não verifica todos os reais,mas o retorno é deduzido por casos. O código não usa float para decidir fronteiras.

Em20min,desenhe os intervalos internos/externos de centro3 e raio2,explique “e”/“ou”,resolva o coeficiente negativo e confira a candidata−1 na original. Revisão pessoal,uso com aluno,Windows real e leitor de tela pendentes.
