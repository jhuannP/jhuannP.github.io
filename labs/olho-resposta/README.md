# Origem ocular e resposta contextual

Atividade original e fictícia para a aula de diferenciação visual. Não é um experimento realizado, simulação de desenvolvimento embrionário ou protocolo de indução do cristalino.

Duas rotas selecionadas: neuroectoderma encefálico → vesícula/cálice óptico → retina; ectoderma superficial → placódio/vesícula do cristalino → cristalino. A interação entre tecidos não equivale a conversão de uma origem na outra. O SVG próprio distingue as relações pelo tipo de linha e pelas legendas.

## Contas prescritas

A e B são estados hipotéticos, S é um sinal fictício e M um marcador fictício. Não identificam BMP4, Sox2 ou formação de cristalino. São dadas A0=2/20, A1=14/20, B0=1/20, B1=3/20.

As mudanças são 3/5 e 1/10; a diferença entre mudanças é 1/2 na escala de frações. As razões são 7 e 3. Escalas diferentes não são intercambiáveis. Reexpressar 2/20 como 6/60 não cria réplicas.

`response.py` usa `Fraction` e valida contagens inteiras, denominador positivo e numerador entre zero e total. `test_response.py` confere valores literais, reexpressões, troca de condições e entradas inválidas. Não estima variabilidade, valor-p, mecanismo ou competência real.

Execute da raiz do protótipo:

```sh
python3 labs/olho-resposta/response.py
python3 -B -m unittest discover -s labs/olho-resposta -t .
```

## Fontes e limites — 29/10/2026

- Bear, Connors e Paradiso, Neurociências, 4ª edição brasileira, 2017, cap. 7, p. 196/PDF 238: releitura textual parcial da rota óptica.
- Alberts et al., Biologia Molecular da Célula, 6ª edição brasileira, 2017, cap. 21, pp. 1153–1154/PDF 1189–1190: trechos textuais sobre indução sequencial; apoio complementar, não bibliografia oficial substituta.
- Gilbert, Developmental Biology, 6ª ed., 2000, [Induction and Competence](https://www.ncbi.nlm.nih.gov/books/NBK9993/): somente trecho indexado; abertura pediu verificação. Gilbert 12 não localizado por nome no acervo, sem equivalência entre edições.
- Furuta e Hogan (1998), [BMP4 is essential for lens induction in the mouse embryo](https://doi.org/10.1101/gad.12.23.3764): somente resumo indexado, sem métodos, artigo integral, imagens ou números incorporados. Editor retornou 403 e PMC pediu verificação.

Não foram copiados diagramas ou exercícios das fontes. A atividade aritmética não reproduz resultados desses autores. Necessidade, suficiência contextual e restauração do sistema são perguntas distintas. Tipos celulares da retina, circuitos, maturação funcional e regeneração não estão cobertos aqui. Revisão pessoal de Jhuann e uso com aluno pendentes.
