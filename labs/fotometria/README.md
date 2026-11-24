# Fotometria e módulo de distância

Execute `python3 experiment.py`. Os quatro testes entram em `python3 -m unittest discover -p 'test_*.py'`, a partir da raiz. `reference.json` contém 27 casos comparados ao JavaScript.

Modelo: mesma banda/sistema, magnitudes calibradas, M conhecido, geometria euclidiana local e tela efetiva A≥0. `photometry(m, absolute, extinction)` calcula módulo corrigido, distância em pc, inferência com A=0, fator de superestimação e transmissão. `apparent(M, d_pc, A)` resolve o sentido direto. Não estima M ou A a partir dos dados, nem contém catálogo ou inferência estatística.

Exemplo original: m=15, M=4, A=1 => módulo 10 mag, distância 1000 pc; ignorar A dá aproximadamente 1584,893 pc. Conferência independente usa fluxo relativo ao ponto zero, diluição por área e transmissão. Testes incluem 48 combinações de fluxo/geometria, potências de dez, sinal da extinção, degenerescência, derivada e domínio. Entradas devem estar em escala numericamente representável; não é uma biblioteca universal de magnitudes extremas.

A curva da demonstração varia a extinção assumida mantendo m e M fixos. Não é perfil de poeira com distância. Mesma magnitude pode admitir diferentes distâncias sob diferentes hipóteses. Fator de viés é condicional a M correto e ao modelo adotado.

Fontes consultadas em 16/10/2026:

- [WKU, Magnitudes and distance](https://astro.wku.edu/labs/m100/mags.html): leitura direta das relações de magnitudes, distância e extinção. Tabelas observacionais antigas não foram incorporadas.
- Sparke e Gallagher, Galaxies in the Universe, segunda edição, 2007: excerto local sobre extinção nas páginas impressas 33–34 (PDF 45–46). Obra identificada previamente no acervo; nenhuma cópia distribuída.

As notas de UNL, Wisconsin e Case Western apareceram nas buscas, mas a abertura direta falhou; não foram usadas como leitura integral. Texto, exemplos, exercícios e código originais preparados com IA, ainda sem revisão de Jhuann. Sem calibração de vela padrão, ajuste multibanda, posterior ou aplicação cosmológica.
