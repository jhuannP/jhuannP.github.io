# Carga, campo e força — notas de aula para reforço

Aula original em rascunho, com Python **opcional**. Não pressupõe cálculo diferencial. Requer potências de10, proporções e interpretação de setas em uma reta. É sequência própria de apoio às aulas particulares; não certifica cobertura integral da BNCC, currículo de uma escola, experiência com alunos ou domínio pessoal de Jhuann.

## O que representa cada símbolo?

Carga q é propriedade de um corpo, em coulomb(C). Campo E é uma grandeza vetorial, em N/C, associada à configuração das cargas-fonte nos pontos do espaço. Força F é a interação sobre uma carga de prova, em newton(N). Para fontes fixas e prova ideal que não modifica significativamente sua configuração, F=q_tE.

Duas cargas puntiformes separadas por d>0 têm módulo de força F=k|q₁q₂|/d². O sentido depende de posição e sinais: sinais iguais repelem; diferentes atraem. As forças do par atuam em corpos diferentes e não se cancelam no diagrama de um único corpo. Usamos k=9,0×10⁹N·m²/C², arredondado para a conta, em vácuo. O arredondamento não é um valor físico exato. Corpo extenso próximo, redistribuição de cargas e meios materiais exigem atenção adicional.

Nano significa10⁻⁹; micro,10⁻⁶. Para+3nC e−4nC a0,20m, o módulo é2,7×10⁻⁶N=2,7μN, atrativo. Dobrar d quadruplica d² e reduz o módulo para1/4; dobrar apenas uma carga dobra o módulo, conservando as demais condições.

## Campo em um ponto

O módulo do campo de uma fonte Q é k|Q|/d². O sentido é para fora da positiva e em direção à negativa. Com várias fontes, some as contribuições **no mesmo ponto** antes de calcular a força de prova. O campo externo exclui o próprio campo singular da carga de prova.

Escolha direita positiva. Fontes+2nC em0 e−2nC em0,40m; observe P em0,20m:

| Contribuição em P | Módulo (N/C) | Sentido | Componente (N/C) |
|---|---:|---|---:|
| Fonte positiva da esquerda | 450 | Direita, para fora da fonte | +450 |
| Fonte negativa da direita | 450 | Direita, em direção à fonte | +450 |
| Campo resultante | 900 | Direita | +900 |

A carga total é zero; o campo no ponto não é. Trocando a fonte da direita por+2nC, as contribuições passam a+450 e−450N/C: campo nulo no ponto, carga total+4nC. Cada campo individual continua não nulo. Essas duas observações mostram por que não se troca soma de cargas por soma de campos.

No primeiro arranjo, q_t=−1nC sofre força−9×10⁻⁷N=−0,9μN: esquerda. Mudar o sinal da prova inverte sua força, sem inverter o campo das fontes. Uma prova de carga zero teria força elétrica zero, sem exigir E=0; não se calcula campo por uma divisão0/0.

Campo nulo em um ponto não significa ausência de outras forças nem estabilidade diante de deslocamentos. Linha de campo não é trajetória: o movimento depende ainda de massa, velocidade inicial e forças. As fontes estão mantidas em posições por hipótese; não se afirma que cargas livres ficariam paradas.

## Código opcional e verificações

Execute `python3 labs/cargas-campo-forca/charges.py`. Posições em metro, cargas em coulomb; campo em N/C e força em N. A componente assinada de uma fonte em uma reta é

`E_x(x)=k Q (x−x_Q)/|x−x_Q|³`.

Ela combina o módulo com o sentido da seta. x diferente de x_Q é obrigatório para fonte não nula. A fonte de carga zero é tratada como ausente. O programa aceita int/Fraction para tornar exatas as contas com os parâmetros arredondados; isso não elimina a aproximação física de k nem cria dados experimentais.

Seis testes: exemplos/unidades;225 configurações de pares conferem ação/reação, módulo e sentido;63 transformações conferem translação e escala de distância; superposição e escala de cargas; distinção entre campo nulo e força nula; contratos. A geometria é unidimensional; não se simula trajetória, campo de distribuições contínuas, potencial, meio material ou propagação do campo. Testes de identidades no programa não substituem evidência experimental das leis físicas.

## Fontes públicas consultadas

- [OpenStax College Physics2e, §18.3 Coulomb’s Law](https://openstax.org/books/college-physics-2e/pages/18-3-coulombs-law), consulta parcial em27/10/2026: força entre cargas puntiformes, módulos, unidade e sentido. O valor didático9×10⁹ é arredondamento adicional do valor apresentado na fonte.
- [OpenStax College Physics2e, §18.4 Electric Field](https://openstax.org/books/college-physics-2e/pages/18-4-electric-field-concept-of-a-field-revisited), consulta parcial em27/10/2026: definição vetorial, dependência da fonte, prova ideal e unidades.

Não são ementas do ensino médio brasileiro nem comprovação de material usado por Jhuann em uma turma. Exemplos, configuração de duas fontes, texto, figura, exercícios e código preparados para estas notas; não foram copiados figuras ou exercícios das fontes. Modelo e princípios são clássicos, sem alegação de descoberta original.

## Próxima revisão — vinte minutos

Sem código, desenhe em qual corpo atua cada força de um par. No mesmo P, desenhe e some as contribuições dos dois arranjos. Depois preveja a força de prova negativa e confira unidades. Explique por que carga total zero não determina campo zero. Registre dúvidas antes de avançar para potencial ou movimento de partículas. Revisão pessoal e uso com aluno pendentes.
