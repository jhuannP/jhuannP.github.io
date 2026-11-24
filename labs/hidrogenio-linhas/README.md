# Hidrogênio: linhas e diferenças de energia

Rascunho original, 22/10/2026, pendente de revisão de Jhuann. Não contém observações nem dados da IC.

## Fontes e escolhas

Atkins/Jones/Laverman, *Princípios de Química*, sétima edição, Bookman 2018, Tópico 1A.3, páginas impressas 6–8/PDF 138–140, consulta parcial por extração local. Os avisos “Invalid Font Weight” não impediram a leitura dos parágrafos relevantes. A edição difere da terceira citada no programa de Química I. Parte de 1A.2 aparece na primeira página, mas não se afirma leitura integral desse tópico. Nenhum PDF, tabela ou figura do exemplar privado foi reproduzido.

[OpenStax Chemistry 2e, 6.2](https://openstax.org/books/chemistry-2e/pages/6-2-the-bohr-model), consulta parcial em 22/10/2026: quantização de níveis, balanço de energia, relação Eγ=hc/λ e limites do modelo de um elétron. A figura própria é um conjunto de marcadores em comprimento de onda; não replica figuras das referências. Exemplo 6→2 e exercícios preparados para este recorte, sem copiar enunciados ou soluções.

Parâmetros didáticos arredondados: Eₙ=−13,6/n² eV e hc=1240 eV nm. Casas decimais dos resultados mostram a aritmética deste modelo, não precisão física. Não usar os valores como banco espectroscópico ou comparação de alta resolução com um instrumento. Emissão direta de n=3,…,8 até n=2. Não se implementam cascatas, intensidades, taxas, larguras ou regras de seleção. Não é descrição espacial de órbitas ou orbitais, nem modelo de átomos multieletrônicos.

## Exploração

Padrão 6→2: E inicial=−17/45 eV, E final=−17/5 eV, fóton=136/45 eV, λ=6975/17 nm≈410,29412 nm. A variação do átomo é o negativo da energia do fóton. Na passagem inversa, a mesma diferença deve ser fornecida ao átomo.

O painel mostra seis posições em escala fixa 350–700 nm: azul contínuo identifica a escolhida, preto tracejado as demais. Alturas iguais são só marcadores, sem eixo vertical físico e sem significado de intensidade. A figura não reproduz cores da luz. n aumenta: energia do fóton aumenta e λ diminui, acima do limite λ=6200/17 nm. O limite exige n→∞ e não é alcançado pelas seis transições.

## Executar e conferir

Na raiz do protótipo:

```sh
python3 labs/hidrogenio-linhas/experiment.py
python3 -m unittest discover -s labs/hidrogenio-linhas -t .
```

Modelo Python usa Fraction; só aceita inteiros 3–8, rejeitando bool e outros tipos. Três testes: identidade inversa do comprimento de onda e conservação de energia nas seis transições; monotonicidade, limite e valores racionais do exemplo; contratos inválidos. Seis referências racionais em JSON confrontadas com JavaScript. A identidade alternativa testa consistência algébrica; não é validação por observação espectral.

Aula com 12 seções/10 exercícios; primeiro recorte de estrutura eletrônica, sem cobertura do eixo. Faltam modelo nuclear, orbitais, configurações, spin, Pauli e periodicidade. Próxima preparação: distinguir estado, orbital e números quânticos antes de configurações; intercalar com outros eixos da biblioteca.


Verificação final: 758 testes Python aprovados; suíte JavaScript 277 demonstrações/831 cenários básicos e referências adicionais aprovada; 445 estruturas MathML conferidas. No navegador, mudança por teclado para n=8 atualizou emissão 8→2 e λ≈389,01961 nm; exercício aceitou 6200/17. Rótulos ampliados, 390 px sem transbordamento horizontal, sem erros de console observados e viewport restaurado. Prévia `hidrogenio-linhas-mobile.jpg` na raiz do protótipo.

Catálogo atual 486 aulas/2527 exercícios; Química I seis aulas/64 exercícios, cinco grupos parciais e quatro lacunas. Próxima alternância global: Biologia I, retomando os fundamentos celulares antes de outro aprofundamento químico. Saldo após o bloco: 74%; parada em 65%.
