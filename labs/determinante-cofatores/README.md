# Cofatores e adjunta clássica

Extensão da aula de área/determinantes,rascunho para revisão pessoal. Sobre R ou Q e dimensão finita. Matriz quadrada até ordem6,int ou Fraction;det([])=1 é convenção para o determinante vazio,necessária aos cofatores de1×1. Sem cálculo simbólico geral ou solver escalável.

`determinant` expande recursivamente a primeira linha. `expansion` retorna contribuições assinadas para qualquer linha válida. `adjugate` retorna C transposta,adjunta clássica; não é a adjunta de operador por produto interno. Não se usa determinante pequeno em float para decidir condicionamento. A expansão é um instrumento de prova/estudo; eliminação tem custo aritmético melhor em dimensão grande. Contagem de operações não é custo de bits de racionais.

Exemplo A=[[2,1,0],[0,3,1],[1,0,2]]:menores primeira linha6,−1,−3;cofatores6,+1,−3;contribuições12,1,0;det13. A inversa existe e entrada(1,2)=C21/13=−2/13. A=[[1,2],[2,4]] tem det0 e adjunta não nula;A adj(A)=0 não permite dividir para obter inversa.

## Fonte

MIT OCW,Calculus with Applications,§32.4 More on Determinants, https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter32/section04.html :recortes textuais de propriedades,cofatores/sinal,composição e argumento da inversa consultados parcialmente em29/10/2026. A imagem da fórmula da inversa não é legível na extração; a aula prova a identidade diretamente,sem alegar leitura da imagem. Não se reproduz o texto ou exemplo da fonte. Prova por expansão multilinear/permutação e matrizes/exercícios próprios. Não houve nova consulta a exemplar privado ou ao Júpiter;programaCCM0213 mantém data anterior28/10/2026,ativação15/07/2024,versão ministrada não comprovada.

## Verificação

```sh
python3 -B -m unittest discover -s labs/determinante-cofatores -t .
python3 labs/determinante-cofatores/cofactors.py
```

Cinco métodos:81 matrizes2×2 por Leibniz independente;48 matrizes de ordens1..6 por Leibniz e eliminação racional independente,com todas as expansões por linha;25 matrizes verificando ambos os produtos com adjunta usando determinante de eliminação;marcos incluindo matriz vazia,1×1 e singular;contratos. Testes finitos verificam exemplos/código, não provam os teoremas gerais. Provas e hipóteses estão na aula;revisão pessoal permanece pendente.
