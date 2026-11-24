# Green: orientação, hipóteses e fronteiras — notas de aula

Rascunho original para revisão de Jhuann. Pré-requisitos: derivadas parciais, integral de linha e integral dupla. Campos matemáticos sem unidades físicas atribuídas. Apoia o recorte de integrais de linha/múltiplas de Matemática IV; não é evidência de domínio ou cobertura integral do curso.

Para uma região limitada D com borda externa simples, regular por trechos, e componentes P,Q de classe C¹ num aberto contendo a região fechada, Green relaciona circulação e integral de área:

`∮_∂D (P dx+Q dy) = ∬_D (Q_x−P_y) dA`.

A borda externa positiva é anti-horária. Se há um número finito de furos regulares com bordas disjuntas, suas bordas positivas são horárias: em todos os percursos, a região permanece à esquerda. As derivadas devem existir e ser contínuas em um entorno da região usada, não apenas nos pontos amostrados da fronteira.

## Demonstração no retângulo

Em [0,a]×[0,b], percorra inferior→direita→superior→esquerda, a,b>0. Nas bordas horizontais, a parcela de P é `∫_0^a[P(x,0)−P(x,b)]dx = −∫_0^a∫_0^b P_y dy dx`, pelo teorema fundamental. Nas verticais, a parcela de Q é `∫_0^b[Q(a,y)−Q(0,y)]dy = ∫_0^b∫_0^a Q_x dx dy`. Fubini permite somar as integrais sobre a mesma área. Isso prova o caso retangular. A extensão a regiões gerais e a construção rigorosa de decomposições não são provadas aqui. Cortes em uma coroa produzem bordas percorridas em sentidos opostos, que se cancelam ao somar as partes.

## Dois campos, duas conclusões

F=(−y,x) é regular no plano, rotacional2. Na curva γ(t)=(Rcos t,Rsen t), 0≤t≤2π, seu produto com γ′ é R², dando circulação2πR², também obtida por Green. Na coroa a≤r≤R, a soma é 2πR²−2πa². Para a=1,R=2, dá6π.

G=(−y/r²,x/r²) só existe para r>0. As derivadas Q_x=P_y=(y²−x²)/r⁴ dão rotacional zero fora da origem. Mas sobre γ o produto é1, dando2π para qualquer raio. Green não se aplica ao disco inteiro, pois G está indefinido na origem. Na coroa é aplicável: externa2π e interna−2π, total0. Cada componente pode ter integral não nula, mesmo com soma zero. G não é gradiente de potencial global de valor único no plano sem a origem; em um aberto simplesmente conexo e para campo C¹, o rotacional nulo é uma condição suficiente usual para conservatividade.

## Fluxo é outra integral

Na curva positiva, normal externa vezes ds é (dy,−dx). O fluxo externo é `∮(P dy−Q dx)=∬(P_x+Q_y)dA`, aplicando Green ao campo(−Q,P). No círculo, F é tangente: circulação2πR² e fluxo0. O campo radial(x,y) tem circulação0 e fluxo2πR². Inverter a orientação da curva sem ajustar a normal troca o sinal da expressão; o código só admite orientação positiva para o fluxo externo.

## Código e limites

Execute `python3 labs/green-fronteiras/green.py`. Cinco testes: 216 comparações racionais de integrais de linha em retângulos traduzidos e orientados com antiderivadas da integral de área; círculos com três campos, três raios, duas orientações e duas malhas; coroas com dois campos e três pares de raios; fluxo versus circulação; contratos. Nas arestas dos campos polinomiais escolhidos, Simpson é exato porque o integrando tem grau no máximo2. Não é integração exata de qualquer campo.

Nas circunferências, o código avalia o campo e a tangente por pontos médios em float, comparando com valores deduzidos analiticamente, com tolerância1e−10. Os exemplos têm integrandos constantes ou nulos e não fornecem uma estimativa geral de erro de quadratura. Malhas não certificam regularidade, não identificam todas as singularidades e não provam Green. A rejeição explícita de G(0,0) conhece este campo; não é detector genérico. O painel existente na aula continua mostrando kF no círculo, com escala ajustável k,, sem representar a coroa ou G.

## Fontes consultadas

- [USP — CCM0223 Matemática IV](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0223), reaberto em27/10/2026; ativação01/01/2025. O programa inclui integrais de linha/múltiplas/superfície e introduções à análise complexa/probabilidade. Não comprova a versão efetivamente ministrada.
- Apostol, *Cálculo*, volume2, tradução Reverté1996, reimpressão2004, original indicado como segunda edição: §11.19 pp.425–428/PDF438–441 e §11.23 pp.435–436/PDF448–449, consulta textual parcial em27/10/2026 no exemplar privado autorizado. Enunciado/hipóteses, provas para regiões particulares e fronteiras múltiplas. Extração contém ruído tipográfico; sem nova inspeção visual, leitura integral ou distribuição do exemplar. Paginação não transferida à edição inglesa oficial.
- [OpenStax — Calculus Volume3, §6.4](https://openstax.org/books/calculus-volume-3/pages/6-4-greens-theorem), consulta parcial em27/10/2026: formas de circulação/fluxo e prova retangular, apoio público complementar. Exposição e exercícios destas notas preparados originalmente; não foram copiados exercícios ou diagramas.

## Próxima revisão — vinte minutos

Reconstrua os quatro lados do retângulo. Depois desenhe a coroa e suas orientações e calcule a soma para F e para G. Explique por que rotacional zero na parte regular não autoriza preencher o furo. Contagens e testes não equivalem a cobertura integral, estudo realizado ou domínio de Jhuann.
