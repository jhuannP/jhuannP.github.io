# Termos LS e contagem de estados

Notas de aula em rascunho; revisão pessoal pendente. Um recorte do item7 de CCM0214, não cobertura integral.

## Fontes

Miessler,Fischer e Tarr,Química Inorgânica5ªed.,Pearson2014,§11.2 pp.398–401/PDF413–416. Consulta textual parcial29/10/2026 ao exemplar privado autorizado, cabeçalhos conferidos com extração dessas páginas; sem nova inspeção visual, leitura integral ou distribuição do PDF. Apoio para Pauli, projeções, termos e contagem por contribuições retangulares. Fórmulas, fatos de configuração e termos são conhecidos; explicação, código e figura próprios, sem transcrever enunciados ou gabarito do livro.

[NIST,§§6–7 LS Coupling e hierarquia](https://physics.nist.gov/Pubs/AtSpec/node06.html) e [§8 Allowed Terms](https://physics.nist.gov/Pubs/AtSpec/node08.html), consulta direta parcial29/10/2026: notação e termos equivalentes. A parte jj da página8 não foi desenvolvida na aula. [JúpiterCCM0214](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0214), reaberto29/10/2026, ativação15/07/2024, captura indicada de dois meses antes; versão da turma não comprovada.

## Executar

Na raiz: `python3 labs/termos-ls/terms.py`; testes: `python3 -m unittest discover -s labs/termos-ls -t .`.

Uma única subcamada s,p ou d, ℓ=0,1,2, até a ocupação completa. Combinações de spin-orbitais distintos representam determinantes de Slater. Histograma em M_L e2M_S. Subtração de maiores pesos fornece os pares(L,2S), repetidos quando necessário. Não obtém coeficientes de funções de onda, energia, senioridade, Racah, intensidade, transição ou configuração misturada. O histograma não é um Hamiltoniano.

Para d²:³F21,³P9,¹G9,¹D5,¹S1, soma45. Em M_S=1, o máximo M_L é3 por Pauli; em M_S=0 existe M_L=4. A decomposição de dimensões não significa que cada determinante inicial pertence sozinho a um termo. ³F contém níveis J2,3,4, dimensões5+7+9; nenhuma ordem energética é atribuída.

## Próxima revisão

Reconstruir as linhas e explicar a exclusão de³G em20min. A teoria formal de representações, operadores de momento, autovetores, repulsão intereletrônica, Racah e ligação com complexos continuam pendentes. Testes finitos não comprovam toda interpretação física ou estudo pessoal.
