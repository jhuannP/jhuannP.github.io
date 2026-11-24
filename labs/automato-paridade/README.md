# AFD: paridade e traçado de prefixos

Rascunho original, pendente de revisão de Jhuann. AFD determinístico sobre {0,1}, estados par/ímpar, início par e aceitação em par. Ler0 mantém; ler1 troca. A prova por indução mantém o estado igual à quantidade de1 no prefixo módulo2. Necessidade de dois estados: ε aceita e1 rejeitada não podem terminar no mesmo único estado de um AFD total.

Exemplo preservado1011: estados0,1,1,0,1. O prefixo101 isolado seria aceito, mas a palavra completa é rejeitada. Painel preserva seleção decimal0–15 das palavras de quatro bits, incluindo zeros iniciais, e passo0–4. São80 configurações. Palavra vazia é tratada no texto/código e no prefixo inicial; não se afirma que o painel permite escolher comprimento arbitrário.

Reconhecer em fluxo guarda apenas o estado, com memória adicional constante e uma transição por símbolo. `trace` e interface guardam a história, com memória adicional linear. A entrada armazenada é excluída da contagem O(1) do reconhecedor. O domínio não aceita símbolos fora do alfabeto; erro de entrada difere de rejeitar uma palavra binária válida.

## Fonte consultada parcialmente

Sedgewick/Wayne, Computer Science: An Interdisciplinary Approach, exemplar2016, §5.1, pp.impressas738–740/PDF759–761. Operação e caracterização do AFD; p.739/PDF760 inspecionada visualmente. Os exemplos do livro usam outras máquinas: nosso autômato binário de paridade, prova, figura e código são próprios. Tentativa de abrir página pública de Princeton retornou403; não foi usada como fonte lida. PDF privado não distribuído.

## Reproduzir

Na raiz do protótipo:

```sh
python3 labs/automato-paridade/experiment.py
python3 -m unittest discover -p 'test_*.py'
node test_simulations.cjs
node test_math.cjs
```

Quatro testes locais:2047 palavras até comprimento10 e todos os prefixos contra contagem independente; concatenação de31×31 palavras e extensão por0/1;80 estados do painel e8 palavras aceitas de comprimento4; ε, testemunhas e domínio inválido. Referências JSON cruzadas com JS. Testes finitos apoiam a implementação; a prova geral é a indução descrita na aula, não a enumeração isolada.

Pendentes: exemplos além da paridade, produtos, minimização geral, não determinismo, conversão de expressões regulares e aplicações. Nenhuma aula ou teste certifica domínio pessoal ou conclusão de ComputaçãoII.
