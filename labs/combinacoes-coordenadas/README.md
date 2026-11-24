# Combinações lineares: existir, reconstruir e ser único

27/10/2026. Aula original em rascunho,12 seções/12 exercícios, aguardando revisão pessoal. Pré-requisitos: vetores2D, soma, escala e igualdade de componentes.

## Revisar em dois blocos

1. Com u=(1,0),v=(1,1), reconstrua(3,2) e prove que a representação é única. Depois acrescente w=(0,1) e varie(3−t,t,2−t),explicando por que todos os coeficientes produzem o mesmo alvo.
2. Mostre que(3,2) não está no gerado por(1,1),(2,2). Troque a ordem da base e compare coordenadas(1,2) com(2,1). Reconstrua a norma ao quadrado13,distinta de5 para a soma dos quadrados dos coeficientes.

## Código e contratos

Execute `python3 labs/combinacoes-coordenadas/coordinates.py` na pasta do protótipo. Fraction garante contas racionais exatas nos exemplos. O programa confere reconstrução,ordem da base,representações redundantes,produto interno e fechamento. Não é resolvedor genérico de sistemas, detector numérico de posto ou teste geral de independência.

Cada vetor tem exatamente duas componentes e há um coeficiente por vetor. A família vazia representa só o vetor zero por convenção. A solução do desafio original passa a validar2D: zip sozinho truncaria a sequência maior. Não se transforma essa validação específica em promessa de suporte a dimensões arbitrárias ou a valores float.

A figura mostra o paralelogramo de u+2v num sistema cartesiano. Ela não transforma coeficientes em comprimentos; a base oblíqua não preserva o produto interno canônico dos coeficientes. A combinação afim exige soma dos coeficientes1,e a convexa também exige não negatividade: são restrições adicionais, não sinônimos do espaço linear gerado.

## Fontes e alcance

- [USP CCM0213](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0213),reaberto em27/10/2026. Ativação15/07/2024,programa inclui espaços lineares e outros oito grupos; a seleção efetiva da turma e a versão ministrada continuam com os limites já registrados. Não se substitui a bibliografia oficial pelo apoio complementar.
- Elon Lages Lima, Álgebra Linear, IMPA2014: §2 p.11/PDF22 e§3 pp.24–26/PDF35–37, consulta textual parcial em27/10/2026 no acervo autorizado. Definições de gerado,independência e coordenadas. Extração usa acentos decompostos; normalizados apenas para leitura. Sem nova inspeção visual,leitura integral,cópia de exercícios ou distribuição do PDF privado.

Exemplos,figura,código e exercícios próprios. O exemplo inicial da aula foi preservado. Espaços de funções,corpo complexo,bases gerais e dependência numérica exigem desenvolvimento adicional. Todas as18 aulas de ÁlgebraLinear agora têm mais de três seções,mas os nove grupos do programa continuam parciais. Contagem de páginas não certifica conclusão,estudo ou domínio pessoal.
