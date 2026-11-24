# Sólidos cúbicos — geometria e limites

Aula/laboratório originais com apoio de IA; revisão pessoal pendente. Entradas prescritas, sem medições. Células convencionais cúbicas SC, BCC, FCC monoatômicas; não modelam bandas ou identificam material real.

`basis` usa representantes meio abertos em [0,1)³; `closed_points` reconstrói fronteiras do cubo fechado. `weighted_count` soma2⁻ᵏ para k coordenadas fronteiriças. `nearest` enumera translações−1,0,1 e compara distâncias quadráticas exatas Fraction. `geometry` calcula raio de esferas em contato e φ. Esferas não são fronteiras físicas da nuvem eletrônica. Célula convencional FCC/BCC não é primitiva.

`density(kind, M, a_pm, occupancy)` usa M em g/mol e a em pm, retorna g/cm³. FaixasM[1e−3,1e4],a[1,1e5],ocupação[0,1]; bool/strings/NaN/Inf rejeitados. ConstanteNₐ6,02214076e23mol⁻¹ exata no SI, cálculo float. Ocupação é média prescrita sem relaxação; não há processo de criação de vacâncias. f=0 é só um limite matemático. Exemplo original FCC M60,a400, sem nome de elemento; não usa dados ou soluções do livro.

## Executar da raiz
```sh
python3 -B -m unittest discover -s labs/solidos-cubicos -t .
```
Seis métodos: categorias de fronteira; nove supercélulas independentes (SC/BCC/FCC×lados3,4,5) geradas por paridade em malha de meio passo e distância periódica; valores literais/ausência de sobreposição; densidade Decimal50 e12 réplicas; escalas/ocupação/comparações a ou r fixos; contratos. Sem imagem mínima ambígua para o primeiro vizinho nos tamanhos escolhidos. Razões fracionárias mantidas exatas até raízes/π/densidade em float.

Figura original de centros esquemáticos, sem raios em escala; cores distinguem posições, não espécies. Contagem efetiva1,2,4 é distinta de coordenação6,8,12. Empacotamento0,524/0,680/0,740 não prevê estabilidade, condutividade ou densidade de espécies com massas/raios distintos.

## Fontes e alcance real —29/10/2026
- JúpiterCCM0114, https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CCM0114 : programa reaberto, ativação15/07/2024, posterior à turma2023. Histórico aprovado preservado; programa ministrado não recuperado.
- Atkins/Jones/Laverman, Princípios de Química7ªed.Bookman2018, exemplar privado já localizado. Recortes textuais3H.1p201/PDF333;3H.4–3H.5pp207–209/PDF339–341;pp211–212/PDF343–344. p211/PDF343 inspecionada visualmente para diagonais e fórmula da densidade por falhas na extração. p202/PDF334 apareceu na extração, mas seu quadro de microscopia não é fonte desta aula. Sem leitura integral ou reprodução de exemplos/figuras. Edição diferente da3ªed.2006 citada no programa. PDF não distribuído.
- OpenStax Chemistry2e10.6, https://openstax.org/books/chemistry-2e/pages/10-6-lattice-structures-in-crystalline-solids : consulta parcial da seção inicial de estruturas/célulasSC/contagem/vizinhança; não se adotou a sugestão geral de que maximizar empacotamento basta para decidir estrutura. Exemplos e figuras não copiados.

Faltam HCP desenvolvido, estruturas iônicas e seus balanços, defeitos/relaxação, teoria eletrônica, estabilidade de fase e propriedades quantitativas reais. Matéria preparada não certifica experiência experimental ou domínio de Jhuann.
