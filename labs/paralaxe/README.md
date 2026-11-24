# Paralaxe: laboratório sintético

Execute `python3 experiment.py`. Na raiz do protótipo: `python3 -m unittest discover -p 'test_*.py'` inclui quatro testes deste laboratório. Não usa rede, bibliotecas adicionais ou catálogos.

`summary(p_mas, sigma_mas)` exige valores finitos, p>0 e σ≥0. Retorna distância central (pc), escala linear local (pc), razão σ/p e imagem da faixa positiva p±σ. Quando σ≥p, o limite superior é `None`: não há teto finito. Não é intervalo de confiança ou posterior sem hipóteses adicionais.

`geometric_distance_au(p_arcsec)` é o triângulo retângulo ideal com cateto de 1 au: cotangente do ângulo em radianos. Só admite ângulo entre zero e 90 graus. Não confundir a fórmula trigonométrica exata com a inversão convencional de pequeno ângulo em parsecs. A paralaxe de dados reais é parâmetro ajustado, não uma leitura isolada deste triângulo.

Verificações independentes: extremos racionais, escala por unidade, triângulos de 30°/45°, sensibilidade por diferença central, assimetria, toque/cruzamento de zero e rejeição de entradas fora do domínio desta rotina. A recusa de paralaxes negativas não é recomendação de excluir observações reais. `reference.json` contém 25 casos comparados ao JavaScript.

Fontes consultadas em 16/10/2026:

- [ESA: unidades e paralaxe](https://www.esa.int/Science_Exploration/Space_Science/Gaia/Cosmic_distances).
- [IAU 2015 B2](https://arxiv.org/abs/1510.06262): registro/resumo com definição exata do parsec.
- [Bailer-Jones et al. (2018)](https://arxiv.org/abs/1804.10121): resumo para limites de inversão. Método de inferência não implementado.

Texto, exercícios e exemplos originais com auxílio de IA, ainda sem revisão de Jhuann. Não reproduz exercícios de livros nem reivindica resultado científico pessoal.
